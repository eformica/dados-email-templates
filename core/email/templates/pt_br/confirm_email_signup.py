from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class ConfirmEmailSignupTemplate(BaseEmailTemplate):
    template_name = "confirm_email_signup"
    language = "pt-br"
    subject_template = "Confirme seu e-mail - Perfecting"
    text_template = (
        "Olá {user_name},\n\n"
        "Bem-vindo(a) à Perfecting!\n\n"
        "Para confirmar seu e-mail e ativar sua conta, acesse o link abaixo:\n"
        "{confirmation_link}\n\n"
        "Se você não solicitou este cadastro, ignore esta mensagem.\n\n"
        "Equipe Perfecting"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Bem-vindo(a) à <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>!</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Para confirmar seu e-mail e ativar sua conta, clique no botão abaixo:</p>"
        "<p style='margin: 30px 0; text-align: center;'>"
        "<a href='{confirmation_link}' style='background-color: #3A71D9; color: white; "
        "padding: 14px 32px; text-decoration: none; border-radius: 6px; "
        "display: inline-block; font-weight: bold; font-size: 16px;'>Confirmar E-mail</a>"
        "</p>"
        "<p style='color: #666; font-size: 14px;'><em>Se você não solicitou este cadastro, ignore esta mensagem.</em></p>"
        "<p style='margin-top: 40px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
