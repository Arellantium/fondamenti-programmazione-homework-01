# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''
import time

def ex1(int_seq, subtotal):
    
    numbers = [eval(x) for x in int_seq.split(',')]
    result = 0
    fine_lista = False

    while fine_lista == False:
        sum_substring = 0
        indice_lista = 0

        for x in numbers:
            sum_substring += x

            if sum_substring == subtotal:
                result += 1
                while numbers[indice_lista+1] == 0:
                    result += 1
                    indice_lista += 1

                numbers.pop(0)
                break  
            elif sum_substring > subtotal:
                numbers.pop(0)
                break
            
            if len(numbers)-1 == indice_lista:
                fine_lista = True
                break

            indice_lista += 1
    return result
    
if __name__ == '__main__':

    st = time.time()

    int_seq = "2,9,1,4,1,7,7,7,6,3,1,7,0,6,6,9,0,7,4,3,9,1,5,0,0,0,8,0,6,3,6,0,8,3,7,7,8,3,5,3,3,7,4,0,6,8,1,2,4,1,5,8,6,8,3,4,4,9,7,8,6,9,0,7,3,6,6,2,5,8,5,1,7,8,1,2,8,6,5,7,0,7,0,4,9,9,9,6,2,2,8,3,0,3,8,8,3,6,8,5,9,5,7,4,8,9,0,6,8,2,8,8,3,6,0,7,5,9,8,3,8,6,7,5,6,5,0,8,8,9,9,5,7,9,0,3,2,8,9,2,1,8,4,0,1,1,0,7,0,4,3,4,1,9,2,5,4,1,2,2,4,8,2,4,4,7,5,7,7,1,0,4,6,5,6,3,4,1,4,8,3,9,6,0,3,0,6,2,0,2,7,8,6,8,3,8,7,3,8,0,6,9,5,6,0,4,2,3,0,4,1,1,4,4,2,6,9,4,2,0,8,0,9,3,9,7,2,9,8,0,6,3,5,1,3,9,6,9,3,7,1,6,4,8,7,0,5,9,6,4,0,2,3,5,9,2,5,6,3,4,1,6,8,5,8,7,8,3,1,0,1,2,2,2,8,3,4,5,9,8,4,5,5,5,1,4,3,9,7,2,9,8,1,5,0,6,1,6,2,2,5,1,9,9,6,1,9,8,3,9,1,4,5,4,9,8,1,7,4,1,0,4,0,9,0,1,6,1,0,3,3,9,6,2,1,7,2,3,2,1,6,6,8,4,8,4,7,5,1,3,5,0,0,0,4,9,5,7,6,5,6,1,1,5,9,7,1,4,3,9,8,7,5,4,2,8,3,4,3,3,5,1,4,1,7,1,9,5,3,6,4,0,5,2,5,9,4,3,5,1,8,9,9,9,1,3,3,0,3,6,1,4,8,1,1,0,0,4,5,7,7,2,1,8,5,1,8,2,2,2,2,5,4,1,8,9,4,2,3,2,8,0,5,9,8,3,2,4,6,8,2,0,3,4,1,7,6,8,4,8,7,8,7,0,6,5,2,4,7,0,6,9,0,0,5,9,2,9,2,2,4,4,6,9,6,2,9,1,3,7,0,2,8,5,8,7,3,3,5,7,7,3,6,5,8,9,4,3,0,1,8,5,2,8,3,4,4,4,8,5,2,7,9,1,1,9,8,9,6,2,2,4,6,3,9,0,7,6,5,6,8,2,8,0,8,1,4,1,4,1,2,9,1,7,3,6,6,6,2,5,7,2,9,7,3,1,6,9,8,6,1,4,4,3,6,8,0,3,8,7,9,0,0,9,3,4,3,2,4,2,8,3,4,4,9,4,7,2,8,5,7,6,1,3,9,6,3,4,1,0,1,9,0,8,4,2,1,8,5,9,4,6,8,5,8,5,0,1,7,7,5,4,8,6,5,9,7,1,6,6,3,8,0,4,9,8,3,7,9,8,6,4,2,7,9,8,3,5,8,0,6,9,6,6,5,9,9,1,7,3,4,0,6,2,6,4,2,1,9,0,5,4,6,8,4,2,7,4,7,2,7,8,0,4,8,1,9,6,1,5,1,7,0,2,8,2,1,6,4,9,4,3,8,3,3,5,4,1,1,8,5,7,8,8,0,2,4,8,4,5,9,3,6,8,6,2,7,4,9,5,3,4,9,3,0,9,6,5,6,3,4,3,1,2,9,7,9,2,9,4,7,8,2,2,2,7,5,4,6,3,1,3,4,1,1,3,6,5,7,1,2,0,0,9,0,3,0,7,8,9,7,5,4,1,9,2,1,3,6,3,7,7,6,2,3,3,4,7,8,9,6,3,7,4,5,7,9,1,3,1,0,0,0,7,5,6,9,4,3,6,2,2,0,0,6,2,8,0,9,6,4,2,1,7,4,0,0,8,0,8,2,0,4,1,6,1,3,0,7,2,4,3,7,6,5,4,4,3,3,0,9,9,2,5,6,9,8,8,0,5,8,6,8,3,8,6,1,4,9,1,4,2,1,2,0,3,6,0,0,1,8,7,8,5,1,5,0,2,8,0,7,2,6,7,0,8,4,1,4,5,1,4,0,6,0,4,5,2,4,6,1,4,1,6,3,8,8,3,5,5,8,6,9,7,1,2,7,8,8,9,8,8,0,4,2,3,5,6,8,5,1,6,5,2,9,1,0,4,8,5,6,4,5,5,4,5,8,8,0,8,1,2,5,5,5,9,1,7,4,7,7,5,6,1,9,0,2,0,8,7"
    subtotal = 11

    risultato = ex1(int_seq, subtotal)
    print(f'risultato: {risultato}')

    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    final_res = elapsed_time * 1000
    print('Execution time:', final_res, 'milliseconds')
