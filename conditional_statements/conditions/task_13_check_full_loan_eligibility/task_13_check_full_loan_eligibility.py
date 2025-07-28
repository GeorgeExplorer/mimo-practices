# set and determine the variables
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
experience =  float(input("Enter your work experience in full or partial years (e.g 2 years; 5.5 years; etc): "))
is_vip_req = input("Are you VIP customer? (yes=1/no=0) ")
is_vip = is_vip_req.strip() == "1" or is_vip_req.lower() == "yes"

# basic conditions
if age in range (21, 71) and income >= 30000 and 2 <= experience <= 40:
  print(" Eligible for loan")
elif age in range (21, 71) and income < 30000 and 2 <= experience <= 40 and is_vip:
  print("Eligible for loan")
# an advance condition in otherwise cases 
else:
  if age not in range(21, 71):
    print("Ineligible: age out of range")
  if income < 30000:
    print("Ineligible: income too low")
  if experience < 2 or experience > 40:
    print("Ineligible: invalid experience")
