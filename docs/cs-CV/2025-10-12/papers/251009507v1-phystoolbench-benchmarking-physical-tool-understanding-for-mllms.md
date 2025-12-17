---
layout: default
title: PhysToolBench: Benchmarking Physical Tool Understanding for MLLMs
---

# PhysToolBench: Benchmarking Physical Tool Understanding for MLLMs

**arXiv**: [2510.09507v1](https://arxiv.org/abs/2510.09507) | [PDF](https://arxiv.org/pdf/2510.09507.pdf)

**作者**: Zixin Zhang, Kanghao Chen, Xingwang Lin, Lutao Jiang, Xu Zheng, Yuanhuiyi Lyu, Litao Guo, Yinchuan Li, Ying-Cong Chen

---

## 💡 一句话要点

**提出PhysToolBench基准以评估多模态大语言模型对物理工具的理解能力**

**关键词**: `物理工具理解` `多模态大语言模型` `视觉问答基准` `具身AI` `工具创造评估`

## 📋 核心要点

1. 核心问题：多模态大语言模型对物理工具的理解能力尚未量化，影响其在具身AI中的应用。
2. 方法要点：构建视觉问答数据集，包含1000+图像-文本对，评估工具识别、理解和创造能力。
3. 实验或效果：评估32个模型，发现工具理解存在显著缺陷，并提出初步解决方案。

## 📄 摘要（原文）

> The ability to use, understand, and create tools is a hallmark of human
> intelligence, enabling sophisticated interaction with the physical world. For
> any general-purpose intelligent agent to achieve true versatility, it must also
> master these fundamental skills. While modern Multimodal Large Language Models
> (MLLMs) leverage their extensive common knowledge for high-level planning in
> embodied AI and in downstream Vision-Language-Action (VLA) models, the extent
> of their true understanding of physical tools remains unquantified. To bridge
> this gap, we present PhysToolBench, the first benchmark dedicated to evaluating
> the comprehension of physical tools by MLLMs. Our benchmark is structured as a
> Visual Question Answering (VQA) dataset comprising over 1,000 image-text pairs.
> It assesses capabilities across three distinct difficulty levels: (1) Tool
> Recognition: Requiring the recognition of a tool's primary function. (2) Tool
> Understanding: Testing the ability to grasp the underlying principles of a
> tool's operation. (3) Tool Creation: Challenging the model to fashion a new
> tool from surrounding objects when conventional options are unavailable. Our
> comprehensive evaluation of 32 MLLMs-spanning proprietary, open-source,
> specialized embodied, and backbones in VLAs-reveals a significant deficiency in
> tool understanding. Furthermore, we provide an in-depth analysis and propose
> preliminary solutions. Code and dataset are publicly available.

