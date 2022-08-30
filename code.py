# Declaração Variáveis
x = input('Deseja criar um novo usuário? ')
listau = []

# Declaração Funções

def novouser():

    usersx = input('Usuário = ')

    listau.append(usersx)
    print(listau)

    with open(r'Usuario.txt', 'w') as fp:
        for item in listau:
            fp.write("%s\n" % item)
    outrouser()

def outrouser():
    outrouser = input('Deseja criar outro usuário ?: ')
    if outrouser == 'sim' or outrouser == 's':
        novouser()
    elif outrouser == 'nao' or outrouser == 'n':
        novouserneg()
    else:
        simounao()


def novouserneg():
    x == 'nao' or x == 'n'
    print('Lista de Usuários: ', listau)


def simounao():
    print('responda apenas sim ou nao')


# Execeução
if x == 'sim' or x == 's':
    novouser()
elif x == 'n' or x == 'nao':
    novouserneg()
else:
    simounao()
