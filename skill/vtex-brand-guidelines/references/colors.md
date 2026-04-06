# VTEX Color System

Source: [brand.vtex.com](https://brand.vtex.com/)

---

## Primary Color

### Rebel Pink
- **Hex:** `#F71963`
- **RGB:** 247, 25, 99
- **CMYK:** 0, 100, 45, 0
- **Pantone:** Rubine Red

**Role:** Main brand identifier. Use for:
- Primary CTAs, buttons, highlights
- Awareness campaigns, covers, impact slides
- Ads and event stands
- Accent lines, borders, and bars
- Section divider slide backgrounds

---

## Secondary Color

### Serious Black
- **Hex:** `#142032`
- **RGB:** 20, 32, 50
- **CMYK:** 90, 80, 50, 60
- **Pantone:** 296 C

**Role:** Transmits exclusivity and authority. Use for:
- Dark-theme slide covers
- Strong headlines on light backgrounds
- Footer and navigation bars
- Use sparingly as a background — reserve for high-impact moments

---

## Pink Variations (Derived from Rebel Pink)

| Name | Hex | Pantone |
|---|---|---|
| Soft Pink | `#FFF3F6` | 705 U |
| Yogurt Pink | `#FFE0EF` | 707 U |
| Bubble Gum Pink | `#FFC4DD` | 1765 U |

**Role:** Provide visual flexibility and lightness. Use as:
- Tinted section backgrounds
- Callout boxes and highlight panels
- Infographic fills

---

## Balance Colors

| Name | Hex | Role |
|---|---|---|
| Plain White | `#FFFFFF` | Default slide/page background, text on dark backgrounds |
| Soft Blue | `#F5F9FF` | Subtle alternative to pure white, content slide backgrounds |

**Purpose:** Balance Rebel Pink energy. Create breathing room and contrast.

---

## Gray Scale

| Name | Hex | Role |
|---|---|---|
| Winter Gray | `#E7E9EE` | Dividers, borders, table lines |
| Cool Gray | `#A1A8B7` | Secondary text, captions, metadata |
| Serious Gray | `#5B6E84` | Supporting body text, subheadings |

---

## Usage Rules

1. **Never combine Rebel Pink and Serious Black as co-primary colors** in the same composition — they fight for dominance
2. Maintain high contrast between text and background — WCAG AA minimum
3. Avoid low-contrast pairings (e.g., Cool Gray text on Soft Blue background)
4. Never use colors outside this system to represent VTEX
5. When using Rebel Pink as a background, use white text only

---

## Recommended Slide Color Schemes

| Slide type | Background | Headline | Body text | Accent |
|---|---|---|---|---|
| Cover | `#142032` | `#FFFFFF` | `#A1A8B7` | `#F71963` |
| Section divider | `#F71963` | `#FFFFFF` | `#FFFFFF` | — |
| Content | `#F5F9FF` | `#142032` | `#5B6E84` | `#F71963` |
| Data / chart | `#FFFFFF` | `#142032` | `#5B6E84` | `#F71963` |
| Quote | `#FFF3F6` | `#142032` | `#5B6E84` | `#F71963` |
| Closing | `#142032` | `#FFFFFF` | `#A1A8B7` | `#F71963` |

---

## python-pptx Color Constants

```python
from pptx.dml.color import RGBColor

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
```

---

## CSS Custom Properties

```css
:root {
  --vtex-rebel-pink:    #F71963;
  --vtex-serious-black: #142032;
  --vtex-plain-white:   #FFFFFF;
  --vtex-soft-blue:     #F5F9FF;
  --vtex-soft-pink:     #FFF3F6;
  --vtex-yogurt-pink:   #FFE0EF;
  --vtex-bubble-gum:    #FFC4DD;
  --vtex-winter-gray:   #E7E9EE;
  --vtex-cool-gray:     #A1A8B7;
  --vtex-serious-gray:  #5B6E84;
}
```
