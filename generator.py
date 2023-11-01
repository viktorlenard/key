import random
import json
import string


f = open('/Users/viktorlenard/Desktop/Repos/key/words.json')
data = json.load(f)

password_request = {
    'human': False,
    'length': 3,
    'div': '_',
    'caps': True,
    'nums': True,
    'valid': None
}

def request_validator(pr):
    if pr['human'] not in [True, False]:
       pr['valid'] = False
       raise ValueError('Invalid request. 1')
    if pr['length'] < 3 or pr['length'] > 8:
        pr['valid'] = False
        raise ValueError('Invalid request. 2')
    if pr['div'] not in ['.', '_', '-']:
        pr['valid'] = False
        raise ValueError('Invalid request. 3')
    if pr['caps'] not in [True, False]:
        pr['valid'] = False
        raise ValueError('Invalid request. 4')
    if pr['nums'] not in [True, False]:
        pr['valid'] = False
        raise ValueError('Invalid request. 5')
    
    pr['valid'] = True
    return pr

def password_generator(pr):
    if pr['valid'] != True:
        raise ValueError('Invalid request. Cannot generate.')
    words = []
    if pr['human'] is True:
        if pr['caps'] is True:
            for _ in range(pr['length'] - 1):
                words.append(random.choice(list(data.keys())).title())
                words.append(pr['div'])
            words.append(random.choice(list(data.keys())).upper())
        elif pr['caps'] is False:
            for _ in range(pr['length'] - 1):
                words.append(random.choice(list(data.keys())))
                words.append(pr['div'])
            words.append(random.choice(list(data.keys())))
        password = ''.join([str(item) for item in words])
        if pr['nums'] is True:
            numbers = ''.join(random.choice(string.digits)for i in range(2))
            password = password + numbers

    else:
        for _ in range(pr['length'] - 1):
            word = ''.join(random.choice(string.ascii_letters + string.digits + '!#$%&*') for i in range(random.randint(5, 8)))
            words.append(word)
            words.append(pr['div'])
        word = ''.join(random.choice(string.ascii_letters + string.digits + '!#$%&*') for i in range(random.randint(5, 8)))
        words.append(word)
        password = ''.join([str(item) for item in words])

    return password

def main():
    request_validator(password_request)
    password = password_generator(password_request)
    print(password)

if __name__ == "__main__":
    main()