print('ABOUT para informações.')
print('ADD para adicionar um projeto.')
print('QUIT para sair do Gestor de Portfólio')
print('LIST para listar todos os projetos.')
print('REMEMBER para relembrar os comandos')
print('UPDATE para atualizar um projeto.')
print('DELETE para remover um projeto')

import datetime
import json
ARQUIVO = 'dados.json'

def carregar_dados():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Se é sua primeira vez abrindo o programa, adicione um projeto para criar um arquivo para salvar os projetos.')
        return []
    except json.JSONDecodeError:
        print('Arquivo vazio ou corrompido!')
        return []

def salvar_dados(lista):
    try:
        with open(ARQUIVO, 'w') as f:
            return json.dump(lista, f, indent=4)
    except FileNotFoundError:
        print('Se é sua primeira vez abrindo o programa, adicione um projeto para criar um arquivo para salvar os projetos.')
        return []
    except json.JSONDecodeError:
        print('Arquivo vazio ou corrompido!')
        return []

lista = carregar_dados()

while True:
    def procurar_projeto_lista(nome, lista):
        try:
            for projeto in lista:
                if projeto['nome'] == nome:

                    return projeto
        except:
            print('Projeto não foi encontrado, digite o nome de um projeto existente.')

    def adicionar_projeto():
        try:
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
                salvar_dados(lista)

        except ValueError:
            print('Formato digitado inválido, tente novamente!')



    def listar_projetos():
        try:
            for elemento in lista:
                print('Detalhes do projeto:')
                for chave, valor in elemento.items():
                    print(f'{chave}: {valor}')
                print()
        except:
            print('Não há nenhum projeto registrado no momento, digite o comando ADD para adicionar um projeto.')


    def atualizar_projetos():
        listar_projetos()
        nome_projeto_modificar = input('Qual projeto deseja modificar?')
        projeto_modificar = procurar_projeto_lista(nome_projeto_modificar, lista)

        if projeto_modificar is not None:
            nome = input('Digite o novo nome do projeto:')
            try:
                status = bool(int(input('Finalizou o projeto? Digite 1 para sim e 0 para não')))
            except ValueError:
                print('Formato digitado inválido, tente novamente')

            projeto_modificar['nome'] = nome
            projeto_modificar['status'] = status

            data_mudanca = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            entrada_atualizacao = (
                projeto_modificar['historico'].append(data_mudanca),
                projeto_modificar['nome'],
                projeto_modificar['status']
            )
            salvar_dados(lista)



        else:
            print('Não encontrei o projeto, sem projetos para atualizar ou nome do projeto digitado errado.')

    def deletar_projetos():
        listar_projetos()
        nome_projeto_remover = input('Qual projeto deseja remover?')
        projeto_remover = procurar_projeto_lista(nome_projeto_remover, lista)
        if projeto_remover is not None:
            lista.remove(projeto_remover)
            print(f"projeto {projeto_remover['nome']} removido com sucesso!")
            salvar_dados(lista)


        else:
            print('Não encontrei o projeto, sem projetos para deletar ou nome do projeto digitado errado.')

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
        salvar_dados(lista)
        break

    elif comando == 'ADD':
        adicionar_projeto()


    elif comando == 'LIST':
        listar_projetos()


    elif comando == 'UPDATE':
        atualizar_projetos()


    elif comando == 'DELETE':
        deletar_projetos()

    else:
        print('ERRO: Comando desconhecido. Tente um comando válido!')
