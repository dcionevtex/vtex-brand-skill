# VTEX Brand Skill for Claude Code

A [Claude Code](https://claude.ai/code) skill that gives Claude complete knowledge of VTEX's official brand guidelines and the ability to generate fully branded documents, presentations, and artifacts.

Brand source: [brand.vtex.com](https://brand.vtex.com/)

---

## What it does

Once installed, Claude will automatically apply VTEX brand standards when you ask it to create presentations, documents, or any visual artifact. This includes:

- Correct color palette (Rebel Pink, Serious Black, and full system)
- VTEX Trust typography rules
- Logo placement and usage rules
- Brand voice and tone guidance
- Full `python-pptx` PowerPoint builder with slide templates
- Marp markdown-to-slides pattern
- **Architecture/solution diagram standard** — color-coded by component type (VTEX native, custom app, external system, middleware), applied by default to any architecture or system diagram, with HTML/CSS, SVG, and Mermaid templates
- **Official logo assets** bundled in `assets/` (SVG in Rebel Pink / Serious Black / White) with a PNG generator for python-pptx
- **Product UI (Admin) design tokens** from styleguide.vtex.com for demo mockups — kept separate from the brand palette

---

## Requirements

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- macOS, Linux, or Windows with WSL
- Python 3.9+ with `python-pptx` (only for `.pptx` generation)

---

## Installation

### Step 1 — Copy the skill to your Claude skills directory

```bash
git clone https://github.com/dcionevtex/vtex-brand-skill.git
mkdir -p ~/.claude/skills
cp -r vtex-brand-skill/skill/vtex-brand-guidelines ~/.claude/skills/
```

### Step 2 — Install python-pptx (for .pptx generation)

```bash
pip3 install python-pptx
```

---

## What's included

```
skill/
└── vtex-brand-guidelines/
    ├── SKILL.md                        ← Core skill loaded by Claude Code
    ├── assets/
    │   ├── vtex-logo-rebel-pink.svg    ← Official logo, light backgrounds (default)
    │   ├── vtex-logo-serious-black.svg ← Official logo, light backgrounds (alt)
    │   ├── vtex-logo-white.svg         ← Official logo, dark backgrounds
    │   └── generate-pngs.py            ← Renders 960px PNGs for python-pptx (pip install cairosvg)
    └── references/
        ├── colors.md                   ← Full palette: hex, RGB, CMYK, Pantone, CSS vars
        ├── typography.md               ← Type scale, line-height, weight rules, CSS
        ├── logo-guidelines.md          ← Clearspace, placement, dos/don'ts, bundled assets
        ├── voice-tone.md               ← Brand personality, copy principles, review checklist
        ├── pptx-generation.md          ← Full python-pptx builder with 6 slide templates
        ├── diagrams.md                 ← Architecture/solution diagram standard + HTML/SVG/Mermaid templates
        └── product-ui-tokens.md        ← styleguide.vtex.com Admin tokens for demo mockups

examples/
└── vtex_composable_commerce.py        ← Ready-to-run 13-slide deck on Composable Commerce
```

---

## Official brand assets

| Asset | URL |
|---|---|
| Logo package | `https://brand.vtex.com/wp-content/uploads/2024/08/Logo-Tagline-Composable-and-Complete.zip` |
| Font (VTEX Trust) | `https://brand.vtex.com/wp-content/uploads/2022/04/Tipografia.zip` |
| Figma assets | [figma.com/design/VNkQ2Zmvn98cSyY9HZQNQZ/VTEX-Brand-Assets](https://www.figma.com/design/VNkQ2Zmvn98cSyY9HZQNQZ/VTEX-Brand-Assets) |
| Brand site | [brand.vtex.com](https://brand.vtex.com/) |

---

## License

MIT. Brand assets, colors, and typography belong to VTEX and are governed by [VTEX brand guidelines](https://brand.vtex.com/).
