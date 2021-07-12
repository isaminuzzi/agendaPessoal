def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Isadora Minuzzi Vieira                                      |')
    print('|                                                             |')
    print('| Versão 3.0 de 20/maio/2021                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    nroDaOpc=1
    for opc in mnu:
        print (nroDaOpc,') ',opc,sep='')
        nroDaOpc+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1,len(mnu)+1)])

'''
procura nom em agd e, se achou:
na posicao 0, retorna 1;
na posicao 1, retorna 2;
na posicao 2, retorna 3;
e assim por diante; MAS, se não achou e concluiu
que o lugar para inserir, mantendo a ordenacao da
lista, aquilo que foi buscado e não foi encontrado era:
a posicao 0, retorna -1;
a posicao 1, retorna -2;
a posicao 2, retorna -3;
e assim por diante.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom==agd[meio][0]:
            return meio+1 # retornamos a posição onde entramos o que buscávamos +1
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
            
    return -(inicio+1) # retornamos, negativada, a posicao onde inserir (já que não encontramos o que procurávamos) +1

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        posicao=ondeEsta(nome,agd)
        if posicao>0:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')

    posicao=-posicao
    posicao-=1
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    digitouDireito=False
    i=0
    while not digitouDireito:
        nomeBusca = input('Digite o nome do contato que deseja buscar:')
        posicao = ondeEsta(nomeBusca, agd)
        if posicao != 0:
            print('\nNome.......:',agd[i][0])
            print('Aniversário:',agd[posicao -1][opcaoAtualiza])
            print('Endereço...:',agd[posicao -1][2])
            print('Telefone...:',agd[posicao -1][3])
            print('Celular....:',agd[posicao -1][4])
            print('e-mail.....:',agd[posicao -1][5])
            digitouDireito = True
            i += 1
            #break
        else:
            print('Nome nao encontrado na lista de contato!\n')
            break
        

def atualizar (agd):
    digitouDireito=False
    i=0
    while not digitouDireito:
        nomeAtualiza = input('Digite o nome do contato que atualizar:')
        posicao = ondeEsta(nomeAtualiza, agd)
        if posicao != 0:
            print('')
            print('1.Aniversário:')
            print('2.Endereço...:')
            print('3.Telefone...:')
            print('4.Celular....:')
            print('5.e-mail.....:')
            opcaoAtualiza = int(input('Digite o numero da opcao que deseja alterar:'))
            if opcaoAtualiza > 0 and opcaoAtualiza < 6:
                valorAtualizado = str(input('Insira o novo valor:'))
                agd[posicao-1][opcaoAtualiza] = valorAtualizado
                digitouDireito = True
            

def listar (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    else:
        for contato in agd:
            print('\nNome.......:',contato[0])
            print('Aniversário:',contato[1])
            print('Endereço...:',contato[2])
            print('Telefone...:',contato[3])
            print('Celular....:',contato[4])
            print('e-mail.....:',contato[5])
        '''
        posicao=0
        while posicao<len(agd):
            print('\nNome.......:',agd[posicao][0])
            print('Aniversário:',agd[posicao][1])
            print('Endereço...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5])
            posicao+=1
        '''

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        posicao=ondeEsta(nome,agd)
        if posicao<0:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True

    posicao-=1
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa'];

opcao=None
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
