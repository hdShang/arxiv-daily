---
layout: default
title: PowerCLIP: Powerset Alignment for Contrastive Pre-Training
---

# PowerCLIP: Powerset Alignment for Contrastive Pre-Training

**arXiv**: [2511.23170v1](https://arxiv.org/abs/2511.23170) | [PDF](https://arxiv.org/pdf/2511.23170.pdf)

**作者**: Masaki Kawamura, Nakamasa Inoue, Rintaro Yanagi, Hirokatsu Kataoka, Rio Yokota

---

## 💡 一句话要点

**提出PowerCLIP框架，通过幂集对齐解决多图像区域组合语义捕获问题。**

**关键词**: `对比预训练` `幂集对齐` `零样本学习` `图像-文本对齐` `计算效率优化`

## 📋 核心要点

1. 核心问题：现有方法难以捕获跨多个图像区域的组合语义。
2. 方法要点：引入幂集对齐，优化区域到短语的全面对齐，并使用非线性聚合器降低计算复杂度。
3. 实验或效果：在零样本分类和检索任务中超越现有方法，展现组合性和鲁棒性。

## 📄 摘要（原文）

> Contrastive vision-language pre-training frameworks such as CLIP have demonstrated impressive zero-shot performance across a range of vision-language tasks. Recent studies have shown that aligning individual text tokens with specific image patches or regions enhances fine-grained compositional understanding. However, it remains challenging to capture compositional semantics that span multiple image regions. To address this limitation, we propose PowerCLIP, a novel contrastive pre-training framework enhanced by powerset alignment, which exhaustively optimizes region-to-phrase alignments by minimizing the loss defined between powersets of image regions and textual parse trees. Since the naive powerset construction incurs exponential computational cost due to the combinatorial explosion in the number of region subsets, we introduce efficient non-linear aggregators (NLAs) that reduce complexity from O(2^M) to O(M) with respect to the number of regions M, while approximating the exact loss value with arbitrary precision. Our extensive experiments demonstrate that PowerCLIP outperforms state-of-the-art methods in zero-shot classification and retrieval tasks, underscoring the compositionality and robustness of our approach. Our code will be made publicly available.

