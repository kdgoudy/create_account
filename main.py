print("Create your account")
user_name1 = input("Create user name: ")
password1 = input("Create password: ")

print("Account successfully create")
print("Login now")

user_name2 = input("Enter user name: ")
password2 = input("Enter password: ")

if user_name1 == user_name2 and password1 == password2:
  print("Logged in successfully")
else:
  print("Invalid credentials")
