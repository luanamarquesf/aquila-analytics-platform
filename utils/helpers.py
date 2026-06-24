import random
def calculate_installments_options(amount):
    """
    Define as opções de parcelas permitidas e seus pesos 
    com base no valor total da transação.
    """
    # Compras até R$ 50,00: Sempre à vista (1x)
    if amount <= 50.0:
        options = [1]
        weights = [1.0]
        
    # Compras de R$ 50,01 até R$ 150,00: À vista ou até 3x
    elif amount <= 150.0:
        options = [1, 2, 3]
        weights = [0.60, 0.25, 0.15] # 60% à vista, 25% em 2x, 15% em 3x
        
    # Compras de R$ 150,01 até R$ 400,00: À vista ou até 6x
    elif amount <= 400.0:
        options = [1, 2, 3, 6]
        weights = [0.40, 0.20, 0.25, 0.15]
        
    # Compras acima de R$ 400,00: Permite até 12x
    else:
        options = [1, 3, 6, 12]
        weights = [0.30, 0.20, 0.30, 0.20]
        
    # Sorteia uma das opções baseado nos pesos definidos
    return random.choices(options, weights=weights, k=1)[0]