import pyautogui
import json
import os

pyautogui.PAUSE = 2
# pyautogui.FAILSAFE = True


def salvar_Pos_Farm(Battle_Button, Battle_Base_Hunt, Battle_One_Liner, Battle_Two_Liner, Kill_Button_Offset=130):
    Battle_Button_list = list(Battle_Button)
    Battle_Base_Hunt_list = list(Battle_Base_Hunt)
    Battle_One_Liner_list = list(Battle_One_Liner)
    Battle_Two_Liner_list = list(Battle_Two_Liner)

    with open("config_Farm_pos.json", "W") as jsonFile:
        json.dump({
            "Battle_Button": Battle_Button_list,
            "Battle_Base_Hunt": Battle_Base_Hunt_list,
            "Battle_One_Liner": Battle_One_Liner_list,
            "Battle_Two_Liner": Battle_Two_Liner_list,
            "Kill_Button_Offset": '"'+Kill_Button_Offset+'"'
        }, jsonFile, indent=4)
        print("Posições salvas")


def salvar_Farm(LvCombate, LvCacada, PorcentagemCombate, PorcentagemCacada, MapaAtual, speed=1, mobs=2, kills=6):
    with open("config_farm.json", "w") as jsonFile:
        jsonFile.write("{\n")
        jsonFile.write("  \"speed\": " + str(speed) + ",\n")
        jsonFile.write("  \"mobs\": " + str(mobs) + ",\n")
        jsonFile.write("  \"kills\": " + str(kills) + ",\n")
        jsonFile.write("  \"LvCombate\": " + str(LvCombate) + ",\n")
        jsonFile.write("  \"LvCacada\": " + str(LvCacada) + ",\n")
        jsonFile.write("  \"PorcentagemCombate\": " +
                       str(PorcentagemCombate) + ",\n")
        jsonFile.write("  \"PorcentagemCacada\": " +
                       str(PorcentagemCacada) + ",\n")
        jsonFile.write("  \"MapaAtual\": " + str(MapaAtual) + "\n")
        jsonFile.write("}\n")
    print("Configurações salvas")


def salvar_Pos_Cacada(Battle_Button, Battle_Base_Hunt, Battle_One_Liner, Battle_Two_Liner):
    # Convert tuples to lists before writing JSON
    Battle_Button_list = list(Battle_Button)
    Battle_Base_Hunt_list = list(Battle_Base_Hunt)
    Battle_One_Liner_list = list(Battle_One_Liner)
    Battle_Two_Liner_list = list(Battle_Two_Liner)

    with open("config_Hunt_pos.json", "w") as jsonFile:
        # Write the dictionary with lists as values
        json.dump({
            "Battle_Button": Battle_Button_list,
            "Battle_Base_Hunt": Battle_Base_Hunt_list,
            "Battle_One_Liner": Battle_One_Liner_list,
            "Battle_Two_Liner": Battle_Two_Liner_list
        }, jsonFile, indent=4)
        print("Posições salvas")


def salvar_Cacada(speed=1, mobs=2, espera=60, pool="n", linhasPrevias=0):
    # salvar como Json
    # abrir o arquivo
    with open("config_caca.json", "w") as jsonFile:
        # escrever as configurações
        jsonFile.write("{\n")
        jsonFile.write("  \"speed\": " + str(speed) + ",\n")
        jsonFile.write("  \"mobs\": " + str(mobs) + ",\n")
        jsonFile.write("  \"espera\": " + str(espera) + ",\n")
        # Add closing quotation mark
        jsonFile.write("  \"pool\": \"" + pool + "\",\n")
        jsonFile.write("  \"linhasPrevias\": " + str(linhasPrevias) + "\n")
        jsonFile.write("}\n")
    print("Configurações salvas")


