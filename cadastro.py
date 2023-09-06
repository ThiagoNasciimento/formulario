class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class CadastroUsuarios:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1
    
    def criar_usuario(self, nome, email):
        novo_usuario = Usuario(self.proximo_id, nome, email)
        self.usuarios.append(novo_usuario)
        self.proximo_id += 1
        return novo_usuario
    
    def listar_usuarios(self):
        return self.usuarios
    
    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None
    
    def atualizar_usuario(self, id, nome, email):
        usuario = self.buscar_usuario(id)
        if usuario:
            usuario.nome = nome
            usuario.email = email
            return usuario
        return None
    
    def deletar_usuario(self, id):
        usuario = self.buscar_usuario(id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

# Exemplo de uso
cadastro = CadastroUsuarios()

usuario1 = cadastro.criar_usuario("João", "joao@example.com")
usuario2 = cadastro.criar_usuario("Maria", "maria@example.com")

print("Usuários cadastrados:")
for usuario in cadastro.listar_usuarios():
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

usuario_para_atualizar = cadastro.buscar_usuario(1)
if usuario_para_atualizar:
    cadastro.atualizar_usuario(usuario_para_atualizar.id, "João Silva", "joao.silva@example.com")

print("\nUsuários após atualização:")
for usuario in cadastro.listar_usuarios():
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

if cadastro.deletar_usuario(2):
    print("\nUsuário removido com sucesso.")

print("\nUsuários após remoção:")
for usuario in cadastro.listar_usuarios():
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
