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
endpoint = 'https://makg.org/sparql'



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

START=@weso-s:Paper

weso-s:Affiliation
{
   rdf:type  [<https://makg.org/class/Affiliation>]  ;          # 100.0 %
   dc-terms:created  xsd:date  ;                               # 100.0 %
   rdfs:seeAlso  IRI  ?;                                        # 100.0 %
   <http://www.w3.org/2002/07/owl#sameAs>  IRI ?;              # 100.0 %
   <http://xmlns.com/foaf/0.1/name>  xsd:string  ;             # 100.0 %
   <https://makg.org/property/citationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/paperCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/paperFamilyCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/rank>  xsd:integer  ;             # 100.0 %
   geo:lat  xsd:string  ?;
            # 95.8 % obj: xsd:string. Cardinality: {1}
   geo:long  xsd:string  ?;
            # 95.8 % obj: xsd:string. Cardinality: {1}
   <http://xmlns.com/foaf/0.1/homepage>  IRI  ?
            # 92.2 % obj: IRI. Cardinality: {1}
}


weso-s:ConferenceInstance
{
   rdf:type  [<https://makg.org/class/ConferenceInstance>]  ;          # 100.0 %
   dc-terms:created  xsd:date  ;                             # 100.0 %
   <http://xmlns.com/foaf/0.1/name>  xsd:string  ;             # 100.0 %
   <https://makg.org/property/citationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/paperFamilyCount>  xsd:integer  ;          # 100.0 %
   <http://purl.org/NET/c4dm/timeline.owl#end>  xsd:date  ;          # 100.0 %
   <http://purl.org/NET/c4dm/timeline.owl#start>  xsd:date  ;          # 100.0 %
   dc-terms:isPartOf  IRI  ;                                   # 100.0 %
   <https://makg.org/property/pageCount>  xsd:integer  ;          # 100.0 %
   <http://xmlns.com/foaf/0.1/homepage>  IRI  ?;
            # 99.8 % obj: IRI. Cardinality: {1}
   <https://makg.org/property/submissionDeadlineDate>  xsd:date  ?;
            # 96.6 % obj: xsd:string. Cardinality: {1}
   <http://dbpedia.org/ontology/location>  IRI  ?;
            # 91.60000000000001 % obj: IRI. Cardinality: {1}
   <http://dbpedia.org/ontology/location>  xsd:string  ?
            
}

weso-s:ConferenceSeries
{
   rdf:type  [<https://makg.org/class/ConferenceSeries>]  ;
   dc-terms:created  xsd:date  ;
   <http://xmlns.com/foaf/0.1/name>  xsd:string  ;
   <https://makg.org/property/citationCount>  xsd:integer  ;
   <https://makg.org/property/paperCount>  xsd:integer  ;   
   <https://makg.org/property/paperFamilyCount>  xsd:integer  ;
   <https://makg.org/property/rank>  xsd:integer
}

weso-s:JournalArticle
{
   rdf:type  [<https://makg.org/class/JournalArticle>]  ;          # 100.0 %
   rdf:type  [<https://makg.org/class/Paper>]  ;               # 100.0 %
   dc-terms:created  xsd:date  ;                             # 100.0 %
   <https://makg.org/property/citationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/rank>  xsd:integer  ;             # 100.0 %
   <http://purl.org/spar/fabio/hasURL>  IRI  +;                # 100.0 %
   <http://prismstandard.org/namespaces/basic/2.0/publicationDate>  xsd:string  ;          # 100.0 %
   dc-terms:title  xsd:date  ;                               # 100.0 %
   <https://makg.org/property/appearsInJournal>  IRI  ;          # 100.0 %
   <https://makg.org/property/estimatedCitationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/referenceCount>  xsd:integer  ;          # 100.0 %
   dc-terms:creator  IRI  +;                                   # 100.0 %
   <http://purl.org/spar/fabio/hasPubMedId>  IRI  *;
            # 99.8 % obj: IRI. Cardinality: +
            # 98.4 % obj: IRI. Cardinality: {1}
   <http://prismstandard.org/namespaces/basic/2.0/startingPage>  xsd:string  ?;
            # 98.4 % obj: xsd:string. Cardinality: {1}
   <http://prismstandard.org/namespaces/basic/2.0/volume>  xsd:string  ?;
            # 97.6 % obj: xsd:string. Cardinality: {1}
   dc-terms:publisher  xsd:string  ?;
            # 92.0 % obj: xsd:string. Cardinality: {1}
   <http://prismstandard.org/namespaces/basic/2.0/issueIdentifier>  xsd:string  ?;
            # 86.8 % obj: xsd:string. Cardinality: {1}
   <http://prismstandard.org/namespaces/basic/2.0/keyword>  xsd:string  *;
            # 80.2 % obj: xsd:string. Cardinality: +
   dc-terms:abstract  xsd:string  ?;
            # 80.2 % obj: xsd:string. Cardinality: {1}
   <http://purl.org/spar/fabio/hasDiscipline>  IRI  ?
            # 80.2 % obj: IRI. Cardinality: {1}
}

weso-s:Paper
{
   rdf:type  [<https://makg.org/class/Paper>] * ;               # 100.0 %
   rdf:type  [<https://makg.org/class/JournalArticle>] *; 
   rdf:type  [<http://purl.org/spar/fabio/PatentDocument>]  *; 
   rdf:type  [<http://purl.org/spar/fabio/ConferencePaper>]  *;
   rdf:type  [<http://purl.org/spar/fabio/Book>]  *;
   dc-terms:created  xsd:date  ;                             # 100.0 %
   <https://makg.org/property/citationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/rank>  xsd:integer  ;             # 100.0 %
   <http://prismstandard.org/namespaces/basic/2.0/publicationDate>  xsd:date  ;          # 100.0 %
   dc-terms:title  xsd:string  +;                              # 100.0 %
   <https://makg.org/property/estimatedCitationCount>  xsd:integer  ;          # 100.0 %
   <https://makg.org/property/referenceCount>  xsd:integer  ;          # 100.0 %
   dc-terms:creator  IRI  +;                                   # 100.0 %
   <http://purl.org/spar/fabio/hasURL>  xsd:anyURI *
            # 88.96853843090402 % obj: IRI. Cardinality: +
}
"""



i = 14600
size = 200
#max = 27000 Affiliation
#max = 17000 ConferenceInstance
#max = 54800 ConferenceSeries
#max = 20000 JournalArticle
#max = 20000 Paper
max = 15000



while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX makg: <https://makg.org/class/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type makg:Paper
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

