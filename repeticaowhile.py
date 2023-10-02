#enquanto i <10 faça
i = 1
resp = 's'
while resp== 's':
    m = int(input('Digite o valor:'))
    while i <=10:
        print(i, 'x' , m , ' = ', i*m)
        i=i+1
    resp = input('Quer continuar? s/n')
    i=1