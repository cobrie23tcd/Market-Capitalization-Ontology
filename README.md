# Market-Capitalization-Ontology
OWL 2 ontology for market capitalisation, developed for the Industrial Alliance on Processors and Semiconductor Technologies (IAPST) Stress Test Working Group
# OWL Market Capitalization Ontology

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

---

## 📌 Description

This ontology models **semiconductor industry market capitalisation** 
data using OWL 2, providing a structured semantic representation of 
the semiconductor supply chain as defined by the **Industrial Alliance 
on Processors and Semiconductor Technologies**.

It integrates market capitalisation data for use by the 
**Stress Test Working Group**, enabling time-series querying, 
regional concentration analysis, and supply-chain cluster mapping 
across the global semiconductor ecosystem.

> *"Ontologies serve as the semantic layer necessary to building 
> competent AI Agents with explicit domain knowledge. They serve to 
> avoid AI hallucination in information retrieval by building a highly 
> knowledgeable semiconductor supply chain model."*

---

## 👥 Authors

- **Yannic Schlosser** (GSD SID IN)  
- **Christine O'Brien** (GSD SID IN)

---

## 🔍 Ontology Details

| Field | Details |
|-------|---------|
| **Format** | Turtle (.ttl) / OWL 2 |
| **Base URI** | `http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/` |
| **Namespace Prefix** | `:` |
| **External Vocabularies** | OWL 2, RDF, RDFS, XSD, W3C Time Ontology (`time:`) |
| **Domain** | Semiconductor Supply Chain / Financial Markets |
| **Purpose** | Market Capitalisation Stress Testing & Supply Chain Mapping |

---

## 🏗️ Class Hierarchy

### Top-Level Classes
owl:Thing
├── Organisation
│ └── Company
├── Cluster
│ ├── Industrial_Alliance_Supply_Chain_Cluster
│ │ ├── Materials_Cluster
│ │ ├── Equipment_Cluster
│ │ ├── Intellectual_Property_and_Electronic_Design_Automation_Cluster
│ │ ├── Fabless_Cluster
│ │ ├── Silicon_Foundry_and_Integrated_Device_Manufacturer_Frontend_Cluster
│ │ ├── Outsourced_Semiconductor_Assembly_and_Test_and_Integrated_Device_Manufacturer_Backend_Cluster
│ │ ├── Photonics_Cluster
│ │ ├── Research_&_Development_and_Academia_Cluster
│ │ ├── Associations_and_Others_Cluster
│ │ └── Customer_Cluster
│ │ ├── Applications_Cluster
│ │ ├── Components_Cluster
│ │ └── Electronic_Manufacturing_Services_and_Original_Design_Manufacturer_Cluster
├── Region
│ ├── USA
│ ├── China
│ ├── Taiwan
│ ├── South_Korea
│ ├── Japan
│ └── Other
└── Report
├── Market_Capitalization
└── Regional_Concentration

---

## 📦 Cluster Descriptions

### Supply Chain Clusters

| Cluster | Description |
|---------|-------------|
| **Materials** | Ultra-high-purity substances and consumables used in fab and packaging (silicon wafers, process gases, photoresists, CMP slurries, metals, dielectrics) |
| **Equipment** | Capital tools for making, inspecting, assembling, and testing chips — lithography scanners, deposition, etch, metrology, ATE systems |
| **IP / EDA** | Software and reusable IP blocks for semiconductor design, verification, and sign-off — including CPU/GPU/connectivity IP for SoC integration |
| **Fabless** | Companies that design and sell chips while outsourcing wafer fabrication to foundries such as TSMC |
| **SiFo / IDM Frontend** | Silicon foundries and IDMs performing front-end wafer processing (100–300mm), including lithography, deposition, etch, implant, CMP |
| **OSAT / IDM Backend** | Assembly, packaging, and final test after wafer fab — wafer bumping, die attach, advanced packaging, system-level test |
| **Photonics** | Integrated photonics and optical interconnects using silicon, silicon nitride, and III–V compound semiconductors for data centres, telecoms, and sensing |
| **R&D / Academia** | Universities and public research organisations providing talent, shared cleanrooms, pilot lines, and design ecosystems |
| **Associations & Others** | Cross-cutting systemic risks, growth themes, and leading indicators across the full supply chain |

### Customer Clusters

| Cluster | Description |
|---------|-------------|
| **Applications** | Downstream system makers integrating chips into smartphones, PCs, data centres, automobiles, industrial systems |
| **Components** | Suppliers of passive and electro-mechanical building blocks — capacitors, connectors, EMI filters, power components |
| **EMS / ODM** | Electronic Manufacturing Services / Original Design Manufacturers providing design, sourcing, assembly, and test for OEMs |

---

## 🔗 Object Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `hasCompany` | Cluster | Company | Links a Cluster to its member Companies |
| `isInCluster` | Company | Cluster | Inverse of `hasCompany` |
| `hasHeadquartersIn` | Organisation | Region | Associates an Organisation with its HQ region for regional market cap aggregation |
| `flowsGoodsTo` | Cluster | Cluster | Goods flow between clusters in the supply chain |
| `flowsMoneyTo` | Cluster | Cluster | Money flow between clusters |
| `flowsInformationTo` | Cluster | Cluster | Information flow between clusters |
| `recievesGoodsFrom` | Cluster | Cluster | Inverse of `flowsGoodsTo` |
| `recievesMoneyFrom` | Cluster | Cluster | Inverse of `flowsMoneyTo` |
| `recievesInformationFrom` | Cluster | Cluster | Inverse of `flowsInformationTo` |
| `reportsOnCompany` | Market_Capitalization | Company | Links a MC report to the Company it covers |
| `reportsOnCluster` | Market_Capitalization | Cluster | Links a MC report to the Cluster it covers |
| `reportsOnRegion` | Regional_Concentration | Region | Links a Regional Concentration report to its Region |
| `snapshotDate` | Market_Capitalization | — | Time instant of the market cap observation |

