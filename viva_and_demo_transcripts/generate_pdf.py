import os
from fpdf import FPDF

class AcademicReportPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(100, 110, 120)
            self.cell(0, 8, "Scaler School of Technology | Deep Learning I | Capstone Project", border="B", align="L")
            self.cell(0, 8, "Section A - Group 3", border="B", align="R")
            self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def create_report_pdf():
    pdf = AcademicReportPDF()
    pdf.alias_nb_pages()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # ------------------ COVER HEADER ------------------
    pdf.set_y(25)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(11, 15, 25) # Dark Slate
    pdf.cell(0, 10, "Deep Learning Optimization & Sequence Generation", align="C")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(180, 115, 20) # Gold Accent
    pdf.cell(0, 8, "Comparative Study of Character-Level LSTMs & Batch Normalization", align="C")
    pdf.ln(10)
    
    # Gold Horizontal Separator
    pdf.set_draw_color(180, 115, 20)
    pdf.set_line_width(0.8)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)
    
    # Group Info Block
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "Section: A | Group: G03 (Group 3)", align="C")
    pdf.ln(10)
    
    # Presenters Panel
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(60, 60, 60)
    
    # Columns for Group Members
    members_col1 = [
        "MD Kaif Molla (md.24bcs10221@sst.scaler.com)",
        "Arhan Das (Arhan.24bcs10023@sst.scaler.com)",
        "Sumit Akhuli (Sumit.24bcs10158@sst.scaler.com)",
        "Shiva Gupta (shiva.24bcs10461@sst.scaler.com)"
    ]
    members_col2 = [
        "Sarthak Mishra (Sarthak.24bcs10470@sst.scaler.com)",
        "Netram Faran (netram.24bcs10329@sst.scaler.com)",
        "Aditya Prasad (aditya.24bcs10179@sst.scaler.com)"
    ]
    
    max_len = max(len(members_col1), len(members_col2))
    for i in range(max_len):
        name1 = members_col1[i] if i < len(members_col1) else ""
        name2 = members_col2[i] if i < len(members_col2) else ""
        pdf.cell(85, 5, name1, align="L")
        pdf.cell(85, 5, name2, align="R")
        pdf.ln(5)
        
    pdf.ln(10)
    
    # ------------------ TASK 1 SECTION ------------------
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 8, "1. Task 1: AI Story Continuation (Project 21)")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "1.1 Problem Statement")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    p1_desc = (
        "The objective of this project is to model sequential text data at the character level to generate coherent "
        "continuations from user-defined prompts. Traditional language models relied on hand-crafted n-gram features or "
        "Markov chains, which suffer from the curse of dimensionality and contain very limited context memory windows. "
        "This project demonstrates representation learning and sequence modeling by training a Recurrent Neural Network "
        "(specifically, an LSTM) to learn the orthographic and grammatical structure of English text from scratch. "
        "By training on two highly distinct corpuses - William Shakespeare's dramatic plays and Arthur Conan Doyle's Sherlock Holmes "
        "detective stories - we analyze how the source corpus style and the decoding temperature affect text generation."
    )
    pdf.multi_cell(0, 5, p1_desc)
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "1.2 Technical Approach & Model Architecture")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    
    p1_tech = (
        "We implement a character-level sequence-to-sequence model using PyTorch:\n"
        "1. Data Pipeline: The raw text is lowercased and mapped to a unique vocabulary. Sliding input sequences "
        "of length T=100 characters are extracted with overlapping steps. The targets are the sequences shifted by 1 index.\n"
        "2. Embedding Layer: Projects discrete character tokens into a dense 128-dimensional continuous vector space.\n"
        "3. LSTM Recurrent Core: A stacked 2-layer LSTM with 256 hidden units per layer. Gates (Forget, Input, and Output) "
        "regulate cell state update equations to maintain long-term gradient flows without decay.\n"
        "4. Decoding Layer: A fully-connected linear layer projecting the hidden state back to the vocabulary size.\n"
        "5. Optimization & Training: Trained using the Adam optimizer (LR=0.002) and Cross-Entropy Loss over all timesteps. "
        "Dropout of 0.2 is applied between LSTMs, and gradient clipping is capped at 5.0 to mitigate exploding gradients."
    )
    pdf.multi_cell(0, 5, p1_tech)
    pdf.ln(6)
    
    # ------------------ PAGE 2 ------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "1.3 LSTM Experiments & Results")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    
    p1_exp = (
        "Both models were trained for 8 epochs (80 batches per epoch, batch size = 128) using PyTorch MPS GPU acceleration.\n"
        "- Shakespeare Model: Loss converged smoothly from 2.1700 (Epoch 1) to 0.9955 (Epoch 8).\n"
        "- Sherlock Holmes Model: Loss converged from 2.3608 (Epoch 1) to 1.1377 (Epoch 8).\n\n"
        "We tested the models with a prompt: 'the secret of ' under different decoding temperatures (T):"
    )
    pdf.multi_cell(0, 5, p1_exp)
    pdf.ln(4)
    
    # Temperature Outputs formatting
    temp_results = [
        ("Greedy (T=0)", "Deterministic choice. Leads to repetitive loops:\n- Shakespeare: 'the secret of the world is a proper my lord, and my lord, i will not be...'\n- Sherlock: 'the secret of his mistle spoting and hadnestrand, however and west...'"),
        ("Low Temp (T=0.2)", "Very safe, but highly repetitive:\n- Shakespeare: 'the secret of the world is the world is the world is a proper my lord...'\n- Sherlock: 'the secret of his colners was a bother of his columble took...'"),
        ("Balanced (T=0.6)", "Optimal creativity and style mimicry. Correct spelling and syntax:\n- Shakespeare: 'the secret of this too, well of parish that's worth's voice...'\n- Sherlock: 'the secret of home upon his waiting. he woild dost the band, hereself...'"),
        ("Extreme (T=1.5)", "Uniform probability choice. spelling and coherence disintegrate:\n- Shakespeare: 'the secret of cit, fanlerithly to authartial, git dog...'\n- Sherlock: 'the secret of yourlecmust. we enkgaiqh, go fors; themes-funl...'")
    ]
    
    for t_name, t_text in temp_results:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(180, 115, 20)
        pdf.cell(0, 5, t_name)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 4.5, t_text)
        pdf.ln(4)

    pdf.ln(4)
    
    # ------------------ TASK 2 SECTION ------------------
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 8, "2. Task 2: Batch Normalization Study (Project 23)")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "2.1 Problem Statement")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    p2_desc = (
        "Deep feedforward networks are difficult to optimize because of Internal Covariate Shift - where intermediate "
        "layer activation distributions shift continuously as weights are adjusted - and gradient anomalies (vanishing "
        "and exploding gradients). This project evaluates how Batch Normalization stabilizes optimization, accelerates "
        "convergence, and provides resilience against aggressive hyperparameters (high learning rates) and near-zero "
        "initialization scales."
    )
    pdf.multi_cell(0, 5, p2_desc)
    pdf.ln(6)
    
    # ------------------ PAGE 3 ------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "2.2 Technical Setup & Parameters")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    p2_tech = (
        "We build a 6-layer Deep MLP classifier trained on the MNIST dataset (28x28 grayscale, 10 classes):\n"
        "- Model Layout: Input (784) -> 5 hidden layers (512 nodes each) with ReLU -> Output (10).\n"
        "- Setup A (Baseline): Standard Linear layers followed directly by ReLU activations.\n"
        "- Setup B (Batch Norm): Insertion of a BatchNorm1d layer before each ReLU activation.\n"
        "- Training details: Trained using mini-batch SGD with a batch size of 128 for 5 epochs. We evaluated three "
        "controlled experiments to analyze training dynamics."
    )
    pdf.multi_cell(0, 5, p2_tech)
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "2.3 Controlled Stress Tests & Results")
    pdf.ln(8)
    
    # FPDF2 Native Tables integration
    pdf.set_font("Helvetica", "", 9)
    with pdf.table(col_widths=(30, 45, 45, 50), text_align="C", padding=2) as table:
        # Header Row
        row = table.row()
        row.cell("Experiment")
        row.cell("Configuration")
        row.cell("No Batch Norm (Baseline)")
        row.cell("With Batch Norm")
        
        # Row 1
        row = table.row()
        row.cell("Exp 1:\nStandard")
        row.cell("LR = 0.01\nKaiming Init")
        row.cell("Slow convergence\nFinal Test Acc: 92.83%")
        row.cell("Fast convergence\nFinal Test Acc: 97.10%")
        
        # Row 2
        row = table.row()
        row.cell("Exp 2:\nHigh LR")
        row.cell("LR = 0.2\nKaiming Init")
        row.cell("DIVERGED / FAILED\nFinal Test Acc: 11.35%")
        row.cell("STABLE / OPTIMAL\nFinal Test Acc: 98.24%")
        
        # Row 3
        row = table.row()
        row.cell("Exp 3:\nSmall Init")
        row.cell("LR = 0.01\nStd Dev = 0.001")
        row.cell("VANISHED / FAILED\nFinal Test Acc: 11.35%")
        row.cell("STABLE / RECOVERED\nFinal Test Acc: 97.48%")
        
    pdf.ln(8)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 6, "2.4 Empirical Analysis & Insights")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    p2_analysis = (
        "- Experiment 1 (Standard): Batch Norm speeds up learning immediately. By epoch 2, the BN network hits "
        "95.2% accuracy, whereas the baseline lags at 88.6%. The final margin is 97.10% vs 92.83%.\n"
        "- Experiment 2 (High LR = 0.2): The baseline diverges immediately. Aggressive updates blow up activations, "
        "leading to saturated losses (2.3026) and random guessing (11.35%). Batch Norm handles the high learning rate "
        "with complete stability, yielding our highest overall score of 98.24% test accuracy.\n"
        "- Experiment 3 (Small Init = 0.001): Without BN, activation variances decay exponentially across the 6 layers "
        "down to zero. Learning stops. Batch Norm recalculates and rescales intermediate variances back to unit scale "
        "at each step, allowing the network to recover and achieve 97.48% accuracy."
    )
    pdf.multi_cell(0, 5, p2_analysis)
    pdf.ln(6)
    
    # ------------------ PAGE 4 ------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 8, "3. Comparative Synthesis & Core Theory Connections")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    synthesis = (
        "Our empirical studies connect directly to core Deep Learning Theory:\n"
        "1. Decoupling Weight Scales: Dividing layer outputs by their standard deviation makes Batch Norm scale-invariant. "
        "Scaling weights does not change output distributions or gradient magnitudes, enabling stable high learning rates.\n"
        "2. Representation Learning: The character LSTM proves that networks can self-assemble hierarchical features "
        "(spelling rules, syntactic breaks, and author styles) directly from raw text sequences without word boundaries.\n"
        "3. Decoupling Logit Entropy: In language modeling, temperature acts as an entropy scale. At low temperature, "
        "predictions are deterministic and repetitious. High temperature distributes probabilities evenly, producing "
        "high-entropy gibberish. T=0.6 acts as the optimal point for vocabulary creativity and formatting consistency."
    )
    pdf.multi_cell(0, 5, synthesis)
    pdf.ln(6)
    
    # ------------------ CONTRIBUTIONS SECTION ------------------
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(11, 15, 25)
    pdf.cell(0, 8, "4. Subgroup Contributions & Tasks")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    contributions = (
        "To ensure collaborative productivity, our 7 group members divided code and slides as follows:\n\n"
        "- Subgroup Project 21 (LSTM sequence modeling): Developed the embedding-LSTM model code, character mapping "
        "functions, and temperature logit decoding loops.\n"
        "  * MD Kaif Molla, Arhan Das, and Sumit Akhuli.\n\n"
        "- Subgroup Project 23 (Batch Normalization analysis): Built the 6-layer MLP models, coded the SGD optimizer "
        "sweeps, and evaluated training logs under high learning rate and poor initialization scales.\n"
        "  * Sarthak Mishra, Netram Faran, Aditya Prasad, and Shiva Gupta.\n\n"
        "- Subgroup Presentation & Report Design: Co-designed and compiled the final 15-slide PowerPoint deck "
        "using python-pptx templates and structured this academic report.\n"
        "  * Shiva Gupta and Arhan Das."
    )
    pdf.multi_cell(0, 5, contributions)
    
    output_filename = "A_G03_Final_Project_Report.pdf"
    pdf.output(output_filename)
    print(f"Report PDF successfully generated as: {output_filename}")

if __name__ == "__main__":
    create_report_pdf()
