import customtkinter as ctk
from pkg_resources import resource_filename
import PIL.Image
from tkcalendar import Calendar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
import sqlite3

# Cria classe para backend
class backend():
    
    # Conecta banco de dados
    def connect_db(self):
        self.conn = sqlite3.connect("Estoque.db")
        self.cursor = self.conn.cursor()
    
    # Desconecta banco de dados
    def disconnect_db(self):
        self.conn.close()
        
    # Cria tabela Users    
    def create_table_users(self):
        self.connect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                "Confirma Senha" TEXT NOT NULL 
            );
        """)
        self.conn.commit()
        self.disconnect_db()
    
    # Cria tabela Itens
    def create_table_itens(self):
        self.connect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Itens (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Produto TEXT NOT NULL,
                Quantidade INTEGER NOT NULL,
                "Valor Unitário" REAL NOT NULL,
                Tipo TEXT NOT NULL,
                Marca TEXT NOT NULL,
                "Data de entrada" TEXT NOT NULL
            );
        """)
        self.conn.commit()
        self.disconnect_db()
    
    # Pega dados das entrys de cadastro
    def pick_data_register(self):
        self.register_email = self.entry_register_email.get()
        self.register_password = self.entry_register_password.get()
        self.register_confirm_password = self.entry_register_confirm_password.get()

    # Pega dados das entrys de login
    def pick_data_login(self):
        self.login_email = self.entry_login_email.get()
        self.login_password = self.entry_login_password.get()

    # Pega dados das entrys de itens 
    def pick_data_itens(self):
        self.id = self.entry_id.get()
        self.product = self.entry_product.get()
        self.quantity = self.entry_quantity.get()
        self.value = self.entry_value.get()
        
        if self.quantity or self.value not in "": 
            self.quantity_int = int(self.quantity)
            self.value_float = float(self.value)
            
        self.type = self.entry_type.get()
        self.brand = self.entry_brand.get()
        self.date = self.calendar_for_menu.get_date()
        
    # Adiciona dados de cadastro na tabela Users
    def register_user(self):
        self.pick_data_register()
        self.connect_db()
        
        self.cursor.execute("""
            INSERT INTO Users(Email, Senha, "Confirma Senha") Values (?, ?, ?)""", (self.register_email, self.register_password, self.register_confirm_password))
        
        try:
            if self.register_email == "" or self.register_password == "" or self.register_confirm_password == "":
                messagebox.showwarning(title="Cadastro de Usuário", message="Por favor preencha todos os campos !!!")
                self.disconnect_db()
            elif self.register_password != self.register_confirm_password:
                messagebox.showerror(title="Cadastro de Usuário", message="As senhas devem ser iguais !!!")
                self.disconnect_db()
            elif len(self.register_password) < 5:
                messagebox.showwarning(title="Cadastro de Usuário", message="A senha deve ter no minímo 5 caractéres !!!")
                self.disconnect_db()
            else:
                messagebox.showinfo(title="Cadastro de Usuário", message=f"O seu cadastro foi realizado com sucesso !!!")
                self.conn.commit()
                self.disconnect_db()
                self.back_to_login_screen()
        except:
            messagebox.showerror(title="ERRO", message="Não foi possível realizar o seu cadastro, por favor tente novamente mais tarde.")
            self.disconnect_db()
    
    # Verifica se o usuario está cadastrado para fazer login
    def login_user(self):
        self.pick_data_login()
        self.connect_db()
        
        self.cursor.execute(""" SELECT * FROM Users WHERE (Email = ? AND Senha = ?)""", (self.login_email, self.login_password))
        
        self.verify_data = self.cursor.fetchone()
        
        try:
            if self.login_email in self.verify_data and self.login_password in self.verify_data:
                messagebox.showinfo(title="Login de Usuário", message="Login realizado com sucesso!!!")
                self.conn.commit()
                self.disconnect_db()
                self.widgets_of_toplevel_window()
        except:   
            messagebox.showwarning(title="Login de Usuário", message="Informações de login não encontradas em nosso sistema, por favor faça o login!!!")
            self.disconnect_db()
            
    # Deleta itens na tabela Itens
    def delete_entrys_itens(self):
            self.entry_product.delete(0, END)
            self.entry_quantity.delete(0,END)
            self.entry_value.delete(0,END)
            self.entry_type.delete(0,END)
            self.entry_brand.delete(0,END)
    # Adiciona itens na tabela Itens
    def add_data(self):
        self.pick_data_itens()
        
        self.connect_db()
    
        self.cursor.execute("""
            INSERT INTO Itens(Produto, Quantidade,"Valor Unitário", Tipo, Marca, "Data de entrada")Values (?, ?, ?, ?, ?, ?)""", (self.product, self.quantity_int, f"{self.value_float:.2f}", self.type, self.brand, self.date))
        
        try:
            if self.product == "" or self.quantity_int == "" or self.value_float == "" or self.type == "" or self.brand == "" or self.date == "":
                messagebox.showwarning(title="Adicionando produto", message="Todos os campos devem ser preenchidos!!!")
                self.disconnect_db()
            else:
                messagebox.showinfo(title="Adicionando produto", message="Produto cadastrado com sucesso!!!")
                self.conn.commit()
                self.disconnect_db()
                self.add_data_in_table()
                self.delete_entrys_itens()
        except:
            messagebox.showerror(title="Adicionando produto", message="Não foi possivel adicionar o produto, por favor tente novamente!!!")
            self.disconnect_db()
                    
    # Pesquisa itens na tabela Itens        
    def seach_product(self):
        self.delete_entrys_itens()
        self.pick_data_itens()
        self.connect_db()
        
        self.cursor.execute("""SELECT * FROM Itens WHERE Id = ?""", (self.id))
        data = self.cursor.fetchone() 
        try:
            self.entry_product.insert(0,data[1])
            self.entry_quantity.insert(0,data[2])
            self.entry_value.insert(0,data[3])
            self.entry_type.insert(0,data[4])
            self.entry_brand.insert(0,data[5])
            self.disconnect_db()
        except:
            messagebox.showerror(title="ERRO",message="O ID pesquisado não existe no estoque")

    # Atualiza itens na tabela Itens
    def update_data(self):
        self.pick_data_itens()
        self.connect_db()
        
        self.cursor.execute("""UPDATE Itens SET Produto=?, Quantidade=?,"Valor Unitário"=?, Tipo=?, Marca=?, "Data de entrada"=? WHERE Id=?""",(self.product, self.quantity_int, self.value_float, self.type, self.brand, self.date, self.id))
    
        try:
            messagebox.showinfo(title="Atualizando produto", message="O produto foi atualizado com sucesso!!!")
            self.update_data_in_table()
            self.conn.commit()
            self.disconnect_db()
            self.delete_entrys_itens()
        except:
            messagebox.showerror(title="Atualizando produto", message=" Não foi possivel atualizar o produto, por favor tente novamente!!!")
            self.disconnect_db()    
            
    # Deleta itens na tabela Itens        
    def delete_data(self):
        self.pick_data_itens() 
        self.connect_db()
         
        self.cursor.execute("""DELETE FROM Itens WHERE Id =?""", (self.id))
        
        try:
            messagebox.showinfo(title="Excluindo produto", message="O produto foi excluído com sucesso!!!")
            self.conn.commit()
            self.delete_data_in_table()
            self.disconnect_db()
            
        except:
            messagebox.showerror(title="Excluindo produto", message="Não foi possivel excluir o produto, por favor tente novamentr!!!")
            self.disconnect_db()
        
