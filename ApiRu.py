import requests
from Mapping import ApiModel

# https://sistemas.uft.edu.br/cardapioru/api/campus.json
# https://sistemas.uft.edu.br/cardapioru/api/refeicao/semana/v2.json

class ApiRu:

    url = None
    model = None

    def __init__(self):
        self.url = "https://sistemas.uft.edu.br/cardapioru/api/refeicao/semana/v2.json"
        response = requests.request("GET", self.url)
        data = response.json()
        self.model = ApiModel(data)
        
    def getPalmasSegunda(self):
        return "Almoço\n" + self.model.Palmas.segunda.almoco.getCardapio() + "\n " + "Jantar\n" + self.model.Palmas.segunda.jantar.getCardapio()

    def getPalmasTerca(self):
        return "Almoço\n" + self.model.Palmas.terca.almoco.getCardapio() + "\n " + "Jantar\n" + self.model.Palmas.terca.jantar.getCardapio()

    def getPalmasQuarta(self):
        return "Almoço\n" + self.model.Palmas.quarta.almoco.getCardapio() + "\n " + "Jantar\n" + self.model.Palmas.quarta.jantar.getCardapio()
    
    def getPalmasQuinta(self):
        return "Almoço\n" + self.model.Palmas.quinta.almoco.getCardapio() + "\n " + "Jantar\n" + self.model.Palmas.quinta.jantar.getCardapio()
    
    def getPalmasSexta(self):
        return "Almoço\n" + self.model.Palmas.sexta.almoco.getCardapio() + "\n " + "Jantar\n" + self.model.Palmas.sexta.jantar.getCardapio()
    
if __name__ == '__main__':
    bot = ApiRu()
    # bot.getPalmas()