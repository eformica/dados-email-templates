from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class ResetPasswordTemplate(BaseEmailTemplate):
    template_name = "reset_password"
    language = "pt-br"
    subject_template = "Redefinição de senha - Perfecting"
    text_template = (
        "Olá {user_name},\n\n"
        "Recebemos uma solicitação para redefinir sua senha.\n\n"
        "Para criar uma nova senha, acesse o link abaixo:\n"
        "{reset_link}\n\n"
        "Este link expira em {expiration_hours} horas.\n\n"
        "Se você não solicitou esta redefinição, ignore esta mensagem e sua senha permanecerá inalterada.\n\n"
        "Equipe Perfecting"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Redefinição de Senha</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Recebemos uma solicitação para redefinir sua senha na plataforma <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>.</p>"
        "<p>Para criar uma nova senha, clique no botão abaixo:</p>"
        "<p style='margin: 30px 0; text-align: center;'>"
        "<a href='{reset_link}' style='background-color: #3A71D9; color: white; "
        "padding: 14px 32px; text-decoration: none; border-radius: 6px; "
        "display: inline-block; font-weight: bold; font-size: 16px;'>Redefinir Senha</a>"
        "</p>"
        "<p style='color: #666; font-size: 14px;'><strong>⚠️ Este link expira em {expiration_hours} horas.</strong></p>"
        "<p style='color: #666; font-size: 14px;'><em>Se você não solicitou esta redefinição, ignore esta mensagem e sua senha permanecerá inalterada.</em></p>"
        "<p style='margin-top: 40px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
