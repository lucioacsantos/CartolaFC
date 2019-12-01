#
# Fazer um programa em  Python que CartolaFC selecione os melhores jogadores
# de cada posição e apresente conforme um esquema tático informado
#

#
# Método import
#
import sys
import os


#
# Limpando a tela
#
os.system('cls||clear')

#
# Título
#

print("\nS E L E Ç Ã O   D E   J O G A D O R E S   C A R T O L A    F C\n")

#
# Solicitando esquema tático
#

print("Esquemas Táticos Disponíveis:\n")
print("Digite '1' para o esquema 3-4-3\n")
print("Digite '2' para o esquema 3-5-2\n")
print("Digite '3' para o esquema 4-3-3\n")
print("Digite '4' para o esquema 4-4-2\n")
print("Digite '5' para o esquema 4-5-1\n")
print("Digite '6' para o esquema 5-3-2\n")
print("Digite '7' para o esquema 5-4-1\n")

try:
	esquema = int(input("Informe o esquema desejado: "))
	print()
	#
	# Apresentando maiores pontuadores de cada posição conforme esquema tático
	#

	if esquema == 1:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("3-4-3")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 3-4-3\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num'],
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos; e\n {9}, do {10}, com {11:.2f} pontos.\n'
		    .format(
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num'],
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num']
		    	))
		print('Os Atacantes selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num'],
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 2:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("3-5-2")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 3-5-2\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num'],
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos;\n {9}, do {10}, com {11:.2f} pontos; e\n {12}, do {13}, com {14:.2f} pontos.\n'
		    .format(
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num'],
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num'],
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num']
		    	))
		print('Os Atacantes selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 3:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("4-3-3")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 4-3-3\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Laterais selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num']
		    	))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num'],
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num']
		    	))
		print('Os Atacantes selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num'],
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 4:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("4-4-2")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 4-4-2\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Laterais selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num']
		    	))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num'],
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos; e\n {9}, do {10}, com {11:.2f} pontos.\n'
		    .format(
		    	
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num'],
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num']
		    	))
		print('Os Atacantes selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 5:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("4-5-1")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 4-5-1\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Laterais selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num']
		    	))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num'],
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos;\n {6}, do {7}, com {8:.2f} pontos; e\n {9}, do {10}, com {11:.2f} pontos; e\n {12}, do {13}, com {14:.2f} pontos.\n'
		    .format(
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num'],
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num'],
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num'],
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num']
		    	))
		print('O Atacantes selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 6:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("5-3-2")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 5-3-2\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Laterais selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num']
		    	))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos; \n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num'],
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num'],
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num'],
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num']
		    	))
		print('O Atacantes selecionado é:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num'],
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	elif esquema == 7:
		os.system('cls||clear')
		print("\nProcessando...\n")
		import cartolafc_function
		selecao = cartolafc_function.select_esquema("5-4-1")
		os.system('cls||clear')
		print("\nO esquema tático escolhido foi 5-4-1\n")
		print('O Goleiro selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[0]['apelido'],selecao[0]['nome_clube'],selecao[0]['jogos_num'] * selecao[0]['media_num']))
		print('Os Laterais selecionados são:\n {0}, do {1}, com {2:.2f} pontos; e\n {3}, do {4}, com {5:.2f} pontos.\n'
		    .format(
		    	selecao[1]['apelido'],selecao[1]['nome_clube'],selecao[1]['jogos_num'] * selecao[1]['media_num'],
		    	selecao[2]['apelido'],selecao[2]['nome_clube'],selecao[2]['jogos_num'] * selecao[2]['media_num']
		    	))
		print('Os Zagueiros selecionados são:\n {0}, do {1}, com {2:.2f} pontos; \n {3}, do {4}, com {5:.2f} pontos; e\n {6}, do {7}, com {8:.2f} pontos.\n'
		    .format(
		    	selecao[3]['apelido'],selecao[3]['nome_clube'],selecao[3]['jogos_num'] * selecao[3]['media_num'],
		    	selecao[4]['apelido'],selecao[4]['nome_clube'],selecao[4]['jogos_num'] * selecao[4]['media_num'],
		    	selecao[5]['apelido'],selecao[5]['nome_clube'],selecao[5]['jogos_num'] * selecao[5]['media_num']
		    	))
		print('Os Meias selecionados são:\n {0}, do {1}, com {2:.2f} pontos;\n {3}, do {4}, com {5:.2f} pontos; \n {6}, do {7}, com {8:.2f} pontos; e\n {9}, do {10}, com {11:.2f} pontos.\n'
		    .format(
		    	selecao[6]['apelido'],selecao[6]['nome_clube'],selecao[6]['jogos_num'] * selecao[6]['media_num'],
		    	selecao[7]['apelido'],selecao[7]['nome_clube'],selecao[7]['jogos_num'] * selecao[7]['media_num'],
		    	selecao[8]['apelido'],selecao[8]['nome_clube'],selecao[8]['jogos_num'] * selecao[8]['media_num'],
		    	selecao[9]['apelido'],selecao[9]['nome_clube'],selecao[9]['jogos_num'] * selecao[9]['media_num']
		    	))
		print('O Atacantes selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(
		    	
		    	selecao[10]['apelido'],selecao[10]['nome_clube'],selecao[10]['jogos_num'] * selecao[10]['media_num']
		    	))
		print('E o Técnico selecionado é:\n {0}, do {1}, com {2:.2f} pontos.\n'
		    .format(selecao[11]['apelido'],selecao[11]['nome_clube'],selecao[11]['jogos_num'] * selecao[11]['media_num']))

	else: print("\nFornecida opção inválida, tente novamente.\n")

except:
	print("\nFornecida opção inválida, tente novamente.\n")