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

def getI(letra): #getI o que significa isso?
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
    executivo = valorBase * 2.5
    economica = valorBase * 0.9
    exit = valorBase * 1.1 # essa variavel deveria ter outro nome
    semReclinagem = valorBase * 0.8

    # if numero >= 1:
    #     if numero <= 6:
    #         if idadePassageiro > 12:
    #             print('O valor total na classe executiva é {}'.format(executivo))
    #         else:
    #             print('O valor total na classe executiva é {}'.format(executivo))
    #     else:
    #         print('O valor total na classe executiva é {}'.format(executivo))
    # else:
    #      print('O valor total na classe executiva é {}'.format(executivo))
    if idadePassageiro < 2:
        executivo = executivo - (executivo * 0.2) 
        print('O valor total na classe executiva é {}'.format(executivo))
        if idadePassageiro >= 2:
            executivo = executivo - (executivo * 0.1)
            print('O valor total na classe executiva com desconto é {}'.format(executivo))
            if idadePassageiro < 12:
               executivo = executivo - (executivo * 0.1)
               print('O valor total na classe executiva com desconto é {}'.format(executivo))
        
    if numero >= 1 and numero <=6 and idadePassageiro > 12:
        print('O valor total na classe executiva é {}'.format(executivo))
    elif numero >= 1 and numero <=6 and idadePassageiro < 2:
        executivo = executivo - (executivo * 0.2)
        print('O valor total na classe executiva com desconto é {}'.format(executivo))
    elif numero >= 1 and numero <=6 and idadePassageiro >= 2 and idadePassageiro < 12:
        executivo = executivo - (executivo * 0.1)
        print('O valor total na classe executiva com desconto é {}'.format(executivo))
    
    if numero >= 7 and numero <= 10 and idadePassageiro > 12 or numero >= 14 and numero <= 28 and idadePassageiro > 12:
        print('O valor total econômica é {}'.format(economica))
    elif numero >= 7 and numero <= 10 and idadePassageiro < 2 or numero >= 14 and numero <= 28 and idadePassageiro < 2:
        economica = economica - (economica * 0.5)
        print('O valor total econômica com desconto é {}'.format(economica))
    elif numero >= 7 and numero <= 10 and idadePassageiro >= 2 and idadePassageiro < 12 or numero >= 14 and numero <= 28 and idadePassageiro >= 2 and idadePassageiro < 12:
        economica = economica - (economica * 0.3)
        print('O valor total econômica com desconto  é {}'.format(economica))

    if numero == 12 or numero == 13 and idadePassageiro > 12:
        print('O valor total na saída de emergência é {}'.format(exit))
    elif numero == 12 or numero == 13 and idadePassageiro < 2:
        exit = exit - (exit * 0.3)
        print('O valor total com desconto na saída de emergência é {}'.format(exit))
    elif numero == 12 or numero == 13 and idadePassageiro >= 2 and idadePassageiro < 12:
        exit = exit - (exit * 0.2)
        print('O valor total com desconto na saída de emergência é {}'.format(exit))

    if numero == 11 or numero == 29 and idadePassageiro > 12:
        print('O valor total sem reclinagem é {}'.format(semReclinagem))        
    elif numero == 11 or numero == 29 and idadePassageiro < 2:
        semReclinagem = semReclinagem - (semReclinagem * 0.7)
        print('O valor total sem reclinagem com desconto é {}'.format(semReclinagem))
    elif numero == 11 or numero == 29 and idadePassageiro >= 2 and idadePassageiro < 12:
        semReclinagem = semReclinagem - (semReclinagem * 0.5)
        print('O valor total sem reclinagem com desconto é {}'.format(semReclinagem))

    return executivo, economica, exit, semReclinagem
################################

matAssentos = [] #matriz vazia

for i in range(6): #linhas
    aux = ['[]'] * 29
    matAssentos.append(aux)


letra = input('Informe a letra do assento (a-f): ')
numero = int(input('Informe o número do assento (1-29): '))
idadePassageiro = int(input('Informe a idade do passageiro: '))
matAssentos[getI(letra)][numero -1] = idadePassageiro



imprimirMatriz(matAssentos,6,29)

nomeArquivo = input('Digite o nome do arquivo: ')

salvarMatriz(nomeArquivo,matAssentos,6,29)

valorBase = int(input('Informe o valor base da passagem: '))
categoria(numero)
                           






#mat[fileiras.A][0] = 'X'