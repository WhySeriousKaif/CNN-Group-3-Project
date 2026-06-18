# 7-Member Google Meet Video Presentation Script

This document contains the complete, word-for-word spoken script for your group's video presentation. It maps out each slide (from your 15-slide deck) to a specific presenter, providing visual cues, exact lines, and natural transition cues (hand-offs) between team members to ensure a smooth, professional recording on Google Meet.

---

## 📅 Presentation Overview & Speaking Roles

* **Total Slides**: 15
* **Target Duration**: 8 - 10 Minutes
* **Recording Setup**: One member (e.g., Mohammad Kaif) will share their screen to present the slide deck (`presentation.pptx` or the compiled PDF) and advance the slides while all 7 members are in the Google Meet call with their cameras on. Each member will speak when their assigned slide is displayed.

### Speaking Assignments:
1. **Mohammad Kaif** (Slides 1 & 2) — *Group Leader & Host*
2. **Arhan Das** (Slide 3)
3. **Sumit Akhuli** (Slides 4 & 5)
4. **Shiva Gupta** (Slide 6 & 11)
5. **Sarthak Mishra** (Slides 7 & 8)
6. **Netram Faran** (Slides 9 & 10)
7. **Aditya Prasad** (Slides 12, 13, 14, & 15) — *Conclusion & Q&A Lead*

---

## 🎬 Act-by-Act Spoken Script

### 🎙️ PART 1: TITLE & TASK 1 (LSTM STORY CONTINUATION) OVERVIEW

#### **Slide 1: Title Slide**
* **Presenter**: **Mohammad Kaif**
* **On-Screen Visuals**: *Slide 1 showing the title "Optimization Dynamics and Sequence Generation in Deep Learning", subtitle "Comparative Analysis of Batch Normalization & Character-Level LSTMs", and list of 7 group members.*
* **Visual Action**: *Mohammad Kaif shares screen showing Slide 1. All members are muted except Kaif.*
* **Spoken Script**:
  > "Good afternoon, everyone. Welcome to our group video presentation for the Deep Learning course. My name is **Mohammad Kaif**, and I will be starting our presentation today. 
  > 
  > Our project is titled **'Optimization Dynamics and Sequence Generation in Deep Learning'**. In this work, our team conducted a detailed, comparative study across two core deep learning domains: first, sequence modeling and representation learning using character-level LSTMs; and second, optimization dynamics and training stability using Deep Feedforward Multi-Layer Perceptrons with and without Batch Normalization.
  > 
  > Our group members are myself—Mohammad Kaif—along with Arhan Das, Sumit Akhuli, Shiva Gupta, Sarthak Mishra, Netram Faran, and Aditya Prasad. Let's move to Slide 2."

---

#### **Slide 2: Task 1: AI Story Continuation Overview**
* **Presenter**: **Mohammad Kaif**
* **On-Screen Visuals**: *Slide 2 showing Task 1 Objective, core questions explored (representation learning without word dictionaries, decoding strategies, and stylistic corpuses).*
* **Visual Action**: *Kaif advances screen to Slide 2.*
* **Spoken Script**:
  > "On Slide 2, we introduce our first task: **AI Story Continuation**. Our main goal here was to train a character-level recurrent neural network that can read a raw text prompt and write a natural, grammatically correct continuation.
  > 
  > In doing this, we set out to answer three main questions:
  > First, can a neural network learn spelling, spacing, and grammar entirely from scratch, using raw sequences of letters instead of a pre-defined English word dictionary?
  > Second, how do different text decoding strategies—specifically greedy decoding versus temperature-based probabilistic sampling—affect the creativity and coherence of the text?
  > And third, how does training the model on completely different styles of writing transfer that vocabulary and tone to the final output?
  > 
  > To explain the sequence modeling architecture we chose to solve this, I will now hand over the presentation to **Arhan Das**. Arhan, please take us through Slide 3."

---

