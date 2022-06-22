import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4     #-----> Estandar de la industria

    def to_dict(self):
        return vars(self)

    @staticmethod     #-----> Metodo que se puede ejecutar sin una instancia de clase
    def schema():
        return ["name", "company", "email", "position", "uid"]