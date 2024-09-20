print("Act 9 clase humano")
print("David Salazar Mat: 22308051281082")
# Zona de class
class Humano1082:
    # Zona de atributos
    edad=0
    estatura=0
    colordeojos=""
    colordecabello=""
    peso=0
    fechadenacimiento=""
    # Zona de funciones dentro de la clase
    def saltar1082(self,n):
        print(f"{n} esta saltando ufff....")
    def comer1082(self,n):
        print(f"{n} esta comiendo ufff....")
    def viajar1082(self,n):
        print(f"{n} esta viajando ufff....")
    def trabajar1082(self,n):
        print(f"{n} esta trabajando ufff....")

# Zona de creacion de objetos
David=Humano1082()
Kristina=Humano1082()
# Zona de usando objetos
print(" Resultados para David")
David.edad=17
print(f"Edad : {David.edad}")
David.estatura=200
print(f"Estatura : {David.estatura}")
David.colordeojos="Cafe Oscuro"
print(f"Color de ojos : {David.colordeojos}")
David.colordecabello="Negro"
print(f"Color de cabello : {David.colordecabello}")
David.peso=90
print(f"Peso : {David.peso} kilos")
David.fechadenacimiento="03/01/07"
print(f"Fecha de nacimiento : {David.fechadenacimiento}")

# Zona de usando funciones
David.saltar1082("David")
David.comer1082("David")
David.viajar1082("David")
David.trabajar1082("David")

print(" Resultados para Kristina")
Kristina.edad=18
print(f"Edad : {Kristina.edad}")
Kristina.estatura=160
print(f"Estatura : {Kristina.estatura}")
Kristina.colordeojos="Azules"
print(f"Color de ojos : {Kristina.colordeojos}")
Kristina.colordecabello="Castaño Oscuro"
print(f"Color de cabello : {Kristina.colordecabello}")
Kristina.peso=50
print(f"Peso : {Kristina.peso} kilos")

# Zona de usando funciones
Kristina.saltar1082("Kristina")
Kristina.comer1082("Kristina")
Kristina.viajar1082("Kristina")
