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
endpoint = 'https://statistics.gov.scot/sparql'



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
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX bibo: <http://purl.org/ontology/bibo/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX skos-xl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

START=@weso-s:Collection

weso-s:Observation
{
   rdf:type  [qb:Observation]  ;                               # 100.0 %
   <http://purl.org/linked-data/sdmx/2009/dimension#refArea>  IRI  ;          # 100.0 %
   <http://purl.org/linked-data/sdmx/2009/attribute#unitMeasure>  IRI  ;          # 100.0 %
   <http://purl.org/linked-data/sdmx/2009/dimension#refPeriod>  IRI  ;          # 100.0 %
   qb:measureType  IRI  ;                                      # 100.0 %
   qb:dataSet  @weso-s:Dataset  ;                              # 100.0 %
   <http://statistics.gov.scot/def/dimension/gender>  IRI  ;          # 100.0 %
   <http://statistics.gov.scot/def/dimension/secondarySchoolStage>  IRI  ;          # 100.0 %
   <http://statistics.gov.scot/def/dimension/scqfLevel>  IRI  ;          # 100.0 %
   <http://statistics.gov.scot/def/dimension/numberOfAwards>  IRI            # 100.0 %
}

weso-s:Dataset
{
   rdf:type  [qb:DataSet]  ;                                   # 100.0 %
   rdf:type  [<http://publishmydata.com/def/dataset#Dataset>] ? ;          # 100.0 %
   rdf:type  [<http://publishmydata.com/def/dataset#LinkedDataset>] ? ;          # 100.0 %
   rdf:type [void:Dataset] ?;     
   rdf:type [dcat:Dataset] ?;
   rdf:type [<http://publishmydata.com/def/dataset#DeprecatedDataset>] ?;
   rdfs:label  xsd:string  ;                                   # 100.0 %
   dc-terms:title  xsd:string  ;                               # 100.0 %
   <http://publishmydata.com/def/dataset#contactEmail>  IRI  ;          # 100.0 %
   <http://publishmydata.com/def/dataset#graph>  IRI  ;          # 100.0 %
   dc-terms:issued  xsd:dateTime  +;                             # 100.0 %
            # 89.66789667896678 % obj: xsd:string. Cardinality: {1}
   dc-terms:modified  xsd:dateTime  ;                            # 100.0 %
   dc-terms:license  IRI  ;                                    # 100.0 %
   dc-terms:creator  IRI  ;                                    # 100.0 %
   dc-terms:publisher  IRI  ;                                  # 100.0 %
   dc-terms:references  IRI  ;                                 # 100.0 %
   void:sparqlEndpoint  IRI  ;                                 # 100.0 %
   qb:structure  @weso-s:DataStructureDefinition  ;            # 100.0 %
   <http://www.w3.org/ns/dcat#theme>  IRI  *;
            # 99.63099630996311 % obj: IRI. Cardinality: +
            # 90.7749077490775 % obj: IRI. Cardinality: {2}
   <http://publishmydata.com/def/ontology/folder/inFolder>  IRI  *;
            # 99.63099630996311 % obj: IRI. Cardinality: +
            # 98.1549815498155 % obj: IRI. Cardinality: {2}
   rdfs:comment  xsd:string  ?;
            # 97.41697416974169 % obj: xsd:string. Cardinality: {1}
   dc-terms:description  xsd:string  ?;
            # 95.20295202952029 % obj: xsd:string. Cardinality: {1}
   <http://publishmydata.com/def/dataset#nextUpdateDue>  xsd:string  ?;
            # 90.03690036900369 % obj: xsd:string. Cardinality: {1}
   <http://statistics.gov.scot/def/statistical-quality/accuracy-and-reliability>  xsd:string  ?
            # 80.81180811808119 % obj: xsd:string. Cardinality: {1}
}
             
weso-s:DataStructureDefinition
{
   rdf:type  [qb:DataStructureDefinition]  ;                   # 100.0 %
   qb:component  IRI  +                                        # 100.0 %
}


weso-s:ComponentSpecification
{
   rdf:type  [qb:ComponentSpecification]                       # 100.0 %
}


weso-s:Collection
{
   rdf:type  [skos:Collection]  ?;                              # 100.0 %
   rdf:type  [<http://publishmydata.com/def/ontology/foi/AreaCollection>] ?;
   rdf:type  [<http://publishmydata.com/def/ontology/foi/OrgCollection>] ?;
   skos:member  IRI  *
            # 95.39999999999999 % obj: IRI. Cardinality: +
}
"""



i = 400
size = 200
max = 600


while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX qb: <http://purl.org/linked-data/cube#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type skos:Collection 
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

