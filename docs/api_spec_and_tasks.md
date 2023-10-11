# Required Python third-party packages

TODO: Finish rewriting this.

- flask>2.0.0
- rdflib==7.0.0

## Required Other language third-party packages

- 

## Full API spec

openapi: 3.0.0
info:
  title: Unit and Currency Conversion API
  version: 1.0.0
paths:
  /unit/{unit}:
    get:
      summary: Get a unit conversion
      parameters:
        - in: path
          name: unit
          required: true
          description: The unit to convert
          schema:
            type: string
        - in: query
          name: conversion_multiplier
          required: false
          description: The conversion multiplier to use
          schema:
            type: number
        - in: query
          name: label
          required: false
          description: The label to use for the converted value
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/rdf+xml:
              schema:
                type: string
            application/rdf+json:
              schema:
                type: string
            application/n-triples:
              schema:
                type: string
            application/n-quads:
              schema:
                type: string
            application/trig:
              schema:
                type: string
            application/trix:
              schema:
                type: string
            application/turtle:
              schema:
                type: string
            application/x-turtle:
              schema:
                type: string
            application/xml:
              schema:
                type: string
            text/plain:
              schema:
                type: string
        '400':
          description: Bad Request
          content:
            text/plain:
              schema:
                type: string
  /currency/{currency}:
    get:
      summary: Get a currency conversion
      parameters:
        - in: path
          name: currency
          required: true
          description: The currency to convert
          schema:
            type: string
        - in: query
          name: conversion_multiplier
          required: false
          description: The conversion multiplier to use
          schema:
            type: number
        - in: query
          name: label
          required: false
          description: The label to use for the converted value
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/rdf+xml:
              schema:
                type: string
            application/rdf+json:
              schema:
                type: string
            application/n-triples:
              schema:
                type: string
            application/n-quads:
              schema:
                type: string
            application/trig:
              schema:
                type: string
            application/trix:
              schema:
                type: string
            application/turtle:
              schema:
                type: string
            application/x-turtle:
              schema:
                type: string
            application/xml:
              schema:
                type: string
            text/plain:
              schema:
                type: string
        '400':
          description: Bad Request
          content:
            text/plain:
              schema:
                type: string
    

## Logic Analysis

- ['app.py', 'FlaskApp']
- ['unit_converter.py', 'UnitConverter']
- ['rdf_generator.py', 'RDFGenerator']

## Task list

- unit_converter.py
- rdf_generator.py
- app.py

## Shared Knowledge


        'unit_converter.py' contains the 'UnitConverter' class which is responsible for extending base QUDT units. 
        'rdf_generator.py' contains the 'RDFGenerator' class which is responsible for generating RDF responses. 
        'app.py' contains the 'FlaskApp' class which uses 'UnitConverter' and 'RDFGenerator' to handle API requests.
    

## Anything UNCLEAR

The specific RDF format for the responses needs to be clarified. Additionally, the range of base QUDT units to be supported by the API needs to be specified.

