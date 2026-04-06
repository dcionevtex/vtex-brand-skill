# VTEX python-pptx Generation Guide

Complete reference for generating `.pptx` files following VTEX brand guidelines.

---

## Setup

```bash
pip install python-pptx
```

---

## Brand Constants Module

Save this as `vtex_brand.py` or inline at the top of any generation script:

```python
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt, Emu

# ── Colors ────────────────────────────────────────────────────────────────────
REBEL_PINK    = RGBColor(0xF7, 0x19, 0x63)
SERIOUS_BLACK = RGBColor(0x14, 0x20, 0x32)
PLAIN_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
SOFT_BLUE     = RGBColor(0xF5, 0xF9, 0xFF)
SOFT_PINK     = RGBColor(0xFF, 0xF3, 0xF6)
YOGURT_PINK   = RGBColor(0xFF, 0xE0, 0xEF)
BUBBLE_GUM    = RGBColor(0xFF, 0xC4, 0xDD)
WINTER_GRAY   = RGBColor(0xE7, 0xE9, 0xEE)
COOL_GRAY     = RGBColor(0xA1, 0xA8, 0xB7)
SERIOUS_GRAY  = RGBColor(0x5B, 0x6E, 0x84)

# ── Fonts ─────────────────────────────────────────────────────────────────────
FONT_PRIMARY  = 'VTEX Trust'
FONT_FALLBACK = 'Calibri'  # Use when VTEX Trust is not installed

# ── Slide dimensions: 16:9 widescreen ────────────────────────────────────────
SLIDE_WIDTH  = Inches(13.33)
SLIDE_HEIGHT = Inches(7.5)

# ── Common margins ────────────────────────────────────────────────────────────
MARGIN_LEFT   = Inches(0.8)
MARGIN_TOP    = Inches(0.8)
MARGIN_RIGHT  = Inches(0.8)
CONTENT_WIDTH = SLIDE_WIDTH - Inches(1.6)
```

---

## Presentation Initializer

```python
from pptx import Presentation

def create_vtex_presentation():
    """Create a new VTEX-branded presentation with correct dimensions."""
    prs = Presentation()
    prs.slide_width  = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    return prs
```

---

## Helper: Set Slide Background Color

```python
from pptx.oxml.ns import qn
from lxml import etree

def set_slide_background(slide, color: RGBColor):
    """Fill a slide background with a solid color."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color
```

---

## Helper: Add Text Box

```python
def add_text(slide, text, left, top, width, height,
             font_name=FONT_PRIMARY, font_size=24,
             color=SERIOUS_BLACK, bold=False, italic=False,
             align='left'):
    from pptx.enum.text import PP_ALIGN

    align_map = {
        'left':   PP_ALIGN.LEFT,
        'center': PP_ALIGN.CENTER,
        'right':  PP_ALIGN.RIGHT,
    }

    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.text = text

    for para in tf.paragraphs:
        para.alignment = align_map.get(align, PP_ALIGN.LEFT)
        for run in para.runs:
            run.font.name   = font_name
            run.font.size   = Pt(font_size)
            run.font.color.rgb = color
            run.font.bold   = bold
            run.font.italic = italic

    return txBox
```

---

## Helper: Add Logo Placeholder

```python
def add_logo(slide, logo_path=None,
             left=Inches(0.3), top=Inches(0.15),
             height=Inches(0.5)):
    """
    Add the VTEX logo to a slide.
    If logo_path is provided, inserts the image file.
    Otherwise, inserts a pink text placeholder.
    """
    if logo_path:
        slide.shapes.add_picture(logo_path, left, top, height=height)
    else:
        # Text placeholder — replace with real logo before distribution
        width = Inches(1.4)
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.text = "VTEX"
        run = tf.paragraphs[0].runs[0]
        run.font.bold  = True
        run.font.name  = FONT_PRIMARY
        run.font.size  = Pt(20)
        run.font.color.rgb = REBEL_PINK
```

---

## Helper: Add Pink Accent Bar

```python
def add_accent_bar(slide, orientation='horizontal',
                   position='top', thickness=Inches(0.06)):
    """Add a Rebel Pink accent line to a slide."""
    from pptx.util import Inches

    if orientation == 'horizontal':
        if position == 'top':
            left, top = Inches(0), Inches(0)
            width, height = SLIDE_WIDTH, thickness
        else:  # bottom
            left = Inches(0)
            top  = SLIDE_HEIGHT - thickness
            width, height = SLIDE_WIDTH, thickness
    else:  # vertical left bar
        left, top = Inches(0), Inches(0)
        width, height = thickness, SLIDE_HEIGHT

    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = REBEL_PINK
    shape.line.fill.background()  # no border
    return shape
```

---

## Slide Templates

### Cover Slide

```python
def add_cover_slide(prs, title, subtitle=None, logo_path=None):
    """
    Dark cover: Serious Black background, white title,
    pink accent bar at bottom, logo top-left.
    """
    slide_layout = prs.slide_layouts[6]  # blank layout
    slide = prs.slides.add_slide(slide_layout)

    # Background
    set_slide_background(slide, SERIOUS_BLACK)

    # Pink accent bar (bottom)
    add_accent_bar(slide, orientation='horizontal', position='bottom')

    # Logo
    add_logo(slide, logo_path)

    # Title
    add_text(
        slide, title,
        left=MARGIN_LEFT,
        top=Inches(2.2),
        width=CONTENT_WIDTH,
        height=Inches(2.0),
        font_size=48,
        color=PLAIN_WHITE,
        bold=False,
    )

    # Subtitle
    if subtitle:
        add_text(
            slide, subtitle,
            left=MARGIN_LEFT,
            top=Inches(4.4),
            width=CONTENT_WIDTH,
            height=Inches(0.8),
            font_size=20,
            color=COOL_GRAY,
        )

    return slide
```

