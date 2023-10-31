import random
import json


f = open('/Users/viktorlenard/Desktop/Repos/key/words.json')
data = json.load(f)

def password_generator(human, length, div):
    if length < 3 or length > 6:
        raise ValueError('Invalid lenght. Must be between 3-6.')
    if div not in ['-', '.', '_']:
        raise ValueError('Invalid divider. Must be "." "_" "-" ')
    if human is True:
        words = []
        for _ in range(length - 1):
            words.append(random.choice(list(data.keys())))
            words.append(div)
        words.append(random.choice(list(data.keys())))
        
        password = ''.join([str(item) for item in words])
    else:
        ...
    
    return password

password = password_generator(True, 5, '.')
print(password)

''' if __name__ == "__main__":
    main() '''