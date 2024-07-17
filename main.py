import discord
import  random
import  requests
import  os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot está online como {client.user}')



def algebra(operation , a , b):
    """
    essa função realiza a operação
    :param operation: número da operação à ser realizada
    :param a: numero da esquerda
    :param b: numero da direita
    :return: resultado da operação
    """
    if operation == 0:
        return float(a)+float(b)
    elif operation==1:
        return float(a)-float(b)
    elif operation == 2:
        return  float(a)*float(b)
    return  float(a)/float(b)

def calculate(content):
    """
    essa função define a operação a ser realizada e chama a função que realiza a operação
    :param content: próximos caracteres após o !calcule
    :return: retorna o resultado da operaçaõ
    """
    activator = False
    leftcontent = ""
    rightcontent = ""
    operation = 0;  # 0 soma , 1 subtrai , 2 multiplica ,3 divide
    for i in range(len(content) - 1):
        if content[i] == "x":
            operation = 2
            activator = True
        elif content[i] == "+":
            activator = True
        elif content[i] == "-":
            operation = 1
            activator = True
        elif content[i] == "/":
            operation = 3
            activator = True
        if activator:
            if content[i + 1] != " ":
                rightcontent += content[i + 1]
        else:
            if content[i] != " ":
                leftcontent += content[i]

    result = algebra(operation, leftcontent, rightcontent)
    return  result



def callApiFacts():
    """
    essa função chama a api de fatos matemáticos
    :return: o texto profindo do fato matemático
    """

    number = random.randint(0,1000)
    url = f"http://numbersapi.com/{number}/math"
    response = requests.get(url)
    return  response.text

#contador de players no jogo
counterP = 0








#jogo do bicho
players = []
def takePlayers(player,group):
    """
    essa função cadastra o player e seu grupo no jogo
    :param player: no do player que entrou no jogo
    :param group: array de grupos de animais que pertencem ao game
    """
    players.append({"nameP":player,"group":group})
groups = [
    {'name': 'zebra', 'numbers': ['1', '2', '3','4']},
    {'name': 'leão', 'numbers': ['5', '6', '7','8']},
    {'name': 'cobra', 'numbers': ['9', '10', '11','12']},
    {'name': 'elefante', 'numbers': ['45', '46', '47','48']}
]
def checkGroupExist(group):
    """
    essa função checka se o grupo escolhido pelo jogador existe no game
    :param group: array de grupos de animais que pertencem ao game
    :return: True se o grupo existe , False caso contrário
    """
    exist = False
    for i in  range(len(groups)):
        if(group==groups[i]["name"]):
            exist = True
    if not(exist):
        return False
    return True

def gameOver(players):
    """
    esta função limpa o array de players , ou seja, reinicia o jogo
    :param players: array de cada player com seu respctivo grupo escolhido
    :return:
    """
    counterP = 0
    players.clear();


def startGame(players,milhar):
    """
    Essa função da start ao jogo do bixo
    :param players: array de cada player com seu respctivo grupo escolhido
    :param milhar: numero milhar sorteado
    :return: retorna o grupo de animais que venceeram a aposta
    """
    groupswinners = []
    winners = []
    lastdecimal = milhar[2:]
    lastAlgarism = milhar[3:]
    #milhar = str(generateMilhar())
    for g in range(len(groups)):
        for num in range(len(groups[g]["numbers"])):
            #itero sobre a lista de numeros de cada grupo
            if(len(groups[g]["numbers"][num])>1):
                #se o grupo tiver numeros decimais
                # comparo a parte decilmal do numero sorteado com a os numeros decilamis de cada grupo
                if lastdecimal==groups[g]["numbers"][num]:
                    groupswinners.append(groups[g]['name'])
            else:
                #se não , comparo o ultimo algarismo do numero sorteado
                if lastAlgarism==groups[g]["numbers"][num]:
                    groupswinners.append(groups[g]['name'])

    for p in range(len(players)):
        for gpwinner in groupswinners:
            if players[p]["group"]==gpwinner:
                winners.append(players[p]["nameP"])
    return winners

def generateMilhar():
    milhar = random.randint(1000,10000)
    return milhar


