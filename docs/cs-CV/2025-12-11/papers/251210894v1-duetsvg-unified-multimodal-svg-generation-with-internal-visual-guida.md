---
layout: default
title: DuetSVG: Unified Multimodal SVG Generation with Internal Visual Guidance
---

# DuetSVG: Unified Multimodal SVG Generation with Internal Visual Guidance

**arXiv**: [2512.10894v1](https://arxiv.org/abs/2512.10894) | [PDF](https://arxiv.org/pdf/2512.10894.pdf)

**作者**: Peiying Zhang, Nanxuan Zhao, Matthew Fisher, Yiran Xu, Jing Liao, Difan Liu

---

## 💡 一句话要点

**提出DuetSVG，通过联合生成图像与SVG令牌，解决复杂语义下SVG生成质量不足的问题。**

**关键词**: `SVG生成` `多模态模型` `视觉语言模型` `端到端训练` `测试时缩放`

## 📋 核心要点

1. 现有VLM方法在SVG生成中因缺乏视觉信号，常导致语义复杂时几何不连贯或视觉吸引力差。
2. DuetSVG统一多模态模型，端到端联合生成图像与SVG令牌，并利用测试时缩放策略以视觉预测指导解码。
3. 实验表明，该方法在多种应用中优于现有方法，生成视觉忠实、语义对齐且语法清晰的SVG。

## 📄 摘要（原文）

> Recent vision-language model (VLM)-based approaches have achieved impressive results on SVG generation. However, because they generate only text and lack visual signals during decoding, they often struggle with complex semantics and fail to produce visually appealing or geometrically coherent SVGs. We introduce DuetSVG, a unified multimodal model that jointly generates image tokens and corresponding SVG tokens in an end-to-end manner. DuetSVG is trained on both image and SVG datasets. At inference, we apply a novel test-time scaling strategy that leverages the model's native visual predictions as guidance to improve SVG decoding quality. Extensive experiments show that our method outperforms existing methods, producing visually faithful, semantically aligned, and syntactically clean SVGs across a wide range of applications.

