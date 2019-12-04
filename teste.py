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

def menu():
	print("Esquemas Táticos Disponíveis:\n")
	print("Digite '1' para o esquema 3-4-3\n")
	print("Digite '2' para o esquema 3-5-2\n")
	print("Digite '3' para o esquema 4-3-3\n")
	print("Digite '4' para o esquema 4-4-2\n")
	print("Digite '5' para o esquema 4-5-1\n")
	print("Digite '6' para o esquema 5-3-2\n")
	print("Digite '7' para o esquema 5-4-1\n")
	print("Digite '0' para encerrar\n")

def principal():
	menu()
	esquema = int(input("Informe o esquema desejado: "))
	while True:
		if esquema == 0:
			print("\n Encerrando...\n")
			break

		else:
			continuar = input("Efetuar nova escalação (S/N) ? ")
			if continuar == 'S' or continuar == 's':
				os.system('cls||clear')
				menu()

			else:
				print("\n Encerrando...\n")
				break


if __name__ == '__main__':
	principal()