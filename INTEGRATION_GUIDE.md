# Guia de Implantação — Módulo de E-mail

Guia prático para copiar e integrar o módulo de e-mail em outros projetos Python.

---

## 1. Estrutura de arquivos a copiar

Copie o diretório `core/email/` inteiro para o projeto destino:

```
seu-projeto/
└── src/
    └── core/
        └── services/
            └── email/
                ├── __init__.py
                ├── _base_email.py       ← motor de templates e registry
                ├── _email_config.py     ← lê DEFAULT_LANGUAGE do GetEnv
                ├── send_email.py        ← função principal de envio
                └── templates/
                    └── pt_br/
                        ├── __init__.py
                        ├── confirm_email_signup.py
                        ├── invite_activation.py
                        ├── reset_password.py
                        ├── temp_password_additional_user.py
                        ├── temp_password_reset.py
                        ├── welcome_after_activation.py
                        └── welcome_new_user.py
```

> **Nota:** O caminho de destino precisa bater com o `module_path` usado em `_base_email.py`.
> O padrão é `src.core.services.email.templates.{lang}.{template_name}`.
> Se o seu projeto usar outro caminho, ajuste a constante em `_base_email.py` (ver seção 5).

---

## 2. Dependência

Instale a única dependência externa:

```bash
pip install python-dotenv
```

Ou adicione ao `requirements.txt` do projeto:

```
python-dotenv>=1.0.0
```

---

## 3. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (ou configure no ambiente de produção):

```dotenv
# ── SMTP ──────────────────────────────────────────────
SMTP_HOST=smtp.gmail.com          # servidor SMTP
SMTP_PORT=587                     # porta (587 = TLS, 465 = SSL, 25 = sem criptografia)
SMTP_USER=seu@email.com           # usuário de autenticação
SMTP_PASSWORD=sua-senha-app       # senha ou App Password
SMTP_USE_TLS=true                 # true habilita STARTTLS
SMTP_FROM=seu@email.com           # endereço do remetente (padrão: SMTP_USER)
SMTP_FROM_NAME=Suporte MeuProjeto # nome exibido no remetente

# ── APP ───────────────────────────────────────────────
ENVIRONMENT=DEV                   # DEV | PROD
APP_DOMAIN=https://meuapp.com.br  # URL base da aplicação
```

### Provedores comuns

| Provedor | SMTP_HOST | SMTP_PORT | Observação |
|---|---|---|---|
| Gmail | `smtp.gmail.com` | `587` | Usar App Password com 2FA |
| Outlook/Hotmail | `smtp.office365.com` | `587` | — |
| Amazon SES | `email-smtp.<região>.amazonaws.com` | `587` | Chaves IAM como user/pass |
| SendGrid | `smtp.sendgrid.net` | `587` | Usar `apikey` como SMTP_USER |
| Mailgun | `smtp.mailgun.org` | `587` | — |

---

## 4. Integração com GetEnv

O módulo lê as configurações SMTP através de `GetEnv.Email`. Garanta que sua classe
`GetEnv` (ou equivalente) exponha as seguintes propriedades:

```python
class GetEnv:
    class Email:
        SMTP_HOST      = os.getenv("SMTP_HOST")
        SMTP_PORT      = int(os.getenv("SMTP_PORT", "587"))
        SMTP_USER      = os.getenv("SMTP_USER")
        SMTP_PASSWORD  = os.getenv("SMTP_PASSWORD")
        SMTP_USE_TLS   = os.getenv("SMTP_USE_TLS", "true").lower() in {"1", "true", "yes"}
        SMTP_FROM      = os.getenv("SMTP_FROM") or os.getenv("SMTP_USER")
        SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "Suporte")
        DEFAULT_LANGUAGE = "pt-br"
```

---

## 5. Ajustar os caminhos de importação (se necessário)

Se a estrutura do seu projeto for diferente de `src.core.services.email`, você precisa
atualizar **dois** lugares:

### 5.1 `_base_email.py` — caminho de descoberta automática de templates

```python
# Linha ~70 — ajuste o prefixo do module_path
module_path = f"src.core.services.email.templates.{lang_module}.{template_name}"
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^ altere para o seu caminho
```

```python
# Linha ~86 — mesma mudança para o fallback de idioma
default_path = (
    f"src.core.services.email.templates."
    f"{default_lang_module}.{template_name}"
)
```

### 5.2 Cada arquivo de template — importação da classe base

```python
# Antes (caminho antigo)
from src.core.services.email._base_email import BaseEmailTemplate

# Depois (exemplo com caminho diferente)
from app.email._base_email import BaseEmailTemplate
```

