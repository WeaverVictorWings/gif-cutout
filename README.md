[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

Remove white, black or any solid background from animated GIFs — right in your browser. One file, no install, nothing uploaded.

![screenshot](docs/screenshot.png)

## Use it

- **Online:** open **https://weavervictorwings.github.io/gif-cutout/**
- **Offline:** download [`index.html`](index.html) and double-click it. That is the whole installation.

## Quick start

1. Drop in a GIF (or click **Choose file**; **White sample** lets you try it instantly).
2. Check the preview. If edges look dirty, raise **Tolerance**.
3. Press the big **Export** button at the bottom.

## Features

- Auto-detects the background (even fake “transparent” checkerboards); eyedropper adds up to 6 background colours
- **Leak guard** and **auto-fill gaps** stop thin lines in the source from cutting slits into the subject
- Smart **magic wand** (follows gradients, stops at outlines; drag to tune tolerance, Shift/Alt to add/subtract, tracks the subject across frames), lasso, marquee, **smart brush**, fill brush; **mark the subject** with two brushes to cut out complex photo backgrounds, then follow all frames; undo / redo for everything
- Outline, shadow, glow, colour tweaks; reverse, ping-pong, frame skipping, new backgrounds
- Zoom & pan, hold **C** to peek at the original, in/out points, copy a frame as transparent PNG, keyboard shortcuts, settings remembered
- Input: GIF, APNG, WebP, PNG, JPG, paste, batch folders
- Export: GIF (target file size, colour count, edge pre-blend), APNG, animated WebP, PNG sequence (zip), sprite sheet — several formats at once in one zip
- Sticker presets (WeChat, Discord, Slack, LINE), square padding, crop box, merge duplicate frames, live size estimate
- 10 languages, auto-detected, switch at the top-left

## Limits

- GIF transparency is on/off only, so edges are slightly jagged. Use APNG or WebP for smooth edges.
- Reading APNG/WebP animation needs a browser with `ImageDecoder` (recent Chrome, Edge, Safari); others load the first frame only.
- Gradients, shadows or textured backgrounds cannot be removed perfectly with a solid-colour approach; use the manual tools.

## License

[MIT](LICENSE)
