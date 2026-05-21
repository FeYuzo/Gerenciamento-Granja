class Cliente:
    def __init__(self, id_cliente, nome, telefone, endereco, qntd_compra_bandeija, observacoes):
        self._id_cliente = id_cliente
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco
        self._qntd_compra_bandeija = qntd_compra_bandeija
        self._observacoes = observacoes

    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, novo_id_cliente):
        self._id_cliente = novo_id_cliente

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone


    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco


    @property
    def qntd_compra_bandeija(self):
        return self._qntd_compra_bandeija
    
    @qntd_compra_bandeija.setter
    def qntd_compra_bandeija(self, nova_quantidade):
        self._qntd_compra_bandeija = nova_quantidade


    @property
    def observacoes(self):
        return self._observacoes
    
    @observacoes.setter
    def observacoes(self, nova_observacao):
        self._observacoes = nova_observacao


    def __str__(self):
        return (
            f"Cliente(id_cliente={self._id_cliente}, nome={self._nome}, telefone={self._telefone}, endereço={self._endereco}, "
            f"qntd_compra_bandeija={self._qntd_compra_bandeija}, observações={self._observacoes})"
        )
