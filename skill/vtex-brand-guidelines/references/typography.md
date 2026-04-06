# VTEX Typography System

Source: [brand.vtex.com](https://brand.vtex.com/)

---

## Typeface

**VTEX Trust** — custom typeface unique to the brand. Download from the brand site:
- [brand.vtex.com](https://brand.vtex.com/) → Typography section → Google Drive link

**CSS fallback stack:**
```css
font-family: 'VTEX Trust', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

For documents where VTEX Trust is unavailable (e.g., stock python-pptx templates, Google Slides):
- Use **Calibri** or **Inter** as substitutes
- Note in the document: "Uses VTEX Trust font — install before final distribution"

---

## Type Scale

VTEX uses a **1.5 ratio** ("the perfect fifty") for typographic hierarchy.

Example scale with 16px base:

| Level | Multiplier | Size (16px base) | Role |
|---|---|---|---|
| Display | 1.5⁴ | ~81px | Hero headlines, cover titles |
| H1 | 1.5³ | ~54px | Section titles |
| H2 | 1.5² | ~36px | Subsection titles |
| H3 | 1.5¹ | 24px | Card titles, callout headers |
| Body Large | — | 18px | Lead paragraphs |
| Body | — | 16px | Default body text |
| Caption | — | 12–13px | Footnotes, labels, metadata |

In presentations, scale is relative to slide dimensions — maintain clear visual hierarchy with at least a 1.5× step between heading and body.

---

## Line Height (Leading)

| Element | Line height |
|---|---|
| Headings | 100% of font size (tight) |
| Subheadings | 120% of font size |
| Body text | 150% of font size (relaxed) |

```css
h1, h2, h3 { line-height: 1.0; }
h4, h5     { line-height: 1.2; }
p, li      { line-height: 1.5; }
```

---

## Weight Rules

| Use | Weight | Notes |
|---|---|---|
| All titles | Regular (400) | Bold titles are prohibited |
| Body text | Regular (400) default | Bold/italic permitted sparingly for emphasis |
| UI labels | Regular (400) | |
| Data callouts | Regular (400) or medium if available | |

**Never:**
- Use bold for titles or headlines
- Use italics for entire paragraphs
- Use all-caps (UPPERCASE) text

---

## Alignment Rules

| Context | Alignment |
|---|---|
| Default (all text) | Left |
| Website | Left (preferred), center permitted for hero sections |
| Presentations | Left preferred; center permitted for single-line display headlines on cover/divider slides |
| Right alignment | Never |

---

## Spacing Rules

- **Never alter letter spacing (tracking)**  
  VTEX Trust is designed with specific spacing — do not use `letter-spacing` adjustments
- **Baseline grid:** maintain proportional spacing using the 1.5 scale as reference
- **Paragraph spacing:** use spacing-after equal to the line height of the current text size

---

## python-pptx Typography Application

```python
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN

def apply_heading_style(tf, size_pt=36):
    """Apply VTEX heading typography to a text frame."""
    for para in tf.paragraphs:
        para.alignment = PP_ALIGN.LEFT
        for run in para.runs:
            run.font.name = 'VTEX Trust'
            run.font.size = Pt(size_pt)
            run.font.bold = False
            run.font.italic = False
    # Set line spacing to 100% (1.0 multiple)
    from pptx.util import Pt
    from pptx.oxml.ns import qn
    from lxml import etree
    for para in tf.paragraphs:
        pPr = para._pPr
        if pPr is None:
            pPr = para._p.get_or_add_pPr()
        lnSpc = etree.SubElement(pPr, qn('a:lnSpc'))
        spcPct = etree.SubElement(lnSpc, qn('a:spcPct'))
        spcPct.set('val', '100000')  # 100%

def apply_body_style(tf, size_pt=18):
    """Apply VTEX body typography to a text frame."""
    for para in tf.paragraphs:
        para.alignment = PP_ALIGN.LEFT
        for run in para.runs:
            run.font.name = 'VTEX Trust'
            run.font.size = Pt(size_pt)
            run.font.bold = False
```

---

## CSS Implementation

```css
/* VTEX Typography */
body {
  font-family: 'VTEX Trust', system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  text-align: left;
  color: #142032;
}

h1 { font-size: 3.375rem; line-height: 1.0; font-weight: 400; }
h2 { font-size: 2.25rem;  line-height: 1.0; font-weight: 400; }
h3 { font-size: 1.5rem;   line-height: 1.2; font-weight: 400; }
h4 { font-size: 1rem;     line-height: 1.2; font-weight: 400; }
p  { font-size: 1rem;     line-height: 1.5; }

/* Never bold titles */
h1, h2, h3 { font-weight: 400 !important; }

/* Never use uppercase */
* { text-transform: none !important; }
```

---

## Common Mistakes to Avoid

| Wrong | Correct |
|---|---|
| Bold headline | Regular weight headline |
| ALL CAPS title | Mixed case title |
| Condensed letter spacing | Default letter spacing only |
| Right-aligned text | Left-aligned text |
| Centered body paragraphs | Left-aligned paragraphs |
| 3 different font sizes on same level | Consistent scale ratio |
