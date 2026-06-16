# Slide-by-Slide Viva Presentation Guide

This guide is designed to help you present your PowerPoint slide deck (`presentation.pptx`) to your professor ("Sir") in simple, professional, and easy-to-understand spoken English.

---

## Slide 1: Title Slide
### What to Say:
> "Good morning/afternoon, Sir. Today, our group will present our deep learning project on **'Optimization Dynamics and Sequence Generation in Deep Learning'**. We have performed a comparative study of two key architectures: Character-Level LSTMs for sequence generation, and Deep Feedforward Networks to analyze the effects of Batch Normalization. 
> 
> Our group members are MD Kaif Molla, Arhan Das, Sumit Akhuli, Shiva Gupta, Sarthak Mishra, Netram Faran, and Aditya Prasad. Let's move to Slide 2."

---

## Slide 2: Task 1: AI Story Continuation Overview
### What to Say:
> "On Slide 2, we introduce Task 1: AI Story Continuation. Our goal here is to train a character-level recurrent neural network to read a text prompt and generate a continuation. 
> 
> We wanted to answer three core questions:
> 1. Can a neural network learn spelling, grammar, and literary style entirely from raw character sequences, without any pre-defined word dictionary?
> 2. How do different decoding strategies—like greedy decoding vs. temperature sampling—change the quality of the generated text?
> 3. And how does the style of the training text change the vocabulary and tone of what the model generates?"

---

## Slide 3: Sequence Modeling: LSTM Architecture
### What to Say:
> "Moving to Slide 3, we look at why we chose LSTMs and how they work. Standard RNNs fail on longer text sequences because gradients either vanish or explode when multiplied over many time steps. 
> 
> LSTMs solve this using a **Cell State**—which acts like an information highway—and three key gates:
> * The **Forget Gate** decides what old information we should discard.
> * The **Input Gate** decides what new details we should write into the cell state.
> * The **Output Gate** decides what the next hidden state should be.
> 
> Our specific network configuration uses a 128-dimensional embedding layer, two stacked LSTM layers with 256 memory units each, 0.2 dropout to prevent overfitting, and a linear decoder to map the output back to character scores."

---

## Slide 4: Data Pipeline & Corpuses
### What to Say:
> "On Slide 4, we explain our data pipeline. We trained two separate models on completely different text styles to compare them:
> * First, **Tiny Shakespeare**, which is filled with old English dialogue and has a small vocabulary of 37 unique characters.
> * Second, **Sherlock Holmes**, which is modern narrative prose and has a larger vocabulary of 57 unique characters.
> 
> Our preprocessing pipeline is straightforward: we convert all text to lowercase to keep the vocabulary compact, create index mappings for the characters, and slice the text into overlapping chunks of length T = 100. The model's task is simple: look at 100 characters, and predict the 101st character."

---

## Slide 5: Decoding and Sampling Techniques
### What to Say:
> "Slide 5 covers how we generate text from our trained model. The model outputs raw scores (logits) for the next character, and we have two ways to select the next character:
> * **Greedy Decoding (T=0)** always selects the character with the absolute highest probability. This is highly deterministic, but it often gets stuck in infinite, repetitive loops.
> * **Temperature Sampling (T > 0)** divides the logits by a temperature factor before applying the Softmax function.
> 
> We tested three temperature settings:
> 1. **Low Temperature (T=0.2)**: Safe but highly repetitive and lacks creativity.
> 2. **Balanced Temperature (T=0.6)**: The sweet spot. It produces creative, fluent text with correct spelling and grammar.
> 3. **High Temperature (T=1.5)**: Complete chaos. The model takes too many risks, leading to misspelled words and random gibberish."

---

## Slide 6: Task 1: Training Loss & Text Samples
### What to Say:
> "On Slide 6, we look at the training results. If you look at the loss curve on the right, you'll see both models converged smoothly. The Shakespeare model reached a final training loss of 0.9955 in 8 epochs, and the Sherlock model reached 1.1377.
> 
> When we prompt both models with the phrase *'the secret of '*, you can see how clearly they captured their respective styles:
> * Shakespeare generates poetic, theatrical phrases like *'this too, well of parish that's worth's voice'*.
> * Sherlock generates mystery-novel style sentences like *'home upon his waiting. he woild dost the band'*.
> This proves the character-level LSTM successfully learned vocabulary, syntax, and stylistic tone."

---

## Slide 7: Task 2: Batch Norm vs. No Batch Norm
### What to Say:
> "Now, Sir, let's shift to Task 2: Batch Normalization. Here, our objective is to train a deep, 6-layer Feedforward Network on the MNIST dataset and compare how it performs with and without Batch Normalization.
> 
> Training very deep networks is difficult because of two major challenges:
> 1. **Internal Covariate Shift**: The distribution of activations at intermediate layers shifts constantly as earlier layers update their weights. Later layers have to constantly adapt, which slows down training.
> 2. **Vanishing and Exploding Gradients**: As gradients are backpropagated through many layers, they can shrink to zero or grow exponentially, preventing parameter updates or causing the model to diverge."

