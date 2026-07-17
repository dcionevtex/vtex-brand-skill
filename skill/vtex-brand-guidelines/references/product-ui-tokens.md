# VTEX Product UI Tokens (Styleguide / Admin Design System)

Source: [styleguide.vtex.com](https://styleguide.vtex.com/) — tokens extracted from the official `vtex-tachyons` package (the design token source behind @vtex/styleguide).

**Scope:** Use these ONLY when mocking VTEX Admin screens, product UIs, or demo interfaces. For marketing/brand materials (slides, proposals, documents), use the brand palette in SKILL.md.

Key difference from the brand palette: the product's primary action color is **blue**, not pink. Pink (`#F71963`) appears in the product only as `emphasis`.

## Semantic Colors (primary reference)

| Token | Hex | Use |
|---|---|---|
| action-primary | `#134CD8` | Primary buttons, links, active states |
| action-secondary | `#EEF3F7` | Secondary button background |
| emphasis | `#F71963` | Emphasis/highlight elements only |
| background base | `#FFFFFF` | Default surface |
| background inverted | `#3F3F40` | Dark surfaces |
| text on base | `#3F3F40` | Default text |
| text link | `#134CD8` | Links |
| disabled | `#F2F4F5` bg / `#979899` text | Disabled controls |

## State Colors

| State | Solid | Faded (background) | Text |
|---|---|---|---|
| Success | `#8BC34A` | `#EAFCE3` | `#79B03A` |
| Danger | `#FF4C4C` | `#FFE6E6` | `#FF4C4C` |
| Warning | `#FFB100` | `#FFF6E0` | `#E19D00` |

## Gray Scale (muted)

| Token | Hex |
|---|---|
| muted-1 | `#727273` |
| muted-2 | `#979899` |
| muted-3 | `#CACBCC` |
| muted-4 | `#E3E4E6` |
| muted-5 | `#F2F4F5` |
| near-white | `#F7F9FA` |

## Named Colors (legacy flat palette)

near-black `#3F3F40` · dark-gray `#585959` · mid-gray `#727273` · gray `#979899` · silver `#CACBCC` · light-gray `#E3E4E6` · light-silver `#F2F4F5` · washed-blue `#EDF4FA` · light-blue `#CCE8FF` · blue `#368DF7` · heavy-blue `#2A6DBF` · light-marine `#3D5980` · marine `#25354D` · serious-black `#142032` · elite-purple `#8914CC` · heavy-rebel-pink `#DD1659`

## Admin Mockup Quick Pattern (HTML)

```css
:root {
  --action-primary: #134CD8;
  --bg-base: #FFFFFF;
  --bg-muted: #F7F9FA;
  --text-base: #3F3F40;
  --text-muted: #979899;
  --border: #E3E4E6;
  --success: #8BC34A;
  --danger: #FF4C4C;
  --warning: #FFB100;
}
/* Admin uses system fonts (VTEX Trust is brand-only) */
body { font-family: -apple-system, system-ui, sans-serif; color: var(--text-base); }
.btn-primary { background: var(--action-primary); color: #fff; border-radius: 4px; }
```