### Section Divider Slide

```python
def add_section_slide(prs, section_title, logo_path=None):
    """
    Rebel Pink background, white centered title.
    """
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    set_slide_background(slide, REBEL_PINK)
    add_logo(slide, logo_path)

    add_text(
        slide, section_title,
        left=MARGIN_LEFT,
        top=Inches(2.8),
        width=CONTENT_WIDTH,
        height=Inches(1.8),
        font_size=44,
        color=PLAIN_WHITE,
        bold=False,
        align='left',
    )

    return slide
```

### Content Slide (Title + Body)

```python
def add_content_slide(prs, title, body_lines: list[str], logo_path=None):
    """
    Soft Blue background, dark title, body as bullet list.
    """
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    set_slide_background(slide, SOFT_BLUE)
    add_logo(slide, logo_path)

    # Top pink accent bar
    add_accent_bar(slide, orientation='horizontal', position='top', thickness=Inches(0.04))

    # Title
    add_text(
        slide, title,
        left=MARGIN_LEFT,
        top=Inches(0.9),
        width=CONTENT_WIDTH,
        height=Inches(0.9),
        font_size=32,
        color=SERIOUS_BLACK,
    )

    # Body text
    body_text = '\n'.join(f'• {line}' for line in body_lines)
    add_text(
        slide, body_text,
        left=MARGIN_LEFT,
        top=Inches(2.0),
        width=CONTENT_WIDTH,
        height=Inches(4.5),
        font_size=18,
        color=SERIOUS_GRAY,
    )

    return slide
```

### Quote / Callout Slide

```python
def add_quote_slide(prs, quote, attribution=None, logo_path=None):
    """
    Soft Pink background, large quote in Serious Black.
    """
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    set_slide_background(slide, SOFT_PINK)
    add_logo(slide, logo_path)

    add_text(
        slide, f'"{quote}"',
        left=MARGIN_LEFT,
        top=Inches(1.8),
        width=CONTENT_WIDTH,
        height=Inches(3.5),
        font_size=28,
        color=SERIOUS_BLACK,
        italic=True,
    )

    if attribution:
        add_text(
            slide, f'— {attribution}',
            left=MARGIN_LEFT,
            top=Inches(5.5),
            width=CONTENT_WIDTH,
            height=Inches(0.6),
            font_size=16,
            color=SERIOUS_GRAY,
        )

    return slide
```

### Closing Slide

```python
def add_closing_slide(prs, headline, cta=None, logo_path=None):
    """
    Mirror of cover: dark background, pink accent, CTA.
    """
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    set_slide_background(slide, SERIOUS_BLACK)
    add_accent_bar(slide, orientation='vertical', thickness=Inches(0.15))
    add_logo(slide, logo_path,
             left=Inches(0.3),
             top=SLIDE_HEIGHT - Inches(1.0),
             height=Inches(0.5))

    add_text(
        slide, headline,
        left=Inches(1.2),
        top=Inches(2.5),
        width=Inches(10.0),
        height=Inches(1.8),
        font_size=44,
        color=PLAIN_WHITE,
    )

    if cta:
        add_text(
            slide, cta,
            left=Inches(1.2),
            top=Inches(4.5),
            width=Inches(6.0),
            height=Inches(0.6),
            font_size=18,
            color=REBEL_PINK,
        )

    return slide
```

---

## Complete Example: Build a Full Deck

```python
from pptx import Presentation

def build_vtex_deck(output_path: str, logo_path: str = None):
    prs = create_vtex_presentation()

    add_cover_slide(
        prs,
        title="Composable Commerce at Scale",
        subtitle="Enterprise Architecture Review — Q2 2026",
        logo_path=logo_path,
    )

    add_section_slide(prs, "The Challenge", logo_path=logo_path)

    add_content_slide(
        prs,
        title="Current State",
        body_lines=[
            "Monolithic platform with 18-month release cycles",
            "3 separate systems for B2C, B2B, and Marketplace",
            "60% of dev time spent on infrastructure, not features",
        ],
        logo_path=logo_path,
    )

    add_section_slide(prs, "The Approach", logo_path=logo_path)

    add_content_slide(
        prs,
        title="Composable Architecture Principles",
        body_lines=[
            "API-first: every capability exposed as an API",
            "Headless frontend: deploy independently",
            "VTEX IO for managed extensions",
            "Single OMS for all channels",
        ],
        logo_path=logo_path,
    )

    add_quote_slide(
        prs,
        quote="We went from 8-week sprints to deploying twice a week.",
        attribution="CTO, Leading Brazilian Retailer",
        logo_path=logo_path,
    )

    add_closing_slide(
        prs,
        headline="Ready to architect the next chapter?",
        cta="vtex.com/enterprise",
        logo_path=logo_path,
    )

    prs.save(output_path)
    print(f"Saved: {output_path}")

# Run
build_vtex_deck("vtex_presentation.pptx")
```

---

## Tips

- **Font availability:** The generated .pptx will show the correct font only if VTEX Trust is installed on the machine opening the file. Include a note in your README or email when distributing.
- **Logo:** Always use the `.png` or `.svg` version from the official brand site. The text placeholder is for draft use only.
- **Images:** Add via `slide.shapes.add_picture(path, left, top, width, height)`. Use high-res images (min 1920×1080 for full-bleed backgrounds).
- **Tables:** Use `REBEL_PINK` for header row fill, `SERIOUS_BLACK` text on pink, `WINTER_GRAY` for row dividers.
- **Charts:** Set the first data series fill to `REBEL_PINK`, subsequent series to `SERIOUS_GRAY`, `COOL_GRAY`, `BUBBLE_GUM` in that order.
