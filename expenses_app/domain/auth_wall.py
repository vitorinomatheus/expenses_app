from flask import current_app
import jwt
from jwt.exceptions import PyJWTError
from typing import Callable

class AuthWall:

    def validate_token(self, token: str) -> dict:
        try:
            secret_key = current_app.config.get('SECRET_KEY')
            algorithm = current_app.config.get('JWT_ALGORITHM')
            payload = jwt.decode(token, secret_key, algorithms=[algorithm])
            return payload
        except PyJWTError:
            raise Exception("Token inválido ou expirado")

    def authorize(self, token: str, method: Callable, *args, **kwargs):
        try:
            obj_type = kwargs.get('model')

            if not token:
                raise Exception ("Token não informado")
            
            payload = self.validate_token(token)
            request_user_id = kwargs.get('id')

            if request_user_id is None:
                if hasattr(obj_type, 'user_id'):
                    request_user_id = getattr(obj_type, 'user_id')
                elif hasattr(obj_type, 'id'):
                    request_user_id = getattr(obj_type, 'id')

            if request_user_id and str(request_user_id) != str(payload['user_id']):
                raise Exception("Acesso não autorizado: tentativa de acessar dados de outro usuário")
            
            return method(**kwargs)
        
        except Exception as e:
            if obj_type:
                obj_type.error = str(e) 
                return obj_type  
            else:
                raise Exception(f"Erro de autenticação: {str(e)}")