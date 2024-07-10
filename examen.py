import csv
import random
import math

trabajadores = [
    {
        "Nombre":  "Juan Perez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Maria Garcia",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Carlos Lopez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Ana Martinez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Pedro Rodriguez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Laura Hernandez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Miguel Sanchez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Isabel Gomez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Francisco Diaz",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
    {
        "Nombre":  "Elena Fernandez",
        "Sueldo": 0,
        "Desc. salud": 0,
        "Desc. afp": 0,
        "Sueldo liquido": 0,
    },
]

try:
    
    def menu():
        menu = int(input("""
                        ----------Menú----------
                        1. Asignar sueldos aleatorios
                        2. Clasificar sueldos
                        3. Ver estadísticas
                        4. Reporte de sueldos
                        5. Salir del programa
                        Seleccione su opción:  
                        """))
        return menu
    
    def asignar_aleatorios():
        for i in trabajadores:
            sueldo = random.randint(300000, 2500000)
            i['Sueldo'] = sueldo
            print(f"Nombre: {i['Nombre']}   Sueldo: ${i['Sueldo']} ")
        print("Se han asignado con exito los sueldos aleatorios")
        
        
    def clasificar_sueldos():
        sueldo1 =[]
        sueldo2 = []
        sueldo3 = []
        for trabajador in trabajadores:
            if trabajador['Sueldo'] < 800000:
                sueldo1.append(trabajador)
            elif 800000 < trabajador['Sueldo'] and trabajador['Sueldo'] < 2000000:
                sueldo2.append(trabajador)
            elif trabajador['Sueldo'] > 2000000 :
                sueldo3.append(trabajador)
        
        print(f"""   Sueldos menores a $800.000      Total : {len(sueldo1)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldo1:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                     """)     
        
        print(f"""   Sueldos entre $800.000 y $2.000.000    Total : {len(sueldo2)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldo2:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                      """)   
        
        print(f"""   Sueldos superior a $2.000.000    Total : {len(sueldo3)}  
                     Nombre empleado                   Sueldo""")
        for trabajador in sueldo3:
            print(f"""
                    {trabajador['Nombre']}            ${trabajador['Sueldo']}
                       """)   
            
    def esata():
        if not trabajadores:
            asignar_aleatorios()
        larga=max(trabajadores,key=lambda x: x['Sueldo'])
        corta=min(trabajadores,key=lambda x: x['Sueldo'])
        print(f'el empleado que mas genera es : {larga['Nombre']}  sueldo de : {larga['Sueldo']:,}')
        print(f'el empleado que mas genera es : {corta['Nombre']} sueldo de : {corta['Sueldo']:,}')
        totales=sum(i['Sueldo'] for i in trabajadores)
        totales=int(totales/10)
        print(f'El promedio de sueldos es de ${totales:,}')
        totales=math.prod(i['Sueldo'] for i in trabajadores)
        totales=math.pow(totales,1/10)
        
        
        
    def reportesueldos():
        print(f"""
                  Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo liquido
                  """)
        for trabajador in trabajadores:
            trabajador['Desc. salud'] = trabajador['Sueldo'] * 0.7
            trabajador['Desc. afp'] = trabajador['Sueldo'] * 0.12
            
            descTotales = trabajador['Desc. salud'] + trabajador['Desc. afp']
            
            trabajador['Sueldo liquido'] = trabajador['Sueldo'] - descTotales
            
            print(f"""
                  {trabajador['Nombre']}  {trabajador['Sueldo']} {trabajador['Desc. salud']} {trabajador['Desc. afp']} {trabajador['Sueldo liquido']}
                  """)

            with open("reporte_de_sueldos.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['Nombre', 'Sueldo base', 'Desc. salud', 'Desc. afp', 'Sueldo liquido'])
                for i in trabajadores:
                    escritor.writerows(
                        [[i['Nombre'], i['Sueldo'], i['Desc. salud'], i['Desc. afp'], i['Sueldo liquido']]
                         ])   
        print("Se descargara el archivo!")
    

    while True:
        op = menu()
        if op == 1:
            print("Asignar sueldos ")
            asignar_aleatorios()
        elif op == 2:
            print(" Clasificar sueldo ")
            clasificar_sueldos()
        elif op == 3:
            print(" Reporte de sueldo ")
            reportesueldos()
        elif op == 4:
            print ("Estadisticas")
            esata()
            
        elif op == 5:
            print(""" Finalizando programa...
                      Realizado por : 
                      Matias Vilugron
                      20.637.356-3
                      """)
            break
            
        else: print("pOR FAVOR INGRESE UNA OPCION VALIDA EN EL SISTEMA  ")
    
except Exception as e: print(f"OCURRIO UN ERROR!!!!!!, {e}")