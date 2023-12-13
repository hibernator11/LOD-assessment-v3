from shexer.shaper import Shaper
from shexer.consts import RDF_XML

#https://lod.sztaki.hu/sparql?default-graph-uri=&should-sponge=&query=SELECT+DISTINCT+%3FObjectType+WHERE+%7B+%3FURI+a+%3FObjectType+%7D+LIMIT+100&debug=on&timeout=&format=text%2Fhtml&save=display&fname=

target_classes = [
     "http://xmlns.com/foaf/0.1/Person",
     "http://purl.org/ontology/bibo/ThesisDegree",
     "http://xmlns.com/foaf/0.1/Document",
     "http://purl.org/dc/terms/BibliographicResource"
#     "http://purl.org/ontology/bibo/Book" -> no
#     "http://purl.org/ontology/bibo/Document", -> no 
#     "http://purl.org/ontology/bibo/DocumentStatus"
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
                   "http://data.nobelprize.org/terms/": "nobel"
                   }

url_endpoint="https://lod.sztaki.hu/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=RDF_XML,
                limit_remote_instances=800,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shex_hu_all.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
