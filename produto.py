class Produto:
    def __init__(self, descricao, fornecedor, quantidade, preco, total, data, idCategoria) -> None:
        #atributos
        self.__descricao = descricao
        self.__fornecedor = fornecedor
        self.__quantidade = quantidade
        self.__preco = preco
        self.__total = total
        self.__data = data
        self.__idCategoria = idCategoria
        
    #Getters e setters
    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, desc: str) -> None:
        self.__descricao = desc

    @property
    def fornecedor(self) -> str:
        return self.__fornecedor
    
    @fornecedor.setter
    def comprado(self, fornecedor: str) -> None:
        self.__fornecedor = fornecedor

    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, qtd: int) -> None:
        self.__quantidade = qtd

    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, preco:float) -> None:
        self.__preco = preco

    @property
    def total(self) -> float:
        return self.__total
    
    @total.setter
    def total(self, tot) -> None:
        self.__total = tot
        
    @property
    def data(self) -> str:
        return self.__data
    
    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    @property
    def idCategoria(self) -> int:
        return self.__idCategoria
    
    @idCategoria.setter
    def idCategoria(self, id: int) -> None:
        self.__idCategoria = id