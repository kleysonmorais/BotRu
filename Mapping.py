import json

class ApiModel:

    load        = None
    Palmas      = None
    Gurupi      = None
    Araguaina   = None

    def __init__(self, data):
        dump = json.dumps(data)
        self.load = json.loads(dump)
        campusList = self.load['campusList']
        # self.Gurupi = Campus(campusList[0])
        self.Palmas = Campus(campusList[1])
        # self.Araguaina = Campus(campusList[2])

class Campus:

    nomeCampus  = None
    segunda     = None
    terca       = None
    quarta      = None
    quinta      = None
    sexta       = None

    def __init__(self, campus):
        self.nomeCampus = campus['nomeCampus']
        self.segunda    = Dia(campus['segunda'])
        self.terca      = Dia(campus['terca'])
        self.quarta     = Dia(campus['quarta'])
        self.quinta     = Dia(campus['quinta'])
        self.sexta      = Dia(campus['sexta'])

    def getNomeCampus(self):
        return self.nomeCampus

class Dia:

    data = None
    almoco = None
    jantar = None

    def __init__(self, dia):
        self.data = dia['data']
        cardapio = dia['refeicoes']
        self.almoco = Cardapio(cardapio[0])
        self.jantar = Cardapio(cardapio[1])

    def getData(self):
        return self.data

class Cardapio:

    nomeRefeicao = None
    descricao = ""

    def __init__(self, cardapio):
        self.nomeRefeicao = cardapio['nomeRefeicao']
        self.textoDescricao(cardapio['itens'])

    def textoDescricao(self, itens):
        for item in itens:
            self.descricao += item['tipoItem'] + ":\n"
            for item_interno in item['itens']:
                self.descricao += "- " + item_interno['nome'] + "\n"
            self.descricao += "\n"

    def getCardapio(self):
        return self.descricao
