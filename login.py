# login.py
guards = {
    "G123": "pass123",
    "G456": "admin456"
}

def login_user(badge, password):
    if badge in guards and guards[badge] == password:
        return True, "Login successful"
    return False, "Invalid credentials"
  
