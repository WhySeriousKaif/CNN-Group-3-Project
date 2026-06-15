# Viva Q&A Cheat Sheet: Speak-to-Score Answers

Keep this cheat sheet open or memorize it before the viva. These answers are designed to demonstrate a deep, combined understanding of theory and practical code.

---

### Q1: "Why does the loss flatline at exactly 2.3026 when the model fails?"
* **What they are testing**: If you understand Cross-Entropy loss and the dataset.
* **Exact Answer to Speak**:
  > "Sir, 2.3026 is the negative log-likelihood of random guessing on a 10-class dataset. Since MNIST has 10 classes, a model that cannot learn will predict a probability of 0.1 for each class. The formula for Cross-Entropy is $-\ln(P_{target})$. For a uniform prediction, this is $-\ln(0.1)$, which is exactly $2.30258$. This proves the baseline model was stuck at random guessing and did not learn at all."

---

### Q2: "How does Batch Normalization solve the vanishing gradient issue under poor initialization ($\sigma=0.001$)?"
* **What they are testing**: Your mathematical intuition of normalization.
* **Exact Answer to Speak**:
  > "When weights are initialized to 0.001, the variance of layer activations shrinks exponentially as they pass through the 6 layers, ending up near zero. Batch Norm calculates the mean and standard deviation of these activations over the mini-batch, and normalizes them by dividing by the standard deviation. This rescales the variance back to 1.0 at every layer, keeping the signal alive and allowing gradients to flow back during backpropagation."

---

### Q3: "What does the temperature ($T$) parameter mathematically do in the Softmax layer?"
* **What they are testing**: If you understand decoding probability math.
* **Exact Answer to Speak**:
  > "The temperature parameter divides the logits before they enter the softmax: $P(x_i) = \frac{\exp(logits_i / T)}{\sum \exp(logits_j / T)}$. 
  > 
  > When $T$ is very low, it accentuates differences, making the highest-probability character dominate, which makes the model conservative and repetitive. 
  > 
  > When $T$ is high, it flattens the differences, making the output distribution closer to a uniform distribution. This leads to high entropy and creative but scrambled, misspelled words."

---

### Q4: "Why use Cross-Entropy Loss for Task 1 instead of Mean Squared Error (MSE)?"
* **What they are testing**: Selection of loss functions for classification vs. regression.
* **Exact Answer to Speak**:
  > "We treat character prediction as a multi-class classification problem where the vocabulary (e.g., 37 characters for Shakespeare) represents our classes. Cross-Entropy measures the distance between the predicted probability distribution and the true one-hot target index. MSE is designed for regression with continuous values and would penalize character predictions based on arbitrary index distances, which is mathematically incorrect."

---

### Q5: "What is the difference in how Batch Norm behaves during training vs. evaluation?"
* **What they are testing**: Model state management (`model.train()` vs `model.eval()`).
* **Exact Answer to Speak**:
  > "During training, Batch Norm uses the statistics (mean and variance) of the current mini-batch to normalize the data. 
  > 
  > During evaluation, we cannot rely on batch statistics because we might predict on a single sample. Instead, Batch Norm uses running averages of the mean and variance that were calculated and tracked during training. In PyTorch, calling `model.eval()` automatically switches Batch Norm to use these running statistics."

---

### Q6: "Why did you use an LSTM instead of a standard Recurrent Neural Network (RNN)?"
* **What they are testing**: Core understanding of sequence architectures.
* **Exact Answer to Speak**:
  > "Vanilla RNNs multiply gradients by the recurrent weight matrix at every time step during backpropagation. Over a 100-character sequence, this leads to vanishing or exploding gradients. LSTMs introduce a cell state ($C_t$) that updates additively, which acts as a linear conveyor belt. Gradients flow back through this additive path without being repeatedly multiplied by weights, allowing the model to learn long-term dependencies."

---

### Q7: "What does the embedding layer do in the character-level model?"
* **What they are testing**: Representational lookup tables.
* **Exact Answer to Speak**:
  > "It maps sparse, one-hot encoded character indices into dense, continuous vector spaces of a lower dimension (128 in our case). The linear layers and LSTMs can then learn semantic relationships between characters (like which letters often appear together) based on vector proximity."

---

### Q8: "How does Batch Normalization act as a regularizer?"
* **What they are testing**: Regularization side-effects.
* **Exact Answer to Speak**:
  > "Because Batch Norm calculates mean and variance over a mini-batch, the normalization of any single training sample depends on the other random samples present in that batch. This introduces a small amount of noise into the activations. This noise acts as a regularizer, similar to Dropout, reducing overfitting."

---

### Q9: "Why does the baseline model fail under a high learning rate ($0.2$)?"
* **What they are testing**: Optimization stability.
* **Exact Answer to Speak**:
  > "At a high learning rate, parameter updates are too large, which exponentially increases activation values in deep layers. This leads to exploding gradients, where the weight updates become so massive they overflow standard floating-point representation, causing the model parameters to diverge and rendering it unable to learn."

---

### Q10: "Explain Backpropagation Through Time (BPTT)."
* **What they are testing**: RNN training dynamics.
* **Exact Answer to Speak**:
  > "Sir, BPTT is the standard backpropagation algorithm applied to recurrent networks. We unroll the recurrent network over a sequence length (100 timesteps in our project), compute the loss at each step, and accumulate gradients by propagating the error backwards through the temporal connections from the final step to the first step."
