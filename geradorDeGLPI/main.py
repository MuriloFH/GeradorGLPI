import funcoes
import datetime

dataHora = datetime.datetime.now().strftime('%d-%m-%Y %H.%M')
print(dataHora)

arquivo = open(f'GLPI {dataHora}.txt',"a", encoding="UTF-8")

continuar = True
repetir = True
texto = ''
while continuar:
    nomeColaborador = input("Nome do colaborador: ")
    centroCusto = input("Centro de custo: ")
    codAtendimento = input("Codigo do atendimento: ")
    finalidade = input("Finalidade: ")
    nomeProduto = input("Nome do produto: ")
    nomeMunicipio = input("Municipio: ")
    meiaDiaria= input("Quantidade de meia diária: ")
    diariaInteira = input("Quantidade de diárias inteiras: ")
    data = input("Data de uso: ")

    while True:
        x = input("Cadastrar mais um? Responda s ou n: ")
        if x != 'n' and x != 'N' and x != 's' and x != 'S':
            print("Respostá incorreta!")
        if x == 's' or x == 'S':
            texto += funcoes.gerador(nomeColaborador, centroCusto, codAtendimento, finalidade, nomeProduto, nomeMunicipio, meiaDiaria, diariaInteira, data)
            break
        elif x == 'n' or x == 'N':
            texto += funcoes.gerador(nomeColaborador, centroCusto, codAtendimento, finalidade, nomeProduto, nomeMunicipio, meiaDiaria, diariaInteira, data)
            continuar = False
            break

arquivo.write(texto)
print(texto)

