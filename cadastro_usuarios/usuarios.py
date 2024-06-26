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

            c.execute("INSERT INTO usuarios (nome, telefone, email, usuario, senha) VALUES(?, ?, ?, ?, ?)", (self.nome, self.telefone, self.email, self.usuario, self.senha))

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except NameError:
            print(NameError)
            return "Ocorreu um erro ao cadastrar o usuário!"
        
    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("UPDATE usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? WHERE id = ? ", (self.nome, self.telefone, self.email, self.usuario, self.senha, self.id))

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except NameError:
            print(NameError)
            return "Ocorreu um erro na alteração do usuário"
        
    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("DELETE FROM usuarios WHERE id = ? ", self.id)

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except NameError:
            print(NameError)
            return "Ocorreu um erro na exclusão do usuário"
        
    def selectUser(self, id):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM usuarios WHERE id = " + id + "  ")

            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except NameError:
            print(NameError)
            return "Ocorreu um erro na busca do usuário"
        
    def selectUsers(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("SELECT * FROM usuarios")

        except:
            pass