def imprimirMatriz(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end=' ')
        print()

def salvarMatriz(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ' ')
        arqEscrita.write('\n')
    arqEscrita.close()

def salvarMatrizCSV(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ';')
        arqEscrita.write('\n')
    arqEscrita.close()


def getI(letra):
    if letra == 'A' or letra == 'a':
        return 5
    elif letra == 'B' or letra == 'b':
        return 4
    elif letra == 'C' or letra == 'c':
        return 3
    elif letra == 'D' or letra == 'd':
        return 2
    elif letra == 'E' or letra == 'e':
        return 1
    elif letra == 'F' or letra == 'f':
        return 0
    else:
        return -1

def categoria(numero):
    exe = valorBase * 2.5
    eco = valorBase * 0.9
    exit = valorBase * 1.1
    sRecl = valorBase * 0.8

    if numero >= 1 and numero <=6 and idade > 12:
        print('O valor total na classe executiva é {}'.format(exe))
    elif numero >= 1 and numero <=6 and idade < 2:
        exe = exe - (exe * 0.2)
        print('O valor total na classe executiva com desconto é {}'.format(exe))
    elif numero >= 1 and numero <=6 and idade >= 2 and idade < 12:
        exe = exe - (exe * 0.1)
        print('O valor total na classe executiva com desconto é {}'.format(exe))
    
    if numero >= 7 and numero <= 10 and idade > 12 or numero >= 14 and numero <= 28 and idade > 12:
        print('O valor total econômica é {}'.format(eco))
    elif numero >= 7 and numero <= 10 and idade < 2 or numero >= 14 and numero <= 28 and idade < 2:
        eco = eco - (eco * 0.5)
        print('O valor total econômica com desconto é {}'.format(eco))
    elif numero >= 7 and numero <= 10 and idade >= 2 and idade < 12 or numero >= 14 and numero <= 28 and idade >= 2 and idade < 12:
        eco = eco - (eco * 0.3)
        print('O valor total econômica com desconto  é {}'.format(eco))

    if numero == 12 or numero == 13 and idade > 12:
        print('O valor total na saída de emergência é {}'.format(exit))
    elif numero == 12 or numero == 13 and idade < 2:
        exit = exit - (exit * 0.3)
        print('O valor total com desconto na saída de emergência é {}'.format(exit))
    elif numero == 12 or numero == 13 and idade >= 2 and idade < 12:
        exit = exit - (exit * 0.2)
        print('O valor total com desconto na saída de emergência é {}'.format(exit))

    if numero == 11 or numero == 29 and idade > 12:
        print('O valor total sem reclinagem é {}'.format(sRecl))        
    elif numero == 11 or numero == 29 and idade < 2:
        sRecl = sRecl - (sRecl * 0.7)
        print('O valor total sem reclinagem com desconto é {}'.format(sRecl))
    elif numero == 11 or numero == 29 and idade >= 2 and idade < 12:
        sRecl = sRecl - (sRecl * 0.5)
        print('O valor total sem reclinagem com desconto é {}'.format(sRecl))

    return exe, eco, exit, sRecl

    
################################

matAssentos = [] #matriz vazia

for i in range(6): #linhas
    aux = ['[]'] * 29
    matAssentos.append(aux)

cont = 0

while cont < 29:
    letra = input('Informe a letra do assento: ')
    numero = int(input('Informe o numero do assento: '))
    idade = int(input('Informe a idade do passageiro: '))
    matAssentos[getI(letra)][numero -1] = '{}'.format(idade)

    if numero == True:
        cont = cont + 1


    imprimirMatriz(matAssentos,6,29)

    nomeArquivo = input('Digite o nome do arquivo: ')

    salvarMatriz(nomeArquivo,matAssentos,6,29)

    valorBase = int(input('Informe o valor base da passagem: '))

    categoria(numero)





#mat[fileiras.A][0] = 'X'