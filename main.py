a = int(input("Digite o número a:"))
b = int(input("Digite o número b:"))
c = int(input("Digite o número c:"))

X = (b + c > a)
Y = (a + c > b)
Z = (a + b > c)
print(X)
print(Y)
print(Z)
if X ==False or Y==False or Z==False:
    print("Não é um triângulo")
else:
    if a == b and b == c and c == a:
        print("Equilátero")
    if a != b and b != c and c != a:
        print("Escaleno")
    if (a==b!=c) or (a==c!=b) or (a!=b==c):
        print("Isósceles")
