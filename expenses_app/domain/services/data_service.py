from ...infra.repository import Repository
from ...imports import BaseModel

class DataService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_list(self, model_class: BaseModel):
        return self.repository.get_list(model_class)
    
    def get_entity(self, model_class: BaseModel, id):
        return self.repository.get_entity(model_class, id)
