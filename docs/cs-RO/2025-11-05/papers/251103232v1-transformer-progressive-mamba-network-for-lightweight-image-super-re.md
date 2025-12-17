---
layout: default
title: Transformer-Progressive Mamba Network for Lightweight Image Super-Resolution
---

# Transformer-Progressive Mamba Network for Lightweight Image Super-Resolution

**arXiv**: [2511.03232v1](https://arxiv.org/abs/2511.03232) | [PDF](https://arxiv.org/pdf/2511.03232.pdf)

**作者**: Sichen Guo, Wenjie Li, Yuanyang Liu, Guangwei Gao, Jian Yang, Chia-Wen Lin

---

## 💡 一句话要点

**提出T-PMambaSR轻量级超分框架，结合窗口自注意力和渐进Mamba以提升特征表示效率。**

**关键词**: `图像超分辨率` `轻量级模型` `渐进Mamba` `窗口自注意力` `高频细节恢复`

## 📋 核心要点

1. 现有Mamba超分方法缺乏跨尺度细粒度过渡，限制特征表示效率。
2. 集成窗口自注意力与渐进Mamba，实现线性复杂度下的多尺度交互和渐进增强。
3. 实验显示T-PMambaSR性能优于Transformer或Mamba方法，计算成本更低。

## 📄 摘要（原文）

> Recently, Mamba-based super-resolution (SR) methods have demonstrated the
> ability to capture global receptive fields with linear complexity, addressing
> the quadratic computational cost of Transformer-based SR approaches. However,
> existing Mamba-based methods lack fine-grained transitions across different
> modeling scales, which limits the efficiency of feature representation. In this
> paper, we propose T-PMambaSR, a lightweight SR framework that integrates
> window-based self-attention with Progressive Mamba. By enabling interactions
> among receptive fields of different scales, our method establishes a
> fine-grained modeling paradigm that progressively enhances feature
> representation with linear complexity. Furthermore, we introduce an Adaptive
> High-Frequency Refinement Module (AHFRM) to recover high-frequency details lost
> during Transformer and Mamba processing. Extensive experiments demonstrate that
> T-PMambaSR progressively enhances the model's receptive field and
> expressiveness, yielding better performance than recent Transformer- or
> Mamba-based methods while incurring lower computational cost. Our codes will be
> released after acceptance.

