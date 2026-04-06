# VTEX python-pptx Generation Guide

Complete reference for generating `.pptx` files following VTEX brand guidelines.

---

## Setup

```bash
pip install python-pptx
```

---

## Brand Constants Module

```python
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

# Colors
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

# Font
FONT_PRIMARY  = 'VTEX Trust'
FONT_FALLBACK = 'Calibri'

# Slide dimensions: 16:9 widescreen
SLIDE_WIDTH  = Inches(13.33)
SLIDE_HEIGHT = Inches(7.5)

# Margins
MARGIN_LEFT   = Inches(0.8)
CONTENT_WIDTH = SLIDE_WIDTH - Inches(1.6)
```

---

## Core Helpers

```python
from pptx import Presentation

def create_vtex_presentation():
    prs = Presentation()
    prs.slide_width  = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    return prs

def set_slide_background(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_text(slide, text, left, top, width, height,
            font_name=FONT_PRIMARY, font_size=24,
            color=SERIOUS_BLACK, bold=False, italic=False, align='left'):
    from pptx.enum.text import PP_ALIGN
    align_map = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}
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

def add_logo(slide, logo_path=None, left=Inches(0.3), top=Inches(0.15), height=Inches(0.5)):
    if logo_path:
        slide.shapes.add_picture(logo_path, left, top, height=height)
    else:
        txBox = slide.shapes.add_textbox(left, top, Inches(1.4), height)
        tf = txBox.text_frame
        tf.text = "VTEX"
        run = tf.paragraphs[0].runs[0]
        run.font.bold  = True
        run.font.name  = FONT_PRIMARY
        run.font.size  = Pt(20)
        run.font.color.rgb = REBEL_PINK

def add_accent_bar(slide, orientation='horizontal', position='top', thickness=Inches(0.06)):
    if orientation == 'horizontal':
        left = Inches(0)
        top  = Inches(0) if position == 'top' else SLIDE_HEIGHT - thickness
        width, height = SLIDE_WIDTH, thickness
    else:
        left, top = Inches(0), Inches(0)
        width, height = thickness, SLIDE_HEIGHT
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = REBEL_PINK
    shape.line.fill.background()
    return shape
```

---

## Slide Templates

### Cover Slide

```python
def add_cover_slide(prs, title, subtitle=None, logo_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, SERIOUS_BLACK)
    add_accent_bar(slide, position='bottom')
    add_logo(slide, logo_path)
    add_text(slide, title,
             left=MARGIN_LEFT, top=Inches(2.2),
             width=CONTENT_WIDTH, height=Inches(2.0),
             font_size=48, color=PLAIN_WHITE)
    if subtitle:
        add_text(slide, subtitle,
                 left=MARGIN_LEFT, top=Inches(4.4),
                 width=CONTENT_WIDTH, height=Inches(0.8),
                 font_size=20, color=COOL_GRAY)
    return slide
```

### Section Divider

```python
def add_section_slide(prs, section_title, logo_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, REBEL_PINK)
    add_logo(slide, logo_path)
    add_text(slide, section_title,
             left=MARGIN_LEFT, top=Inches(2.8),
             width=CONTENT_WIDTH, height=Inches(1.8),
             font_size=44, color=PLAIN_WHITE)
    return slide
```

### Content Slide

```python
def add_content_slide(prs, title, body_lines, logo_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, SOFT_BLUE)
    add_logo(slide, logo_path)
    add_accent_bar(slide, position='top', thickness=Inches(0.04))
    add_text(slide, title,
             left=MARGIN_LEFT, top=Inches(0.9),
             width=CONTENT_WIDTH, height=Inches(0.9),
             font_size=32, color=SERIOUS_BLACK)
    body_text = '\n'.join(f'• {line}' for line in body_lines)
    add_text(slide, body_text,
             left=MARGIN_LEFT, top=Inches(2.0),
             width=CONTENT_WIDTH, height=Inches(4.5),
             font_size=18, color=SERIOUS_GRAY)
    return slide
```

### Quote Slide

```python
def add_quote_slide(prs, quote, attribution=None, logo_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, SOFT_PINK)
    add_logo(slide, logo_path)
    add_text(slide, f'"{quote}"',
             left=MARGIN_LEFT, top=Inches(1.8),
             width=CONTENT_WIDTH, height=Inches(3.5),
             font_size=28, color=SERIOUS_BLACK, italic=True)
    if attribution:
        add_text(slide, f'— {attribution}',
                 left=MARGIN_LEFT, top=Inches(5.5),
                 width=CONTENT_WIDTH, height=Inches(0.6),
                 font_size=16, color=SERIOUS_GRAY)
    return slide
```

### Closing Slide

```python
def add_closing_slide(prs, headline, cta=None, logo_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, SERIOUS_BLACK)
    add_accent_bar(slide, orientation='vertical', thickness=Inches(0.15))
    add_logo(slide, logo_path,
             left=Inches(0.3),
             top=SLIDE_HEIGHT - Inches(1.0),
             height=Inches(0.5))
    add_text(slide, headline,
             left=Inches(1.2), top=Inches(2.5),
             width=Inches(10.0), height=Inches(1.8),
             font_size=44, color=PLAIN_WHITE)
    if cta:
        add_text(slide, cta,
                 left=Inches(1.2), top=Inches(4.5),
                 width=Inches(6.0), height=Inches(0.6),
                 font_size=18, color=REBEL_PINK)
    return slide
```

---

## Logo Variants by Slide Type

| Slide background | Logo to use |
|---|---|
| Serious Black (`#142032`) | White logo |
| Rebel Pink (`#F71963`) | White logo |
| Soft Blue (`#F5F9FF`) | Rebel Pink logo |
| Plain White (`#FFFFFF`) | Rebel Pink logo |
| Soft Pink (`#FFF3F6`) | Rebel Pink logo |

```python
# Pattern: pass the right logo per slide
LOGO_REBEL = 'path/to/VTEX-Logo-Rebel.png'
LOGO_WHITE = 'path/to/VTEX-Logo-White.png'

add_cover_slide(prs, "Title", logo_path=LOGO_WHITE)    # dark bg
add_section_slide(prs, "Section", logo_path=LOGO_WHITE) # pink bg
add_content_slide(prs, "Title", [...], logo_path=LOGO_REBEL) # light bg
```

---

## Tips

- **Font:** VTEX Trust must be installed on the machine opening the file. Fallback is Calibri.
- **Logo files:** Download from `brand.vtex.com` → Logo & Tagline ZIP. Use Digital/PNG variants.
- **Images:** `slide.shapes.add_picture(path, left, top, width, height)` — min 1920×1080 for full-bleed.
- **Tables:** REBEL_PINK header fill, SERIOUS_BLACK text on pink, WINTER_GRAY row dividers.
- **Charts:** First series = REBEL_PINK, subsequent = SERIOUS_GRAY, COOL_GRAY, BUBBLE_GUM.
