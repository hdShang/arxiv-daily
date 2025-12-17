---
layout: default
title: From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature
---

# From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature

**arXiv**: [2512.02566v1](https://arxiv.org/abs/2512.02566) | [PDF](https://arxiv.org/pdf/2512.02566.pdf)

**作者**: Kun Yuan, Min Woo Sun, Zhen Chen, Alejandro Lozano, Xiangteng He, Shi Li, Nassir Navab, Xiaoxiao Sun, Nicolas Padoy, Serena Yeung-Levy

---

## 💡 一句话要点

**提出Panel2Patch数据管道，通过挖掘生物医学文献中的层次结构，解决视觉语言预训练中忽略局部对应关系的问题。**

**关键词**: `生物医学视觉语言模型` `层次结构挖掘` `多粒度监督` `数据管道` `科学文献分析` `局部语义对齐`

## 📋 核心要点

1. 核心问题：当前生物医学视觉语言预训练将科学图表压缩为粗粒度图级配对，丢弃了临床医生依赖的局部语义对应。
2. 方法要点：Panel2Pipeline解析图表布局、面板和视觉标记，构建图、面板和补丁级别的层次对齐视觉语言对。
3. 实验或效果：使用少量文献图表提取更有效监督，在较少预训练数据下实现显著性能提升。

## 📄 摘要（原文）

> There is a growing interest in developing strong biomedical vision-language models. A popular approach to achieve robust representations is to use web-scale scientific data. However, current biomedical vision-language pretraining typically compresses rich scientific figures and text into coarse figure-level pairs, discarding the fine-grained correspondences that clinicians actually rely on when zooming into local structures. To tackle this issue, we introduce Panel2Patch, a novel data pipeline that mines hierarchical structure from existing biomedical scientific literature, i.e., multi-panel, marker-heavy figures and their surrounding text, and converts them into multi-granular supervision. Given scientific figures and captions, Panel2Patch parses layouts, panels, and visual markers, then constructs hierarchical aligned vision-language pairs at the figure, panel, and patch levels, preserving local semantics instead of treating each figure as a single data sample. Built on this hierarchical corpus, we develop a granularity-aware pretraining strategy that unifies heterogeneous objectives from coarse didactic descriptions to fine region-focused phrases. By applying Panel2Patch to only a small set of the literature figures, we extract far more effective supervision than prior pipelines, enabling substantially better performance with less pretraining data.

