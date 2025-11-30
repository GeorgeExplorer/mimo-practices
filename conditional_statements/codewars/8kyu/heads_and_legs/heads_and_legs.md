# Heads and Legs (8 kyu)

**Languages / Языки:** Python, TypeScript  
**Topic / Тема:** Conditional Statements, basic arithmetic, edge cases

---

## 📄 Original Description (English)

**Description**  

Everybody has probably heard of the animal heads and legs problem from the earlier years at school.  
It goes:

>“A farm contains chickens and cows.  
>There are `x` heads and `y` legs.  
>How many chickens and cows are there?”  
>Where `x <= 1000` and `y <=1000`  

**Task**  

Assuming there are no other types of animals, work out how many of each animal are there.

Return a **tuple** in Python
- `(chickens, cows)`  
- or **an array list** `[chickens, cows] / {chickens, cows}` in all other languages  

If either 
- the heads & legs is negative
- the result of your calculation is negative
- or the calculation is a float

return **"No solutions"** (no valid cases), or `[-1, -1]` in COBOL (we don't need it).

**In the form**:

For input:
`(Heads, Legs) = (72, 200)`

*VALID solution*

`(72, 200) => (44 , 28)`

Where `(Chickens, Cows)` = `(44, 28)`

*INVALID solution*

`(72, 201)` => `"No solutions"`  
However, if `0` heads and `0` legs are given always return `[0, 0]` since zero heads must give zero animals.

There are many different ways to solve this, but they all give the same answer.

You will only be given **integers** types - however **negative** values (edge cases) will be given.

Happy coding!

---

## 🇷🇺 Перевод на русский

**Описание**

Наверняка почти каждый сталкивался в школе с задачей про головы и ноги животных.  
Она формулируется так:

> «На ферме есть куры и коровы.  
> Всего на ферме `x` голов и `y` ног.  
> Сколько на ферме кур и коров?»  

Где `x <= 1000` и `y <= 1000`.

**Задача**

Считая, что других типов животных нет, нужно определить, **сколько кур** и **сколько коров** находится на ферме.

- В Python нужно вернуть **кортеж** вида `(chickens, cows)`.  
- В остальных языках — **массив / список** `[chickens, cows]` или `{chickens, cows}`.

Если:

- количество голов или ног отрицательное,  
- или в результате вычислений получается отрицательное число животных,  
- или расчёт даёт нецелое число (дробь),

то нужно вернуть **"No solutions"** (нет корректных вариантов).  
(В COBOL — `[-1, -1]`, но нам это не нужно.)

**Формат примеров**

Для входных данных:

`(Heads, Legs) = (72, 200)`

Корректное решение (VALID):

`(72, 200) => (44, 28)`  
где `(Chickens, Cows)` = `(44, 28)`.

Некорректное решение (INVALID):

`(72, 201) => "No solutions"`

Однако, если переданы `0` голов и `0` ног, всегда возвращаем `[0, 0]`,  
так как ноль голов означает ноль животных.

Существует много разных способов решить эту задачу,  
но все корректные способы дают один и тот же ответ.

На вход всегда подаются **целые числа**,  
но среди них могут быть и **отрицательные** значения (граничные случаи).

---

## 🎯 Goal / Цель задачи

Реализовать функцию, которая:

1. Принимает два целых числа:
   - `heads` — количество голов;
   - `legs` — количество ног.
2. Возвращает:
   - количество кур и коров, если есть хотя бы одно корректное решение;
   - строку `"No solutions"`, если задача не имеет корректного решения.

---

## 📌 Function Signatures

### Python ###

```python
def animals(heads: int, legs: int):
    """
    Return (chickens, cows) as a tuple,
    or "No solutions" as a string if there is no valid answer.
    """
    ...
```

### Typescript ### 

```typescript
export function animals(heads: number, legs: number): [number, number] | "No solutions" {
   "Return [countOfChickens, countOfCows]"
}
```