#### **Slide 3: Sequence Modeling: LSTM Architecture**
* **Presenter**: **Arhan Das**
* **On-Screen Visuals**: *Slide 3 showing "Why LSTM?", descriptions of Forget, Input, and Output gates, and the network configuration (Embedding Layer 128-dim, Stacked LSTM 2 layers, 256 units, Dropout 0.2, Linear Decoder).*
* **Visual Action**: *Kaif advances screen to Slide 3. Arhan unmutes; Kaif remains muted.*
* **Spoken Script**:
  > "Thank you, Kaif. Moving to Slide 3, we look at why we chose Long Short-Term Memory networks, or LSTMs, for this sequence generation task. 
  > 
  > Standard Recurrent Neural Networks fail on longer sequences because gradients either shrink to zero or grow to infinity when multiplied repeatedly over many time steps. LSTMs solve this by introducing a **Cell State**—which acts like an information highway—along with three gating mechanisms:
  > * The **Forget Gate** decides what historical information we should discard.
  > * The **Input Gate** decides what new details we should write into the cell state.
  > * The **Output Gate** decides what hidden state to output next.
  > 
  > Our network configuration consists of:
  > 1. An **Embedding Layer** that maps character indexes to a dense 128-dimensional space.
  > 2. A **Stacked LSTM** with 2 layers and 256 memory units in each layer, using a 0.2 dropout rate to prevent overfitting.
  > 3. A **Linear Decoder** that projects the 256 hidden dimensions back to raw scores for our vocabulary.
  > 
  > I will now pass the presentation to **Sumit Akhuli** to discuss our data pipeline. Sumit, over to you."

---

#### **Slide 4: Data Pipeline & Corpuses**
* **Presenter**: **Sumit Akhuli**
* **On-Screen Visuals**: *Slide 4 showing the details of the Tiny Shakespeare and Sherlock Holmes corpuses, and the preprocessing pipeline steps (lowercasing, sequence length T=100).*
* **Visual Action**: *Kaif advances screen to Slide 4. Sumit unmutes; Arhan mutes.*
* **Spoken Script**:
  > "Thank you, Arhan. On Slide 4, we examine our data pipeline and the text datasets we selected. 
  > 
  > We trained two separate LSTMs on two highly contrasting writing styles:
  > * The first is the **Tiny Shakespeare** corpus, which consists of poetic dialogue, plays, and a compact vocabulary of 37 unique characters.
  > * The second is the **Sherlock Holmes** corpus, representing 19th-century detective prose, narrative sentences, and a larger vocabulary of 57 characters.
  > 
  > For preprocessing, we lowercase all text to keep the vocabulary size small and speed up training. We slice the text into overlapping blocks of length **T = 100 characters**. The model's task is simple: look at a window of 100 characters and predict the 101st character. This forces the model to learn structural relationships, spelling, and spacing. 
  > Let's move to Slide 5."

---

#### **Slide 5: Decoding and Sampling Techniques**
* **Presenter**: **Sumit Akhuli**
* **On-Screen Visuals**: *Slide 5 showing Greedy Decoding vs. Temperature Sampling, including the Softmax temperature scaling equation and the effects of Low (0.2), Balanced (0.6), and High (1.5) temperatures.*
* **Visual Action**: *Kaif advances screen to Slide 5. Sumit continues speaking.*
* **Spoken Script**:
  > "On Slide 5, we look at how the model actually writes new text after it is trained. The model outputs raw scores, or logits, for the next character. We tested two main decoding methods:
  > * First, **Greedy Decoding**, where the model always picks the letter with the highest probability. While this is fast, it is highly deterministic and gets stuck in infinite, repetitive word loops.
  > * Second, **Temperature Sampling**, where we divide the logits by a temperature parameter 'T' before running them through the Softmax function.
  > 
  > We tested three temperature levels:
  > 1. **Low Temperature (T = 0.2)**: Highly conservative and repetitive text.
  > 2. **Balanced Temperature (T = 0.6)**: The sweet spot. The model produces coherent words, correct grammar, and stylistic sentences.
  > 3. **High Temperature (T = 1.5)**: Extremely chaotic. The model takes too many risks, leading to spelling breakdowns and random gibberish.
  > 
  > To show our training convergence and final story samples, I will hand over to **Shiva Gupta**. Shiva, please explain Slide 6."

---

