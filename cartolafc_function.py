#
# Biblioteca de funções CartolaFC
#

#
# Método import
#
import sys
import os
import datetime
import requests
import json
import urllib.request

#
# Contatando a API do CartolaFC
#
horaInicial = datetime.datetime.now()

print("\nContatando API do CartolaFC...\n")

#with urllib.request.urlopen("https://api.cartolafc.globo.com/atletas/mercado") as url:
#    data = json.loads(url.read().decode())

data = requests.get('https://api.cartolafc.globo.com/atletas/mercado', verify=True).json()

horaFinal= datetime.datetime.now()
tempoGasto = horaFinal - horaInicial

print('\nPronto em: {0}\n'.format(tempoGasto))

#
# Leitura e preparação dos dados de mercado.json
#

horaInicial = datetime.datetime.now()
print("\nPreparando dados...\n")

#cartola = open('/home/lacs/Documentos/mercado.json', 'r')
#cartola_json = json.loads(cartola.read())
cartola_json = data
clubes = cartola_json['clubes']
atletas = cartola_json['atletas']
posicoes = cartola_json['posicoes']
status = cartola_json['status']

print("\nCalculando pontuação dos atletas e técnicos...\n")

atletas = sorted (atletas, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)

#
# Listas por posição com os atletas
#

print("\nOrganizando atletas mais pontuados por posição...\n")

for a in atletas:
    goleiros = [a for a in atletas if a["posicao_id"] == 1]
    laterais = [a for a in atletas if a["posicao_id"] == 2]
    zagueiros = [a for a in atletas if a["posicao_id"] == 3]
    meias = [a for a in atletas if a["posicao_id"] == 4]
    atacantes = [a for a in atletas if a["posicao_id"] == 5]
    tecnicos = [a for a in atletas if a["posicao_id"] == 6]

horaFinal= datetime.datetime.now()
tempoGasto = horaFinal - horaInicial

print('\nPronto em: {0}\n'.format(tempoGasto))

#
# Seleção dos cinco maiores pontuadores por posição
#
"""
goleiros = sorted (goleiros, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:1]
laterais = sorted (laterais, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:2]
zagueiros = sorted (zagueiros, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:5]
meias = sorted (meias, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:5]
atacantes = sorted (atacantes, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:3]
tecnicos = sorted (tecnicos, key=lambda a: a['jogos_num'] * a['media_num'],reverse=True)[0:1]
"""

#
# Função menu
#

def menu():
    print("Esquemas Táticos Disponíveis:\n")
    print("Digite '1' para o esquema 3-4-3\n")
    print("Digite '2' para o esquema 3-5-2\n")
    print("Digite '3' para o esquema 4-3-3\n")
    print("Digite '4' para o esquema 4-4-2\n")
    print("Digite '5' para o esquema 4-5-1\n")
    print("Digite '6' para o esquema 5-3-2\n")
    print("Digite '7' para o esquema 5-4-1\n")

#
# Função para selecionar jogadores de cada posição
#
def jogador(posicao,qtde=0):
    if posicao == "goleiros":
        jogador = (goleiros[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador
    
    if posicao == "tecnicos":
        jogador = (tecnicos[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador
    
    if posicao == "laterais":
        jogador = (laterais[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador

    if posicao == "zagueiros":
        jogador = (zagueiros[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador

    if posicao == "meias":
        jogador = (meias[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador

    if posicao == "atacantes":
        jogador = (atacantes[qtde])
        clube = [c["nome"] for c in clubes.values() if c["id"] == jogador["clube_id"]][0]
        jogador["nome_clube"] = clube
        return jogador


# Função para selecionar jogadores conforme o esquema
def select_esquema(esquema):

    if esquema == "3-4-3":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 2:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 3:
            selecao.append(jogador("meias", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("atacantes", cont))
            cont += 1
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "3-5-2":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 2:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 4:
            selecao.append(jogador("meias", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("atacantes", cont))
            cont += 1
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "4-3-3":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 1:
            selecao.append(jogador("laterais", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("meias", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("atacantes", cont))
            cont += 1
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "4-4-2":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 1:
            selecao.append(jogador("laterais", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 3:
            selecao.append(jogador("meias", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("atacantes", cont))
            cont += 1
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "4-5-1":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 1:
            selecao.append(jogador("laterais", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 4:
            selecao.append(jogador("meias", cont))
            cont += 1
        selecao.append(jogador("atacantes"))
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "5-3-2":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 1:
            selecao.append(jogador("laterais", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("meias", cont))
            cont += 1
        cont = 0
        while cont <= 1:
            selecao.append(jogador("atacantes", cont))
            cont += 1
        selecao.append(jogador("tecnicos"))
        return selecao

    if esquema == "5-4-1":
        selecao = []
        selecao.append(jogador("goleiros"))
        cont = 0
        while cont <= 1:
            selecao.append(jogador("laterais", cont))
            cont += 1
        cont = 0
        while cont <= 2:
            selecao.append(jogador("zagueiros", cont))
            cont += 1
        cont = 0
        while cont <= 3:
            selecao.append(jogador("meias", cont))
            cont += 1
        selecao.append(jogador("atacantes"))
        selecao.append(jogador("tecnicos"))
        return selecao



"""
selecao = select_esquema("3-4-3")
os.system('cls||clear')
print("\nO esquema tático escolhido foi 3-4-3\n")
print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
    .format(selecao[0]['nome'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
    .format(
        selecao[1]['nome'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
        selecao[2]['nome'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num'],
        selecao[3]['nome'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num']
        ))
print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos; e\n {9}, do {10}, com {11:.2f} pontos.\n'
    .format(
        selecao[4]['nome'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num'],
        selecao[5]['nome'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
        selecao[6]['nome'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
        selecao[7]['nome'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num']
        ))
print('Os Atacantes selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
    .format(
        selecao[8]['nome'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num'],
        selecao[9]['nome'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
        selecao[10]['nome'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
        ))
print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
    .format(selecao[11]['nome'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))


selecao = select_esquema("4-4-2")
print(selecao)

"""