def configurar():
    print("o que quer configurar? \n1 - Posições de caçada \n2 - Configurações de caçada \n3 - Posições de Farm \n4 - Configurações de Farm")
    opcao = int(input("Digite a opção desejada: "))
    # To Do agora!
    if opcao == 1:
        print("Configurando Posições de Caçada:")
        confirma = input("Deseja usar as posições padrão? s ou n: ")
        if confirma == "s":
            Battle_button = (74, 880)
            Battle_Base_Hunt = (872, 269)
            Battle_One_Liner = (1146, 225)
            Battle_Two_Liner = (1146, 310)
            salvar_Pos_Cacada(Battle_button, Battle_Base_Hunt,
                              Battle_One_Liner, Battle_Two_Liner)
        else:
            tempo = 7
            print("A cada "+str(tempo)+" segundos o programa irá salvar uma posição na tela sendo elas em ordem:\n1 - Botão de navegação para Batalha\n2- Botão para Caçada (situação onde nenhum monstro foi caçado)\n3 - Botão de caçada (será necessário uma escolha)")
            confirmacao = input(
                "Deseja alterar a pos do botão de navegação? s ou n: ")
            if confirmacao == "s":
                print("Aguarde "+str(tempo)+" segundos")
                pyautogui.sleep(tempo)
                Battle_button = pyautogui.position()
            else:
                Battle_button = (74, 880)
            confirmacao = "potato"
            confirmacao = input(
                "Deseja alterar a pos do botão de caçada (central)? s ou n: ")
            if confirmacao == "s":
                print("Aguarde "+str(tempo)+" segundos")
                pyautogui.sleep(tempo)
                Battle_Base_Hunt = pyautogui.position()
            else:
                Battle_Base_Hunt = (872, 269)
            confirmacao = "potato"
            confirmacao = input(
                "Deseja alterar a pos do botão de caçada? s ou n: ")
            if confirmacao == "s":
                quantidade = input(
                    "Quantos Mobs aparecem? menos que 8 ou 9 a 16?")
                if quantidade == 1:
                    print("Aguarde "+str(tempo)+" segundos")
                    pyautogui.sleep(tempo)
                    Battle_One_Liner = pyautogui.position()
                    Battle_Two_Liner = Battle_One_Liner[0], Battle_One_Liner[1]+55
                if quantidade == 2:
                    print("Aguarde "+str(tempo)+" segundos")
                    pyautogui.sleep(tempo)
                    Battle_Two_Liner = pyautogui.position()
                    Battle_One_Liner = Battle_Two_Liner[0], Battle_Two_Liner[1]-55
            else:
                Battle_One_Liner = (1146, 225)
                Battle_Two_Liner = (1146, 310)
            print("Salvando...")
            salvar_Pos_Cacada(Battle_button, Battle_Base_Hunt,
                              Battle_One_Liner, Battle_Two_Liner)

    # Feito
    if opcao == 2:
        print("Configurando Caçada:")
        print("A velocidade da sua máquina ou internet")
        print(" 1 - rápida \n2 - normal \n3 - lenta")
        speed = int(input("Digite a opção desejada: "))
        print("Quantos Mobs você acha por vez?")
        print("1 - 8 ou menos \n2 - Entre 9 e 16")
        mobs = int(input("Digite a opção desejada: "))
        print("Quanto tempo de caçada?")
        print("Em segundos")
        espera = int(input("Digite o tempo total de caçada: "))
        print("Já existem Mobs caçados?")
        pool = input("Digite s ou n: ")
        if pool == "s":
            print("Quantos Mobs já estão caçados?")
            linhasPrevias = int(input("Digite o número de linhas: "))
        else:
            linhasPrevias = 0
        print("Configuração completa")
        print("Velocidade: ", speed)
        print("Mobs por vez: ", mobs)
        print("Tempo de caçada: ", espera)
        print("Mobs caçados: ", pool)
        print("Linhas caçadas: ", linhasPrevias)
        salvar = input("Deseja salvar as configurações? s ou n: ")
        if salvar == "s":
            salvar_Cacada(speed, mobs, espera, pool, linhasPrevias)
        else:
            print("Configurações não salvas, saindo")
    # Todo
    if opcao == 3:
        pass
    # Feito
    if opcao == 4:
        print("Configurando Farm:")
        print("A velocidade da sua máquina ou internet")
        print(" 1 - rápida \n2 - normal \n3 - lenta")
        speed = int(input("Digite a opção desejada: "))
        print("Quantos Mobs você acha por vez?")
        print("1 - 8 ou menos \n2 - Entre 9 e 16")
        mobs = int(input("Digite a opção desejada: "))
        print("Quantos Mobs mata por vez?")
        kills = int(input("Digite o número de mobs mortos por vez: "))
        LvCombate = int(input("Digite o nível de combate: "))
        LvCacada = int(input("Digite o nível de caçada: "))
        PorcentagemCombate = int(input("Digite a porcentagem de combate: "))
        PorcentagemCacada = int(input("Digite a porcentagem de caçada: "))
        MapaIncorreto = True
        while MapaIncorreto:
            MapaAtual = input(
                "Digite o nível do mapa atual (1,10,20,33,50,72,80,92 ou 93): ")
            if MapaAtual == "1" or MapaAtual == "10" or MapaAtual == "20" or MapaAtual == "33" or MapaAtual == "50" or MapaAtual == "72" or MapaAtual == "80" or MapaAtual == "92" or MapaAtual == "93":
                MapaIncorreto = False
        print("Configuração completa")
        print("Velocidade: ", speed)
        print("Mobs encontrados por vez: ", mobs)
        print("Mobs mortos por vez: ", kills)
        print("Nível de combate: ", LvCombate)
        print("Nível de caçada: ", LvCacada)
        print("Lvl do Mapa Atual: ", MapaAtual)


