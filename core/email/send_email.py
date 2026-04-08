import sys, pathlib
sys.path.append(str(pathlib.Path(__file__)).split("src")[0])

import logging
import smtplib
from email.message import EmailMessage
from typing import Optional, Sequence, Mapping

from src.core.services.email._base_email import BaseEmailTemplate
from src.core.services.email._email_config import DEFAULT_LANGUAGE
from config.getenv import GetEnv

logger = logging.getLogger(__name__)


def send_email(
	to_emails: Sequence[str] | str,
	template_name: str,
	template_context: Optional[Mapping[str, object]] = None,
	language: str = DEFAULT_LANGUAGE,
	subject: Optional[str] = None,
	reply_to: Optional[str] = None,
	cc_emails: Optional[Sequence[str]] = None,
	bcc_emails: Optional[Sequence[str]] = None,
	subtype: str = "plain",
) -> None:
	"""
	Envia e-mail via SMTP.

	O template é carregado automaticamente pelo nome do arquivo e pelo idioma.
	As configurações SMTP são sempre lidas de GetEnv.Email.

	Parâmetros:
	    to_emails        – destinatário(s).
	    template_name    – nome do arquivo do template (sem extensão).
	                       O arquivo deve estar em templates/{lang}/{template_name}.py.
	    template_context – dicionário com as variáveis do template.
	                       Todos os campos exigidos pelo template devem estar
	                       preenchidos; caso contrário, um ValueError é levantado.
	    language         – código do idioma (padrão: DEFAULT_LANGUAGE).
	                       Fallback automático para DEFAULT_LANGUAGE se o template
	                       não existir no idioma solicitado.
	    subject          – assunto (sobrescreve o definido no template).
	    reply_to         – endereço de Reply-To.
	    cc_emails        – lista de destinatários em cópia.
	    bcc_emails       – lista de destinatários em cópia oculta.
	    subtype          – subtipo do corpo texto ("plain" ou "html").
	"""
	if isinstance(to_emails, str):
		to_emails = [to_emails]

	smtp_host     = GetEnv.Email.SMTP_HOST
	smtp_port     = GetEnv.Email.SMTP_PORT
	smtp_user     = GetEnv.Email.SMTP_USER
	smtp_password = GetEnv.Email.SMTP_PASSWORD
	use_tls       = GetEnv.Email.SMTP_USE_TLS
	from_email    = GetEnv.Email.SMTP_FROM
	from_name     = GetEnv.Email.SMTP_FROM_NAME

	if not smtp_host:
		raise ValueError("SMTP_HOST não definido em GetEnv.Email.")
	if not from_email:
		raise ValueError("SMTP_FROM/SMTP_USER não definido em GetEnv.Email.")

	# Carrega o template (com fallback automático de idioma)
	template_cls = BaseEmailTemplate.load(template_name, language)

	# Valida se todos os parâmetros exigidos pelo template foram fornecidos
	template_cls._validate_context(template_context)

	subject  = subject or template_cls.render_subject(template_context)
	body     = template_cls.render_text(template_context)
	html_body = template_cls.render_html(template_context)

	if not subject:
		raise ValueError("Assunto do e-mail não definido.")

	# Formata o campo From com nome do remetente
	if from_name:
		from_header = f"{from_name} <{from_email}>"
	else:
		from_header = from_email

	msg = EmailMessage()
	msg["Subject"] = subject
	msg["From"]    = from_header
	msg["To"]      = ", ".join(to_emails)
	if cc_emails:
		msg["Cc"] = ", ".join(cc_emails)
	if reply_to:
		msg["Reply-To"] = reply_to

	if body:
		msg.set_content(body, subtype=subtype)
	else:
		msg.set_content(" ", subtype="plain")

	if html_body:
		msg.add_alternative(html_body, subtype="html")

	all_recipients = list(to_emails)
	if cc_emails:
		all_recipients.extend(cc_emails)
	if bcc_emails:
		all_recipients.extend(bcc_emails)

	logger.info("Sending email to %s via %s:%s", all_recipients, smtp_host, smtp_port)

	with smtplib.SMTP(smtp_host, smtp_port) as server:
		server.ehlo()
		if use_tls:
			server.starttls()
			server.ehlo()
		if smtp_user and smtp_password:
			server.login(smtp_user, smtp_password)
		server.send_message(msg, from_addr=from_email, to_addrs=all_recipients)