# Cria classe para frontend                 
class frontend(ctk.CTk,backend):
    
    # Construtor
    def __init__(self):
        super().__init__()
        self.config_of_login_and_register_window()
        self.widgets_of_login_window() 
        self.create_table_itens()
        self.create_table_users()
    
    # Configurações da janela de Login/Cadastro
    def config_of_login_and_register_window(self):
        self.title("Gerenciador de Estoque")
        self._set_appearance_mode("light")
        self.geometry("950x550") 
        self.resizable(False, False)
        self.arquivo = resource_filename(__name__,"mercado.ico")
        self.iconbitmap(self.arquivo)

    # Widgets da tela de login
    def widgets_of_login_window(self):
        
        self.wallpaper = resource_filename(__name__,"wallpaper.jpg")
        self.open_wallpaper = PIL.Image.open(self.wallpaper)
        self.convert_wallpaper = ctk.CTkImage(self.open_wallpaper,size=(530,550))
        self.label_wallpaper = ctk.CTkLabel(self,text="", image=self.convert_wallpaper).place(x = 0, y = 0)

        self.frame_login_window = ctk.CTkFrame(self, width= 420, height=550, fg_color="white",corner_radius=0)
        self.frame_login_window.pack_propagate(False)
        self.frame_login_window.pack(side="right")

        self.label_no_account = ctk.CTkLabel(self.frame_login_window, text="Não possui uma conta ?", text_color="#8B8989", font=("Helvetica", 15)).pack(side = "left", anchor= "n", padx = (60,0),pady = (20,0))

        self.font_button_for_register_screen = ctk.CTkFont(family="Helvetica", size=16, weight="bold")
        self.button_for_register_screen = ctk.CTkButton(self.frame_login_window, width=100, height=40, corner_radius=20, text="Cadastre-se",font=self.font_button_for_register_screen, fg_color="white",border_width=2, border_color="#FF00FF", text_color="#FF00FF", hover_color="#EEE9E9", command=self.widgets_of_register_window).pack(side= "left", anchor= "n",padx = (20,0),pady = (15,0))

        
        self.label_tittle_login = ctk.CTkLabel(self.frame_login_window, text="Login", font=("04b", 50), text_color="black").place(x=50, y=130)

        self.label_login_email = ctk.CTkLabel(self.frame_login_window, text="Email", font=("Helvetica", 15), text_color="black").place(x=60, y= 230)

        self.entry_login_email = ctk.CTkEntry(self.frame_login_window, width=300, height=35, corner_radius=5,border_width=2,fg_color="white", border_color="#CDC9C9", text_color="black")
        self.entry_login_email.place(x=60,y= 255)

        self.label_password = ctk.CTkLabel(self.frame_login_window, text="Senha", font=("Helvetica", 15), text_color="black").place(x=60, y= 310)
        self.entry_login_password = ctk.CTkEntry(self.frame_login_window, width=300, height=35, corner_radius=5,border_width=2,fg_color="white", border_color="#CDC9C9", text_color="black", show="*")
        self.entry_login_password.place(x=60,y= 335)

        self.label_forget_password = ctk.CTkLabel(self.frame_login_window, text="Esqueceu a senha?", font=("Helvetica", 15), text_color="#8B8989").place(x=225,y=373)

        self.button_login = ctk.CTkButton(self.frame_login_window, width=100, height=40, text="Log in", corner_radius=20, font = self.font_button_for_register_screen , fg_color="#FF00FF", text_color="white", hover_color="#EE82EE", command=self.login_user).place(x=55, y=420  )

        self.radio_remember = ctk.CTkRadioButton(self.frame_login_window, radiobutton_height=18, radiobutton_width=18, text="Lembrar de mim", text_color="#8B8989", font=("Helvetica", 15), hover_color="#FF00FF", border_width_checked=3, border_width_unchecked=3, fg_color="#FF00FF",).place(x=215, y=430)
    
    # Widgets da tela de cadastro 
    def widgets_of_register_window(self):
        self.frame_login_window.pack_forget()

        self.frame_register_window = ctk.CTkFrame(self, width= 420, height=550, fg_color="white",corner_radius=0)
        self.frame_register_window.pack_propagate(False)
        self.frame_register_window.pack(side="right")

        self.label_tittle_register = ctk.CTkLabel(self.frame_register_window, text="Cadastre-se", font=("04b", 38), text_color="black").pack(pady=(60,0))

        self.label_register_email = ctk.CTkLabel(self.frame_register_window, text="Email", font=("Helvetica", 15), text_color="black").place(x=60, y= 150)
        self.entry_register_email = ctk.CTkEntry(self.frame_register_window, width=300, height=35, corner_radius=5,border_width=2,fg_color="white", border_color="#CDC9C9", text_color="black")
        self.entry_register_email.place(x=60,y= 175)

        self.label_register_password = ctk.CTkLabel(self.frame_register_window, text="Senha", font=("Helvetica", 15), text_color="black").place(x=60, y= 220)
        self.entry_register_password = ctk.CTkEntry(self.frame_register_window, width=300, height=35, corner_radius=5,border_width=2,fg_color="white", border_color="#CDC9C9", text_color="black",show="* ")
        self.entry_register_password.place(x=60,y= 245)

        self.label_register_confirm_password = ctk.CTkLabel(self.frame_register_window, text="Confirme a senha", font=("Helvetica", 15), text_color="black").place(x=60, y= 290)
        self.entry_register_confirm_password = ctk.CTkEntry(self.frame_register_window, width=300, height=35, corner_radius=5,border_width=2,fg_color="white", border_color="#CDC9C9", text_color="black",show="* ")
        self.entry_register_confirm_password.place(x=60,y= 315)

        self.button_register = ctk.CTkButton(self.frame_register_window,width=300, height=40, corner_radius=10, text="Cadastrar", text_color="white",hover_color="#EE82EE", fg_color="#FF00FF",font=self.font_button_for_register_screen, command=self.register_user).place(x=60,y=370)
    
    # Volta para a tela de login
    def back_to_login_screen(self):
        self.frame_register_window.pack_forget()
        self.frame_login_window.pack(side="right")

    # Configurações da janela toplevel
    def config_of_toplevel_window(self):
        self.withdraw()
        ctk.set_appearance_mode("light")
        self.toplevel_window = ctk.CTkToplevel()
        self.toplevel_window.title("Gerenciador de Estoque")
        self.toplevel_window.iconbitmap(self.arquivo)
        self.toplevel_window.geometry("1050x650")
        self.toplevel_window.resizable(False,False)

    # Widgets da tela de Estoque
    def widgets_of_toplevel_window(self):
        self.config_of_toplevel_window()
        
        self.frame_for_label_stock = ctk.CTkFrame(self.toplevel_window, width=1050, height=80, fg_color="#FF00FF", corner_radius=0)
        self.frame_for_label_stock.pack()
        self.frame_for_label_stock.pack_propagate(False)
        
        self.icon_pokeball = resource_filename(__name__,"pokeball.png")
        self.open_icon_pokeball = PIL.Image.open(self.icon_pokeball)
        self.convert_icon_pokeball = ctk.CTkImage(self.open_icon_pokeball,size=(50, 50))
        self.label_icon_pokeball = ctk.CTkLabel(self.frame_for_label_stock,text="", image=self.convert_icon_pokeball).pack(side="left", padx= (30,20))

        self.label_for_frame_stock = ctk.CTkLabel(self.frame_for_label_stock, text="Estoque", font= ("04b", 40), text_color="white").pack(side="left",pady=(5,0))
        
        self.font_label_name = ctk.CTkFont(family="Helvetica", size=15, weight="bold")

        self.label_id = ctk.CTkLabel(self.toplevel_window, text="ID", font=self.font_label_name, text_color="black").place(x=20, y= 120)
        self.entry_id = ctk.CTkEntry(self.toplevel_window, width=115, height=5,corner_radius=0)
        self.entry_id.place(x=140,y=122)
        
        self.button_search = ctk.CTkButton(self.toplevel_window, width=100, height=5, text="Procurar", fg_color="#FF00FF",hover_color="#EE82EE", font=self.font_button_for_register_screen, text_color="white", command=self.seach_product)
        self.button_search.place(x=269, y= 121)
        
        self.label_product = ctk.CTkLabel(self.toplevel_window, text="Produto", font=self.font_label_name, text_color="black").place(x=20, y= 160)
        self.entry_product = ctk.CTkEntry(self.toplevel_window, width=230, height=5,corner_radius=0)
        self.entry_product.place(x=140,y=162)

        self.label_quantity = ctk.CTkLabel(self.toplevel_window, text="Quantidade", font=self.font_label_name, text_color="black").place(x=20, y= 200)
        self.entry_quantity = ctk.CTkEntry(self.toplevel_window, width=230, height=5,corner_radius=0)
        self.entry_quantity.place(x=140,y=202)

        self.label_value = ctk.CTkLabel(self.toplevel_window, text="Valor Unitário", font=self.font_label_name, text_color="black").place(x=20, y= 240)
        self.entry_value = ctk.CTkEntry(self.toplevel_window, width=230, height=5,corner_radius=0)
        self.entry_value.place(x=140,y=242)

        self.label_type = ctk.CTkLabel(self.toplevel_window, text="Tipo", font=self.font_label_name, text_color="black").place(x=20, y= 280)
        self.entry_type = ctk.CTkEntry(self.toplevel_window, width=230, height=5,corner_radius=0)
        self.entry_type.place(x=140,y=282)

        self.label_brand = ctk.CTkLabel(self.toplevel_window, text="Marca", font=self.font_label_name, text_color="black").place(x=20, y= 320)
        self.entry_brand = ctk.CTkEntry(self.toplevel_window, width=230, height=5,corner_radius=0)
        self.entry_brand.place(x=140,y=322)

        self.label_date = ctk.CTkLabel(self.toplevel_window, text="Data de entrada", font=self.font_label_name, text_color="black").place(x=20, y= 362)
        
        # Salva data clicada no calendário
        def save_date(event):
            self.save = self.calendar_for_menu.get_date()
            self.calendar_for_menu.place_forget()
            
        # Posiciona o calendário
        def positions_calendar():
            self.calendar_for_menu.place(x=140, y= 162)
            self.calendar_for_menu.bind("<<CalendarSelected>>", save_date)

        self.date_menu = ctk.CTkButton(self.toplevel_window, width=50, height=25, command=positions_calendar,text="Selecione", fg_color="#FF00FF",hover_color="#EE82EE", font=self.font_button_for_register_screen, text_color="white").place(x=210, y= 363)

        self.calendar_for_menu = Calendar(self.toplevel_window, selectmode="day",year=2024, month=7, day=25)

        self.add = resource_filename(__name__,"add.png")
        self.open_add = PIL.Image.open(self.add)
        self.convert_add = ctk.CTkImage(self.open_add)
        self.button_add = ctk.CTkButton(self.toplevel_window, image=self.convert_add, text="Adicionar", width=120, height=36, fg_color="#FF00FF",hover_color="#EE82EE",text_color="white", border_width=1, border_color="#EE82EE", font=self.font_button_for_register_screen, command=self.add_data).place(x=400,y= 132)

        self.update = resource_filename(__name__,"update.png")
        self.open_update = PIL.Image.open(self.update)
        self.convert_update = ctk.CTkImage(self.open_update)
        self.button_update = ctk.CTkButton(self.toplevel_window, image=self.convert_update, text="Atualizar", width=120, height=36, fg_color="#FF00FF",hover_color="#EE82EE",text_color="white", border_width=1, border_color="#EE82EE", font=self.font_button_for_register_screen, command=self.update_data).place(x=400,y= 182)

        self.delete = resource_filename(__name__,"delete.png")
        self.open_delete = PIL.Image.open(self.delete)
        self.convert_delete = ctk.CTkImage(self.open_delete)
        self.button_delete = ctk.CTkButton(self.toplevel_window, image=self.convert_delete, text="Excluir", width=120, height=36, fg_color="#FF00FF",hover_color="#EE82EE",text_color="white", border_width=1, border_color="#EE82EE", font=self.font_button_for_register_screen, command=self.delete_data).place(x=400,y= 232)
    
        self.frame_treeview = ctk.CTkFrame(self.toplevel_window, width=1050, height=250, corner_radius=0)
        self.frame_treeview.pack(side="bottom", )
        self.frame_treeview.propagate(False)
        
        self.columns = ("Id", "Produto","Quantidade","Valor Unitário","Tipo ","Marca ","Data de entrada")
        self.treeview_toplevel_window = ttk.Treeview(self.frame_treeview, columns=self.columns, show="headings")
        self.treeview_toplevel_window.pack(fill=ctk.BOTH, expand=True)
        
        for col in self.columns:
            self.treeview_toplevel_window.heading(col, text=col)
            
        self.treeview_toplevel_window.column(self.columns[0], width=10, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[1], width=150, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[2], width=70, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[3], width=50, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[4], width=60, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[5], width=70, anchor=ctk.CENTER)
        self.treeview_toplevel_window.column(self.columns[6], width=30, anchor=ctk.CENTER)
        
        self.show_all_data()
        
        
        self.frame_sum_stock = ctk.CTkFrame(self.toplevel_window, width=250, height=90, fg_color="#FF00FF")
        self.frame_sum_stock.place(x = 670, y = 160)
        self.frame_sum_stock.propagate(False)
        
        self.font_label_sum_stock = ctk.CTkFont(family="Helvetica", size=23, weight="bold")
        self.label_sum_stock = ctk.CTkLabel(self.frame_sum_stock, text=f"Valor total do estoque\nR${self.sum:.2f}", text_color="white", font=self.font_label_sum_stock)
        self.label_sum_stock.pack(pady=20)
        
    # Funções da treeview    
    def show_all_data(self):
        self.connect_db()
        self.cursor.execute("""SELECT * FROM Itens""")
        self.all_data = self.cursor.fetchall()
        self.sum = 0
        for item in self.all_data:
            self.treeview_toplevel_window.insert("", ctk.END,iid=item[0],values=(item))
            self.sum += item[3] * item[2]
    
    def add_data_in_table(self):
        self.connect_db()
        self.cursor.execute(""" SELECT * FROM Itens""")
        self.cont = self.cursor.fetchall()
        self.sum = 0
        for c in self.cont:
            
            self.sum += c[3] * c[2]
            
        self.treeview_toplevel_window.insert("", ctk.END,iid=c[0],values=(c[0], self.product, self.quantity_int, self.value_float, self.type, self.brand, self.date))
        
        self.label_sum_stock.pack_forget()  
        self.label_sum_stock = ctk.CTkLabel(self.frame_sum_stock, text=f"Valor total do estoque\nR${self.sum:.2f}", text_color="white", font=self.font_label_sum_stock)
        self.label_sum_stock.pack(pady=20)

    def update_data_in_table(self):

        self.cursor.execute(""" SELECT * FROM Itens""")
        self.cont = self.cursor.fetchall()

        self.sum = 0 
        for c in self.cont:
            self.sum += c[3] * c[2]


        self.label_sum_stock.pack_forget()  
        self.label_sum_stock = ctk.CTkLabel(self.frame_sum_stock, text=f"Valor total do estoque\nR${self.sum:.2f}", text_color="white", font=self.font_label_sum_stock)
        self.label_sum_stock.pack(pady=20)    

        self.cursor.execute("""SELECT * FROM Itens WHERE Id=?""",(self.id))
        self.atualiza = self.cursor.fetchone()
        self.treeview_toplevel_window.item(self.id, values= self.atualiza)  
        
    def delete_data_in_table(self):

        self.cursor.execute(""" SELECT * FROM Itens""")
        self.cont = self.cursor.fetchall()

        self.sum = 0 
        for p in self.cont:
            self.sum += p[3] * p[2]
        
        self.label_sum_stock.pack_forget()  
        self.label_sum_stock = ctk.CTkLabel(self.frame_sum_stock, text=f"Valor total do estoque\nR${self.sum:.2f}", text_color="white", font=self.font_label_sum_stock)
        self.label_sum_stock.pack(pady=20)
        
        self.treeview_toplevel_window.delete(self.id)


        self.toplevel_window.mainloop() 
                
if __name__ == "__main__":
    window = frontend()
    window.mainloop()
    
