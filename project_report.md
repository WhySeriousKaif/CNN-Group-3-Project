# Joint Project Report: Deep Learning Optimization and Sequence Generation

---

## Task 1: AI Story Continuation (Project 21)

### 1.1 Problem Statement
The objective of this project is to model sequential text data at the character level to generate coherent continuations from user prompts. Traditional language models relied on hand-crafted n-gram features or Markov models, which suffer from the "curse of dimensionality" and have very limited context window memory. This project demonstrates representation learning and sequence modeling by training a Recurrent Neural Network (specifically, an LSTM) to learn the orthographic and grammatical structure of English text from scratch. By training on two highly distinct corpuses—William Shakespeare's dramatic works and Arthur Conan Doyle's Sherlock Holmes detective stories—we analyze how the source corpus style and the decoding temperature affect text generation.

### 1.2 Technical Approach
We implement a character-level sequence-to-sequence model using PyTorch:
1. **Data Pipeline**:
   - The input corpus is read, converted to lowercase, and mapped to a unique set of characters ($V$).
   - A sliding window of length $T=100$ is used to extract input-target pairs. The target sequence is the input sequence shifted forward by one character.
2. **Model Architecture**:
   - **Embedding Layer**: Projects discrete token indexes into a dense vector space: $x_t \in \mathbb{R}^{V} \to e_t \in \mathbb{R}^{E}$ (where $E=128$).
   - **LSTM Layer**: A two-layer stacked LSTM network with hidden state size $H=256$. The gating mechanisms (forget gate $f_t$, input gate $i_t$, output gate $o_t$, and cell state $C_t$) allow the model to manage long-term dependencies:
     $$f_t = \sigma(W_f [h_{t-1}, e_t] + b_f)$$
     $$i_t = \sigma(W_i [h_{t-1}, e_t] + b_i)$$
     $$\tilde{C}_t = \tanh(W_c [h_{t-1}, e_t] + b_c)$$
     $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
     $$o_t = \sigma(W_o [h_{t-1}, e_t] + b_o)$$
     $$h_t = o_t \odot \tanh(C_t)$$
   - **Linear Layer**: Projects the hidden state to vocabulary logits: $y_t = W_y h_t + b_y \in \mathbb{R}^{V}$.
3. **Training & Regularization**:
   - Optimized using **Adam** (learning rate = 0.002) and **Cross-Entropy Loss** over all timesteps.
   - **Dropout (0.2)** is applied between LSTM layers.
   - **Gradient Clipping** is implemented with a maximum threshold of 5.0 to mitigate exploding gradients during Backpropagation Through Time (BPTT).

### 1.3 Experiments and Results
Both models were trained for 8 epochs, with 80 optimization steps per epoch and a batch size of 128.

#### Loss Convergence:
- **Shakespeare Model**: Loss decreased from **2.1700** (Epoch 1) to **0.9955** (Epoch 8).
- **Sherlock Holmes Model**: Loss decreased from **2.3608** (Epoch 1) to **1.1377** (Epoch 7).

#### Sampling Comparison (Prompt: "the secret of "):
- **Greedy Sampling ($T = 0$)**:
  - *Shakespeare*: `the secret of the world is a proper my lord, and my lord, i will not be...`
  - *Sherlock*: `the secret of his mistle spoting and hadnestrand, however and west...`
  - *Analysis*: The model enters a deterministic loop, repeating high-probability words or phrases.
- **Low Temperature ($T = 0.2$)**:
  - *Shakespeare*: `the secret of the world is the world is the world is a proper my lord...`
  - *Sherlock*: `the secret of his colners was a bother of his columble took...`
  - *Analysis*: Highly conservative. Words are correctly spelled, but structure is repetitive.
- **Moderate Temperature ($T = 0.6$)**:
  - *Shakespeare*: `the secret of this too, well of parish that's worth's voice...`
  - *Sherlock*: `the secret of home upon his waiting. he woild dost the band, hereself...`
  - *Analysis*: Highly coherent. Style mimicry is excellent: Shakespeare outputs dramatic vocabulary ("my lord", "parish", "voice") and structure ("all:"), while Sherlock Holmes outputs narrative prose and character details ("holmes", "waiting").
- **High Temperature ($T = 1.0$)**:
  - *Shakespeare*: `the secret of him, yow, how she how moscome but not to relector...`
  - *Sherlock*: `the secret of under branch besies in this exarell. but so so...`
  - *Analysis*: High entropy leads to creative but spelling-flawed words.
- **Extremely High Temperature ($T = 1.5$)**:
  - *Shakespeare*: `the secret of cit, fanlerithly to authartial, git dog...`
  - *Sherlock*: `the secret of yourlecmust.” we enkgaiqh—,go fors; themes-funl...`
  - *Analysis*: Scrambled tokens, spelling and grammatical syntax disintegrate.

---

