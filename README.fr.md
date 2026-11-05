[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

Supprimez le fond blanc, noir ou de toute couleur unie des GIF animés — directement dans votre navigateur. Un seul fichier, aucune installation, rien n’est envoyé.

![screenshot](docs/screenshot.png)

## Utilisation

- **En ligne :** ouvrez **https://weavervictorwings.github.io/gif-cutout/**
- **Hors ligne :** téléchargez [`index.html`](index.html) et double-cliquez dessus. C’est toute l’installation.

## Démarrage en 3 étapes

1. Déposez un GIF (ou cliquez sur **Choisir un fichier** ; **Exemple fond blanc** permet d’essayer tout de suite).
2. Vérifiez l’aperçu. Si les bords sont sales, augmentez la **Tolérance**.
3. Cliquez sur le grand bouton **Exporter** en bas.

## Fonctionnalités

- Détecte automatiquement le fond (même les faux damiers « transparents ») ; la pipette ajoute jusqu’à 6 couleurs de fond
- **Anti-fuite** et **comblement auto des fentes** : les lignes fines de la source ne creusent plus de fentes dans le sujet
- **Baguette magique** intelligente (suit dégradés et textures, s’arrête aux contours ; glissez pour régler la tolérance, Maj/Alt ajoutent/retirent, suit le sujet d’une image à l’autre), lasso, rectangle, **pinceau intelligent**, pinceau de remplissage ; annuler / rétablir partout
- Contour, ombre, lueur, couleur ; inversion, aller-retour, saut d’images, nouveaux fonds
- Zoom et déplacement, maintenez **C** pour voir l’original, points d’entrée / sortie, copie d’une image en PNG transparent, raccourcis clavier, réglages mémorisés
- Entrée : GIF, APNG, WebP, PNG, JPG, collage, dossiers par lot
- Sortie : GIF (taille cible, nombre de couleurs, prémélange des bords), APNG, WebP animé, séquence PNG (zip), planche de sprites ; plusieurs formats à la fois dans un seul zip
- Préréglages pour stickers (WeChat, Discord, Slack, LINE), complétion en carré, cadre de recadrage, fusion des images identiques, estimation de la taille
- Aussi : **vidéo → animation** (mp4 / webm, plage, fps, taille), **plusieurs images → une animation**, **légendes** ; vos retouches manuelles sont **enregistrées automatiquement dans le navigateur** et proposées à la réouverture du même fichier ; liste de vérification avant export et préréglage WhatsApp ; **détourage IA** optionnel et expérimental (le modèle s’exécute dans le navigateur, téléchargé au premier usage)
- Trois outils de détourage juste au-dessus de l'aperçu — **Retirer le fond uni**, **Détourage IA** et **Baguette magique** (cliquez sur le fond pour le retirer) — avec la plus adaptée recommandée pour chaque fichier. Les animations très lourdes sont réduites automatiquement pour ne pas saturer la mémoire, le nombre de lectures (en boucle ou N fois) est conservé à l'export, et la page ne charge aucune police externe (elle s'ouvre aussitôt même là où Google est bloqué).
- Bords plus propres : après le détourage, les **fragments isolés** autour du sujet sont effacés automatiquement (jamais ce que vous avez restauré à la main), et le **lissage inter-images** réduit le scintillement des zones fixes. Aussi : **découpe de planche de sprites** en animation, **vérification de boucle** avec coupe en un clic, réglage de **teinte** et **mes préréglages** (enregistrés dans le navigateur).
- 10 langues, détection automatique, changement en haut à gauche

## Limites

- La transparence du GIF est tout ou rien, les bords sont donc légèrement crénelés. Utilisez APNG ou WebP pour des bords lisses.
- La lecture des animations APNG/WebP nécessite un navigateur avec `ImageDecoder` (Chrome, Edge, Safari récents) ; les autres ne chargent que la première image.
- Les dégradés, ombres ou fonds texturés ne peuvent pas être retirés parfaitement par couleur unie ; utilisez les outils manuels.
- Le détourage IA est expérimental : il nécessite l'accès à cdn.jsdelivr.net / unpkg.com, et les modèles ne sont téléchargés que lorsque vous les choisissez (5–179 Mo, mis en cache dans votre navigateur). Il essaie d'abord l'image actuelle pour que vous vérifiiez avant de traiter toutes les images, et ne traite que celles qui seront exportées. Aucun modèle ne convient à tous les clips (« Général, haute qualité » a été le plus fiable sur nos 18 clips de test). La vitesse dans le navigateur et l'accélération WebGPU dépendent de votre appareil.

## Licence

[MIT](LICENSE)
