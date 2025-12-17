---
layout: default
title: Thinking with Programming Vision: Towards a Unified View for Thinking with Images
---

# Thinking with Programming Vision: Towards a Unified View for Thinking with Images

**arXiv**: [2512.03746v1](https://arxiv.org/abs/2512.03746) | [PDF](https://arxiv.org/pdf/2512.03746.pdf)

**作者**: Zirun Guo, Minjie Hong, Feng Zhang, Kai Jia, Tao Jin

---

## 💡 一句话要点

**提出CodeVision框架，通过代码作为通用工具接口，提升多模态大语言模型在图像推理中的鲁棒性与可扩展性。**

**关键词**: `多模态大语言模型` `代码生成工具` `鲁棒性评估` `强化学习` `图像推理`

## 📋 核心要点

1. 揭示当前MLLMs在图像方向变化或自然损坏下性能显著下降的脆弱性问题。
2. 提出基于代码生成的两阶段训练方法，结合SFT和RL优化工具使用策略。
3. 实验表明，该方法在Qwen系列模型上提升了性能，并涌现出灵活工具组合等能力。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) that think with images can interactively use tools to reason about visual inputs, but current approaches often rely on a narrow set of tools with limited real-world necessity and scalability. In this work, we first reveal a critical and previously overlooked weakness: even state-of-the-art MLLMs are surprisingly brittle, showing significant performance degradation on images with simple orientation changes or natural corruptions, underscoring the need for more robust tool-based reasoning. To address this, we propose CodeVision, a flexible and scalable code-as-tool framework where the model generates code as a universal interface to invoke any image operation, moving beyond fixed tool registries. We train our model using a two-stage methodology, beginning with Supervised Fine-Tuning (SFT) on a high-quality dataset curated for complex, multi-turn tool composition and error recovery, followed by Reinforcement Learning (RL) with a novel and dense process reward function to encourage strategic and efficient tool use. To facilitate this research, we construct new SFT and RL datasets and introduce a challenging new benchmark suite designed to rigorously evaluate robustness to orientation changes and multi-tool reasoning. Experiments on Qwen2.5-VL and Qwen3-VL series show that our approach significantly improves model performance and fosters emergent capabilities such as flexible tool composition, efficient chained execution, and robust error recovery from runtime feedback. Code is available at https://github.com/ByteDance-BandAI/CodeVision.

