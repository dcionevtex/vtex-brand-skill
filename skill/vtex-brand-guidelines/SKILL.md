---
name: VTEX Brand Guidelines
description: This skill should be used when the user asks to "create a VTEX presentation", "make a VTEX slide deck", "apply VTEX brand guidelines", "generate a VTEX-branded document", "create a PPT following VTEX brand", "apply VTEX visual identity", "use VTEX colors and fonts", "create a VTEX proposal", or any request to produce documents, slides, or artifacts that must follow VTEX's official brand standards.
version: 0.1.0
---

# VTEX Brand Guidelines Skill

Apply VTEX's official visual identity and voice standards when generating documents, presentations, proposals, and any branded artifacts.

Source: [brand.vtex.com](https://brand.vtex.com/)

---

## Core Brand Identity

VTEX's brand is built around three personality traits that must always remain in balance:

- **Bold** — fresh and transformative, not immature
- **Trustworthy** — technically authoritative, not pretentious
- **Optimistic** — confident about the future, not naive

The brand revolves around the customer as protagonist. VTEX is always the guide, never the hero.

---

## Quick Color Reference

| Name | Hex | Role |
|---|---|---|
| Rebel Pink | `#F71963` | Primary brand color, main accent |
| Serious Black | `#142032` | Dark backgrounds, headlines on light |
| Plain White | `#FFFFFF` | Balance color, clean backgrounds |
| Soft Blue | `#F5F9FF` | Balance color, subtle backgrounds |
| Winter Gray | `#E7E9EE` | Dividers, borders |
| Cool Gray | `#A1A8B7` | Secondary text |
| Serious Gray | `#5B6E84` | Supporting text |
| Soft Pink | `#FFF3F6` | Pink tint backgrounds |
| Bubble Gum Pink | `#FFC4DD` | Pink accent |

**Critical rule:** Never combine Rebel Pink and Serious Black as primary colors simultaneously in the same composition.

---

## Quick Typography Reference

| Element | Size Ratio | Line Height | Alignment |
|---|---|---|---|
| Heading | Base × 1.5ⁿ | 100% | Left |
| Subheading | Base × 1.5ⁿ | 120% | Left |
| Body | Base | 150% | Left |

- **Font:** VTEX Trust (custom family). Download from [brand.vtex.com](https://brand.vtex.com/)
- **Fallback stack:** `'VTEX Trust', system-ui, -apple-system, sans-serif`
- **Weight:** Regular by default. Bold and italic permitted in body text only for emphasis — never in titles
- **Case:** Never use all-caps or fully bold titles
- **Letter spacing:** Never alter

---

## Document and Presentation Generation

### Output Formats

Choose the format based on the use case:

| Use case | Recommended format |
|---|---|
| Formal client deliverable | python-pptx → `.pptx` |
| Internal presentation | Marp markdown → `.pdf` or `.html` |
| Web embed / demo | HTML + inline CSS |
| Google Slides | Export Marp or manually styled |

### python-pptx Pattern (for .pptx output)

When generating a PowerPoint file with python-pptx, apply the following brand defaults:

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Brand colors
REBEL_PINK   = RGBColor(0xF7, 0x19, 0x63)
SERIOUS_BLACK = RGBColor(0x14, 0x20, 0x32)
PLAIN_WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
COOL_GRAY    = RGBColor(0xA1, 0xA8, 0xB7)
SOFT_BLUE    = RGBColor(0xF5, 0xF9, 0xFF)

# Slide size: widescreen 16:9
prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
```

**Slide types to implement:**

1. **Cover slide** — Serious Black background (`#142032`), Rebel Pink accent line or block, white headline, VTEX logo top-left
2. **Section divider** — Rebel Pink background (`#F71963`), white text
3. **Content slide** — White or Soft Blue background (`#F5F9FF`), Serious Black headlines, Serious Gray body text
4. **Data/chart slide** — White background, Rebel Pink as primary data color, Serious Black labels
5. **Closing slide** — Mirror of cover or Rebel Pink background

Logo placement: always top-left or bottom-left. Minimum 60px equivalent at 96dpi.

For detailed python-pptx patterns including full slide builder functions, see `references/pptx-generation.md`.

### Marp Pattern (for markdown-to-slides)

```markdown
---
marp: true
theme: default
style: |
  section {
    background: #F5F9FF;
    font-family: 'VTEX Trust', system-ui, sans-serif;
    color: #142032;
  }
  section.cover {
    background: #142032;
    color: #FFFFFF;
  }
  section.pink {
    background: #F71963;
    color: #FFFFFF;
  }
  h1 { color: #142032; line-height: 1.0; }
  h2 { color: #5B6E84; line-height: 1.2; }
  p  { line-height: 1.5; }
---
```

---

## Layout and Composition Rules

- Use an **even number of columns** (symmetrical grid)
- Margins: ¼ column width; gutters: ¼ margin width
- **Anchor content to bottom, then top, fill middle**
- Prioritize white space — avoid crowded compositions
- Left-align text consistently; center alignment only in specific slide/web contexts
- Maintain strong contrast between text and background (WCAG AA minimum)

---

## Brand Voice in Text Content

When writing copy inside generated documents:

- Open with the audience's pain point, not with VTEX capabilities
- Position VTEX as guide, the customer as protagonist
- Keep language simple and direct — no jargon without explanation
- Balance boldness, trustworthiness, and optimism across the document
- Never open a sentence with "VTEX is the solution" — reframe around what the customer achieves

---

## Logo Usage in Generated Files

- Include logo in every slide/page unless explicitly told not to
- Preferred position: **top-left or bottom-left**
- Use Rebel Pink version on light backgrounds; white version on dark backgrounds
- Minimum size: 60px (digital) / 1cm (print)
- Never distort, rotate, add shadows, or place inside shapes
- For placeholder purposes, use a text label `[VTEX LOGO]` with a pink background block when the actual SVG/PNG is not available

---

## Additional References

| File | Contents |
|---|---|
| `references/colors.md` | Full color palette with RGB, CMYK, Pantone values and usage rules |
| `references/typography.md` | Complete typographic system, scale, spacing, and prohibition list |
| `references/logo-guidelines.md` | Logo variants, clearspace, dos and don'ts |
| `references/voice-tone.md` | Brand voice, tone, personality traits, and copy examples |
| `references/pptx-generation.md` | Full python-pptx builder with slide templates |