### 5.3 `send_email.py` — importações internas

```python
# Ajuste os imports relativos ou absolutos conforme o seu projeto
from src.core.services.email._base_email import BaseEmailTemplate
from src.core.services.email._email_config import DEFAULT_LANGUAGE
from config.getenv import GetEnv
```

---

## 6. Uso básico

### 6.1 Envio via função `send_email`

```python
from src.core.services.email.send_email import send_email

send_email(
    to_emails="usuario@exemplo.com",
    template_name="confirm_email_signup",
    template_context={
        "user_name": "João Silva",
        "confirmation_link": "https://meuapp.com/activate?token=abc123",
    },
)
```

### 6.2 Envio via método `.send()` na classe do template

```python
from src.core.services.email.templates.pt_br.confirm_email_signup import (
    ConfirmEmailSignupTemplate,
)

ConfirmEmailSignupTemplate.send(
    to_emails="usuario@exemplo.com",
    context={
        "user_name": "João Silva",
        "confirmation_link": "https://meuapp.com/activate?token=abc123",
    },
)
```

### 6.3 Múltiplos destinatários e CC

```python
send_email(
    to_emails=["a@exemplo.com", "b@exemplo.com"],
    template_name="welcome_new_user",
    template_context={
        "user_name": "Maria",
        "user_email": "a@exemplo.com",
        "temp_password": "Temp@123",
        "organization_name": "Minha Empresa",
        "platform_url": "https://meuapp.com",
    },
    cc_emails=["gestor@empresa.com"],
    reply_to="suporte@empresa.com",
)
```

---

## 7. Criar um novo template

1. Crie o arquivo em `templates/pt_br/meu_template.py`:

```python
from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class MeuTemplate(BaseEmailTemplate):
    template_name = "meu_template"      # deve bater com o nome do arquivo
    language = "pt-br"
    subject_template = "Assunto do e-mail - Meu Projeto"
    text_template = (
        "Olá {user_name},\n\n"
        "Mensagem em texto puro.\n\n"
        "Equipe Meu Projeto"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Mensagem em HTML.</p>"
        "</div>"
    )
```

2. Use normalmente:

```python
send_email(
    to_emails="usuario@exemplo.com",
    template_name="meu_template",
    template_context={"user_name": "João"},
)
```

> O sistema descobre o arquivo automaticamente por `importlib` — não é necessário
> nenhum registro manual além do decorator `@BaseEmailTemplate.register`.

---

## 8. Templates disponíveis e variáveis obrigatórias

| Template | Variáveis obrigatórias |
|---|---|
| `confirm_email_signup` | `user_name`, `confirmation_link` |
| `invite_activation` | `user_name`, `organization_name`, `activation_link` |
| `reset_password` | `user_name`, `reset_link`, `expiration_hours` |
| `temp_password_additional_user` | `user_name`, `organization_name`, `temp_password`, `platform_url` |
| `temp_password_reset` | `user_name`, `temp_password` |
| `welcome_after_activation` | `user_name`, `user_email`, `platform_url` |
| `welcome_new_user` | `user_name`, `user_email`, `temp_password`, `organization_name`, `platform_url` |

> Se uma variável obrigatória estiver ausente ou vazia, um `ValueError` é levantado
> antes de qualquer envio.

---

## 9. Suporte a múltiplos idiomas

Para adicionar um novo idioma (ex.: inglês):

1. Crie o diretório `templates/en_us/` com um `__init__.py` vazio.
2. Crie os arquivos de template com `language = "en-us"`.
3. Chame `send_email(..., language="en-us")`.

O sistema faz **fallback automático** para `pt-br` (DEFAULT_LANGUAGE) se o template
não existir no idioma solicitado, emitindo um `WARNING` no log.

---

## 10. Diagnóstico rápido

| Erro | Causa provável | Solução |
|---|---|---|
| `ValueError: SMTP_HOST não definido` | Variável de ambiente ausente | Verificar `.env` e `load_dotenv()` |
| `KeyError: Template 'x' não encontrado` | Arquivo do template não existe | Verificar nome e caminho do arquivo |
| `ValueError: Variáveis obrigatórias ausentes` | `template_context` incompleto | Passar todas as variáveis listadas na seção 8 |
| `SMTPAuthenticationError` | Credenciais inválidas | Usar App Password (Gmail) ou verificar SMTP_USER/PASSWORD |
| `ModuleNotFoundError` no import | Caminhos de importação incorretos | Ajustar conforme seção 5 |
