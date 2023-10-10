from rdflib import Graph, BNode, Literal, Namespace, RDF
from pint import Quantity

class RDFGenerator:
    def __init__(self):
        self.graph = Graph()
        self.qudt = Namespace("http://qudt.org/schema/qudt#")

    def generate_rdf(self, unit: Quantity) -> str:
        if not isinstance(unit, Quantity):
            raise ValueError("The 'unit' parameter must be an instance of 'pint.Quantity'.")
        
        node = BNode()
        self.graph.add((node, RDF.type, self.qudt.Unit))
        self.graph.add((node, self.qudt.symbol, Literal(str(unit.units))))
        self.graph.add((node, self.qudt.conversionMultiplier, Literal(float(unit.magnitude))))
        return self.graph.serialize(format='xml').decode('utf-8')
