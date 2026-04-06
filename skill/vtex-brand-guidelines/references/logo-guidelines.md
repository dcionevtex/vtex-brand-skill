# VTEX Logo Guidelines

Source: [brand.vtex.com](https://brand.vtex.com/)

---

## Logo Assets

Official logo files available at:
- **Figma:** figma.com/design/VNkQ2Zmvn98cSyY9HZQNQZ/VTEX-Brand-Assets
- **Download:** brand.vtex.com → Logo & Tagline → Logo-Tagline-Composable-and-Complete.zip

The logo combines the VTEX icon + wordmark. Both must appear together in all cases except digital avatars.

---

## Color Variants

| Variant | Background | When to use |
|---|---|---|
| Rebel Pink (`#F71963`) | Light backgrounds | Primary — preferred for brand recognition |
| White (`#FFFFFF`) | Dark backgrounds | Covers, dark slides, Serious Black backgrounds |
| Serious Black (`#142032`) | Light backgrounds | When pink is not appropriate; use sparingly |

Never use the logo in any other color (no grays, no gradients, no Bubble Gum Pink).

---

## Minimum Size Requirements

| Medium | Minimum size |
|---|---|
| Digital screens | 60px height |
| Print | 1cm (0.78 inches) height |

Do not render the logo below these thresholds — it becomes illegible and off-brand.

---

## Clearspace

Maintain a protected margin around the logo equal to the **vertical axis width of the letter "V" in VTEX** on all four sides.

In practice: if the logo is 100px tall, the clearspace should be approximately 15–20px on each side.

Never place text, images, or other elements inside this clearspace zone.

---

## Placement Rules

| Position | Rule |
|---|---|
| Top-left | Preferred for all compositions |
| Bottom-left | Permitted |
| Bottom-right | Restricted — footers and closing slides only |
| Top-right | Avoid |
| Center | Avoid (exception: avatar/profile contexts) |

In presentations: place the logo top-left on cover, section dividers, and content slides. Use bottom-left on the closing slide as an alternative.

---

## What to Do

- Prioritize Rebel Pink logo on light backgrounds for maximum brand recognition
- Maintain clearspace in all applications
- Use the full logo (icon + wordmark) at all times
- For digital avatars (profile pictures, app icons): icon-only version is acceptable

---

## What Never to Do

| Prohibition | Notes |
|---|---|
| Icon without wordmark | Only exception: digital avatars |
| Distort proportions | Never stretch or squash |
| Rotate | Always horizontal |
| Reposition icon relative to wordmark | Fixed arrangement |
| Add shadows, glows, bevels, embossing | Clean flat version only |
| Place inside geometric shapes | No boxes, circles, badges |
| Use as texture or pattern | Not a repeating element |
| Place on unclear or busy backgrounds | Ensure contrast and clearspace |
| Use on items subject to wear | No floors, mats, disposable items |
| Use outline versions | Filled versions only |

---

## Placeholder for Documents Without Logo File

When generating a document and the logo file is unavailable, use this HTML/CSS placeholder:

```html
<div style="
  display: inline-flex;
  align-items: center;
  background: #F71963;
  padding: 6px 14px;
  border-radius: 2px;
">
  <span style="
    color: white;
    font-family: 'VTEX Trust', sans-serif;
    font-weight: 700;
    font-size: 18px;
    letter-spacing: 0.05em;
  ">VTEX</span>
</div>
```

For python-pptx, when the logo PNG/SVG is unavailable:

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def add_logo_placeholder(slide, left=Inches(0.3), top=Inches(0.2)):
    """Add a text-based VTEX logo placeholder when image file is unavailable."""
    txBox = slide.shapes.add_textbox(left, top, Inches(1.2), Inches(0.4))
    tf = txBox.text_frame
    tf.text = "VTEX"
    p = tf.paragraphs[0]
    run = p.runs[0]
    run.font.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(0xF7, 0x19, 0x63)
    run.font.name = 'VTEX Trust'
```

---

## Logo in Partnerships

When placing the VTEX logo alongside a partner logo:

- Spacing between logos derives from the width of the VTEX symbol (icon)
- Use only Rebel Pink or White VTEX logo — never Serious Black in a co-brand context
- Prevent partner logos from mimicking VTEX visual style
- VTEX logo and partner logo should be visually equal in size (not dominant on either side)
