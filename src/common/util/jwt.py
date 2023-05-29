from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from starlette import status

from src.common.settings import settings

auth_scheme = HTTPBearer()


class JwtUtils:
    @staticmethod
    def decode_jwt(token: str):
        try:
            decoded_token = jwt.decode(
                token,
                settings.app.security.secret_key,
                algorithms=[settings.app.security.algorithm],
            )
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado"
            )
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
            )

    @staticmethod
    def jwt_authentication(
        credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    ):
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas"
            )
        token = credentials.credentials
        decoded_token = JwtUtils.decode_jwt(token)

        # Verificar se os campos 'sub', 'exp', 'scope' e 'roles' estão presentes no token decodificado
        if not all(key in decoded_token for key in ["sub", "exp", "scope", "roles"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token JWT inválido"
            )

        # Aqui você pode adicionar validações adicionais com base nos campos do JWT, se necessário

        return decoded_token
