---
layout: default
title: SmokeBench: Evaluating Multimodal Large Language Models for Wildfire Smoke Detection
---

# SmokeBench: Evaluating Multimodal Large Language Models for Wildfire Smoke Detection

**arXiv**: [2512.11215v1](https://arxiv.org/abs/2512.11215) | [PDF](https://arxiv.org/pdf/2512.11215.pdf)

**作者**: Tianye Qi, Weihao Li, Nick Barnes

---

## 💡 一句话要点

**提出SmokeBench基准以评估多模态大语言模型在野火烟雾检测中的性能**

**关键词**: `野火烟雾检测` `多模态大语言模型` `基准评估` `图像定位` `早期检测` `安全监控`

## 📋 核心要点

1. 野火烟雾透明、无定形，易与云混淆，早期检测困难
2. 基准包含分类、基于瓦片/网格的定位和检测四项任务
3. 评估显示模型在烟雾大面积时分类尚可，但定位能力普遍不足

## 📄 摘要（原文）

> Wildfire smoke is transparent, amorphous, and often visually confounded with clouds, making early-stage detection particularly challenging. In this work, we introduce a benchmark, called SmokeBench, to evaluate the ability of multimodal large language models (MLLMs) to recognize and localize wildfire smoke in images. The benchmark consists of four tasks: (1) smoke classification, (2) tile-based smoke localization, (3) grid-based smoke localization, and (4) smoke detection. We evaluate several MLLMs, including Idefics2, Qwen2.5-VL, InternVL3, Unified-IO 2, Grounding DINO, GPT-4o, and Gemini-2.5 Pro. Our results show that while some models can classify the presence of smoke when it covers a large area, all models struggle with accurate localization, especially in the early stages. Further analysis reveals that smoke volume is strongly correlated with model performance, whereas contrast plays a comparatively minor role. These findings highlight critical limitations of current MLLMs for safety-critical wildfire monitoring and underscore the need for methods that improve early-stage smoke localization.

