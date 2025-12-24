# Chandamama Magazine Indexer (Catalogue 2.0)

A comprehensive structured searchable JSON catalogue for the *Chandamama* magazine archive (1947–2012).

## 📂 Repository Structure

```text
Chandamama_2.0_Catalouge/
├── 1947-2012/                   # Data Archive (The Dataset)
│   ├── 1947/                    # Year-wise Folders
│   ├── ...
│   └── 2012/
│       └── [Month_Folders_&_PDFs]
│
└── MetaData_Extractor/          # Python Application Code
    ├── instructions.md          # How to Run the Code
    ├── streamlit_indexer.py     # Main Application
    ├── regenerate_stats.py      # Statistics Script
    ├── report.md                # Project Report
    └── global_stats.json        # Live Repository Statistics
```

## 📊 Global Dataset Insights

Below are the aggregated statistics from the entire archive (`1947-2012`).

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
| 1 | **చందమామ బృందం** | 5,115 |
| 2 | **Unknown** | [Aggregated] |
| 3 | **చక్రపాణి** | 80 |
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

## � Getting Started

### Clone the Repository
```bash
git clone https://github.com/your-username/Chandamama_2.0_Catalouge.git
cd Chandamama_2.0_Catalouge
```

### Running the Code
For detailed instructions on how to install dependencies and run the Metadata Extractor tool, please refer to:
👉 **[MetaData_Extractor/instructions.md](MetaData_Extractor/instructions.md)**

---
*Last Updated: December 24, 2025*
