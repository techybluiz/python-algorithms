import json
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
        
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nnehuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()

def refazer (tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop() 
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Voce não digitou nenhuma tarefa')
        return
    print(f'{tarefa =} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()     


def ler(tarefas, caminho_arquivo):
    dados = []
    try: 
        with open(caminho_arquivo, 'r' , encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo , indent=2)
        return dados
        
CAMINHO_ARQUIVO = 'exer118.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: Listar, desfazer, refazer')
    print()
    tarefa = input('Digite a tarefa ou comando: ')
    
    if tarefa == 'listar':
        listar(tarefas)
        print(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    else:
        adicionar(tarefa , tarefas)
        listar(tarefas)
        continue
    