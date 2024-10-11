import customtkinter as ctk
from PIL import Image as PILImage
from tkinter import *
from tkinter import messagebox
import sqlite3

class BackEnd():
    
    def conect_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado com sucesso")

    def disconect_db(self):
        self.conn.close()
        print("Banco de dados desconectado")
        
    def create_table(self):
        self.conect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );              
        """)
        self.conn.commit()
        print("Tabela criada")
        self.disconect_db()
        
    def register_user(self):
        self.username_register = self.username_entry_register.get()
        self.email_register = self.email_entry_register.get()
        self.password_register = self.password_entry_register.get()
        self.confirm_password_register = self.confirm_password_entry_register.get()
        
        self.conect_db()
        
        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ? , ?, ?)""", (self.username_register, self.email_register, self.password_register, self.confirm_password_register))
        
        try:
            if self.username_register == "" or self.email_register == "" or self.password_register == "" or self.confirm_password_register == "":
                messagebox.showerror(title="Sistema de Cadastro", message="Erro!!!\nPor favor preencha todos os campos!")
                self.disconect_db()
            elif len(self.username_register) < 4:
                messagebox.showwarning(title="Sistema de Cadastro", message="O nome de usuario deve ser de pelo menos 4 caractéres")
                self.disconect_db()
            elif len(self.password_register) < 7:
                messagebox.showwarning(title="Sistema de Cadastro", message="A senha deve ser de pelo menos 7 caractéres")
                self.disconect_db()
            elif self.password_register != self.confirm_password_register:
                messagebox.showerror(title="Sistema de Cadastro", message="Erro!!!\nAs senhas devem ser iguais")
                self.disconect_db()
            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de Cadastro", message=f"Parabéns {self.username_register}, o cadastro foi realizado com sucesso!")
                self.disconect_db()
                self.clean_register_entry()
                
        except:
            messagebox.showerror(title="Sistema de Cadastro", message="Erro no processamento do seu cadastro!\nPor favor tente novamente.")
            self.disconect_db()
        
    def login_verify(self):
        self.username_login = self.username_entry_login.get()
        self.password_login = self.password_entry_login.get()
        
        self.conect_db()
        
        self.cursor.execute(""" SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ? )""", (self.username_login, self.password_login))
        
        self.verify_data = self.cursor.fetchone()
        
        try:
            if self.username_login in self.verify_data and self.password_login in self.verify_data:
                messagebox.showinfo(title="Sistema de Login", message=f"Parabéns {self.username_login}\nseu login foi um sucesso!")
                self.disconect_db()
                self.clean_login_entry()
        except:
            messagebox.showerror(title="Sistema de Login", message="ERRO!!!\nDados não encontrados no sistema.\nPor favor verifique os seus dados ou cadastre-se no nosso sistema!")
            self.disconect_db()        