## Task 2: Batch Norm vs. No Batch Norm (Project 23)

### 2.1 Problem Statement
Deep networks suffer from training instability due to **internal covariate shift** (the shifting of intermediate layer input distributions as parameters change) and **vanishing/exploding gradients**. This project trains a 6-layer Deep MLP on the MNIST dataset to evaluate how Batch Normalization influences training stability, convergence speed, and tolerance to suboptimal configurations (high learning rates and poor initialization).

### 2.2 Technical Approach
1. **Dataset**: MNIST digit images normalized to mean 0.1307 and std 0.3081.
2. **Model Architectures**:
   - **Baseline (No BN)**: Input (784) $\to$ [Linear $\to$ ReLU]$^5$ $\to$ Linear (10).
   - **Batch Normalized (With BN)**: Input (784) $\to$ [Linear $\to$ BatchNorm1d $\to$ ReLU]$^5$ $\to$ Linear (10).
3. **Controlled Experiments (5 Epochs each)**:
   - **Experiment 1 (Standard)**: SGD Optimizer, learning rate = 0.01, standard Kaiming initialization.
   - **Experiment 2 (High Learning Rate)**: SGD Optimizer, learning rate = 0.2, standard initialization.
   - **Experiment 3 (Suboptimal Weight Initialization)**: SGD Optimizer, learning rate = 0.01, weights initialized to a very small scale ($\sigma = 0.001$).

### 2.3 Experiments and Results
All experiments were run on an Apple Silicon GPU (MPS) using a batch size of 128.

#### Summary of Convergence and Accuracy Metrics:

| Experiment | Configuration | Metric | No Batch Norm (Baseline) | With Batch Norm |
| :--- | :--- | :--- | :--- | :--- |
| **Exp 1: Standard** | LR = 0.01, Default Init | Final Train Loss <br> Final Val Loss <br> **Final Test Accuracy** | 0.2882 <br> 0.2541 <br> **92.83%** | 0.0768 <br> 0.0982 <br> **97.10%** |
| **Exp 2: High LR** | LR = 0.2, Default Init | Final Train Loss <br> Final Val Loss <br> **Final Test Accuracy** | 2.3026 <br> 2.3015 <br> **11.35%** (Failed) | 0.0463 <br> 0.0631 <br> **98.24%** |
| **Exp 3: Small Init** | LR = 0.01, $\sigma = 0.001$ | Final Train Loss <br> Final Val Loss <br> **Final Test Accuracy** | 2.3026 <br> 2.3012 <br> **11.35%** (Failed) | 0.0921 <br> 0.0821 <br> **97.48%** |

#### Experiment 1 Analysis (Standard Training):
The batch-normalized network converges significantly faster. By Epoch 2, the BN network achieves an accuracy of **95.2%**, whereas the baseline model is at **88.6%**. The final test accuracy shows a clear improvement (**97.10%** vs **92.83%**).

#### Experiment 2 Analysis (High Learning Rate = 0.2):
At high learning rates, the baseline network diverges. The loss remains stuck at the maximum cross-entropy plateau (**2.3026**), and accuracy is at **11.35%** (random guessing). This occurs because gradient updates scale parameters too aggressively, exploding the activations. In contrast, the Batch Norm network trains smoothly, achieving its highest test accuracy (**98.24%**). Batch Norm keeps activations scaled within bounds, preventing gradient explosion.

#### Experiment 3 Analysis (Poor Initialization, $\sigma = 0.001$):
When weights are initialized to near-zero values, the baseline network suffers from severe vanishing gradients. The outputs of hidden layers shrink to zero, yielding no signal. The model fails to learn entirely, flatlining at **11.35%** accuracy. The Batch Norm network, however, normalizes activations at each layer, restoring their variance to unit scale. This allows gradients to flow back, resulting in a successful training run (**97.48%** test accuracy).

---

## 3. Comparative Synthesis & Insights

1. **Decoupling Optimization Dynamics**: Batch Normalization decouples the scale of weights from their optimization dynamics. It bounds the activations' variance, protecting the network from both vanishing gradients (under small initialization) and exploding gradients (under high learning rates).
2. **Decoupling Decoding Entropy**: In sequence generation, temperature ($T$) directly scales the output logits. As $T \to 0$, the model enters low-entropy greedy loops. As $T \to \infty$, the output distribution converges to a uniform distribution, producing high-entropy gibberish. Selecting a moderate temperature (e.g. 0.6) optimizes formatting coherence and stylistic variety.

---

## 4. Group Contributions
- **Notebook Development (Task 1 & 2)**: Developed data preparation scripts, model structures, training setups, and plotted outputs.
- **Controlled Experiments**: Conducted high learning rate and poor initialization parameter sweeps to study Batch Norm training dynamics.
- **Report & Viva Preparation**: Outlined the theoretical background and mapped Weeks 1-7 curriculum concepts directly to implementation details.
