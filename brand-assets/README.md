# Fornax Labs — Brand Assets

The Forge mark and lockups. Use these everywhere.

## The mark

A solid filled diamond (rotated square) with a small V-notch cut from its top vertex. One shape, four strokes, drawable from memory.

- **Geometry:** 100×100 viewBox. SVG path: `M 8 50 L 44 14 L 50 22 L 56 14 L 92 50 L 50 92 Z`
- **Minimum size:** 16 px (the notch still resolves at one pixel deep)
- **Clear space:** keep a margin of at least one quarter of the mark's height on every side

## Colors

| Token  | Hex       | Use                                  |
|--------|-----------|--------------------------------------|
| Ink    | `#1d1e26` | Primary mark on light surfaces       |
| Paper  | `#fafbfc` | Primary mark on dark surfaces        |
| Brand  | `#5b58e6` | Accent / link / hover only           |
| White  | `#ffffff` | Reversed surfaces, photography       |
| Black  | `#000000` | Print / single-color reproduction    |

The mark itself never carries a gradient and never sits inside a circle or rounded square *except* in favicon form.

## Files in this folder

```
svg/
  mark-ink.svg                  · Ink fill, transparent bg
  mark-paper.svg                · Paper fill (for dark surfaces)
  mark-brand.svg                · Indigo fill (accent uses only)
  mark-white.svg / mark-black.svg
  wordmark-ink.svg / wordmark-paper.svg
  lockup-horizontal-ink.svg     · Mark + "Fornax Labs"
  lockup-horizontal-paper.svg
  lockup-horizontal-brand.svg
  lockup-horizontal-on-ink.svg  · Ready-made dark-bg lockup
  lockup-horizontal-on-paper.svg
  lockup-stacked-ink.svg
  lockup-stacked-paper.svg

png/
  mark-ink-{16…1024}.png        · Ink on transparent
  mark-white-{16…1024}.png      · White on transparent (use on dark bg)
  mark-brand-{16…1024}.png      · Indigo on transparent
  lockup-horizontal-ink-{256…2048}.png
  lockup-horizontal-white-{256…2048}.png
  lockup-stacked-ink-{512,1024}.png
  lockup-stacked-white-{512,1024}.png
  wordmark-ink-{512,1024}.png
  social-og-1200x630.png        · Editorial OG image

favicon/
  favicon.svg                   · Rounded ink chip + paper mark
  favicon-{16,32,48,64,96}.png
  apple-touch-icon-180.png
  android-chrome-192.png
  android-chrome-512.png
```

## HTML head snippet (already wired into the sites)

```html
<link rel="icon" type="image/svg+xml" href="brand-assets/favicon/favicon.svg" />
<link rel="icon" type="image/png" sizes="32x32" href="brand-assets/favicon/favicon-32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="brand-assets/favicon/favicon-16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="brand-assets/favicon/apple-touch-icon-180.png" />
```

## What not to do

- Don't outline the mark.
- Don't tilt, mirror, or stretch it.
- Don't fill the notch.
- Don't apply shadows, glows, or bevels.
- Don't combine with another logo within 1× clear space.
- Don't use the indigo Brand color as the primary mark fill on white — it should remain Ink. Indigo is for accent and small UI moments only.
