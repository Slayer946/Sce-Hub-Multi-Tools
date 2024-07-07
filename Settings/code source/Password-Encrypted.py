from Config.Util import *
from Config.config import *
import bcrypt
import hashlib
import base64
from hashlib import pbkdf2_hmac

# Définition de la bannière pour l'encryption
encrypted_banner = """
*************************************
*       Password Encrypted         *
*************************************
"""

try:
    Title("Password Encrypted")
    Slow(f"""{encrypted_banner}
{white}[{red}01{white}] {red}->{white} BCRYPT
{white}[{red}02{white}] {red}->{white} MD5
{white}[{red}03{white}] {red}->{white} SHA-1
{white}[{red}04{white}] {red}->{white} SHA-256
{white}[{red}05{white}] {red}->{white} PBKDF2 (SHA-256)
{white}[{red}06{white}] {red}->{white} Base64 Encode
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Encryption Method -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password to Encrypt -> {white}")

    # Fonction pour encrypter le mot de passe selon le choix
    def encrypt_password(choice, password):
        if choice in ['1', '01']:
            try:
                salt = bcrypt.gensalt()
                encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                return encrypted_password.decode('utf-8')
            except Exception as e:
                Error(f"Error encrypting with BCRYPT: {e}")
        elif choice in ['2', '02']:
            try:
                encrypted_password = hashlib.md5(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error(f"Error encrypting with MD5: {e}")
        elif choice in ['3', '03']:
            try:
                encrypted_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error(f"Error encrypting with SHA-1: {e}")
        elif choice in ['4', '04']:
            try:
                encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                return encrypted_password
            except Exception as e:
                Error(f"Error encrypting with SHA-256: {e}")
        elif choice in ['5', '05']:
            try:
                salt = "this_is_a_salt".encode('utf-8')
                encrypted_password = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
                return encrypted_password
            except Exception as e:
                Error(f"Error encrypting with PBKDF2 (SHA-256): {e}")
        elif choice in ['6', '06']:
            try:
                encrypted_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
                return encrypted_password
            except Exception as e:
                Error(f"Error encoding with Base64: {e}")
        else:
            return None

    encrypted_password = encrypt_password(choice, password)
    if encrypted_password:
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Encrypted Password: {white}{encrypted_password}{reset}")
        Continue()
        Reset()

except Exception as e:
    Error(e)
