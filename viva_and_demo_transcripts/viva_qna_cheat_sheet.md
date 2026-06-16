# Viva Q&A Cheat Sheet: Speak-to-Score Answers (Easy Language)

Use this guide to study the 10 most common questions. The answers are written in simple, plain English so you can explain them easily in front of your professor ("Sir").

---

### Q1: "Why does the loss stay at exactly 2.3026 when the model fails to learn?"
* **Easy Explanation**: 
  > "Sir, since the MNIST dataset has 10 different digit classes (0 to 9), a model that is completely failing to learn will just guess randomly. The chance of guessing the right digit is 1 out of 10, which is a probability of 0.1 (or 10%). 
  > 
  > When we calculate the Cross-Entropy loss for a 10% guess, the mathematical formula is $-\ln(0.1)$, which is exactly 2.3026. So, seeing a loss of 2.3026 just means the model is guessing completely randomly and has not learned anything."

---

### Q2: "How does Batch Normalization solve the vanishing gradient issue under poor initialization (tiny weights = 0.001)?"
* **Easy Explanation**: 
  > "When weights are initialized to a tiny number like 0.001, the signals get smaller and smaller as they pass through the 6 layers, eventually shrinking to almost zero at the output. Because the output signal is near zero, the gradients also become zero, and the model cannot learn. 
  > 
  > Batch Norm solves this by taking the signals at each layer, calculating their size (variance), and dividing by it to scale them back to a standard size. This keeps the signal alive and lets the gradients flow back during backpropagation."

---

### Q3: "What does the temperature ($T$) parameter do when generating text?"
* **Easy Explanation**: 
  > "Temperature controls how creative or random the AI is when writing. Before the probabilities are calculated, we divide the scores (logits) by the temperature $T$.
  > 
  > If temperature is very low (like 0.2 or 0), the AI plays it safe and always picks the highest score. This causes it to get stuck in loops and repeat the same words over and over.
  > 
  > If temperature is high (like 1.5), it flattens the scores, making them almost equal. This makes the AI pick letters randomly, which leads to spelling errors and gibberish.
  > 
  > A moderate temperature of 0.6 is the sweet spot because it makes the output creative but readable."

---

### Q4: "Why use Cross-Entropy Loss for character prediction instead of Mean Squared Error (MSE)?"
* **Easy Explanation**: 
  > "Sir, predicting the next character is a classification problem where each letter in our alphabet represents a separate class (like 37 classes for Shakespeare). Cross-Entropy is the standard loss function for classification because it measures how close our predicted class probabilities are to the actual target letter. 
  > 
  > MSE is designed for predicting continuous numbers (like house prices) and is not correct for guessing discrete categories like letters."

---

### Q5: "What is the difference in how Batch Norm behaves during training vs. testing (evaluation)?"
* **Easy Explanation**: 
  > "During training, Batch Norm calculates the average (mean) and size (variance) of the current batch of images to normalize them. 
  > 
  > During testing, we might only predict on one image at a time, so we cannot calculate batch averages. Instead, Batch Norm uses the running averages that it calculated and saved during the training phase."

---

### Q6: "Why did you use an LSTM instead of a standard Recurrent Neural Network (RNN)?"
* **Easy Explanation**: 
  > "Standard RNNs struggle with memory because they multiply gradients repeatedly over time, which causes the signal to shrink to zero (vanish) or blow up to infinity (explode) over long sentences. 
  > 
  > LSTMs solve this by introducing a 'Cell State' (which acts as a direct memory conveyor belt) and 'Gates' that decide what to remember or forget. The gradients can flow directly back through this channel without fading away."

---

### Q7: "What does the embedding layer do in the character-level model?"
* **Easy Explanation**: 
  > "It converts simple letter numbers (like 'a' = 1, 'b' = 2) into a list of 128 numbers (a dense vector). This allows the model to learn relationships between letters. For example, it can learn that the vector for 'q' is close to the vector for 'u' because they often appear together in English words."

---

### Q8: "How does Batch Normalization act as a regularizer?"
* **Easy Explanation**: 
  > "Because Batch Norm calculates the average and variance over a random batch of images, each image is normalized slightly differently depending on which other images are in the same batch. This introduces a small amount of random noise during training. This noise acts as a regularizer, helping to prevent the model from overfitting (memorizing the data too perfectly)."

---

### Q9: "Why does the baseline model fail under a high learning rate (0.2)?"
* **Easy Explanation**: 
  > "At a high learning rate of 0.2, the step size is too large. The weight updates are too aggressive, which causes the numbers inside the deep layers to grow exponentially until they become too large for the computer to handle (exploding gradients). This makes the model parameters blow up and fail to learn."

---

### Q10: "Explain Backpropagation Through Time (BPTT)."
* **Easy Explanation**: 
  > "BPTT is how we train recurrent networks like LSTMs. We unroll the network over a sentence of 100 characters, calculate the loss for the predicted letters, and then propagate the errors backward step-by-step from the last character to the first character to update the weights."
