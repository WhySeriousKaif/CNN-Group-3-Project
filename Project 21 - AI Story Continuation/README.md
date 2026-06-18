# Project 21: AI Story Continuation using Character-Level LSTM

This directory contains the implementation, datasets, and generation outputs for **Project 21: AI Story Continuation**. The project trains a character-level Recurrent Neural Network (LSTM) to learn the spelling, syntax, and style of two distinct historical authors from scratch, demonstrating representation learning.

---

## 📂 Directory Structure

```
Project 21 - AI Story Continuation/
├── data/                       # Text corpus storage
│   ├── shakespeare.txt         # William Shakespeare dramatic works
│   └── sherlock.txt            # Arthur Conan Doyle Sherlock Holmes detective stories
├── plots/                      # Generated visualization of training loss curves
│   └── loss_curves.png         # Cross-Entropy loss over 8 epochs
├── A_G03_Task1.ipynb           # Main Jupyter Notebook containing code, training, and evaluations
└── README.md                   # Project documentation (This file)
```

---

## 🧠 Model Architecture (`CharLSTM`)

The model processes text at the **character level**, using a vocabulary of approximately 40 unique characters (letters, numbers, space, and basic punctuation):

1. **Embedding Layer (`nn.Embedding`)**: Projects sparse, integer character indices into a dense, continuous vector space:
   $$\mathbb{R}^{B \times T} \to \mathbb{R}^{B \times T \times 128}$$
2. **LSTM Layer (`nn.LSTM`)**: A 2-layer LSTM with a hidden state size of `256` and dropout of `0.2`. It maintains sequence history across long contexts via a dedicated memory cell state ($C_t$) regulated by forget, input, and output gates.
3. **Linear Decoder (`nn.Linear`)**: A fully connected classification layer projecting the hidden state back into vocabulary log-probabilities (logits) for the next character prediction:
   $$\mathbb{R}^{B \times T \times 256} \to \mathbb{R}^{B \times T \times V}$$

---

## 🔍 Behind-the-Scenes: Step-by-Step Walkthrough with a Concrete Example

To understand the PyTorch code, let's walk through exactly what happens when you feed the single character **`'c'`** into the model to predict the next letter.

### Setup
* **Vocabulary Size (`vocab_size`)**: Let's say we have `40` unique characters.
* **Input**: The character `'c'` corresponds to index `3` in `dataset.char_to_idx`.
* **Tensor Form**: PyTorch represents this input as `x = torch.tensor([[3]])` with shape `(1, 1)` representing `[Batch Size, Sequence Length]`.

---

### Step 1: Embedding Lookup (`self.embedding`)
```python
embed = self.embedding(x)
```
* **What it does**: The embedding layer contains a weight lookup matrix of size `(40, 128)`.
* **Behind the scenes**: PyTorch retrieves the 4th row (index `3`) of this matrix. This row is a dense vector of 128 numbers (e.g., `[0.12, -0.45, 0.89, ..., -0.01]`) representing the character `'c'`.
* **Result**: The output tensor `embed` has shape `(1, 1, 128)` representing `[Batch Size, Sequence Length, Embedding Size]`.

---

### Step 2: LSTM Gate Processing (`self.lstm`)
```python
out, state = self.lstm(embed, state)
```
Behind the scenes, the 128-dimensional embedding vector and the previous states (hidden state $h_{t-1}$ and cell state $C_{t-1}$, both size `256`) are concatenated into a combined vector of size `384` ($256 + 128$) and fed into the 4 LSTM gates:

1. **Forget Gate ($f_t$)**:
   * **Formula**: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$
   * **Action**: Multiplies the `384`-size combined vector by a `(256, 384)` weight matrix to produce a `256`-size vector of values between $0$ and $1$. It decides what past memory to forget.
2. **Input Gate ($i_t$) & Candidate Cell State ($\tilde{C}_t$)**:
   * **Formulas**: $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$ and $\tilde{C}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$
   * **Action**: Both produce vectors of size `256`. They determine what new information to add to the memory.
