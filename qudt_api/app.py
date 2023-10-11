## app.py
from flask import Flask, request
# from flask_restful import Api, Resource
from qudt_api.qudt_extender import Unit, Currency

app = Flask(__name__)

formats = ["json-ld", "n3", "nquads", "nt", "hext", "pretty-xml", "trig", "trix", "turtle", "longturtle", "xml"]
    
@app.route("/unit/<unit>", methods=["GET", "POST"])
def unit(unit):
    conversion_multiplier = request.args.get("conversion_multiplier")
    label = request.args.get("label")
    format = request.headers.get(key="Accept", default="json-ld")
    if format == "*/*":
        format = "json-ld"
    if not format in formats:
        return "Invalid format. Please use one of the following: json-ld, n3, nquads, nt, hext, pretty-xml, trig, trix, turtle, longturtle, xml.", 400

    return Unit(unit, conversion_multiplier, label).graph.serialize(format=format), 200, {"Content-Type": f"application/rdf+{format}"}

@app.route("/currency/<currency>", methods=["GET", "POST"])
def currency(currency):
    conversion_multiplier = request.args.get("conversion_multiplier")
    label = request.args.get("label")
    format = request.headers.get(key="Accept", default="json-ld")
    if format == "*/*":
        format = "json-ld"
    if not format in formats:
        return "Invalid format. Please use one of the following: json-ld, n3, nquads, nt, hext, pretty-xml, trig, trix, turtle, longturtle, xml.", 400

    return Currency(currency, conversion_multiplier, label).graph.serialize(format=format), 200, {"Content-Type": f"application/rdf+{format}"}

if __name__ == "__main__":
    app.run(debug=True)
