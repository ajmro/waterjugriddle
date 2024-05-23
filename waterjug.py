import requests
import json

def waterjugrequest(x, y, z):
    data = {'X': x, 'Y': y, 'Z': z}
    try:
        r = requests.post('http://localhost:8000', json=data)
        return json.dumps(r.json(), indent=4)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
        
def execute():
    while True:
        try:
            a = int(input('Enter X value (greater than 0 integer): '))
            if a > 0:
                break
        except ValueError:
            pass
        
    while True:
        try:
            b = int(input('Enter Y value (greater than 0 integer): '))
            if b > 0:
                break
        except ValueError:
            pass
        
    while True:
        try:
            c = int(input('Enter Z value (greater than 0 integer): '))
            if c > 0:
                break
        except ValueError:
            pass

    print(waterjugrequest(a, b, c))
    
if __name__ == '__main__':
    execute()
