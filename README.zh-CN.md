[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Русский](README.ru.md) · [Español](README.es.md) · [한국어](README.ko.md)

# GIF 抠底台

在浏览器里把动图的白底、黑底或任意纯色背景抠掉。单个文件，不用安装，文件不会上传。

![screenshot](docs/screenshot.png)

## 怎么用

- **在线使用：** 打开 **https://weavervictorwings.github.io/gif-cutout/**
- **离线使用：** 下载 [`index.html`](index.html)，双击用浏览器打开就行，这就是全部「安装」步骤。

## 三步上手

1. 拖入一个 GIF（或点**选择文件**；点**白底示例**可以立刻试玩）。
2. 看预览，边缘不干净就调高**容差**。
3. 点底部那个大大的**导出**按钮。

## 功能

- 自动识别背景色，也可用吸管点选任意纯色
- **穿透保护**和**自动补缝**：原图里的细线不会再在主体上抠出缝
- 画笔和**魔棒**手动修补，可撤销重做；边缘平滑、去白边/黑边
- 描边、投影、发光、调色；倒放、来回播放、抽帧、换背景
- 输入：GIF、APNG、WebP、PNG、JPG，支持粘贴和批量处理文件夹
- 导出：GIF（可设目标大小）、APNG、动画 WebP、PNG 序列（zip）、精灵图
- 6 种语言，自动识别，左上角可切换

## 已知限制

- GIF 的透明只有「有 / 没有」，边缘会有些锯齿；要平滑边缘请导出 APNG 或 WebP。
- 读取 APNG / WebP 动画需要浏览器支持 `ImageDecoder`（较新的 Chrome、Edge、Safari），其他浏览器只载入第一帧。
- 渐变、阴影或有纹理的背景无法用纯色方式完美去除，可配合手动工具。

## 许可证

[MIT](LICENSE)
