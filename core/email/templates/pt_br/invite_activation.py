from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class InviteActivationTemplate(BaseEmailTemplate):
    template_name = "invite_activation"
    language = "pt-br"
    subject_template = "Você foi convidado(a) para a {organization_name} — ative sua conta"
    text_template = (
        "Olá {user_name},\n\n"
        "Você foi convidado(a) a fazer parte da {organization_name} na plataforma Perfecting!\n\n"
        "Para ativar sua conta e criar sua senha, acesse o link abaixo:\n"
        "{activation_link}\n\n"
        "Este link não possui data de expiração, mas recomendamos que você ative sua conta o quanto antes.\n\n"
        "Se você não esperava este convite, ignore esta mensagem.\n\n"
        "Equipe Perfecting"
    )
    html_template = (
        "<div style='font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;'>"
        "<h2 style='color: #3A71D9;'>Você foi convidado(a)! 🎉</h2>"
        "<p>Olá <strong>{user_name}</strong>,</p>"
        "<p>Você recebeu um convite para fazer parte da "
        "<strong>{organization_name}</strong> na plataforma "
        "<span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>.</p>"
        "<p>Para ativar sua conta e definir sua senha, clique no botão abaixo:</p>"
        "<p style='margin: 30px 0; text-align: center;'>"
        "<a href='{activation_link}' style='background-color: #3A71D9; color: white; "
        "padding: 14px 32px; text-decoration: none; border-radius: 6px; "
        "display: inline-block; font-weight: bold; font-size: 16px;'>Ativar Minha Conta</a>"
        "</p>"
        "<p style='color: #666; font-size: 14px;'>"
        "Ou copie e cole o link abaixo no seu navegador:<br>"
        "<span style='color: #3A71D9; word-break: break-all;'>{activation_link}</span>"
        "</p>"
        "<p style='color: #888; font-size: 13px;'>"
        "<em>Se você não esperava este convite, ignore esta mensagem.</em>"
        "</p>"
        "<p style='margin-top: 40px; color: #888; font-size: 0.9em; border-top: 1px solid #eee; padding-top: 20px;'>"
        "Equipe <span style='color: #3A71D9; font-weight: bold;'>Perfecting</span>"
        "</p>"
        "</div>"
    )
