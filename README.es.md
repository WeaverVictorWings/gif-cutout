[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Русский](README.ru.md) · [Español](README.es.md) · [한국어](README.ko.md)

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

- Detecta el fondo automáticamente; cuentagotas para cualquier otro color sólido
- **Anti-fugas** y **rellenar huecos**: las líneas finas del original ya no abren rendijas en el sujeto
- Pincel y **varita mágica** para retocar, con deshacer/rehacer; suavizado de bordes, quitar halo
- Contorno, sombra, resplandor, ajuste de color; reversa, ida y vuelta, saltar fotogramas, nuevo fondo
- Entrada: GIF, APNG, WebP, PNG, JPG, pegar, procesar carpetas por lotes
- Salida: GIF (con tamaño objetivo), APNG, WebP animado, secuencia PNG (zip), hoja de sprites
- 6 idiomas, detección automática, selector arriba a la izquierda

## Limitaciones

- La transparencia de GIF es solo sí/no, por eso los bordes salen algo dentados. Para bordes suaves usa APNG o WebP.
- Leer animaciones APNG/WebP requiere un navegador con `ImageDecoder` (Chrome, Edge o Safari recientes); en otros solo se carga el primer fotograma.
- Degradados, sombras o fondos con textura no se pueden quitar a la perfección con un método de color sólido; usa las herramientas manuales.

## Licencia

[MIT](LICENSE)
