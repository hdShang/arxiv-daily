---
layout: default
title: MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning
---

# MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning

**arXiv**: [2510.14958v1](https://arxiv.org/abs/2510.14958) | [PDF](https://arxiv.org/pdf/2510.14958.pdf)

**作者**: Weikang Shi, Aldrich Yu, Rongyao Fang, Houxing Ren, Ke Wang, Aojun Zhou, Changyao Tian, Xinyu Fu, Yuxuan Hu, Zimu Lu, Linjiang Huang, Si Liu, Rui Liu, Hongsheng Li

---

## 💡 一句话要点

**提出MathCanvas框架以增强多模态模型在数学推理中的视觉思维链能力**

**关键词**: `多模态数学推理` `视觉思维链` `图表生成` `预训练数据集` `基准评估`

## 📋 核心要点

1. 核心问题：现有视觉思维链方法在数学领域受限于外部工具，难以生成高保真、适时图表。
2. 方法要点：通过视觉操作预训练和策略性视觉辅助推理微调，实现内在视觉思维链。
3. 实验或效果：在MathCanvas-Bench上相对基线提升86%，并泛化至其他数学基准。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have excelled in textual reasoning, they
> struggle with mathematical domains like geometry that intrinsically rely on
> visual aids. Existing approaches to Visual Chain-of-Thought (VCoT) are often
> limited by rigid external tools or fail to generate the high-fidelity,
> strategically-timed diagrams necessary for complex problem-solving. To bridge
> this gap, we introduce MathCanvas, a comprehensive framework designed to endow
> unified Large Multimodal Models (LMMs) with intrinsic VCoT capabilities for
> mathematics. Our approach consists of two phases. First, a Visual Manipulation
> stage pre-trains the model on a novel 15.2M-pair corpus, comprising 10M
> caption-to-diagram pairs (MathCanvas-Imagen) and 5.2M step-by-step editing
> trajectories (MathCanvas-Edit), to master diagram generation and editing.
> Second, a Strategic Visual-Aided Reasoning stage fine-tunes the model on
> MathCanvas-Instruct, a new 219K-example dataset of interleaved visual-textual
> reasoning paths, teaching it when and how to leverage visual aids. To
> facilitate rigorous evaluation, we introduce MathCanvas-Bench, a challenging
> benchmark with 3K problems that require models to produce interleaved
> visual-textual solutions. Our model, BAGEL-Canvas, trained under this
> framework, achieves an 86% relative improvement over strong LMM baselines on
> MathCanvas-Bench, demonstrating excellent generalization to other public math
> benchmarks. Our work provides a complete toolkit-framework, datasets, and
> benchmark-to unlock complex, human-like visual-aided reasoning in LMMs. Project
> Page: https://mathcanvas.github.io/

