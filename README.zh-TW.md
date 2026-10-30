[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

# GIF Cutout

在瀏覽器裡去除動態 GIF 的白底、黑底或任何純色背景。單一檔案、免安裝、不上傳。

![screenshot](docs/screenshot.png)

## 使用

- **線上：**開啟 **https://weavervictorwings.github.io/gif-cutout/**
- **離線：**下載 [`index.html`](index.html) 後雙擊開啟，這就是全部安裝步驟。

## 三步上手

1. 拖入一個 GIF（或點**選擇檔案**；點**白底範例**可立刻試玩）。
2. 看預覽，邊緣不乾淨就調高**容差**。
3. 點底部那個大大的**匯出**按鈕。

## 功能

- 自動辨識背景色（連假「透明」棋盤格也能辨識），滴管可追加最多 6 種背景色
- **穿透保護**與**自動補縫**：原圖裡的細線不會再在主體上摳出縫
- 智慧**魔術棒**（順著漸層與紋理擴展、遇到輪廓停下，拖曳調容差，Shift 加選 / Alt 減選，會跟著主體在各幀間移動）、套索、框選、**智慧畫筆**、補色畫筆；所有操作都能復原 / 重做
- 描邊、陰影、發光、調色；倒放、來回播放、抽幀、換背景
- 縮放平移、按住 **C** 看原圖、起點 / 終點、複製目前幀為透明 PNG、快捷鍵、自動記住設定
- 輸入：GIF、APNG、WebP、PNG、JPG，支援貼上與批次處理資料夾
- 匯出：GIF（可設目標大小、顏色數、邊緣預混合）、APNG、動態 WebP、PNG 序列（zip）、精靈圖；可同時匯出多種格式並打包成一個 zip
- 貼圖預設（微信、Discord、Slack、LINE）、補成正方形、裁切框、合併重複幀、即時體積估算
- 10 種語言，自動偵測，左上角可切換

## 已知限制

- GIF 的透明只有「有 / 沒有」，邊緣會有些鋸齒；要平滑邊緣請匯出 APNG 或 WebP。
- 讀取 APNG / WebP 動畫需要支援 `ImageDecoder` 的瀏覽器（較新的 Chrome、Edge、Safari），其他瀏覽器只載入第一幀。
- 漸層、陰影或有紋理的背景無法用純色方式完美去除，可搭配手動工具。

## 授權條款

[MIT](LICENSE)
