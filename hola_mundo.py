<<<<<<< HEAD
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []

for numero in range(1, 1001):
    if es_primo(numero):
        primos.append(numero)

print(primos)

=======
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []

for numero in range(1, 1001):
    if es_primo(numero):
        primos.append(numero)

print(primos)
>>>>>>> 0e3df33d2c6f87e8d193c181b4738320f20f6e69
