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
- Pincel, **pincel de relleno** y **varita mágica** (sigue al sujeto entre fotogramas); deshacer / rehacer para ajustes y retoques
- Contorno, sombra, brillo, color; reversa, ping-pong, salto de fotogramas, nuevos fondos
- Zoom y desplazamiento, mantén **C** para ver el original, puntos de inicio / fin, copiar un fotograma como PNG transparente, atajos de teclado, ajustes recordados
- Entrada: GIF, APNG, WebP, PNG, JPG, pegar, carpetas por lotes
- Salida: GIF (tamaño objetivo, número de colores, premezcla de bordes), APNG, WebP animado, secuencia PNG (zip), hoja de sprites; varios formatos a la vez en un solo zip
- Preajustes para stickers (WeChat, Discord, Slack, LINE), relleno cuadrado, recuadro de recorte, fusión de fotogramas repetidos, estimación de tamaño
- 10 idiomas, detección automática, cambio arriba a la izquierda

## Limitaciones

- La transparencia de GIF es solo sí/no, por eso los bordes salen algo dentados. Para bordes suaves usa APNG o WebP.
- Leer animaciones APNG/WebP requiere un navegador con `ImageDecoder` (Chrome, Edge o Safari recientes); en otros solo se carga el primer fotograma.
- Degradados, sombras o fondos con textura no se pueden quitar a la perfección con un método de color sólido; usa las herramientas manuales.

## Licencia

[MIT](LICENSE)
