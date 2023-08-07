import eventos
from libs import *


class appPrincipal(eventos.Conectivos):

    def __init__(self) -> None:
        self.appl = CTk()
        self.configTela()
        self.framePrincipal()
        self.widgetsTela()
        self.appl.mainloop()
        
    
    def configTela(self):
        self.appl.title('Projeto Reforma - Menu Principal')
        self.appl.configure(bg='#ffffff')
        self.larTela = 1200
        self.altTela = 600
        self.largMonitor = self.appl.winfo_screenwidth()
        self.altMonitor = self.appl.winfo_screenheight()
        self.posX = (self.largMonitor / 2) - (self.larTela / 2)
        self.posY = (self.altMonitor / 2) - (self.altTela / 2)
        self.appl.geometry("%dx%d+%d+%d" % (self.larTela, self.altTela, self.posX, self.posY))
        self.appl.minsize(width=1200, height=600)
        self.appl.resizable(False, False)

    
    def framePrincipal(self):
        self.PrincFrame = CTkFrame(self.appl, width=1180, height=580, fg_color='#3b3f49')
        self.PrincFrame.place(relx=0.01, rely=0.02)

    def widgetsTela(self):
        self.treeLista = ttk.Treeview(self.PrincFrame,   height=4, columns=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8'),  show='headings')
        self.treeLista.heading('#0', text='')
        self.treeLista.heading('#1', text='Código')
        self.treeLista.heading('#2', text='Descrição')
        self.treeLista.heading('#3', text='Fornecedor')
        self.treeLista.heading('#4', text='Qtd')
        self.treeLista.heading('#5', text='Preço Unit')
        self.treeLista.heading('#6', text='Preço Total')
        self.treeLista.heading('#7', text='Data')
        self.treeLista.heading('#8', text='Categoria')

        self.treeLista.column('#0', width=1, anchor='center')
        self.treeLista.column('#1', width=40, anchor='center')
        self.treeLista.column('#2', width=170, anchor='center')
        self.treeLista.column('#3', width=100, anchor='center')
        self.treeLista.column('#4', width=40, anchor='center')
        self.treeLista.column('#5', width=70, anchor='center')
        self.treeLista.column('#6', width=70, anchor='center')
        self.treeLista.column('#7', width=65, anchor='center')
        self.treeLista.column('#8', width=70, anchor='center')

        self.treeLista.place(relx=0.01, rely=0.02, relwidth=0.57, relheight=0.96)

        self.scrollLista = CTkScrollbar(self.PrincFrame, orientation='vertical', command=self.treeLista.yview)
        self.scrollLista.place(relx=0.58, rely=0.02, relheight=0.96)
        self.treeLista.configure(yscrollcommand=self.scrollLista.set)
        self.treeLista.bind("<Double-1>", self.duplo_clique_produto)

        self.imgSearch = CTkImage(dark_image=Image.open('.\\img\search.png'), size=(20, 20))

        self.lbl_consultaCategoria = CTkLabel(self.PrincFrame, text='Buscar por categoria: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_consultaCategoria.place(relx=0.62, rely=0.03)
        self.et_consultaCategoria = CTkEntry(self.PrincFrame, font=('Arial', 12), width=60, height=30, placeholder_text='Código')
        self.et_consultaCategoria.place(relx=0.62, rely=0.07)

        self.btn_exibirCategoria = CTkButton(self.PrincFrame, 
                                text='',
                                image=self.imgSearch,
                                text_color='#000', 
                                font=('Arial', 12, 'bold'), 
                                width=40, height=20,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.buscarPorCategoria)
        self.btn_exibirCategoria.place(relx=0.675, rely=0.07)

        self.lbl_consulta = CTkLabel(self.PrincFrame, text='Buscar: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_consulta.place(relx=0.82, rely=0.03)
        self.et_consulta = CTkEntry(self.PrincFrame, font=('Arial', 12), width=150, height=30, placeholder_text='Digite a descrição')
        self.et_consulta.place(relx=0.82, rely=0.07)

        
        self.btn_consultar = CTkButton(self.PrincFrame, 
                                image=self.imgSearch,
                                text='',  
                                width=40, height=20,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.buscarProduto)
        self.btn_consultar.place(relx=0.95, rely=0.07)

        self.btn_salvar = CTkButton(self.PrincFrame, 
                                text='Cadastrar', 
                                text_color='#000',
                                font=('Arial', 12, 'bold'), 
                                width=70, height=40,
                                fg_color='#FF9044',
                                hover_color='#fa7a32')
        self.btn_salvar.place(relx=0.925, rely=0.19)

        self.btn_exibir = CTkButton(self.PrincFrame, 
                                text='Listar', 
                                text_color='#000',
                                font=('Arial', 12, 'bold'), 
                                width=70, height=40,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.exibirProdutos)
        self.btn_exibir.place(relx=0.925, rely=0.29)

        self.btn_editar = CTkButton(self.PrincFrame, 
                                text='Editar', 
                                text_color='#000',
                                font=('Arial', 12, 'bold'), 
                                width=70, height=40,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.editarProduto)
        self.btn_editar.place(relx=0.925, rely=0.39)

        self.btn_excluir = CTkButton(self.PrincFrame, 
                                text='Excluir', 
                                text_color='#000',
                                font=('Arial', 12, 'bold'), 
                                width=70, height=40,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.deletarProduto
                                )
        self.btn_excluir.place(relx=0.925, rely=0.49)

        self.imgLogoff = CTkImage(dark_image=Image.open('.\\img\logoff.png'), size=(40, 40))
        self.btn_sair =CTkButton(self.PrincFrame, 
                                text='', 
                                image=self.imgLogoff, 
                                width=40, height=20,
                                fg_color='#FF9044',
                                hover_color='#fa7a32',
                                command=self.appl.destroy)
        self.btn_sair.place(relx=0.938, rely=0.9)

        self.lbl_descricao = CTkLabel(self.PrincFrame, text='Descrição*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_descricao.place(relx=0.62, rely=0.15)
        self.et_descricao = CTkEntry(self.PrincFrame, font=('Arial', 12), width=200, height=30, placeholder_text='Digite a descrição')
        self.et_descricao.place(relx=0.62, rely=0.19)
        self.et_descricao.focus()

        self.lbl_fornecedor = CTkLabel(self.PrincFrame, text='Fornecedor*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_fornecedor.place(relx=0.62, rely=0.25)
        self.et_fornecedor = CTkEntry(self.PrincFrame, font=('Arial', 12), width=200, height=30, placeholder_text='Digite o fornecedor')
        self.et_fornecedor.place(relx=0.62, rely=0.29)

        self.lbl_categoria = CTkLabel(self.PrincFrame, text='Categoria*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_categoria.place(relx=0.62, rely=0.35)
        self.categoria = StringVar()
        self.categoria.set('Acabamento')
        self.comboxCategoria = CTkComboBox(self.PrincFrame, variable=self.categoria, values=['Acabamento', 'Alvenaria'], height=30)
        self.comboxCategoria.place(relx=0.62, rely=0.39)

        self.lbl_quantidade = CTkLabel(self.PrincFrame, text='Quantidade*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_quantidade.place(relx=0.62, rely=0.45)
        self.et_quantidade = CTkEntry(self.PrincFrame, font=('Arial', 12), width=70, height=30, placeholder_text='Qtd')
        self.et_quantidade.place(relx=0.62, rely=0.49)

        self.lbl_precoUnit = CTkLabel(self.PrincFrame, text='Preço*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_precoUnit.place(relx=0.62, rely=0.55)
        self.et_precoUnit = CTkEntry(self.PrincFrame, font=('Arial', 12), width=70, height=30, placeholder_text='Preço R$')
        self.et_precoUnit.place(relx=0.62, rely=0.59)
        
        self.lbl_Data = CTkLabel(self.PrincFrame, text='Data*: ', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_Data.place(relx=0.62, rely=0.65)
        self.et_data = CTkEntry(self.PrincFrame, font=('Arial', 12), width=75, height=30, placeholder_text='dd/mm/yyyy')
        self.et_data.place(relx=0.62, rely=0.69)
        
        self.imgCalendario = CTkImage(dark_image=Image.open('.\\img\calendar.png'), size=(20, 20))
        self.btn_calendario = CTkButton(self.PrincFrame, 
                                    image=self.imgCalendario,
                                    text='', 
                                    width=40, height=22,
                                    fg_color='#FF9044',
                                    hover_color='#fa7a32',
                                    command=self.calendarioCads)
        self.btn_calendario.place(relx=0.685, rely=0.69)

        self.lbl_total = CTkLabel(self.PrincFrame, text='Total da Compra: R$', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_total.place(relx=0.62, rely=0.77)
        self.resultado = StringVar()
        self.resTotalCompra = CTkLabel(self.PrincFrame, 
                            text='', 
                            textvariable=self.resultado,
                            font=('Arial', 16, 'bold'), 
                            text_color='#fff', width=85)
        self.resTotalCompra.place(relx=0.76, rely=0.77)

        self.lbl_totalGeral = CTkLabel(self.PrincFrame, text='Total: R$', font=('Arial', 16, 'bold'), text_color='#fff')
        self.lbl_totalGeral.place(relx=0.62, rely=0.85)
        self.resFull = StringVar()
        self.resTotalGeral = CTkLabel(self.PrincFrame, 
                            text='', 
                            textvariable=self.resFull,
                            font=('Arial', 16, 'bold'), 
                            text_color='#fff', width=85)
        self.resTotalGeral.place(relx=0.68, rely=0.85)
        

    def calendarioCads(self):
        self.calen = Calendar(self.PrincFrame, fg_color='#CCC', font=('Arial', 12), locale='pt_br')
        self.calen.place(relx=0.6, rely=0.6)

        

        self.confirmaData = CTkButton(self.PrincFrame, 
                                    text='Confirmar',
                                    font=('Arial', 14, 'bold'),
                                    text_color='#fff',
                                    fg_color='#FF9044',
                                    hover_color='#fa7a32',
                                    height=20,
                                    command=self.inserirData)
        self.confirmaData.place(relx=0.74, rely=0.55)

        

appPrincipal()