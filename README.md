# Deep Learning Optimization & Sequence Generation (CNN Group 3 Project)

This repository contains the complete codebase, outputs, and documentation for our two deep learning projects (Project 21: AI Story Continuation via LSTM, and Project 23: Batch Normalization Analysis). It also includes slides, reports, and viva preparation scripts to assist in the evaluation.

---

## 📂 Repository Structure

```
CNN-Group-3-Project/
├── Project 21 - AI Story Continuation/       # Task 1: LSTM Character Model
│   ├── data/                                 # Cached Text Corpuses (Shakespeare & Sherlock)
│   ├── plots/                                # Loss curves visualizations
│   ├── A_G03_Task1.ipynb                     # Main Story Generation Notebook
│   └── README.md                             # Project 21 Documentation
│
├── Project 23 - Batch Norm vs No Batch Norm/  # Task 2: Deep MLP Stress-Test
│   ├── data/                                 # MNIST dataset cache
│   ├── A_G03_Task2.ipynb                     # Main Batch Norm Comparison Notebook
│   └── README.md                             # Project 23 Documentation
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
3. Open `Project 21 - AI Story Continuation/A_G03_Task1.ipynb` or `Project 23 - Batch Norm vs No Batch Norm/A_G03_Task2.ipynb`.
4. Click **Run All** in the toolbar. All data is cached locally so training runs will complete in under 2 minutes.

---

## 📊 Summary of Projects

### Project 21: Character-Level LSTM Story Generator (Easy Language)
This project is about training an AI to write stories character-by-character. Instead of giving the AI a list of English words, it starts with zero knowledge of English and learns spelling, punctuation, spacing, and writing styles entirely on its own. We trained this model on two very different kinds of writing: William Shakespeare's plays (which are poetic and old-fashioned) and Sherlock Holmes detective stories (which are structured detective novels). 

To generate text, the AI looks at a window of 100 characters and guesses the next character. We tested three ways to make the AI generate stories:
1. **Greedy Mode (Temperature = 0)**: The AI always picks the single most likely next letter. This causes the AI to get stuck in loops, repeating the same words over and over (e.g. *"the world is the world is the world..."*).
2. **High Temperature Mode (Temperature = 1.5)**: The AI picks letters almost randomly. This results in chaotic text and gibberish, where spelling breaks down completely.
3. **Balanced Mode (Temperature = 0.6)**: The AI picks letters in a smart, slightly creative way. This produces readable, correctly spelled text that perfectly mimics either Shakespeare's dramatic style or Sherlock's detective tone.

### Project 23: Batch Normalization Analysis (Easy Language)
This project compares two deep neural networks: one with a special feature called **Batch Normalization (Batch Norm)** and one without it. Deep networks (we used a 6-layer model to classify handwritten digits) are notoriously hard to train because the signal either shrinks to zero (vanishes) or grows to infinity (explodes) as it passes through many layers. Batch Norm works by automatically resizing the signals at each layer to make sure they stay stable.

We ran three controlled experiments to test how Batch Norm helps:
1. **Standard Training**: The model with Batch Norm trained much faster and reached a higher classification accuracy (**97.10%**) than the standard model (**92.83%**).
2. **High Learning Rate Stress Test**: If the model takes updates that are too aggressive, the standard model fails completely and behaves like random guessing (11% accuracy). With Batch Norm, the signals are kept stable, allowing the model to train successfully and reach **98.24%** accuracy.
3. **Suboptimal Initialization Stress Test**: If we start the network with weights that are near-zero, the signals vanish in a standard model and it learns nothing. With Batch Norm, the network rescales these small signals back up, letting the model train successfully to **97.48%** accuracy.

---

## 🎓 Viva & Presentation Deliverables
To prepare for the individual and group evaluation:
* **Academic Report**: Open [project_report.md](project_report.md) for details on implementation, metrics, and theoretical analysis.
* **Slides**: Open [slide_deck.md](slide_deck.md) for a structured outline of 15 slides with detailed speaker notes.
* **Spoken Transcripts**: Refer to [viva_and_demo_transcripts/](viva_and_demo_transcripts/) for word-for-word scripts on what to say during the demo and how to answer the top 10 mock questions.
