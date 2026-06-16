# Viva Preparation Guide: ML Project 21 & 23 (Simple Language Version)

This guide translates the theory behind both projects into simple, conversational English. Rehearse these answers so you can speak naturally and confidently in front of your professor ("Sir").

---

## 1. Core Theory Connections

### Q1: Why do we use Deep Learning instead of old-school Machine Learning? What are "hand-crafted features"?
* **Easy Explanation**: 
  > "In traditional machine learning, human experts had to manually design rules or formulas to extract patterns from data—like finding specific lines and edges to identify a shape (called 'hand-crafted features'). 
  > 
  > The problem is that these manual features take too much time, require domain experts, and break easily if the data changes even slightly (like lighting changes in an image). 
  > 
  > Deep learning solves this because the model automatically learns what features are important directly from the raw data without any human help."
* **Connection to our Project**:
  > "In **Project 21 (LSTM)**, we did not write any grammar rules or give the model an English dictionary. It started with zero knowledge and learned spelling, word boundaries, and Shakespeare's/Sherlock's writing styles entirely on its own from raw letters."

### Q2: What is the "Universal Approximation Theorem" in simple terms?
* **Easy Explanation**: 
  > "This theorem is a mathematical promise. It says that a standard neural network with just one hidden layer and a non-linear activation function (like ReLU) is powerful enough to learn and copy *any* complex pattern or relationship in data, as long as we give it enough nodes.
  > 
  > Basically, it promises us that our network *can* solve the problem."
* **Connection to our Project**: 
  > "This explains why our 6-layer network (**Project 23**) is capable of classifying handwritten digits, and why our LSTM (**Project 21**) can learn to write text. 
  > 
  > However, the theorem only promises that a solution *exists*—it doesn't guarantee that the model will actually find it. To make it find the solution, we need good optimization, weight initialization, and normalization."

### Q3: Explain Sigmoid, Tanh, and ReLU. Why do we prefer ReLU?
* **Easy Explanation**: 
  * **Sigmoid**: Squishes any number between 0 and 1. The problem is that if the input numbers get too large or too small, the output becomes flat (close to 0 or 1). The gradient becomes zero, and the model stops learning (called the vanishing gradient problem).
  * **Tanh**: Squishes numbers between -1 and 1. It centers the data around zero, which helps training speed, but it still flatlines on large inputs just like Sigmoid.
  * **ReLU (Rectified Linear Unit)**: The simplest activation function. If a number is negative, it turns it to 0. If it is positive, it keeps it exactly the same. 
  * **Why we prefer ReLU**: Because for any positive number, the slope (gradient) is always exactly 1. It never flatlines, so the training signals flow perfectly back through the network, making training super fast.
* **Connection to our Project**: 
  > "We used **ReLU** in our 6-layer digit classifier to ensure the learning signals could travel all the way back through the deep layers without fading out."

### Q4: What is the difference between Xavier and He (Kaiming) weight initialization?
* **Easy Explanation**: 
  > "When we start training, we cannot set all neural weights to zero (otherwise all neurons learn the exact same thing) or to huge numbers (otherwise numbers explode). We must size them just right.
  > 
  > **Xavier initialization** is sized perfectly for networks using Sigmoid or Tanh activations.
  > 
  > **He (Kaiming) initialization** is sized perfectly for networks using ReLU. It accounts for the fact that ReLU turns off half of our inputs (all negative numbers)."
* **Connection to our Project**: 
  > "In Project 23, our default code uses Kaiming initialization, which works great. In Experiment 3, we deliberately broke this by initializing our weights to near-zero (0.001) to prove that a bad initialization will completely break training unless you use Batch Normalization."

---

## 2. Project 21: AI Story Continuation (LSTM)

### Q5: What is an LSTM, and how does it solve Vanilla RNN limitations?
* **Easy Explanation**: 
  > "A basic RNN has short-term memory. When unrolling over a long sentence, the model repeatedly multiplies gradients by its weight matrix. This math makes the training signals shrink to zero (vanish) or blow up (explode), meaning it forgets the beginning of the sentence.
  > 
  > **LSTM (Long Short-Term Memory)** solves this by adding a **Cell State**. You can think of the Cell State as a direct memory conveyor belt running through the network. Data flows down this belt with only basic additions and subtractions, so the signal doesn't fade.
  > 
  > It regulates this conveyor belt using three gates:
  > 1. **Forget Gate**: Decides what old memory to throw away.
  > 2. **Input Gate**: Decides what new information to add to the conveyor belt.
  > 3. **Output Gate**: Decides what parts of our memory to use for the next predicted letter."

