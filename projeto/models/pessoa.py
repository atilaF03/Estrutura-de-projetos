
class Pessoa:
    def __init__(self, nome: str,idade: int) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)

def _veririficar_idade (self,valor):
    if valor <0:
        raise ValueError("a idade não pode ser negativa")
    if valor > 100:
        raise ValueError(" a idade não pode ser maior que 100 vc não está vivo")
    
    self.idade = valor
    return self.idade
