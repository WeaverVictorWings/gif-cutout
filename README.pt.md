[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

Remova fundos brancos, pretos ou de qualquer cor sólida de GIFs animados — diretamente no navegador. Um só ficheiro, sem instalação, nada é enviado.

![screenshot](docs/screenshot.png)

## Como usar

- **Online:** abra **https://weavervictorwings.github.io/gif-cutout/**
- **Offline:** descarregue [`index.html`](index.html) e faça duplo clique. Essa é toda a instalação.

## Começar em 3 passos

1. Arraste um GIF (ou clique em **Escolher ficheiro**; **Exemplo fundo branco** deixa-o experimentar logo).
2. Veja a pré-visualização. Se as bordas ficarem sujas, aumente a **Tolerância**.
3. Clique no grande botão **Exportar** em baixo.

## Funcionalidades

- Deteta o fundo automaticamente (até os falsos xadrezes «transparentes»); o conta-gotas adiciona até 6 cores de fundo
- **Proteção contra fugas** e **preenchimento automático de frestas**: linhas finas da origem já não abrem fendas no sujeito
- **Varinha mágica** inteligente (segue gradientes e texturas, para nos contornos; arraste para ajustar a tolerância, Shift/Alt somam/subtraem, acompanha o sujeito entre fotogramas), laço, retângulo, **pincel inteligente**, pincel de preenchimento; anular / refazer em tudo
- Contorno, sombra, brilho, cor; reverso, vaivém, salto de fotogramas, novos fundos
- Zoom e deslocamento, mantenha **C** para ver o original, pontos de início / fim, copiar um fotograma como PNG transparente, atalhos de teclado, definições memorizadas
- Entrada: GIF, APNG, WebP, PNG, JPG, colar, pastas em lote
- Saída: GIF (tamanho alvo, número de cores, pré-mistura das bordas), APNG, WebP animado, sequência PNG (zip), folha de sprites; vários formatos de uma vez num único zip
- Predefinições para stickers (WeChat, Discord, Slack, LINE), preenchimento quadrado, caixa de recorte, união de fotogramas repetidos, estimativa de tamanho
- Também: **vídeo → animação** (mp4 / webm, intervalo, fps, tamanho), **várias imagens → uma animação**, **legendas**; as edições manuais são **guardadas automaticamente no navegador** e oferecidas ao reabrir o mesmo ficheiro; lista de verificação antes de exportar e predefinição do WhatsApp; **recorte com IA** opcional e experimental (o modelo corre no navegador e é descarregado na primeira utilização)
- 10 idiomas, deteção automática, alternar no canto superior esquerdo

## Limitações

- A transparência do GIF é só ligada/desligada, por isso as bordas ficam ligeiramente serrilhadas. Use APNG ou WebP para bordas suaves.
- Ler animações APNG/WebP requer um navegador com `ImageDecoder` (Chrome, Edge ou Safari recentes); os outros carregam só o primeiro fotograma.
- Gradientes, sombras ou fundos com textura não se removem na perfeição com cor sólida; use as ferramentas manuais.
- O recorte com IA é experimental: precisa de acesso a cdn.jsdelivr.net / unpkg.com e de descarregar um modelo; não foi verificado com todos os modelos e, em animações muito agitadas, o resultado pode cintilar entre fotogramas.

## Licença

[MIT](LICENSE)
