import requests
from Mapping import ApiModel
from datetime import datetime

# https://sistemas.uft.edu.br/cardapioru/api/campus.json
# https://sistemas.uft.edu.br/cardapioru/api/refeicao/semana/v2.json

class ApiRu:

    SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA, SABADO, DOMINGO = range(7)
    ANTES_ALMOCO, DURANTE_ALMOCO, ANTES_JANTAR, DURANTE_JANTAR, ENCERROU = range(5)
    url = None
    model = None
    dia = None
    refeicao = None
    horario = None

    def __init__(self):
        self.url = "https://sistemas.uft.edu.br/cardapioru/api/refeicao/semana/v2.json"
        response = requests.request("GET", self.url)
        data = response.json()
        self.model = ApiModel(data)
        self.dia = datetime.weekday(datetime.now())
        self.getRefeicao()

    def getHoje(self):
    
        if self.horario is self.ENCERROU:
            return "Ru tá fechado 😓"
    
        texto = "Cardápio de Hoje "
        if self.dia is self.SEGUNDA:
            return texto + "(Segunda-Feira)\n" + self.getPalmasSegunda()
        elif self.dia is self.TERCA:
            return texto + "(Terça-Feira)\n" + self.getPalmasTerca()
        elif self.dia is self.QUARTA:
            return texto + "(Quarta-Feira)\n" + self.getPalmasQuarta()
        elif self.dia is self.QUINTA:
            return texto + "(Quinta-Feira)\n" + self.getPalmasQuinta()
        elif self.dia is self.SEXTA:
            return texto + "(Sexta-Feira)\n" + self.getPalmasSexta()
        elif self.dia is self.SABADO:
            return "Hoje é Sábado, Ru tá fechado 😓"
        elif self.dia is self.DOMINGO:
            return "Hoje é Domingo e não tem RU 😓\nMas amanhã tem 😍!"
        
    
    def cardapioAtualizado(self):
        numeroSemana = datetime.now().isocalendar()[1]
        aux = str(self.model.Palmas.segunda.getData()).split("-")
        semanaSalva = datetime(int(aux[0]), int(aux[1]), int(aux[2]))
        numeroSemanaSalva = semanaSalva.isocalendar()[1]

        print(numeroSemanaSalva)
        print(numeroSemana)

        if numeroSemana is numeroSemanaSalva:
            print("Mesma Semana")
        else:
            print("Semana Errada")

    def getRefeicao(self):
        tempo = datetime.timetz(datetime.now())
        hora = tempo.hour
        minutos = tempo.minute
        if hora >= 0 and (hora <= 11 and minutos <= 30):
            self.refeicao = "a hora do almoço está próxima! Gostaria de saber qual é o cardápio de hoje?\n\nTenho certeza que a comida estará maravilhosa 😜.\n\nSe quiser, também posso te passar umas informações sobre os RUs da UFT."
            self.horario = self.ANTES_ALMOCO
        elif hora <= 13 and minutos <= 59:
            self.refeicao = "tá na hora do almoço! Gostaria de saber qual é o cardápio de hoje?\n\nTenho certeza que a comida estará maravilhosa 😜.\n\nSe quiser, também posso te passar umas informações sobre os RUs da UFT."
            self.horario = self.DURANTE_ALMOCO
        elif hora <= 17 and minutos <= 30:
            self.refeicao = "a hora do jantar está próxima! Gostaria de saber qual é o cardápio de hoje?\n\nTenho certeza que a comida estará maravilhosa 😜.\n\nSe quiser, também posso te passar umas informações sobre os RUs da UFT."
            self.horario = self.ANTES_JANTAR
        elif hora <= 19 and minutos <= 30:
            self.refeicao = "tá na hora do jantar! Gostaria de saber qual é o cardápio de hoje?\n\nTenho certeza que a comida estará maravilhosa 😜.\n\nSe quiser, também posso te passar umas informações sobre os RUs da UFT."
            self.horario = self.DURANTE_JANTAR
        else:
            self.refeicao = "o ru já fechou! Mas se quiser saber sobre outro dia, é só falar 😜"
            self.horario = self.ENCERROU


    def getPalmasSegunda(self, completo=False):
        if completo:
            return "Almoço 🍽\n" + self.model.Palmas.segunda.almoco.getCardapio() + "\nJantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

        if self.horario is self.ANTES_ALMOCO or self.horario is self.DURANTE_ALMOCO:
            return "Almoço 🍽\n" + self.model.Palmas.segunda.almoco.getCardapio() 
        else: 
            return "Jantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

    def getPalmasTerca(self, completo=False):
        if completo:
            return "Almoço 🍽\n" + self.model.Palmas.terca.almoco.getCardapio() + "\nJantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

        if self.horario is self.ANTES_ALMOCO or self.horario is self.DURANTE_ALMOCO:
            return "Almoço 🍽\n" + self.model.Palmas.terca.almoco.getCardapio()
        else:
            return "Jantar 🍽\n" + self.model.Palmas.terca.jantar.getCardapio()

    def getPalmasQuarta(self, completo=False):
        if completo:
            return "Almoço 🍽\n" + self.model.Palmas.quarta.almoco.getCardapio() + "\nJantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

        if self.horario is self.ANTES_ALMOCO or self.horario is self.DURANTE_ALMOCO:
            return "Almoço 🍽\n" + self.model.Palmas.quarta.almoco.getCardapio() 
        else:
            return "Jantar 🍽\n" + self.model.Palmas.quarta.jantar.getCardapio()
    
    def getPalmasQuinta(self, completo=False):
        if completo:
            return "Almoço 🍽\n" + self.model.Palmas.quinta.almoco.getCardapio() + "\nJantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

        if self.horario is self.ANTES_ALMOCO or self.horario is self.DURANTE_ALMOCO:
            return "Almoço 🍽\n" + self.model.Palmas.quinta.almoco.getCardapio() 
        else:
            return "Jantar 🍽\n" + self.model.Palmas.quinta.jantar.getCardapio()
    
    def getPalmasSexta(self, completo=False):
        if completo:
            return "Almoço 🍽\n" + self.model.Palmas.sexta.almoco.getCardapio() + "\nJantar 🍽\n" + self.model.Palmas.segunda.jantar.getCardapio()

        if self.horario is self.ANTES_ALMOCO or self.horario is self.DURANTE_ALMOCO:
            return "Almoço 🍽\n" + self.model.Palmas.sexta.almoco.getCardapio() 
        else:
            return "Jantar 🍽\n" + self.model.Palmas.sexta.jantar.getCardapio()
    
if __name__ == '__main__':
    bot = ApiRu()
    print(bot.getRefeicao())
    # print(bot.cardapioAtualizado())
    # bot.getPalmas()