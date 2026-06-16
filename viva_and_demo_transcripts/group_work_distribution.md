# Viva & Presentation Group Work Distribution

This document outlines a balanced task distribution for presenting the 15 slides and conducting the live Jupyter notebook code demonstrations during the viva.

---

## 6-Presenter Distribution Plan (Primary)

### Presenter 1: Introduction & Task 1 Theory
* **Slides to Present**:
  * **Slide 1**: Title Slide (Group Introduction)
  * **Slide 2**: Task 1 Overview (Story Continuation Objectives & Core Questions)
  * **Slide 3**: Sequence Modeling: LSTM Architecture (Why LSTM? Forget, Input, Output Gates)
* **Focus Area**: Set the stage, introduce the team, and explain why standard RNNs fail (vanishing/exploding gradients) and how LSTM gates protect memory.

### Presenter 2: Data Pipeline & Decoding Strategies
* **Slides to Present**:
  * **Slide 4**: Data Pipeline & Corpuses (Shakespeare vs. Sherlock Holmes, input slicing length T=100)
  * **Slide 5**: Decoding and Sampling (Greedy decoding vs. Temperature-based probabilistic sampling)
* **Focus Area**: Explain how characters are prepared and text is sliced, and the theory of why temperature ($T$) controls randomness/creativity.

### Presenter 3: Task 1 Results & Live LSTM Demo
* **Slides to Present**:
  * **Slide 6**: Task 1: Training Loss & Text Samples
* **Live Demo Duty**:
  * Open `task1_story_continuation.ipynb` on Jupyter.
  * Show the loss convergence plot.
  * Generate text live starting with the prompt `"the secret of "` under different temperatures ($T=0.2, 0.6, 1.5$) to demonstrate the transition from repetitive text to balanced writing, and finally to chaotic gibberish.
* **Focus Area**: Show empirical results and stylistic differences (Shakespeare's poetic vs. Sherlock's modern detective tone).

### Presenter 4: Task 2 Overview & MLP Setup
* **Slides to Present**:
  * **Slide 7**: Task 2: Batch Norm vs. No Batch Norm (Objective, Internal Covariate Shift, Vanishing Gradients)
  * **Slide 8**: Deep MLP Architecture and Setup (6-layer layout on MNIST dataset)
  * **Slide 9**: Experiment 1: Standard SGD Training (LR = 0.01, standard initialization)
* **Focus Area**: Introduce the deep feedforward setup and show that under standard conditions, Batch Norm acts as an optimization accelerator (97.10% vs. 92.83% accuracy).

### Presenter 5: Task 2 Stress Tests & Live MLP Demo
* **Slides to Present**:
  * **Slide 10**: Experiment 2: High Learning Rate Stress Test (LR = 0.2)
  * **Slide 11**: Experiment 3: Poor Initialization Stress Test ($\sigma = 0.001$)
* **Live Demo Duty**:
  * Open `task2_batch_norm.ipynb` on Jupyter.
  * Show the live performance curves.
  * Highlight that without Batch Norm, both stress tests completely fail (accuracy flatlines at 11.35% random guessing), whereas with Batch Norm, the model trains successfully (>97% accuracy).
* **Focus Area**: Explain how normalization stabilizes the network under aggressive hyperparameters and bad weight scales.

### Presenter 6: Batch Norm Math, Theory & Conclusion
* **Slides to Present**:
  * **Slide 12**: How Batch Normalization Stabilizes Gradients (Mini-batch Mean, Variance, Normalize, Scale & Shift)
  * **Slide 13**: Summary of Empirical Findings (Table walkthrough)
  * **Slide 14**: Connections to Deep Learning Theory (Representation learning, He/Xavier initialization, optimization landscapes)
  * **Slide 15**: Conclusion & Q&A
* **Focus Area**: Explain the mathematical step-by-step calculations of normalization, walk through the summary table, tie the project back to the Weeks 1-7 curriculum, and field the final questions.

---

## 7-Presenter Distribution Plan (Alternative)
*If Shiva Gupta is also presenting, use this modified split to distribute the final sections more evenly:*

* **Presenter 1**: Slides 1, 2, 3 (Intro & LSTM Theory)
* **Presenter 2**: Slides 4, 5 (Data Pipeline & Temperature Theory)
* **Presenter 3**: Slide 6 + **Live LSTM Demo** (Task 1 Results)
* **Presenter 4**: Slides 7, 8, 9 (Task 2 Intro, Setup & Standard Training)
* **Presenter 5**: Slide 10, 11 + **Live MLP Demo** (Stress Tests)
* **Presenter 6 (Shiva Gupta)**: Slides 12, 13 (Batch Norm Math & Empirical Summary Table)
* **Presenter 7**: Slides 14, 15 (Deep Learning Theory Connections, Conclusions & Q&A)
