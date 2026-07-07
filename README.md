# Market Capitalisation Ontology — Mapping Pipeline

Maps semiconductor **market capitalisation** and **regional concentration** data
onto the [Market Capitalisation Ontology (MCO)](ontology/MarketCapitalizationOntology_16.05_base_for_mapping.ttl)
using morph-kgc (RML) and produces a merged knowledge graph.

> **📖 Full ontology reference:** [docs/ONTOLOGY_REFERENCE.md](docs/ONTOLOGY_REFERENCE.md)
> — class hierarchy, cluster descriptions, object/data properties, report triple
> structures, market-cap formulas, modelled companies, temporal/regional coverage,
> and SPARQL query examples. (This is the original detailed README, preserved.)

## Directory structure

```
Ontology Development/
├── ontology/
│   └── MarketCapitalizationOntology_16.05_base_for_mapping.ttl   Base ontology (TBox)
├── data/                                                         ← populate these
│   ├── market_capitalization.csv
│   └── regional_concentration.csv
├── mappings/
│   ├── mapper_market_capitalization.ttl                          RML: MC individuals
│   └── mapper_regional_concentration.ttl                         RML: regional individuals
├── scripts/
│   └── run_mapping.py                                            ← run this
├── output/
│   └── knowledge_graph.ttl                                       Generated (ontology + data)
├── docs/
│   └── ONTOLOGY_REFERENCE.md                                     Full ontology documentation
└── archive/
    ├── database_market_capitalization_populated.csv             Previous data (legacy format)
    └── database_revisions/
```

## How to run the mapping

From the project root:

```powershell
# 1. (once) install dependencies
pip install -r requirements.txt

# 2. run the mapping (materialises BOTH report types in one pass)
python scripts/run_mapping.py
```

The script loads the base ontology, runs both RML mappers, merges the result,
and writes the combined graph to `output/knowledge_graph.ttl`. It resolves all
paths relative to the project root, so it works from any working directory.

## Populating the data

Two blank CSVs are ready to fill in. Column headers double as RML template
variables, so they must not be renamed.

**`data/market_capitalization.csv`** — one row per company–date–cluster:

```
company,snapshotDate,reportsOnCluster,hasMarketCapitalizationValueBillionsUSD,hasProportionInCluster
```

**`data/regional_concentration.csv`** — one row per company–date–region:

```
company,snapshotDate,reportsOnRegion,hasConcentrationInRegion
```

### Formatting notes

- **Decimal separator is `.`** (e.g. `220.5`, not `220,5`). Files are standard
  comma-delimited CSV — the legacy `archive/` data used `;` / European decimals
  and is kept separate rather than migrated.
- **`snapshotDate`** must be `DD_MM_YYYY` (e.g. `31_12_2024`).
- **`reportsOnCluster` / `reportsOnRegion`** must match the ontology individual
  names exactly, including underscores — e.g. `Fabless_Cluster`, `South_Korea`.
- **`company`** must match the company individual name (underscores for spaces),
  e.g. `Applied_Materials`.
- **`hasProportionInCluster`** per company across all clusters should sum to `1.0`.
- **`hasConcentrationInRegion`** per company across all regions should sum to `1.0`.

Generated individual IRIs follow:

```
Market_Capitalization_<company>_<DD_MM_YYYY>_<cluster>
Regional_Concentration_<company>_<DD_MM_YYYY>_<region>
```

## Pushing changes going forward

```powershell
git add .
git commit -m "Describe what you changed"
git push
```

To work on a feature without touching `main`:

```powershell
git checkout -b my-feature      # create + switch to a branch
# ...edit files...
git add .
git commit -m "My change"
git push -u origin my-feature   # first push of a new branch
```

Then open a Pull Request on GitHub to merge the branch into `main`.
