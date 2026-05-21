class Venda:
    def __init__(self, id_venda, codigo, data_venda, qntd_bandeijas_vendidas, qntd_caixas_vendidas, valor_bandeija, valor_caixa, id_cliente, id_entreposto, id_ovo):
        self._id_venda = id_venda
        self._codigo = codigo
        self._data_venda = data_venda
        self._qntd_bandeijas_vendidas = qntd_bandeijas_vendidas
        self._qntd_caixas_vendidas = qntd_caixas_vendidas
        self._valor_bandeija = valor_bandeija
        self._valor_caixa = valor_caixa
        self._id_cliente = id_cliente
        self._id_entreposto = id_entreposto
        self._id_ovo = id_ovo

    @property
    def id_venda(self):
        return self._id_venda
    
    @id_venda.setter
    def id_venda(self, novo_id_venda):
        self._id_venda = novo_id_venda

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self._codigo = novo_codigo

    @property
    def data_venda(self):
        return self._data_venda
    
    @data_venda.setter
    def data_venda(self, nova_data_venda):
        self._data_venda = nova_data_venda

    @property
    def qntd_bandeijas_vendidas(self):
        return self._qntd_bandeijas_vendidas
    
    @qntd_bandeijas_vendidas.setter
    def qntd_bandeijas_vendidas(self, nova_qntd):
        if nova_qntd < 0:
            raise ValueError("A quantidade de bandejas vendidas não pode ser negativa.")
        self._qntd_bandeijas_vendidas = nova_qntd

    @property
    def qntd_caixas_vendidas(self):
        return self._qntd_caixas_vendidas
    
    @qntd_caixas_vendidas.setter
    def qntd_caixas_vendidas(self, nova_qntd):
        if nova_qntd < 0:
            raise ValueError("A quantidade de caixas vendidas não pode ser negativa.")
        self._qntd_caixas_vendidas = nova_qntd

    @property
    def valor_bandeija(self):
        return self._valor_bandeija
    
    @valor_bandeija.setter
    def valor_bandeija(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor da bandeja não pode ser negativo.")
        self._valor_bandeija = novo_valor

    @property
    def valor_caixa(self):
        return self._valor_caixa
    
    @valor_caixa.setter
    def valor_caixa(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor da caixa não pode ser negativo.")
        self._valor_caixa = novo_valor

    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, novo_id_cliente):
        self._id_cliente = novo_id_cliente

    @property
    def id_entreposto(self):
        return self._id_entreposto
    
    @id_entreposto.setter
    def id_entreposto(self, novo_id_entreposto):
        self._id_entreposto = novo_id_entreposto

    @property
    def id_ovo(self):
        return self._id_ovo
    
    @id_ovo.setter
    def id_ovo(self, novo_id_ovo):
        self._id_ovo = novo_id_ovo

    def __str__(self):
        return (
            f"Venda(id_venda={self._id_venda}, codigo={self._codigo}, data_venda={self._data_venda}, "
            f"qntd_bandeijas_vendidas={self._qntd_bandeijas_vendidas}, qntd_caixas_vendidas={self._qntd_caixas_vendidas}, "
            f"valor_bandeija={self._valor_bandeija}, valor_caixa={self._valor_caixa}, id_cliente={self._id_cliente}, "
            f"id_entreposto={self._id_entreposto}, id_ovo={self._id_ovo})"
        )
