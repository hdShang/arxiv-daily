---
layout: default
title: A Geometric Unification of Concept Learning with Concept Cones
---

# A Geometric Unification of Concept Learning with Concept Cones

**arXiv**: [2512.07355v1](https://arxiv.org/abs/2512.07355) | [PDF](https://arxiv.org/pdf/2512.07355.pdf)

**作者**: Alexandre Rocchi--Henry, Thomas Fel, Gianni Franchi

---

## 💡 一句话要点

**提出概念锥几何框架，统一监督与非监督概念学习，并建立量化评估指标。**

**关键词**: `概念学习` `几何框架` `稀疏自编码器` `概念瓶颈模型` `可解释性` `量化评估`

## 📋 核心要点

1. 核心问题：监督与非监督概念学习方法（如CBM与SAE）缺乏统一框架与量化评估标准。
2. 方法要点：将CBM与SAE统一为学习激活空间中的线性方向，其非负组合形成概念锥，并基于锥包含关系建立评估指标。
3. 实验或效果：发现稀疏性与扩展因子的“甜点”，最大化与CBM概念的几何和语义对齐。

## 📄 摘要（原文）

> Two traditions of interpretability have evolved side by side but seldom spoken to each other: Concept Bottleneck Models (CBMs), which prescribe what a concept should be, and Sparse Autoencoders (SAEs), which discover what concepts emerge. While CBMs use supervision to align activations with human-labeled concepts, SAEs rely on sparse coding to uncover emergent ones. We show that both paradigms instantiate the same geometric structure: each learns a set of linear directions in activation space whose nonnegative combinations form a concept cone. Supervised and unsupervised methods thus differ not in kind but in how they select this cone. Building on this view, we propose an operational bridge between the two paradigms. CBMs provide human-defined reference geometries, while SAEs can be evaluated by how well their learned cones approximate or contain those of CBMs. This containment framework yields quantitative metrics linking inductive biases -- such as SAE type, sparsity, or expansion ratio -- to emergence of plausible\footnote{We adopt the terminology of \citet{jacovi2020towards}, who distinguish between faithful explanations (accurately reflecting model computations) and plausible explanations (aligning with human intuition and domain knowledge). CBM concepts are plausible by construction -- selected or annotated by humans -- though not necessarily faithful to the true latent factors that organise the data manifold.} concepts. Using these metrics, we uncover a ``sweet spot'' in both sparsity and expansion factor that maximizes both geometric and semantic alignment with CBM concepts. Overall, our work unifies supervised and unsupervised concept discovery through a shared geometric framework, providing principled metrics to measure SAE progress and assess how well discovered concept align with plausible human concepts.

