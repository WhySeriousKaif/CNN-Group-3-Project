# Slide Deck: Joint Presentation Outline

This document outlines the slide deck (max 15 slides) covering both tasks. Each slide contains key bullet points and dedicated **Speaker Notes** to help you deliver a smooth, well-paced presentation.

---

### Slide 1: Title Slide
* **Title**: Optimization Dynamics and Sequence Generation in Deep Learning
* **Subtitle**: Comparative Analysis of Batch Normalization & Character-Level LSTMs
* **Presenter Names**: [Your Group Member Names]
* **Speaker Notes**:
  > "Good morning, everyone. In this presentation, we will walk you through our joint projects: Task 1, where we trained a character-level LSTM on different corpuses to generate story continuations; and Task 2, where we ran controlled experiments to analyze how Batch Normalization stabilizes training in deep neural networks. Let's get started."

---

### Slide 2: Task 1: AI Story Continuation Overview
* **Objective**: Train a character-level recurrent neural network to generate continuations from prompts.
* **Core Questions Explored**:
  - Can a model learn spelling, grammar, and style from raw characters without pre-trained word tokens?
  - How does greedy decoding compare to temperature-based probabilistic sampling?
  - How does the style of the training corpus affect the generated text?
* **Speaker Notes**:
  > "For our first task, we wanted to build a text generation model. Instead of using word-level tokens, we train it at the character level. This forced the network to learn spelling, punctuation, and grammar from scratch, which is a great demonstration of representation learning."

---

### Slide 3: Sequence Modeling: LSTM Architecture
* **Why LSTM?** Vanilla RNNs suffer from vanishing and exploding gradients due to repeated matrix multiplications over time.
* **Gating Mechanism**:
  - **Forget Gate ($f_t$)**: Decides what history to discard.
  - **Input Gate ($i_t$)**: Decides what new information to store in cell state ($C_t$).
  - **Output Gate ($o_t$)**: Decides what hidden state ($h_t$) to output.
* **Our Network**:
  - `EmbeddingLayer` (Char index $\to$ 128-dim vector)
  - `Stacked LSTM` (2 layers, 256 hidden units, 0.2 Dropout)
  - `Linear Decoder` (256 $\to$ Vocabulary size logits)
* **Speaker Notes**:
  > "To model sequences, we chose a 2-layer LSTM. Unlike standard RNNs, LSTMs have a cell state and three gates. The cell state acts as an information highway, allowing gradients to flow back over time without vanishing. Our architecture embeds character indices into a 128-dimensional space before feeding them to the LSTM layers."

---

### Slide 4: Data Pipeline & Corpuses
* **Data Sources**:
  - **Shakespeare Corpus**: Archival vocabulary, poetic syntax, dramatic plays (e.g. `all:`, `lord`).
  - **Sherlock Holmes Corpus**: 19th-century detective prose, narrative syntax, descriptive sentences.
* **Preprocessing**:
  - Lowerecased all text to keep the vocabulary size small (37 characters for Shakespeare, 57 for Sherlock).
  - Created overlapping input-target sequences of length $T = 100$.
* **Speaker Notes**:
  > "We selected two highly contrasting corpuses to study style transfer: tinyshakespeare and Sherlock Holmes. By converting them to lowercase, we minimized vocabulary size to keep training fast. We trained our LSTMs on chunks of 100 characters, trying to predict the next character at every single step."

---

### Slide 5: Decoding and Sampling Techniques
* **Greedy Decoding ($T = 0$)**:
  - Always picks the character with the maximum probability.
  - **Issue**: Very prone to repetition and local loops (deterministic).
* **Temperature Sampling ($T > 0$)**:
  - Divides logits by temperature $T$ before running Softmax:
    $$P(c_i) = \frac{\exp(logits_i / T)}{\sum_j \exp(logits_j / T)}$$
  - **Low $T$ (0.2)**: High confidence, conservative, repetitive.
  - **Moderate $T$ (0.6)**: Balanced, creative, mostly grammatically correct.
  - **High $T$ (1.0+)**: Creative but chaotic, spelling errors occur.
