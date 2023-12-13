from shexer.shaper import Shaper
from shexer.consts import RDF_XML


target_classes = [
     "http://www.cidoc-crm.org/cidoc-crm/E21_Person",
     "http://www.cidoc-crm.org/cidoc-crm/E74_Group",
     "http://www.cidoc-crm.org/cidoc-crm/E53_Place",
     "http://www.cidoc-crm.org/cidoc-crm/E73_Information_Object"
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

url_endpoint="http://ldf.fi/corresp/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=RDF_XML,
                limit_remote_instances=800,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shex_letter_all.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
