Viewed slide_deck.md:1-20

Here is a **1-Day Quick Prep Roadmap** and a **Bare Minimum Core Concept Summary** to help you learn both projects and score high in your viva tomorrow.

---

## 📅 The 5-Step Order of Study (Takes ~2 Hours Total)

Follow this exact order to build your understanding step-by-step without getting overwhelmed:

1. **Step 1: The Bird's-Eye View (10 Mins)**
   * **File to read**: [README.md](file:///Users/mdkaif/Desktop/ML%20Project/README.md)
   * **Goal**: Understand what both projects are at a high level and what the repository contains.
2. **Step 2: The Core Cheat Sheet (30 Mins) 🔑 *Most Important!***
   * **File to read**: [viva_qna_cheat_sheet.md](file:///Users/mdkaif/Desktop/ML%20Project/viva_and_demo_transcripts/viva_qna_cheat_sheet.md)
   * **Goal**: Memorize the answers to the top 10 questions the professor might ask (like why the model fails, how temperature works, and what Batch Norm does).
3. **Step 3: Visual Walkthrough (30 Mins)**
   * **Files to use**: Open the [demonstration_script.md](file:///Users/mdkaif/Desktop/ML%20Project/viva_and_demo_transcripts/demonstration_script.md) side-by-side with the notebooks ([task1_story_continuation.ipynb](file:///Users/mdkaif/Desktop/ML%20Project/Project%2021%20-%20AI%20Story%20Continuation/task1_story_continuation.ipynb) and [task2_batch_norm.ipynb](file:///Users/mdkaif/Desktop/ML%20Project/Project%2023%20-%20Batch%20Norm%20vs%20No%20Batch%20Norm/task2_batch_norm.ipynb)).
   * **Goal**: Learn what to point at on the screen and what to say out loud when demonstrating the code to your professor.
4. **Step 4: Connect to Class Syllabus (30 Mins)**
   * **File to read**: [viva_prep_guide.md](file:///Users/mdkaif/Desktop/ML%20Project/viva_prep_guide.md)
   * **Goal**: Understand how your code connects to what you were taught in weeks 1-7 (ReLU, Sigmoid, He/Xavier initialization, Chain Rule, Backpropagation).
5. **Step 5: Presentation Outline (20 Mins)**
   * **Files to read**: [slide_deck.md](file:///Users/mdkaif/Desktop/ML%20Project/slide_deck.md) and [project_report.md](file:///Users/mdkaif/Desktop/ML%20Project/project_report.md)
   * **Goal**: Familiarize yourself with the slide flow and the experimental numbers so you can quote them confidently.

---

## 💡 The "Bare Minimum" Core Concepts to Focus On

If you are short on time, make sure you understand these **5 fundamental pillars** of the projects:

### 1. Representation Learning (Task 1)
* **What it is**: The model learns spelling, grammar, and sentence structure entirely from raw character inputs.
* **Why it matters**: It proves that deep networks can discover hidden hierarchies (letters $\to$ syllables $\to$ words $\to$ grammar) without us writing hard-coded grammatical rules.

### 2. Why we use LSTM instead of standard RNN (Task 1)
* **Standard RNN problem**: Suffers from **vanishing/exploding gradients** because gradients are repeatedly multiplied by weight matrices over long sequences (time steps).
* **LSTM solution**: Introduces a **Cell State** (an information highway) controlled by **forget, input, and output gates**. Gradients backpropagate through addition instead of multiplication, preserving long-term memory.

### 3. Logit Temperature ($T$) (Task 1)
* **$T = 0$ (Greedy)**: The model is deterministic. It always picks the most likely next character, causing it to get stuck in boring, repetitive loops.
* **$T = 0.6$ (Balanced)**: The sweet spot. Outputs are creative yet grammatically and stylistically correct.
* **$T = 1.5$ (High Entropy)**: Flattens probabilities so predictions become almost random, resulting in misspelled, chaotic words.

### 4. What is Batch Normalization & Internal Covariate Shift (Task 2)
* **Internal Covariate Shift**: The input distribution to deep layers changes continuously during training as weights update, which slows down training.
* **Batch Norm**: Normalizes the activations of each layer across the mini-batch (mean = 0, variance = 1), stabilizing training.

### 5. The 3 Batch Norm Experiments (Task 2)
* **Exp 1 (Standard)**: Batch Norm converges faster and reaches higher accuracy (**97.1%** vs **92.8%**).
* **Exp 2 (High Learning Rate = 0.2)**: Without Batch Norm, weights explode, and the model fails completely (loss flatlines at **`2.3026`**). Batch Norm keeps activations scaled and trains successfully.
* **Exp 3 (Small Initialization = 0.001)**: Without Batch Norm, signals vanish to zero across 6 layers, and the model cannot learn. Batch Norm rescales the signals back to unit variance, allowing successful training.