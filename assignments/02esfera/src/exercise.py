def main():
    #escribe tu código abajo de esta línea
    import math
    r=float(input("dame el radio de la esfera: "))
    area=float(4*math.pi*r**2)
    volumen=float((4/3)*math.pi*math.pow(r,3))
    print("El volumen de la esfera es: ", volumen)
    print("El area de la esfera es: ", area)
if __name__=='__main__':
    main()
