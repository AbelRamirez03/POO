
class Boleto:
    def __init__(self, funcion, horario, clasificacion, aciento, sala, tipo_de_boleto, cantidad_boletos):
        self.precio = 70
        self.funcion = funcion
        self.horario = horario
        self.clasificacion = clasificacion
        self.aciento = aciento 
        self.sala = sala
        self.tipo_de_boleto = tipo_de_boleto
        self.cantidad_boletos = cantidad_boletos

    def mostrar_clasificacion(self):
        print(f"Pelicula Clasificacion {self.clasificacion}")

    def mostrar_boleto(self):
        print("\n--- Boleto de Cine ---")
        print(f"Película: {self.funcion}")
        print(f"Horario: {self.horario}")
        print(f"Clasificación: {self.clasificacion}")
        print(f"Asiento: {self.aciento}")
        print(f"Sala: {self.sala}")
        print(f"Tipo de boleto: {self.tipo_de_boleto}")
        print("----------------------")

    def calcular_total_boletos(self):
        total = self.precio * self.cantidad_boletos
        return total

class BoletoCombo(Boleto):
    def __init__(self, funcion, horario, clasificacion, aciento, sala, tipo_de_boleto, cantidad_boletos, combo, precio_combo, articulos):
        super().__init__(funcion, horario, clasificacion, aciento, sala, tipo_de_boleto, cantidad_boletos)
        self.combo = combo
        self.precio_combo = precio_combo
        self.articulos = articulos

    def calcular_precio_w_combo(self):
        total_boletos = super().calcular_total_boletos()
        total = self.precio_combo + total_boletos
        print(f"El precio total de los boletos con el combo: {self.combo}"
              f"Es de {total}")
        pass

    def mostrar_boleto(self):
        super()

peliculas = {
    1: {"nombre": "Matrix", "sala": 1, "horario": "18:00", "clasificacion": "B"},
    2: {"nombre": "The Godfather", "sala": 2, "horario": "20:00", "clasificacion": "C"},
    3: {"nombre": "Padington", "sala": 3, "horario": "16:00", "clasificacion": "A"},
    4: {"nombre": "Avengers: Endgame", "sala": 4, "horario": "21:00", "clasificacion": "B"},
    5: {"nombre": "Inseption", "sala": 5, "horario": "19:00", "clasificacion": "B"}
}

combos = {
    1: {"combo": "Combo Cuates", "precio": 280, "articulos": "Palomitas grandes, dos refrescos grandes"},
    2: {"combo": "Combo Nachos en Pareja", "precio": 350, "articulos": "Palomitas grandes, dos refrescos grandes, nachos garndes"},
    3: {"combo": "Combo M&M's", "precio": 230, "articulos": "Palomitas grandes, chocolates M&M's 250g"}

}

while True:
    print("\t\tBienvenido a la taquilla de cine")
    print("\n\nCatalogo de Peliculas")

    for pelicula_id, pelicula in peliculas.items():
        print(f"{pelicula_id}: {pelicula['nombre']} (Sala {pelicula['sala']}, Horario: {pelicula['horario']})")

    
    seleccion = int(input("Selecciona una película (1-5) o 0 para salir: "))
    if seleccion < 0 or seleccion > 5:
        print("Selección inválida. Por favor, elige una opción válida.")
        continue
    if seleccion == 0:
        print("Gracias por usar el sistema de boletos de cine.")
        break
    else:
        question=input("¿Desea comprar un combo? (si/no): ").strip().lower()
        if question == "si":
            print("Combos disponibles:")
            for combo_id, combo in combos.items():
                print(f"{combo_id}: {combo['combo']} - Precio: {combo['precio']} - Artículos: {combo['articulos']}")
            
            seleccion_combo = int(input("Selecciona un combo (1-3): "))
            if seleccion_combo < 1 or seleccion_combo > 3:
                print("Selección inválida. Por favor, elige una opción válida.")
                continue
            
            combo_seleccionado = combos[seleccion_combo]["combo"]
            precio_combo = combos[seleccion_combo]["precio"]
            articulos_combo = combos[seleccion_combo]["articulos"]
            print(f"Has seleccionado el {combo_seleccionado} que incluye: {articulos_combo}")

            boletoconCombo=BoletoCombo(
                funcion=peliculas[seleccion]["nombre"],
                horario=peliculas[seleccion]["horario"],
                clasificacion=peliculas[seleccion]["clasificacion"],
                aciento=input("Ingrese el número de asiento: "),
                sala=peliculas[seleccion]["sala"],
                tipo_de_boleto=input("Ingrese el tipo de boleto (adulto/nino): "),
                cantidad_boletos=int(input("Ingrese la cantidad de boletos: ")),
                combo=combo_seleccionado,
                precio_combo=precio_combo,
                articulos=articulos_combo
            )
            boletoconCombo.mostrar_boleto()
            boletoconCombo.mostrar_clasificacion()
    break
