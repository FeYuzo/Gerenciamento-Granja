class Rancho:
    def __init__(self, id_rancho, id_galinha, numeracao, gastos, producao):
        self._id_rancho = id_rancho
        self._id_galinha = id_galinha
        self._numeracao = numeracao
        self._gastos = gastos
        self._producao = producao
        
    @property
    def id_rancho(self):
        return self._id_rancho
    
    @id_rancho.setter
    def id_rancho(self, novo_id_rancho):
        self._id_rancho = novo_id_rancho

    @property
    def id_galinha(self):
        return self._id_galinha
    
    @id_galinha.setter
    def id_galinha(self, novo_id_galinha):
        self._id_galinha = novo_id_galinha

    @property
    def numeracao(self):
        return self._numeracao
        
    @numeracao.setter
    def numeracao(self, value):
        self._numeracao = value

    @property
    def gastos(self):
        return self._gastos

    @gastos.setter
    def gastos(self, value):
        self._gastos = value

    @property
    def producao(self):
        return self._producao

    @producao.setter
    def producao(self, value):
        if value < 0:
            raise ValueError("Produção não pode ser negativa")
        self._producao = value

    def calcular_indice_produtividade(self):
        if not isinstance(self._numeracao, (int, float)):
            raise TypeError("A numeração deve ser um valor numérico para este cálculo.")
        return self._numeracao

    def __str__(self):
        return (
            f"Rancho(id_rancho={self._id_rancho}, id_galinha={self._id_galinha}, numeracao={self._numeracao}, "
            f"gastos={self._gastos}, producao={self._producao})"
        )