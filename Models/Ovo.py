class Ovo:
    def __init__(self, id_ovo, id_galinha, categoria, tamanho, tipo_ovo):
        self._id_ovo = id_ovo
        self._id_galinha = id_galinha
        self._categoria = categoria      
        self._tamanho = tamanho           
        self._tipo_ovo = tipo_ovo         
    
    @property
    def id_ovo(self):
        return self._id_ovo
    @id_ovo.setter
    def id_ovo(self, novo_id_ovo):
        self._id_ovo = novo_id_ovo

    @property
    def id_galinha(self):
        return self._id_galinha
    @id_galinha.setter
    def id_galinha(self, novo_id_galinha):
        self._id_galinha = novo_id_galinha

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria


    @property
    def tamanho(self):
        return self._tamanho
    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self._tamanho = novo_tamanho


    @property
    def tipo_ovo(self):
        return self._tipo_ovo
    @tipo_ovo.setter
    def tipo_ovo(self, novo_tipo_ovo):
        self._tipo_ovo = novo_tipo_ovo


    def __str__(self):
        return (
            f"Ovo(id_ovo={self._id_ovo}, id_galinha={self._id_galinha}, categoria={self._categoria}, "
            f"tamanho={self._tamanho}, tipo_ovo={self._tipo_ovo})"
        )
