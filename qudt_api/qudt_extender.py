from typing import Optional
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS
from qudt_api.file_services import HttpCachedFile
from qudt_api.rdf import ONSUNITS, QUDTUNIT, ONSCURRENCIES, QUDTCURRENCY, QUDT


class Currency:
    currenceCode: str
    conversionMultiplier: Optional[float]
    label: Optional[str]

    def __init__(self, currenceCode: str, conversionMultiplier=None, label=None):
        self.full_graph = Graph()
        self.full_graph.bind("qudt", QUDT)
        self.full_graph.parse(
            HttpCachedFile("http://qudt.org/vocab/currency").filepath,
            format="ttl",
        )

        if not QUDTCURRENCY[currenceCode] in self.full_graph.subjects():
            raise ValueError(f"{currenceCode} is not a valid QUDT currency.")
        else:
            self.graph = Graph()
            self.graph.bind("qudt", QUDT)
            [
                self.graph.add(t)
                for t in self.full_graph.triples(
                    (QUDTCURRENCY[currenceCode], None, None)
                )
            ]

        if conversionMultiplier and label:
            self.extended_currency = ONSCURRENCIES[
                "".join([currenceCode, "#", str(conversionMultiplier)])
            ]
            self.graph.add(
                (self.extended_currency, QUDT.isScalingOf, QUDTCURRENCY[currenceCode])
            )
            self.graph.add(
                (
                    self.extended_currency,
                    QUDT.conversionMultiplier,
                    Literal(conversionMultiplier),
                )
            )
            self.graph.add((self.extended_currency, RDFS.label, Literal(label)))
        elif not (conversionMultiplier or label):
            pass
        else:
            raise ValueError(f"Both conversionMultiplier and label must be provided.")


class Unit:
    unit: str
    conversionMultiplier: Optional[float]
    label: Optional[str]

    def __init__(self, unit: str, conversionMultiplier=None, label=None):
        self.full_graph = Graph()
        self.full_graph.bind("qudt", QUDT)
        self.full_graph.parse(
            HttpCachedFile("http://qudt.org/vocab/unit").filepath, format="ttl"
        )

        if not QUDTUNIT[unit] in self.full_graph.subjects():
            raise ValueError(f"{unit} is not a valid QUDT unit.")
        else:
            self.graph = Graph()
            self.graph.bind("qudt", QUDT)
            [
                self.graph.add(t)
                for t in self.full_graph.triples((QUDTUNIT[unit], None, None))
            ]

        if conversionMultiplier and label:
            self.extended_unit = ONSUNITS[
                "".join([unit, "#", str(conversionMultiplier)])
            ]
            self.graph.add((self.extended_unit, QUDT.isScalingOf, QUDTUNIT[unit]))
            self.graph.add(
                (
                    self.extended_unit,
                    QUDT.conversionMultiplier,
                    Literal(conversionMultiplier),
                )
            )
            self.graph.add((self.extended_unit, RDFS.label, Literal(label)))
        elif not (conversionMultiplier or label):
            pass
        else:
            raise ValueError(f"Both conversionMultiplier and label must be provided.")
