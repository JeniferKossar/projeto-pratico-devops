# Arquivo: test/test.py
import sys
import os

# Permite que o Python encontre a pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import (  # type: ignore[reportMissingImports]
    calcular_total_carrinho, 
    finalizar_compra, 
    aplicar_desconto, 
    verificar_estoque, 
    status_sistema
)

# Teste 1: Valida o cálculo do carrinho
def test_calcular_total_carrinho():
    assert calcular_total_carrinho(50.0, 2) == 100.0

# Teste 2: Valida a finalização da compra
def test_finalizar_compra():
    assert finalizar_compra(True) == "Compra finalizada com sucesso"
    assert finalizar_compra(False) == "Pagamento recusado"

# Teste 3: Valida a aplicação de desconto
def test_aplicar_desconto():
    assert aplicar_desconto(100.0, True) == 90.0  # Com desconto
    assert aplicar_desconto(100.0, False) == 100.0 # Sem desconto

# Teste 4: Valida a checagem de estoque
def test_verificar_estoque():
    assert verificar_estoque(10, 5) == True   # Tem estoque
    assert verificar_estoque(2, 5) == False   # Faltou estoque

# Teste 5: Valida o status do sistema
def test_status_sistema():
    assert status_sistema() == "Online"