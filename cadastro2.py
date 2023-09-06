import tkinter as tk
from tkinter import messagebox

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")
        
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()
        
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()
        
        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.pack()
        
        self.usuarios_cadastrados = []
        
    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        
        if nome and email:
            self.usuarios_cadastrados.append((nome, email))
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