* **Speaker Notes**:
  > "Once the model is trained, we generate text character-by-character. We compare greedy sampling, which is deterministic and gets stuck in repetitive loops, with temperature-based sampling. By scaling the logits before the softmax, temperature controls the randomness. At a low temperature, the output is safe but repetitive. At a high temperature, it's chaotic. At a moderate temperature, like 0.6, we get the best result."

---

### Slide 6: Task 1: Training Loss & Text Samples
* **Training Convergence**:
  - Shakespeare final loss: **0.9955** (8 epochs, 80 steps/epoch).
  - Sherlock Holmes final loss: **1.1377**.
* **Stylistic Output Comparison (Prompt: "the secret of ")**:
  - **Shakespeare ($T=0.6$)**: `the secret of this too, well of parish that's worth's voice...`
  - **Sherlock ($T=0.6$)**: `the secret of home upon his waiting. he woild dost the band, hereself...`
* **Speaker Notes**:
  > "Here are our training loss curves and generation outputs. Both models trained in under a minute, with cross-entropy loss dropping steadily. Look at the outputs at temperature 0.6: Shakespeare's model generates dramatic dialogue with words like 'parish' and 'voice', while Sherlock's model generates investigative narrative prose, using words like 'waiting' and 'band'."

---

### Slide 7: Task 2: Batch Norm vs. No Batch Norm
* **Objective**: Train and compare a deep feedforward network (6 layers) with and without Batch Normalization.
* **Key Challenges in Deep Nets**:
  - **Internal Covariate Shift**: Activation distributions drift during training, slowing down convergence.
  - **Vanishing/Exploding Gradients**: Signals vanish or blow up as they propagate through many layers.
* **Solution**: Batch Normalization scales layer activations to zero mean and unit variance.
* **Speaker Notes**:
  > "Now, we will move to Task 2, where we analyze Batch Normalization. In networks with six or more layers, training is difficult because intermediate activation distributions shift continuously, a problem called internal covariate shift. Batch Norm addresses this by normalizing the inputs to each activation function."

---

### Slide 8: Deep MLP Architecture and Setup
* **Dataset**: MNIST digit images (28x28 grayscale, 10 classes).
* **Model Configuration**:
  - **Input**: Flattened vector of size 784.
  - **Hidden Layers**: 5 hidden layers, 512 units each.
  - **Output Layer**: 10 units.
  - **Activation**: ReLU.
* **Comparative Variables**:
  - **Setup A (Baseline)**: Linear $\to$ ReLU.
  - **Setup B (Batch Norm)**: Linear $\to$ `BatchNorm1d` $\to$ ReLU.
* **Speaker Notes**:
  > "To test Batch Norm, we set up a 6-layer Deep MLP. Our baseline has just linear projections followed by ReLUs, while our Batch Norm model places a 1D Batch Normalization layer after each linear layer. We trained both on MNIST using standard SGD optimization."

---

### Slide 9: Experiment 1: Standard Training
* **Parameters**: Learning rate = 0.01, standard initialization, 5 epochs.
* **Observations**:
  - **With BN**: Converges much faster, reaching **97.10%** test accuracy.
  - **No BN**: Converges slowly, reaching **92.83%** test accuracy.
* **Takeaway**: Batch Norm acts as an optimization accelerator, helping the network achieve higher accuracy in fewer epochs.
* **Speaker Notes**:
  > "In our first experiment, we used a standard learning rate of 0.01. The results are clear: the model with Batch Normalization converges much faster, hitting 95.2% accuracy by epoch 2. The baseline model is slower to train, ending up at 92.83%, whereas the Batch Norm model reaches 97.10% accuracy."

---

### Slide 10: Experiment 2: Stress-Test with High Learning Rate
* **Parameters**: Learning rate = 0.2, standard initialization, 5 epochs.
* **Observations**:
  - **With BN**: Trains stably and converges to **98.24%** test accuracy (our highest score!).
  - **No BN**: Fails to train. Loss flatlines at **2.3026**, test accuracy stays at **11.35%** (random guessing).
