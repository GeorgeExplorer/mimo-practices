# Получаем значение от пользователя, как строку
value = input ("Enter your digit value: ")

# True, если число можно преобразовать в float: только одна точка и остальное цифры
is_available_convert_to_float = value.count(".") == 1 and value.replace(".", "").isdigit()

# True, если  не float и содержит только цифры
is_available_convert_to_int = not is_available_convert_to_float and value.isdigit()

# конвертируем value (string), в int, float или оставляем string
converted_value_to_other_types = (
  int(value) if is_available_convert_to_int else
  float(value) if is_available_convert_to_float else
  str(value)
)

# формируем текст на печать, в зависимости от типа данных
result = (
  "Integer number" if isinstance(converted_value_to_other_types, int) else
  "Float number" if isinstance(converted_value_to_other_types, float) else
  "String value"
)

# печатаем текст из переменной result
print(result)
