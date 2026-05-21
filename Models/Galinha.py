class Galinha:
    def __init__(self, tipo_galinha, idade, data_vacinacao, id_galinha=None):
        self._id_galinha = id_galinha
        self._tipo_galinha = tipo_galinha
        self._idade = idade
        self._data_vacinacao = data_vacinacao
        
    @property
    def id_galinha(self):
        return self._id_galinha
    
    @id_galinha.setter
    def id_galinha(self, novo_id_galinha):
        self._id_galinha = novo_id_galinha

    @property
    def tipo_galinha(self):
        return self._tipo_galinha
    @tipo_galinha.setter
    def tipo_galinha(self, novo_tipo_galinha):
        self._tipo_galinha = novo_tipo_galinha


    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = nova_idade


    @property
    def data_vacinacao(self):
        return self._data_vacinacao


    @data_vacinacao.setter
    def data_vacinacao(self, nova_data_vacinacao):
        self._data_vacinacao = nova_data_vacinacao
    
    def __str__(self):
        return f"Galinha(id_galinha={self._id_galinha}, tipo_galinha={self._tipo_galinha}, idade={self._idade}, data vacinação={self._data_vacinacao})"
