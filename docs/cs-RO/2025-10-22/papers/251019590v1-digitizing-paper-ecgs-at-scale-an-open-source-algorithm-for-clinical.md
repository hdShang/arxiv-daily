---
layout: default
title: Digitizing Paper ECGs at Scale: An Open-Source Algorithm for Clinical Research
---

# Digitizing Paper ECGs at Scale: An Open-Source Algorithm for Clinical Research

**arXiv**: [2510.19590v1](https://arxiv.org/abs/2510.19590) | [PDF](https://arxiv.org/pdf/2510.19590.pdf)

**作者**: Elias Stenhede, Agnar Martin Bjørnstad, Arian Ranjbar

---

## 💡 一句话要点

**提出开源算法框架，将纸质心电图数字化以支持临床研究。**

**关键词**: `心电图数字化` `开源算法` `临床研究` `信号处理` `自动化诊断`

## 📋 核心要点

1. 核心问题：大量心电图仅存为纸质扫描，无法用于自动化诊断。
2. 方法要点：开发全自动模块化框架，将扫描或拍摄心电图转换为数字信号。
3. 实验或效果：在37,191张图像上验证，信噪比达19.65 dB，优于现有技术。

## 📄 摘要（原文）

> Millions of clinical ECGs exist only as paper scans, making them unusable for
> modern automated diagnostics. We introduce a fully automated, modular framework
> that converts scanned or photographed ECGs into digital signals, suitable for
> both clinical and research applications. The framework is validated on 37,191
> ECG images with 1,596 collected at Akershus University Hospital, where the
> algorithm obtains a mean signal-to-noise ratio of 19.65 dB on scanned papers
> with common artifacts. It is further evaluated on the Emory Paper Digitization
> ECG Dataset, comprising 35,595 images, including images with perspective
> distortion, wrinkles, and stains. The model improves on the state-of-the-art in
> all subcategories. The full software is released as open-source, promoting
> reproducibility and further development. We hope the software will contribute
> to unlocking retrospective ECG archives and democratize access to AI-driven
> diagnostics.

