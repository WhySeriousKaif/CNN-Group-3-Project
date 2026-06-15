# Presentation Strategy & Demonstration Guidelines

This document outlines how to organize your presentation, handle questions under pressure, and manage the live Jupyter Notebook server during the evaluation.

---

## 1. Live Server Management (In case you need to execute code live)

* **Current Status**: A Jupyter server is currently running in your background. If you open:
  `http://localhost:8888/tree?token=3044ef9184eec40c3afa62982e4934d8247c6e5483614435`
  in your browser, you will see your notebook files.
* **If the professor says: "Run this cell for me right now"**:
  1. Simply navigate to the relevant cell.
  2. Press **Shift + Enter** or click the **Run** button at the top of the Jupyter window.
  3. The notebook will run instantly. The datasets are already downloaded and cached locally, so it will execute in a few seconds.
* **Note on Python versions**: If you ever need to restart the notebook server manually, remember to use `/usr/bin/python3 -m notebook` instead of the Homebrew python (which does not have the packages installed).

---

## 2. Group Presentation Roles & Flow (8-10 Minutes Total)

If you are presenting as a group, divide your roles clearly so you don't talk over each other:

1. **Presenter 1 (Introduction & Task 1 Theory)**:
   - Introduce the group and state the objectives.
   - Explain character-level representation learning and the LSTM architecture (Embedding, Gates, unrolling).
2. **Presenter 2 (Task 1 Demonstration & Sampling)**:
   - Walk through the `task1_story_continuation.ipynb` notebook.
   - Point out the loss curves and explain the differences between **Shakespeare** and **Sherlock Holmes** output styles.
   - Demonstrate the effect of **temperature** ($T=0$ greedy vs $T=0.6$ balanced vs $T=1.5$ chaotic).
3. **Presenter 3 (Task 2 Batch Norm Theory & Stress Tests)**:
   - Introduce Project 23 and the 6-layer Deep MLP architecture.
   - Explain internal covariate shift and why deep models struggle.
   - Explain the 3 stress test configurations (Standard, High LR, Small Init).
4. **Presenter 4 (Task 2 Demonstration & Results)**:
   - Show the `task2_batch_norm.ipynb` notebook.
   - Walk through the three plots and point out where the baseline fails (flatlining at loss 2.3026 / accuracy 11.35%).
   - Show that Batch Norm successfully completes all tests.
   - Deliver the concluding slides.

---

## 3. How to Handle Tough Questions (Viva Strategy)

Evaluators like to test how you handle unexpected scenarios. Use these strategic replies:

* **Scenario 1: You don't know the exact answer.**
  * *Bad response*: "I don't know" or guessing randomly.
  * *Good response*: *"Sir, we didn't test that specific parameter choice in our notebook, but based on the theory of [mention concept], we would expect the model to [explain theoretical consequence]."*
* **Scenario 2: The professor asks: "Why didn't you use a Transformer model like GPT for Task 1?"**
  * *Good response*: *"Sir, while Transformers utilize self-attention to process entire sequences in parallel, they require massive datasets and computing resources to train. For a character-level model trained locally on consumer hardware, LSTMs are far more resource-efficient and highly capable of demonstrating sequential memory and recurrence concepts within a short training window."*
* **Scenario 3: The professor asks: "Why did you use Batch Norm instead of Layer Norm?"**
  * *Good response*: *"For feedforward neural networks (MLPs) and CNNs, Batch Norm is the standard because normalizing across the batch stabilizes training by utilizing batch statistics. Layer Norm normalizes across features instead, which is preferred for Recurrent Neural Networks (RNNs) or Transformers where batch lengths vary, but Batch Norm is ideal for our static 6-layer MLP."*
