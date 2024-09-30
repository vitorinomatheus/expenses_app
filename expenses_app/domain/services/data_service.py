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
        if model is Expense:
            return self.process_expense_analysis(model)
        elif model is User:
            model.password = self.encrypt_user_password(model)

        return self.repository.save_entity(model)
        
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
