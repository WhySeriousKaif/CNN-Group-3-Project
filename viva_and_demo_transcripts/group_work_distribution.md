# Group Task & Code Distribution Plan (7 Members)

This document outlines the collaborative task distribution for our group project, dividing tasks by project work, slide-making, and presentation roles.

---

## 1. Project & Code Division (How the Team Worked)

To ensure high-quality implementations, we divided our group of 7 members into two project-focused subgroups:

### A. Project 21 (Task 1: AI Story Continuation - LSTMs)
* **Code Contributors**: 
  * **MD Kaif Molla** (LSTM Network Architecture & hidden state mechanics)
  * **Arhan Das** (Data preprocessing pipeline, lowercasing, and overlapping sequence generation)
  * **Sumit Akhuli** (Temperature-based inference sampling functions and logit decoding)

### B. Project 23 (Task 2: Batch Normalization Comparison)
* **Code Contributors**:
  * **Sarthak Mishra** (6-layer Deep MLP design and baseline training code)
  * **Netram Faran** (Learning rate and weight initialization scale stress-test setups)
  * **Aditya Prasad** (Mathematical derivations and empirical summary table)
  * **Shiva Gupta** (Training metrics logs, convergence curves, and final output plots)

### C. Slide-Making & Presentation Design
* **Slide Designers**:
  * **Shiva Gupta** & **Arhan Das** (Designed the presentation slides, programmatically compiled `presentation.pptx` using `python-pptx`, and styled the layouts and mathematical formulas for maximum readability)

---

## 2. Spoken Script: What to Say to Sir

During the viva/presentation, the group leader can explain the distribution to the evaluator as follows:

> **"Sir, to ensure maximum quality and focus, we distributed our group responsibilities by project expertise and skills:**
> 
> * **Project 21 (Character-level LSTM)** was developed by **Kaif Molla**, **Arhan Das**, and **Sumit Akhuli**. They handled the sequence modeling, data slicing, and temperature decoding logic.
> * **Project 23 (Batch Norm vs. Baseline)** was developed by **Sarthak Mishra**, **Netram Faran**, **Aditya Prasad**, and **Shiva Gupta**. They built the deep MLP, implemented the optimization stress-tests, and compiled the normalization equations.
> * **The Slides & Presentation Design** were co-authored and formatted by **Shiva Gupta** and **Arhan Das**, ensuring all technical tables and formulas are properly aligned.
> 
> **For this presentation, the members who coded Task 1 will present the first half of the slides (our LSTM results), and the members who coded Task 2 will present the second half of the slides (our Batch Norm analysis), along with our live Jupyter demonstrations."**

---

## 3. Individual Presentation & Demo Assignments

| Group Member | Core Project Area | Slide Presentation Assignment | Live Demonstration Duty |
| :--- | :--- | :--- | :--- |
| **1. MD Kaif Molla** | Project 21 (LSTM) | **Slides 1, 2**: Title Slide & Task 1 Overview. | **Live LSTM Demo**: Runs text generation live in Jupyter. |
| **2. Arhan Das** | Project 21 & Slides | **Slide 3**: LSTM Gating Architecture. | *Co-presents data loading details.* |
| **3. Sumit Akhuli** | Project 21 (LSTM) | **Slides 4, 5**: Data Pipeline & Decoding (Temperature). | *Co-presents temperature parameters.* |
| **4. Sarthak Mishra** | Project 23 (BN) | **Slides 7, 8**: Task 2 Overview & MLP Setup. | *Co-presents MLP architecture.* |
| **5. Netram Faran** | Project 23 (BN) | **Slides 9, 10**: Standard Training & High Learning Rate Test. | **Live MLP Demo**: Runs MNIST convergence stability comparison live. |
| **6. Shiva Gupta** | Project 23 & Slides | **Slide 6** (LSTM Results) & **Slide 11** (Poor Initialization Test). | *Assists both live notebook demos.* |
| **7. Aditya Prasad** | Project 23 (BN) | **Slides 12, 13, 14, 15**: BN Equations, Summary Table, Theory Connections, and Q&A. | *Coordinates Q&A slides.* |
