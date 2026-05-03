from manim import *

class PDFExtractionFull(Scene):
    def construct(self):
        # 标题
        title = Text("Automated Evidence Discovery: PDF Hierarchy Extraction", font_size=26, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # ========== 左栏：步骤1 + PDF 截图 ==========
        s1 = Text("Step 1: Input — Scanned Legal PDF", font_size=20, color=YELLOW)
        pdf_img = ImageMobject("vietnam_law_sample.png")
        pdf_img.scale_to_fit_width(4.5)
        file_label = Text("Vietnam_Law_on_Cybersecurity_2018.pdf\nPages 45–52 (scanned)", font_size=13, color=WHITE)

        left_col = Group(s1, pdf_img, file_label).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        left_col.scale(0.9)

        # ========== 右栏：步骤2~4 ==========
        s2 = Text("Step 2: OCR + Structure Parsing (Docling)", font_size=20, color=YELLOW)
        parse_items = Group(
            Text("• Detect text blocks via OCR", font_size=14, color=WHITE),
            Text("• Identify headings: Chapter, Article, Clause", font_size=14, color=WHITE),
            Text("• Preserve hierarchy as Markdown", font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        s3 = Text("Step 3: Structured Output (Markdown)", font_size=20, color=YELLOW)
        output = Text(
            "## Article 26: Data Localization\n"
            "### Clause 1\n"
            "Data must be stored on servers located in Vietnam.\n"
            "### Clause 2\n"
            "Foreign service providers must establish a branch office.",
            font_size=13, color=GREEN, line_spacing=1.1
        )

        s4 = Text("Step 4: Map to Pillar 6 Indicators", font_size=20, color=YELLOW)
        map_result = Group(
            Text("Clause 1 → Pillar 6.2: Local Storage", font_size=15, color=ORANGE),
            Text("Clause 2 → Pillar 6.1: Local Processing", font_size=15, color=ORANGE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        right_col = Group(
            s2, parse_items,
            s3, output,
            s4, map_result
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_col.scale(0.85)

        # ========== 并排布局 ==========
        columns = Group(left_col, right_col).arrange(RIGHT, buff=1.2)
        columns.next_to(title, DOWN, buff=0.5)
        columns.move_to(ORIGIN)

        # ========== 动画 ==========
        # 左栏
        self.play(Write(s1))
        self.play(FadeIn(pdf_img), Write(file_label))
        self.wait(0.5)

        # 右栏
        self.play(Write(s2))
        for item in parse_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.2)
        self.wait(0.5)
        self.play(Write(s3))
        self.play(FadeIn(output, shift=DOWN))
        self.wait(1)
        self.play(Write(s4))
        self.play(FadeIn(map_result, shift=RIGHT))
        self.wait(2)