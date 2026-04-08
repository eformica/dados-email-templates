import sys, pathlib
sys.path.append(str(pathlib.Path(__file__)).split("config")[0])

from config.getenv_mixins.postgres import PostgresMixin
from config.getenv_mixins.validate_env import ValidateEnvMixin

from dotenv import load_dotenv
load_dotenv()

import os

ENVIRONMENT = os.getenv("ENVIRONMENT")

if ENVIRONMENT == "PROD":
    APP_DOMAIN = os.getenv("APP_DOMAIN", "https://app.perfecting.com.br")
else:
    APP_DOMAIN = os.getenv("APP_DOMAIN", "https://homolog.perfecting.com.br")

class GetEnv(ValidateEnvMixin):
    ENVIRONMENT = ENVIRONMENT

    class Email:
        SMTP_HOST = os.getenv("SMTP_HOST")
        SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
        SMTP_USER = os.getenv("SMTP_USER")
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
        SMTP_USE_TLS = os.getenv("SMTP_USE_TLS", "true").strip().lower() in {"1", "true", "yes", "y", "on"}
        SMTP_FROM = os.getenv("SMTP_FROM") or os.getenv("SMTP_USER")
        SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "Perfecting - Suporte")
        DEFAULT_LANGUAGE = "pt-br"

    class Routes:
        # Ativação após auto-cadastro (confirmação de e-mail, usuário já tem senha)
        ACCOUNT_ACTIVATION_PAGE_SIGNUP = f"{APP_DOMAIN}/activate/signup"
        # Ativação via convite do gestor (usuário define a senha na página)
        ACCOUNT_ACTIVATION_PAGE_INVITE = f"{APP_DOMAIN}/activate/invite"
        PLATFORM_URL = APP_DOMAIN

if __name__ == "__main__":
    GetEnv.validate_all_env_vars()
#    print(GetEnv.MQ.get_conn_str())