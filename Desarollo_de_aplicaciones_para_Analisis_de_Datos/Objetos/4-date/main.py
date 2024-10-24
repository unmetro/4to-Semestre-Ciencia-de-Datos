from datetime import date

class Date(object):

    DIAS_SEMANA = ["DOMINGO", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO"]
    MESES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

    def __init__(self, day: int, month:int, year:int) -> None:
        if day < 1 or day > 31:
            self.day = 1
        else:
            self.day = day
        if month < 1 or month > 12:
            self.month = 1
        else:
            self.month = month
        if year < 1900 or year > 2050:
            self.year = 1900
        else:
            self.year = year
    
    @staticmethod
    def is_leap_year(year:int) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    
    @staticmethod
    def get_days_in_month(month:int, year:int) -> int:
        if month == 2:
            if Date.is_leap_year(year):
                return 29
            return 28
        if month in [4, 6, 9, 11]:
            return 30
        return 31
    
    def days_elapsed_full_years(self) -> int:
        days = 0
        for year in range(1900, self.year):
            if Date.is_leap_year(year):
                days += 366
            else:
                days += 365
        return days

    def days_elapsed_full_months(self) -> int:
        days = 0
        for month in range(1, self.month):
            days += Date.get_days_in_month(month, self.year)
        return days

    def get_delta_days(self) -> int:
        days = self.days_elapsed_full_years()
        days += self.days_elapsed_full_months()
        days += self.day - 1
        return days
    
    # Zeller Algorithm

    def weekday(self) -> int:
        month = self.month
        year = self.year
        if month < 3:
            month += 12
            year -= 1
        
        q = self.day
        m = month
        k = year % 100  # Últimos dos dígitos del año
        j = year // 100  # Primeros dos dígitos del año
        
        # Aplicando la fórmula de Zellera
        f = q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j
        week_day = f % 7
        
        # Ajustar el resultado al formato Domingo(0), Lunes(1), ..., Sábado(6)
        # Zeller devuelve: Sábado(0), Domingo(1), ..., Viernes(6)
        # Queremos: Domingo(0), Lunes(1), ..., Sábado(6)
        week_day = (week_day + 6) % 7  # Ajuste para que Domingo sea 0

        return week_day
    
    def is_weekend(self) -> bool:
        return self.weekday() == 0 or self.weekday() == 6
    
    def short_date(self) -> str:
        return f"{self.day:02}/{self.month:02}/{self.year:04}"
    
    def __str__(self) -> str:
        week_day = self.DIAS_SEMANA[self.weekday()]
        month_name = self.MESES[self.month - 1]
        return f"{week_day} {self.day} DE {month_name} DE {self.year}"

    
    def __add__(self, days_to_add: int) -> 'Date':
        new_day = self.day
        new_month = self.month
        new_year = self.year

        while days_to_add > 0:
            days_current_month = self.get_days_in_month(new_month, new_year)
            
            if new_day + days_to_add <= days_current_month:
                new_day += days_to_add
                break
            else:
                days_to_add -= (days_current_month - new_day + 1)
                new_day = 1 
                new_month += 1
                if new_month > 12:  
                    new_month = 1
                    new_day += 1
        return Date(new_day, new_month, new_year)
        
    def to_days(self) -> int:
        total_days = 0
        for year in range(1, self.year):
            total_days += 366 if self.is_leap_year(year) else 365
        for month in range(1, self.month):
            total_days += self.get_days_in_month(month, self.year)
        total_days += self.day
        return total_days

    def from_days(self, total_days: int) -> 'Date':
        year = 1
        while total_days > (366 if self.is_leap_year(year) else 365):
            total_days -= 366 if self.is_leap_year(year) else 365
            year += 1

        month = 1
        while total_days > self.get_days_in_month(month, year):
            total_days -= self.get_days_in_month(month, year)
            month += 1

        day = total_days
        return Date(day, month, year)

    def __sub__(self, other):
        if isinstance(other, Date):
            return abs(self.to_days() - other.to_days())
        elif isinstance(other, int):
            total_days = self.to_days() - other
            return self.from_days(total_days)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return False
        return self.day == other.day and self.month == other.month and self.year == other.year
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return False
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                return self.day > other.day
        return False
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return False
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False
    
if __name__ == "__main__":
    date1 = Date(day=1, month=3, year=1979) 
    date2 = Date(day=24, month=6, year=1984)
    print(date1)
    print(date2)
    print(date1 == date2)
    print(date1 < date2)
    print(date1 > date2)
    print(date1 + 10)
    print(date1 - 10)
    print(date1 - date2)
    print(date1.is_weekend())
    print(date2.is_weekend())
    print(date1.short_date())
    print(date2.short_date())
    print(date1.weekday())
    print(date2.weekday())
    print(date1.to_days())
    print(date2.to_days())
    print(date1.from_days(28913))
    print(date2.from_days(4748))

