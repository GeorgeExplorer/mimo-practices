number = int(float(input("Enter any integer number: ")))

result_checked_number = (
  "Special number!" if number == 15 else
  "Number is in range" if number in range(10, 21) else
  "Number is too small" if number < 10 else
  "Number is too big" if number > 20 else
  "Number is undefined"
)

print(number)
print(result_checked_number)
