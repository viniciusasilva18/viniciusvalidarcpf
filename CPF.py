

cpf = input("Digite o CPF: ")

# Remove pontos e traços
cpf = cpf.replace(".", "").replace("-", "")

# Verificações básicas
if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF inválido")
else:
    # Primeiro dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    d1 = (soma * 10) % 11
    if d1 == 10:
        d1 = 0

    # Segundo dígito
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    d2 = (soma * 10) % 11
    if d2 == 10:
        d2 = 0

    # Resultado final
    if cpf[-2:] == str(d1) + str(d2):
        print("CPF válido")
    else:
        print("CPF inválido")
