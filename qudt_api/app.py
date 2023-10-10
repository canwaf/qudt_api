## app.py
from flask import Flask, request
from flask_restful import Api, Resource
from unit_converter import UnitConverter
from rdf_generator import RDFGenerator

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.unit_converter = UnitConverter()
        self.rdf_generator = RDFGenerator()
        self.setup_routes()

    def setup_routes(self):
        self.api.add_resource(ExtendUnit, "/extend_unit", resource_class_args=(self.unit_converter, self.rdf_generator))

    def run(self):
        self.app.run(debug=True)

class ExtendUnit(Resource):
    def __init__(self, unit_converter: UnitConverter, rdf_generator: RDFGenerator):
        self.unit_converter = unit_converter
        self.rdf_generator = rdf_generator

    def post(self):
        unit = request.json.get('unit')
        scaling_factor = request.json.get('scaling_factor')
        label = request.json.get('label')

        if not unit or not scaling_factor or not label:
            return "Missing parameters: 'unit', 'scaling_factor', and 'label' are required.", 400

        new_unit = self.unit_converter.extend_unit(unit, scaling_factor, label)
        rdf_string = self.rdf_generator.generate_rdf(new_unit)

        return rdf_string, 200, {'Content-Type': 'application/xml'}

if __name__ == "__main__":
    app = FlaskApp()
    app.run()
