while True:
    falta = int(input(f"quantas faltas você teve? "))
    pre = ((20 - falta) / 20) * 100
    print(f"sua frequencia em aula é: {pre}%")
    if pre >= 75:
        np1 = input(f"Digite sua NP1: ")
        np1 = np1.replace(",", ".")
        np1 = float(np1)
        np2 = input(f"Digite sua NP2: ")
        np2 = np2.replace(",", ".")
        np2 = float(np2)
        pim = input(f"Digite a nota do seu pim: ")
        pim = pim.replace(",", ".")
        pim = float(pim)
        media = (np1 * 4 + np2 * 4 + pim * 2) / 10
        exm = 10 - media

        print(f"Sua nota no NP1 é: {np1} a sua nota da NP2 é: {np2} e sua nota do pim é: {pim}")
        print(f"Sua nota final é: {media:0.2f}")

        if media < 7:
            print(f"Você precisará fazer o exame.\n")
            print(f"Você precisará tirar no mínimo: {exm:2.0f} para passar!")
            nf = float(input(f"Qual sua Nota do exame? "))
            if nf >= exm:
                print("Aprovado")
            else:
                print("Pegou DP OTÁRIO")
        else:
            print("Aprovado")
    else:
        print("Reprovado por falta")

    repetir = input("Deseja rodar o programa novamente? (s/n): ").lower()
    if repetir != "s":
        print("Programa encerrado.")
        break
