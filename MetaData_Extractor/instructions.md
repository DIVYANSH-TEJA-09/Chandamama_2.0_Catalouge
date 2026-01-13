# Indexer Usage Instructions

This document contains detailed instructions on how to use the **Metadata Extractor** tool.

## 🚀 Installation

### 1. Prerequisites
-   Python 3.8 or higher.
-   A Google Gemini API Key.

### 2. Install Dependencies
Navigate to the `MetaData_Extractor` directory and run:
```bash
cd MetaData_Extractor
pip install -r requirements.txt
```

## 🛠️ Running the Application

### Start the Indexer
Run the Streamlit app:
```bash
streamlit run streamlit_indexer.py
```

## 📖 Features Guide

### Mode 1: Single File Processing
Use this to debug specific PDFs or check extraction quality.
1.  Select **"Single File"** in the sidebar.
2.  Upload a PDF.
3.  Enter your API Key.
4.  Click **"Analyze PDF"**.
5.  Download the result as JSON.

### Mode 2: Bulk Processing
Use this to index an entire folder (e.g., a specific Year).
1.  Select **"Bulk Processing"**.
2.  Enter the directory path (e.g., `../1947-2012/1954`).
3.  Click **"Start Batch Processing"**.
    -   The app creates a `_bulk_progress_backup.json` to save state.
    -   You can stop and resume at any time.

### Global Statistics Regeneration
If you have added new files or want to refresh the stats:
1.  Open `MetaData_Extractor`.
2.  Run the regeneration script:
    ```bash
    python regenerate_stats.py
    ```
3.  This will verify all JSONs in the `1947-2012` folder and update `global_stats.json`.