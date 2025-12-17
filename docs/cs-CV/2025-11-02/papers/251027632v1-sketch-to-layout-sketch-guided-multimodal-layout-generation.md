---
layout: default
title: Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation
---

# Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation

**arXiv**: [2510.27632v1](https://arxiv.org/abs/2510.27632) | [PDF](https://arxiv.org/pdf/2510.27632.pdf)

**作者**: Riccardo Brioschi, Aleksandr Alekseev, Emanuele Nevali, Berkay Döner, Omar El Malki, Blagoj Mitrevski, Leandro Kieliger, Mark Collier, Andrii Maksai, Jesse Berent, Claudiu Musat, Efi Kokiopoulou

---

## 💡 一句话要点

**提出基于草图的布局生成方法，以解决用户约束复杂性问题。**

**关键词**: `草图引导布局生成` `多模态Transformer` `合成数据生成` `图形布局` `约束优化` `用户体验`

## 📋 核心要点

1. 核心问题：用户约束在布局生成中复杂，降低可用性。
2. 方法要点：使用多模态Transformer，结合草图和内容资产生成布局。
3. 实验或效果：在公开数据集上超越现有方法，提供直观设计体验。

## 📄 摘要（原文）

> Graphic layout generation is a growing research area focusing on generating
> aesthetically pleasing layouts ranging from poster designs to documents. While
> recent research has explored ways to incorporate user constraints to guide the
> layout generation, these constraints often require complex specifications which
> reduce usability. We introduce an innovative approach exploiting user-provided
> sketches as intuitive constraints and we demonstrate empirically the
> effectiveness of this new guidance method, establishing the sketch-to-layout
> problem as a promising research direction, which is currently under-explored.
> To tackle the sketch-to-layout problem, we propose a multimodal
> transformer-based solution using the sketch and the content assets as inputs to
> produce high quality layouts. Since collecting sketch training data from human
> annotators to train our model is very costly, we introduce a novel and
> efficient method to synthetically generate training sketches at scale. We train
> and evaluate our model on three publicly available datasets: PubLayNet,
> DocLayNet and SlidesVQA, demonstrating that it outperforms state-of-the-art
> constraint-based methods, while offering a more intuitive design experience. In
> order to facilitate future sketch-to-layout research, we release O(200k)
> synthetically-generated sketches for the public datasets above. The datasets
> are available at https://github.com/google-deepmind/sketch_to_layout.

