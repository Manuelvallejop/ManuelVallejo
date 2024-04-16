"""
Realiza un programa que reciba tres números por teclado  
calcule su promedio 
se debe mostrar el resultado en pantalla.
"""
laboratorio_1 = float(input("La nota del laboratorio 1 es: "))
laboratorio_2 = float(input("la nota del laboratorio 2 es: "))
laboratorio_3 = float(input("la nota del laboratorio 3 es: "))

tarea_1 = float(input("La nota de la tarea 1 es: "))
tarea_2 = float(input("La nota de la tarea 2 es: "))
tarea_3 = float(input("la nota de la tarea 3 es: "))

solemne_1 = float(input("La nota solemne 1 es: "))
solemne_2 = float(input("La nota solemne 2 es: ")) 

prom_lab = (laboratorio_1 + laboratorio_2 + laboratorio_3) //3
prom_tareas = (tarea_1 + tarea_2 + tarea_3) //3
nota_de_presentacion = prom_lab*0.15 + prom_tareas * 0.15 + solemne_1 * 0.35 + solemne_2 * 0.35
print("La nota final es: ", nota_de_presentacion)