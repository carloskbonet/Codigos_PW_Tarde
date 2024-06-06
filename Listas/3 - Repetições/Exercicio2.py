intervalo_1 = int(0);
intervalo_2 = int(0);
verificar = int(0);

print('Digite 2 intervalos. O algoritmo irá exibir os números impares entre eles.');

intervalo_1 = int(input('1° : '));
intervalo_2 = int(input('2° : '));


for i in range( intervalo_1+1 , intervalo_2 , 1 ):
    
    verificar = i % 2;

    if ( verificar == 1 ):
        print(i);