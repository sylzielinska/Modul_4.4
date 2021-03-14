import sys
import logging
logging.basicConfig(level=logging.DEBUG)

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
first_step = float(input("Podaj składnik 1. "))
second_step = float(input("Podaj składnik 2. "))
#operation_list = list("Dodaję ", "Odejmuję ", "Mnożę ", "Dzielę ")
if operation == 1:
    logging.info("Dodaję " + str(first_step) + " i " + str(second_step))
    logging.info("Wynik to " + str(first_step + second_step))
elif operation == 2:
    logging.info("Odejmuję " + str(first_step) + " i " + str(second_step))
    logging.info("Wynik to " + str(first_step - second_step))
elif operation == 3:
    logging.info("Mnożę " + str(first_step) + " i " + str(second_step))
    logging.info("Wynik to " + str(first_step * second_step))
elif operation == 4 :
    logging.info("Dzielę " + str(first_step) + " i " + str(second_step))
    logging.info("Wynik to " + str(first_step / second_step))
else: logging.info("Podaj liczby z zakresu 1-4")


