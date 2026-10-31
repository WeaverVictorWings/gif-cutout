[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

Entfernen Sie weiße, schwarze oder beliebige einfarbige Hintergründe aus animierten GIFs — direkt im Browser. Eine einzige Datei, keine Installation, nichts wird hochgeladen.

![screenshot](docs/screenshot.png)

## Verwendung

- **Online:** **https://weavervictorwings.github.io/gif-cutout/** öffnen
- **Offline:** [`index.html`](index.html) herunterladen und doppelklicken. Mehr Installation gibt es nicht.

## In 3 Schritten loslegen

1. Ein GIF hineinziehen (oder auf **Datei wählen** klicken; mit **Beispiel Weiß** gleich ausprobieren).
2. Vorschau prüfen. Bei unsauberen Kanten die **Toleranz** erhöhen.
3. Unten auf den großen **Export**-Button klicken.

## Funktionen

- Erkennt den Hintergrund automatisch (auch falsche „transparente“ Schachbretter); die Pipette fügt bis zu 6 Hintergrundfarben hinzu
- **Leckschutz** und **automatisches Füllen von Spalten**: feine Linien im Original schneiden keine Schlitze mehr ins Motiv
- Intelligenter **Zauberstab** (folgt Verläufen und Texturen, stoppt an Konturen; Toleranz durch Ziehen, Umschalt/Alt fügen hinzu/ziehen ab, folgt dem Motiv über alle Bilder), Lasso, Rahmen, **intelligenter Pinsel**, Füllpinsel; Rückgängig / Wiederholen überall
- Kontur, Schatten, Leuchten, Farbkorrektur; rückwärts, Hin-und-zurück, Bilder auslassen, neue Hintergründe
- Zoomen und Verschieben, **C** gedrückt halten zeigt das Original, Start-/Endpunkt, Bild als transparentes PNG kopieren, Tastenkürzel, gemerkte Einstellungen
- Eingabe: GIF, APNG, WebP, PNG, JPG, Einfügen, Ordner im Stapel
- Ausgabe: GIF (Zielgröße, Farbanzahl, Kanten vormischen), APNG, animiertes WebP, PNG-Sequenz (zip), Sprite-Sheet; mehrere Formate gleichzeitig in einer ZIP-Datei
- Sticker-Voreinstellungen (WeChat, Discord, Slack, LINE), Auffüllen zu Quadrat, Zuschneiderahmen, doppelte Bilder zusammenfassen, Größenschätzung
- Außerdem: **Video → Animation** (mp4 / webm, Bereich, fps, Größe), **mehrere Bilder → eine Animation**, **Untertitel**; manuelle Änderungen werden **automatisch im Browser gespeichert** und beim erneuten Öffnen derselben Datei angeboten; Prüfliste vor dem Export und WhatsApp-Voreinstellung; optionale, experimentelle **KI-Freistellung** (Modell läuft im Browser, wird beim ersten Mal geladen)
- 10 Sprachen, automatisch erkannt, Umschalten oben links

## Einschränkungen

- GIF-Transparenz gibt es nur an/aus, daher sind die Kanten leicht gezackt. Für weiche Kanten APNG oder WebP verwenden.
- Das Lesen von APNG-/WebP-Animationen erfordert einen Browser mit `ImageDecoder` (aktuelles Chrome, Edge, Safari); andere laden nur das erste Bild.
- Verläufe, Schatten oder strukturierte Hintergründe lassen sich mit einer Volltonfarbe nicht perfekt entfernen; nutzen Sie die manuellen Werkzeuge.
- Die KI-Freistellung ist experimentell: Sie braucht Zugriff auf cdn.jsdelivr.net / unpkg.com und einen Modell-Download; sie wurde nicht mit allen Modellen geprüft, und bei sehr bewegten Animationen kann das Ergebnis zwischen Bildern flackern.

## Lizenz

[MIT](LICENSE)
