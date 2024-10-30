from Models.Entity import Entity

class EntityController:
    def __init__(self):
        self.model = Entity()

    def store(self, data):
        result = self.model.create(data)

        if result:
            return {"message": "Entity created successfully"}, 200
        
        return {"error": "Error on create entity"}, 400
    
    def index(self):
        return self.model.read_all()

    def show(self, id):
        try:
            return self.model.read(id), 200
        
        except:
            return {"error": "Entity has not been found"}, 404

    def update(self, id, new_values):
        try:
            result = self.model.update(id, new_values)

            print(result.matched_count)

            if result.matched_count > 0:
                return {"message": "Entity updated successfully"}, 200
            else:
                return {"error": "Entity has not been found"}, 404
            
        except:
            return {"error": "Entity has not been found"}, 404

    def destroy(self, id):
        try:
            result = self.model.delete(id)

            if result and result.deleted_count > 0:
                return {"message": "Entity deleted successfully"}, 200
            else:
                return {"error": "Entity has not been found"}, 404
        except:
            return {"error": "Entity has not been found"}, 404
