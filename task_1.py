import re

car_numbers_list = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "123BB59",
                    "K000MH59", "K007MH59", "1AAABA234", "O001OO159"]
car_numbers_list = ' '.join(car_numbers_list)

pattern = r'[АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}(?<!000)[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2,3}\b'
list_result = list(re.findall(pattern, car_numbers_list))
print(list_result)
