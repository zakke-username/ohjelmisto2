from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku')
def alkuluku():
    n = int(request.args.get("luku"))
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                is_prime = False
    vastaus = {
        "Number": n,
        "isPrime": is_prime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)