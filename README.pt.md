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
- Dois métodos de recorte logo acima da prévia — **Remover fundo liso** e **Recorte por IA** — com o mais indicado recomendado para cada arquivo. Animações muito grandes são reduzidas automaticamente para não faltar memória, o número de reproduções (loop infinito ou N vezes) é mantido na exportação e a página não carrega fontes externas (abre na hora mesmo onde o Google é bloqueado).
- Bordas mais limpas: depois do recorte, os **fragmentos soltos** ao redor do sujeito são apagados automaticamente (nunca o que você restaurou à mão), e a **suavização entre quadros** reduz a cintilação em áreas paradas. Também: **dividir sprite sheet** em animação, **verificação de loop** com corte em um clique, ajuste de **matiz** e **minhas predefinições** (salvas no navegador).
- 10 idiomas, deteção automática, alternar no canto superior esquerdo

## Limitações

- A transparência do GIF é só ligada/desligada, por isso as bordas ficam ligeiramente serrilhadas. Use APNG ou WebP para bordas suaves.
- Ler animações APNG/WebP requer um navegador com `ImageDecoder` (Chrome, Edge ou Safari recentes); os outros carregam só o primeiro fotograma.
- Gradientes, sombras ou fundos com textura não se removem na perfeição com cor sólida; use as ferramentas manuais.
- O recorte por IA é experimental: precisa de acesso a cdn.jsdelivr.net / unpkg.com, e os modelos só são baixados quando você os escolhe (5–179 MB, guardados no navegador). Primeiro testa o quadro atual para você conferir antes de processar todos, e processa apenas os quadros que serão exportados. Nenhum modelo serve para todos os clipes («Geral, alta qualidade» foi o mais confiável nos nossos 18 clipes de teste). A velocidade no navegador e a aceleração WebGPU dependem do seu dispositivo.

## Licença

[MIT](LICENSE)
