import hashlib

def analyse_hash(hash, file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip()
            if hash == hashlib.md5(password.encode()).hexdigest():
                return password
        return None