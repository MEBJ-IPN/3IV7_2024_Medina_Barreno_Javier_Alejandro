Algoritmo COBRAR
	Definir horaentrada, minutoentrada, horasalida, minutosalida Como real
	Definir toalHoras, totalMinutos, minutostotalescuenta Como real
	Definir totalcobro Como real
	
	//entrada de datos
	
	Escribir "Ingrese la hora de entrada (formato de 24 horas)"
	Leer horaentrada
	Escribir "Ingrese los minutos de entrada (formato de 0 - 59)"
	Leer minutoentrada
	Escribir "Ingrese la hora de salida (formato de 24 horas)"
	Leer horasalida
	Escribir "Ingrese los minutos de salida (formato de 0 - 59)"
	Leer minutosalida
	
	//Proceso
	//caluclar tiempo total en minutos
	
	totalHoras = horasalida - horaentrada
	totalMinutos = minutosalida - minutoentrada
	
	//evaluar casos
	
	Si totalMinutos<0 Entonces
		totalMinutos = totalMinutos+60
		//totalMinutos += 60
		totalHoras = totalHoras-1
		//totalHoras -=1
	FinSi
	
	//convertir a minutos
	
	totalMinutos = (totalHoras*60)+totalMinutos
	//totalMinutos += totalHoras*60
	
	//calcular cobro
	totalcobro = 0
	
	//calcular el cobro por hora completa
	
	Si totalMinutos >= 60 Entonces
		totalcobro = totalcobro + (totalMinutos/60)*15
	FinSi
	
	//calcular el cobro de cada fracción
	
	minutosrestantes = totalMinutos%60
	
	Si minutosrestantes>0 Entonces
		fracciones15min = mintosrestantes 
		
		//cobrar
		
		totalcobro = totalcobro + fracciones15min * 6
	FinSi
	
 Escribir "El total a pagar es de: ", totalcobro, " pesos" 
	

	
FinAlgoritmo
