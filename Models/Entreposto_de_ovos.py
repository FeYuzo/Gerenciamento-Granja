class EntrePostoOvos:
    def __init__(self, id_entreposto, cnpj, endereco, capacidade_armazenamento, quantidade_compra):
        self._id_entreposto = id_entreposto
        self._cnpj = cnpj
        self._endereco = endereco
        self._capacidade_armazenamento = capacidade_armazenamento
        self._quantidade_compra = quantidade_compra

    @property
    def id_entreposto(self):
        return self._id_entreposto
    
    @id_entreposto.setter
    def id_entreposto(self, novo_id_entreposto):
        self._id_entreposto = novo_id_entreposto

    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj


    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco


    @property
    def capacidade_armazenamento(self):
        return self._capacidade_armazenamento
    
    @capacidade_armazenamento.setter
    def capacidade_armazenamento(self, nova_capacidade):
        self._capacidade_armazenamento = nova_capacidade


    @property
    def quantidade_compra(self):
        return self._quantidade_compra
    
    @quantidade_compra.setter
    def quantidade_compra(self, nova_quantidade):
        self._quantidade_compra = nova_quantidade


    def __str__(self):
        return (
            f"EntrePostoOvos(id_entreposto={self._id_entreposto}, CNPJ={self._cnpj}, endereço={self._endereco}, "
            f"capacidade={self._capacidade_armazenamento}, quantidade_compra={self._quantidade_compra})"
        )
