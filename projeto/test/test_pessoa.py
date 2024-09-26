import pytest
from projeto.models.pessoa import Pessoa


@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("marta",22)
    return pessoa

def test_pessoa_valido(pessoa_valida):
    assert pessoa_valida.nome == "marta"

def test_pessoa_valido(pessoa_valida):
    assert pessoa_valida.idade== 22

def test_pessoa_idade_negativa_retornar_messagem():
    with pytest.raises(ValueError, "a idade não pode"):
        Pessoa("marta",-1)

def test_pessoa_idade_maior_retornar_messagem():
    with pytest.raises(ValueError, "a idade não corresponde"):
        Pessoa("marta",100)