def cacar():
    print("Caçando")
    print("Aguarde alguns segundos")
    print("Buscando por configuração Salva...")
    try:
        with open("config_Hunt_pos.json", "r") as jsonFile:
            # Read the file contents
            config_data = jsonFile.read()

            print("Configuração encontrada")
            print(config_data)

            # Load the JSON data into a dictionary
            # Use json.loads() for string data
            config = json.loads(config_data)

            Battle_Button_loaded = config["Battle_Button"]
            Battle_Base_Hunt = config["Battle_Base_Hunt"]
            Battle_One_Liner = config["Battle_One_Liner"]
            Battle_Two_Liner = config["Battle_Two_Liner"]
    except FileNotFoundError:
        Battle_button = (74, 880)
        Battle_Base_Hunt = (872, 269)
        Battle_One_Liner = (1146, 225)
        Battle_Two_Liner = (1146, 310)
        salvar_Pos_Cacada(Battle_button, Battle_Base_Hunt,
                          Battle_One_Liner, Battle_Two_Liner)

    try:
        with open("config_caca.json", "r") as jsonFile:
            # Read the file contents
            config_data = jsonFile.read()

            print("Configuração encontrada")
            print(config_data)

            # Load the JSON data into a dictionary
            # Use json.loads() for string data
            config = json.loads(config_data)

            speed = config["speed"]
            mobs = config["mobs"]
            espera = config["espera"]
            pool = config["pool"]
            linhasPrevias = config["linhasPrevias"]

    except FileNotFoundError:
        print("Configuração não encontrada")
        print("Configurando")
        print("A velocidade da sua máquina ou internet")
        print(" 1 - rápida \n2 - normal \n3 - lenta")
        speed = int(input("Digite a opção desejada: "))
        print("Quantos Mobs você acha por vez?")
        print("1 - 8 ou menos \n2 - Entre 9 e 16")
        mobs = int(input("Digite a opção desejada: "))
        print("Quanto tempo de caçada?")
        print("Em segundos")
        espera = int(input("Digite o tempo total de caçada: "))
        print("Já existem Mobs caçados?")
        pool = input("Digite s ou n: ")
        if pool == "s":
            print("Quantos Mobs já estão caçados?")
            linhasPrevias = int(input("Digite o número de linhas: "))
        print("Configuração completa")
        print("Velocidade: ", speed)
        print("Mobs por vez: ", mobs)
        print("Tempo de caçada: ", espera)
        print("Mobs caçados: ", pool)
        print("Linhas caçadas: ", linhasPrevias)
        salvar = input("Deseja salvar as configurações? s ou n: ")
        if salvar == "s":
            salvar_Cacada(speed, mobs, espera, pool, linhasPrevias)
        else:
            print("Configurações não salvas, saindo")
            exit()
    runs = 0
    print("Começando em 3 segundos")
    pyautogui.sleep(3)
    print("Para parar aperte Ctrl + C ou mova o mouse para o canto superior esquerdo")
    if pool != "s":
        pyautogui.click(Battle_Button_loaded)
    try:
        if pool != "s":
            pyautogui.sleep(1*speed)
            pyautogui.click(Battle_Base_Hunt)
        pyautogui.sleep(1*speed)
        espera_original = espera
        espera += 6
        while True:
            if linhasPrevias != 0:
                if linhasPrevias == 1:
                    pyautogui.click(Battle_One_Liner)
                    print("Clicado!")
                    linhasPrevias = 0
                    pyautogui.sleep(espera)
                if linhasPrevias == 2:
                    pyautogui.click(Battle_Two_Liner)
                    print("Clicado!")
                    linhasPrevias = 0
                    pyautogui.sleep(espera)
            else:
                if mobs == 1:
                    pyautogui.click(Battle_One_Liner)
                    print("Clicado!")
                    print("Aguardando", espera, "segundos")
                    pyautogui.sleep(espera)
                if mobs == 2:
                    pyautogui.click(Battle_Two_Liner)
                    print("Clicado!")
                    print("Aguardando", espera, "segundos")
                    pyautogui.sleep(espera)
                else:
                    "Opção inválida"
                    break
            pyautogui.sleep(2 * speed)
            runs += 1
            espera += 0.25
            print("ciclo Completo! aguardando " + str(2*speed) + " segundos")
    except KeyboardInterrupt:
        print("Parando")
        print("ultima Configuração:")
        print("Velocidade: ", speed)
        print("Mobs por vez: ", mobs)
        print("Tempo de caçada: ", espera)
        print("Mobs caçados: ", pool)
        print("Linhas caçadas: ", linhasPrevias)
        print("Ciclos completos: ", runs)


def coletar():
    print("ainda não desenvolvida")


def farmar():
    print("Em testes!! use por sua conta e risco")


def main():
    sair = False
    while sair == False:
        print("IdleMMO Automator")
        print("O que deseja fazer?")
        print("0 - Configurar")
        print("1 - Caçar")
        print("2 - Coletar")
        print("3 - Farmar mobs")
        print("8 - Ver Posição do Mouse( 5s de intervalo)")
        print("9 - Ver Posição do Mouse( 1s de intervalo)")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cacar()
        elif opcao == "2":
            coletar()
        elif opcao == "3":
            farmar()
        elif opcao == "0":
            configurar()
        elif opcao == "8":
            while True:
                print(pyautogui.position())
                pyautogui.sleep(5)
        elif opcao == "9":
            while True:
                print(pyautogui.position())
                pyautogui.sleep(1)

        else:
            print("Opção inválida")
        sair = input("Deseja sair? s ou n: ")
        if sair == "s":
            sair = True
        else:
            sair = False


if __name__ == '__main__':
    main()
