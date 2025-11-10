class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = tilavuus if tilavuus > 0.0 else 0.0
        self.saldo = self._alku_saldo(alku_saldo)

    def _alku_saldo(self, alku_saldo):
        if alku_saldo < 0.0:
            return 0.0
        if alku_saldo <= self.tilavuus:
            return alku_saldo
        return self.tilavuus

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo
#BREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAK
    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
