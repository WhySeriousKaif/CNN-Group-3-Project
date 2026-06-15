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
* **Objective**: Model natural language spelling, vocabulary, and grammar at a character-by-character level.
* **Architecture**: Character Embedding (128-dim) $\to$ Stacked 2-Layer LSTM (256-units, 0.2 Dropout) $\to$ Linear Decoder.
* **Findings**:
  * **Greedy sampling ($T=0$)** causes the model to loop repetitively.
  * **Moderate temperature ($T=0.6$)** generates style-appropriate sentences matching the target corpus (poetic Shakespeare plays vs narrative Sherlock Holmes stories).
  * **High temperature ($T \ge 1.0$)** increases entropy and introduces spelling errors.

### Project 23: Batch Normalization Stress-Testing
* **Objective**: Evaluate training convergence of a 6-layer Deep MLP on MNIST with and without Batch Normalization.
* **Stress Test Experiments**:
  1. **Standard training ($LR=0.01$)**: Batch Norm accelerates convergence, reaching **97.10%** test accuracy vs the baseline's **92.83%**.
  2. **High Learning Rate ($LR=0.2$)**: Baseline network suffers from exploding gradients and completely fails (loss stuck at **2.3026**, accuracy **11.35%**). Batch Norm network stabilizes gradient magnitude, achieving **98.24%** test accuracy.
  3. **Suboptimal Initialization ($\sigma=0.001$)**: Baseline network suffers from vanishing gradients (accuracy flatlines at **11.35%**). Batch Norm automatically rescales the variance at each layer, enabling convergence to **97.48%** test accuracy.

---

## 🎓 Viva & Presentation Deliverables
To prepare for the individual and group evaluation:
* **Academic Report**: Open [project_report.md](project_report.md) for details on implementation, metrics, and theoretical analysis.
* **Slides**: Open [slide_deck.md](slide_deck.md) for a structured outline of 15 slides with detailed speaker notes.
* **Spoken Transcripts**: Refer to [viva_and_demo_transcripts/](viva_and_demo_transcripts/) for word-for-word scripts on what to say during the demo and how to answer the top 10 mock questions.
