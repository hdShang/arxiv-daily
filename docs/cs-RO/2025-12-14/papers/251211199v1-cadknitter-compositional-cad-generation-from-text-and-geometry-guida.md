---
layout: default
title: CADKnitter: Compositional CAD Generation from Text and Geometry Guidance
---

# CADKnitter: Compositional CAD Generation from Text and Geometry Guidance

**arXiv**: [2512.11199v1](https://arxiv.org/abs/2512.11199) | [PDF](https://arxiv.org/pdf/2512.11199.pdf)

**作者**: Tri Le, Khang Nguyen, Baoru Huang, Tung D. Ta, Anh Nguyen

---

## 💡 一句话要点

**提出CADKnitter框架，通过几何引导扩散采样实现从文本和几何约束的组合式CAD生成。**

**关键词**: `CAD生成` `组合式设计` `扩散模型` `几何约束` `文本引导` `3D建模`

## 📋 核心要点

1. 核心问题：现有单部件CAD生成方法不适用于需语义和几何约束的多部件组装实际应用。
2. 方法要点：采用几何引导扩散采样策略，生成符合给定CAD模型几何约束和设计文本语义约束的互补部件。
3. 实验或效果：构建KnitCAD数据集，包含超31万样本，实验显示方法明显优于其他先进基线。

## 📄 摘要（原文）

> Crafting computer-aided design (CAD) models has long been a painstaking and time-intensive task, demanding both precision and expertise from designers. With the emergence of 3D generation, this task has undergone a transformative impact, shifting not only from visual fidelity to functional utility but also enabling editable CAD designs. Prior works have achieved early success in single-part CAD generation, which is not well-suited for real-world applications, as multiple parts need to be assembled under semantic and geometric constraints. In this paper, we propose CADKnitter, a compositional CAD generation framework with a geometry-guided diffusion sampling strategy. CADKnitter is able to generate a complementary CAD part that follows both the geometric constraints of the given CAD model and the semantic constraints of the desired design text prompt. We also curate a dataset, so-called KnitCAD, containing over 310,000 samples of CAD models, along with textual prompts and assembly metadata that provide semantic and geometric constraints. Intensive experiments demonstrate that our proposed method outperforms other state-of-the-art baselines by a clear margin.

