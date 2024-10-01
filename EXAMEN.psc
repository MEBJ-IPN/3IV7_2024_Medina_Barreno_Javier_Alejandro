Algoritmo EXAMEN
	
	Escribir "Introducir número de personas por registrar:"
	Leer n
	
	Definir fn, ff, r, f, u Como Entero
	Dimension fn(n)
	Dimension ff(n)
	
	
	Para i=1 Hasta n Con Paso 1
		r <- 1
		Mientras r = 1 Hacer
			f <- 1
			Mientras f = 1 Hacer
				Escribir "Introducir fecha de nacimiento de persona ", i, ":"
				Leer fn(i)
				Si fn(i) >= 0 y fn(i) <= 2024 Entonces
					f <- 0
				SiNo	
					Escribir "Introducir un valor dentro del parametro (0-2024)"
					f <- f
				FinSi
			FinMientras
			u <- 1
			Mientras u = 1 Hacer
				Escribir "Introducir fecha de fallecimiento de persona ", i, ":"
				Leer ff(i)
				Si ff(i) >= 0 y ff(i) <= 2024 Entonces
					u <- 0
				SiNo
					Escribir "Introducir un valor dentro del parametro (0-2024)"
					u <- u
				FinSi
			FinMientras
			Si ff(i) >= fn(i) Entonces
				r <- 0
			SiNo
				Escribir "Introducir una fecha de fallecimiento mayor a la de nacimiento"
				r <- 1
			FinSi
		FinMientras
	FinPara
	
	Definir ar Como Entero
	p <- 1
	Mientras p = 1 Hacer
		Escribir "Introducir año de referencia:"
		Leer ar
		Si ar <= 2024 y ar >= 0 Entonces
			p <- 0
		SiNo
			Escribir "Introducir un valor dentro del parametro (0-2024)."
			p <- 1
		FinSi
	FinMientras

	
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