### Q6: Explain Greedy vs. Temperature Sampling. Why does Greedy repeat phrases?
* **Easy Explanation**: 
  * **Greedy Sampling**: The AI plays it safe and always picks the single letter with the absolute highest score. It repeats itself because it gets stuck in logical loops. For example, if it writes *'the world is the '*, the most probable next word is *'world'*, leading back to *'is the'*, creating an infinite loop: *'the world is the world is the world...'*.
  * **Temperature**: A knob that adjusts how 'creative' or random the AI's guesses are. 
    * **Low Temperature (T = 0.2)**: AI plays it safe, behaves like greedy, and loops.
    * **High Temperature (T = 1.5)**: AI chooses random letters, causing spelling mistakes and generating complete gibberish.
    * **Balanced Temperature (T = 0.6)**: The sweet spot. Spelling and grammar are correct, but it varies its choice of letters so it doesn't loop.

---

## 3. Project 23: Batch Norm vs. No Batch Norm

### Q7: What is "Internal Covariate Shift"?
* **Easy Explanation**: 
  > "As a deep network trains, the weights of the early layers change. This means the input signals entering the later layers are constantly shifting and changing distribution. 
  > 
  > Later layers are basically trying to learn on a moving target, which makes training very slow and requires us to use very low learning rates."

### Q8: How does Batch Normalization work mathematically in simple steps?
* **Easy Explanation**: 
  > "Batch Norm stabilizes the signals at each layer using four steps:
  > 1. **Find the average (Mean)** of the current batch of numbers.
  > 2. **Find the spread (Variance)** of the numbers.
  > 3. **Normalize**: Subtract the average and divide by the spread. Now the numbers are centered around zero with a standard range of 1.
  > 4. **Scale & Shift**: Multiply by a learnable scale ($\gamma$) and add a learnable shift ($\beta$). This lets the network undo the normalization if it decides that unnormalized numbers were actually better for learning."

### Q9: Why did the baseline network fail in Experiment 2 (High LR = 0.2)?
* **Easy Explanation**: 
  > "With a huge step size of 0.2, the updates to the weights are too aggressive. The values inside the 6 layers multiply exponentially at each step until they blow up into infinity (exploding gradients). The model breaks and guesses randomly, flatlining at a loss of 2.3026.
  > 
  > **Why Batch Norm succeeded**: Batch Norm automatically divides the numbers by their standard deviation at each layer. Even if the weights try to blow up the numbers, Batch Norm scales them right back down to a stable range of 1, keeping training stable."

### Q10: Why did the baseline network fail in Experiment 3 (Tiny Initialization = 0.001)?
* **Easy Explanation**: 
  > "Since we started with tiny weights of 0.001, the signals shrank exponentially as they went through the 6 layers. By the output layer, the signals were basically zero. The network couldn't pass information forward, gradients became zero, and the model couldn't learn.
  > 
  > **Why Batch Norm succeeded**: Even when the inputs are tiny, Batch Norm calculates the standard deviation of those tiny numbers and divides by it. This automatically scales the tiny numbers back up to a normal size, rescuing the signal and letting the model train successfully."

---

## 4. Simulated Viva Scenarios: High-Score Q&A

### Scenario A: The evaluator spots the loss flatlining at 2.3026.
* **Evaluator**: *"I see your baseline MLP has a loss of 2.3026 for 5 epochs. Why this specific number?"*
* **Your Answer**: 
  > "Sir, 2.3026 is the negative natural log of $10\%$ ($-\ln(0.1) \approx 2.3026$). 
  > 
  > Since there are 10 digits to guess from in the MNIST dataset, a model that hasn't learned anything guesses randomly with a $10\%$ chance for each digit. This mathematically gives a loss of exactly 2.3026. 
  > 
  > This flatline shows our baseline network completely failed to learn due to vanishing or exploding gradients."

### Scenario B: The evaluator asks about placing Batch Norm before or after activation.
* **Evaluator**: *"In your code, you placed Batch Norm before the ReLU activation. What would happen if you placed it after?"*
* **Your Answer**: 
  > "Sir, we placed it before ReLU (Linear $\to$ Batch Norm $\to$ ReLU), which matches the original paper's recommendation. 
  > 
  > If we placed it after ReLU, all the numbers would be strictly positive (since ReLU turns negative numbers to zero). Normalizing positive-only numbers shifts half of them below zero, which the next ReLU would immediately destroy. 
  > 
  > Placing it before ReLU keeps the distribution balanced and symmetric."

### Scenario C: The evaluator asks about Batch Norm during testing (Inference).
* **Evaluator**: *"During testing, your batch size could be 1. How does Batch Norm calculate mean and variance then?"*
* **Your Answer**: 
  > "Sir, during testing (when we call `model.eval()`), Batch Norm stops calculating batch statistics. 
  > 
  > Instead, it uses the running average of the mean and variance that it calculated and saved during the training phase. 
  > 
  > This ensures that our predictions are stable, consistent, and do not depend on the batch size during testing."
