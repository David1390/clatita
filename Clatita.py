class Clatita:
    def __init__(self, diametru, aria, masa):
        self.diametru = diametru
        self.aria = aria
        self.masa = masa
        self.raza = 0
        self.greutate = 0
    def __str__(self):
        return f'Clatita are un diametru de {self.diametru}cm, aria este agala cu {self.aria}, are o masa de {self.masa}Kg si o greutate de {self.greutate}N.'

    def arie(self):
        self.raza = self.diametru/2
        self.aria = self.raza * self.raza * 3.14

    def greutatea(self):
        self.masa = self.diametru * 0.005 #0.005mm = grosimea
        self.greutate = self.masa * 9.81 #9.81 = g

c = Clatita(8, 0, 0)
c.arie()
c.greutatea()
print(c)

class Clatita_Miere(Clatita):
    def __init__(self, cantitate_miere, aspect_topping, diametru, aria, masa):
        super().__init__(diametru, aria, masa)
        self.cantitate_miere = cantitate_miere
        self.aspect_topping = aspect_topping

    def __str__(self):
        return f'Clatita cu miere are o greutate de {self.greutate}N si un aspect {self.aspect_topping}.'
    def greutatea(self):
        self.cantitate_miere = 0.005 #0.005 kg
        self.masa = self.diametru * 0.005 #0.005mm = grosimea
        self.greutate = self.masa * 9.81 + self.cantitate_miere #9.81 = g

c1 = Clatita_Miere(0, "galben-auriu", 8, 0, 0)
c1.greutatea()
print(c1)

class Clatita_Ciocolata(Clatita):
    def __init__(self, cantitate_ciocolata, aspect_topping, diametru, aria, masa):
        super().__init__(diametru, aria, masa)
        self.cantitate_ciocolata = cantitate_ciocolata
        self.aspect_topping = aspect_topping

    def __str__(self):
        return f'Clatita cu ciocolata are o greutate de {self.greutate}N si un aspect {self.aspect_topping}.'
    def greutatea(self):
        self.cantitate_ciocolata = 0.015 #0.015 kg
        self.masa = self.diametru * 0.005 #0.005mm = grosimea
        self.greutate = self.masa * 9.81 + self.cantitate_ciocolata #9.81 = g

c2 = Clatita_Ciocolata(0, "maroniu", 8, 0, 0)
c2.greutatea()
print(c2)

class Clatita_Gem_Capsuni(Clatita):
    def __init__(self, cantitate_gem, aspect_topping, diametru, aria, masa):
        super().__init__(diametru, aria, masa)
        self.cantitate_gem = cantitate_gem
        self.aspect_topping = aspect_topping

    def __str__(self):
        return f'Clatita cu gem de capsuni are o greutate de {self.greutate}N si un aspect {self.aspect_topping}.'
    def greutatea(self):
        self.cantitate_gem = 0.030 #0.030 kg
        self.masa = self.diametru * 0.005 #0.005mm = grosimea
        self.greutate = self.masa * 9.81 + self.cantitate_gem #9.81 = g

c3 = Clatita_Gem_Capsuni(0, "rosu-rozaliu", 8, 0, 0)
c3.greutatea()
print(c3)
