from msilib.schema import ControlEvent
import mysql.connector

class connexaoDB:
    _conn = None
    _host = "localhost"
    _user = "root"
    _password = ""
    _bd = "pow"

    @staticmethod
    def conectar():
            if conexaoDB._conn == None:
                try:
                    connexaoDB._conn = mysql.connector.connect(
                        host = connexaoDB._host,
                        database = connexaoDB._bd,
                        user = connexaoDB._user,
                        password = connexaoDB._password)
                    return connexaoDB._conn
                except Exception as e:
                    return e
            return connexaoDB._conn
            
    @staticmethod
    def executaSql(sql, dados):
        try:
            cursor = connexaoDB._conn.cursor(prepared=True)
            cursor.execute(sql, dados)
            connexaoDB._conn.commit()
            return cursor.rowcount()
        except Exception as e:
            return e