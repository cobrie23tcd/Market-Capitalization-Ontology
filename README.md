# Market Capitalisation Ontology 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20702097.svg)](https://doi.org/10.5281/zenodo.20729152)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![OWL 2](https://img.shields.io/badge/OWL-2-blue.svg)](https://www.w3.org/TR/owl2-overview/)
[![Turtle](https://img.shields.io/badge/Serialisation-Turtle-green.svg)](https://www.w3.org/TR/turtle/)
[![WebVOWL](https://img.shields.io/badge/Visualise-WebVOWL-orange.svg)](https://service.tib.eu/webvowl/#iri=https://zenodo.org/records/20729152/files/MarketCapitalizationOntology_16.05_base_for_mapping.ttl?download=1)

> **🔍 Explore the ontology interactively:**
> [Open in WebVOWL](https://service.tib.eu/webvowl/#iri=https://zenodo.org/records/20729152/files/MarketCapitalizationOntology_16.05_base_for_mapping.ttl?download=1)
>
> _"Ontologies serve as the semantic layer necessary to building competent AI Agents with explicit domain knowledge. They serve to avoid AI hallucination in information retrieval by building a highly knowledgeable semiconductor supply chain model."_

---

## 📌 Description

The **Market Capitalisation Ontology (MCO)** is an OWL 2 ontology that models **semiconductor industry market capitalisation data**, providing a structured semantic representation of the global semiconductor supply chain as defined by the **Industrial Alliance on Processors and Semiconductor Technologies (IAPST)**.

It was developed for the **IAPST Stress Test Working Group** and supports:

- Time-series querying of market capitalisation snapshots from **1965 to 2026** with annual, quarterly, monthly, and weekly granularity
- **Regional concentration analysis** across USA, China, Taiwan, South Korea, Japan, and Rest of World
- **Supply-chain cluster mapping** across 13 clusters covering the full semiconductor value chain
- **Cluster-level market cap aggregation** using a proportion-weighted formula
- **Semantic AI grounding** for semiconductor supply chain knowledge graphs

> ⚠️ **Note:** This ontology represents the **base mapping layer only**. It defines the semantic structure for data integration. Data collection is conducted separately and mapped onto this ontology using RML-based knowledge graph materialisation.

---

## 👥 Authors

| Name | Affiliation |
|------|-------------|
| **Yannic Schlosser** | GSD SID IN |
| **Christine O'Brien** | GSD SID IN |

---

## 🔍 Ontology Details

| Field | Details |
|-------|---------|
| **Title** | Market Capitalisation Ontology |
| **Acronym** | MCO |
| **Format** | Turtle (.ttl) / OWL 2 |
| **Authoring Tool** | Protégé |
| **Base URI** | `http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/` |
| **Namespace Prefix** | `:` |
| **External Vocabularies** | OWL 2, RDF, RDFS, XSD, W3C Time Ontology (`time:`) |
| **Domain** | Semiconductor Supply Chain / Financial Markets |
| **Purpose** | Market Capitalisation Stress Testing & Supply Chain Mapping |
| **DOI** | [10.5281/zenodo.20702097](https://doi.org/10.5281/zenodo.20729152) |
| **License** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

---

## 🏗️ Class Hierarchy

```
owl:Thing
├── Organisation
│   └── Company
├── Cluster
│   ├── Industrial_Alliance_Supply_Chain_Cluster
│   │   ├── Materials_Cluster
│   │   ├── Equipment_Cluster
│   │   ├── Intellectual_Property_and_Electronic_Design_Automation_Cluster
│   │   ├── Fabless_Cluster
│   │   ├── Silicon_Foundry_and_Integrated_Device_Manufacturer_Frontend_Cluster
│   │   ├── Outsourced_Semiconductor_Assembly_and_Test_and_Integrated_Device_Manufacturer_Backend_Cluster
│   │   ├── Photonics_Cluster
│   │   ├── Research_&_Development_and_Academia_Cluster
│   │   ├── Associations_and_Others_Cluster
│   │   └── Customer_Cluster
│   │       ├── Applications_Cluster
│   │       ├── Components_Cluster
│   │       └── Electronic_Manufacturing_Services_and_Original_Design_Manufacturer_Cluster
├── Region
│   ├── USA
│   ├── China
│   ├── Taiwan
│   ├── South_Korea
│   ├── Japan
│   └── Other
└── Report
    ├── Market_Capitalization
    └── Regional_Concentration
```

---

## 📦 Cluster Descriptions

| Cluster | Description |
|---------|-------------|
| **Materials** | Ultra-high-purity substances and consumables used in fab and packaging — silicon wafers, process gases, photoresists, CMP slurries, metals, dielectrics |
| **Equipment** | Capital tools for making, inspecting, assembling, and testing chips — lithography scanners, deposition, etch, metrology, ATE systems |
| **IP / EDA** | Software and reusable IP blocks for semiconductor design, verification, and sign-off — including CPU/GPU/connectivity IP for SoC integration |
| **Fabless** | Companies that design and sell chips while outsourcing wafer fabrication to foundries such as TSMC |
| **SiFo / IDM Frontend** | Silicon foundries and IDMs performing front-end wafer processing (100–300 mm), including lithography, deposition, etch, implant, CMP |
| **OSAT / IDM Backend** | Assembly, packaging, and final test after wafer fab — wafer bumping, die attach, advanced packaging, system-level test |
| **Photonics** | Integrated photonics and optical interconnects using silicon, silicon nitride, and III–V compound semiconductors for data centres, telecoms, and sensing |
| **R&D / Academia** | Universities and public research organisations providing talent, shared cleanrooms, pilot lines, and design ecosystems |
| **Associations & Others** | Cross-cutting systemic risks, growth themes, and leading indicators across the full supply chain |
| **Applications** | Downstream system makers integrating chips into smartphones, PCs, data centres, automobiles, and industrial systems |
| **Components** | Suppliers of passive and electro-mechanical building blocks — capacitors, connectors, EMI filters, power components |
| **EMS / ODM** | Electronic Manufacturing Services / Original Design Manufacturers providing design, sourcing, assembly, and test for OEMs |

---

## 🔗 Object Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `hasCompany` | Cluster | Company | Links a Cluster to its member Companies |
| `isInCluster` | Company | Cluster | Inverse of `hasCompany` |
| `hasHeadquartersIn` | Organisation | Region | Associates an Organisation with its HQ region for regional market cap aggregation |
| `flowsGoodsTo` | Cluster | Cluster | Goods flow between supply chain clusters |
| `flowsMoneyTo` | Cluster | Cluster | Money flow between clusters |
| `flowsInformationTo` | Cluster | Cluster | Information flow between clusters |
| `recievesGoodsFrom` | Cluster | Cluster | Inverse of `flowsGoodsTo` |
| `recievesMoneyFrom` | Cluster | Cluster | Inverse of `flowsMoneyTo` |
| `recievesInformationFrom` | Cluster | Cluster | Inverse of `flowsInformationTo` |
| `reportsOnCompany` | Market_Capitalization | Company | Links a MC report individual to the Company it covers |
| `reportsOnCluster` | Market_Capitalization | Cluster | Links a MC report individual to the Cluster it covers |
| `reportsOnRegion` | Regional_Concentration | Region | Links a Regional Concentration individual to its Region |
| `reportsOnCompany` | Regional_Concentration | Company | Links a Regional Concentration individual to the Company it covers |

---

## 📊 Data Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `hasMarketCapitalizationValueBillionsUSD` | Market_Capitalization | `xsd:decimal` | Market cap value in billions USD at snapshot date |
| `hasProportionInCluster` | Market_Capitalization | `xsd:decimal` | Company's proportional attribution to a Cluster (P_ij). Sum across all clusters per company = 1.0 |
| `hasConcentrationInRegion` | Regional_Concentration | `xsd:decimal` | The proportion of a company's market cap attributed to a specific region (P_ir). Sum across all regions per company = 1.0 |
| `snapshotDate` | Market_Capitalization ∪ Regional_Concentration | `xsd:string` | Date of the observation snapshot in format `DD_MM_YYYY` |

---

## 🗂️ Report Triple Structures

The ontology uses a **reification pattern** for both report types, where each individual represents a single atomic observation tied to a company and a snapshot date. This allows companies operating across multiple clusters or regions to have multiple report individuals.

---

### Market_Capitalization

Each `Market_Capitalization` individual represents a single **company–cluster–date** observation.

```
Market_Capitalization_<Company>_<DD_MM_YYYY>_<Cluster>
    ├── :reportsOnCompany                       → :Company    (Object Property)
    ├── :reportsOnCluster                       → :Cluster    (Object Property)
    ├── :hasMarketCapitalizationValueBillionsUSD → xsd:decimal (Data Property)
    ├── :hasProportionInCluster                 → xsd:decimal (Data Property)
    └── :snapshotDate                           → xsd:string  (Data Property)
```

**Example in Turtle:**

```turtle
:Market_Capitalization_AMD_31_12_2024_Fabless_Cluster
    a :Market_Capitalization ;
    :reportsOnCompany                        :AMD ;
    :reportsOnCluster                        :Fabless_Cluster ;
    :hasMarketCapitalizationValueBillionsUSD "220.5"^^xsd:decimal ;
    :hasProportionInCluster                  "0.80"^^xsd:decimal ;
    :snapshotDate                            "31_12_2024"^^xsd:string .
```

> Companies spanning **multiple clusters** will have **multiple separate `Market_Capitalization` individuals**, one per cluster, with the constraint that the sum of `hasProportionInCluster` values per company across all clusters equals `1.0`.
>
> ⚠️ **Why P is critical:** Many companies span multiple clusters (e.g., Samsung is in both `Materials_Cluster` and `Silicon_Foundry_Cluster`). Additionally, many companies are not 100% semiconductors.

---

### Regional_Concentration

Each `Regional_Concentration` individual represents a single **company–region–date** observation.

```
Regional_Concentration_<Company>_<DD_MM_YYYY>_<Region>
    ├── :reportsOnCompany         → :Company    (Object Property)
    ├── :reportsOnRegion          → :Region     (Object Property)
    ├── :hasConcentrationInRegion → xsd:decimal (Data Property)
    └── :snapshotDate             → xsd:string  (Data Property)
```

**Example in Turtle:**

```turtle
:Regional_Concentration_AMD_31_12_2024_Taiwan
    a :Regional_Concentration ;
    :reportsOnCompany         :AMD ;
    :reportsOnRegion          :Taiwan ;
    :hasConcentrationInRegion "0.65"^^xsd:decimal ;
    :snapshotDate             "31_12_2024"^^xsd:string .
```

> Companies spanning **multiple regions** will have **multiple separate `Regional_Concentration` individuals**, one per region, with the constraint that the sum of `hasConcentrationInRegion` values per company across all regions equals `1.0`.
>
> ⚠️ **Why P is critical:** Many companies span multiple regions (e.g., TSMC operates across Taiwan, USA, and Japan).

---

## 📐 Market Capitalisation Formulas

### 1. Market Capitalisation by Cluster

```
MC_j = Σ (MC_i × P_ij)   for all companies i in Co
```

| Symbol | Description |
|--------|-------------|
| `MC_j` | Total market cap attributed to cluster j |
| `MC_i` | Total market cap of company i (raw financial figure) |
| `P_ij` | `hasProportionInCluster` — proportion of company i's market cap allocated to cluster j |
| `Co` | The set of all companies in the ontology |

Constraint: the sum of `P_ij` per company across all clusters equals `1.0`.

Total market capitalisation across all clusters:

```
MC_T = Σ MC_j   summed across all clusters j = 1 to n
```

---

### 2. Market Capitalisation by Region

```
MC_r = Σ (MC_i × P_ir)   for all companies i in Co
```

| Symbol | Description |
|--------|-------------|
| `MC_r` | Total market cap attributed to region r |
| `MC_i` | Total market cap of company i (raw financial figure) |
| `P_ir` | `hasConcentrationInRegion` — proportion of company i's market cap allocated to region r |
| `Co` | The set of all companies in the ontology |

Constraint: the sum of `P_ir` per company across all regions equals `1.0`.

Total market capitalisation across all regions:

```
MC_T = Σ MC_r   summed across all regions r = 1 to n
```

---

## 🏢 Modelled Companies

**Equipment:** ASML · ASM International · Applied Materials · Aixtron · KLA · Lam Research · SUSS MicroTec · TRUMPF · Zeiss · Axelera AI

**Fabless:** NVIDIA · AMD · Qualcomm · Broadcom · NXP · SiPearl · Realtek · Will Semiconductor

**Silicon Foundry / IDM Frontend:** TSMC · Intel · Samsung · GlobalFoundries · SMIC · UMC · STMicroelectronics · Infineon · Texas Instruments · Analog Devices · Micron · NXP · Bosch · Diodes Incorporated · Diotec Semiconductor · Elmos Semiconductor · TMX · Vishay · X-Fab

**OSAT / IDM Backend:** ASE · STMicroelectronics · TSMC · Bosch · Presto Engineering · STATS ChipPAC · Silicon Box · Swissbit

**Materials:** Air Liquide · Entegris · GlobalWafers · Siltronic · Soitec · Tokyo Ohka Kogyo

**IP / EDA:** Arm · Cadence · Synopsys · Siemens · Celus · Codasip · Defacto Technologies

**Photonics:** Broadcom · Coherent Corp · GlobalFoundries · Hamamatsu Photonics · SensL/onsemi · Soitec · Sony Semiconductor Solutions · STMicroelectronics · VCSEL · X-Fab

**Components:** Continental · HELLA · Murata · TDK · TE Connectivity · Valeo · Vishay · Würth Elektronik · ZF · Samsung · Bosch

**Applications:** Apple · BMW · Dell · Denso · HP · Hyundai Motor Group · Samsung · Siemens · Stellantis · Volkswagen · Bosch

**EMS / ODM:** BYD Electronics · Cicor · Compal Electronics · Foxconn · GPV · Quanta Computer · SANMINA-SCI Germany · Videoton · Zollner Elektronik · cms electronics

**R&D / Academia:** Imec · CEA-Leti / MINATEC · TU Dresden Ecosystem · Tsinghua University · University of Twente

**Associations & Others:** AENEAS · AESEMI · AKJ Automotive · BusinessEurope · EPoSS · ESIA · INSIDE Industry Association · SEMI · SIA · ZVEI

---

## ⏱️ Temporal Coverage

| Period | Granularity | Example Individuals |
|--------|-------------|---------------------|
| 1965 – 1994 | Annual (December 31) | `Instant_1965_12_31` … `Instant_1994_12_31` |
| 1995 – 2020 | Quarterly (Mar, Jun, Sep, Dec) | `Instant_1995_03_31` … `Instant_2020_12_31` |
| 2021 – 2025 | Monthly (end of month) | `Instant_2021_01_31` … `Instant_2025_12_31` |
| 2026 | Weekly (from 2 January 2026) | `Instant_2026_01_02` … `Instant_2026_05_01` |

---

## 🌍 Regional Coverage

| Region | Representative Companies |
|--------|--------------------------|
| 🇺🇸 **USA** | NVIDIA, AMD, Qualcomm, Intel, Applied Materials, KLA, Lam Research |
| 🇨🇳 **China** | SMIC, YMTC, Naura Technology, Cambricon Technology, Will Semiconductor, Huawei |
| 🇹🇼 **Taiwan** | TSMC, UMC, ASE, GlobalWafers, MediaTek, Realtek, Compal Electronics |
| 🇰🇷 **South Korea** | Samsung, SK Hynix |
| 🇯🇵 **Japan** | Tokyo Electron, Advantest, Murata, TDK, Hamamatsu Photonics, Tokyo Ohka Kogyo |
| 🌐 **Other** | ASML, ASM International, Infineon, STMicroelectronics, NXP, Soitec, Siltronic, Aixtron |

---

## 🔗 Supply Chain Flow Properties

The ontology models directional flows between clusters using three symmetric property pairs: `flowsGoodsTo` ↔ `recievesGoodsFrom`, `flowsMoneyTo` ↔ `recievesMoneyFrom`, and `flowsInformationTo` ↔ `recievesInformationFrom`.

```
Materials ──────────────────► SiFo/IDM Frontend
Equipment ──────────────────► SiFo/IDM Frontend
                               SiFo/IDM Frontend ──► OSAT/IDM Backend
IP/EDA ─────────────────────► Fabless
                               Fabless ────────────► SiFo/IDM Frontend
IP/EDA ─────────────────────► Photonics
R&D/Academia ───────────────► IP/EDA
OSAT/IDM Backend ───────────► Customer Cluster
Photonics ──────────────────► Customer Cluster
Customer Cluster ────────────► Applications Cluster
```

---

## 💻 SPARQL Query Examples

**Query 1 — List all companies in the Fabless Cluster**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company
WHERE {
    ?company :isInCluster :Fabless_Cluster .
}
ORDER BY ?company
```

**Query 2 — Get market cap value for all companies at a snapshot date**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?company ?capValue ?date
WHERE {
    ?report :reportsOnCompany ?company ;
            :hasMarketCapitalizationValueBillionsUSD ?capValue ;
            :snapshotDate ?date .
}
ORDER BY ?date DESC(?capValue)
```

**Query 3 — Get all clusters a company belongs to**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company ?cluster
WHERE {
    ?company a :Company ;
             :isInCluster ?cluster .
}
ORDER BY ?company
```

**Query 4 — Get all companies in a region via HQ**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company ?region
WHERE {
    ?company a :Company ;
             :hasHeadquartersIn ?regionInstance .
    ?regionInstance a ?region .
    FILTER(?region IN (:USA, :Taiwan, :China, :South_Korea, :Japan, :Other))
}
ORDER BY ?region ?company
```

**Query 5 — Get all supply chain goods flows between clusters**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?sourceCluster ?targetCluster
WHERE {
    ?sourceCluster :flowsGoodsTo ?targetCluster .
}
ORDER BY ?sourceCluster
```

**Query 6 — Get all regional concentration values for a company**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company ?region ?concentration ?date
WHERE {
    ?report a :Regional_Concentration ;
            :reportsOnCompany ?company ;
            :reportsOnRegion ?region ;
            :hasConcentrationInRegion ?concentration ;
            :snapshotDate ?date .
}
ORDER BY ?company ?date ?region
```

**Query 7 — Get regional concentration for all companies at a specific snapshot**

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company ?region ?concentration
WHERE {
    ?report a :Regional_Concentration ;
            :reportsOnCompany ?company ;
            :reportsOnRegion ?region ;
            :hasConcentrationInRegion ?concentration ;
            :snapshotDate "31_12_2024"^^xsd:string .
}
ORDER BY ?company DESC(?concentration)
```

---

## 🌐 Access and Citation

**Interactive Visualisation (WebVOWL)**

🔗 [Open in WebVOWL](https://service.tib.eu/webvowl/#iri=https://zenodo.org/records/20729152/files/MarketCapitalizationOntology_16.05_base_for_mapping.ttl?download=1)

```
https://service.tib.eu/webvowl/#iri=https://zenodo.org/records/20702097/files/MarketCapitalizationOntology_15.05_base_for_mapping.ttl
```

**Zenodo Record**

🔗 : [https://.org/10.5281/zenodo.20702097](https://doi.org/10.5281/zenodo.207291529

**Direct Download (raw Turtle file)**

```
https://zenodo.org/records/20702097/files/MarketCapitalizationOntology_15.05_base_for_mapping.ttl
```

---

## 📖 Citation

```bibtex
@software{schlosser_obrien_mco_2026,
  author    = {Schlosser, Yannic and O'Brien, Christine},
  title     = {Market Capitalisation Ontology (MCO)},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20702097},
  url       = {https://doi.org/10.5281/zenodo.20702097}
}
```

---

## Acknowledgements

| Tool / Resource | Role |
|-----------------|------|
| [Protégé](https://protege.stanford.edu/) | OWL 2 ontology authoring |
| [W3C Time Ontology](https://www.w3.org/TR/owl-time/) | Temporal snapshot representation |
| [WebVOWL (TIB)](https://service.tib.eu/webvowl/) | Interactive ontology visualisation |
| [Zenodo](https://zenodo.org/) | Persistent DOI and archival |

_Developed for the Industrial Alliance on Processors and Semiconductor Technologies (IAPST) — Stress Test Working Group._
