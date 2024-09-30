from ..domain_imports import Repository, BaseModel, Expense, User, CryptographyService
from .expense_analysis_service import ExpenseAnalysisService

class DataService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_list(self, model: BaseModel):
        return self.repository.get_list(model)
    
    def get_entity(self, model: BaseModel, id):
        return self.repository.get_entity(model, id)
    
    def delete_entity(self, model: BaseModel, id):
        return self.repository.delete_entity(model, id)
    
    def save_entity(self, model: BaseModel):
        if isinstance(model, Expense):
            return self.process_expense_analysis(model)
        elif isinstance(model, User):
            model = self.save_user(model)
            if hasattr(model, 'error') and model.error:
                return model

        return self.repository.save_entity(model)

    def save_user(self, user: User):
        validated_user = self.validate_user_register(user)

        if hasattr(validated_user, 'error') and validated_user.error :
            return validated_user
        
        user.password = self.encrypt_user_password(user)
        
        return user

    def encrypt_user_password(self, user: User) -> str:
        try:
            password = getattr(user, 'password', None)

            if password and isinstance(password, str) and not password.startswith("b'gAAAA"):
                crypto_service = CryptographyService()
                return crypto_service.encrypt(password)
        except Exception as e:
            raise Exception(f"Erro ao salvar usuário: {str(e)}")
    
    def process_expense_analysis(self, expense: Expense) -> Expense:
        data_analysis_service = ExpenseAnalysisService()
        return data_analysis_service.process_expense(expense)
    
    def validate_user_register(self, user: User):
        repeated_user = self.repository.get_user_by_username(user.email)

        if not user.id and repeated_user:
            user.error = "Email já cadastrado"
        
        return user