@client.event
async def on_message(message):
    user_name = message.author.name
    if message.content.startswith('!quantas vezes eu reclamei do colucci no semestre passado?'):
        if user_name =="henryhn":
            await message.channel.send("Henri ama o Colucci")
        else:
            vezes = random.randint(40, 1000)
            await message.channel.send("você reclamou do colucci aproximadamente  " + str(vezes) + "  vezes")
    if message.content.startswith('!leo'):
        vezes = random.randint(40, 1000)
        await message.channel.send(f"leo achou que foi mal em {vezes} provas , apenas neste ano")

    if message.content.startswith('!fila'):
        image_path = 'images/fila.jpeg'
        picture = discord.File(image_path)
        await message.channel.send(file=picture)
        await  message.channel.send("corre que dá tempo")
    if message.content.startswith("!comandos"):
        await  message.channel.send("1 - !fila \n 2 - !curiosidades \n3 - !calcule\n 4 - !leo\n 5 - !quantas vezes eu reclamei do colucci no semestre passado?")
    if message.content.startswith("!regras bixo"):
        await  message.channel.send("Há x animais, cada um associado a quatro números, totalizando 100 números.\n"
                                    " Os jogadores escolhem um animal (e, consequentemente, um conjunto de números) para apostar.\n "
                                    "As apostas podem ser feitas em diversas modalidades, como:\n"
                                    "Grupo: Escolher um dos x animais. \n"
                                    "Grupos : Zebra(1,2,3,4)\n"
                                    "Leão(5,6,7,8) \n "
                                    "Cobra(9,10,11,12)\n"
                                    "elefante(45,46,47,48)\n"
                                    "Dezena: Escolher um número específico dentro do grupo de um animal.\n"
                                    "Centena: Combinar três números, considerando a centena.\n"
                                    "Milhar: Combinar quatro números, considerando milhar.\n"
                                    "OBS : só a aposta em grupo funciona , por enquanto.\n"
                                    "Será sorteado um milhar , se alguma número pertencente ao teu grupo fazer parte do milhar sorteado, tu ganharas .")
    #contador de players no jogo
    global counterP

    if message.content.startswith("!começar bixo"):
        if counterP>1:
            await  message.channel.send("o jogo do bixo do bixo irá começar em breveeee")
            milhar = str(generateMilhar())
            await  message.channel.send("o número sorteado ééééee.....")
            await  message.channel.send(milhar)
            winners = startGame(players, milhar)
            if len(winners) >= 1:
                for winner in winners:
                    await  message.channel.send(
                        f"{winner} é um vencedor do grande prêmio de mil pesos argerntinos, parabéns!!!")
                gameOver(players)

            else:
                await  message.channel.send("ngm venceu :(")
                gameOver(players)
        else:
            await  message.channel.send("é necessário pelo menos 2 jogadores para o jogo do bixo começar")

    if message.content.startswith("!jogo do bixo"):
        group = message.content[len("!jogo do bixo "):]
        groupExist = checkGroupExist(group)
        if not(groupExist):
            await  message.channel.send(f" o grupo {group} não existe seu arrombado, escreve o bagulho direito ai cuzão ")
            return
        if(len(players)>0):
            repeatedP = False
            for i in  range(len(players)):
                if players[i]["nameP"]== user_name:
                    repeatedP =True
                    break
            if not(repeatedP):
                takePlayers(user_name, group)
                counterP += 1
                await  message.channel.send(f"{user_name} entrou no jogo do bixo !!!")

            else:
                await  message.channel.send("jogador já entrou no jogo do bixo antes")
        else:
            takePlayers(user_name, group)
            counterP+=1
            await  message.channel.send(f"{user_name} entrou no jogo do bixo !!!")


    if message.content.startswith("!nattan"):
        await  message.channel.send("vo tranca u cursu")

    if message.content.startswith("!caju"):
        await  message.channel.send("já ta bão já, cade o break?")


    if message.content.startswith("!calcule"):
        content = message.content[len("!calcule"):]
        result = calculate(content)
        await  message.channel.send(" o resultado é " +str(result))
    if message.content.startswith("!curiosidades"):
        fact = callApiFacts()
        await  message.channel.send(fact)


client.run(TOKEN)

