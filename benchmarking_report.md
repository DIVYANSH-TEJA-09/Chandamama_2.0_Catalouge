# Deep-Dive Analysis: Gemini OCR vs Test OCR Benchmarking

**Date:** 2026-01-13
**Status:** Complete (Sampled)

## 1. Executive Summary
This document provides a comprehensive analysis of the relative benchmarking performed between two datasets:
1.  **Ground Truth (Reference)**: `gemini_ocr` (Derived from 1947-2012 JSONs).
2.  **Hypothesis (Test)**: `test_ocr` (Originally `verified-text`).

The goal was to purely evaluate the textual deviation of the `test_ocr` dataset against the `gemini_ocr` standard using **Relative Character Error Rate (rCER)**.

**Key Findings:**
-   **Average rCER**: **19.89%** (High deviation).
-   **Safe Pages**: **0%** found in the sample.
-   **Conclusion**: The `test_ocr` dataset is significantly different from the `gemini_ocr` baseline, indicating it is unreliable for downstream tasks without identical manual correction or heavy post-processing.

---

## 2. Methodology

### 2.1 The Metric: Relative Character Error Rate (rCER)
We utilized the Levenshtein Distance algorithms to compute the edit distance between the two text samples.

**The Formula:**
```math
rCER = \frac{Levenshtein(Reference, Hypothesis)}{\max(|Reference|, |Hypothesis|)}
```

**Where:**
-   `Levenshtein(a, b)`: The minimum number of single-character edits (insertions, deletions, or substitutions) required to change *a* into *b*.
-   `|Reference|`: Character count of the Ground Truth text.
-   `|Hypothesis|`: Character count of the Test text.

**Why this metric?**
rCER provides a normalized score between 0.0 (Perfect Match) and 1.0 (Complete Mismatch), making it length-independent.

### 2.2 Text Normalization
Before comparison, both datasets underwent identical rigorous normalization to ensure fair scoring:
1.  **Unicode Normalization**: Converted all text to **NFC** (Normalization Form C) to handle Telugu character composition consistently.
2.  **Whitespace Standardization**:
    -   Removed non-breaking spaces.
    -   Collapsed multiple spaces into a single space.
    -   Trimmed leading/trailing whitespace.
3.  **Punctuation Handling**:
    -   Normalized Danda (`॥`) to dot (`.`).
    -   Normalized Em-dash (`—`) to hyphen (`-`).

---

## 3. Dataset Roles

| Role | Directory | Description |
| :--- | :--- | :--- |
| **Reference (GT)** | `gemini_ocr` | Extracted from the `1947-2012` JSON archive. This represents the current "Gold Standard" for this benchmark. |
| **Hypothesis** | `test_ocr` | Text from the `verified_dataset`. This is the candidate dataset being evaluated for accuracy. |

---

## 4. Quantitative Analysis

Based on a representative sample of **43 processed pages**, the following metrics were observed:

### 4.1 Global Metrics
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Average rCER** | **0.1989** (19.89%) | On average, nearly 20% of characters on every page are incorrect/mismatched. |
| **Median rCER** | **0.1383** (13.83%) | The median suggests that while some pages are very bad, the "typical" page still has ~14% error. |

### 4.2 Confidence Distribution
We categorized pages into four quality tiers. **Not a single page met the high-quality threshold.**

| Confidence Label | Threshold (Error Rate) | Page Count | Percentage |
| :--- | :--- | :--- | :--- |
| **High** | < 3% | **0** | **0.0%** |
| **Medium** | 3% - 7% | 13 | 30.2% |
| **Low** | 7% - 12% | 7 | 16.3% |
| **Very Low** | > 12% | **23** | **53.5%** |

### 4.3 The "Long Tail" of Errors
With **53.5%** of pages falling into the "Very Low" confidence category (Errors > 12%), the dataset exhibits systemic divergence. This isn't just random typos; it suggests structural differences, missing paragraphs, or fundamentally different OCR engines/source texts.

---

## 5. Conclusions & Recommendations

### Conclusions
1.  **High Divergence**: A ~20% error rate is too high for automated unsupervised ingestion.
2.  **No "Safe" Subset**: The absence of any "High Confidence" pages means simple filtering will not yield a usable clean subset.
3.  **Systemic Issue**: The high correlation of errors suggests the `test_ocr` dataset might be derived from a completely different pre-processing pipeline or source file version than `gemini_ocr`.

### Recommendations
1.  **Do Not Merge**: Do not attempt to automatically merge `test_ocr` with `gemini_ocr`.
2.  **Manual Review**: If `test_ocr` contains human corrections (as the name `verified` might imply), a human review is required to see *why* it differs from Gemini. It is possible Gemini is wrong and Test is right, but statistically, they are simply **different**.
3.  **Use Gemini as Base**: For any RAG or Search tasks, utilize `gemini_ocr` as the primary source until manual verification can resolve the 20% delta.
