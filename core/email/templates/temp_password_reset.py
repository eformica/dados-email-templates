from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class TempPasswordResetTemplate(BaseEmailTemplate):
    template_key = "temp_password_reset"
    subject_template = "Sua nova senha de acesso"
    text_template = (
        "Olá {user_name},\n\n"
        "Recebemos uma solicitação de redefinição de senha para sua conta.\n\n"
        "Sua senha provisória de acesso é:\n\n"
        "    {temp_password}\n\n"
        "Por segurança, você será solicitado a criar uma nova senha no próximo acesso.\n\n"
        "Se você não solicitou esta alteração, entre em contato com o suporte."
    )
    html_template = (
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Recebemos uma solicitação de redefinição de senha para sua conta.</p>"
        "<p>Sua senha provisória de acesso é:</p>"
        "<p style='font-size:1.2em; font-weight:bold; letter-spacing:2px;"
        " background:#f4f4f4; padding:8px 16px; display:inline-block; border-radius:4px;'>"
        "{temp_password}</p>"
        "<p>Por segurança, você será solicitado a criar uma nova senha no próximo acesso.</p>"
        "<p>Se você não solicitou esta alteração, entre em contato com o suporte.</p>"
    )