#### **Slide 6: Task 1: Training Loss & Text Samples**
* **Presenter**: **Shiva Gupta**
* **On-Screen Visuals**: *Slide 6 showing the training loss curves (smooth convergence for both models) and the text generated by Shakespeare and Sherlock LSTMs from the prompt "the secret of ".*
* **Visual Action**: *Kaif advances screen to Slide 6. Shiva unmutes; Sumit mutes.*
* **Spoken Script**:
  > "Thank you, Sumit. Slide 6 presents our Task 1 empirical training results and text outputs.
  > 
  > If you look at the loss curve on the right, you can see both models converged smoothly. The Shakespeare model reached a final loss of **0.9955** after 8 epochs, and the Sherlock model reached **1.1377**.
  > 
  > When we prompted both models with the starting phrase *'the secret of '*, they generated highly distinct text:
  > * The Shakespeare model generated poetic, theatrical lines like *'this too, well of parish that's worth's voice'*.
  > * The Sherlock model generated detective narrative prose like *'home upon his waiting. he woild dost the band'*.
  > 
  > This confirms that our LSTMs successfully learned spelling, spacing, and stylistic tone. 
  > 
  > Now, we will shift to Task 2, which focuses on Batch Normalization. I will hand over the presentation to **Sarthak Mishra** to introduce Task 2."

---

### 🎙️ PART 2: TASK 2 (BATCH NORMALIZATION COMPARISON)

#### **Slide 7: Task 2: Batch Norm vs. No Batch Norm**
* **Presenter**: **Sarthak Mishra**
* **On-Screen Visuals**: *Slide 7 showing Task 2 Objective, and the key challenges in training deep networks (Internal Covariate Shift, Vanishing/Exploding Gradients).*
* **Visual Action**: *Kaif advances screen to Slide 7. Sarthak unmutes; Shiva mutes.*
* **Spoken Script**:
  > "Thank you, Shiva. On Slide 7, we introduce Task 2: **Batch Normalization Analysis**. Our objective here is to train a deep, 6-layer Feedforward Neural Network on the MNIST handwritten digits dataset and compare how it performs with and without Batch Normalization.
  > 
  > Training very deep networks is notoriously difficult due to two major challenges:
  > * **Internal Covariate Shift**: As early layers update their weights, the distribution of activations at intermediate layers shifts constantly. Later layers have to constantly adapt, which slows down training.
  > * **Vanishing and Exploding Gradients**: During backpropagation, error signals are multiplied through many layers. They can shrink to zero, stopping learning, or explode to infinity, causing numerical instability.
  > 
  > We will look at how we set up our experiments to analyze this on Slide 8."

---

#### **Slide 8: Deep MLP Architecture and Setup**
* **Presenter**: **Sarthak Mishra**
* **On-Screen Visuals**: *Slide 8 showing MNIST dataset specs (60k train, 10k test), the 6-layer MLP structure (784 flat input, five 512 hidden layers, 10 output, ReLU), and the two configurations (Setup A: Baseline, Setup B: Batch Norm).*
* **Visual Action**: *Kaif advances screen to Slide 8. Sarthak continues speaking.*
* **Spoken Script**:
  > "Slide 8 shows our experimental setup. We use the classic MNIST dataset of handwritten digits. 
  > 
  > Our network is a 6-layer Multi-Layer Perceptron:
  > * The input is a flattened image vector of size 784.
  > * We have 5 hidden layers with 512 nodes each, using ReLU activation.
  > * The output layer has 10 nodes for digit classification.
  > 
  > We compared two configurations:
  > * **Setup A (Baseline)**: Linear layers followed directly by ReLU.
  > * **Setup B (Batch Norm)**: We insert a 1D Batch Normalization layer between each linear layer and the ReLU activation.
  > 
  > Both networks are optimized using standard mini-batch SGD with a batch size of 64. 
  > 
  > To explain our first two experiments, I will hand over to **Netram Faran**. Netram, please walk us through Slide 9."

---

