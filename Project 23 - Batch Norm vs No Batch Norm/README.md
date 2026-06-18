# Project 23: Batch Normalization vs. No Batch Normalization in Deep Networks

This directory contains the implementation, dataset caching, and training evaluation code for **Project 23: Batch Normalization vs. No Batch Normalization**. The project implements a 6-layer Deep Multilayer Perceptron (MLP) to classify MNIST handwritten digits, comparing network stability with and without Batch Normalization under severe training conditions.

---

## 📂 Directory Structure

```
Project 23 - Batch Norm vs No Batch Norm/
├── data/                       # MNIST dataset cache directory
├── A_G03_Task2.ipynb           # Main Jupyter Notebook containing model, datasets, training, and plots
└── README.md                   # Project documentation (This file)
```

---

## 🧠 Model Architecture (`DeepMLP`)

The network is a 6-layer Feedforward Neural Network (5 hidden layers, 1 output layer):

* **Input Dimension**: `784` (flattened $28 \times 28$ grayscale pixel values).
* **Hidden Layers**: 5 layers with `512` hidden units each.
* **Activation**: Rectified Linear Unit (ReLU) for non-linearity.
* **Batch Normalization Layer (`nn.BatchNorm1d`)**: If enabled, inserted after the linear layer and before the activation layer:
  $$\text{Linear Layer} \to \text{Batch Normalization} \to \text{ReLU}$$
  Mathematically, it normalizes each batch feature to mean 0 and variance 1, and then scales ($\gamma$) and shifts ($\beta$) using learnable parameters:
  $$y = \gamma \left( \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}} \right) + \beta$$
* **Output Dimension**: `10` (logits corresponding to digit classes 0 through 9).

---

## 🔬 Stress-Test Experiments and Findings

Three distinct training experiments were conducted to evaluate model resilience:

### Experiment 1: Standard Training (LR = 0.01, Default Initialization)
* **Configuration**: Learning rate = 0.01, default Kaiming weights initialization.
* **Results**: Both models converge, but the Batch Norm model trains much faster and achieves a higher validation accuracy (**97.10%**) compared to the baseline model without Batch Norm (**92.83%**).

### Experiment 2: High Learning Rate Stress Test (LR = 0.2)
* **Configuration**: High learning rate = 0.2.
* **Results (No Batch Norm)**: Diverges immediately. The large weight updates propagate exponentially through 6 layers, causing gradients to explode. The loss flatlines at **2.3026** ($-\ln(0.1)$, representing random 10% guessing on MNIST).
* **Results (With Batch Norm)**: The model is completely stable. Batch Norm constantly rescales exploding intermediate outputs, enabling convergence to **98.24%** accuracy.

### Experiment 3: Suboptimal Initialization Stress Test (Tiny Weights = 0.001)
* **Configuration**: Weight standard deviation initialized to a tiny value of `0.001` (instead of normal Kaiming scale).
* **Results (No Batch Norm)**: The signals shrink exponentially as they travel forward through the 6 layers. By the output layer, values are practically zero, and gradients vanish. The model learns nothing (accuracy stuck at ~10.2%).
* **Results (With Batch Norm)**: Batch Norm calculates the small variance of these tiny activations and divides by it, automatically scaling the signals back up to unit variance. The model recovers and trains successfully to **97.48%** accuracy.

---

## 🚀 How to Run the Notebook

1. Ensure the project prerequisites are installed:
   ```bash
   pip install torch torchvision numpy matplotlib notebook
   ```
2. Launch the Jupyter Notebook interface from the root directory:
   ```bash
   jupyter notebook
   ```
3. Open and run all cells in `A_G03_Task2.ipynb`. The MNIST dataset will automatically download to the `data/` folder, train standard and stress-tested models, and plot validation accuracy/loss comparison curves.
