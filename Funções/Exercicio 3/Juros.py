
def jurosCompostos(initial , fee , months):
    decimal_fee = (fee / 100);
    total_value = initial;

    print(f'\nValor inicial: {initial}');

    for i in range(0 , months , 1):
        total_value = total_value * (1 + decimal_fee);
        print(f'Taxa: {fee} // Valor Atual: {round(total_value , 2)}');
    
    return total_value;