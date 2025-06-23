# 🔍 Task 8: Check Multiple Conditions

## 🎯 Goal / Цель задачи

**ENG:**  
Practice using multiple Boolean expressions combined with logical operators (`and`, `or`, `not`) to evaluate complex conditions.

**RUS:**  
Практика использования нескольких логических выражений, объединённых с помощью операторов (`and`, `or`, `not`) для проверки сложных условий.

---

## 📌 Description (ENG)

You are building a simple access control system.

Create two variables:  
- `is_admin`: a boolean indicating if the user is an admin.  
- `is_verified`: a boolean indicating if the user’s email is verified.

Now write a condition that prints:
- `"Access granted"` if the user is **either** an admin **or** a verified user.
- `"Access denied"` otherwise.

---

## 📌 Описание (RUS)

Ты создаёшь простую систему контроля доступа.

Создай две переменные:  
- `is_admin` — булева переменная, указывающая, является ли пользователь админом.  
- `is_verified` — булева переменная, указывающая, подтверждена ли электронная почта пользователя.

Теперь напиши условие, которое:
- Выводит `"Access granted"`, если пользователь — **админ** **или** подтверждённый.
- В противном случае выводит `"Access denied"`.

---

## ✅ Example Output

```python
is_admin = False
is_verified = True

# Output:
Access granted
```

```python
is_admin = False
is_verified = False

# Output:
Access denied
```
