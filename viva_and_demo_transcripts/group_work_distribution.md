# Group Task & Code Distribution Plan (7 Members)

This document provides a clean distribution of work among the 7 group members, covering both **code development** and **presentation duties (including live demos)**. It also contains the exact spoken script you can use to explain this distribution to your professor ("Sir") during the viva.

---

## 1. Work Distribution Table

| Group Member | Code Development Contribution | Slide Presentation Assignment | Live Demonstration Duty |
| :--- | :--- | :--- | :--- |
| **1. MD Kaif Molla** | Programmed the character-level Stacked LSTM architecture and temporal hidden state mechanics. | **Slides 1, 2, 3**: Title, Task 1 Overview, LSTM Gating Theory. | *Co-presents Task 1 context.* |
| **2. Arhan Das** | Developed the text-processing pipeline, character-to-index vocabulary maps, and dataset sequence generator. | **Slide 4**: Data Pipeline & Corpuses (Shakespeare vs. Sherlock). | *Co-presents data loading details.* |
| **3. Sumit Akhuli** | Programmed the temperature-based decoding inference functions and logit scaling loops. | **Slide 5**: Decoding and Sampling Techniques. | *Co-presents temperature parameters.* |
| **4. Shiva Gupta** | Managed training logs, compiled sequence loss metrics, and extracted final generated text samples. | **Slide 6**: Task 1 Training Loss & Samples. | **Live LSTM Demo**: Runs text generation live under $T=0.2, 0.6, 1.5$ in Jupyter. |
| **5. Sarthak Mishra** | Programmed the 6-layer Deep MLP baseline and inserted `nn.BatchNorm1d` modules. | **Slides 7, 8, 9**: Task 2 Intro, Setup & Standard Training. | *Co-presents standard training metrics.* |
| **6. Netram Faran** | Designed the hyperparameter stress-test suite (exploding learning rate and near-zero weight initialization). | **Slides 10, 11**: Stress-tests (LR=0.2 and $\sigma=0.001$). | **Live MLP Demo**: Runs MNIST convergence stability comparison live in Jupyter. |
| **7. Aditya Prasad** | Drafted mathematical latex formulations for Batch Norm steps and compiled final metrics. | **Slides 12, 13, 14, 15**: BN Equations, Summary Table, Theory Connections, and Q&A. | *Coordinates Q&A slides.* |

---

## 2. Spoken Script: What to Say to Sir

When introducing the presentation and demonstrating your group's contribution, the group leader (or first speaker) can say the following to the evaluator:

> **"Sir, before we begin, we would like to highlight that both our code development and presentation duties have been distributed equally among all 7 members to ensure deep understanding of the entire project:**
> 
> * **Kaif Molla** developed the Stacked LSTM sequence layers in Code Task 1, and will present the LSTM gating mechanics.
> * **Arhan Das** coded the raw data preparation, vocabulary mapping, and overlapping sequence slicing. He will present our data pipeline.
> * **Sumit Akhuli** implemented the temperature inference sampling logic, and will explain the decoding strategies.
> * **Shiva Gupta** managed the training loops and compiled our loss plots, and will handle our live text generation demo.
> * **Sarthak Mishra** programmed the deep MLP baseline and Batch Normalization layers in Task 2, and will introduce the MLP configuration.
> * **Netram Faran** designed the stress-test scripts evaluating extreme learning rates and initialization scales, and will perform the live MLP stabilization demo.
> * **Aditya Prasad** formulated the Batch Norm mathematical equations, analyzed the theory connections, and will walk through our empirical conclusions.
> 
> **Each member has worked hands-on with the code notebooks and report, and is prepared to answer any technical questions about their respective sections."**

---

## 3. Detailed Presentation Roles

### Section 1: Sequence Modeling (Slides 1–6)
* **Presenter 1 (Kaif Molla)**: Introduces the group, outlines the capstone objective (spelling, grammar, and style learning from scratch), and describes how LSTMs solve vanishing gradients using forget, input, and output gates.
* **Presenter 2 (Arhan Das)**: Compares the Tiny Shakespeare dataset (37 chars, poetic) with Sherlock Holmes (57 chars, narrative), explaining why lowercasing and character-to-index mapping are necessary.
* **Presenter 3 (Sumit Akhuli)**: Contrasts greedy decoding (deterministic, loop-prone) with temperature-based softmax scaling.
* **Presenter 4 (Shiva Gupta)**: Explains the loss convergence curves. **Live Jupyter Demo**: Opens `task1_story_continuation.ipynb`, demonstrates loading the model parameters, inputs the prompt `"the secret of "`, and runs the model live at $T=0.2$ (repetitive), $T=0.6$ (fluent), and $T=1.5$ (gibberish) to show spelling deterioration.

### Section 2: Deep MLP & Batch Normalization (Slides 7–15)
* **Presenter 5 (Sarthak Mishra)**: Introduces Task 2, explaining Internal Covariate Shift and gradient failures. Explains the 6-layer architecture (784 $\rightarrow$ 5x512 $\rightarrow$ 10) and standard SGD convergence results (97.10% with BN vs. 92.83% without).
* **Presenter 6 (Netram Faran)**: Presents the two stress-tests: LR = 0.2 (where baseline diverges and BN thrives at 98.24%) and poor initialization scale $\sigma=0.001$ (where baseline vanishes and BN rescues training to 97.48%). **Live Jupyter Demo**: Opens `task2_batch_norm.ipynb`, shows the training runs live, highlighting how the baseline loss remains stuck at 2.3026 while BN recovers smoothly.
* **Presenter 7 (Aditya Prasad)**: Derives the 4-step Batch Norm equations ($\mu_B, \sigma_B^2, \hat{x}_i, y_i$). Summarizes all findings using the empirical table, explains connections to the Universal Approximation Theorem and Xavier/He initializations, and leads the Q&A segment.
