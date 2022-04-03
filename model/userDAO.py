from model.conexaoDB import connexaoDB  
from model.userModel import User

class UserDAO:
    __slots__ =(
        '_con'
    )

    def __init__(self):
        self._con = connexaoDB.conectar()

    def inserirUser(self, user):
        # adiciona usuario ao banco de dados

        sql = ''' INSERT INTO user(nome, idade, email, profissao)
        values (?,?,?,?);'''
        valores = (user.nome, user.idade, user.email, user.profissao)
        res = connexaoDB.executaSql(sql, valores)
        return res == 1
    

    def atualizarUser(self, user):
        sql = '''UPDATE user SET nome=?, idade=?, email=?, profissao=? WHERE id=?;''' 
        valores = (user.nome, user.idade, user.email, user.profissao, user.id)
        res = connexaoDB.executaSql(sql, valores)
        return res == 1
    
    def excluirUser(self, id):
        sql = '''DELETE FROM user WHERE id=?;'''
        res = connexaoDB.executaSql(sql, id)
        return res == 1

    def buscarUser(self, nome):
        try:
            sql = "SELECT id, nome, idade, email, profissao from user where id=" +id
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            user = User(res[0],res[1], res[2], res[3], res[4])
            return user
        except Exception as e:
            print(str(e))
            return None
