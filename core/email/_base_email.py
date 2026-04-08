from __future__ import annotations

import logging
from abc import ABC
from importlib import import_module
from string import Formatter
from typing import Dict, Optional, Type, Mapping, Iterable, Set

_logger = logging.getLogger(__name__)


class BaseEmailTemplate(ABC):
    """
    Classe abstrata base para templates de e-mail.

    Cada template concreto deve definir:
    - template_name : nome do arquivo do template (sem extensão)
    - language      : código do idioma (ex.: "pt-br")
    - subject_template : assunto do e-mail
    - text_template    : corpo em texto plano
    - html_template    : corpo HTML (opcional)

    Os templates devem estar organizados em subdiretórios por idioma dentro de
    ``src/core/services/email/templates/{lang}/``, onde ``lang`` usa underscore
    (ex.: ``pt_br`` para o idioma ``pt-br``).
    """

    template_name: str
    language: str
    subject_template: str
    text_template: str
    html_template: Optional[str] = None

    _registry: Dict[str, Type["BaseEmailTemplate"]] = {}

    @classmethod
    def register(cls, template_cls: Type["BaseEmailTemplate"]) -> Type["BaseEmailTemplate"]:
        """
        Decorator de registro.  Constrói automaticamente o template_key como
        ``"{template_name}:{language}"``.
        """
        name = getattr(template_cls, "template_name", None)
        lang = getattr(template_cls, "language", None)
        if not name or not lang:
            raise ValueError(
                f"template_name e language são obrigatórios em {template_cls.__name__}."
            )
        key = f"{name}:{lang}"
        template_cls.template_key = key          # mantido para compatibilidade
        cls._registry[key] = template_cls
        return template_cls

    @classmethod
    def load(cls, template_name: str, language: str) -> Type["BaseEmailTemplate"]:
        """
        Carrega e retorna o template para o idioma solicitado.

        1. Verifica o registry.  Se já registrado, retorna diretamente.
        2. Tenta importar ``templates.{lang_module}.{template_name}``.
        3. Se não encontrado, tenta o DEFAULT_LANGUAGE (fallback) e emite warning.
        4. Se nenhum dos dois existir, levanta KeyError.
        """
        from src.core.services.email._email_config import DEFAULT_LANGUAGE

        key = f"{template_name}:{language}"

        if key not in cls._registry:
            lang_module = language.replace("-", "_")
            module_path = f"src.core.services.email.templates.{lang_module}.{template_name}"
            try:
                import_module(module_path)
            except ModuleNotFoundError:
                pass

        if key not in cls._registry:
            if language == DEFAULT_LANGUAGE:
                raise KeyError(
                    f"Template '{template_name}' não encontrado no idioma '{language}'."
                )

            # Fallback para idioma padrão
            default_key = f"{template_name}:{DEFAULT_LANGUAGE}"
            if default_key not in cls._registry:
                default_lang_module = DEFAULT_LANGUAGE.replace("-", "_")
                default_path = (
                    f"src.core.services.email.templates."
                    f"{default_lang_module}.{template_name}"
                )
                try:
                    import_module(default_path)
                except ModuleNotFoundError:
                    raise KeyError(
                        f"Template '{template_name}' não encontrado no idioma "
                        f"'{language}' nem no idioma padrão '{DEFAULT_LANGUAGE}'."
                    )

            if default_key not in cls._registry:
                raise KeyError(
                    f"Template '{template_name}' não encontrado no idioma "
                    f"'{language}' nem no idioma padrão '{DEFAULT_LANGUAGE}'."
                )

            _logger.warning(
                "Template '%s' não disponível no idioma '%s'. "
                "Usando idioma padrão '%s'.",
                template_name, language, DEFAULT_LANGUAGE,
            )
            return cls._registry[default_key]

        return cls._registry[key]

    @classmethod
    def get(cls, template_key: str) -> Type["BaseEmailTemplate"]:
        """Busca pelo template_key completo (compatibilidade legada)."""
        if template_key not in cls._registry:
            raise KeyError(f"Template '{template_key}' não registrado.")
        return cls._registry[template_key]

    @classmethod
    def render_subject(cls, context: Optional[Mapping[str, object]] = None) -> str:
        return cls.subject_template.format_map(_SafeFormatDict(context or {}))

    @classmethod
    def render_text(cls, context: Optional[Mapping[str, object]] = None) -> str:
        return cls.text_template.format_map(_SafeFormatDict(context or {}))

    @classmethod
    def render_html(cls, context: Optional[Mapping[str, object]] = None) -> Optional[str]:
        if not cls.html_template:
            return None
        return cls.html_template.format_map(_SafeFormatDict(context or {}))

    @classmethod
    def _extract_fields(cls, template: str) -> Set[str]:
        formatter = Formatter()
        fields: Set[str] = set()
        for _, field_name, _, _ in formatter.parse(template):
            if field_name:
                fields.add(field_name)
        return fields

    @classmethod
    def _required_fields(cls) -> Set[str]:
        fields = set()
        fields.update(cls._extract_fields(cls.subject_template))
        fields.update(cls._extract_fields(cls.text_template))
        if cls.html_template:
            fields.update(cls._extract_fields(cls.html_template))
        return fields

    @classmethod
    def _validate_context(cls, context: Optional[Mapping[str, object]] = None) -> None:
        context = context or {}
        missing = []
        for key in cls._required_fields():
            if key not in context:
                missing.append(key)
                continue
            value = context.get(key)
            if value is None or (isinstance(value, str) and value.strip() == ""):
                missing.append(key)
        if missing:
            missing_list = ", ".join(sorted(set(missing)))
            raise ValueError(f"Variáveis obrigatórias ausentes no template: {missing_list}.")

    @classmethod
    def send(
        cls,
        to_emails: Iterable[str] | str,
        context: Optional[Mapping[str, object]] = None,
        **kwargs,
    ) -> None:
        """
        Envia o e-mail usando este template.
        Parâmetros extras aceitos: reply_to, cc_emails, bcc_emails, subtype, subject.
        """
        from src.core.services.email.send_email import send_email

        send_email(
            to_emails=to_emails,
            template_name=cls.template_name,
            template_context=context or {},
            language=cls.language,
            **kwargs,
        )


class _SafeFormatDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"
