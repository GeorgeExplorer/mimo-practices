# 🐸 The Wide-Mouthed Frog

## 🎯 Goal / Цель задачи

**ENG:**  
Practice using conditional statements (`if-else`) and string comparison with case-insensitive matching to solve a fun logic problem.

**RUS:**  
Практика использования условных операторов (`if-else`) и сравнения строк без учёта регистра для решения забавной логической задачи.

---

## 📌 Description (ENG)

The wide-mouthed frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But then he meets the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, he makes a tiny mouth.

**Your goal** in this kata is to create and complete the `mouth_size` method. This method takes one argument `animal` which corresponds to the animal encountered by the frog.

**Requirements:**
- If the animal is an **alligator** (case-insensitive), return `"small"`
- Otherwise, return `"wide"`

---

## 📌 Описание (RUS)

Лягушка с широким ртом очень интересуется пищевыми привычками других существ.

Она не может перестать спрашивать встреченных существ о том, что они любят есть. Но затем она встречает аллигатора, который просто ОБОЖАЕТ есть лягушек с широким ртом!

Когда она встречает аллигатора, она делает крошечный рот.

**Твоя задача** в этом ката — создать и завершить метод `mouth_size`. Этот метод принимает один аргумент `animal`, который соответствует животному, встреченному лягушкой.

**Требования:**
- Если животное — **аллигатор** (без учёта регистра), вернуть `"small"`
- В противном случае вернуть `"wide"`

---

## ✅ Example Output

```python
mouth_size("toucan")
# Output: "wide"

mouth_size("ant bear")
# Output: "wide"

mouth_size("alligator")
# Output: "small"

mouth_size("ALLIGATOR")
# Output: "small"

mouth_size("AlLiGaToR")
# Output: "small"
```

---

## 💡 Hints / Подсказки

**ENG:**  
- Use the `.lower()` method to make the comparison case-insensitive
- A simple `if-else` statement is all you need

**RUS:**  
- Используй метод `.lower()` для сравнения без учёта регистра
- Для решения достаточно простого оператора `if-else`