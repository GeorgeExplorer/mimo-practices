username = input("Enter your username: ")
password = input("Enter your password: ")

result_of_checking_creds = (
  "Access granted." if username == "admin" and password == "1234" else
  "Wrong password" if username == "admin" and password != "1234" else
  "Wrong username" if username != "admin" and password == "1234" else
  "User not found"
)

print(result_of_checking_creds)
