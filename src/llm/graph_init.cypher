// Create uniqueness constraint required by n10s
CREATE CONSTRAINT n10s_unique_uri IF NOT EXISTS
FOR (r:Resource) REQUIRE r.uri IS UNIQUE;

// Initialize configuration
CALL n10s.graphconfig.init({
  handleVocabUris: "IGNORE",
  handleMultival: "ARRAY",
  keepLangTag: false,
  handleRDFTypes: "LABELS"
});

// Import ontology schema from local file path or URL
CALL n10s.onto.import.fetch(
  "file:///data/narad.owl.ttl", 
  "Turtle"
);

// Import facility instance data
CALL n10s.rdf.import.fetch(
  "file:///data/narad_instance.ttl", 
  "Turtle"
);

// 1. Copy rdfs__label or label properties into a primary 'name' attribute
MATCH (n)
WHERE n.rdfs__label IS NOT NULL AND n.name IS NULL
SET n.name = n.rdfs__label;

MATCH (n)
WHERE n.label IS NOT NULL AND n.name IS NULL
SET n.name = n.label;

// 2. Add an :Instance label to non-ontology nodes for easy filtering by LLMs
MATCH (n:Resource)
WHERE NOT n:Class AND NOT n:Property AND NOT n:Ontology
SET n:Instance;

// 3. Create full-text search index for LLM entity resolution
CREATE FULLTEXT INDEX instance_name_idx IF NOT EXISTS
FOR (n:Instance) ON EACH [n.name, n.uri, n.alias];