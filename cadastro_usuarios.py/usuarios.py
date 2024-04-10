from banco import Banco

class Usuarios(object):
    def __init__(self, id = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            
            c.execute("""INSERT INTO usuarios (nome, telefone, email, usuario, senha) values(
                      '%s', '%s', '%s', '%s', '%s')
            )""")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro ao cadastrar o usuário!"