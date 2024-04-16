try:


    rutSinDigito = input("Ingrese rut: ")

    if not rutSinDigito.isdigit or len(rutSinDigito) !=8:
        raise ValueError ("Elrut es invalido")
    

    suma = (int(rutSinDigito[7]) * 2 +
            int(rutSinDigito[6]) * 3 +
            int(rutSinDigito[5]) * 4 +
            int(rutSinDigito[4]) * 5 +
            int(rutSinDigito[3]) * 6 +
            int(rutSinDigito[2]) * 7 +
            int(rutSinDigito[1]) * 2 +
            int(rutSinDigito[0]) * 3 )
    
    resto = suma % 11

    digitoVerificador = 11 - resto


    if digitoVerificador == 10:
        digitoVerificador ="k"
    elif digitoVerificador == 11:
        digitoVerificador = "0"    

        print("el digito verificador es", digitoVerificador)


    

except ValueError as e:
    print("Error",e)