import re 


def normalize_phone(phone_number: str) -> str:
    formatiing_nambers = re.sub(r'[^\d+]', '',phone_number)
    if  formatiing_nambers.startswith('+38'):
        return formatiing_nambers
    elif formatiing_nambers.startswith('380'):
        return '+' + formatiing_nambers
    else:
        return '+38' + formatiing_nambers
    
    
different_numbers = [
    "    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11  ",
]
    
sanitized_numbers = [normalize_phone(num) for num in different_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)       