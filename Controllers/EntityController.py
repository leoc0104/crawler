from Models.Entity import Entity

class EntityController:
    def __init__(self):
        self.model = Entity()

    def store(self, data):
        return self.model.create(data)
    
    def index(self):
        return self.model.read_all()

    def show(self, query = {}):
        return self.model.read(query)

    def update(self, query, new_values):
        return self.model.update(query, new_values)

    def destroy(self, query):
        return self.model.delete(query)