class Window(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.config_of_mainwindow()
        self.login_screen_content()
        self.create_table()
        
    def config_of_mainwindow(self):     
        self.geometry("1000x600")
        self.title("Sistema de login")
        self.resizable(False,False)
    
    def login_screen_content(self):
        # Imagem
        self.open_img = PILImage.open("programa_login/images.png")
        self.converte_img = ctk.CTkImage(self.open_img, size=(770,600))
        self.label_image = ctk.CTkLabel(master=self, image=self.converte_img, text=None).place(x=-280,y=0)
        
        # Frame de Login
        self.login_frame = ctk.CTkFrame(master=self, width=490, height=580, corner_radius=20)
        self.login_frame.place(x=500, y=10)
        self.frame_tittle = ctk.CTkLabel(master=self.login_frame, text="Sistema de Login", font=("Roboto", 33)).place(x=120, y=10)
        
        # Widgets do Frame de Login
        self.username_entry_login = ctk.CTkEntry(master=self.login_frame, placeholder_text="Username", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto",20))
        self.username_entry_login.place(x=30, y=150)
        self.label_username_entry = ctk.CTkLabel(master=self.login_frame, text="* O campo Username é obrigatório", font=("Roboto",13), text_color="green").place(x=35, y=200)

        self.password_entry_login = ctk.CTkEntry(master=self.login_frame, placeholder_text="Password", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto", 20), show="*")
        self.password_entry_login.place(x=30, y=250)
        self.label_password_entry = ctk.CTkLabel(master=self.login_frame, text="* O campo Password é obrigatório", font=("Roboto", 13), text_color="green").place(x=35, y=300)

        self.checkbox = ctk.CTkCheckBox(master=self.login_frame, width=30, height=30, text="Me lembrar sempre", font=("Roboto", 13)).place(x=35, y=335)
        
        self.login_button = ctk.CTkButton(master=self.login_frame,command=self.login_verify ,width=430, height=40, text="Login", font=("Roboto", 16), corner_radius=10).place(x=35, y=390)
        
        self.label_register = ctk.CTkLabel(master=self.login_frame, text="Se não tem uma conta", font=("Roboto", 16)).place(x=55, y=445)
        
        self.register_button = ctk.CTkButton(master=self.login_frame, command=self.screen_register, width=200, height=30, text="CADASTRE-SE", font=("Roboto", 16), corner_radius=6, fg_color="green", hover_color="#2D9334").place(x=265, y=445)

    def screen_register(self):
        # Apagar o frame de login
        self.login_frame.place_forget()
        
        # Criar novo frame de registro
        self.register_frame = ctk.CTkFrame(master=self, width=490, height=580, corner_radius=20)
        self.register_frame.place(x=500, y=10)
        
        # Widgets do novo frame de registro
        self.register_frame_tittle = ctk.CTkLabel(master=self.register_frame, text="Crie a sua conta", font=("Roboto", 33)).place(x=120, y=10)
        self.register_label = ctk.CTkLabel(master=self.register_frame, text="Preencha todos os campos corretamente", font=("Arial Bold", 13)).place(x=120, y=70)
        
        self.username_entry_register = ctk.CTkEntry(master=self.register_frame, placeholder_text="Username", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto", 20))
        self.username_entry_register.place(x=30, y=150)
        
        self.email_entry_register = ctk.CTkEntry(master=self.register_frame, placeholder_text="E-mail", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto", 20))
        self.email_entry_register.place(x=30, y=210)
        
        self.password_entry_register = ctk.CTkEntry(master=self.register_frame, placeholder_text="Password", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto", 20), show="*")
        self.password_entry_register.place(x=30, y=270)
        
        self.confirm_password_entry_register = ctk.CTkEntry(master=self.register_frame, placeholder_text="Confirm your password", placeholder_text_color="gray", width=430, height=40, corner_radius=10, font=("Roboto", 20), show="*")
        self.confirm_password_entry_register.place(x=30, y=330)
        
        self.register_checkbox = ctk.CTkCheckBox(master=self.register_frame, width=30, height=30, text="Aceito todos Termos e Políticas", font=("Roboto", 13)).place(x=35, y=390)
        
        self.save_button = ctk.CTkButton(master=self.register_frame, command= self.register_user, width=205, height=30, text="FAZER CADASTRO", font=("Roboto", 16), corner_radius=6, fg_color="green", hover_color="#014B05").place(x=255, y=445)
        
        def back_login_screen():
            
            # Apagar o frame de registro
            self.register_frame.place_forget()
            # Voltar para o frame de login
            self.login_frame.place(x=500, y=10)
            
        self.back_button = ctk.CTkButton(master=self.register_frame, command=back_login_screen, width=205, height=30, text="VOLTAR", font=("Roboto", 16), corner_radius=6, fg_color="black", hover_color="gray").place(x=30, y=445)
        
    def clean_register_entry(self):
        self.username_entry_register.delete(0,END)
        self.email_entry_register.delete(0,END)
        self.password_entry_register.delete(0,END)
        self.confirm_password_entry_register.delete(0,END)
        
    def clean_login_entry(self):
        self.username_entry_login.delete(0, END)
        self.password_entry_login.delete(0,END)
    
if __name__ == "__main__":
    window = Window()
    window.mainloop()
