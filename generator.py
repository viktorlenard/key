import random
import json


f = open('/Users/viktorlenard/Desktop/Repos/key/words.json')
data = json.load(f)

password_request = {
    'human': True,
    'length': 3,
    'div': '-',
    'caps': False,
    'nums': False,
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
    if pr['human'] is True:
        words = []
        for _ in range(pr['length'] - 1):
            words.append(random.choice(list(data.keys())))
            words.append(pr['div'])
        words.append(random.choice(list(data.keys())))
        
        password = ''.join([str(item) for item in words])
    else:
        ...
    
    return password

def main():
    request_validator(password_request)
    password = password_generator(password_request)
    print(password)

if __name__ == "__main__":
    main()