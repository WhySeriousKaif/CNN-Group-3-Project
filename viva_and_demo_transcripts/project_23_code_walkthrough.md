# Section-by-Section PyTorch Code Walkthrough: Project 23 (Batch Normalization)

This guide translates the PyTorch code in `task2_batch_norm.ipynb` into plain, conversational English. It explains exactly what the code does line-by-line and what is happening "behind the scenes."

---

## Section 1: The Model Architecture (`DeepMLP`)

This class defines our **6-layer Deep MLP (Multilayer Perceptron)**. It is designed to be modular so we can turn Batch Normalization on or off using a simple flag (`use_batch_norm`).

### 1. The Constructor (`__init__`)
```python
class DeepMLP(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=512, output_dim=10, use_batch_norm=False):
        super().__init__()
        self.use_batch_norm = use_batch_norm
```
* **What is happening**:
  * We inherit from `nn.Module` (which is PyTorch's base class for all neural network modules).
  * `input_dim=784`: The input size is 784 because our input images are MNIST digits of size $28 \times 28$ pixels. We flatten them into a single row of 784 numbers.
  * `hidden_dim=512`: Each hidden layer will have 512 nodes.
  * `output_dim=10`: There are 10 outputs because there are 10 digit classes (0 through 9).
  * `use_batch_norm`: A boolean flag (`True`/`False`) to control whether we normalize intermediate signals.

```python
        # Hidden layers (5 hidden layers)
        self.layers = nn.ModuleList()
        self.bns = nn.ModuleList()
```
* **What is happening**:
  * We use `nn.ModuleList()` instead of a normal Python list. This is a special PyTorch list that registers the layers so PyTorch knows they contain trainable weights (parameters).
  * `self.layers` will hold our linear layers.
  * `self.bns` will hold our batch normalization layers.

```python
        # Layer 1: Input to Hidden
        self.layers.append(nn.Linear(input_dim, hidden_dim))
        if use_batch_norm:
            self.bns.append(nn.BatchNorm1d(hidden_dim))
```
* **What is happening**:
  * We add the first layer (`nn.Linear`) which takes our 784 pixel inputs and connects them to 512 hidden nodes.
  * If `use_batch_norm` is `True`, we add a `nn.BatchNorm1d(512)` layer to normalize those 512 values.

```python
        # Layers 2-5: Hidden to Hidden
        for _ in range(4):
            self.layers.append(nn.Linear(hidden_dim, hidden_dim))
            if use_batch_norm:
                self.bns.append(nn.BatchNorm1d(hidden_dim))
```
* **What is happening**:
  * Since this is a deep 6-layer network, we use a loop to add 4 more hidden layers (each going from 512 nodes to 512 nodes).
  * If Batch Norm is enabled, we append a batch norm layer for each of them.
  * Total hidden layers so far: $1 \text{ (first layer)} + 4 \text{ (in loop)} = 5 \text{ hidden layers}$.

```python
        # Layer 6: Hidden to Output
        self.out_layer = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()
```
* **What is happening**:
  * We define the final (6th) layer which takes the 512 hidden nodes and maps them to the 10 final scores.
  * `self.relu = nn.ReLU()`: We define our activation function. ReLU replaces any negative numbers with 0, adding non-linearity to the model so it can learn complex patterns.

---

### 2. The Forward Pass (`forward`)
The forward pass defines how data flows through the network from inputs to outputs.

```python
    def forward(self, x):
        # Flatten image from (B, 1, 28, 28) to (B, 784)
        x = x.view(x.size(0), -1)
```
* **What is happening**:
  * The raw images are 2D arrays: $28 \times 28$ pixels.
  * `x.view(x.size(0), -1)` flattens each image in the batch into a flat row of 784 values.
  * *Behind the scenes*: If we have a batch of 128 images, the shape changes from `(128, 1, 28, 28)` to `(128, 784)`.

```python
        for i, layer in enumerate(self.layers):
            x = layer(x)
            if self.use_batch_norm:
                x = self.bns[i](x)
            x = self.relu(x)
```
* **What is happening**:
  * We loop through all 5 hidden layers one-by-one:
    1. `x = layer(x)`: Multiply the input values by the weights and add biases.
    2. `x = self.bns[i](x)`: If Batch Norm is enabled, scale and shift the values so their mean is 0 and variance is 1. This keeps the values stable.
    3. `x = self.relu(x)`: Apply the ReLU activation (zero out negative numbers).

```python
        x = self.out_layer(x)
        return x
```
* **What is happening**:
  * Pass the final hidden values through the output layer to get 10 scores (logits) representing each digit (0-9). We return these scores.

---

## Section 2: The Training Loop (`train_epoch`)

This function trains the model on the training dataset for exactly one full pass (one epoch).

```python
def train_epoch(model, loader, optimizer, criterion):
    model.train()
    epoch_loss = 0.0
    correct = 0
    total = 0
```
* **What is happening**:
  * `model.train()` puts the model in training mode. This tells PyTorch to calculate running averages for Batch Norm.
  * We initialize trackers for loss, correct guesses, and total processed items.

```python
    for x, y in loader:
        x, y = x.to(device), y.to(device)
```
* **What is happening**:
  * We loop through the data in mini-batches (e.g., 128 images at a time).
  * `x` contains the images; `y` contains the correct digit labels.
  * `.to(device)` pushes the data to the GPU/MPS (Apple Silicon GPU) or CPU for fast calculation.

```python
        optimizer.zero_grad()
```
* **What is happening**:
  * We reset the gradients (slopes) from the previous step. If we don't do this, PyTorch will add the new gradients to the old ones, leading to incorrect updates.

```python
        outputs = model(x)
        loss = criterion(outputs, y)
```
* **What is happening**:
  * **Forward Pass**: Feed the images `x` into our model to get predictions (`outputs`).
  * **Loss Calculation**: We use Cross Entropy Loss (`criterion`) to compare our predicted scores to the actual correct labels `y`. It calculates a single error number (`loss`).

```python
        loss.backward()
        optimizer.step()
```
* **What is happening**:
  * **Backward Pass**: `loss.backward()` calculates the gradients. It tells us how much we need to tweak each weight in the network to make the loss smaller.
  * **Optimization Step**: `optimizer.step()` actually changes the weights using Stochastic Gradient Descent (SGD) based on the calculated gradients and learning rate.

```python
        epoch_loss += loss.item() * x.size(0)
        _, predicted = outputs.max(1)
        total += y.size(0)
        correct += predicted.eq(y).sum().item()
        
    return epoch_loss / total, correct / total
```
* **What is happening**:
  * Accumulate the total loss and count how many correct predictions the network made.
  * At the end of the epoch, return the average loss and accuracy.

---

## Analogy to Keep in Mind for the Viva

If the professor asks you to explain the code simply:
> *"Sir, our `DeepMLP` class is like a pipeline of 6 processing stations. 
> 
> In the constructor (`__init__`), we construct 6 linear layers. If Batch Norm is turned on, we place a filter (a Batch Norm layer) right after each linear layer to normalize the values before they pass through the ReLU gate.
> 
> During training (`train_epoch`), we send data through in batches. For every batch, we calculate the predictions, check our error using Cross-Entropy, send the error feedback backwards through the network with `loss.backward()`, and adjust all weights using the SGD optimizer.
> 
> Batch Norm keeps the values flowing through the pipeline at a stable volume, preventing them from shrinking to zero or blowing up to infinity."*
