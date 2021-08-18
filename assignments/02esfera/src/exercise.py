def main():
    #escribe tu código abajo de esta línea
    import math
    r=float(input("dame el radio de la esfera: "))
    volumen=float((4/3)*math.pi*math.pow(r,3))
    print("El volumen de la esfera es: ", volumen)

if __name__=='__main__':
    main()
