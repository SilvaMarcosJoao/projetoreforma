from libs import *
import produto

class Conectivos(produto.Produto):
    prod = produto.Produto()
    codigo = None
    def inserirData(self):
        """
        Insere no entry, a data selecionada no calendário.
        :return: Não há retorno.
        """
        self.data = self.calen.get_date()
        if len(self.data) == 0 or len(self.data) != 0:
            self.calen.destroy()
        self.et_data.delete(0, END)
        self.et_data.insert(0, self.data)
        self.confirmaData.destroy()

    def inserirProduto(self):
        """
        Captura os dados digitados e  envia ao método de cadastro utilizado pelo objeto da classe Produto.
        :param: Não há parâmetro.
        :return: Não há retorno. 
        """
        try:
            if (len(self.et_descricao.get()) == 0 or 
                len(self.et_fornecedor.get()) == 0 or 
                self.et_quantidade.get() == 0 or 
                self.et_precoUnit.get() == 0 or
                len(self.categoria.get()) == 0 or
                len(self.et_data.get()) == 0):
                messagebox.showwarning('Alerta', 'Por favor preencha os campos obrigatórios')
            elif len(self.et_descricao.get()) > 120:
                messagebox.showwarning('Atenção', 'Preencha a descrição corretamente')
            elif len(self.et_fornecedor.get()) > 40:
                messagebox.showwarning('Atenção', 'Campo de fornecedor com tamnho maior que o permitido')
            elif len(self.et_data.get()) > 10:
                messagebox.showwarning('Atenção', 'Preencha a data corretamente')
            else:
                self.prod.set_descricao(self.et_descricao.get())
                self.prod.set_fornecedor(self.et_fornecedor.get())
                self.prod.set_quantidade(self.et_quantidade.get())
                self.prod.set_preco(self.et_precoUnit.get())
                if self.categoria.get() == 'Acabamento':
                    self.prod.set_idCategoria(1)
                elif self.categoria.get() == 'Alvenaria':
                    self.prod.set_idCategoria(2)
                self.prod.set_data(self.et_data.get())
                self.prod.set_total(float(self.prod.get_preco()) * int(self.prod.get_quantidade()))
                self.prod.cadastrar(
                                self.prod.get_descricao(), 
                                self.prod.get_fornecedor(), 
                                self.prod.get_quantidade(), 
                                self.prod.get_preco(), 
                                self.prod.get_total(),
                                self.prod.get_data(),
                                self.prod.get_idCategoria())
                messagebox.showinfo('Sistema', 'Produto cadastrado com sucesso!')
                self.exibirProdutos()
        except Exception as erro:
            messagebox.showerror('Erro', 'Houve um erro no cadastro do produto')
            print(erro)
        self.limpa_campos_produto()

    def exibirProdutos(self):
        """
        Exibi todos os produtos.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.treeLista.delete(*self.treeLista.get_children())
        self.listaProdutos = self.prod.listarProdutos()
        try:
            if len(self.listaProdutos) == 0:
                messagebox.showwarning('Atenção', 'Não há produtos cadastrados')
            else:
                self.soma = 0.0
                for p in self.listaProdutos:
                    self.treeLista.insert('',END, values=p)
                    self.soma +=float(p[5])
                    print(p)
                self.resFull.set(f'{self.soma:.2f}')
        except Exception as erro:
            messagebox.showerror('Erro', 'Houve um erro na exibição de produtos', erro)
            print(erro)

    def buscarProduto(self):
        """
        Realiza a captura da descrição digitada e envia ao método de consulta utilizado pelo
        objeto da classe Produto, onde este, retornará os itens de acordo com a descrição.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.descricaoProd = self.et_consulta.get()
        try:
            if len(self.descricaoProd) == 0:
                messagebox.showwarning('Atenção', 'Preencha o campo de busca para consultar')
            else:
                self.treeLista.delete(*self.treeLista.get_children())
                self.busca = self.prod.listarProduto(self.descricaoProd)
                if len(self.busca) == 0:
                    messagebox.showwarning('Atenção', 'Nenhum produto encontrado')
                else:
                    for b in self.busca:
                        self.treeLista.insert('', END, values=b)
        except Exception as erro:
            messagebox.showerror('Erro', 'Não foi possível buscar produtos')
            print(erro)
        self.limpa_campos_produto()

    def buscarPorCategoria(self):
        """
        Realiza a captura do id digitado e envia ao método de consulta por categoria utilizado pelo
        objeto da classe Produto, onde este, retornará os dados requeridos.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.idCat = int(self.et_consultaCategoria.get())
        try:
            if self.idCat == 0:
                messagebox.showwarning('Atenção', 'Preencha o campo de busca por categoria para consultar')
            else:
                self.idCat = int(self.idCat)
                self.treeLista.delete(*self.treeLista.get_children())
                self.resCat = self.prod.listarPorCategoria(self.idCat)
                print(self.resCat)
                if len(self.resCat) == 0:
                    messagebox.showwarning('Atenção', 'Nenhum produto encontrado')
                else:
                    for r in self.resCat:
                        self.treeLista.insert('', END, values=r)
        except Exception as er:  
            messagebox.showerror('Erro', 'Não foi possível buscar por categoria')
            print(er)
        self.limpa_campos_produto()

    def editarProduto(self):
        """
        Captura os dados digitados e  envia ao método de alteração utilizado pelo objeto da classe Produto, onde este, 
        alterado um item específico de acordo com os novos dados passados.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.identicadorProduto = self.codigo
        try:
            if (len(self.et_descricao.get()) == 0 or 
                len(self.et_fornecedor.get()) == 0 or 
                self.et_quantidade.get() == 0 or 
                self.et_precoUnit.get() == 0 or
                len(self.categoria.get()) == 0 or
                len(self.et_data.get()) == 0):
                messagebox.showwarning('Alerta', 'Por favor preencha os campos obrigatórios')
            elif len(self.et_descricao.get()) > 120:
                messagebox.showwarning('Atenção', 'Preencha a descrição corretamente')
            elif len(self.et_fornecedor.get()) > 40:
                messagebox.showwarning('Atenção', 'Campo de fornecedor com tamanho maior que o permitido')
            elif len(self.et_data.get()) > 10:
                messagebox.showwarning('Atenção', 'Preencha a data corretamente')
            else:
                self.prod.set_descricao(self.et_descricao.get())
                self.prod.set_fornecedor(self.et_fornecedor.get())
                self.prod.set_quantidade(self.et_quantidade.get())
                self.prod.set_preco(self.et_precoUnit.get())
                if self.categoria.get() == 'Acabamento':
                    self.prod.set_idCategoria(1)
                elif self.categoria.get() == 'Alvenaria':
                    self.prod.set_idCategoria(2)
                self.prod.set_data(self.et_data.get())
                self.prod.set_total(float(self.et_precoUnit.get()) * int(self.et_quantidade.get()))
                self.prod.alterarProduto(self.identicadorProduto, 
                                self.prod.get_descricao(), 
                                self.prod.get_fornecedor(), 
                                self.prod.get_quantidade(), 
                                self.prod.get_preco(), 
                                self.prod.get_total(),
                                self.prod.get_data(),
                                self.prod.get_idCategoria())
                messagebox.showinfo('Sistema', 'Produto alterado com sucesso!')
                self.exibirProdutos()
        except Exception as e:
            messagebox.showerror('Erro', 'Houve um erro na alteração do produto')
            print(e)
        self.limpa_campos_produto()

    def deletarProduto(self):
        """
        De acordo com o produto selecionado, envia o id deste produto ao método de deleção utilizado
        pelo objeto da classe produto, que fará a exclusão do item. 
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.idProd = self.codigo
        try:
            if not self.treeLista.selection():
                messagebox.showwarning('Alerta', 'Selecione algum produto para excluir')
            else:
                self.prod.excluirProduto(self.idProd)
                messagebox.showinfo('Sistema', 'Produto excluido com sucesso!')
                self.limpa_campos_produto()
                self.exibirProdutos()
        except:
            messagebox.showerror('Erro', 'Não foi possível deletar o cliente')

    def duplo_clique_produto(self, event):
        """
        Ao clicar duas vezes em um item, este, terá seus dados exibidos em seus respectivos campos.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.limpa_campos_produto()
        self.itemSelecionado = self.treeLista.selection()
        self.selecionados = list(self.treeLista.item(self.itemSelecionado, 'values'))
        self.codigo = int(self.selecionados[0])
        self.et_descricao.insert(0, self.selecionados[1])
        self.et_fornecedor.insert(0, self.selecionados[2])
        self.et_quantidade.insert(0, self.selecionados[3])
        self.et_precoUnit.insert(0, f'{float(self.selecionados[4]):.2f}')
        self.resultado.set(f'{float(self.selecionados[5]):.2f}')
        
        self.et_data.insert(0, self.selecionados[6])
        if int(self.selecionados[7]) == 1:
            self.categoria.set('Acabamento')
        elif int(self.selecionados[7]) == 2:
            self.categoria.set('Alvenaria')


    def limpa_campos_produto(self):
        """
        Realiza a limpeza dos campos de cadastro de produto.
        :param: Não há parâmetro.
        :return: Não há retorno.
        """
        self.et_descricao.delete(0,END)
        self.et_fornecedor.delete(0,END)
        self.et_quantidade.delete(0,END)
        self.et_precoUnit.delete(0,END)
        self.et_data.delete(0,END)
        self.et_consultaCategoria.delete(0, END)
        self.et_consulta.delete(0, END)
        self.resultado.set('')
