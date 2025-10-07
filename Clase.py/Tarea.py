import re
COMMON_PASSWORDS = {
    "123", "321"
}
passwords = []
for i in range(3):
    password = input(f"Ingrese la contraseña #{i + 1}: ")
    passwords.append(password)  
def is_weak_password(password):  
    if password.lower() in COMMON_PASSWORDS:
        print("Contraseña común e insegura.")
        return True 
    if len(password) < 6:
        print("Contraseña demasiado débil.")
        return True
    print("Contraseña segura.")
    return False
for i, pwd in enumerate(passwords, 1):
    print(f"\nVerificando la contraseña #{i}: {pwd}")
    is_weak_password(pwd)



    



