from datetime import datetime

def get_days_from_today(date: str) ->int:
    try:
        targer_day = datetime.strptime(date,  "%Y-%m-%d").date()
        today_day = datetime.today().date()
        difference = today_day - targer_day
        
        return difference.days
    except ValueError:
        print("Wrong date format. Please enter the date in the correct format PPPP.MM.DD, for example(2020.10.09)")
        

print(get_days_from_today('2020-10-09'))
    