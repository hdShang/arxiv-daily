---
layout: default
title: SNAP: Towards Segmenting Anything in Any Point Cloud
---

# SNAP: Towards Segmenting Anything in Any Point Cloud

**arXiv**: [2510.11565v1](https://arxiv.org/abs/2510.11565) | [PDF](https://arxiv.org/pdf/2510.11565.pdf)

**作者**: Aniket Gupta, Hanhui Wang, Charles Saunders, Aruni RoyChowdhury, Hanumant Singh, Huaizu Jiang

---

## 💡 一句话要点

**提出SNAP模型，实现跨域交互式3D点云分割，支持点和文本提示。**

**关键词**: `3D点云分割` `交互式分割` `跨域泛化` `开放词汇分割` `域自适应归一化`

## 📋 核心要点

1. 当前交互式3D点云分割方法局限于单一域和交互形式，且多数据集训练易导致负迁移。
2. SNAP采用域自适应归一化，在7个数据集上训练，支持点和文本提示，实现开放词汇分割。
3. 实验显示SNAP在零样本基准测试中表现优异，超越多个领域特定方法。

## 📄 摘要（原文）

> Interactive 3D point cloud segmentation enables efficient annotation of
> complex 3D scenes through user-guided prompts. However, current approaches are
> typically restricted in scope to a single domain (indoor or outdoor), and to a
> single form of user interaction (either spatial clicks or textual prompts).
> Moreover, training on multiple datasets often leads to negative transfer,
> resulting in domain-specific tools that lack generalizability. To address these
> limitations, we present \textbf{SNAP} (\textbf{S}egment a\textbf{N}ything in
> \textbf{A}ny \textbf{P}oint cloud), a unified model for interactive 3D
> segmentation that supports both point-based and text-based prompts across
> diverse domains. Our approach achieves cross-domain generalizability by
> training on 7 datasets spanning indoor, outdoor, and aerial environments, while
> employing domain-adaptive normalization to prevent negative transfer. For
> text-prompted segmentation, we automatically generate mask proposals without
> human intervention and match them against CLIP embeddings of textual queries,
> enabling both panoptic and open-vocabulary segmentation. Extensive experiments
> demonstrate that SNAP consistently delivers high-quality segmentation results.
> We achieve state-of-the-art performance on 8 out of 9 zero-shot benchmarks for
> spatial-prompted segmentation and demonstrate competitive results on all 5
> text-prompted benchmarks. These results show that a unified model can match or
> exceed specialized domain-specific approaches, providing a practical tool for
> scalable 3D annotation. Project page is at, https://neu-vi.github.io/SNAP/

