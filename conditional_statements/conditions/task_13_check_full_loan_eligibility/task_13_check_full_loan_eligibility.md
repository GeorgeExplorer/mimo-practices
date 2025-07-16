
# 🔍 Task 13: Check Full Loan Eligibility

## 🎯 Goal / Цель задачи

**ENG:**  
Practice using `if-elif-else`, `and`, `or`, chain comparison, and `range` to decide if a person is eligible for a loan based on multiple conditions.

**RUS:**  
Практика использования `if-elif-else`, `and`, `or`, цепного сравнения и `range` для решения, может ли человек получить кредит на основе нескольких условий.

---

## 📌 Description (ENG)

Write a program that checks if a person can get a full loan based on:

- `age`: integer
- `income`: integer (monthly)
- `experience`: integer (years of work experience)
- `is_vip`: boolean

**Conditions:**  
- If age is between 21 and 70 inclusive and income is greater than or equal to 30,000 and work experience is at least 2 years → print `"Eligible for loan"`

- If the person is a VIP and age is valid, they can get the loan even if income is lower than 30,000.

- Otherwise:
  - If age is out of range → print `"Ineligible: age out of range"`
  - If income is too low → print `"Ineligible: income too low"`
  - If experience is too low → print `"Ineligible: insufficient experience"`

---

## 📌 Описание (RUS)

Напиши программу, которая проверяет, может ли человек получить полный кредит, основываясь на:

- `age`: целое число
- `income`: целое число (ежемесячный доход)
- `experience`: целое число (лет опыта работы)
- `is_vip`: булево значение (True или False)

**Условия:**  
- Если возраст от 21 до 70 включительно, доход не меньше 30,000 и опыт работы не меньше 2 лет → вывести `"Eligible for loan"`

- Если человек VIP и возраст подходит, можно выдать кредит даже если доход меньше 30,000.

- В остальных случаях:
  - Если возраст вне диапазона → вывести `"Ineligible: age out of range"`
  - Если доход слишком низкий → вывести `"Ineligible: income too low"`
  - Если стаж работы меньше 2 лет → вывести `"Ineligible: insufficient experience"`

---

## ✅ Example Output

```python
age = 35
income = 50000
experience = 5
is_vip = False
# Output:
Eligible for loan
```

```python
age = 25
income = 20000
experience = 5
is_vip = True
# Output:
Eligible for loan
```

```python
age = 25
income = 20000
experience = 1
is_vip = False
# Output:
Ineligible: insufficient experience
```

```python
age = 18
income = 40000
experience = 2
is_vip = False
# Output:
Ineligible: age out of range
```
