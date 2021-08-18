def main():
    #escribe tu código abajo de esta línea
    print("CALCULO DE AREA Y PERIMETRO DE UN CUADRADO")
    print("===================================")
    lado=float(input("Dame el lado del cuadrado:"))
    perimetro = float(4 * lado)
    area = lado ** 2
    print("El perímetro de este cuadrado es: " +str(perimetro))
    print("El área de este cuadrado es: " + str(area))

if __name__=='__main__':
    main()
