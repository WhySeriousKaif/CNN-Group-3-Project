# Spoken Transcript: Project Demonstration Guide

This script walks you through exactly what to say, what to click on, and what to point at on your screen when demonstrating the projects to your professor ("Sir").

---

## Part 1: Introduction (Approx. 30 Seconds)

**What to do**: Open the Jupyter main page showing both folders, then click to open `Project 21 - AI Story Continuation/task1_story_continuation.ipynb`.

**What to say**:
> "Good morning, Sir. For our project evaluation, our group has completed two tasks exploring **Sequence Modeling with LSTMs** and **Optimization Dynamics with Batch Normalization**. 
> 
> We have structured both tasks separately in their own folders. I will start by demonstrating **Task 1: AI Story Continuation**."

---

## Part 2: Project 21 (LSTM Story Continuation) (Approx. 3 Minutes)

**What to do**: Scroll down to Section 1 & 2 in the notebook, pointing out the dataset downloading and dataset class.

**What to say**:
> "In this project, we trained a character-level LSTM. Unlike traditional models that use hand-crafted features or pre-trained words, our model starts with zero knowledge of English grammar. It learns representations directly from character indices.
> 
> We chose two contrasting text styles: William Shakespeare's plays, which are poetic and dramatic, and Arthur Conan Doyle's Sherlock Holmes, which is narrative detective prose. We preprocessed both texts by lowercase mapping and slicing them to train quickly while preserving stylistic features."

**What to do**: Scroll to Section 3 & 4 showing the `CharLSTM` model code.

**What to say**:
> "Here is our model architecture. We project character indices into a 128-dimensional embedding space, which is then fed into a stacked 2-layer LSTM with 256 hidden units. We applied a Dropout of 0.2 between layers. 
> 
> The core reason we use an **LSTM** rather than a Vanilla RNN is to resolve the vanishing gradient problem. The LSTM's additive cell state update acts as a gradient highway, allowing context to propagate over long timesteps.
> 
> For optimization, we use Cross-Entropy Loss calculated at each character timestep, and we apply gradient clipping with a maximum norm of 5.0 to prevent exploding gradients during Backpropagation Through Time."

**What to do**: Scroll to Section 6 showing the Training Loss Curves plot.

**What to say**:
> "As you can see from our loss curves plot, both models trained smoothly on our system's GPU. The Shakespeare model's loss decreased from 2.17 to 0.99, and the Sherlock model's loss dropped to 1.13 over 8 epochs."

**What to do**: Scroll to Section 7 showing the Generated Text outputs for different temperatures.

**What to say**:
> "This section demonstrates the core experiment of this project: **Greedy Sampling vs. Temperature-based Sampling**.
> 
> When we use **Greedy Sampling (or Temperature = 0)**, the model always picks the character with the highest probability. As you can see on the screen, the model gets stuck in repetitive loops, repeating phrases like *'the world is a proper my lord, and my lord...'*.
> 
> When we set the temperature to **0.6**, we get the best balance of coherence and variety. The Shakespeare model successfully outputs dramatic dialogue using words like *'parish'*, *'voice'*, and the character marker *'all:'*. The Sherlock model outputs detective narrative terms like *'holmes'*, *'waiting'*, and *'band'*.
> 
> If we push the temperature up to **1.5**, the output becomes high-entropy gibberish. The probability distribution is flattened, making character choices almost completely random."

---

## Part 3: Project 23 (Batch Norm vs. No Batch Norm) (Approx. 3 Minutes)

**What to do**: Go back to the Jupyter file explorer and open `Project 23 - Batch Norm vs No Batch Norm/task2_batch_norm.ipynb`.

**What to say**:
> "Now, Sir, I will demonstrate **Task 2: Batch Norm vs. No Batch Norm**.
> 
> Deep networks with 6 or more layers are notoriously difficult to train because of **internal covariate shift** and **vanishing or exploding gradients**. In this project, we built a 6-layer Deep MLP and ran three controlled experiments on the MNIST dataset to stress-test the model's robustness."

**What to do**: Scroll down to show Experiment 1 (Standard LR) results and plots.

**What to say**:
> "In **Experiment 1**, we trained both models using a standard learning rate of 0.01 and default He initialization. 
> 
> Looking at the plot, the Batch Normalized network converges much faster, reaching **97.10%** test accuracy. The baseline network without Batch Norm converges much more slowly, ending at **92.83%**."

**What to do**: Scroll to Experiment 2 (High LR) results and plots.

**What to say**:
> "In **Experiment 2**, we stress-tested the networks with a very high learning rate of **0.2**. 
> 
> As you can see, the baseline model without Batch Norm completely fails. The loss stays stuck at **2.3026**, which is the entropy of random guessing on 10 classes ($-\ln(0.1)$), and accuracy is flat at **11.35%**. The gradients exploded, making the weights diverge.
> 
> However, the Batch Norm model trained perfectly, reaching its highest accuracy of **98.24%**. Batch Norm normalizes layer outputs, which restricts activation magnitudes and prevents gradients from exploding."

**What to do**: Scroll to Experiment 3 (Suboptimal Init) results and plots.

**What to say**:
> "In **Experiment 3**, we initialized the weights to near-zero values with a standard deviation of **0.001**.
> 
> Without Batch Norm, the signals shrank exponentially across the 6 layers, leading to vanishing gradients. The baseline model failed to learn, flatlining at **11.35%** accuracy.
> 
> But with Batch Norm, the network automatically rescaled the activations back to unit variance at each layer, restoring the signal. The BN model converged successfully, reaching **97.48%** test accuracy."

---

## Part 4: Conclusion (Approx. 30 Seconds)

**What to say**:
> "To conclude, our experiments show that LSTMs are highly effective at capturing stylistic features in sequence modeling, and Batch Normalization is a critical component that stabilizes deep networks against bad initializations and extreme learning rates.
> 
> Thank you, Sir. We are ready for your questions."
