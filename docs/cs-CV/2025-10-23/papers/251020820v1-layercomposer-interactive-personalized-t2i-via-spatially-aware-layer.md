---
layout: default
title: LayerComposer: Interactive Personalized T2I via Spatially-Aware Layered Canvas
---

# LayerComposer: Interactive Personalized T2I via Spatially-Aware Layered Canvas

**arXiv**: [2510.20820v1](https://arxiv.org/abs/2510.20820) | [PDF](https://arxiv.org/pdf/2510.20820.pdf)

**作者**: Guocheng Gordon Qian, Ruihang Zhang, Tsai-Shien Chen, Yusuf Dalva, Anujraaj Argo Goyal, Willi Menapace, Ivan Skorokhodov, Meng Dong, Arpit Sahni, Daniil Ostashev, Ju Hu, Sergey Tulyakov, Kuan-Chieh Jackson Wang

---

## 💡 一句话要点

**提出LayerComposer框架，通过分层画布和锁定机制解决多主体个性化图像生成的空间控制问题。**

**关键词**: `分层画布` `锁定机制` `多主体生成` `空间控制` `个性化图像生成`

## 📋 核心要点

1. 现有个性化生成模型缺乏空间组合交互控制，且难以扩展到多主体场景。
2. 引入分层画布表示，每个主体独立分层，支持无遮挡组合和直观层操作。
3. 锁定机制保持选定层高保真，其余层灵活适应上下文，实验显示优于现有方法。

## 📄 摘要（原文）

> Despite their impressive visual fidelity, existing personalized generative
> models lack interactive control over spatial composition and scale poorly to
> multiple subjects. To address these limitations, we present LayerComposer, an
> interactive framework for personalized, multi-subject text-to-image generation.
> Our approach introduces two main contributions: (1) a layered canvas, a novel
> representation in which each subject is placed on a distinct layer, enabling
> occlusion-free composition; and (2) a locking mechanism that preserves selected
> layers with high fidelity while allowing the remaining layers to adapt flexibly
> to the surrounding context. Similar to professional image-editing software, the
> proposed layered canvas allows users to place, resize, or lock input subjects
> through intuitive layer manipulation. Our versatile locking mechanism requires
> no architectural changes, relying instead on inherent positional embeddings
> combined with a new complementary data sampling strategy. Extensive experiments
> demonstrate that LayerComposer achieves superior spatial control and identity
> preservation compared to the state-of-the-art methods in multi-subject
> personalized image generation.

