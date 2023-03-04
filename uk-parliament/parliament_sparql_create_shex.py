from shexer.shaper import Shaper
from shexer.consts import NT

target_classes = [
     #"https://id.parliament.uk/schema/TemporalThing", #304800
     "https://id.parliament.uk/schema/AnswerExpectation", #197456
     #"https://id.parliament.uk/schema/ExternalThing", #185126
     #"https://id.parliament.uk/schema/Moderation",#112380
     #"https://id.parliament.uk/schema/ThresholdAttainment",#103068
     #"https://id.parliament.uk/schema/EPetition", #101254
     #"https://id.parliament.uk/schema/UkgapEPetition",#101252
     #"https://id.parliament.uk/schema/UkgapThing",#101252
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://www.w3.org/2000/01/rdf-schema#": "rdfs", 
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://creativecommons.org/ns#": "creativeCommons",
                   "http://purl.org/dc/terms/": "dc-terms",
                   "http://xmlns.com/foaf/0.1/": "foaf",
                   "http://purl.org/ontology/bibo/": "bibo",
                   "http://www.w3.org/2004/02/skos/core#": "skos",
                   "http://purl.org/dc/elements/1.1/": "dc",
                   "http://www.w3.org/2008/05/skos-xl#": "skos-xl",
                   "https://id.parliament.uk/schema/": "par"
                   }

url_endpoint="https://api.parliament.uk/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=100,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shex_parliament_AnswerExpectation.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
