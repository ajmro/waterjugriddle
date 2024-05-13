def jugs(x, y, z, bol=None): # Main algorithm
    if bol == True:
        de = y
        ha = x
        des = 'Y'
        has = 'X'
    else:
        de = x
        ha = y
        des = 'X'
        has = 'Y'
        
    a = de
    b = 0
    t = 1
    msg = 'Fill bucket '+des 
    res = {}
    
    while True:
        if des == 'Y':
            res['STEP '+str(t)] = { has: str(b), des: str(a), 'Explanation': msg}
        else:
            res['STEP '+str(t)] = { des: str(a), has: str(b), 'Explanation': msg}
        if a == z or b == z:
            res['STEP '+str(t)]['Explanation'] = res['STEP '+str(t)]['Explanation']+'. SOLVED'
            break
        if b == ha:
            b = 0
            msg = 'Empty bucket '+has
            t += 1
            continue
        if a == 0:
            a = de
            msg = 'Fill bucket '+des
            t += 1
            continue
        if (a + b) > ha:
            a = a - (ha - b)
            b = ha
            msg = 'Transfer from bucket '+des+' to bucket '+has
            t += 1
            continue
        b = a + b
        a = 0
        msg = 'Transfer from bucket '+des+' to bucket '+has
        t += 1
    return [res, t]
        
def gcd(a, b): # Greatest common divisor calculator
    if b == 0:
        return a
    return gcd(b, a % b)
        
def waterjug(x, y, z): # Data validation and output formatting
    values = {'X': x, 'Y': y, 'Z': z}
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x <= 0 or y <= 0 or z <= 0:
            return {'Error': 'One of the variables is not greater than 0', 'Values': values}
        if z > x and z > y:
            return {'Error': 'Z is greater than X and Y', 'Values': values}
        mcd = gcd(x, y)
        if z % mcd != 0:
            return {'Error': 'No Solution', 'Values': values}
    else:
        return {'Error': 'One of the variables is not an integer', 'Values': values}
    
    res1 = jugs(x, y, z)
    res2 = jugs(x, y, z, True)
    if res1[1] > res2[1]:
        solution = res2[0]
    else:
        solution = res1[0]
    res = {
        'Values': values,
        'Best Solution': str(min(res1[1], res2[1]))+' steps',
        'Worst Solution': str(max(res1[1], res2[1]))+' steps',
        'Best Solution step-by-step': solution 
    }
    return res

# Server code
    
import json 
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_params = json.loads(post_data)
        
            x = request_params['X']
            y = request_params['Y']
            z = request_params['Z']
            
            body = waterjug(x, y, z)
            response = body
            self.wfile.write(json.dumps(response).encode())
        except:
            response = {
                'Error': 'Invalid body format',
                'Example body (keys are case-sensitive)': {'X': 5, 'Y': 3, 'Z': 4}
            }
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8000), Handler)
        print('Starting server at http://localhost:8000')
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print('Stopping by Ctrl+C')
        server.server_close()
        
