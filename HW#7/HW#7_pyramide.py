# Пирамида

N = int(input('Загадайте высоту пирамиды: '))
for i in range(N+1):
    print(((2*i-1)*'*').center(2*N-1))
