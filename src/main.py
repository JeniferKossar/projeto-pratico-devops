# Arquivo: src/main.py

def calcular_total_carrinho(preco_unitario, quantidade):
    """Calcula o valor total de itens no carrinho"""
    return preco_unitario * quantidade

def finalizar_compra(pagamento_aprovado):
    """Verifica se a compra pode ser finalizada"""
    if pagamento_aprovado:
        return "Compra finalizada com sucesso"
    return "Pagamento recusado"

def aplicar_desconto(valor_total, cupom_valido):
    """Aplica 10% de desconto se o cupom for válido"""
    if cupom_valido:
        return valor_total * 0.9
    return valor_total

def verificar_estoque(quantidade_em_estoque, quantidade_solicitada):
    """Verifica se há itens suficientes no estoque"""
    return quantidade_em_estoque >= quantidade_solicitada

def status_sistema():
    """Verifica se o sistema da loja está no ar"""
    return "Online"