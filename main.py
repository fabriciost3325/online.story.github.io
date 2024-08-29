from database import Database

db = Database()

class Usuario:
    def _init_(self, nome, email, idade, cidade):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.cidade = cidade

    @staticmethod
    def criar_tabela():
        db.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            idade INTEGER,
            cidade TEXT
        )
        ''')

    def salvar(self):
        db.execute('''
        INSERT INTO usuarios (nome, email, idade, cidade)
        VALUES (?, ?, ?, ?)
        ''', (self.nome, self.email, self.idade, self.cidade))

    @staticmethod
    def buscar_todos():
        return db.fetchall('SELECT * FROM usuarios')

    @staticmethod
    def buscar_por_email(email):
        return db.fetchone('SELECT * FROM usuarios WHERE email = ?', (email,))

    @staticmethod
    def atualizar(email, nome=None, idade=None, cidade=None):
        if nome:
            db.execute('UPDATE usuarios SET nome = ? WHERE email = ?', (nome, email))
        if idade:
            db.execute('UPDATE usuarios SET idade = ? WHERE email = ?', (idade, email))
        if cidade:
            db.execute('UPDATE usuarios SET cidade = ? WHERE email = ?', (cidade, email))

    @staticmethod
    def deletar(email):
        db.execute('DELETE FROM usuarios WHERE email = ?', (email,))

    @staticmethod
    def fechar_conexao():
        db.close()