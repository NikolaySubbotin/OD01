# Вводим слово.
# Убираем все пробелы.
# Переворачиваем слово.
# Сравниваем введеное слово с перевернутым.
# Если они равны, то слово является палиндромом.
# Если не равны, то слово не является палиндромом

def is_palindrome(s):
    s = s.replace(' ', '')
    reversed_string = s[::-1]
    return s == reversed_string


# Примеры использования
print(is_palindrome("level"))
print(is_palindrome("name"))  