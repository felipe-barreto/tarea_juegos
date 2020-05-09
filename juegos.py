import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg

def guardar(nom,ape,ed,jue):
    datos = {"apellido":ape,"edad":ed,"juego":jue}
    
    # Si no hay un archivo creado lo creo y guardo ahí la información, si ya hay un archivo creado lo abro
    # y le agrego a ese archivo la información nueva. Para hacer esto hago uso del manejo de excepciones.
    
    try:
        archivo = open("juegos.txt", "x")
        cargar = {nom:datos}
    except FileExistsError:
        archivo = open("juegos.txt", "r+")
        cargar = json.loads(archivo.read())
        cargar[nom] = datos
        archivo.seek(0,0)
    json.dump(cargar,archivo,indent=4)
    archivo.close()

def main(args):
    sigo_jugando = True
    while sigo_jugando:
        
        print("¿Querés jugar un juego?")
        seguir = True
        while (seguir):
            print("Ingrese si o no")
            respuesta = input().lower()
            if respuesta != 'si' and respuesta != "no":
                print("No es una respuesta válida")
            else:
                seguir = False
        if respuesta == "no":
            break
        else:
            print("Ingrese su nombre: ")
            nombre = input()
            print("Ingrese su apellido: ")
            apellido = input()
            print("Ingrese su edad: ")
            edad = input()
        
            layout = [[sg.Text('Elegí con qué juego querés jugar')],
                [sg.Button('Ahorcado'), sg.Button('Ta-TE-TI'), sg.Button('Otello'), sg.Button('Salir')]]
            window = sg.Window('Juegos', layout)
            event, values = window.read()
            window.close()
        
            if event == 'Ahorcado':
                hangman.main()
            elif event == 'Ta-TE-TI':
                tictactoeModificado.main()
            elif event == 'Otello':
                reversegam.main()
            elif event in (None, 'Salir'):
                sigo_jugando = False
            if event == "Ahorcado" or event == "Ta-TE-TI" or event == "Otello":
                guardar(nombre,apellido,edad,event)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



# ESTRUCTURA DE DATOS
# La estructura de datos que utilizo es un diccionario de diccionarios, de esta forma es fácil saber
# que es cada dato (o sea si es un apellido, juego, etc.).

# FORMATO DE ARCHIVO
# El formato de archivo que utilizo es json, de esta forma la información persiste y además se puede ver
# esta información abriendo el archivo de texto, que en pickle no ocurre porque se guarda en formato binario.
