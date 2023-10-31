import random
import json


f = open('/Users/viktor.lenard/Desktop/key/words.json')
data = json.load(f)

def password_generator(human, length, div):
    password = ''
    if length < 3 or length > 6:
        raise ValueError('Invalid lenght. Must be between 3-6.')
    if div not in ['-', '.', '_']:
        raise ValueError('Invalid divider. Must be "." "_" "-" ')
    if human is True:
        word1 = random.choice(list(data.keys()))
        word2 = random.choice(list(data.keys()))
        word3 = random.choice(list(data.keys()))
        password = word1 + div + word2 + div + word3
    else:
        ...
    
    return password

password = password_generator(True, 3, '-')
print(password)

''' if __name__ == "__main__":
    main() '''