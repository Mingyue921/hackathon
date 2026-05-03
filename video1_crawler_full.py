from manim import *

class CrawlerFull(Scene):
    def construct(self):
        title = Text("Automated Evidence Discovery: Navigation Prompt", font_size=26, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        s1 = Text("Step 1: Seed URL", font_size=20, color=YELLOW)
        url = Text("https://www.mps.gov.vn/legal-database", font_size=16, color=WHITE)

        s2 = Text("Step 2: Crawl All Subpages", font_size=20, color=YELLOW)
        pages = VGroup(
            Text("• /page/law-on-cybersecurity", font_size=14, color=WHITE),
            Text("• /page/decree-53", font_size=14, color=WHITE),
            Text("• /page/data-protection", font_size=14, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        s3 = Text("Step 3: Keyword Filtering", font_size=20, color=YELLOW)
        keywords = VGroup(
            Text("'data localization'", font_size=15, color=GREEN),
            Text("'cross-border data'", font_size=15, color=GREEN),
            Text("'server in-country'", font_size=15, color=GREEN),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        s4 = Text("Step 4: Document Match", font_size=20, color=YELLOW)
        result = Text("✓ Law on Cybersecurity, Article 26", font_size=16, color=RED)
        mapping = Text("→ Pillar 6.1 & 6.2: Local Storage & Processing", font_size=16, color=ORANGE)

        content = VGroup(
            s1, url,
            s2, pages,
            s3, keywords,
            s4, result, mapping
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        content.next_to(title, DOWN, buff=0.3)

        self.play(Write(s1))
        self.play(FadeIn(url, shift=DOWN))
        self.wait(0.5)
        self.play(Write(s2))
        for p in pages:
            self.play(FadeIn(p, shift=RIGHT), run_time=0.2)
        self.wait(0.5)
        self.play(Write(s3))
        self.play(FadeIn(keywords, shift=DOWN))
        self.wait(0.5)
        self.play(Write(s4))
        self.play(FadeIn(result, shift=RIGHT))
        self.wait(0.5)
        self.play(Write(mapping))
        self.wait(2)