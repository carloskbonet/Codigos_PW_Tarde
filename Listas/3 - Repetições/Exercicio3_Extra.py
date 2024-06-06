inputText = str('');
count = int(0);
vogais = ['a' , 'e' , 'i' , 'o' , 'u'];

print(f'Digite um texto. O código contará quantas vogais foram digitadas.');

inputText = input('Digite: ');

# Processamento

print(f'\nTexto digitado : {inputText}\n');

for word in (inputText.lower()) :
    
    if ( word in vogais ):
        count = count + 1;



# Output
print(f'Quantidade de Vogais: {count}');