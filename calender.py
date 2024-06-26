from datetime import datetime, timedelta

class CustomCalendar:
    def __init__(self, year, month, day):
        self.date = datetime(year, month, day)
        
    def add_days(self, days):
        self.date += timedelta(days=days)
        
    def is_leap_year(self):
        year = self.date.year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def format_date(self, format_str='%Y-%m-%d'):
        return self.date.strftime(format_str)
        
if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    
    my_calendar = CustomCalendar(year, month, day)
    
    days_to_add = int(input("Enter number of days to add: "))
    
    my_calendar.add_days(days_to_add)
    
    print("Is it a leap year?", my_calendar.is_leap_year())
    print("Formatted date:", my_calendar.format_date())