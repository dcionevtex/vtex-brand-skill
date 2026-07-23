---
name: vtex-brand-guidelines
description: This skill should be used when the user asks to "create a VTEX presentation", "make a VTEX slide deck", "apply VTEX brand guidelines", "generate a VTEX-branded document", "create a PPT following VTEX brand", "apply VTEX visual identity", "use VTEX colors and fonts", "create a VTEX proposal", "add the VTEX logo", "create an architecture diagram", "make a solution diagram", "draw a system/integration diagram", "diagram this VTEX architecture", or any request to produce documents, slides, HTML pages, mockups, diagrams, or artifacts that must follow VTEX's official brand standards. Also use when mocking VTEX Admin UI screens for demos (product design system tokens included). Applies automatically to any architecture/solution/integration diagram, even if VTEX branding isn't mentioned explicitly — diagrams for VTEX engagements always follow the brand's diagram standard by default.
metadata:
  version: 0.3.0
---

# VTEX Brand Guidelines Skill

Apply VTEX's official visual identity and voice standards when generating documents, presentations, proposals, and any branded artifacts.

Sources: [brand.vtex.com](https://brand.vtex.com/) (marketing brand) · [styleguide.vtex.com](https://styleguide.vtex.com/) (product/admin design system)

**Two distinct systems — do not mix them:**
- **Brand identity** (this file): marketing, presentations, proposals, documents → Rebel Pink, Serious Black, VTEX Trust font
- **Product UI** (`references/product-ui-tokens.md`): Admin screen mockups, demo UIs → Action Blue `#134CD8`, semantic states

---

## Core Brand Identity

VTEX's brand is built around three personality traits that must always remain in balance:

- **Bold** — fresh and transformative, not immature
- **Trustworthy** — technically authoritative, not pretentious
- **Optimistic** — confident about the future, not naive

The brand revolves around the customer as protagonist. VTEX is always the guide, never the hero.

**Current positioning (2026):** VTEX presents itself as *"The AI-Native Commerce Suite"* and *"The Composable and Complete Commerce Platform"*. Brand architecture spans three platforms: **VTEX Commerce Platform**, **VTEX CX Platform**, and **VTEX Ads Platform**. Use this framing in cover slides and executive summaries.

---

## Logo Assets (bundled in `assets/`)

The official VTEX logo (mark + wordmark, viewBox 0 0 80 29, aspect ratio ~2.76:1) is bundled in three color variants:

| File | Use on |
|---|---|
| `assets/vtex-logo-rebel-pink.svg` / `.png` | Light backgrounds (white, Soft Blue) — default |
| `assets/vtex-logo-serious-black.svg` / `.png` | Light backgrounds when pink would clash |
| `assets/vtex-logo-white.svg` / `.png` | Dark backgrounds (Serious Black, Rebel Pink) |

**Format selection:**
- `.svg` → HTML, Marp, web embeds (crisp at any size)
- `.png` → python-pptx and docx (960px wide, high-res; python-pptx cannot embed SVG)

**Rules:**
- Include the logo on every slide/page unless explicitly told not to
- Position: **top-left or bottom-left**
- Minimum size: 60px wide (digital) / 1cm (print)
- Clearspace: keep at least the height of the "V" mark clear around the logo
- Never distort, rotate, recolor outside the three variants, add shadows, or place inside shapes
- Never pair the pink logo on a Rebel Pink background (use white variant)

---

## Quick Color Reference (Brand)

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
| Heavy Rebel Pink | `#DD1659` | Hover/pressed states on pink elements |

**Critical rules:**
- Never combine Rebel Pink and Serious Black as primary colors simultaneously in the same composition — one leads, the other supports minimally or not at all
- Maintain WCAG AA contrast between text and background

---

## Quick Typography Reference

| Element | Size Ratio | Line Height | Alignment |
|---|---|---|---|
| Heading | Base × 1.5ⁿ | 100% | Left |
| Subheading | Base × 1.5ⁿ | 120% | Left |
| Body | Base | 150% | Left |

- **Font:** VTEX Trust (custom family, single weight philosophy). Download from [brand.vtex.com](https://brand.vtex.com/)
- **Fallback stack:** `'VTEX Trust', system-ui, -apple-system, sans-serif`
- **Weight:** Regular by default. Bold and italic permitted in body text only for emphasis — never in titles
- **Case:** Never use all-caps or fully bold titles
- **Letter spacing:** Never alter

---

## Document and Presentation Generation

### Output Formats

| Use case | Recommended format |
|---|---|
| Formal client deliverable | python-pptx → `.pptx` |
| Internal presentation | Marp markdown → `.pdf` or `.html` |
| Web embed / demo | HTML + inline CSS |
| Google Slides | Export Marp or manually styled |

### python-pptx Pattern (for .pptx output)

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

REBEL_PINK    = RGBColor(0xF7, 0x19, 0x63)
SERIOUS_BLACK = RGBColor(0x14, 0x20, 0x32)
PLAIN_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
COOL_GRAY     = RGBColor(0xA1, 0xA8, 0xB7)
SERIOUS_GRAY  = RGBColor(0x5B, 0x6E, 0x84)
SOFT_BLUE     = RGBColor(0xF5, 0xF9, 0xFF)

prs = Presentation()
prs.slide_width  = Inches(13.33)   # 16:9
prs.slide_height = Inches(7.5)

# Logo embedding — use the bundled PNGs (path relative to this skill)
LOGO_PINK  = "assets/vtex-logo-rebel-pink.png"   # light slides
LOGO_WHITE = "assets/vtex-logo-white.png"        # dark/pink slides

def add_logo(slide, variant=LOGO_PINK, top_left=True):
    w = Inches(1.2)  # aspect 80:29 → height auto
    left = Inches(0.5)
    top  = Inches(0.4) if top_left else prs.slide_height - Inches(0.9)
    slide.shapes.add_picture(variant, left, top, width=w)
```

**Slide types to implement:**

1. **Cover slide** — Serious Black background, Rebel Pink accent line or block, white headline, **white logo** top-left
2. **Section divider** — Rebel Pink background, white text, **white logo**
3. **Content slide** — White or Soft Blue background, Serious Black headlines, Serious Gray body, **pink logo**
4. **Data/chart slide** — White background, Rebel Pink as primary data color, Serious Black labels, **pink logo**
5. **Closing slide** — Mirror of cover

For full slide builder functions, see `references/pptx-generation.md`.

### Marp / HTML Pattern

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
  section.cover { background: #142032; color: #FFFFFF; }
  section.pink  { background: #F71963; color: #FFFFFF; }
  h1 { color: #142032; line-height: 1.0; }
  h2 { color: #5B6E84; line-height: 1.2; }
  p  { line-height: 1.5; }
---
```

For HTML, inline the SVG logo directly (copy contents of the appropriate `assets/*.svg`) or reference the file.

---

## Architecture & Solution Diagrams

**Applies by default to every architecture, solution, integration, or system diagram — even if the request doesn't mention "VTEX brand."** Classify every box into one of four categories and style accordingly:

| Category | Fill | Border | Text |
|---|---|---|---|
| VTEX native (OOTB) | Bubble Gum Pink `#FFC4DD` | Rebel Pink `#F71963` | Serious Black, bold |
| Custom app / VTEX IO | White `#FFFFFF` | Serious Black `#142032` | Serious Black, bold |
| Non-VTEX / external | Serious Gray `#5B6E84` | none | White, bold |
| Middleware / integration layer | Serious Black `#142032` | none | White, bold (full-width banner) |

- Title lockup top-left: **"VTEX"** in bold Rebel Pink + solution name in bold Serious Gray, uppercase
- Always include a legend (bottom-left) mapping swatches to the four categories above
- Arrows: Rebel Pink between VTEX-native components, Serious Gray/Black to or between external systems
- Grouping containers: white fill, border colored to match what's inside; label overlaps the top-left border (like a fieldset legend), never centered
- Never invent new colors for a diagram, and never use Action Blue `#134CD8` (that's Admin-UI-only, see `references/product-ui-tokens.md`)

This is a technical-diagram exception to the marketing typography rules below — bold labels and uppercase sub-titles are fine here for legibility, unlike headline text. Full spec, HTML/CSS template, SVG arrow pattern, and Mermaid `classDef` snippet: `references/diagrams.md`.

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

- Open with the audience's pain point, not with VTEX capabilities
- Position VTEX as guide, the customer as protagonist
- Keep language simple and direct — no jargon without explanation
- Balance boldness, trustworthiness, and optimism across the document
- Never open a sentence with "VTEX is the solution" — reframe around what the customer achieves

---

## References

| File | Contents | Read when |
|---|---|---|
| `references/pptx-generation.md` | Full python-pptx slide builders with logo embedding | Generating .pptx deliverables |
| `references/diagrams.md` | Architecture/solution diagram color-coding, layout rules, HTML/CSS + SVG + Mermaid templates | Generating any architecture, solution, integration, or system diagram |
| `references/colors.md` | Full palette with RGB, CMYK, Pantone values and usage rules | Print work or detailed color decisions |
| `references/typography.md` | Complete typographic system, scale, spacing, prohibitions | Fine typographic control |
| `references/logo-guidelines.md` | Logo variants, clearspace, dos and don'ts | Detailed logo application questions |
| `references/voice-tone.md` | Brand voice, tone, personality traits, copy examples | Writing substantial branded copy |
| `references/product-ui-tokens.md` | VTEX Styleguide (Admin) color tokens and semantics | Mocking Admin UI screens or demo interfaces |

`assets/` contains the logo in three color variants (SVG + PNG) plus `generate-pngs.py` to rebuild PNGs from the SVGs.
