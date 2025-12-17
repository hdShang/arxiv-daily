---
layout: default
title: Learning by Neighbor-Aware Semantics, Deciding by Open-form Flows: Towards Robust Zero-Shot Skeleton Action Recognition
---

# Learning by Neighbor-Aware Semantics, Deciding by Open-form Flows: Towards Robust Zero-Shot Skeleton Action Recognition

**arXiv**: [2511.09388v1](https://arxiv.org/abs/2511.09388) | [PDF](https://arxiv.org/pdf/2511.09388.pdf)

**作者**: Yang Chen, Miaoge Li, Zhijie Rao, Deze Zeng, Song Guo, Jingcai Guo

---

## 💡 一句话要点

**提出Flora方法以解决零样本骨架动作识别中的语义对齐和分类器僵化问题**

**关键词**: `零样本学习` `骨架动作识别` `语义对齐` `流匹配` `跨模态学习` `鲁棒分类`

## 📋 核心要点

1. 核心问题：零样本骨架动作识别中语义对齐脆弱和分类器决策边界僵化
2. 方法要点：使用邻居感知语义调整和开放形式流分类器提升鲁棒性
3. 实验或效果：在三个基准数据集上验证有效性，仅10%可见数据训练表现优异

## 📄 摘要（原文）

> Recognizing unseen skeleton action categories remains highly challenging due to the absence of corresponding skeletal priors. Existing approaches generally follow an "align-then-classify" paradigm but face two fundamental issues, i.e., (i) fragile point-to-point alignment arising from imperfect semantics, and (ii) rigid classifiers restricted by static decision boundaries and coarse-grained anchors. To address these issues, we propose a novel method for zero-shot skeleton action recognition, termed $\texttt{$\textbf{Flora}$}$, which builds upon $\textbf{F}$lexib$\textbf{L}$e neighb$\textbf{O}$r-aware semantic attunement and open-form dist$\textbf{R}$ibution-aware flow cl$\textbf{A}$ssifier. Specifically, we flexibly attune textual semantics by incorporating neighboring inter-class contextual cues to form direction-aware regional semantics, coupled with a cross-modal geometric consistency objective that ensures stable and robust point-to-region alignment. Furthermore, we employ noise-free flow matching to bridge the modality distribution gap between semantic and skeleton latent embeddings, while a condition-free contrastive regularization enhances discriminability, leading to a distribution-aware classifier with fine-grained decision boundaries achieved through token-level velocity predictions. Extensive experiments on three benchmark datasets validate the effectiveness of our method, showing particularly impressive performance even when trained with only 10\% of the seen data. Code is available at https://github.com/cseeyangchen/Flora.

