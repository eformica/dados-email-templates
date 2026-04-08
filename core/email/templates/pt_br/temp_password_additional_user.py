from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class TempPasswordAdditionalUserTemplate(BaseEmailTemplate):
    template_name = "temp_password_additional_user"
    language = "pt-br"
    subject_template = "Seu acesso à plataforma Perfecting foi criado"
    text_template = (
        "Olá {user_name},\n\n"
        "Você foi adicionado à plataforma Perfecting pela organização {organization_name}.\n\n"
        "Sua senha provisória de acesso é:\n\n"
        "    {temp_password}\n\n"
        "Por segurança, você será solicitado a criar uma nova senha no primeiro acesso.\n\n"
        "Acesse a plataforma em: {platform_url}\n\n"
        "Se você não esperava receber este e-mail, entre em contato com o suporte.\n\n"
        "Equipe Perfecting"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Bem-vindo(a) à <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>!</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Você foi adicionado à plataforma <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span> pela organização <strong>{organization_name}</strong>.</p>"
        "<p>Sua senha provisória de acesso é:</p>"
        "<div style='background-color: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;'>"
        "<p style='font-size:1.3em; font-weight:bold; letter-spacing:2px; "
        "background:#ffffff; padding:12px 20px; display:inline-block; "
        "border-radius:6px; border: 2px solid #3A71D9; color: #333; margin: 0;'>"
        "{temp_password}</p>"
        "</div>"
        "<p style='color: #666;'><em>Por segurança, você será solicitado a criar uma nova senha no primeiro acesso.</em></p>"
        "<p style='margin-top: 30px; text-align: center;'>"
        "<a href='{platform_url}' style='background-color: #3A71D9; color: white; "
        "padding: 14px 32px; text-decoration: none; border-radius: 6px; "
        "display: inline-block; font-weight: bold; font-size: 16px;'>Acessar a Plataforma</a>"
        "</p>"
        "<p style='color: #666; font-size: 14px;'><em>Se você não esperava receber este e-mail, entre em contato com o suporte.</em></p>"
        "<p style='margin-top: 40px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
