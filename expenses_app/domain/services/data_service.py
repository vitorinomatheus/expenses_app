from .domain_imports import *

class DataService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_list(self, model_class: BaseModel):
        return self.repository.get_list(model_class)
    
    def get_entity(self, model_class: BaseModel, id):
        return self.repository.get_entity(model_class, id)
    
    def delete_entity(self, model_class: BaseModel, id):
        return self.repository.delete_entity(model_class, id)
    
    def save_entity(self, model_class: BaseModel):
        if (model_class is Expense):
            return self.process_expense_analysis(model_class)
        else:
            return self.repository.save_entity(model_class)
    
    def process_expense_analysis(self, expense: Expense):
        pass
