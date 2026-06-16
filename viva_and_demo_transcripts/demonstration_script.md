# Spoken Transcript: Project Demonstration Guide (Easy Language)

This script walks you through exactly what to do and say in front of your professor ("Sir"). It is written in simple, plain English to avoid sounding too "bookish" or formal.

---

## Part 1: Introduction (Approx. 30 Seconds)

**What to do**: Open the Jupyter main page showing both folders, then click to open `Project 21 - AI Story Continuation/task1_story_continuation.ipynb`.

**What to say**:
> "Good morning, Sir. For our project evaluation, our group worked on two main tasks. 
> 
> First, we built an AI that learns to write stories character-by-character. Second, we analyzed how a technique called Batch Normalization helps deep neural networks train stably. 
> 
> We have organized both projects into separate folders. I will start by showing you our first notebook: **Task 1: AI Story Continuation**."

---

## Part 2: Project 21 (LSTM Story Continuation) (Approx. 3 Minutes)

**What to do**: Scroll down to Section 1 & 2 in the notebook (pointing out the Shakespeare and Sherlock datasets).

**What to say**:
> "In this task, we wanted our AI to learn to write text. Instead of giving the AI a pre-made list of English words, it starts with zero knowledge and has to learn spelling, spacing, punctuation, and sentence styles entirely on its own from raw letters.
> 
> Looking at the code here, we import standard PyTorch libraries like `torch.nn` for neural network layers and `torch.optim` for optimization. We wrote a custom Dataset class that reads the text files, maps each letter to a unique number, and slices the text into inputs of exactly 100 characters.
> 
> For example, if the text is 'deep learning' and our sequence length is 4:
> - The model takes the input sequence 'd', 'e', 'e', 'p'.
> - The target letter we want the model to predict next is ' ' (the space).
> - We map these letters to numbers: 'd' becomes 4, 'e' becomes 5, 'p' becomes 16, and space becomes 0. So the input is [4, 5, 5, 16] and the target is 0.
> - Our model does this exact same mapping, but it slices the text into blocks of 100 characters to predict the 101st character.
> 
> We trained it on two very different styles of writing: William Shakespeare's plays, which are poetic and old-fashioned, and Sherlock Holmes detective stories, which are structured narrative novels."

**What to do**: Scroll to Section 3 & 4 (showing the model code).

**What to say**:
> "Here is our model structure. We defined a Python class called `CharLSTM` that inherits from PyTorch's `nn.Module`. 
> 
> Inside the code, we first use an `nn.Embedding` layer to convert each character number into a 128-dimensional vector. Then, we pass these vectors into a stacked 2-layer `nn.LSTM` with 256 memory units. Finally, we use an `nn.Linear` decoder layer to output a score for every possible next character.
> 
> The reason we use an **LSTM** instead of a basic RNN is to solve the memory fading problem. In a basic RNN, training signals fade out or blow up over long sequences. LSTMs solve this by introducing a direct memory channel that keeps the training signals healthy.
> 
> In our training loop code, we calculate the `nn.CrossEntropyLoss`, call `loss.backward()` to run backpropagation, and use `nn.utils.clip_grad_norm_` to clip the gradients to 5.0 so our updates don't explode during training."

**What to do**: Scroll to Section 6 (showing the Training Loss Curves plot).

**What to say**:
> "As you can see on the screen, the training loss dropped smoothly for both models. The Shakespeare model loss went down to 0.99, and the Sherlock model went down to 1.13 over 8 training loops."

**What to do**: Scroll to Section 7 (showing the Generated Text output).

**What to say**:
> "This section shows our main experiment: testing the 'temperature' parameter, which controls the AI's creativity.
> 
> If we set the temperature to **0 (Greedy Mode)**, the AI plays it safe and always picks the single most likely letter. This makes it repeat itself in loops, like saying *'the world is the world is the world...'* over and over.
> 
> If we set the temperature to **0.6 (Balanced Mode)**, we get the best results. The spelling is correct, and the AI copies the poetic style of Shakespeare or the detective style of Sherlock Holmes perfectly.
> 
> But if we push it to **1.5 (High Mode)**, the AI becomes too random. The letters scramble, and it generates complete gibberish."

---

## Part 3: Project 23 (Batch Norm vs. No Batch Norm) (Approx. 3 Minutes)

**What to do**: Go back to the Jupyter file manager, open the `Project 23 - Batch Norm vs No Batch Norm` folder, and open `task2_batch_norm.ipynb`.

**What to say**:
> "Now, Sir, I will demonstrate **Task 2: Batch Norm vs. No Batch Norm**.
> 
> Deep neural networks with many layers—like the 6-layer model we built here to classify handwritten digits—are very hard to train because the signal shrinks or blows up as it goes deep. Batch Normalization works by automatically resizing the signals at each layer to keep them stable.
> 
> Looking at the code in this notebook, we created a modular neural network class called `DeepMLP`. We designed the constructor so that if the `use_batch_norm` flag is set to `True`, the code automatically inserts an `nn.BatchNorm1d` layer right before each `nn.ReLU` activation function. This allows us to toggle Batch Norm on and off easily.
> 
> We also wrote a training helper function that loops through PyTorch's `DataLoader` for MNIST, calculates cross-entropy loss, runs the `optim.SGD` optimizer to update parameters, and keeps track of training loss and test accuracy. We ran three experiments to compare a model with Batch Norm against a normal model without it."

**What to do**: Scroll to Experiment 1 (Standard LR) results and plot.

**What to say**:
> "In **Experiment 1**, we trained both models using a standard learning rate of 0.01. 
> 
> Looking at the plot, the Batch Norm model (green line) trained much faster and reached **97.10%** accuracy. The normal model (red dashed line) was much slower and only reached **92.83%**."

**What to do**: Scroll to Experiment 2 (High LR) results and plot.

**What to say**:
> "In **Experiment 2**, we tested a high learning rate of **0.2** where the updates are very aggressive. 
> 
> The baseline model without Batch Norm failed completely, guessing randomly at **11.35%** accuracy (flat red line). This is because the weights exploded. 
> 
> However, the model with Batch Norm trained perfectly and reached **98.24%** accuracy because Batch Norm kept the internal signals under control."

**What to do**: Scroll to Experiment 3 (Suboptimal Init) results and plot.

**What to say**:
> "In **Experiment 3**, we started the model with weights that are extremely small—almost zero. 
> 
> Without Batch Norm, the signals vanished as they went through the 6 layers, and the model could not learn (accuracy flatlined at **11.35%**). 
> 
> But with Batch Norm, the network automatically scaled those tiny signals back up to a normal size, allowing it to train successfully to **97.48%** accuracy."

---

## Part 4: Conclusion (Approx. 30 Seconds)

**What to say**:
> "To sum up, our projects show that LSTMs are great at learning writing styles and spelling, and Batch Normalization is essential for keeping deep networks stable under extreme training conditions.
> 
> Thank you, Sir. We are ready for your questions."