* **Takeaway**: Batch Norm scale-invariance stabilizes gradient updates, permitting higher learning rates that accelerate training.
* **Speaker Notes**:
  > "Next, we stress-tested the networks with a high learning rate of 0.2. Without Batch Norm, the gradient updates are too aggressive, causing the weights to blow up. The baseline model fails completely, flatlining at 11% accuracy. However, the Batch Norm model handles this learning rate perfectly, achieving its highest test accuracy of 98.24%."

---

### Slide 11: Experiment 3: Stress-Test with Poor Initialization
* **Parameters**: Learning rate = 0.01, weights scaled to near-zero ($\sigma = 0.001$), 5 epochs.
* **Observations**:
  - **With BN**: Successfully trains and converges to **97.48%** test accuracy.
  - **No BN**: Fails completely. Loss remains at **2.3026**, accuracy is stuck at **11.35%**.
* **Takeaway**: Batch Norm rescales the activations at each layer, maintaining gradient magnitude and preventing vanishing gradients.
* **Speaker Notes**:
  > "Our third experiment used a poor initialization scale of 0.001. When weights are this small, activations shrink to zero as they pass through the layers. Without Batch Norm, the gradients vanish completely, and the model cannot learn. With Batch Norm, the activations are rescaled at each layer back to unit variance, allowing gradients to flow and enabling the model to converge to 97.48%."

---

### Slide 12: How Batch Normalization Stabilizes Gradients
* **Mathematical Intuition**:
  - Normalization scales the feedforward signals: $\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$.
  - The scale parameter $\gamma$ handles representation capacity, ensuring the layer is not restricted to standard normal distributions.
* **Gradient Backpropagation**:
  - The gradient with respect to input is computed through $\mu_B$ and $\sigma_B^2$.
  - It prevents gradients from scaling proportionally with the magnitude of weights, solving vanishing/exploding gradients.
* **Speaker Notes**:
  > "Mathematically, why does Batch Norm prevent these failure modes? By dividing by the standard deviation of the batch, the scale of the weights is decoupled from the scale of the activations. This guarantees that layer activations never shrink to zero or blow up to infinity, maintaining a stable gradient flow."

---

### Slide 13: Summary of Empirical Findings
* Let's look at the results side-by-side:

| Experiment                      | Metric        | No Batch Norm (Baseline) | With Batch Norm      |
| :------------------------------ | :------------ | :----------------------- | :------------------- |
| **Standard (LR=0.01)**          | Test Accuracy | 92.83%                   | **97.10%**           |
| **High LR (0.2)**               | Test Accuracy | 11.35% (Diverged)        | **98.24%** (Trained) |
| **Small Init ($\sigma=0.001$)** | Test Accuracy | 11.35% (Vanished)        | **97.48%** (Trained) |

* **Speaker Notes**:
  > "This table summarizes our empirical findings. We have demonstrated three distinct properties of Batch Norm: faster convergence, robustness to high learning rates, and independence from weight initialization scales. In all stress tests, the Batch Norm model trained successfully, while the baseline model failed."

---

### Slide 14: Connections to Deep Learning Theory (Weeks 1-7)
* **Universal Approximation**: Representation learning in LSTMs automatically discovers vocabulary and grammar without manual rules.
* **Initialization (Xavier/He)**: Kaiming initialization works well under normal conditions, but is highly sensitive. Batch Norm relaxes this requirement.
* **Optimization (SGD/Adam)**: Optimization depends on a smooth loss landscape. Batch Norm smoothens the loss landscape, preventing gradient explosion.
* **Speaker Notes**:
  > "To connect this to our curriculum: universal approximation explains how our character LSTM learns grammar from scratch. We've also seen the critical importance of weight initialization, and how optimization algorithms depend on a smooth loss landscape—which Batch Norm directly provides."

---

### Slide 15: Conclusion and Q&A
* **Conclusion**:
  1. Sequence modeling using LSTMs successfully captures structural and stylistic nuances of natural text.
  2. Batch Normalization is a critical architectural component for deep networks, providing optimization acceleration and stability.
* **Thank you! Questions?**
* **Speaker Notes**:
  > "In conclusion, we successfully implemented and analyzed both tasks. Our character-level LSTMs captured clear stylistic properties, and our Batch Norm experiments demonstrated how normalization stabilizes deep networks. Thank you for your time, and we are happy to take any questions."
