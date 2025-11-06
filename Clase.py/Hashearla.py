import hashlib

texto = "oswaldo viejito"
hash_hex = hashlib.sha256(texto.encode()).hexdigest()
print("SHA-256:", hash_hex)