# Viva Preparation Guide: ML Project 21 & 23

This guide prepares you for the **Individual Viva (30% / 11 Marks)**. To score in the **9–11 mark range**, you must explain your project decisions confidently, handle follow-ups, and connect theory to practice.

---

## 1. Core Theory Connections (Weeks 1–7)

### Q1: Why Deep Learning? What are the limitations of hand-crafted features?
* **Core Answer**: Traditional machine learning relied on expert-designed, hand-crafted features (like SIFT in computer vision or TF-IDF/n-grams in NLP). The limitations are:
  1. They are highly domain-specific and do not generalize.
  2. They are static and cannot adapt to complex, high-dimensional patterns in data.
* **Connection to Project**: In **Project 21 (LSTM)**, we did not write any grammatical rules or define English vocabularies. The model learned representations of spelling, word boundaries, and style directly from raw character indices (Representation Learning).

### Q2: What is the Universal Approximation Theorem?
* **Core Answer**: A feedforward neural network with a single hidden layer and a non-linear activation function can approximate any continuous function on compact subsets of $\mathbb{R}^n$ to any arbitrary precision, provided it has sufficient hidden units.
* **Connection to Project**: This explains why our 6-layer Deep MLP (**Project 23**) can classify hand-written digits (MNIST) and why the LSTM can model English syntax. However, the theorem only guarantees *existence*, not *learnability* (which depends on initialization, optimization, and normalization).

### Q3: Explain Sigmoid, Tanh, and ReLU. Why do we prefer ReLU?
* **Core Answer**:
  - **Sigmoid**: $\sigma(x) = \frac{1}{1 + e^{-x}}$. Outputs in $(0, 1)$. Gradients saturate at 0 and 1, causing vanishing gradients.
  - **Tanh**: $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$. Outputs in $(-1, 1)$ (zero-centered, which aids optimization). Gradients still saturate.
  - **ReLU**: $f(x) = \max(0, x)$. Gradients are $1$ for $x > 0$. It does not saturate in the positive region, which mitigates vanishing gradients and accelerates SGD convergence.
* **Connection to Project**: We used **ReLU** in our 6-layer MLP hidden layers to maintain gradient flow.

### Q4: Contrast Xavier and He (Kaiming) initialization.
* **Core Answer**:
  - **Xavier (Glorot) Initialization**: Sets weight variance to $\frac{2}{n_{in} + n_{out}}$. Designed for symmetric activations (Sigmoid, Tanh) to keep activation variance constant across layers.
  - **He (Kaiming) Initialization**: Sets weight variance to $\frac{2}{n_{in}}$. Designed for asymmetric activations (ReLU) to account for the fact that ReLU outputs zero for half its inputs.
* **Connection to Project**: In Project 23, Experiment 1 uses default Kaiming initialization, which allows both models to train under standard conditions. Experiment 3 stress-tests this by scaling weights to near-zero ($\sigma=0.001$), forcing the baseline network to fail.

---

## 2. Task 1: AI Story Continuation (Project 21)

### Q5: What is an LSTM and how does it solve Vanilla RNN limitations?
* **Core Answer**: Vanilla RNNs backpropagate gradients through time by repeatedly multiplying by the weight matrix $W_{hh}$. If eigenvalues of $W_{hh}$ are $<1$, gradients vanish; if $>1$, gradients explode.
* **LSTM Gates**: An LSTM introduces a **Cell State ($C_t$)** (linear information highway) regulated by three gates:
  1. **Forget Gate ($f_t = \sigma(W_f[h_{t-1}, x_t] + b_f)$)**: Controls how much of the cell state is forgotten.
  2. **Input Gate ($i_t = \sigma(W_i[h_{t-1}, x_t] + b_i)$)**: Decides which new values to write to the cell state.
  3. **Output Gate ($o_t = \sigma(W_o[h_{t-1}, x_t] + b_o)$)**: Controls which parts of the cell state are exposed in the hidden state ($h_t$).
* **gradient flow**: The gradient backpropagates through the cell state additive update ($C_t = f_t C_{t-1} + i_t \tilde{C}_t$) instead of multiplicative weight multiplication, preventing vanishing gradients.

### Q6: Explain Greedy vs. Temperature Sampling. Why does Greedy repeat phrases?
* **Core Answer**:
  - **Greedy Sampling**: $x_{t+1} = \arg\max_c P(c)$. Always selects the most probable character. It repeats phrases because it gets stuck in deterministic, local loops (e.g., predicting "the" leads to "world", which leads back to predicting "the").
  - **Temperature Sampling**: Scales logits by temperature $T$: $y'_i = y_i / T$, then runs Softmax.
