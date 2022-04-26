texto = ''
def gerador(nomeColaborador, centroCusto, codAtendimento, finalidade, nomeProduto, nomeMunicipio, meiaDiaria, diariaInteira, data):
    texto=(f'''
Meia Diária - {nomeColaborador}

Nome do Colaborador :{nomeColaborador}
Centro de Custo: {centroCusto}
Código do Atendimento (Jira): {codAtendimento}
Projeto: "{finalidade}" / "{nomeProduto}" / "{nomeMunicipio}"

__________
Alimentação:

Quantidade de Meia Diária: {meiaDiaria}
Quantidade de Diária: {diariaInteira}
Data: {data}

-------------------------------------------------------------------------------
    ''')
    return texto
