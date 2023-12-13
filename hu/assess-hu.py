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
endpoint = 'https://lod.sztaki.hu/sparql'



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
PREFIX se: <https://id.kb.se/vocab/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dbpedia: <http://dbpedia.org/ontology/>
PREFIX ont: <http://www.w3.org/2006/gen/ont#>

START=@weso-s:BibliographicResource

weso-s:Person
{
   rdf:type  [foaf:Person]  ;                                  # 100.0 %
   rdf:type  [schema:Person] *;
   rdf:type  [schema:Thing] *;
   rdf:type  [dbpedia:Person] *;
   foaf:name  xsd:string  *;
            # 99.8 % obj: xsd:string. Cardinality: +
   <http://dbpedia.org/property/birthYear>  xsd:string  *
            # 87.0 % obj: xsd:string. Cardinality: +
            # 86.2 % obj: xsd:string. Cardinality: {1}
}


weso-s:ThesisDegree
{
   rdf:type  [bibo:ThesisDegree]  ;                            # 100.0 %
   rdfs:label  rdf:langString  *;                               # 100.0 %
   rdfs:comment  rdf:langString  *;                             # 100.0 %
   rdfs:label  xsd:string  *;                               
   rdfs:comment  xsd:string  *; 
   <http://www.w3.org/2003/06/sw-vocab-status/ns#term_status>  xsd:string            # 100.0 %
}


weso-s:Document
{
   rdf:type  [foaf:Document]  *;                                # 100.0 %
   rdf:type [ont:InformationResource]  ;
   dc-terms:subject  IRI  ?;
            # 83.33333333333334 % obj: IRI. Cardinality: {1}
   foaf:primaryTopic  IRI  ?
            # 83.33333333333334 % obj: IRI. Cardinality: {1}
}


weso-s:BibliographicResource
{
   rdf:type  [bibo:Book]  ;                                    # 100.0 %
   rdf:type  [dc-terms:BibliographicResource]  ;               # 100.0 %
   rdf:type  [<http://www.openarchives.org/ore/terms/Aggregation>]  ;          # 100.0 %
   rdfs:label  xsd:string  ;                                   # 100.0 %
   dc-terms:title  xsd:string  ;                               # 100.0 %
   dc-terms:date  xsd:string  ;                                # 100.0 %
   dc-terms:identifier  xsd:string  ;                          # 100.0 %
   dc-terms:issued  xsd:string  ;                              # 100.0 %
   dc-terms:language  IRI  +;                                  # 100.0 %
            # 97.95918367346938 % obj: IRI. Cardinality: {1}
   dc-terms:subject  xsd:string  +;                            # 100.0 %
   dc-terms:type  xsd:string  +;                               # 100.0 %
   dc-terms:type  IRI  ;                                       # 100.0 %
   <http://www.openarchives.org/ore/terms/aggregates>  IRI  +;          # 100.0 %
   dc-terms:creator  xsd:string  *;
            # 97.95918367346938 % obj: xsd:string. Cardinality: +
   dc-terms:temporal  xsd:string  *;
            # 93.87755102040816 % obj: xsd:string. Cardinality: +
            # 91.83673469387756 % obj: xsd:string. Cardinality: {1}
   dc-terms:source  xsd:string  ?
            # 81.63265306122449 % obj: xsd:string. Cardinality: {1}
}


"""



i = 0
size = 200
max = 400



while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX dc-terms: <http://purl.org/dc/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type dc-terms:BibliographicResource
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