* **Follow-up: How does Temperature scale entropy?**
  - **$T \to 0$**: The probability of the argmax character approaches 1.0 (approximates greedy).
  - **$T = 1.0$**: Sampling follows the model's output probabilities directly.
  - **$T \to \infty$**: All logits become close to zero, yielding a uniform distribution (producing random characters).
  - **$T = 0.6$**: Smoothens the distribution slightly, preserving spelling and grammar while allowing stylistic variety.

---

## 3. Task 2: Batch Norm vs. No Batch Norm (Project 23)

### Q7: What is Internal Covariate Shift?
* **Core Answer**: As training progresses, the parameters of early layers change, which alters the distribution of inputs to later layers. Later layers must continuously adapt to these shifting distributions, slowing down training and requiring low learning rates.

### Q8: How does Batch Normalization work mathematically?
* **Core Answer**: Given a batch $B = \{x_1, \dots, x_m\}$:
  1. Mean: $\mu_B = \frac{1}{m} \sum_{i=1}^m x_i$
  2. Variance: $\sigma_B^2 = \frac{1}{m} \sum_{i=1}^m (x_i - \mu_B)^2$
  3. Normalize: $\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$ (stabilizes input distribution to mean 0, variance 1)
  4. Scale & Shift: $y_i = \gamma \hat{x}_i + \beta$ (restores representation capacity, allowing the model to represent identity mappings if needed).

### Q9: Why did the baseline fail in Experiment 2 (High LR = 0.2)?
* **Core Answer**: With a high learning rate, parameter updates are too large, causing layer activations to blow up. In a 6-layer network, this exploding signal propagates exponentially. The gradients explode, weights diverge to infinity, and loss flatlines at 2.3026 (random guess cross-entropy).
* **Why Batch Norm succeeded**: Batch Norm scales activations at each layer. Even if weights are scaled up, normalization divides by the standard deviation, neutralizing the scale change. This keeps activations bounded and training stable.

### Q10: Why did the baseline fail in Experiment 3 (Small Init = 0.001)?
* **Core Answer**: Because we initialized weights to near-zero ($\sigma=0.001$). As signal propagates forward through 6 layers, activations shrink by $0.001^6 \approx 10^{-18}$, meaning the input to the output layer is essentially zero. Consequently, gradients backpropagating through the network shrink to zero, and the model cannot learn.
* **Why Batch Norm succeeded**: Even if layer outputs shrink to near-zero, Batch Norm recalculates the batch mean and standard deviation, dividing the outputs by their small standard deviation. This rescales activations back to unit variance, restoring the signal and allowing gradients to propagate.

---

## 4. Simulated Viva Scenario: High-Score Q&A

### Scenario A: Evaluator spots the loss flatlining at 2.3026.
* **Evaluator**: "I see your baseline MLP has a loss of 2.3026 for 5 epochs. Why this specific number?"
* **Your Answer**: "2.3026 is the negative log-likelihood of random guessing on a 10-class dataset: $-\ln(0.1) \approx 2.30258$. This indicates the network is not learning and is predicting class probabilities uniformly. This occurred because gradients either exploded (Experiment 2) or vanished (Experiment 3) due to the depth of the 6-layer network."

### Scenario B: Evaluator asks about placing Batch Norm before or after activation.
* **Evaluator**: "In your code, you placed Batch Norm before the ReLU. What would happen if you placed it after?"
* **Your Answer**: "We placed it before ReLU (Linear $\to$ BN $\to$ ReLU), which matches the original paper's recommendation. If placed after ReLU, the input to Batch Norm is strictly non-negative, meaning the distribution is asymmetric. Normalizing it shifts some values below zero, which are then clipped if followed by another ReLU. Research shows both can work, but placing it before activation is standard because it provides a symmetric, zero-centered distribution to the non-linearity."

### Scenario C: Evaluator asks about Batch Norm during testing (Inference).
* **Evaluator**: "During testing, your batch size could be 1. How does Batch Norm calculate mean and variance then?"
* **Your Answer**: "During evaluation (when we call `model.eval()`), Batch Norm does not calculate batch statistics. Instead, it uses running averages of the mean and variance computed during the training phase using a momentum factor (typically 0.1). This ensures that predictions are deterministic and independent of batch size."