3. **Cell State Update ($C_t$)**:
   * **Formula**: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$
   * **Action**: Performs element-wise multiplication ($\odot$) to update the cell state (long-term memory conveyor belt) to a new vector of size `256`.
4. **Output Gate ($o_t$) & Hidden State ($h_t$)**:
   * **Formulas**: $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$ and $h_t = o_t \odot \tanh(C_t)$
   * **Action**: Computes the final hidden output state $h_t$ of size `256`.
* **Result**: `out` has shape `(1, 1, 256)` and `state` holds the updated hidden/cell states for the next timestep.

---

### Step 3: Fully Connected Decoder (`self.fc`)
```python
logits = self.fc(out)
```
* **What it does**: The linear layer `self.fc` contains a projection weight matrix of shape `(256, 40)`.
* **Behind the scenes**: It multiplies the 256-dimensional hidden output vector by this projection matrix.
* **Result**: It outputs a logit vector of shape `(1, 1, 40)` containing raw, unnormalized prediction scores for each of the 40 characters in our vocabulary.

---

### Step 4: Temperature scaling and Sampling
We take the final character logits of shape `(40,)` to generate the next character:

1. **Temperature Scaling**: We divide the logits by our temperature parameter (e.g. `0.6`):
   $$\text{scaled\_logits} = \frac{\text{logits}}{0.6}$$
2. **Probability Calculation**: We run Softmax to convert these scaled logits into probabilities:
   $$\text{probs} = \text{softmax}(\text{scaled\_logits})$$
3. **Sampling**: We call `torch.multinomial(probs, 1)` to randomly pick a character according to its probability. If it returns index `1` (which corresponds to `'a'`), the character `'a'` is appended to our text, making it `"ca"`.
4. **Recurrence**: For the next character prediction, index `1` (`'a'`) and the updated hidden and cell states are fed back into the model.

---

## 🔬 Sampling Techniques Compared

Generating continuation text from a prompt (e.g., `"the secret of "`) involves predicting characters one-by-one autoregressively. This project compares two main decoding strategies:

### 1. Greedy Decoding ($T = 0.0$)
* Always selects the character index with the absolute highest probability:
  $$x_{t+1} = \arg\max_c P(c)$$
* **Result**: Highly repetitive, loops into infinite grammatical dead-ends (e.g., `"the world is the world is the world..."`).

### 2. Temperature-based Sampling ($T > 0.0$)
* Scales the raw model logits ($y$) by a temperature parameter ($T$) before applying Softmax to compute probability distribution:
  $$P(c_i) = \frac{\exp(y_i / T)}{\sum_j \exp(y_j / T)}$$
* **Low Temperature ($T = 0.2$)**: Conservative, high spelling accuracy, but low variety.
* **Balanced Temperature ($T = 0.6$)**: **The Sweet Spot**. Captures vocabulary, grammar, and punctuation accurately while maintaining creative stylistic variety.
* **High Temperature ($T = 1.5$)**: High randomness. Results in word spelling breakdowns and chaotic gibberish.

---

## 📊 Training Specifications

* **Optimizer**: Adam with learning rate `0.002`.
* **Loss Function**: Multi-class Cross-Entropy computed over all timesteps.
* **Sequence Length**: 100 characters per training sequence.
* **Batch Size**: 128 sequences.
* **Clipping**: Gradient norm clipped at `5.0` to prevent exploding gradients.
* **Execution Hardware**: Apple Silicon GPU (`mps`) / NVIDIA CUDA / CPU.

---

## 🚀 How to Run the Notebook

1. Ensure the project prerequisites are installed:
   ```bash
   pip install torch torchvision numpy matplotlib notebook
   ```
2. Launch the Jupyter Notebook interface from the root directory:
   ```bash
   jupyter notebook
   ```
3. Open and run all cells in `A_G03_Task1.ipynb`. The corpus datasets will automatically download to the `data/` folder, train for 8 epochs, plot loss curves, and output comparative text continuations.
