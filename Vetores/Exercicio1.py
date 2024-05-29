numbers = [];
inputNumber = int(1);
sum = int(0);

print(f'Preencha o vetor. Digite 0 para parar de inserir.');

while (inputNumber != 0):
    inputNumber = int(input('Digite: '));

    numbers.append(inputNumber);



for i in range(0 , len(numbers) , 1):
    print(numbers[i]);

    sum = sum + numbers[i];

print(f'Somatória final: {sum}');