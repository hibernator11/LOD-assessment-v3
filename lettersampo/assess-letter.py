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
endpoint = 'http://ldf.fi/corresp/sparql'



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

START=@weso-s:E73_Information_Object

weso-s:E21_Person
{
   rdf:type  [cidoc-crm:E21_Person]  ;                         # 100.0 %
   rdf:type  [cidoc-crm:E74_Group]  ?;
   rdf:type  [cidoc-crm:E53_Place]  ?;
   <http://ldf.fi/schema/lssc/source>  IRI  ;                  # 100.0 %
   skos:prefLabel  xsd:string  ;                               # 100.0 %
   <http://ldf.fi/schema/lssc/has_statistic>  IRI  *;
            # 92.7797833935018 % obj: IRI. Cardinality: +
   <http://ldf.fi/schema/lssc/num_correspondences>  xsd:string  ?;
            # 92.7797833935018 % obj: xsd:string. Cardinality: {1}
   <http://ldf.fi/schema/lssc/num_correspondences>  xsd:integer  ?;
   skos-xl:prefLabel  IRI  *
            # 88.8086642599278 % obj: IRI. Cardinality: +
}


weso-s:E74_Group
{
   rdf:type  [cidoc-crm:E74_Group]  ;                          # 100.0 %
   rdf:type  [cidoc-crm:E53_Place]  ?;
   rdf:type  [cidoc-crm:E21_Person]  ?;    
   <http://ldf.fi/schema/lssc/is_related_to>  IRI  +;          # 100.0 %
   skos:prefLabel  xsd:string  ;                               # 100.0 %
   <http://ldf.fi/schema/lssc/source>  IRI  ?;
            # 97.63779527559055 % obj: IRI. Cardinality: {1}
   skos:altLabel  xsd:string  *
            # 93.7007874015748 % obj: xsd:string. Cardinality: +
}


weso-s:E53_Place
{
   rdf:type  [cidoc-crm:E53_Place]  ;                          # 100.0 %
   rdf:type  [cidoc-crm:E74_Group]  ?;
   rdf:type  [cidoc-crm:E21_Person]  ?;   
   <http://ldf.fi/schema/lssc/is_related_to>  IRI  +;          # 100.0 %
   skos:prefLabel  xsd:string  ;                               # 100.0 %
   <http://www.w3.org/2003/01/geo/wgs84_pos#lat>  xsd:string  ?;
            # 89.53922789539229 % obj: xsd:string. Cardinality: {1}
   <http://www.w3.org/2003/01/geo/wgs84_pos#long>  xsd:string  ?
            # 89.53922789539229 % obj: xsd:string. Cardinality: {1}
}


weso-s:E73_Information_Object
{
   rdf:type  [cidoc-crm:E73_Information_Object]  ;             # 100.0 %
   <http://ldf.fi/schema/lssc/source>  IRI  ?
            # 81.42857142857143 % obj: IRI. Cardinality: {1}
}


"""



i = 0
size = 100
max = 500



while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type cidoc-crm:E73_Information_Object
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

