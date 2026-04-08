from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class ConfirmEmailSignupTemplate(BaseEmailTemplate):
    template_key = "confirm_email_signup"
    subject_template = "Confirme seu e-mail"
    text_template = (
        "Olá {user_name},\n\n"
        "Para confirmar seu e-mail, acesse o link abaixo:\n"
        "{confirmation_link}\n\n"
        "Se você não solicitou este cadastro, ignore esta mensagem."
    )
    html_template = (
        "<p>Olá {user_name},</p>"
        "<p>Para confirmar seu e-mail, acesse o link abaixo:</p>"
        "<p><a href='{confirmation_link}'>Confirmar e-mail</a></p>"
        "<p>Se você não solicitou este cadastro, ignore esta mensagem.</p>"
    )
