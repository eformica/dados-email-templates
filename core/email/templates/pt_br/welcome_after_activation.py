"""
Template de e-mail de boas-vindas após ativação da conta
"""
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__)).split("src")[0])

from src.core.services.email._base_email import BaseEmailTemplate


@BaseEmailTemplate.register
class WelcomeAfterActivation(BaseEmailTemplate):
    template_name = 'welcome_after_activation'
    language = 'pt-br'
    subject_template = "Bem-vindo(a) à Perfecting! 🎉"
    
    text_template = """Olá {user_name}!

Parabéns! Seu e-mail foi confirmado com sucesso e sua conta está ativa. 🎉

Agora você já pode acessar a plataforma Perfecting e aproveitar todos os recursos disponíveis para aprimorar suas habilidades de vendas.

PRÓXIMOS PASSOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Acesse a plataforma: {platform_url}
2. Faça login com seu e-mail: {user_email}
3. Complete seu perfil
4. Explore os recursos de treinamento

RECURSOS DISPONÍVEIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Role-plays interativos com IA
✓ Feedback personalizado e detalhado
✓ Métricas de desempenho
✓ Sessões de treinamento estruturadas

Estamos muito felizes em tê-lo(a) conosco!

Se tiver qualquer dúvida ou precisar de ajuda, não hesite em entrar em contato com nosso suporte.

Bons treinos!

Equipe Perfecting
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    
    html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem-vindo à Perfecting</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f5f5f5;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f5f5f5;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 30px; text-align: center; background: #3A71D9; border-radius: 8px 8px 0 0;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: 700;">
                                🎉 Bem-vindo(a)!
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px;">
                            <p style="margin: 0 0 20px; color: #333333; font-size: 16px; line-height: 1.6;">
                                Olá <strong>{user_name}</strong>!
                            </p>
                            
                            <p style="margin: 0 0 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                                Parabéns! Seu e-mail foi confirmado com sucesso e sua conta está ativa. 🎉
                            </p>
                            
                            <p style="margin: 0 0 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                                Agora você já pode acessar a plataforma <strong style="color: #3A71D9;">Perfecting</strong> e aproveitar todos os recursos disponíveis para aprimorar suas habilidades de vendas.
                            </p>
                            
                            <!-- CTA Button -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: 30px 0;">
                                <tr>
                                    <td style="text-align: center;">
                                        <a href="{platform_url}" style="display: inline-block; padding: 16px 40px; background: #3A71D9; color: #ffffff; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 16px;">
                                            Acessar Plataforma
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Next Steps -->
                            <div style="margin: 30px 0; padding: 25px; background-color: #f8f9fa; border-radius: 8px; border-left: 4px solid #3A71D9;">
                                <h2 style="margin: 0 0 20px; color: #333333; font-size: 18px; font-weight: 600;">
                                    📋 Próximos Passos
                                </h2>
                                <ol style="margin: 0; padding-left: 20px; color: #555555; font-size: 15px; line-height: 1.8;">
                                    <li style="margin-bottom: 10px;">Acesse a plataforma usando o botão acima</li>
                                    <li style="margin-bottom: 10px;">Faça login com seu e-mail: <strong>{user_email}</strong></li>
                                    <li style="margin-bottom: 10px;">Complete seu perfil</li>
                                    <li>Explore os recursos de treinamento</li>
                                </ol>
                            </div>
                            
                            <!-- Features -->
                            <div style="margin: 30px 0; padding: 25px; background-color: #f8f9fa; border-radius: 8px;">
                                <h2 style="margin: 0 0 20px; color: #333333; font-size: 18px; font-weight: 600;">
                                    ✨ Recursos Disponíveis
                                </h2>
                                <ul style="margin: 0; padding-left: 20px; color: #555555; font-size: 15px; line-height: 1.8;">
                                    <li style="margin-bottom: 10px;">✓ Role-plays interativos com IA</li>
                                    <li style="margin-bottom: 10px;">✓ Feedback personalizado e detalhado</li>
                                    <li style="margin-bottom: 10px;">✓ Métricas de desempenho</li>
                                    <li>✓ Sessões de treinamento estruturadas</li>
                                </ul>
                            </div>
                            
                            <p style="margin: 30px 0 20px; color: #333333; font-size: 16px; line-height: 1.6;">
                                Estamos muito felizes em tê-lo(a) conosco!
                            </p>
                            
                            <p style="margin: 0 0 10px; color: #666666; font-size: 14px; line-height: 1.6;">
                                Se tiver qualquer dúvida ou precisar de ajuda, não hesite em entrar em contato com nosso suporte.
                            </p>
                            
                            <p style="margin: 20px 0 0; color: #333333; font-size: 16px; line-height: 1.6; font-weight: 600;">
                                Bons treinos!
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 30px 40px; background-color: #f8f9fa; border-radius: 0 0 8px 8px; text-align: center;">
                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                <strong>Equipe <span style="color: #3A71D9;">Perfecting</span></strong>
                            </p>
                            <p style="margin: 10px 0 0; color: #999999; font-size: 12px;">
                                © 2026 <span style="color: #3A71D9;">Perfecting</span>. Todos os direitos reservados.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

