# Deep Learning Optimization & Sequence Generation (CNN Group 3 Project)

This repository contains the complete codebase, outputs, and documentation for our two deep learning projects (Project 21: AI Story Continuation via LSTM, and Project 23: Batch Normalization Analysis). It also includes slides, reports, and viva preparation scripts to assist in the evaluation.

---

## 📂 Repository Structure

```
CNN-Group-3-Project/
├── Project 21 - AI Story Continuation/       # Task 1: LSTM Character Model
│   ├── data/                                 # Cached Text Corpuses
│   │   ├── shakespeare.txt                   # William Shakespeare Dramatic Works
│   │   └── sherlock.txt                      # Arthur Conan Doyle Sherlock Holmes
│   └── task1_story_continuation.ipynb        # Pre-computed Story Generation Notebook
│
├── Project 23 - Batch Norm vs No Batch Norm/  # Task 2: Deep MLP Stress-Test
│   ├── data/                                 # MNIST dataset cache
│   └── task2_batch_norm.ipynb                # Pre-computed Batch Norm comparison Notebook
│
├── viva_and_demo_transcripts/                # Spoken Presentation Scripts
│   ├── demonstration_script.md               # Script for sharing screen
│   ├── viva_qna_cheat_sheet.md               # Top 10 Mock Questions & Answers
│   └── viva_strategy_and_guidelines.md       # Group coordination & troubleshooting
│
├── project_report.md                         # 5-6 Page Academic Joint Report
├── slide_deck.md                             # 15-Slide presentation outline & speaker notes
└── README.md                                 # Project Overview & Setup Instructions (This file)
```

---

## 🚀 Getting Started & Running the Code

### Prerequisites
Make sure you have PyTorch, torchvision, numpy, matplotlib, and Jupyter notebook installed.
```bash
/usr/bin/python3 -m pip install torch torchvision numpy matplotlib notebook --user
```

### Running the Notebooks
To view and run the notebooks interactively:
1. Open terminal and run:
   ```bash
   /usr/bin/python3 -m notebook
   ```
2. Open the printed local URL (e.g. `http://localhost:8888`) in your browser.
3. Open `task1_story_continuation.ipynb` or `task2_batch_norm.ipynb`.
4. Click **Run All** in the toolbar. All data is cached locally so training runs will complete in under 2 minutes.

---

## 📊 Summary of Projects

### Project 21: AI Story Continuation via Character-Level LSTM
Project 21 explores character-level sequence modeling to generate natural language continuations. By training a stacked LSTM network on two distinct styles—William Shakespeare's dramatic plays and Arthur Conan Doyle's Sherlock Holmes novels—the model learns orthography, word boundaries, grammar, and style from scratch without any pre-defined word-level tokens. The network feeds character embedding vectors into a two-layer LSTM with 256 hidden units, using a dropout rate of 0.2 to prevent overfitting and gradient clipping to stabilize the training. During testing, we evaluate the model using different decoding sampling temperatures ($T$). Greedy sampling ($T=0$) causes the network to repeat high-probability sequences in loops, while high temperatures ($T \ge 1.0$) introduce high entropy, leading to spelling and structural disintegration. We find that a moderate temperature of $0.6$ provides the optimal balance, successfully outputting coherent sentences that accurately mimic the vocabulary and style of the source corpus.

### Project 23: Batch Normalization Stress-Testing
Project 23 investigates the training dynamics of deep networks by comparing a 6-layer Feedforward Neural Network (MLP) with and without Batch Normalization on the MNIST dataset. Deep networks are notoriously hard to train due to internal covariate shift—where activation distributions shift as weights update—and vanishing or exploding gradients. Batch Normalization resolves this by normalizing intermediate activations to zero mean and unit variance over each mini-batch, and scaling/shifting them using learnable parameters. We conduct three controlled stress-test experiments. In standard training (learning rate = 0.01), Batch Norm accelerates convergence, leading to a test accuracy of 97.10% compared to 92.83% for the baseline. Under a high learning rate (0.2), the baseline network diverges due to exploding gradients (achieving only 11.35% accuracy, which represents random guessing), whereas the Batch Norm network trains stably to reach 98.24% accuracy. Finally, under suboptimal near-zero initialization ($\sigma=0.001$), the baseline network fails completely due to vanishing gradients, while the Batch Norm network rescales the signals at each layer, successfully converging to 97.48% test accuracy.

---

## 🎓 Viva & Presentation Deliverables
To prepare for the individual and group evaluation:
* **Academic Report**: Open [project_report.md](project_report.md) for details on implementation, metrics, and theoretical analysis.
* **Slides**: Open [slide_deck.md](slide_deck.md) for a structured outline of 15 slides with detailed speaker notes.
* **Spoken Transcripts**: Refer to [viva_and_demo_transcripts/](viva_and_demo_transcripts/) for word-for-word scripts on what to say during the demo and how to answer the top 10 mock questions.