#### **Slide 9: Experiment 1: Standard Training**
* **Presenter**: **Netram Faran**
* **On-Screen Visuals**: *Slide 9 showing Experiment 1 parameters (LR=0.01, standard initialization) and the train/test loss and accuracy plots (comparing No BN and With BN).*
* **Visual Action**: *Kaif advances screen to Slide 9. Netram unmutes; Sarthak mutes.*
* **Spoken Script**:
  > "Thank you, Sarthak. On Slide 9, we look at our first experiment, where we trained both models under standard conditions with a normal learning rate of 0.01.
  > 
  > Looking at the plots on the right:
  > * The green curve represents the model **With Batch Normalization**. It converges extremely rapidly, reaching **97.10%** test accuracy in just 5 epochs.
  > * The blue dashed curve represents the baseline model **Without Batch Normalization**. Training is significantly slower and only reaches **92.83%** accuracy.
  > 
  > This experiment demonstrates that even under normal conditions, Batch Normalization acts as an optimization accelerator, allowing the model to train faster and achieve higher final accuracy.
  > Let's move to Slide 10."

---

#### **Slide 10: Experiment 2: Stress-Test with High Learning Rate**
* **Presenter**: **Netram Faran**
* **On-Screen Visuals**: *Slide 10 showing Experiment 2 parameters (LR=0.2, standard initialization) and the flatline failure of No BN vs. the stable training of With BN.*
* **Visual Action**: *Kaif advances screen to Slide 10. Netram continues speaking.*
* **Spoken Script**:
  > "On Slide 10, we stress-tested the networks with an extremely aggressive learning rate of 0.2. 
  > 
  > The results are night and day:
  > * The baseline model **Without Batch Norm** (the blue curve) failed completely. The training loss flatlined at **2.3026**, and accuracy stayed stuck at **11.35%**, which is equivalent to random guessing. The gradients exploded, making the weights unusable.
  > * The model **With Batch Norm** (the green curve) trained with complete stability, reaching its highest overall accuracy of **98.24%**.
  > 
  > This stress test proves that Batch Norm's scale-invariance stabilizes gradient updates, permitting the use of much higher learning rates.
  > 
  > I will now pass the presentation back to **Shiva Gupta** to present Slide 11."

---

#### **Slide 11: Experiment 3: Stress-Test with Poor Initialization**
* **Presenter**: **Shiva Gupta**
* **On-Screen Visuals**: *Slide 11 showing Experiment 3 parameters (LR=0.01, tiny weights with standard deviation 0.001) and the flatline failure of No BN vs. the rescue by With BN.*
* **Visual Action**: *Kaif advances screen to Slide 11. Shiva unmutes; Netram mutes.*
* **Spoken Script**:
  > "Thank you, Netram. Slide 11 shows our third experiment, where we stress-tested the models with poor initialization. We set the weights to a tiny scale, with a standard deviation of 0.001.
  > 
  > * The baseline network **Without Batch Norm** failed completely. The initial signals were so small that they vanished as they went through the 6 layers, and accuracy flatlined at **11.35%**.
  > * However, the model **With Batch Norm** was completely rescued. Because Batch Norm rescales the activations at each layer back to unit variance, it kept the signals alive, allowing the model to train successfully and achieve **97.48%** test accuracy.
  > 
  > This shows that Batch Norm drastically reduces a network's dependency on careful weight initialization.
  > 
  > To explain the mathematical foundations behind these results, I will now hand over to **Aditya Prasad**. Aditya, please take us through Slide 12."

---

### 🎙️ PART 3: MATHEMATICAL INSIGHTS & CONCLUSION

#### **Slide 12: How Batch Normalization Stabilizes Gradients**
* **Presenter**: **Aditya Prasad**
* **On-Screen Visuals**: *Slide 12 showing the Batch Normalization equations (Mini-batch Mean, Mini-batch Variance, Normalization, Scale and Shift).*
* **Visual Action**: *Kaif advances screen to Slide 12. Aditya unmutes; Shiva mutes.*
* **Spoken Script**:
  > "Thank you, Shiva. On Slide 12, we lay out the mathematics of Batch Normalization. For a mini-batch of size m:
  > 1. We compute the batch mean.
  > 2. We compute the batch variance.
  > 3. We normalize the activation by subtracting the mean and dividing by the standard deviation.
  > 4. We apply a learnable scale parameter gamma and shift parameter beta to preserve the layer's representation capacity.
  > 
  > The key intuition here is **scale-invariance**. By dividing by the standard deviation, Batch Norm decouples the scale of the weights from the scale of the activations. Even if weights are scaled up or down, the output activations and gradient magnitudes remain stable. This prevents vanishing and exploding gradients.
  > Let's move to Slide 13."

