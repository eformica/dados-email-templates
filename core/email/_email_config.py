# Idioma padrão usado pelo módulo de e-mail.
# Quando um template não existir no idioma solicitado, o sistema emite um aviso
# e faz fallback para este idioma.  Se o template também não existir aqui, um
# erro será levantado.

import sys, pathlib
sys.path.append(str(pathlib.Path(__file__)).split("src")[0])

from config.getenv import GetEnv

DEFAULT_LANGUAGE: str = GetEnv.Email.DEFAULT_LANGUAGE
