import datetime
from lib.servidor.conversor import SpeedConversor, VolumeConversor, VolumeUnit, SpeedUnit, AllowedGrandezas

mapa_grandeza = {
    1: AllowedGrandezas.speed,
    2: AllowedGrandezas.volume
}

mapa_unidade = {
    3: SpeedUnit.mps,
    4: SpeedUnit.kmph,
    5: SpeedUnit.mph,
    6: VolumeUnit.m3,
    7: VolumeUnit.liter,
    8: VolumeUnit.barrel,
}


class Logger:
    
    
    @classmethod
    def salvarArquivo(cls, dado):
        try:
            a = open('registro.txt', 'a+')
        except:
            print('Deu tudo errado, que droga.')
        else:
            a.write(dado)
            a.close()
    
    
    @classmethod
    def LerArquivo(cls):
        try:
            a = open('registro.txt', 'r')
        except:
            print('O arquivo não existe.')
        else:
            for linha in a:
                linha = linha.strip().split(';')
                datahora = datetime.datetime.fromisoformat((linha[0]))
                grand = linha[1]
                origem = mapa_unidade[int(linha[2])].value[0]
                destino = mapa_unidade[int(linha[3])].value[0]
                entrada = linha[4]
                resposta = linha[5]
                print(f'{datahora.day}/{datahora.month}/{datahora.year} {datahora.hour}:{datahora.minute} foi convertido {entrada} {origem}  para {resposta} {destino}  ')