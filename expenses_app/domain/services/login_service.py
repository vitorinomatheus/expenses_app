import jwt
from ..domain_imports import Repository, User
from ...api.graphql.graphql_mutations.graphql_login import LoginInput, LoginResponse
from .cryptography_service import CryptographyService
from datetime import datetime, timedelta, timezone
from flask import current_app

class LoginService:
    
    def login(self, login_input: LoginInput) -> LoginResponse:
        try:
            repository = Repository()
            user = repository.get_user_by_username(login_input['username'])

            if not user:
                login_response = LoginResponse()
                login_response.error = "Login não validado"
                return login_response
            
            informed_password = login_input['password']

            if self.compare_passwords(informed_password, user.password):
                login_response = LoginResponse()
                login_response.token = self.generate_jwt(user)
                login_response.user = user
                return login_response
            else:
                login_response = LoginResponse()
                login_response.error = "Login não validado"
                return login_response
        except Exception as e:
                login_response = LoginResponse()
                login_response.error = "Erro interno durante login"
                return login_response


    def compare_passwords(self, password_informed: str, password: User) -> bool:
        cryptography_service = CryptographyService()        
        decrypted = cryptography_service.decrypt(password)
        if decrypted == password_informed:
            return True
        else:
            return False

    def generate_jwt(self, user: User):
        SECRET_KEY = current_app.config.get('SECRET_KEY')
        ALGORITHM = current_app.config.get('JWT_ALGORITHM')
        TOKEN_EXPIRATION_MINUTES = 30

        payload = {
            "user_id": user.id,
            "username": user.email,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return token