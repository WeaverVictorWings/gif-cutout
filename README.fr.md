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
- 10 langues, détection automatique, changement en haut à gauche

## Limites

- La transparence du GIF est tout ou rien, les bords sont donc légèrement crénelés. Utilisez APNG ou WebP pour des bords lisses.
- La lecture des animations APNG/WebP nécessite un navigateur avec `ImageDecoder` (Chrome, Edge, Safari récents) ; les autres ne chargent que la première image.
- Les dégradés, ombres ou fonds texturés ne peuvent pas être retirés parfaitement par couleur unie ; utilisez les outils manuels.
- Le détourage IA est expérimental : il faut accéder à cdn.jsdelivr.net / unpkg.com et télécharger un modèle ; il n’a pas été vérifié avec tous les modèles et, sur des animations très mouvementées, le résultat peut scintiller d’une image à l’autre.

## Licence

[MIT](LICENSE)
