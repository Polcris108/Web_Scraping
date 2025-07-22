# Creado por Cristian Bravo
# Inspirado en el video del youtuber "El Pingüino de Mario" en el video 

import requests as re
from bs4 import BeautifulSoup

url = "https://dockerlabs.es"
respuesta = re.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    maquinas = soup.find_all("div", onclick = True)

    #Variable control
    bandera = 0
    
    #Bienvenida
    print("Bienvenid@ al uso de Web Scrapping en DockerLabs creado por \033[1;36mCristian Bravo\033[0m\n")
    print("1 - Dificultad\033[1;32m fácil\033[0m\n2 - Dificultad\033[1;33m media\033[0m\n3 - Dificultad\033[1;31m difícil\033[0m\n4 - Mostrar \033[1;35mtodas\033[0m las dificultades\n")
    op = int(input("Seleccione la opcion para continuar: "))
    
    #Recorrer texto recuperado
    for maquina in maquinas:
        onclick_text = maquina["onclick"]
        nombre = onclick_text.split("'")[1]
        autor = onclick_text.split("'")[7]
        fecha = onclick_text.split("'")[11]
        dificultad = onclick_text.split("'")[3]        
         
        while (op != 1 and op != 2 and op != 3 and op != 4):
            print("Favor de ingresar un número válido del menú")
            print("1 - Dificultad\033[1;32m fácil\033[0m\n2 - Dificultad\033[1;33m media\033[0m\n3 - Dificultad\033[1;31m difícil\033[0m\n4 - Mostrar todas las dificultades\n")
            op = int(input("Seleccione la opcion para continuar: ")) 
                
        if op == 1 and dificultad == "Fácil":
            
            while bandera == 0:
                print("\n\033[1;32m======================== Ejercicios con dificultad Fácil ========================\033[0m\n")
                bandera = 1
                
            contador_maquinas_f += 1
            print(f"\033[1;36mNombre\033[0m: {nombre}")
            print(f"Autor: {autor}")
            print(f"Fecha de publicación: {fecha} \n")
        
        elif op == 2 and dificultad == "Medio":  
            
            while bandera == 0:
                print("\n\033[1;33m======================== Ejercicios con dificultad Media ========================\033[0m\n")
                bandera = 1
            
            contador_maquinas_m += 1
            print(f"\033[1;36mNombre:\033[0m {nombre}")
            print(f"\033[1;36mAutor:\033[0m {autor}")
            print(f"\033[1;36mFecha de publicación:\033[0m {fecha} \n")
        
        elif op == 3 and dificultad == "Difícil":  
            
            while bandera == 0:
                print("\n\033[1;31m======================== Ejercicios con dificultad Difícil ========================\033[0m\n")
                bandera = 1
            
            contador_maquinas_d += 1
            print(f"\033[1;36mNombre:\033[0m {nombre}")
            print(f"\033[1;36mAutor:\033[0m {autor}")
            print(f"\033[1;36mFecha de publicación:\033[0m {fecha} \n")
        
        elif op == 4:
            
            while bandera == 0:
                print("\n\033[1;35m======================== Todos los ejercicios ========================\033[0m\n")
                bandera = 1

            print(f"\033[1;36mNombre:\033[0m {nombre}")
            print(f"\033[1;36mAutor:\033[0m {autor}")           
            print("Dificultad:", end="")
            
            if dificultad == "Fácil":
                print("\033[1;32m Fácil\033[0m")
            elif dificultad == "Medio":
                print("\033[1;33m Media\033[0m")
            elif dificultad == "Difícil":
                print("\033[1;31m Difícil\033[0m")
            
            print(f"\033[1;36mFecha de publicación:\033[0m {fecha} \n")
                        
else:
    print("Error, no se logró conectar con la página")