---

## 📊 Data Properties

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `hasMarketCapitalizationValueBillionsUSD` | Market_Capitalization | xsd:decimal | Market cap value in billions USD at snapshot date |
| `hasProportionInCluster` | Market_Capitalization | xsd:decimal | Company's proportional attribution to a Cluster (P_ij). Sum across all clusters per company = 1.0 |

---

## 📐 Market Capitalisation Formula

The cluster-level market capitalisation is computed as:
MC_j = Σ (P_ij × MC_i) for all companies i in Co

Where:
- `MC_i` = `hasMarketCapitalizationValueBillionsUSD` on the Market_Capitalization individual
- `P_ij` = `hasProportionInCluster` (preliminary assumption, to be refined)
- `Co` = all Company individuals
- Constraint: `Σ P_ij = 1.0` for each company across all clusters

---

## 🏢 Modelled Companies (Selected)

### Equipment Cluster
ASML, ASM International, Applied Materials, Aixtron, KLA, 
Lam Research, SUSS MicroTec, TRUMPF, Zeiss, Axelera AI

### Fabless Cluster
NVIDIA, AMD, Qualcomm, Broadcom, NXP, SiPearl, Realtek, 
Will Semiconductor

### Silicon Foundry / IDM Frontend
TSMC, Intel, Samsung, GlobalFoundries, SMIC, UMC, 
STMicroelectronics, Infineon, Texas Instruments, 
Analog Devices, Micron, NXP, Bosch, Diodes Incorporated,
Diotec Semiconductor, Elmos Semiconductor, TMX, Vishay, X-Fab

### OSAT / IDM Backend
ASE, STMicroelectronics, TSMC, Bosch, Presto Engineering, 
STATS ChipPAC, Silicon Box, Swissbit

### Materials Cluster
Air Liquide, Entegris, GlobalWafers, Siltronic, 
Soitec, Tokyo Ohka Kogyo

### IP / EDA Cluster
Arm, Cadence, Synopsys, Siemens, Celus, 
Codasip, Defacto Technologies

### Photonics Cluster
Broadcom, Coherent Corp, GlobalFoundries, Hamamatsu Photonics,
SensL/onsemi, Soitec, Sony Semiconductor Solutions, 
STMicroelectronics, VCSEL, X-Fab

### Components Cluster
Continental, HELLA, Murata, TDK, TE Connectivity, 
Valeo, Vishay, Würth Elektronik, ZF, Samsung, Bosch

### Applications Cluster
Apple, BMW, Dell, Denso, HP, Hyundai Motor Group, 
Samsung, Siemens, Stellantis, Volkswagen, Bosch

### EMS / ODM Cluster
BYD Electronics, Cicor, Compal Electronics, Foxconn, 
GPV, Quanta Computer, SANMINA-SCI Germany, Videoton, 
Zollner Elektronik, cms electronics

### R&D / Academia
Imec, CEA-Leti / MINATEC, TU Dresden Ecosystem, 
Tsinghua University, University of Twente

### Associations & Others
AENEAS, AESEMI, AKJ Automotive, BusinessEurope, 
EPoSS, ESIA, INSIDE Industry Association, 
SEMI, SIA, ZVEI

---

## ⏱️ Temporal Coverage

The ontology includes time-stamped snapshot individuals using the 
**W3C Time Ontology** (`time:inXSDDateTimeStamp`):

| Period | Granularity |
|--------|------------|
| 1965 – 1994 | Annual (December 31) |
| 1995 – 2020 | Quarterly (March, June, September, December) |
| 2021 – 2025 | Monthly (end of month) |
| 2026 | Weekly (from January 2, 2026) |

---

## 🌍 Regional Coverage

Regions modelled as subclasses of `Region`:

- 🇺🇸 **USA**
- 🇨🇳 **China**
- 🇹🇼 **Taiwan**
- 🇰🇷 **South Korea**
- 🇯🇵 **Japan**
- 🌐 **Other** (rest of world)

Regional concentration is captured via the `Regional_Concentration` 
report class, linked to regions via `reportsOnRegion`.

---

## 🔗 Supply Chain Flow Diagram

---

## 💻 SPARQL Query Examples

### Query 1 — Get all companies in the Fabless Cluster

```sparql
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company
WHERE {
  ?company :isInCluster :Fabless_Cluster .
}Query 2 — Get market cap value for a company at a snapshot date
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?company ?capValue ?date
WHERE {
  ?report :reportsOnCompany ?company ;
          :hasMarketCapitalizationValueBillionsUSD ?capValue ;
          :snapshotDate ?date .
}
ORDER BY ?date
Query 3 — Get all clusters a company belongs to
PREFIX : <http://www.semanticweb.org/schlosseryan/ontologies/2026/2/MarketCapitalizationOntology/>

SELECT ?company ?cluster
WHERE {
  ?company a :Company ;
           :isInCluster ?cluster .
}
ORDER BY ?company
🌐 Explore Interactively
🔗 WebVOWL (interactive visual exploration):


Collapse
Save
Copy
1
2
https://service.tib.eu/webvowl/#iri=https://raw.githubusercontent.com/
YOUR_USERNAME/YOUR_REPO_NAME/main/MarketCapitalizationOntology.ttl
🔗 Zenodo DOI: https://doi.org/10.5281/zenodo.XXXXXXX
