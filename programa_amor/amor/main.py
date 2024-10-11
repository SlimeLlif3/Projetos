import customtkinter as ctk
from pkg_resources import resource_filename
from random import randint
from datetime import datetime
from PIL import Image
import pygame
import sqlite3
from tkinter import *
from tkinter import messagebox

pygame.mixer.init()
class Back():
    
    def connect_db(self):
        self.connect = sqlite3.connect("Cadastro_amor.db")
        self.cursor = self.connect.cursor()
        
    def disconect_db(self):
        self.connect.close()

    def create_table(self):
        self.connect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuários(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL,
                Confirm_password TEX NOT NULL
            );          
        """)
        self.connect.commit()
        self.disconect_db()
        
    def register_entrys_in_db(self):
        self.register_username = self.register_username_entry.get()
        self.register_password = self.register_password_entry.get()
        self.register_confirm_password = self.register_confirm_password_entry.get()
        
        self.connect_db()
        self.cursor.execute("""
            INSERT INTO Usuários(Username, Password, Confirm_password)
            VALUES(?, ?, ?)""", (self.register_username, self.register_password, self.register_confirm_password))

        try:
            if self.register_username == "" or self.register_password == "" or self.register_confirm_password == "":
                messagebox.showerror(title="Cadastrando Usuário", message="Preenche todos os campos, se não da ruim ")
                self.disconect_db()
            elif len(self.register_username) < 4:
                messagebox.showwarning(title="Cadastrando Usuário", message="Escolha um nome de usuário com no mínimo 5 caractéres")
                self.disconect_db()
            elif len(self.register_password) < 6:
                messagebox.showwarning(title="Cadastrando Usuário", message="Escolha uma senha com no mínimo 6 caractéres")
                self.disconect_db()
            elif self.register_password != self.register_confirm_password:
                messagebox.showerror(title="Cadastrando Usuário", message="As duas senhas digitadas devem ser iguais")
                self.disconect_db()
            else:
                self.connect.commit()
                messagebox.showinfo(title="Cadastrando Usuário", message=f"Parabéns {self.register_username}!\nSeu cadastro foi realizado com sucesso")
                self.disconect_db()
                self.clean_entry_register()

        except:
            messagebox.showerror(title="ERRO",message="Infelizmente não foi possível fazer o seu cadastro\nQue pena! Tente novamente mais tarde")
            self.disconect_db()
            
    def login_verify(self):
        self.login_username = self.login_username_entry.get()
        self.login_password = self.login_password_entry.get()
        self.connect_db()
        
        self.cursor.execute("""
            SELECT * FROM Usuários WHERE (Username = ? AND Password = ?)""" , (self.login_username, self.login_password))
        self.verify_date = self.cursor.fetchone()
        try:
            if self.login_username in self.verify_date and self.login_password in self.verify_date:
                messagebox.showinfo(title="Login de Usuário", message=f"Parabéns {self.login_username}!\nSeu Login foi um sucesso")
                self.disconect_db()
                self.content_frame_login.pack_forget()
                self.widgets_window1()
        except:
            messagebox.showinfo(title="Login de Usuário", message="Erro!\nDados não encontrados no sistema, por favor tente novamente.")
            self.disconect_db()
        
class front(ctk.CTk,Back):
    def __init__(self):
        super().__init__()
        self.config_window1()
        self.login_screen()
        self.create_table()
        
    def clean_entry_register(self):
        self.register_username_entry.delete(0,END)
        self.register_password_entry.delete(0,END)
        self.register_confirm_password_entry.delete(0,END)
        
    def config_window1(self):
        self.title("Eu amo Ana Carolina")
        self.resource_icon = resource_filename(__name__,"coracao.ico")
        self.iconbitmap(self.resource_icon)
        self.geometry("800x500")
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")
    
    def login_screen(self):
        self.content_frame_login = ctk.CTkFrame(self,fg_color="transparent")
        self.content_frame_login.pack()
        
        self.tittle_login_screen = ctk.CTkLabel(self.content_frame_login, text="Faz login pra ver seu projetin do amor S2", font=("Roboto",40),text_color="#FF3E96").pack(pady=(20,0))
        
        self.login_username_entry = ctk.CTkEntry(self.content_frame_login, placeholder_text="Nome de usuário", font= ("Roboto",20),width=400, height=40, corner_radius=10)
        self.login_username_entry.pack(pady=(100,0))
        self.login_password_entry = ctk.CTkEntry(self.content_frame_login, placeholder_text="Senha", font= ("Roboto",20), width=400,height=40, corner_radius=10, show="*")
        self.login_password_entry.pack(pady=(20,0))
        
        self.frame_butons_login = ctk.CTkFrame(self.content_frame_login,fg_color="transparent")
        self.frame_butons_login.pack(pady=(20,0))
        
        self.button_login = ctk.CTkButton(self.frame_butons_login,text="LOGIN", width=150,height=40, corner_radius=15,fg_color="#FF3E96",font=("Roboto",16), hover_color="#CD3278",command=self.login_verify).pack(side=ctk.LEFT,padx=(0,45))
        self.button_for_register = ctk.CTkButton(self.frame_butons_login,text="CADASTRO", width=150,height=40, corner_radius=15,fg_color="#FF3E96",font=("Roboto",16), hover_color="#CD3278", command=self.register_screen).pack(side=ctk.LEFT,padx=(45,0))
        
    def register_screen(self):
        self.content_frame_login.pack_forget()
        
        self.content_frame_register = ctk.CTkFrame(self,fg_color="transparent")
        self.content_frame_register.pack()
        
        self.tittle_register_screen = ctk.CTkLabel(self.content_frame_register, text="Faz cadastro aí amor S2", text_color="#FF3E96", font=("Roboto",40)).pack(pady=(20,0))
        
        self.register_username_entry = ctk.CTkEntry(self.content_frame_register, placeholder_text="Nome de usuário", font= ("Roboto",20),width=400, height=40, corner_radius=10)
        self.register_username_entry.pack(pady=(70,0))
        
        self.register_password_entry = ctk.CTkEntry(self.content_frame_register, placeholder_text="Senha", font= ("Roboto",20), width=400,height=40, corner_radius=10, show="*")
        self.register_password_entry.pack(pady=(20,0))
        
        self.register_confirm_password_entry = ctk.CTkEntry(self.content_frame_register, placeholder_text="Confirmar Senha", font= ("Roboto",20), width=400,height=40, corner_radius=10, show="*")
        self.register_confirm_password_entry.pack(pady=(20,0))
        
        self.frame_butons_register = ctk.CTkFrame(self.content_frame_register,fg_color="transparent")
        self.frame_butons_register.pack(pady=(20,0))
        
        self.button_voltar = ctk.CTkButton(self.frame_butons_register,text="VOLTAR", width=150,height=40, corner_radius=15,fg_color="#FF3E96",font=("Roboto",16), hover_color="#CD3278",command=self.back_login_screen).pack(side=ctk.LEFT,padx=(0,45))
        self.button_register = ctk.CTkButton(self.frame_butons_register,text="CADASTRAR", width=150,height=40, corner_radius=15,fg_color="#FF3E96",font=("Roboto",16), hover_color="#CD3278", command=self.register_entrys_in_db).pack(side=ctk.LEFT,padx=(45,0))
        
    def back_login_screen(self):
        self.content_frame_register.pack_forget()
        self.content_frame_login.pack()
    
    def widgets_window1(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.titulo = ctk.CTkLabel(self, text="Você quer se casar comigo ? 💍", font=("arial bold", 35))
        self.titulo.pack(pady=(80,0))

        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=(170,0))
        
        self.button1 = ctk.CTkButton(self.frame_botoes, text="Sim", fg_color="#F00C14", hover_color="#BD595D", font=("arial bold", 30), command=self.outra_janela)
        self.button1.pack(side= ctk.LEFT, padx= (0, 100))

        self.button2 = ctk.CTkButton(self.frame_botoes, text="Não", fg_color="#F00C14", hover_color="#BD595D", font=("arial bold", 30))
        self.button2.pack(side=ctk.LEFT,padx = (100,00))
        self.button2.bind("<Button-1>", self.muda_de_lugar_botao)
        
        self.button3 = ctk.CTkButton(self, text="Não", fg_color="#F00C14", hover_color="#BD595D", font=("arial bold", 30))
        self.button3.bind("<Button-1>", self.muda_de_lugar_botao)
 
    def muda_de_lugar_botao(self,a):
        
        self.button2.pack_forget()
        self.button3.place(x=randint(0,700),y=randint(0,400))

    def outra_janela(self):
        def maximiza_janela():
            self.janela2.state("zoomed")
            
        def toca_musica():
            resource_music = resource_filename(__name__,"Eu Amo Você.mp3")
            pygame.mixer.music.load(resource_music)
            pygame.mixer.music.play(-1)
        
        # Configurações do contador
        hoje = datetime.today()
        data_alvo = datetime(2031, 1, 22)
        falta = data_alvo - hoje
        horas_restantes = falta.total_seconds() / 3600 
        em_str = str(horas_restantes)
        minutos_restantes = (falta.total_seconds() % 3600) // 60
        segundos_restantes = falta.total_seconds() % 60

        # Crio e configuro a janela2
        self.destroy()
        self.janela2 = ctk.CTk()
        self.janela2.iconbitmap(self.resource_icon)
        self.janela2.after(0, maximiza_janela)
        self.janela2.title("Casamento Marcado")
        toca_musica()
        
        # Textos da minha janela2
        ctk.CTkLabel(master=self.janela2, text=f"FALTAM EXATOS {falta.days} DIAS, {em_str[0:2]} HORAS, {minutos_restantes:.0f} MINUTOS E {segundos_restantes:.0f} SEGUNDOS PRA GENTE CASAR\nVAI TER QUE ME AGUENTAR KKKKK",font=("arial bold", 30), text_color="red").pack(pady=(10,0))
        
        self.textbox = ctk.CTkTextbox(master=self.janela2, width=400, height=270, fg_color="red", corner_radius= 50, border_width=8, border_color="#F5746E", scrollbar_button_color="#F5746E", scrollbar_button_hover_color="#F5746E", font=("arial bold",16))
        self.textbox.pack(pady = (20,0))
        self.textbox.insert("0.0","TE AMO ❤️" * 1000)
        self.textbox.insert("0.0","❤️❤️❤️❤️❤️❤️❤️\n")
        self.textbox.insert("0.0","Para minha namorada❤️\n\nFeliz dia dos namorados minha\nprincesa, enfim chegou o dia de\nmatar a curiosidade kkkkkk, saiba \nque foi de coração e deu um \ntrabalhoooo(serio deu muito kk).\nAaa Ana Carolina, minha eterna \nnamorada, sou grato todos os dias por te ter na minha vida e poder \npassar mais uma data dessa ao \nseu lado, saiba que eu te amo \nmuito, e mesmo depois de \ncasados você vai continuar sendo minha eterna namorada, nesse \nmomento a gente deve estar de \npandu cheio e todo boiolinha um \ncom o outro ksksksks, eu amo isso e espero que nunca se perca em \nnosso relacionamento, obrigado \npor tudo, principalmente por \nsegurar a minha mão em todos os \nmomentos e ser minha companhe-ira de vida. Bom agora que você \ndisse sim, vai ter que salvar esse \nprograma e guardar para acompa-nhar o calendário heinn, porque \nvamo casar quando o contador \nchegar a 0 kkkkk. Não preciso falar eu te amo, porque logo abaixo te  disse te amo 1000x kkkkkk, \nobrigado por tudo sempre minha \nprincesa.\n\n")
        
        self.textbox.configure(state="disabled")
        
        # Adicionando as imagens na minha janela2
        resource_foto_1 = resource_filename(__name__,"foto1.jpeg")
        abrir_foto1 = Image.open(resource_foto_1)
        converter_foto1 = ctk.CTkImage(abrir_foto1, size=(261,305))
        ctk.CTkLabel(master=self.janela2, image = converter_foto1, text="").pack(side=ctk.LEFT,padx=(144,0))

        resource_foto_2 = resource_filename(__name__,"foto2.jpeg")
        abrir_foto2 = Image.open(resource_foto_2)
        converter_foto2 = ctk.CTkImage(abrir_foto2, size=(261,305))
        ctk.CTkLabel(master=self.janela2, image = converter_foto2, text="").pack(side=ctk.LEFT,padx=(144,0))
        
        resource_foto_3 = resource_filename(__name__,"foto3.jpeg")
        abrir_foto3 = Image.open(resource_foto_3)
        converter_foto3 = ctk.CTkImage(abrir_foto3,size=(261,305))
        ctk.CTkLabel(master=self.janela2, image = converter_foto3, text="").pack(side=ctk.LEFT,padx=(144,0))

        self.janela2.mainloop()
    
if __name__ == "__main__":
    front = front()
    front.mainloop()

    