# reverse-engineering-ai-sca
Deep Learning-based Reverse Engineering via Side Channel Analysis

## 📌 Overview
This repository contains the code, datasets, and experimental setup for the PhD thesis project:  
**"Pseudo-labeling for Deep Learning-based Side-channel Disassembly Using Contextual Layer and Feature Engineering"**

The study proposes a multi-phase framework for advanced side-channel based disassembly and dummy instruction detection using deep learning, feature engineering, and contextual sequence modeling.

---

## Objectives

- Develop a **pseudo-labeling** model to estimate power traces from assembly code.
- Create a **disassembly** model using engineered features and contextual models.
- Implement a **dummy instruction detection** model using sequence labeling.

---

## Methodology Summary

1. **Dataset Creation**
   - Real cryptographic implementations (AES, RSA, DES, etc.)
   - Power traces generated via Signed Hamming Distance model
   - Total: 1.76 million samples, 24 instruction classes

2. **Leakage Modeling**
   - Side channel leakage modeling using a sequential model.
   - Leveraging contextual and embedding layers for accurate power leakage prediction.

4. **Pseudo-labeling**
   - GRU-based model with context embeddings and temporal attention
   - Outputs estimated power traces for unlabeled instruction sequences

5. **Feature Engineering**
   - Moving average, autocorrelation, and MLTI (Moving Log-transformed Temporal Interaction)

6. **Dummy Detection**
   - LSTM-based sequence labeling with token embedding
   - Detects obfuscation techniques like inserted dummy instructions
7. **LLM for Assembly to C**
   - After recovering the Assembly language, an LLM is used for converting it to human-readable C code

---

## Key Results

- Power Estimation (R² = 0.9963)
- Disassembly Accuracy: High with MLTI + window size = 15
- Dummy Detection Accuracy: 97.9% with LSTM

---

## Figures & Tables

> Placeholder: Replace with actual image links or embedded visuals

- **Fig 1:** Side-channel disassembly steps  
- **Fig 2:** Disassembly via template device  
- **Fig 3:** DL Models Overview  
- **Fig 4:** Dummy instruction example  
- **Fig 5:** Proposed Architecture  
- **Fig 6:** Instruction Prediction Flow  
- **Fig 7–11:** Experimental results, performance comparisons, and variation analyses

> Place figures in the `figures/` folder and reference them here using:  
> `![Figure Title](figures/figure-name.png)`

---

## Experiments

- Architecture comparisons: GRU, Transformer, LSTM + ANN
- Window size sensitivity analysis
- The effect of contextual layers in leakage modeling
- Cross-dataset validation
- Dummy instruction detection with sequence tokenization

---

## Related Publications

1. *Applied Sciences* — CTGAN for IDS dataset generation (Accepted)
2. *Expert Systems with Applications* — Feature engineering for SCA (Revision)
3. *Sensors* — CTGAN for privacy-preserving IDS (Revision)
4. *ACM TOSEM* — Contextual leakage modeling (Under review)
