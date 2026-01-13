# Metadata Generation Procedure Report

**Date:** January 13, 2026
**Model Used:** `gemini-2.5-flash-preview-09-2025`
**Tooling:** Streamlit, Python (`requests`, `json_repair`)

## 1. Overview
This report outlines the procedure used to extract structured metadata and content from the Chandamama magazine archive (PDFs) using the Google Gemini 2.5 Flash Preview model. The goal was to transform raw scanned documents into a queryable JSON dataset.

## 2. Methodology

### 2.1 Model Configuration
- **Model**: `gemini-2.5-flash-preview-09-2025` was selected for its enhanced long-context understanding and reasoning capabilities.
- **Access**: Accessed via direct REST API calls (`generativelanguage.googleapis.com`) to allow fine-grained control over request headers and retry logic.

### 2.2 The Pipeline

#### Step 1: Ingestion & Preprocessing
- **Interface**: A custom **Streamlit** application (`streamlit_indexer.py`) serves as the control center, offering "Single File" and "Bulk Processing" modes.
- **Encoding**: PDF files are read as binary and converted to **Base64** strings for inline transmission to the API.

#### Step 2: Prompt Engineering
A robust system instruction was designed to act as an "Expert Chandamama Magazine Indexer". Key components of the prompt include:
- **Structural Tasks**: Extracting the Index/Table of Contents.
- **Content Extraction**: Capturing full story text in Telugu, ensuring no truncation.
- **Metadata Fields**:
    - `author`: Defaults to "చందమామ బృందం" if not explicitly named.
    - `genre`, `moral`, `keywords`, `characters`, `locations`.
    - **Page Mapping**: Distinguishing between `pdf_page_start` (file sequence) and `book_page_start` (printed page number).
- **Format Control**: Strict JSON schema enforcement.

#### Step 3: Post-Processing & Validation
- **JSON Repair**: The `json_repair` library is utilized to handle and fix common LLM JSON syntax errors (e.g., missing commas, unescaped quotes).
- **Heuristics**: A custom logic calculates `book_page_end` by combining the extracted `book_page_start` with the physical `pdf_page_count`.
- **Statistics**: Scripts automatically aggregate global statistics (Author counts, Genre distributions) into `global_stats.json`.

#### Step 4: Verification
- The Streamlit UI provides a "Verification" step where users can review the extracted data, make manual edits to the JSON structure, and mark files as "Verified" before final export.

## 3. Output Artifacts
- **Individual JSONs**: Each magazine issue is saved as `[book_id].json` containing the full array of stories.
- **Global Stats**: A cumulative `global_stats.json` tracking the entire corpus's metadata distribution.
