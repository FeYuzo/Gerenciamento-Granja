from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, id_funcionario, CPF, nome, rg, endereco, telefone, email):  
        self._id_funcionario = id_funcionario
        self._CPF = CPF
        self._nome = nome
        self._rg = rg
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        
    @property
    def id_funcionario(self):        
        return self._id_funcionario
    @id_funcionario.setter
    def id_funcionario(self, novo_id_funcionario):   
        self._id_funcionario = novo_id_funcionario

    @property
    def CPF(self):        
        return self._CPF
    @CPF.setter
    def CPF(self, novo_CPF):   
        self._CPF = novo_CPF

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def rg(self):
        return self._rg
    @rg.setter
    def rg(self, novo_rg):
        self._rg = novo_rg
    

    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco


    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone


    @property
    def email(self):
        return self._email    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email


    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return (
            f"Funcionario(id_funcionario={self._id_funcionario}, CPF={self._CPF}, nome={self._nome}, RG={self._rg}, endereço={self._endereco}, "
            f"telefone={self._telefone}, email={self._email})"
        )