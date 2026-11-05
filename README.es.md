[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

Quita el fondo blanco, negro o de cualquier color sólido de GIFs animados, directamente en el navegador. Un solo archivo, sin instalar, sin subir nada.

![screenshot](docs/screenshot.png)

## Cómo usarlo

- **En línea:** abre **https://weavervictorwings.github.io/gif-cutout/**
- **Sin conexión:** descarga [`index.html`](index.html) y haz doble clic. Esa es toda la instalación.

## Inicio rápido

1. Arrastra un GIF (o pulsa **Elegir archivo**; **Ejemplo fondo blanco** sirve para probar al instante).
2. Mira la vista previa. Si los bordes se ven sucios, sube la **Tolerancia**.
3. Pulsa el botón grande **Exportar** de abajo.

## Funciones

- Detecta el fondo automáticamente (incluso los falsos tableros «transparentes»); el cuentagotas añade hasta 6 colores de fondo
- **Protección contra fugas** y **relleno automático de huecos**: las líneas finas del original ya no abren rendijas en el sujeto
- **Varita mágica** inteligente (sigue degradados y texturas, se detiene en los contornos; arrastra para ajustar la tolerancia, Shift/Alt suman/restan, sigue al sujeto entre fotogramas), lazo, recuadro, **pincel inteligente**, pincel de relleno; deshacer / rehacer en todo
- Contorno, sombra, brillo, color; reversa, ping-pong, salto de fotogramas, nuevos fondos
- Zoom y desplazamiento, mantén **C** para ver el original, puntos de inicio / fin, copiar un fotograma como PNG transparente, atajos de teclado, ajustes recordados
- Entrada: GIF, APNG, WebP, PNG, JPG, pegar, carpetas por lotes
- Salida: GIF (tamaño objetivo, número de colores, premezcla de bordes), APNG, WebP animado, secuencia PNG (zip), hoja de sprites; varios formatos a la vez en un solo zip
- Preajustes para stickers (WeChat, Discord, Slack, LINE), relleno cuadrado, recuadro de recorte, fusión de fotogramas repetidos, estimación de tamaño
- También: **vídeo → animación** (mp4 / webm, rango, fps, tamaño), **varias imágenes → una animación**, **subtítulos**; tus ediciones manuales se **guardan automáticamente en el navegador** y se ofrecen al reabrir el mismo archivo; lista de comprobación antes de exportar y preajuste de WhatsApp; **recorte con IA** opcional y experimental (el modelo se ejecuta en el navegador y se descarga la primera vez)
- Dos métodos de recorte justo encima de la vista previa — **Quitar fondo liso** y **Recorte con IA** — con el adecuado recomendado para cada archivo. Las animaciones muy grandes se reducen automáticamente para no agotar la memoria, se conserva el número de reproducciones (bucle infinito o N veces) y la página no carga fuentes externas (abre al instante aunque Google esté bloqueado).
- Bordes más limpios: tras recortar, los **fragmentos sueltos** alrededor del sujeto se borran solos (nunca lo que restauraste a mano), y el **suavizado entre fotogramas** reduce el parpadeo en zonas quietas. Además: **dividir hojas de sprites** en animación, **revisión de bucle** con recorte en un clic, cambio de **tono** y **mis ajustes** (guardados en tu navegador).
- 10 idiomas, detección automática, cambio arriba a la izquierda

## Limitaciones

- La transparencia de GIF es solo sí/no, por eso los bordes salen algo dentados. Para bordes suaves usa APNG o WebP.
- Leer animaciones APNG/WebP requiere un navegador con `ImageDecoder` (Chrome, Edge o Safari recientes); en otros solo se carga el primer fotograma.
- Degradados, sombras o fondos con textura no se pueden quitar a la perfección con un método de color sólido; usa las herramientas manuales.
- El recorte con IA es experimental: necesita acceso a cdn.jsdelivr.net / unpkg.com y los modelos se descargan solo cuando los eliges (5–179 MB, en caché en tu navegador). Primero prueba el fotograma actual para que lo revises antes de procesar todos, y solo procesa los fotogramas que vas a exportar. Ningún modelo sirve para todos los clips («General, alta calidad» fue el más fiable en nuestros 18 clips de prueba). La velocidad en el navegador y la aceleración WebGPU dependen de tu dispositivo.

## Licencia

[MIT](LICENSE)
