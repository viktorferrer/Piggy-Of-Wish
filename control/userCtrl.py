from model.userDAO import UserDAO
from model.userModel import User

class userCtrl:
    def salvarAtualizarUser(self, id=None, nome="", idade=None, email="", profissao=""):
        if len(nome) > 3:
            inseriuAtualizou = False
            user = User(nome = nome, idade = idade, email = email, profissao = profissao)
            dao = UserDAO()

            if id:
                user.id = id
                inseriuAtualizou = dao.atualizarUser(user)
            else:
                inseriuAtualizou = dao.inserirUser(user)
            if inseriuAtualizou:
                return "Usuário adicionado no banco de dados"
            else:
                return "O usuário não pôde ser criado"
        else:
            return "O nome do usuário deve ter mais de 3 caractéres"

    def excluirUser(self, id):
        dao = UserDAO()
        excluiu = dao.excluirUser(str(id))
        if excluiu:
            return "Usuario excluido"
        else:
            return "Usuário não pôde ser removido"