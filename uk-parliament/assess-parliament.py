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
endpoint = "https://api.parliament.uk/sparql"


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
PREFIX par: <https://id.parliament.uk/schema/>


START=@weso-s:TemporalThing

weso-s:TemporalThing
{
   rdf:type  [rdfs:Resource]  ;                                # 100.0 %
   rdf:type  [par:TemporalThing]  ;                            # 100.0 %
   rdf:type  [par:ExternalThing]  ;                            # 100.0 %
   par:startDate  xsd:string  ;                                # 100.0 %
   par:date  xsd:string  +;                                    # 100.0 %
   rdf:type  [par:MnisThing]  ?;
            # 88.6 % obj: par:MnisThing. Cardinality: {1}
   rdf:type  [par:NamedThing]  ?;
            # 88.6 % obj: par:NamedThing. Cardinality: {1}
   rdf:type  [par:ContactableThing]  ?;
            # 88.6 % obj: par:ContactableThing. Cardinality: {1}
   rdf:type  [par:Person]  ?;
            # 88.6 % obj: par:Person. Cardinality: {1}
   rdf:type  [par:Member]  ?;
            # 88.6 % obj: par:Member. Cardinality: {1}
   rdf:type  [par:PartyMember]  ?;
            # 88.6 % obj: par:PartyMember. Cardinality: {1}
   rdf:type  [par:GovernmentPerson]  ?;
            # 88.6 % obj: par:GovernmentPerson. Cardinality: {1}
   rdf:type  [par:MnisMember]  ?;
            # 88.6 % obj: par:MnisMember. Cardinality: {1}
   rdfs:label  xsd:string  *;
            # 88.6 % obj: xsd:string. Cardinality: +
   par:governmentPersonHasGovernmentIncumbency  IRI  *;
            # 88.6 % obj: IRI. Cardinality: +
   par:memberHasParliamentaryIncumbency  IRI  *;
            # 88.6 % obj: IRI. Cardinality: +
   par:personHasGenderIdentity  IRI  ?;
            # 88.6 % obj: IRI. Cardinality: {1}
   par:partyMemberHasPartyMembership  IRI  *;
            # 88.6 % obj: IRI. Cardinality: +
   par:name  xsd:string  *;
            # 88.6 % obj: xsd:string. Cardinality: +
   par:mnisId  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   par:personDateOfBirth  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   par:externalIdentifier  xsd:string  *;
            # 88.6 % obj: xsd:string. Cardinality: +
   par:personFamilyName  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   par:personGivenName  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   par:personHasIncumbency  IRI  *;
            # 88.6 % obj: IRI. Cardinality: +
   par:memberMnisId  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   <http://example.com/F31CBD81AD8343898B49DC65743F0BDF>  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   <http://example.com/A5EE13ABE03C4D3A8F1A274F57097B6C>  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   <http://example.com/D79B0BAC513C4A9A87C9D5AFF1FC632F>  xsd:string  ?;
            # 88.6 % obj: xsd:string. Cardinality: {1}
   rdf:type  [par:SesThing]  ?;
            # 85.0 % obj: par:SesThing. Cardinality: {1}
   par:sesId  xsd:string  ?
            # 85.0 % obj: xsd:string. Cardinality: {1}
}"""



i = 0
size = 2
max = 4


while i < max:
    
    # SPARQL Query
    sparql = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX par: <https://id.parliament.uk/schema/>

    SELECT DISTINCT ?item WHERE {
      ?item rdf:type par:TemporalThing
    } 
    """
    print(i)
    sparql = sparql + "LIMIT " + str(size) + " OFFSET " + str(i)
    print(sparql)
    print(" OFFSET " + str(i) + " LIMIT " + str(size))
   
    i += size

    result = ShExEvaluator(SlurpyGraphWithAgent(endpoint),
                       shex,
                       SPARQLQuery(endpoint, sparql).focus_nodes()).evaluate()
    for r in result:
        print(f"{r.focus}: ", end="")
        if not r.result:
            print(f"FAIL: {r.reason}")
        else:
            print("PASS")

    result = 0
    print("finish")