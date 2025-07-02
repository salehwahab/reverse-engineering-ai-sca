# reverse-engineering-ai-sca
Deep Learning-based Reverse Engineering via Side Channel Analysis

## 📌 Overview
This repository contains the code, datasets, and experimental setup for the PhD thesis project:  
**"Pseudo-labeling for Deep Learning-based Side-channel Disassembly Using Contextual Layer and Feature Engineering"**

The study proposes a multi-phase framework for advanced side-channel based disassembly and dummy instruction detection using deep learning, feature engineering, and contextual sequence modeling.

---

## Contents

- `notebooks/` — Jupyter notebooks for each stage of modeling
- `datasets/` — Processed datasets for training and evaluation
- `models/` — Pretrained models and architecture definitions
- `figures/` — Placeholder for result visualizations and architecture diagrams
- `README.md` — This file

---

## Research Objectives

- Develop a **pseudo-labeling** model to estimate power traces from assembly code.
- Create a **disassembly** model using engineered features and contextual models.
- Implement a **dummy instruction detection** model using sequence labeling.

---

## Methodology Summary

1. **Dataset Creation**
   - Real cryptographic implementations (AES, RSA, DES, etc.)
   - Power traces generated via Signed Hamming Distance model
   - Total: 1.76 million samples, 24 instruction classes

2. **Pseudo-labeling**
   - GRU-based model with context embeddings and temporal attention
   - Outputs estimated power traces for unlabeled instruction sequences

3. **Feature Engineering**
   - Moving average, autocorrelation, and MLTI (Moving Log-transformed Temporal Interaction)

4. **Dummy Detection**
   - LSTM-based sequence labeling with token embedding
   - Detects obfuscation techniques like inserted dummy instructions

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
- Cross-dataset validation
- Dummy instruction detection with sequence tokenization

---

## Related Publications

1. *Applied Sciences* — CTGAN for IDS dataset generation (Accepted)
2. *Expert Systems with Applications* — Feature engineering for SCA (Revision)
3. *Sensors* — CTGAN for privacy-preserving IDS (Revision)
4. *ACM TOSEM* — Contextual leakage modeling (Under review)
