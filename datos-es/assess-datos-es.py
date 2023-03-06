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
endpoint = 'http://datos.gob.es/virtuoso/sparql'


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
PREFIX dcat: <http://www.w3.org/ns/dcat#>


START=@weso-s:Dataset

weso-s:Distribution
{
   rdf:type  [dcat:Distribution]  ;                            # 100.0 %
   dc-terms:title  xsd:string  +;                          # 100.0 %
            # 93.5 % obj: rdf:langString. Cardinality: {2}
   dc-terms:format  IRI  ;                                     # 100.0 %
   dcat:accessURL  IRI                                         # 100.0 %
}


weso-s:Dataset
{
   rdf:type  [dcat:Dataset]  ;                                 # 100.0 %
   dc-terms:description  xsd:string +;                    # 100.0 %
   dc-terms:language  xsd:string  +;                           # 100.0 %
   dc-terms:publisher  @weso-s:Concept  ;                      # 100.0 %
   dc-terms:title  xsd:string  +;                          # 100.0 %
   dcat:distribution  IRI  +;                                  # 100.0 %
   dcat:theme  @weso-s:Concept  +;                             # 100.0 %
   dc-terms:license  IRI  ;                                    # 100.0 %
   dc-terms:modified  xsd:dateTime  ?;
            # 97.5 % obj: xsd:string. Cardinality: {1}
   dcat:keyword  xsd:string  *;
            # 89.5 % obj: rdf:langString. Cardinality: +
   dc-terms:spatial  IRI  *
            # 81.0 % obj: IRI. Cardinality: +
}


weso-s:Frequency
{
   rdf:type  [dc-terms:Frequency]  ;                           # 100.0 %
   rdf:value  IRI                                              # 100.0 %
}


weso-s:DurationDescription
{
   rdf:type  [<http://www.w3.org/2006/time#DurationDescription>]            # 100.0 %
}


weso-s:PeriodOfTime
{
   rdf:type  [dc-terms:PeriodOfTime]  ;                        # 100.0 %
   schema:startDate  xsd:dateTime  ;                             # 100.0 %
   schema:endDate  xsd:dateTime  ?
            # 93.0 % obj: xsd:string. Cardinality: {1}
}


weso-s:Concept
{
   rdf:type  [skos:Concept]  ;                                 # 100.0 %
   skos:notation  xsd:string  ;                                # 100.0 %
   skos:prefLabel  xsd:string  *
            # 87.64044943820225 % obj: xsd:string. Cardinality: {1}
}

"""



i=10600
size = 100
max = 15000

errors = 0
while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX dcat: <http://www.w3.org/ns/dcat#>
    PREFIX dc-terms: <http://purl.org/dc/terms/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type dcat:Dataset
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
            errors = errors + 1
        #else:
        #    print("PASS")

    result = 0
    print("finish iteration errors:" + str(errors))
print("total errors:" + str(errors))