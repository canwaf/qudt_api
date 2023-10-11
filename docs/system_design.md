# Implementation approach

TODO: This is hilarious, MetaGPT wrote this, and tbh not entirely wrong, but wrong enough to require a complete rewrite. I'll rewrite this later. Never used flask before this though.

We will use the Flask framework to build the API, as it is lightweight and suitable for building APIs. We will use the rdflib library for generating RDF responses. For extending base QUDT units, we will use the pint library which provides a robust platform for working with units. We will use the flask-restful library to simplify the creation of API endpoints. The difficult points in the requirements are generating RDF responses and extending base QUDT units. We will overcome these by using the rdflib and pint libraries respectively.

## Python package name

qudt_api

## File list

- app.py
- unit_converter.py
- rdf_generator.py

## Data structures and interface definitions


    classDiagram
        class FlaskApp{
            +Flask app
            +Api api
            +__init__()
            +run()
        }
        class UnitConverter{
            +Pint.UnitRegistry ureg
            +__init__()
            +extend_unit(string: unit, float: scaling_factor, string: label) : Pint.Quantity
        }
        class RDFGenerator{
            +rdflib.Graph graph
            +__init__()
            +generate_rdf(Pint.Quantity: unit) : string
        }
        FlaskApp -- UnitConverter : uses
        FlaskApp -- RDFGenerator : uses
    

## Program call flow


    sequenceDiagram
        participant F as FlaskApp
        participant U as UnitConverter
        participant R as RDFGenerator
        F->>U: extend_unit(unit, scaling_factor, label)
        U-->>F: new_unit
        F->>R: generate_rdf(new_unit)
        R-->>F: rdf_string
    

## Anything UNCLEAR

The specific RDF format for the responses needs to be clarified. Additionally, the range of base QUDT units to be supported by the API needs to be specified.

