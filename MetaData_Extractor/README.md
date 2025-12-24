# Chandamama Magazine Indexer (Catalogue 2.0)

A comprehensive tool to extract, index, and analyze metadata from the *Chandamama* magazine archive (1947–2012). This project leverages the **Google Gemini API** (using the official SDK and File API) to process thousands of scanned PDFs into a structured, searchable JSON catalogue.

## 📂 Repository Structure

The project is organized as follows:

```text
Chandamama_2.0_Catalouge/
├── 1947-2012/                   # Data Archive
│   ├── 1947/                    # Year-wise Folders
│   ├── ...
│   └── 2012/
│       └── [Month_Folders_&_PDFs]
│
└── MetaData_Extractor/          # Core Application
    ├── streamlit_indexer.py     # Main Application (Streamlit)
    ├── regenerate_stats.py      # Global Statistics Aggregator
    ├── report.md                # Detailed Project Journey Report
    ├── global_stats.json        # Live Repository Statistics
    └── requirements.txt         # Python Dependencies
```

## 📊 Global Insights

We have processed and indexed the vast majority of the archive. Based on `global_stats.json`:

*   **Total Stories Indexed**: **10,212**
*   **Unique Authors**: 2,509
*   **Unique Keywords**: 17,739

### Top Categories

#### 📝 Top 5 Authors
1.  **చందమామ బృందం** (Chandamama Team) - 5,115 stories
2.  **Unknown** - (Various unsigned)
3.  **చక్రపాణి** (Chakrapani) - 80 stories
4.  **కొడవటిగంటి కుటుంబరావు** (Kodavatiganti Kutumbarao)
5.  **దాసరి సుబ్రహ్మణ్యం** (Dasari Subrahmanyam)

#### 📚 Top 5 Genres
1.  **నీతి కథ** (Moral Story) - 1,648 stories
2.  **జానపదం** (Folklore)
3.  **పౌరాణికం** (Mythology) - 276 stories
4.  **హాస్యం** (Humor)
5.  **అద్భుత కథ** (Fantasy/Wonder)

#### 🏷️ Top 5 Keywords
1.  **మోసం** (Deception) - 500
2.  **విక్రమార్కుడు** (Vikramarka) - 372
3.  **దొంగతనం** (Theft) - 272
4.  **తెలివి** (Wit/Wisdom)
5.  **రాజకుమారి** (Princess)

---

## 🚀 Installation & Usage

### 1. Setup
Navigate to the `MetaData_Extractor` directory and install dependencies:
```bash
cd MetaData_Extractor
pip install -r requirements.txt
```

### 2. Run the Indexer
Start the Streamlit interface:
```bash
streamlit run streamlit_indexer.py
```

### 3. Features
*   **Single File Mode**: Debug and analyze individual PDFs.
*   **Bulk Processing**: Batch process entire year directories.
*   **Verification**: Review and verify extracted metadata.
*   **Regeneration**: Run `python regenerate_stats.py` to update the global stats file by scanning the entire catalogue.

---
*Last Updated: December 24, 2025*