if __name__ == "__main__":
	"""
	Demonstração de envio de e-mails para todos os templates disponíveis.
	Execute: python -m src.core.services.email.send_email
	
	NOTA: Este script requer credenciais SMTP válidas configuradas nas variáveis de ambiente:
	- SMTP_HOST
	- SMTP_PORT
	- SMTP_USER
	- SMTP_PASSWORD
	- SMTP_FROM
	
	Se você receber erro 535 (authentication failed), verifique suas credenciais SMTP.
	"""
	import sys
	import pathlib
	sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent))
	
	from config.getenv import GetEnv
	
	destination_email = "eformica@gmail.com"
	
	print("=" * 80)
	print("DEMONSTRAÇÃO DE ENVIO DE E-MAILS")
	print("=" * 80)
	print(f"Destinatário: {destination_email}")
	print(f"SMTP: {GetEnv.Email.SMTP_HOST}:{GetEnv.Email.SMTP_PORT}")
	print(f"From: {GetEnv.Email.SMTP_FROM_NAME} <{GetEnv.Email.SMTP_FROM}>")
	print(f"User: {GetEnv.Email.SMTP_USER}")
	print("=" * 80)
	print()
	
	# Verificar se as credenciais SMTP estão configuradas
	if not GetEnv.Email.SMTP_PASSWORD:
		print("⚠️  AVISO: SMTP_PASSWORD não está configurado!")
		print("   Configure as variáveis de ambiente SMTP antes de executar este script.\n")
	
	success_count = 0
	fail_count = 0
	
	# 1. E-mail de confirmação de cadastro
	print("📧 1. Enviando e-mail de confirmação de cadastro...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="confirm_email_signup",
			template_context={
				"user_name": "Eduardo Formica",
				"confirmation_link": f"{GetEnv.Routes.ACCOUNT_ACTIVATION_PAGE_SIGNUP}?token=demo-token-123456"
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	# 2. E-mail de boas-vindas após ativação
	print("📧 2. Enviando e-mail de boas-vindas após ativação...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="welcome_after_activation",
			template_context={
				"user_name": "Eduardo Formica",
				"user_email": destination_email,
				"platform_url": GetEnv.Routes.PLATFORM_URL
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	# 3. E-mail de boas-vindas com senha provisória (novo usuário)
	print("📧 3. Enviando e-mail de boas-vindas com senha provisória...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="welcome_new_user",
			template_context={
				"user_name": "Eduardo Formica",
				"user_email": destination_email,
				"temp_password": "SenhaDemo@123",
				"organization_name": "Perfecting Demo",
				"platform_url": GetEnv.Routes.PLATFORM_URL
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	# 4. E-mail de redefinição de senha
	print("📧 4. Enviando e-mail de redefinição de senha...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="reset_password",
			template_context={
				"user_name": "Eduardo Formica",
				"reset_link": f"{GetEnv.Routes.PLATFORM_URL}/reset-password?token=demo-reset-token-789",
				"expiration_hours": GetEnv.Security.ACTIVATION_TOKEN_EXPIRES_HOURS
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	# 5. E-mail de senha temporária (adicional)
	print("📧 5. Enviando e-mail de senha temporária (usuário adicional)...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="temp_password_additional_user",
			template_context={
				"user_name": "Eduardo Formica",
				"user_email": destination_email,
				"temp_password": "TempPass@456",
				"organization_name": "Perfecting Demo",
				"platform_url": GetEnv.Routes.PLATFORM_URL
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	# 6. E-mail de reset de senha temporária
	print("📧 6. Enviando e-mail de reset de senha temporária...")
	try:
		send_email(
			to_emails=destination_email,
			template_name="temp_password_reset",
			template_context={
				"user_name": "Eduardo Formica",
				"user_email": destination_email,
				"temp_password": "ResetTemp@789"
			}
		)
		print("   ✅ E-mail enviado com sucesso!\n")
		success_count += 1
	except Exception as e:
		print(f"   ❌ Erro ao enviar: {e}\n")
		fail_count += 1
	
	print("=" * 80)
	print("DEMONSTRAÇÃO CONCLUÍDA")
	print("=" * 80)
	print(f"\n📊 Resultados:")
	print(f"   ✅ Enviados com sucesso: {success_count}")
	print(f"   ❌ Falhas: {fail_count}")
	print()
	
	if fail_count > 0:
		print("💡 Dica: Se todos falharam com erro 535 (authentication failed),")
		print("   verifique as credenciais SMTP nas variáveis de ambiente:")
		print("   - SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD")
		print()
