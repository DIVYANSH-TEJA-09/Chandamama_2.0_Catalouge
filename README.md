# Chandamama Magazine Metadata Project (1947-2012)

## Project Overview

This project aims to digitize and index the complete metadata of **Chandamama Magazine**, a legendary Telugu children's publication that has been serving readers for 66 years. We are systematically extracting and cataloging stories, articles, and other content from each monthly issue published between 1947 and 2012.

## What We Have Done

We have developed an automated indexing system using **Google's Gemini API** (via the official SDK) to extract metadata from Chandamama magazine PDFs. The system:

-   **Automatically extracts** story information from PDF files
-   **Generates structured JSON metadata** for each magazine issue
-   **Supports bulk processing** for entire years of publications
-   **Includes verification UI** for manual review and corrections
-   **Features auto-backup** to prevent data loss during processing

---

## 📊 Global Content Insights

We have analyzed the metadata from the scanned archive (`1947-2012`) to generate the following insights:

### 📈 Overview
| Metric | Count |
| :--- | :--- |
| **Total Stories** | **10,212** |
| **Unique Authors** | **2,509** |
| **Unique Keywords** | **17,739** |

### 🏆 Top Categories

#### 📝 Top 5 Authors
| Rank | Author Name (Telugu) | Stories Count |
| :--- | :--- | :--- |
| 1 | **చందమామ బృందం** (Chandamama Team) | 5,115 |
| 2 | **Unknown** (Various/Unsigned) | [Aggregated] |
| 3 | **చక్రపాణి** (Chakrapani) | 80 |
| 4 | **కొడవటిగంటి కుటుంబరావు** | 72 |
| 5 | **దాసరి సుబ్రహ్మణ్యం** | 65 |

#### 📚 Top 5 Genres
| Rank | Genre (Telugu) | English | Count |
| :--- | :--- | :--- | :--- |
| 1 | **నీతి కథ** | Moral Story | 1,648 |
| 2 | **జానపదం** | Folklore | 834 |
| 3 | **పౌరాణికం** | Mythology | 276 |
| 4 | **హాస్యం** | Humor | 195 |
| 5 | **అద్భుత కథ** | Fantasy | 142 |

#### 🏷️ Top 5 Keywords
| Rank | Keyword (Telugu) | English | Count |
| :--- | :--- | :--- | :--- |
| 1 | **మోసం** | Deception | 500 |
| 2 | **విక్రమార్కుడు** | Vikramarka | 372 |
| 3 | **దొంగతనం** | Theft | 272 |
| 4 | **తెలివి** | Wit | 185 |
| 5 | **రాజకుమారి** | Princess | 134 |

---

## Completion Status

### Overall Progress: **757 JSON files created out of 786 expected (Jul 1947 — Dec 2012)**

#### By Year Summary:

