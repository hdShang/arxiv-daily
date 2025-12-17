---
layout: default
title: MMD-Thinker: Adaptive Multi-Dimensional Thinking for Multimodal Misinformation Detection
---

# MMD-Thinker: Adaptive Multi-Dimensional Thinking for Multimodal Misinformation Detection

**arXiv**: [2511.13242v1](https://arxiv.org/abs/2511.13242) | [PDF](https://arxiv.org/pdf/2511.13242.pdf)

**作者**: Junjie Wu, Guohong Fu

---

## 💡 一句话要点

**提出MMD-Thinker框架，通过自适应多维思考解决多模态虚假信息检测问题**

**关键词**: `多模态虚假信息检测` `自适应多维思考` `指令调优` `强化学习` `MMR数据集` `推理能力增强`

## 📋 核心要点

1. 核心问题：通用多模态大模型在多模态虚假信息检测中推理不足且存在偏见，难以应对快速演变的虚假信息
2. 方法要点：设计定制化思考模式，通过任务特定指令调优和强化学习策略增强推理能力
3. 实验或效果：在领域内外基准数据集上实现最优性能，并构建MMR数据集支持进展

## 📄 摘要（原文）

> Multimodal misinformation floods on various social media, and continues to evolve in the era of AI-generated content (AIGC). The emerged misinformation with low creation cost and high deception poses significant threats to society. While recent studies leverage general-purpose multimodal large language models (MLLMs) to achieve remarkable results in detection, they encounter two critical limitations: (1) Insufficient reasoning, where general-purpose MLLMs often follow the uniform reasoning paradigm but generate inaccurate explanations and judgments, due to the lack of the task-specific knowledge of multimodal misinformation detection. (2) Reasoning biases, where a single thinking mode make detectors a suboptimal path for judgment, struggling to keep pace with the fast-growing and intricate multimodal misinformation. In this paper, we propose MMD-Thinker, a two-stage framework for multimodal misinformation detection through adaptive multi-dimensional thinking. First, we develop tailor-designed thinking mode for multimodal misinformation detection. Second, we adopt task-specific instruction tuning to inject the tailored thinking mode into general-purpose MLLMs. Third, we further leverage reinforcement learning strategy with a mixed advantage function, which incentivizes the reasoning capabilities in trajectories. Furthermore, we construct the multimodal misinformation reasoning (MMR) dataset, encompasses more than 8K image-text pairs with both reasoning processes and classification labels, to make progress in the relam of multimodal misinformation detection. Experimental results demonstrate that our proposed MMD-Thinker achieves state-of-the-art performance on both in-domain and out-of-domain benchmark datasets, while maintaining flexible inference and token usage. Code will be publicly available at Github.

