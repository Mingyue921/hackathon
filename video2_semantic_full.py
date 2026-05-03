from manim import *

class SemanticFull(Scene):
    def construct(self):
        # 标题
        title = Text("Automated Evidence Discovery: Semantic Cueing", font_size=26, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # ========== 左栏：步骤1 + PDF 截图 ==========
        s1 = Text("Step 1: Load Legal Document", font_size=20, color=YELLOW)
        pdf_img = ImageMobject("thailand_pdpa_sample.png")
        pdf_img.scale_to_fit_width(4.5)             # 缩小宽度，适应左栏
        file_label = Text("thailand_pdpa_2019.pdf", font_size=14, color=WHITE)

        left_col = Group(s1, pdf_img, file_label).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        left_col.scale(0.9)                          # 微调，防止过高

        # ========== 右栏：步骤2~4 ==========
        s2 = Text("Step 2: Extract Text Passages", font_size=20, color=YELLOW)
        passage = Text(
            '"The cross-border transfer of personal data\n'
            'shall be permitted only if the destination country\n'
            'has adequate data protection standards..."',
            font_size=14, color=WHITE, line_spacing=1.2
        )

        s3 = Text("Step 3: Semantic Pattern Matching", font_size=20, color=YELLOW)
        hit1 = Text("⚡ MATCH: 'adequate data protection standards'", font_size=15, color=RED)
        hit2 = Text("⚡ MATCH: 'cross-border transfer...permitted only if'", font_size=15, color=RED)

        s4 = Text("Step 4: Classify to Pillar 6 Indicator", font_size=20, color=YELLOW)
        classify = Text("→ Pillar 6.4: Conditional Flow Regime", font_size=18, color=ORANGE)

        right_col = Group(
            s2, passage,
            s3, hit1, hit2,
            s4, classify
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_col.scale(0.85)

        # ========== 并排布局 ==========
        columns = Group(left_col, right_col).arrange(RIGHT, buff=1.2)
        columns.next_to(title, DOWN, buff=0.5)
        columns.move_to(ORIGIN)   # 整体居中

        # ========== 动画 ==========
        # 左栏动画
        self.play(Write(s1))
        self.play(FadeIn(pdf_img), Write(file_label))
        self.wait(0.5)

        # 右栏动画（在左栏显示后依次出现）
        self.play(Write(s2))
        self.play(FadeIn(passage, shift=DOWN))
        self.wait(0.5)
        self.play(Write(s3))
        self.play(Write(hit1))
        self.play(Write(hit2))
        self.wait(0.5)
        self.play(Write(s4))
        self.play(FadeIn(classify, shift=RIGHT))
        self.wait(2)