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

---

## Requirements

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- macOS, Linux, or Windows with WSL
- Python 3.9+ with `python-pptx` (only for `.pptx` generation)

---

## Installation

### Step 1 — Copy the skill to your Claude skills directory

```bash
# Clone this repo
git clone https://github.com/dcionevtex/vtex-brand-skill.git

# Create the skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r vtex-brand-skill/skill/vtex-brand-guidelines ~/.claude/skills/
```

That's it. No restart needed — Claude Code picks up skills automatically.

### Step 2 — Install the VTEX Trust font (optional, recommended)

The font is required for `.pptx` files to render correctly.

```bash
# macOS — automated install
curl -L -o /tmp/vtex-fonts.zip "https://brand.vtex.com/wp-content/uploads/2022/04/Tipografia.zip" \
  && unzip -o /tmp/vtex-fonts.zip -d /tmp/vtex-fonts \
  && unzip -o "/tmp/vtex-fonts/Tipografia/VTEX Trust_Public-20220427T202038Z-001.zip" \
     -d /tmp/vtex-trust \
  && cp /tmp/vtex-trust/"VTEX Trust_Public"/VTEXTrust-*.otf ~/Library/Fonts/ \
  && echo "VTEX Trust installed"
```

For **Windows**: extract the ZIP and double-click each `.otf` file to install.

### Step 3 — Install python-pptx (for .pptx generation)

```bash
pip3 install python-pptx
```

---

## Usage

Once the skill is installed, just ask Claude naturally:

```
create a VTEX presentation on our Q3 roadmap
```
```
make a VTEX-branded slide deck for a customer discovery call
```
```
apply VTEX brand guidelines to this document
```
```
generate a VTEX proposal following brand standards
```

Claude will load the brand guidelines automatically and produce a ready-to-run Python script that generates the `.pptx` file.

---

## Trigger phrases

The skill activates on any of these:

| Phrase | What happens |
|---|---|
| "create a VTEX presentation" | Generates a branded `.pptx` script |
| "make a VTEX slide deck" | Generates a branded `.pptx` script |
| "apply VTEX brand guidelines" | Applies brand rules to existing content |
| "generate a VTEX-branded document" | Produces a branded artifact |
| "create a PPT following VTEX brand" | Generates a branded `.pptx` script |
| "use VTEX colors and fonts" | Applies color/type system |

---

## What's included

```
skill/
└── vtex-brand-guidelines/
    ├── SKILL.md                        ← Core skill loaded by Claude Code
    └── references/
        ├── colors.md                   ← Full palette: hex, RGB, CMYK, Pantone, CSS vars
        ├── typography.md               ← Type scale, line-height, weight rules, CSS
        ├── logo-guidelines.md          ← Clearspace, placement, dos/don'ts, placeholders
        ├── voice-tone.md               ← Brand personality, copy principles, review checklist
        └── pptx-generation.md          ← Full python-pptx builder with 6 slide templates

examples/
└── vtex_composable_commerce.py        ← Ready-to-run 13-slide deck on Composable Commerce
```

---

## Example: Composable Commerce deck

A ready-to-run example is included in `examples/`.

```bash
cd examples
pip3 install python-pptx

# Without logos (uses text placeholder)
python3 vtex_composable_commerce.py

# With official logos (download from brand.vtex.com)
python3 vtex_composable_commerce.py \
  --logo-rebel /path/to/VTEX-Logo-Rebel.png \
  --logo-white /path/to/VTEX-Logo-White.png

# Custom output path
python3 vtex_composable_commerce.py --output my_deck.pptx
```

This generates a 13-slide deck covering:

| # | Type | Content |
|---|---|---|
| 1 | Cover | Title slide — dark bg, pink accent |
| 2 | Section | The Problem |
| 3 | Content | Pain points of monolithic platforms |
| 4 | Stats | Cost of inaction — 3 large-number stats |
| 5 | Section | What composable actually means |
| 6 | Content | Composable vs headless, MACH definition |
| 7 | Two-col | Monolith vs Composable side-by-side |
| 8 | Section | How VTEX enables composable |
| 9 | Content | VTEX architecture pillars |
| 10 | Content | Three migration paths |
| 11 | Quote | Customer quote slide |
| 12 | Stats | Results — 3 large-number stats |
| 13 | Closing | CTA slide — dark bg, vertical accent |

---

## Official brand assets

Download directly from VTEX:

| Asset | URL |
|---|---|
| Logo package | `https://brand.vtex.com/wp-content/uploads/2024/08/Logo-Tagline-Composable-and-Complete.zip` |
| Font (VTEX Trust) | `https://brand.vtex.com/wp-content/uploads/2022/04/Tipografia.zip` |
| Figma assets | [figma.com/design/VNkQ2Zmvn98cSyY9HZQNQZ/VTEX-Brand-Assets](https://www.figma.com/design/VNkQ2Zmvn98cSyY9HZQNQZ/VTEX-Brand-Assets) |
| Brand site | [brand.vtex.com](https://brand.vtex.com/) |

---

## Keeping it updated

To get the latest version of the skill:

```bash
cd vtex-brand-skill
git pull
cp -r skill/vtex-brand-guidelines ~/.claude/skills/
```

---

## License

MIT. Brand assets, colors, and typography belong to VTEX and are governed by [VTEX brand guidelines](https://brand.vtex.com/).
