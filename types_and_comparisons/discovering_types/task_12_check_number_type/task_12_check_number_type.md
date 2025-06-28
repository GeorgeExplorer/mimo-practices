
# 🔍 Task 12: Check Number Type

## 🎯 Goal / Цель задачи

**ENG:**  
Practice discovering the type of user input using string methods, `type()` and `isinstance()`.

**RUS:**  
Практика определения типа введённого пользователем значения с помощью строковых методов, `type()` и `isinstance()`.

---

## 📌 Description (ENG)

Write a program that asks the user to enter any value.

1. Store the input in a variable `value`.

2. Your program should check:
   - If the value is all digits (use `.isdigit()`), convert it to `int` and check its type using `type()` or `isinstance()`. Print `"Integer number"` if it is an integer.
   - If the value contains a dot (`"." in value`) and can look like a float, you can convert it to `float` and check with `type()` or `isinstance()`. Print `"Float number"`.
   - If it doesn't match any of these, treat it as a string and print `"String value"`.

---

## 📌 Описание (RUS)

Напиши программу, которая просит пользователя ввести любое значение.

1. Сохрани введённое значение в переменную `value`.

2. Твоя программа должна проверить:
   - Если значение состоит только из цифр (используй `.isdigit()`), преобразуй его в `int` и проверь тип с помощью `type()` или `isinstance()`. Если это `int` — выведи `"Integer number"`.
   - Если значение содержит точку (`"." in value`) и похоже на число с точкой, преобразуй его в `float` и проверь тип. Если это `float` — выведи `"Float number"`.
   - Если не подходит ни одно из условий, считай это строкой и выведи `"String value"`.

---

## ✅ Example Output

```python
value = "15"
# Output:
Integer number
```

```python
value = "15.5"
# Output:
Float number
```

```python
value = "hello"
# Output:
String value
```

```python
value = "123abc"
# Output:
String value
```
