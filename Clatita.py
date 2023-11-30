class Clatita:
    def __init__(self, diametru, aria, masa):
        self.diametru = diametru
        self.aria = aria
        self.masa = masa
        self.raza = 0
        self.greutate = 0
    def __str__(self):
        return f'Are un diametru de {self.diametru}, aria este agala cu {self.aria}, are o masa de {self.masa}Kg si o greutate de {self.greutate}N.'

    def arie(self):
        self.raza = self.diametru/2
        self.aria = self.raza * self.raza * 3.14

    def greutatea(self):
        self.masa = self.diametru * 0.005 #0.005mm = grosimea
        self.greutate = self.masa * 9.81 #9.81 = g

c = Clatita(4, 0, 0)
c.arie()
c.greutatea()
print(c)

class Clatita_Miere(Clatita)
    def __init__(self, diametru, aria, masa cantitate_miere, ):
        super().__init__(diametru, aria, masa)
        self.cantitate_miere = cantitate_miere
