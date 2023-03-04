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
endpoint = 'https://agrovoc.fao.org/sparql'

# SPARQL Query
sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT DISTINCT ?item WHERE {
  ?item rdf:type skos:Concept
}
LIMIT 1000 offset 19000
"""

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


START=@weso-s:Concept

weso-s:ConceptScheme
{
   rdf:type  [skos:ConceptScheme]  ;                           # 100.0 %
   void:inDataset  IRI                                         # 100.0 %
}

weso-s:Concept
{
   rdf:type  [skos:Concept]  ;                                 # 100.0 %
   skos:prefLabel  xsd:string  *;                          # 100.0 %
   skos-xl:prefLabel  IRI  *;                                  # 100.0 %
   skos:inScheme  @weso-s:ConceptScheme  +;                    # 100.0 %
   dc-terms:modified  xsd:dateTime  ;                            # 100.0 %
   dc-terms:created  xsd:dateTime  ;                             # 100.0 %
   void:inDataset  IRI  ;                                      # 100.0 %
   skos:broader  IRI  *
            # 99.8 % obj: IRI. Cardinality: +
            # 95.0 % obj: IRI. Cardinality: {1}
}

weso-s:Image
{
   rdf:type  [foaf:Image]  ;            # 100.0 %
   rdfs:comment  xsd:string  ;                             # 100.0 %
   rdf:value  xsd:string  ;                                # 100.0 %
   dc-terms:created  xsd:dateTime  ;                             # 100.0 %
   dc-terms:source  IRI  ;                                     # 100.0 %
   dc-terms:modified  xsd:dateTime  ?
            # 81.66666666666667 % obj: xsd:string. Cardinality: {1}
}"""


result = ShExEvaluator(SlurpyGraphWithAgent(endpoint),
                       shex,
                       SPARQLQuery(endpoint, sparql).focus_nodes()).evaluate()
for r in result:
    #print(f"{r.focus}: ", end="")
    if not r.result:
        print(f"FAIL: {r.reason}")
    #else:
    #    print("PASS")
print("Done!")