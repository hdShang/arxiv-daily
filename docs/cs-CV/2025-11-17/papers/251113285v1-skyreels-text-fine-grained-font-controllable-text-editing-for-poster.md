---
layout: default
title: SkyReels-Text: Fine-grained Font-Controllable Text Editing for Poster Design
---

# SkyReels-Text: Fine-grained Font-Controllable Text Editing for Poster Design

**arXiv**: [2511.13285v1](https://arxiv.org/abs/2511.13285) | [PDF](https://arxiv.org/pdf/2511.13285.pdf)

**作者**: Yunjie Yu, Jingchen Wu, Junchen Zhu, Chunze Lin, Guibin Chen

---

## 💡 一句话要点

**提出SkyReels-Text框架以解决海报设计中细粒度字体可控文本编辑问题**

**关键词**: `字体可控文本编辑` `海报设计` `细粒度编辑` `图像编辑模型` `字形补丁控制`

## 📋 核心要点

1. 核心问题：现有图像编辑模型在细粒度、字体感知的文本操作方面不足，限制专业设计应用
2. 方法要点：无需字体标签或微调，用户提供裁剪字形补丁即可控制多文本区域字体编辑
3. 实验或效果：在多个数据集上实现文本保真度和视觉真实性的最先进性能

## 📄 摘要（原文）

> Artistic design such as poster design often demands rapid yet precise modification of textual content while preserving visual harmony and typographic intent, especially across diverse font styles. Although modern image editing models have grown increasingly powerful, they still fall short in fine-grained, font-aware text manipulation, limiting their utility in professional design workflows such as poster editing. To address this issue, we present SkyReels-Text, a novel font-controllable framework for precise poster text editing. Our method enables simultaneous editing of multiple text regions, each rendered in distinct typographic styles, while preserving the visual appearance of non-edited regions. Notably, our model requires neither font labels nor fine-tuning during inference: users can simply provide cropped glyph patches corresponding to their desired typography, even if the font is not included in any standard library. Extensive experiments on multiple datasets, including handwrittent text benchmarks, SkyReels-Text achieves state-of-the-art performance in both text fidelity and visual realism, offering unprecedented control over font families, and stylistic nuances. This work bridges the gap between general-purpose image editing and professional-grade typographic design.

