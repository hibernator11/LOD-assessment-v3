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
endpoint = 'http://data.fondazionezeri.unibo.it/sparql'


# ShEx Expression
shex = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX weso-s: <http://weso.es/shapes/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX schema: <http://schema.org/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX creativeCommons: <http://creativecommons.org/ns#>
PREFIX dc-terms: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX bibo: <http://purl.org/ontology/bibo/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX skos-xl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>


START=@weso-s:E22_Man-Made_Object

weso-s:E39_Actor
{
   rdf:type  [cidoc-crm:E39_Actor]  ;                          # 100.0 %
   rdf:type [cidoc-crm:E40_Legal_Body]  ?;
   rdf:type [foaf:Agent]  ?;
   rdfs:label  xsd:string  *;
            # 99.8 % obj: rdf:langString. Cardinality: +
            # 98.0 % obj: rdf:langString. Cardinality: {1}
   <http://purl.org/spar/pro/holdsRoleInTime>  IRI  *;
            # 99.4 % obj: IRI. Cardinality: +
   cidoc-crm:P76_has_contact_point  IRI  *
            # 97.0 % obj: IRI. Cardinality: +
            # 80.4 % obj: IRI. Cardinality: {1}
}

weso-s:E53_Place
{
   rdf:type  [cidoc-crm:E53_Place]  ;                          # 100.0 %
   rdfs:label  xsd:string  +                               # 100.0 %
}


weso-s:E65_Creation
{
   rdf:type  [cidoc-crm:E65_Creation]  ;                       # 100.0 %
   rdfs:label  xsd:string  {2};                            # 100.0 %
   cidoc-crm:P14_carried_out_by  IRI                           # 100.0 %
}


weso-s:E35_Title
{
   rdf:type  [cidoc-crm:E35_Title]                             # 100.0 %
}


weso-s:E22_Man-Made_Object
{
   rdf:type  [cidoc-crm:E22_Man-Made_Object]  ?;                # 100.0 %
   rdf:type [<http://purl.org/spar/fabio/AnalogItem>] ?;
   rdf:type [<http://purl.org/spar/fabio/AnalogManifestation>] ? ;
   rdfs:label  xsd:string  {2}                             # 100.0 %
}


"""


i = 15000
size = 250
max = 20000


while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type cidoc-crm:E22_Man-Made_Object
    }
    """
    print(i)
    sparql = sparql + "LIMIT " + str(size) + " OFFSET " + str(i)
    #print(sparql)
    print(" OFFSET " + str(i) + " LIMIT " + str(size))
   
    i += size

    result = ShExEvaluator(SlurpyGraphWithAgent(endpoint),
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