from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class WelcomeNewUserTemplate(BaseEmailTemplate):
    template_name = "welcome_new_user"
    language = "pt-br"
    subject_template = "Bem-vindo à {organization_name}!"
    text_template = (
        "Olá {user_name},\n\n"
        "Seja bem-vindo(a) à {organization_name}!\n\n"
        "Sua conta foi criada com sucesso em nossa plataforma. "
        "Para acessar, utilize as seguintes credenciais:\n\n"
        "E-mail: {user_email}\n"
        "Senha provisória: {temp_password}\n\n"
        "Por segurança, você será solicitado(a) a criar uma nova senha no primeiro acesso.\n\n"
        "Acesse a plataforma: {platform_url}\n\n"
        "Estamos felizes em tê-lo(a) conosco!\n\n"
        "Equipe {organization_name}"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Bem-vindo(a) à {organization_name}!</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Sua conta foi criada com sucesso na plataforma <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>. "
        "Para acessar, utilize as seguintes credenciais:</p>"
        "<div style='background-color: #f9f9f9; padding: 20px; border-radius: 8px; margin: 20px 0;'>"
        "<p style='margin: 10px 0;'><strong>E-mail:</strong> {user_email}</p>"
        "<p style='margin: 10px 0;'><strong>Senha provisória:</strong></p>"
        "<p style='font-size:1.3em; font-weight:bold; letter-spacing:2px; "
        "background:#ffffff; padding:12px 20px; display:inline-block; "
        "border-radius:6px; border: 2px solid #3A71D9; color: #333;'>"
        "{temp_password}</p>"
        "</div>"
        "<p style='color: #666;'><em>Por segurança, você será solicitado(a) a criar "
        "uma nova senha no primeiro acesso.</em></p>"
        "<p style='margin-top: 30px; text-align: center;'>"
        "<a href='{platform_url}' style='background-color: #3A71D9; color: white; "
        "padding: 14px 32px; text-decoration: none; border-radius: 6px; "
        "display: inline-block; font-weight: bold; font-size: 16px;'>Acessar a Plataforma</a>"
        "</p>"
        "<p style='margin-top: 30px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Estamos felizes em tê-lo(a) conosco!<br>"
        "Equipe {organization_name} | <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
