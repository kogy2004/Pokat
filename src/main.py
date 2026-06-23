import pokat as pk

if __name__ == "__main__":
    pikachu = pk.Pokat("Pikachu", 5, 50)
    print(pikachu.mostrar_info)
    
    print(pikachu.ganar_exp(30))
    print(pikachu.mostrar_info)
    
    print(pikachu.ganar_exp(20))
    print(pikachu.mostrar_info)
    
    pikachu.cambiar_nombre("Raichu")
    print(pikachu.mostrar_info)