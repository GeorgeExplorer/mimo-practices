
# 🔍 Task 11: Check Login

## 🎯 Goal / Цель задачи

**ENG:**  
Practice comparing strings and using multiple conditions to handle simple login logic.

**RUS:**  
Практика сравнения строк и использование нескольких условий для обработки простой логики входа.

---

## 📌 Description (ENG)

Write a program that checks the username and password.

1. Create two variables:
   - `username`: a string with any value.
   - `password`: a string with any value.

2. Your program should:
   - Print `"Access granted."` if `username` is `"admin"` **and** `password` is `"1234"`.
   - Print `"Wrong password."` if `username` is `"admin"` but the password is not `"1234"`.
   - Print `"Unknown user."` if `username` is not `"admin"`.

---

## 📌 Описание (RUS)

Напиши программу, которая проверяет имя пользователя и пароль.

1. Создай две переменные:
   - `username` — строка с любым значением.
   - `password` — строка с любым значением.

2. Твоя программа должна:
   - Вывести `"Access granted."`, если `username` равно `"admin"` **и** `password` равно `"1234"`.
   - Вывести `"Wrong password."`, если `username` равно `"admin"`, но пароль не `"1234"`.
   - Вывести `"Unknown user."`, если `username` не `"admin"`.

---

## ✅ Example Output

```python
username = "admin"
password = "1234"
# Output:
Access granted.
```

```python
username = "admin"
password = "0000"
# Output:
Wrong password.
```

```python
username = "guest"
password = "1234"
# Output:
Unknown user.
```
