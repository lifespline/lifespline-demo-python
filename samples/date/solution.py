from datetime import date

today = date.today()

# get current date formatter as DD-MM-YYYY
tday = today.strftime("%d-%m-%Y")
print(tday)