Algoritmo EXAMEN
	
	Escribir "Introducir número de personas por registrar:"
	Leer n
	
	Definir fn, ff Como Entero
	Dimension fn(n)
	Dimension ff(n)
	
	
	Para i=1 Hasta n Con Paso 1
		Escribir "Introducir fecha de nacimiento de persona ", i, ":"
		Leer fn(i)
		Escribir "Introducir fecha de fallecimiento de persona ", i, ":"
		Leer ff(i)
	FinPara
	
	Definir ar Como Entero
	Escribir "Introducir año de referencia:"
	Leer ar
	
	Definir count, mark, pv, emj, emv, edad Como Entero
	count <- 1
	mark <-0
	
	Mientras count = 1 Hacer
		Escribir "Introducir lo que se desea hacer:"
		Escribir "1- Consultar número de personas vivas en ", ar,"."
		Escribir "2- Consultar edad de la persona más joven en ", ar,"."
		Escribir "3- Consultar edad de la persona más vieja en ", ar,"."
		Escribir "4- Introducir nuevo año de referencia."
		Escribir "5- Salir."
		Leer mark
		
		Si mark = 1 Entonces
			pv <- 0
			Para i = 1 Hasta n Con Paso 1
				Si ar >= fn(i) y ar <= ff(i) Entonces
					pv = pv+1
				FinSi
			FinPara
			Si pv > 0 Entonces
				Escribir "La cantidad de personas vivas en ", ar, " es: ", pv
			SiNo
				Escribir "En ", ar, " no habian personas vivas."
			FinSi
		FinSi
		
		Si mark = 2 Entonces
			emj <- 99999999
			Para i = 1 Hasta n Con Paso 1
				Si ar >= fn(i) y ar <= ff(i) Entonces
					edad = ar-fn(i)
					Si edad < emj Entonces
						emj = edad
					FinSi
				FinSi
			FinPara
			Escribir "La persona más joven en ", ar, " tiene: ", emj, " años."
		FinSi
		
		Si mark = 3 Entonces
			emv <- -1
			Para i = 1 Hasta n Con Paso 1
				Si ar >= fn(i) y ar <= ff(i) Entonces
					edad = ar-fn(i)
					Si edad > emv Entonces
						emv = edad
					FinSi
				FinSi
			FinPara
			Escribir "La persona más vieja en ", ar, " tiene: ", emv, " años."
		FinSi
		
		Si mark = 4 Entonces
			Escribir "Introducir nuevo año de referencia:"
			Leer ar
		FinSi
		
		Si mark = 5 Entonces
			count <- 0
		FinSi
		
		Si mark < 0 o mark > 5 Entonces
			Escribir "Introducir un parametro disponible."
		FinSi
	FinMientras
	
FinAlgoritmo
