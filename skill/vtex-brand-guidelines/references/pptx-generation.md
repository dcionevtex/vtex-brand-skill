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

FONT_PRIMARY  = 'VTEX Trust'
FONT_FALLBACK = 'Calibri'

SLIDE_WIDTH  = Inches(13.33)
SLIDE_HEIGHT = Inches(7.5)

MARGIN_LEFT   = Inches(0.8)
MARGIN_TOP    = Inches(0.8)
MARGIN_RIGHT  = Inches(0.8)
CONTENT_WIDTH = SLIDE_WIDTH - Inches(1.6)
```

---

## Helper: Add Logo (bundled official assets)

The skill bundles the official VTEX logo in `assets/` (see `references/logo-guidelines.md`).
Use the PNG variants — python-pptx cannot embed SVG. If PNGs are missing, run
`python assets/generate-pngs.py` first.

```python
import os

SKILL_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_PINK  = os.path.join(SKILL_DIR, "assets", "vtex-logo-rebel-pink.png")
LOGO_WHITE = os.path.join(SKILL_DIR, "assets", "vtex-logo-white.png")
LOGO_BLACK = os.path.join(SKILL_DIR, "assets", "vtex-logo-serious-black.png")

def add_logo(slide, logo_path=None,
             left=Inches(0.3), top=Inches(0.15),
             height=Inches(0.5)):
    if logo_path is None:
        logo_path = LOGO_PINK
    if os.path.exists(logo_path):
        slide.shapes.add_picture(logo_path, left, top, height=height)
    else:
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

**Variant rule:** cover/section/closing on Serious Black or Rebel Pink -> `LOGO_WHITE`; content/data on white or Soft Blue -> `LOGO_PINK`.

---

## Tips

- **Logo:** Use the bundled assets in `assets/` (run `python assets/generate-pngs.py` once to create the PNGs). Pass `LOGO_WHITE` on dark/pink slides. The text placeholder is for draft use only.
- **Charts:** Set the first data series fill to `REBEL_PINK`, subsequent series to `SERIOUS_GRAY`, `COOL_GRAY`, `BUBBLE_GUM` in that order.
- **Tables:** Use `REBEL_PINK` for header row fill, `SERIOUS_BLACK` text on pink, `WINTER_GRAY` for row dividers.

For full slide template functions (cover, section, content, quote, closing), see the complete file in the sandbox or the `.patch` delivered earlier.
