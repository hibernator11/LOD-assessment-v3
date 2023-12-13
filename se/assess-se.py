#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:05:24 2023

@author: gustavo
"""

from pyshex.shex_evaluator import ShExEvaluator
from pyshex.user_agent import SlurpyGraphWithAgent
from pyshex.utils.sparql_query import SPARQLQuery

# SPARQL Endpoint
endpoint = 'https://libris.kb.se/sparql'



# ShEx Expression
shex = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.org/>
PREFIX weso-s: <http://weso.es/shapes/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX schema: <http://schema.org/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX creativeCommons: <http://creativecommons.org/ns#>
PREFIX dc-terms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX bibo: <http://purl.org/ontology/bibo/>
PREFIX edm: <http://www.europeana.eu/schemas/edm/>
PREFIX ore: <http://www.openarchives.org/ore/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX doap: <http://usefulinc.com/ns/doap#>
PREFIX sioc: <http://rdfs.org/sioc/services#>
PREFIX kbv: <https://id.kb.se/vocab/>

START=@weso-s:Organization

weso-s:Person
{
   a  [kbv:Person]  ;                                    # 100.0 %
   kbv:familyName  xsd:string  ?;
            # 98.0 % obj: xsd:string. Cardinality: {1}
   kbv:givenName  xsd:string  ?;
            # 98.0 % obj: xsd:string. Cardinality: {1}
   kbv:lifeSpan  xsd:string  ?;
            # 93.4 % obj: xsd:string. Cardinality: {1}
   kbv:nationality  IRI  *;
            # 89.2 % obj: IRI. Cardinality: +
            # 87.2 % obj: IRI. Cardinality: {1}
   kbv:sameAs  IRI  ?
            # 86.8 % obj: IRI. Cardinality: {1}
}


weso-s:Organization
{
   a  [kbv:Organization]  ;                              # 100.0 %
   kbv:sameAs  IRI  ?;
            # 96.39999999999999 % obj: IRI. Cardinality: {1}
   kbv:name  xsd:string  ?;
            # 88.4 % obj: xsd:string. Cardinality: {1}
   kbv:hasVariant  xsd:string  *
            # 85.6 % obj: xsd:string. Cardinality: +
}


weso-s:Topic
{
   rdf:type  [kbv:Topic]  ;                                     # 100.0 %
   kbv:inScheme  IRI  ;                                         # 100.0 %
   kbv:prefLabel  xsd:string  ;                                 # 100.0 %
   kbv:sameAs  IRI  +;                                          # 100.0 %
            # 99.0 % obj: IRI. Cardinality: {1}
   kbv:inCollection  IRI  *;
            # 94.39999999999999 % obj: IRI. Cardinality: +
   kbv:broadMatch  xsd:string  *
            # 80.60000000000001 % obj: xsd:string. Cardinality: +
}


weso-s:Manuscript
{
   rdf:type  [kbv:Manuscript]  ;                                # 100.0 %
   kbv:hasTitle  xsd:string  +;                                 # 100.0 %
            # 95.0 % obj: xsd:string. Cardinality: {1}
   kbv:instanceOf  xsd:string  ;                                # 100.0 %
   kbv:issuanceType  IRI  ;                                     # 100.0 %
   kbv:extent  xsd:string  ?;
            # 98.6 % obj: xsd:string. Cardinality: {1}
   kbv:hasNote  xsd:string  *
            # 80.2 % obj: xsd:string. Cardinality: +
}


"""



i = 0
size = 200
max = 600



while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX kbv: <https://id.kb.se/vocab/>

    SELECT DISTINCT ?item WHERE {
      ?item a kbv:Organization
    }
    """
    print(i)
    sparql = sparql + "LIMIT " + str(size) + " OFFSET " + str(i)
    #print(sparql)
    print(" OFFSET " + str(i) + " LIMIT " + str(size))
   
    i += size
    from SPARQLWrapper import SPARQLWrapper
    result = ShExEvaluator(SPARQLWrapper(endpoint),
                       shex,
                       SPARQLQuery(endpoint, sparql).focus_nodes()).evaluate()
    for r in result:
        #print(f"{r.focus}: ", end="")
        if not r.result:
            print(f"FAIL: {r.reason}")
        #else:
        #    print("PASS")

    result = 0
    print("finish")

