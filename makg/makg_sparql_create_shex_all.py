#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:18:23 2023

@author: gustavo
"""
from shexer.shaper import Shaper
from shexer.consts import NT

target_classes = [
    "https://makg.org/class/Affiliation",
    "https://makg.org/class/ConferenceInstance",
    "https://makg.org/class/ConferenceSeries",
    "https://makg.org/class/JournalArticle",
    "https://makg.org/class/Paper",
    "http://purl.org/spar/fabio/PatentDocument",
    "http://purl.org/spar/fabio/ConferencePaper",
    "http://purl.org/spar/fabio/Book",
    "http://purl.org/spar/fabio/BookChapter",
    "https://makg.org/class/FieldOfStudy",
    "https://makg.org/class/Citation",
    "http://purl.org/spar/fabio/Work",
    "https://makg.org/class/Author"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://www.w3.org/2000/01/rdf-schema#": "rdfs", 
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://creativecommons.org/ns#": "creativeCommons",
                   "http://purl.org/dc/terms/": "dc-terms",
                   "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
                   "http://purl.org/ontology/bibo/": "bibo",
                   "http://www.europeana.eu/schemas/edm/": "edm",
                   "http://www.openarchives.org/ore/terms/": "ore",
                   "http://www.w3.org/2004/02/skos/core#": "skos",
                   "http://purl.org/dc/elements/1.1/": "dc",
                   "http://usefulinc.com/ns/doap#": "doap",
                   "http://rdfs.org/sioc/services#": "sioc"
                   }

url_endpoint="https://makg.org/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=500,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shex_makg_all.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")

