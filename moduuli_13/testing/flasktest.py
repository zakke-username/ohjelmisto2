from flask import Flask, request

app = Flask(__name__)

@app.route('/kaiku/<teksti>')
def kaiku(teksti):
    vastaus = {
        "kaiku": teksti + " " + teksti
    }
    return vastaus

@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2
    division = luku1 / luku2
    sq1 = luku1 * luku1
    sq2 = luku2 * luku2

    vastaus = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa,
        "division": division,
        "sq1": sq1,
        "sq2": sq2
    }

    return vastaus

@app.route('/multiply')
def multiply():
    args = request.args
    nimi = str(args.get("nimi"))
    if nimi != "None":
        return f"Moi {nimi}"
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    return str(luku1 * luku2)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
