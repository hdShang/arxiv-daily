---
layout: default
title: XBench: A Comprehensive Benchmark for Visual-Language Explanations in Chest Radiography
---

# XBench: A Comprehensive Benchmark for Visual-Language Explanations in Chest Radiography

**arXiv**: [2510.19599v1](https://arxiv.org/abs/2510.19599) | [PDF](https://arxiv.org/pdf/2510.19599.pdf)

**作者**: Haozhe Luo, Shelley Zixin Shu, Ziyu Zhou, Sebastian Otalora, Mauricio Reyes

---

## 💡 一句话要点

**提出XBench基准以评估胸片视觉语言模型的跨模态可解释性**

**关键词**: `视觉语言模型` `医学图像解释` `胸片基准` `跨模态定位` `可解释性评估`

## 📋 核心要点

1. 核心问题：视觉语言模型在医学图像中的视觉证据对齐能力不足，影响临床可靠性。
2. 方法要点：使用交叉注意力和相似性定位图生成视觉解释，并与放射科医生标注区域对齐评估。
3. 实验或效果：发现模型对小病灶定位性能下降，特定数据集预训练可改善对齐，识别与定位能力相关。

## 📄 摘要（原文）

> Vision-language models (VLMs) have recently shown remarkable zero-shot
> performance in medical image understanding, yet their grounding ability, the
> extent to which textual concepts align with visual evidence, remains
> underexplored. In the medical domain, however, reliable grounding is essential
> for interpretability and clinical adoption. In this work, we present the first
> systematic benchmark for evaluating cross-modal interpretability in chest
> X-rays across seven CLIP-style VLM variants. We generate visual explanations
> using cross-attention and similarity-based localization maps, and
> quantitatively assess their alignment with radiologist-annotated regions across
> multiple pathologies. Our analysis reveals that: (1) while all VLM variants
> demonstrate reasonable localization for large and well-defined pathologies,
> their performance substantially degrades for small or diffuse lesions; (2)
> models that are pretrained on chest X-ray-specific datasets exhibit improved
> alignment compared to those trained on general-domain data. (3) The overall
> recognition ability and grounding ability of the model are strongly correlated.
> These findings underscore that current VLMs, despite their strong recognition
> ability, still fall short in clinically reliable grounding, highlighting the
> need for targeted interpretability benchmarks before deployment in medical
> practice. XBench code is available at
> https://github.com/Roypic/Benchmarkingattention