| Year | Status | Months | Notes |
|------|--------|--------|-------|
| **1947** | ✓ Completed | 6/6 | Jul-Dec (Jan-Jun not published) |
| **1948** | ✓ Completed | 12/12 | All months |
| **1949** | ✓ Completed | 12/12 | All months |
| **1950** | ✓ Completed | 9/12 | Jan-Jul,Nov,Dec (Aug-Oct not published) |
| **1951** | ✓ Completed | 12/12 | All months |
| **1952** | ✓ Completed | 12/12 | All months |
| **1953** | ✓ Completed | 12/12 | All months |
| **1954** | ✓ Completed | 11/12 | Jan not verified |
| **1955** | ✓ Completed | 12/12 | All months |
| **1956** | ✓ Completed | 11/12 | May not verified |
| **1957** | ✓ Completed | 12/12 | All months |
| **1958** | ✓ Completed | 12/12 | All months |
| **1959** | ✓ Completed | 12/12 | All months |
| **1960** | ✓ Completed | 12/12 | All months |
| **1961** | ✓ Completed | 12/12 | All months |
| **1962** | ✓ Completed | 12/12 | All months |
| **1963** | ✓ Completed | 12/12 | All months |
| **1964** | ✓ Completed | 12/12 | All months |
| **1965** | ✓ Completed | 12/12 | All months |
| **1966** | ✓ Completed | 12/12 | All months |
| **1967** | ✓ Completed | 12/12 | All months |
| **1968** | ✓ Completed | 12/12 | All months |
| **1969** | ✓ Completed | 12/12 | All months |
| **1970** | ✓ Completed | 12/12 | All months |
| **1971** | ✓ Completed | 12/12 | All months |
| **1972** | ✓ Completed | 12/12 | All months |
| **1973** | ✓ Completed | 12/12 | All months |
| **1974** | ✓ Completed | 12/12 | All months |
| **1975** | ✓ Completed | 12/12 | All months |
| **1976** | ✓ Completed | 12/12 | All months |
| **1977** | ✓ Completed | 11/12 | Aug not published |
| **1978** | ✓ Completed | 12/12 | All months |
| **1979** | ✓ Completed | 12/12 | All months |
| **1980** | ✓ Completed | 12/12 | All months |
| **1981** | ✓ Completed | 12/12 | All months |
| **1982** | ✓ Completed | 12/12 | All months |
| **1983** | ✓ Completed | 12/12 | All months |
| **1984** | ✓ Completed | 12/12 | All months |
| **1985** | ✓ Completed | 12/12 | All months |
| **1986** | ✓ Completed | 12/12 | All months |
| **1987** | ✓ Completed | 12/12 | All months |
| **1988** | ✓ Completed | 12/12 | All months |
| **1989** | ✓ Completed | 12/12 | All months |
| **1990** | ✓ Completed | 12/12 | All months |
| **1991** | ✓ Completed | 12/12 | All months |
| **1992** | ✓ Completed | 12/12 | All months |
| **1993** | ✓ Completed | 12/12 | All months |
| **1994** | ✓ Completed | 11/12 | Dec not verified |
| **1995** | ✓ Completed | 11/12 | Feb not verified |
| **1996** | ✓ Completed | 12/12 | All months |
| **1997** | ✓ Completed | 12/12 | All months |
| **1998** | ⚠️ Partial | 3/12 | Feb,Apr,Jun-Dec not published |
| **1999** | ⚠️ Partial | 1/12 | Jan-Nov not published |
| **2000** | ✓ Completed | 12/12 | All months |
| **2001** | ✓ Completed | 12/12 | All months |
| **2002** | ✓ Completed | 12/12 | All months |
| **2003** | ✓ Completed | 12/12 | All months |
| **2004** | ✓ Completed | 12/12 | All months |
| **2005** | ✓ Completed | 12/12 | All months |
| **2006** | ✓ Completed | 11/12 | Feb not verified |
| **2007** | ✓ Completed | 12/12 | All months |
| **2008** | ✓ Completed | 12/12 | All months |
| **2009** | ✓ Completed | 12/12 | All months |
| **2010** | ✓ Completed | 12/12 | All months |
| **2011** | ✓ Completed | 12/12 | All months |
| **2012** | ✓ Completed | 12/12 | All months |

### Key Statistics:

-   **Total Years Covered**: 66 years (1947-2012)
-   **Total JSON Files (in `1947-2012/` data folder)**: 757
-   **Expected Total (Jul 1947 — Dec 2012)**: 786 months
-   **Missing Months**: 29
-   **Completion Rate**: **96.31%** (757 / 786)

*Notes: expected total count months from July 1947 (first available issue) through December 2012.*

### Books Not Published / Incomplete:

The following years have missing or incomplete publication records:
1947, 1950, 1954, 1956, 1977, 1994, 1995, 1998, 1999, 2006 (See table above for details).

## Team Assignments

The project has been distributed across team members for verification and completion:

-   **Divyansh**: 1947-1963, 2003-2012
-   **Sanjay**: 1964-1980, 1997-2002
-   **Sudheer**: 1981-1996

## Project Structure

```text
Chandamama_2.0_Catalouge/
├── 1947-2012/                   # Main data directory
│   ├── 1947/                    # Year folders
│   ├── ...
│   └── 2012/
│       └── [Month_Folders_&_PDFs]
│
└── MetaData_Extractor/          # Python Application Code
    ├── instructions.md          # Guide: How to Run the Code
    ├── streamlit_indexer.py     # Main application
    ├── regenerate_stats.py      # Stats Aggregator
    ├── report.md                # Project Report
    ├── global_stats.json        # Live Repository Statistics
    └── requirements.txt         # Python dependencies
```

## How to Use This Data

1.  **Browse by Year**: Navigate to any year folder (1947-2012) to find issues for that year
2.  **JSON Format**: Each issue is stored as a JSON file with metadata including stories, authors, and content information
3.  **File Naming**: Files follow the pattern `చందమామ_YEAR_MONTH.json` (in Telugu script)

## How to Run the Code

For detailed instructions on installation and running the Indexer tool, see:
👉 **[MetaData_Extractor/instructions.md](MetaData_Extractor/instructions.md)**

## License & Attribution

This is a digitization project of Chandamama Magazine archives. Please attribute appropriately when using this data.

---

**Last Updated**: December 24, 2025