---

## Slide 8: Deep MLP Architecture and Setup
### What to Say:
> "Slide 8 shows our experimental setup. We use the MNIST dataset of handwritten digits, which has 60,000 training images and 10,000 test images. 
> 
> Our model is a 6-layer MLP:
> * It takes a flattened image vector of size 784 as input.
> * It has 5 hidden layers with 512 nodes each, using ReLU activation.
> * It has a 10-node output layer for digit classifications.
> 
> We compare two setups:
> * **Setup A (Baseline)**: Simple linear layers followed directly by ReLU.
> * **Setup B (Batch Norm)**: We insert a `BatchNorm1d` layer between the linear transformation and the ReLU activation.
> Both are optimized using standard mini-batch SGD with a batch size of 64."

---

## Slide 9: Experiment 1: Standard Training
### What to Say:
> "On Slide 9, we run our first experiment using standard training conditions: a standard learning rate of 0.01 and normal weight initialization.
> 
> Looking at the plots on the right:
> * **With Batch Norm** (the green curve), the model converges very rapidly, reaching **97.10%** test accuracy in just 5 epochs.
> * **Without Batch Norm** (the blue curve), training is much slower and only reaches **92.83%** accuracy.
> This shows that even under ideal conditions, Batch Norm acts as an optimization accelerator."

---

## Slide 10: Experiment 2: High Learning Rate Stress Test
### What to Say:
> "On Slide 10, we stress-test both networks with an extremely aggressive learning rate of 0.2.
> 
> The results are night and day:
> * **Without Batch Norm** (the blue curve), the model fails completely. The training loss flatlines at 2.3026 and accuracy stays stuck at **11.35%**, which is equivalent to random guessing. The gradients exploded, making the weights unusable.
> * **With Batch Norm** (the green curve), the network trains with complete stability and actually reaches its highest overall score of **98.24%** test accuracy.
> This proves that Batch Norm's scale-invariance stabilizes gradient updates, permitting much higher learning rates."

---

## Slide 11: Experiment 3: Poor Initialization Stress Test
### What to Say:
> "Slide 11 shows our third experiment, where we stress-test the networks using a tiny weight initialization scale, setting the standard deviation to 0.001.
> 
> * **Without Batch Norm**, the baseline model fails completely. The initial signals are so tiny that they completely vanish as they propagate through the 6 layers, and accuracy stays stuck at **11.35%**.
> * **With Batch Norm**, the network is rescued. Because Batch Norm rescales the activations at each layer back to unit variance, it prevents the signal from vanishing and achieves **97.48%** test accuracy.
> This shows that Batch Norm drastically reduces the network's dependency on weight initialization scale."

---

## Slide 12: How Batch Normalization Stabilizes Gradients
### What to Say:
> "On Slide 12, we lay out the mathematical operations of Batch Normalization. For a mini-batch of size m:
> 1. We compute the mini-batch mean (μ_B).
> 2. We compute the mini-batch variance (σ_B²).
> 3. We normalize the activation (x̂_i) by subtracting the mean and dividing by the standard deviation.
> 4. We apply a learnable scale (γ) and shift (β) parameter to preserve the network's capacity.
> 
> **The main intuition is scale-invariance**: dividing by the standard deviation means that scaling the weights does not change the outputs or the gradient magnitudes. This keeps gradients stable, prevents activation explosion, and smoothens the loss landscape."

---

## Slide 13: Summary of Empirical Findings
### What to Say:
> "Slide 13 summarizes all our Batch Normalization experiments in a single table. 
> 
> As you can see, in the standard case, Batch Norm speeds up convergence. In both stress tests—high learning rate and poor initialization—it successfully rescues the network from complete training failure. This highlights why Batch Normalization is a standard, essential layer in modern deep learning."

---

## Slide 14: Connections to Deep Learning Theory
### What to Say:
> "On Slide 14, we connect our practical experiments back to deep learning theory:
> * **Representation Learning**: We demonstrated how a character-level model learns representation features (like spelling and grammar) purely from data.
> * **Initialization**: While careful initialization schemes (like Xavier or He) are useful, they are highly sensitive. Batch Norm relaxes this sensitivity.
> * **Optimization Landscapes**: Batch Norm stabilizes the backpropagation of gradients, smoothing the loss landscape and allowing for much faster, more robust optimization."

---

## Slide 15: Conclusion and Q&A
### What to Say:
> "Finally, on Slide 15, we conclude our presentation.
> 
> To summarize:
> 1. Character-level LSTMs are highly capable of learning spelling and syntactic styles directly from raw sequences.
> 2. Batch Normalization is an indispensable component for deep architectures, providing massive optimization speedup and stability under extreme training conditions.
> 
> Thank you, Sir, for your time. Our team is now ready to take any questions you have."
