print('ABOUT para informações.')
print('ADD para adicionar um projeto.')
print('QUIT para sair do Gestor de Portfólio')
print('LIST para listar todos os projetos.')
print('REMEMBER para relembrar os comandos')
print('UPDATE para atualizar um projeto.')
print('DELETE para remover um projeto')
import datetime
lista =[]

while True:
    def procurar_projeto_lista(nome, lista):

        for projeto in lista:
            if projeto['nome'] == nome:

                return projeto

    def adicionar_projeto():
        quantidade_projetos = int(input('Informe quantos projetos gostaria de cadastrar:'))

        if quantidade_projetos <= 0:
            print('Quantidade digitada invalida, tente novamente.')
        else:
            for i in range(quantidade_projetos):
                nome_projeto = input('Digite o nome do projeto:')
                print('Parabéns, novo projeto cadastrado!')
                cadastro_projeto = {
                    'nome': (f'{nome_projeto}'),
                    'status': False,
                    'historico': []
                }


                lista.append(cadastro_projeto)
    def listar_projetos():
        if lista == []:
            print('Não há nenhum projeto registrado no momento, digite o comando ADD para adicionar um projeto.')
        else:
            for elemento in lista:
                print('Detalhes do projeto:')
                for chave, valor in elemento.items():
                    print(f'{chave}: {valor}')
                print()

    def relembrar_comandos():
        print('ABOUT para informações.')
        print('ADD para adicionar um projeto.')
        print('QUIT para sair do Gestor de Portfólio')
        print('LIST para listar todos os projetos.')
        print('REMEMBER para relembrar os comandos')
        print('UPDATE para atualizar um projeto')
        print('DELETE para remover um projeto')

    def sobre_usuario():
        print('Este é o Gestor de Portfólio do Murilo')


    comando = input('Digite um comando:')
    comando = comando.upper()
    if comando == 'ABOUT':
        sobre_usuario()

    elif comando == 'REMEMBER':
        relembrar_comandos()

    elif comando == 'QUIT':
        print('Saindo do Gestor de Portfólio...Até logo!') 
        break

    elif comando == 'ADD':
        adicionar_projeto()


    elif comando == 'LIST':
        listar_projetos()


    elif comando == 'UPDATE':
        nome_projeto_modificar = input('Qual projeto deseja modificar?')
        projeto_modificar = procurar_projeto_lista(nome_projeto_modificar, lista)

        if projeto_modificar is not None:
            nome = input('Digite o novo nome do projeto:')
            status = bool(input('Finalizou o projeto? Digite 1 para sim e 0 para não'))
            projeto_modificar['nome'] = nome
            projeto_modificar['status'] = status

            data_mudanca = datetime.datetime.now()
            entrada_atualizacao = (data_mudanca,projeto_modificar['nome'], projeto_modificar['status'])
            projeto_modificar['historico'].append(entrada_atualizacao)


        else:
            print('Não encontrei o projeto')


    elif comando == 'DELETE':
        nome_projeto_remover = input('Qual projeto deseja remover?')
        projeto_remover = procurar_projeto_lista(nome_projeto_remover, lista)
        if projeto_remover is not None:
            lista.remove(projeto_remover)
            print(f"projeto {projeto_remover['nome']} removido com sucesso!")

        else:
            print('Não encontrei o projeto')


    else:
        print('ERRO: Comando desconhecido')
