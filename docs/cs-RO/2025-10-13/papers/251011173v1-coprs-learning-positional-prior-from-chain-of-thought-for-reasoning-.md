---
layout: default
title: CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation
---

# CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation

**arXiv**: [2510.11173v1](https://arxiv.org/abs/2510.11173) | [PDF](https://arxiv.org/pdf/2510.11173.pdf)

**作者**: Zhenyu Lu, Liupeng Li, Jinpeng Wang, Yan Feng, Bin Chen, Ke Chen, Yaowei Wang

---

## 💡 一句话要点

**提出CoPRS模型，通过可微分热图桥接语言推理与分割，提升可解释性与精度。**

**关键词**: `推理分割` `多模态思维链` `可微分热图` `位置先验` `掩码生成` `可解释性`

## 📋 核心要点

1. 现有推理分割方法直接连接语言模型特征或文本位置，限制可解释性与语义细节。
2. CoPRS基于多模态思维链生成可微分位置先验热图，通过轻量解码器输出精确掩码。
3. 在RefCOCO系列和ReasonSeg数据集上，性能达到或超越现有最佳结果，热图质量影响掩码质量。

## 📄 摘要（原文）

> Existing works on reasoning segmentation either connect hidden features from
> a language model directly to a mask decoder or represent positions in text,
> which limits interpretability and semantic detail. To solve this, we present
> CoPRS, a Multi-modal Chain-of-Thought (MCoT)-based positional perception model
> that bridges language reasoning to segmentation through a differentiable and
> interpretable positional prior instantiated as a heatmap. By making the
> reasoning process clear via MCoT and expressing it as a dense, differentiable
> heatmap, this interface enhances interpretability and diagnostic analysis and
> yields more concentrated evidence on the target. A learnable concentration
> token aggregates features of the image and reasoning text to generate this
> positional prior, which is decoded to precise masks through a lightweight
> decoder, providing a direct connection between reasoning and segmentation.
> Across the RefCOCO series and ReasonSeg, CoPRS matches or surpasses the best
> reported metrics on each standard split under comparable protocols, with
> performance at or above prior state of the art across both validation and test
> partitions. Extensive experiments reveal that the quality of the heatmap
> strongly influences the resulting mask quality, supporting a consistent
> association between the reasoning output and downstream mask generation.
> Collectively, these findings support the utility of this paradigm in bridging
> reasoning and segmentation and show advantages in concentration driven by
> reasoning and predicting masks more precisely. Code, checkpoints and logs are
> released at https://github.com/ZhenyuLU-Heliodore/CoPRS.git.

