from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

#DATE trzeba podac rok miesiac i dzien KONIECZNIE bo inaczej nie zadziala
#x = timedelta(1)
#y = date(2026,5,1)
#z = y + x
#print(y)
#TIMEDELTA mozna dodawac i odejmowac okreslona ilosc czasu - w tym przypadku bedziesz dodawac po 1 dzien

class CalendarValidationError(Exception):
        def __init__(self, year_value: int, month_value: int, first_day_val: int):
            self.year_value = year_value
            self.month_value = month_value
            self.first_day_val = first_day_val
             
            if not (isinstance(year_value, int) and isinstance(month_value, int) and isinstance(first_day_val, int)):
                self.message = 'The variable must be of type int!'
                super().__init__(self.message)
                raise self
            
            if not (0 <= first_day_val <= 6):
                self.message = 'The "first_day" variable must be in the range 0 to 6!'
                super().__init__(self.message)
                raise self
            
            if not (1 <= month_value <= 12):
                self.message = 'The "month" variable must be in the range 0 to 12!'
                super().__init__(self.message)
                raise self
            
class Calendar:
    def __init__(self, year: int, month: int, first_day = 0):
        CalendarValidationError(year, month, first_day)
        self.year = year
        self.month = month

        first_day_of_month = date(self.year, self.month, 1)
        first_day_of_month = date.weekday(first_day_of_month)

        last_day_of_month = first_day_of_month + relativedelta(months=+1) #brak mozliwosci dodania 1 miesiaca za pomoca timedelta 

        print(last_day_of_month)




    




        

    #def first_day():
        #fdom = date()
    #1 dzien miesiaca jaki to dzien tygodnia sprawdz

    #def last_day():
    #ostatni dzien miesiaca

    
Calendar(2021, 8)
    
    


#obsluga bledow screen 
#first day to ma byc opcjonalny argument do podania przez uzytkownika


# najpierw sprawdzam 1 dzien danego miesiaca jaki to dzien tygodnia
# ostatni dzien jaki to dzien tygodnia
# 