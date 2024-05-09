from Distancias import kmToMiles;
from Medidas import metersToFeets;
from Temperaturas import celsiusToFahrenheit;


inputNumber = float(0);
result = float(-1);
number = float(0);


while ( result != 0 ):
    print(f'\nDigite 1 para acessar o algoritmo de temperatura.');
    print(f'Digite 2 para medidas.');
    print(f'Digite 3 para distâncias.');

    inputNumber = int(input('Digite: '));

    if ( inputNumber < 0 or inputNumber > 3 ):
        print(f'Digite apenas números presentes no menu.\n');

    else:
        number = float(input('\nDigite o valor a ser convertido: '));

        if ( inputNumber == 1 ):
            #codigo codigo
            result = celsiusToFahrenheit(number);
            print(f'\n{number}°C = {result}°F');

        if (inputNumber == 2):
            #codigo codigo
            result = metersToFeets(number);
            print(f'\n{number}m = {result} feets');
        
        if (inputNumber == 3):
            #codigo codigo
            result = kmToMiles(number);
            print(f'\n{number}km = {result} milhas');

