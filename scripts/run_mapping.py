"""
Materialise the Market Capitalisation knowledge graph.

Runs the morph-kgc RML mapping for BOTH report types in a single pass:
  * Market_Capitalization   (data/market_capitalization.csv)
  * Regional_Concentration  (data/regional_concentration.csv)

The generated triples are merged with the base ontology and written to
output/knowledge_graph.ttl.

Usage:
    python scripts/run_mapping.py
"""

import os
import morph_kgc
from rdflib import Graph

# ── Project layout ────────────────────────────────────────────────────────
# Resolve everything relative to the project root (the parent of /scripts),
# and switch into it so the rml:source paths inside the mappers resolve
# correctly no matter where the script is launched from.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)

ONTOLOGY_PATH = os.path.join("ontology", "MarketCapitalizationOntology_16.05_base_for_mapping.ttl")
OUTPUT_PATH   = os.path.join("output", "knowledge_graph.ttl")

# Both mappers are declared here so a single materialise() call produces the
# market-capitalisation and regional-concentration triples together.
MAPPING_CONFIG = """
[MarketCapitalization]
mappings: mappings/mapper_market_capitalization.ttl

[RegionalConcentration]
mappings: mappings/mapper_regional_concentration.ttl
"""


def mapping():
    print("✅ Script started...")

    # ── 1. Load ontology ──────────────────────────────────────────────────
    existing_ontology = Graph()
    try:
        existing_ontology.parse(ONTOLOGY_PATH, format="turtle")
        print(f"✅ Ontology loaded ({len(existing_ontology)} triples) → {ONTOLOGY_PATH}")
    except FileNotFoundError:
        print(f"❌ Ontology file not found: {ONTOLOGY_PATH}")
        print("⚠️  Continuing with mapped data only...")
    except Exception as e:
        print(f"❌ Could not parse ontology: {e}")
        print("⚠️  Continuing with mapped data only...")

    # ── 2. Run morph-kgc mapping (market cap + regional concentration) ────
    try:
        mapped_graph = morph_kgc.materialize(MAPPING_CONFIG)
        print(f"✅ Mapping complete ({len(mapped_graph)} triples generated)")
    except Exception as e:
        print(f"❌ Mapping failed: {e}")
        return

    # ── 3. Merge ontology + mapped data ───────────────────────────────────
    merged_graph = existing_ontology + mapped_graph
    print(f"✅ Graphs merged ({len(merged_graph)} total triples)")

    # ── 4. Serialise to Turtle ────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    merged_graph.serialize(destination=OUTPUT_PATH, format="turtle")
    print(f"✅ Done! Saved → {OUTPUT_PATH}")


if __name__ == "__main__":
    mapping()
