import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    # Initialize Presentation
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette Constants
    BG_COLOR = RGBColor(11, 15, 25)         # Deep Navy/Slate
    CARD_BG = RGBColor(20, 27, 45)          # Dark Card Fill
    CARD_BORDER = RGBColor(180, 115, 20)     # Bronze/Gold Border
    BORDER_SUBTLE = RGBColor(40, 50, 75)    # Subtle Slate Border
    TEXT_WHITE = RGBColor(255, 255, 255)    # Primary Text
    TEXT_GRAY = RGBColor(209, 213, 219)     # Body Text
    TEXT_MUTED = RGBColor(148, 163, 184)    # Subtitle/Cap Text
    ACCENT_GOLD = RGBColor(251, 191, 36)    # Warm Gold Highlight
    TABLE_HEADER_BG = RGBColor(180, 115, 20)

    # Fonts
    HEADER_FONT = "Georgia"
    BODY_FONT = "Calibri"

    def apply_background(slide):
        """Applies solid dark background to the slide."""
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

    def add_slide_header(slide, title_text):
        """Adds a standard slide header with a gold separator line."""
        apply_background(slide)
        
        # Title box
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.8))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = HEADER_FONT
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        
        # Horizontal Separator line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, border_color=BORDER_SUBTLE):
        """Draws a premium rounded rectangle background card."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    def style_paragraph(p, text, font_name, size_pt, color_rgb, bold=False, italic=False, space_after=6):
        """Helper to style paragraph text."""
        p.text = text
        p.font.name = font_name
        p.font.size = Pt(size_pt)
        p.font.color.rgb = color_rgb
        p.font.bold = bold
        p.font.italic = italic
        p.space_after = Pt(space_after)
        p.line_spacing = 1.15

    # ==========================================
    # SLIDE 1: Title Slide (Widescreen layout)
    # ==========================================
    slide_layout = prs.slide_layouts[6] # Blank layout
    slide = prs.slides.add_slide(slide_layout)
    apply_background(slide)

    # Title box
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    style_paragraph(p, "Optimization Dynamics and Sequence Generation in Deep Learning", HEADER_FONT, 36, ACCENT_GOLD, bold=True)
    p.alignment = PP_ALIGN.CENTER

    # Subtitle
    p_sub = tf.add_paragraph()
    style_paragraph(p_sub, "Comparative Analysis of Batch Normalization & LSTMs", BODY_FONT, 20, TEXT_MUTED, italic=True)
    p_sub.alignment = PP_ALIGN.CENTER

    # Divider Line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(4.3), Inches(10.333), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = CARD_BORDER
    line.line.fill.background()

    # Column 1 Team members
    team1_box = slide.shapes.add_textbox(Inches(1.5), Inches(4.6), Inches(5.0), Inches(2.4))
    tf1 = team1_box.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    style_paragraph(p1, "MD Kaif Molla", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p1_sub = tf1.add_paragraph()
    style_paragraph(p1_sub, "md.24bcs10221@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED, space_after=6)
    
    p2 = tf1.add_paragraph()
    style_paragraph(p2, "Arhan Das", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p2_sub = tf1.add_paragraph()
    style_paragraph(p2_sub, "Arhan.24bcs10023@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED, space_after=6)

    p3 = tf1.add_paragraph()
    style_paragraph(p3, "Sumit Akhuli", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p3_sub = tf1.add_paragraph()
    style_paragraph(p3_sub, "Sumit.24bcs10158@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED, space_after=6)

    p4 = tf1.add_paragraph()
    style_paragraph(p4, "Shiva Gupta", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p4_sub = tf1.add_paragraph()
    style_paragraph(p4_sub, "shiva.24bcs10461@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED)

    # Column 2 Team members
    team2_box = slide.shapes.add_textbox(Inches(6.8), Inches(4.6), Inches(5.0), Inches(2.4))
    tf2 = team2_box.text_frame
    tf2.word_wrap = True
    
    p5 = tf2.paragraphs[0]
    style_paragraph(p5, "Sarthak Mishra", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p5_sub = tf2.add_paragraph()
    style_paragraph(p5_sub, "Sarthak.24bcs10470@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED, space_after=6)
    
    p6 = tf2.add_paragraph()
    style_paragraph(p6, "Netram Faran", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p6_sub = tf2.add_paragraph()
    style_paragraph(p6_sub, "netram.24bcs10329@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED, space_after=6)

    p7 = tf2.add_paragraph()
    style_paragraph(p7, "Aditya Prasad", HEADER_FONT, 13, TEXT_WHITE, bold=True, space_after=1)
    p7_sub = tf2.add_paragraph()
    style_paragraph(p7_sub, "aditya.24bcs10179@sst.scaler.com", BODY_FONT, 10, TEXT_MUTED)


    # ==========================================
    # SLIDE 2: Task 1: AI Story Continuation Overview (Layout: Single Large Card)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Task 1: AI Story Continuation Overview")

    # Unified background card
    add_card(slide, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.0), CARD_BORDER)
    
    # Left sub-column
    box1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.85), Inches(5.2), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Project Objective", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)
    
    p = tf.add_paragraph()
    style_paragraph(p, "• Train a character-level recurrent neural network to generate story continuations from text prompts.", BODY_FONT, 14, TEXT_GRAY, space_after=12)
    p = tf.add_paragraph()
    style_paragraph(p, "• Forces the model to learn spelling, grammar, punctuation, and style from scratch, without using pre-trained word tokens.", BODY_FONT, 14, TEXT_GRAY, space_after=12)
    p = tf.add_paragraph()
    style_paragraph(p, "• Serves as an illustration of sequence representation learning directly from raw text sequences.", BODY_FONT, 14, TEXT_GRAY)

    # Right sub-column
    box2 = slide.shapes.add_textbox(Inches(6.933), Inches(1.85), Inches(5.2), Inches(4.5))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Core Questions Explored", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf2.add_paragraph()
    style_paragraph(p, "• Representation Learning: Can a model learn English syntax and style entirely at the character level?", BODY_FONT, 14, TEXT_GRAY, space_after=12)
    p = tf2.add_paragraph()
    style_paragraph(p, "• Decoding Strategies: How does deterministic greedy decoding compare to temperature-based probabilistic sampling?", BODY_FONT, 14, TEXT_GRAY, space_after=12)
    p = tf2.add_paragraph()
    style_paragraph(p, "• Stylistic Nuance: How does the style of the training corpus affect the vocabulary, tone, and pacing of the generated output?", BODY_FONT, 14, TEXT_GRAY)


    # ==========================================
    # SLIDE 3: Sequence Modeling: LSTM Architecture (Layout: 3 Narrow Columns)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Sequence Modeling: LSTM Architecture")

    # Column 1 (Left): Why LSTM?
    add_card(slide, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.6))
    tf1 = box1.text_frame
    tf1.word_wrap = True
    style_paragraph(tf1.paragraphs[0], "Why LSTM?", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    p = tf1.add_paragraph()
    style_paragraph(p, "• Vanilla RNNs suffer from vanishing and exploding gradients due to repeated temporal multiplications.\n\n• LSTMs solve this by establishing cell states (Cₜ) acting as information highways where gradients can flow back freely over time.", BODY_FONT, 13, TEXT_GRAY)

    # Column 2 (Middle): Gating Mechanism (Highlighted)
    add_card(slide, Inches(4.816), Inches(1.6), Inches(3.7), Inches(5.0), CARD_BORDER)
    box2 = slide.shapes.add_textbox(Inches(5.016), Inches(1.8), Inches(3.3), Inches(4.6))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Gating Mechanism", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    
    p = tf2.add_paragraph()
    style_paragraph(p, "• Forget Gate (f_t):", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  Decides what history to discard.", BODY_FONT, 12, TEXT_GRAY, space_after=10)

    p = tf2.add_paragraph()
    style_paragraph(p, "• Input Gate (i_t):", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  Decides what new values to write to the cell state.", BODY_FONT, 12, TEXT_GRAY, space_after=10)

    p = tf2.add_paragraph()
    style_paragraph(p, "• Output Gate (o_t):", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  Decides what hidden state to output.", BODY_FONT, 12, TEXT_GRAY)

    # Column 3 (Right): Our Network Config
    add_card(slide, Inches(8.833), Inches(1.6), Inches(3.7), Inches(5.0), BORDER_SUBTLE)
    box3 = slide.shapes.add_textbox(Inches(9.033), Inches(1.8), Inches(3.3), Inches(4.6))
    tf3 = box3.text_frame
    tf3.word_wrap = True
    style_paragraph(tf3.paragraphs[0], "Our Network", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    p = tf3.add_paragraph()
    style_paragraph(p, "• Embedding Layer:\n  Converts character indices to 128-dimensional dense vectors.\n\n• Stacked LSTM:\n  2 layers with 256 memory units, using 0.2 Dropout to prevent overfitting.\n\n• Linear Decoder:\n  Maps 256 hidden features to vocabulary logits.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 4: Data Pipeline & Corpuses (Layout: 2 Top split cards, 1 Unified bottom card)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Data Pipeline & Corpuses")

    # Top Left Card
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.6), Inches(2.3), CARD_BORDER)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(2.0))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Shakespeare plays", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=4)
    p = tf.add_paragraph()
    style_paragraph(p, "• Dramatic old English vocabulary, poetic structures.\n• Compact vocabulary of 37 unique characters.", BODY_FONT, 13, TEXT_GRAY)

    # Top Right Card
    add_card(slide, Inches(6.933), Inches(1.6), Inches(5.6), Inches(2.3), CARD_BORDER)
    box2 = slide.shapes.add_textbox(Inches(7.183), Inches(1.75), Inches(5.1), Inches(2.0))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Sherlock Holmes", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=4)
    p = tf2.add_paragraph()
    style_paragraph(p, "• 19th-century detective stories, structured narrative prose.\n• Larger vocabulary of 57 unique characters.", BODY_FONT, 13, TEXT_GRAY)

    # Bottom Full-width Card
    add_card(slide, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.4), BORDER_SUBTLE)
    
    # Left column of bottom card
    box3_l = slide.shapes.add_textbox(Inches(1.05), Inches(4.35), Inches(5.3), Inches(2.1))
    tf3_l = box3_l.text_frame
    tf3_l.word_wrap = True
    style_paragraph(tf3_l.paragraphs[0], "Preprocessing Pipeline", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=6)
    p = tf3_l.add_paragraph()
    style_paragraph(p, "• Lowercase Conversion: Keeps the vocabulary size compact for faster convergence.", BODY_FONT, 13, TEXT_GRAY)

    # Right column of bottom card
    box3_r = slide.shapes.add_textbox(Inches(6.933), Inches(4.35), Inches(5.3), Inches(2.1))
    tf3_r = box3_r.text_frame
    tf3_r.word_wrap = True
    style_paragraph(tf3_r.paragraphs[0], "Input-Target Slicing", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=6)
    p = tf3_r.add_paragraph()
    style_paragraph(p, "• Slices raw text into overlapping input sequences of length T = 100 characters. Target sequences are shifted by one character.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 5: Decoding and Sampling Techniques (Layout: 1 Left column card, 3 Right horizontal stack cards)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Decoding and Sampling Techniques")

    # Left card: Concept
    add_card(slide, Inches(0.8), Inches(1.6), Inches(4.5), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(4.0), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Decoding Overview", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)
    
    p = tf.add_paragraph()
    style_paragraph(p, "• Greedy Decoding (T = 0):\n  - Always selects the character with the absolute highest probability.\n  - Very deterministic, but highly prone to getting stuck in infinite repeating loops.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Temperature Sampling (T > 0):\n  - Scales the logits by dividing them by T before applying Softmax to control randomness.", BODY_FONT, 13, TEXT_GRAY)

    # Right Stack Card 1 (Low Temp)
    add_card(slide, Inches(5.6), Inches(1.6), Inches(6.933), Inches(1.4), BORDER_SUBTLE)
    box_s1 = slide.shapes.add_textbox(Inches(5.85), Inches(1.75), Inches(6.433), Inches(1.1))
    tf_s1 = box_s1.text_frame
    tf_s1.word_wrap = True
    style_paragraph(tf_s1.paragraphs[0], "Low Temperature (T = 0.2)", HEADER_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf_s1.add_paragraph()
    style_paragraph(p, "• Highly conservative, repetitive, and safe output. Vocabulary remains narrow.", BODY_FONT, 12, TEXT_GRAY)

    # Right Stack Card 2 (Balanced Temp - Highlighted)
    add_card(slide, Inches(5.6), Inches(3.4), Inches(6.933), Inches(1.4), CARD_BORDER)
    box_s2 = slide.shapes.add_textbox(Inches(5.85), Inches(3.55), Inches(6.433), Inches(1.1))
    tf_s2 = box_s2.text_frame
    tf_s2.word_wrap = True
    style_paragraph(tf_s2.paragraphs[0], "Balanced Temperature (T = 0.6) — Recommended", HEADER_FONT, 14, ACCENT_GOLD, bold=True, space_after=2)
    p = tf_s2.add_paragraph()
    style_paragraph(p, "• High quality output: creative and styled language with correct spelling.", BODY_FONT, 12, TEXT_GRAY)

    # Right Stack Card 3 (High Temp)
    add_card(slide, Inches(5.6), Inches(5.2), Inches(6.933), Inches(1.4), BORDER_SUBTLE)
    box_s3 = slide.shapes.add_textbox(Inches(5.85), Inches(5.35), Inches(6.433), Inches(1.1))
    tf_s3 = box_s3.text_frame
    tf_s3.word_wrap = True
    style_paragraph(tf_s3.paragraphs[0], "High Temperature (T = 1.5)", HEADER_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf_s3.add_paragraph()
    style_paragraph(p, "• Complete chaos. Grammatical structure collapses and words disintegrate into random gibberish.", BODY_FONT, 12, TEXT_GRAY)


    # ==========================================
    # SLIDE 6: Task 1: Training Loss & Text Samples
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Task 1: Training Loss & Text Samples")

    # Left Card: Text info
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(4.7), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Empirical Findings & Text Samples", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=8)

    p = tf.add_paragraph()
    style_paragraph(p, "• Loss Convergence:", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Shakespeare Model: final loss of 0.9955 (8 epochs).\n  - Sherlock Model: final loss of 1.1377.", BODY_FONT, 12, TEXT_GRAY, space_after=8)

    p = tf.add_paragraph()
    style_paragraph(p, "• Generated Samples (Prompt: \"the secret of \")", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    
    p = tf.add_paragraph()
    style_paragraph(p, "  - Shakespeare (T=0.6):", BODY_FONT, 12, ACCENT_GOLD, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "    \"the secret of this too, well of parish that's worth's voice...\"", BODY_FONT, 11, TEXT_GRAY, italic=True, space_after=6)
    
    p = tf.add_paragraph()
    style_paragraph(p, "  - Sherlock Holmes (T=0.6):", BODY_FONT, 12, ACCENT_GOLD, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "    \"the secret of home upon his waiting. he woild dost the band...\"", BODY_FONT, 11, TEXT_GRAY, italic=True)

    # Right Card: Image Frame
    add_card(slide, Inches(6.4), Inches(1.6), Inches(6.133), Inches(5.0), CARD_BORDER)
    # Add Image
    img_path = "extracted_plots/task1_lstm_loss.png"
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(6.6), Inches(1.8), Inches(5.733), Inches(4.6))


    # ==========================================
    # SLIDE 7: Task 2: Batch Norm vs. No Batch Norm (Layout: Single Large Card)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Task 2: Batch Norm vs. No Batch Norm")

    # Unified background card
    add_card(slide, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.0), CARD_BORDER)
    
    # Left sub-column
    box1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.85), Inches(5.2), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Project Objective", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)
    
    p = tf.add_paragraph()
    style_paragraph(p, "• Train and compare deep feedforward neural networks (6 layers) with and without Batch Normalization on the MNIST dataset.", BODY_FONT, 14, TEXT_GRAY, space_after=12)
    p = tf.add_paragraph()
    style_paragraph(p, "• Systematically evaluate convergence speed, final test accuracy, and stability under different optimization stress-tests.", BODY_FONT, 14, TEXT_GRAY)

    # Right sub-column
    box2 = slide.shapes.add_textbox(Inches(6.933), Inches(1.85), Inches(5.2), Inches(4.5))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Core Challenges in Deep Networks", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf2.add_paragraph()
    style_paragraph(p, "• Internal Covariate Shift:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  - Activation distributions shift continuously as weights update during training, slowing down training and forcing small learning rates.", BODY_FONT, 13, TEXT_GRAY, space_after=12)
    
    p = tf2.add_paragraph()
    style_paragraph(p, "• Vanishing/Exploding Gradients:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  - Signals vanish or blow up as they propagate through deep layers, stopping learning or causing divergence.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 8: Deep MLP Architecture and Setup (Layout: 3 Narrow Columns)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Deep MLP Architecture and Setup")

    # Column 1 (Left): Dataset
    add_card(slide, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.6))
    tf1 = box1.text_frame
    tf1.word_wrap = True
    style_paragraph(tf1.paragraphs[0], "Dataset", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    p = tf1.add_paragraph()
    style_paragraph(p, "• MNIST Digits Classification:\n  Grayscale 28x28 handwritten digit images.\n\n• Splits:\n  60,000 training samples and 10,000 testing samples, divided into 10 class categories.", BODY_FONT, 13, TEXT_GRAY)

    # Column 2 (Middle): Configuration
    add_card(slide, Inches(4.816), Inches(1.6), Inches(3.7), Inches(5.0), CARD_BORDER)
    box2 = slide.shapes.add_textbox(Inches(5.016), Inches(1.8), Inches(3.3), Inches(4.6))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Configuration (6 Layers)", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    p = tf2.add_paragraph()
    style_paragraph(p, "• Input Layer:\n  784 nodes (flattened 28x28 pixels).\n\n• Hidden Layers:\n  5 layers with 512 nodes each.\n\n• Output Layer:\n  10 nodes (digit category scores).\n\n• Activation:\n  ReLU in all hidden layers.", BODY_FONT, 13, TEXT_GRAY)

    # Column 3 (Right): Tested Setups
    add_card(slide, Inches(8.833), Inches(1.6), Inches(3.7), Inches(5.0), BORDER_SUBTLE)
    box3 = slide.shapes.add_textbox(Inches(9.033), Inches(1.8), Inches(3.3), Inches(4.6))
    tf3 = box3.text_frame
    tf3.word_wrap = True
    style_paragraph(tf3.paragraphs[0], "Tested Setups", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=12)
    p = tf3.add_paragraph()
    style_paragraph(p, "• Setup A (Baseline):\n  Standard MLP with Linear -> ReLU layers. No batch normalization.\n\n• Setup B (Batch Norm):\n  Normalized MLP with Linear -> BatchNorm1d -> ReLU layers.\n\n• Optimization:\n  Mini-batch SGD with batch size = 64.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 9: Experiment 1: Standard Training
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Experiment 1: Standard Training")

    # Left Card: Info
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(4.7), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Standard SGD Training", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Hyperparameters:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Learning rate = 0.01, standard initialization, trained for 5 epochs.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Observations:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - With Batch Norm: Converges rapidly, reaching 97.10% test accuracy.", BODY_FONT, 13, TEXT_GRAY, space_after=4)
    p = tf.add_paragraph()
    style_paragraph(p, "  - No Batch Norm: Converges slowly, reaching 92.83% test accuracy.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Key Takeaway:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Batch Norm acts as an optimization accelerator, helping the model reach higher accuracy in fewer epochs.", BODY_FONT, 13, TEXT_GRAY)

    # Right Card: Image Frame
    add_card(slide, Inches(6.4), Inches(1.6), Inches(6.133), Inches(5.0), CARD_BORDER)
    # Add Image
    img_path = "extracted_plots/task2_exp1_standard.png"
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(6.6), Inches(1.8), Inches(5.733), Inches(4.6))


    # ==========================================
    # SLIDE 10: Experiment 2: Stress-Test with High Learning Rate (Layout: Flipped split layout)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Experiment 2: High Learning Rate Stress Test")

    # Left Card: Image Frame (Flipped!)
    add_card(slide, Inches(0.8), Inches(1.6), Inches(6.133), Inches(5.0), CARD_BORDER)
    # Add Image
    img_path = "extracted_plots/task2_exp2_high_lr.png"
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(1.0), Inches(1.8), Inches(5.733), Inches(4.6))

    # Right Card: Info
    add_card(slide, Inches(7.333), Inches(1.6), Inches(5.2), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(7.583), Inches(1.85), Inches(4.7), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "High Learning Rate Stress Test", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Hyperparameters:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Learning rate = 0.2 (extremely aggressive), trained for 5 epochs.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Observations:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - With Batch Norm: Extremely stable training, reaching 98.24% test accuracy (best overall score).", BODY_FONT, 13, TEXT_GRAY, space_after=4)
    p = tf.add_paragraph()
    style_paragraph(p, "  - No Batch Norm: Fails completely. Weights explode, loss flatlines at 2.3026, and accuracy stays stuck at 11.35% (random guessing).", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Key Takeaway:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Batch Norm scale-invariance stabilizes gradient updates, allowing the network to train under massive learning rates.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 11: Experiment 3: Stress-Test with Poor Initialization
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Experiment 3: Poor Initialization Stress Test")

    # Left Card: Info
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(4.7), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Suboptimal Initialization scale", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Hyperparameters:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Learning rate = 0.01, weights initialized scaled to near-zero (stddev = 0.001), 5 epochs.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Observations:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - With Batch Norm: Successfully rescales weak signals, training to 97.48% test accuracy.", BODY_FONT, 13, TEXT_GRAY, space_after=4)
    p = tf.add_paragraph()
    style_paragraph(p, "  - No Batch Norm: Fails completely. Signal vanishes through 6 layers; loss stays at 2.3026, test accuracy stuck at 11.35% (vanishing gradients).", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Key Takeaway:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Batch Norm rescales the activations at each layer, maintaining gradient magnitude and preventing vanishing gradients.", BODY_FONT, 13, TEXT_GRAY)

    # Right Card: Image Frame
    add_card(slide, Inches(6.4), Inches(1.6), Inches(6.133), Inches(5.0), CARD_BORDER)
    # Add Image
    img_path = "extracted_plots/task2_exp3_poor_init.png"
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(6.6), Inches(1.8), Inches(5.733), Inches(4.6))


    # ==========================================
    # SLIDE 12: How Batch Normalization Stabilizes Gradients
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "How Batch Normalization Stabilizes Gradients")

    # Card 1: Math equations
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), CARD_BORDER)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.1), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Feedforward Normalization Equations", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=10)

    p = tf.add_paragraph()
    style_paragraph(p, "• Step 1: Mini-batch Mean", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "     μ_B = (1/m) * Σᵢ₌₁ᵐ xᵢ", HEADER_FONT, 20, ACCENT_GOLD, bold=True, space_after=8)

    p = tf.add_paragraph()
    style_paragraph(p, "• Step 2: Mini-batch Variance", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "     σ_B² = (1/m) * Σᵢ₌₁ᵐ (xᵢ - μ_B)²", HEADER_FONT, 20, ACCENT_GOLD, bold=True, space_after=8)

    p = tf.add_paragraph()
    style_paragraph(p, "• Step 3: Normalize Activation", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "     x̂ᵢ = (xᵢ - μ_B) / √(σ_B² + ε)", HEADER_FONT, 20, ACCENT_GOLD, bold=True, space_after=8)

    p = tf.add_paragraph()
    style_paragraph(p, "• Step 4: Scale and Shift (Learnable)", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "     yᵢ = γ * x̂ᵢ + β", HEADER_FONT, 20, ACCENT_GOLD, bold=True)

    # Card 2: Why it prevents failures
    add_card(slide, Inches(6.933), Inches(1.6), Inches(5.6), Inches(5.0), BORDER_SUBTLE)
    box2 = slide.shapes.add_textbox(Inches(7.183), Inches(1.85), Inches(5.1), Inches(4.5))
    tf = box2.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Scale Invariance Intuition", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Mathematical Scale Invariance:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Because we divide by the standard deviation, scaling the weights by any factor does not change the output of the normalization layer. This stabilizes gradient flow.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Preserving Representation Capacity (γ and β):", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Learnable scale (γ) and shift (β) parameters let the network restore the original distribution if it is optimal for learning.", BODY_FONT, 13, TEXT_GRAY, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Smoother Loss Landscape:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Standardizing intermediate layers prevents extreme gradient fluctuations, leading to a much smoother optimization path.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 13: Summary of Empirical Findings (TABLE!)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Summary of Empirical Findings")

    # Native PPTX Table in the middle
    rows, cols = 4, 4
    left = Inches(1.5)
    top = Inches(1.8)
    width = Inches(10.333)
    height = Inches(3.2)

    table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # Column Widths
    table.columns[0].width = Inches(3.5)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(2.5)
    table.columns[3].width = Inches(2.533)

    # Table Contents
    data = [
        ["Experiment", "Metric", "No Batch Norm (Baseline)", "With Batch Norm"],
        ["Standard Training (LR=0.01)", "Test Accuracy", "92.83%", "97.10% (Trained)"],
        ["High Learning Rate Stress Test (LR=0.2)", "Test Accuracy", "11.35% (Diverged)", "98.24% (Trained)"],
        ["Suboptimal Initialization (σ=0.001)", "Test Accuracy", "11.35% (Vanished)", "97.48% (Trained)"]
    ]

    for r_idx, row in enumerate(data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            
            # Format paragraph
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            
            # Formatting styles
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = TABLE_HEADER_BG
                style_paragraph(p, val, HEADER_FONT, 15, TEXT_WHITE, bold=True, space_after=0)
            else:
                cell.fill.solid()
                if r_idx % 2 == 1:
                    cell.fill.fore_color.rgb = RGBColor(26, 32, 44)
                else:
                    cell.fill.fore_color.rgb = RGBColor(16, 22, 34)
                
                # Check if BN column for bold highlight
                is_bn_col = (c_idx == 3)
                txt_color = ACCENT_GOLD if (is_bn_col and r_idx > 0) else TEXT_GRAY
                style_paragraph(p, val, BODY_FONT, 14, txt_color, bold=is_bn_col, space_after=0)

    # Add Takeaway at the bottom
    takeaway_box = slide.shapes.add_textbox(Inches(1.5), Inches(5.3), Inches(10.333), Inches(1.4))
    tf = takeaway_box.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Key Empirical Findings", HEADER_FONT, 16, ACCENT_GOLD, bold=True, space_after=4)
    p = tf.add_paragraph()
    style_paragraph(p, "• Batch Normalization consistently out-performs the baseline in standard settings and successfully rescues the network from extreme training failures (learning rate explosion and weight initialization vanishing).", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 14: Connections to Deep Learning Theory (Layout: 3 Horizontal Stacked Cards)
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Connections to Deep Learning Theory")

    # Card 1: Representation Learning
    add_card(slide, Inches(0.8), Inches(1.6), Inches(11.733), Inches(1.4), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(11.233), Inches(1.2))
    tf1 = box1.text_frame
    tf1.word_wrap = True
    style_paragraph(tf1.paragraphs[0], "• Representation Learning:", HEADER_FONT, 14, ACCENT_GOLD, bold=True, space_after=2)
    p = tf1.add_paragraph()
    style_paragraph(p, "  Character-level LSTMs automatically discover complex spelling, grammar, and language patterns directly from raw sequences without manual, hard-coded rules.", BODY_FONT, 13, TEXT_GRAY)

    # Card 2: Initialization (Highlighted)
    add_card(slide, Inches(0.8), Inches(3.2), Inches(11.733), Inches(1.4), CARD_BORDER)
    box2 = slide.shapes.add_textbox(Inches(1.05), Inches(3.3), Inches(11.233), Inches(1.2))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "• Weight Initialization Dynamics:", HEADER_FONT, 14, ACCENT_GOLD, bold=True, space_after=2)
    p = tf2.add_paragraph()
    style_paragraph(p, "  Kaiming initialization works well under normal conditions, but is highly sensitive to depth. Batch Norm relaxes this scale dependency by dynamically adjusting variance.", BODY_FONT, 13, TEXT_GRAY)

    # Card 3: Optimization Landscapes
    add_card(slide, Inches(0.8), Inches(4.8), Inches(11.733), Inches(1.4), BORDER_SUBTLE)
    box3 = slide.shapes.add_textbox(Inches(1.05), Inches(4.9), Inches(11.233), Inches(1.2))
    tf3 = box3.text_frame
    tf3.word_wrap = True
    style_paragraph(tf3.paragraphs[0], "• Optimization landscapes:", HEADER_FONT, 14, ACCENT_GOLD, bold=True, space_after=2)
    p = tf3.add_paragraph()
    style_paragraph(p, "  Deep backpropagation requires gradient stability. Batch Norm smoothens the loss landscape, preventing gradient explosion and allowing for higher learning rates.", BODY_FONT, 13, TEXT_GRAY)


    # ==========================================
    # SLIDE 15: Conclusion and Q&A
    # ==========================================
    slide = prs.slides.add_slide(slide_layout)
    add_slide_header(slide, "Conclusion and Q&A")

    # Card 1: Summary points
    add_card(slide, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.0), BORDER_SUBTLE)
    box1 = slide.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.1), Inches(4.5))
    tf = box1.text_frame
    tf.word_wrap = True
    style_paragraph(tf.paragraphs[0], "Key Summary Takeaways", HEADER_FONT, 18, ACCENT_GOLD, bold=True, space_after=12)

    p = tf.add_paragraph()
    style_paragraph(p, "• Task 1 Sequence Modeling:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Character-level LSTMs successfully capture the structural, orthographical, and grammatical nuances of different corpuses.", BODY_FONT, 13, TEXT_GRAY, space_after=16)

    p = tf.add_paragraph()
    style_paragraph(p, "• Task 2 Normalization:", BODY_FONT, 14, TEXT_WHITE, bold=True, space_after=2)
    p = tf.add_paragraph()
    style_paragraph(p, "  - Batch Normalization is a critical architectural component for deep networks, providing optimization speedup and stability under stress.", BODY_FONT, 13, TEXT_GRAY)

    # Card 2: Thank you panel (Highlighted)
    add_card(slide, Inches(6.933), Inches(1.6), Inches(5.6), Inches(5.0), CARD_BORDER)
    box2 = slide.shapes.add_textbox(Inches(7.183), Inches(1.85), Inches(5.1), Inches(4.5))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    style_paragraph(tf2.paragraphs[0], "Thank you! Questions?", HEADER_FONT, 22, ACCENT_GOLD, bold=True, space_after=12)
    
    p = tf2.add_paragraph()
    style_paragraph(p, "We are ready for your questions, Sir.", BODY_FONT, 14, TEXT_WHITE, italic=True, space_after=14)

    p = tf2.add_paragraph()
    style_paragraph(p, "Presenters Panel (Group 3):", BODY_FONT, 13, TEXT_WHITE, bold=True, space_after=6)

    presenters = [
        "MD Kaif Molla",
        "Arhan Das",
        "Sumit Akhuli",
        "Shiva Gupta",
        "Sarthak Mishra",
        "Netram Faran",
        "Aditya Prasad"
    ]
    for pres in presenters:
        p = tf2.add_paragraph()
        style_paragraph(p, "  • " + pres, BODY_FONT, 12, TEXT_GRAY, space_after=3)

    # Save presentation
    prs.save("presentation.pptx")
    print("Presentation successfully saved to presentation.pptx!")

if __name__ == "__main__":
    create_presentation()
