from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class TempPasswordResetTemplate(BaseEmailTemplate):
    template_name = "temp_password_reset"
    language = "pt-br"
    subject_template = "Sua nova senha de acesso - Perfecting"
    text_template = (
        "Olá {user_name},\n\n"
        "Recebemos uma solicitação de redefinição de senha para sua conta.\n\n"
        "Sua senha provisória de acesso é:\n\n"
        "    {temp_password}\n\n"
        "Por segurança, você será solicitado a criar uma nova senha no próximo acesso.\n\n"
        "Se você não solicitou esta alteração, entre em contato com o suporte.\n\n"
        "Equipe Perfecting"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Nova Senha de Acesso</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Recebemos uma solicitação de redefinição de senha para sua conta na <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>.</p>"
        "<p>Sua senha provisória de acesso é:</p>"
        "<div style='background-color: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;'>"
        "<p style='font-size:1.3em; font-weight:bold; letter-spacing:2px; "
        "background:#ffffff; padding:12px 20px; display:inline-block; "
        "border-radius:6px; border: 2px solid #3A71D9; color: #333; margin: 0;'>"
        "{temp_password}</p>"
        "</div>"
        "<p style='color: #666;'><em>Por segurança, você será solicitado a criar uma nova senha no próximo acesso.</em></p>"
        "<p style='color: #666; font-size: 14px;'><em>Se você não solicitou esta alteração, entre em contato com o suporte imediatamente.</em></p>"
        "<p style='margin-top: 40px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