---

#### **Slide 13: Summary of Empirical Findings**
* **Presenter**: **Aditya Prasad**
* **On-Screen Visuals**: *Slide 13 showing the side-by-side comparison table of all three experiments.*
* **Visual Action**: *Kaif advances screen to Slide 13. Aditya continues speaking.*
* **Spoken Script**:
  > "Slide 13 summarizes all our Batch Normalization experiments in a single table.
  > 
  > Under standard training, Batch Norm accelerated convergence and improved test accuracy. In both stress tests—high learning rate and poor initialization—the baseline model without Batch Norm failed completely, guessing randomly at 11.35% accuracy with a flat loss of 2.3026. Batch Norm rescued the network in both cases, achieving 98.24% and 97.48% accuracy.
  > 
  > This table is concrete proof of why Batch Normalization is a standard, essential layer in modern deep neural networks.
  > Let's move to Slide 14."

---

#### **Slide 14: Connections to Deep Learning Theory**
* **Presenter**: **Aditya Prasad**
* **On-Screen Visuals**: *Slide 14 showing connections to theory: Universal Approximation (LSTMs), Optimization Landscapes (Batch Norm), and Initialization Sensitivity.*
* **Visual Action**: *Kaif advances screen to Slide 14. Aditya continues speaking.*
* **Spoken Script**:
  > "On Slide 14, we connect our experimental findings back to deep learning theory:
  > * **Representation Learning**: We demonstrated how our LSTM learned character representations (like spelling and grammar rules) purely from sequence data.
  > * **Optimization Landscapes**: Batch Normalization smoothens the optimization landscape, which makes backpropagation more stable and allows optimization algorithms like SGD to converge much faster.
  > * **Initialization Sensitivity**: While initialization schemes like Xavier or He are standard, Batch Norm significantly relaxes the network's sensitivity to these initial scales.
  > 
  > Let's move to our final slide."

---

#### **Slide 15: Conclusion and Q&A**
* **Presenter**: **Aditya Prasad**
* **On-Screen Visuals**: *Slide 15 showing the final conclusion points (LSTMs for style/syntax representation, Batch Norm for training stability) and a "Thank you! Questions?" text.*
* **Visual Action**: *Kaif advances screen to Slide 15. Aditya continues speaking.*
* **Spoken Script**:
  > "To conclude our presentation on Slide 15:
  > 1. Character-level LSTMs are highly effective at learning and generating text, capturing grammatical and stylistic properties directly from data.
  > 2. Batch Normalization is a critical architectural component for deep feedforward networks, providing optimization acceleration and robust protection against vanishing and exploding gradients.
  > 
  > That concludes our presentation. Thank you, Sir, and thank you everyone for your time. We are now open to any questions you may have."

* **Visual Action**: *All team members unmute briefly to say "Thank you, Sir". Kaif keeps the screen share active on Slide 15 in case the evaluator asks to refer to a previous slide or asks to see a code run in the Jupyter Notebook.*

---

## 💡 Tips for a Smooth Recording

1. **Test Your Audio**: Ensure everyone has a quiet environment and a working microphone before starting the recording.
2. **Smooth Transitions**: Unmute yourself *just before* the previous speaker finishes their slide so that there is no awkward silence.
3. **Screen Sharing**: Whoever shares the screen (usually Mohammad Kaif) should use "Present a Window" or "Present Entire Screen" and have the slide deck ready in presentation mode. Let other speakers focus entirely on their spoken lines.
4. **Jupyter Notebook Ready**: Keep the Jupyter Notebook server running in the background. If the professor asks you to show the live code run during the presentation, Kaif can quickly swap the screen share window to show the notebooks (`task1_story_continuation.ipynb` or `task2_batch_norm.ipynb`) and run the cells.
