---
layout: default
title: Sliding Window Attention Adaptation
---

# Sliding Window Attention Adaptation

**arXiv**: [2512.10411v1](https://arxiv.org/abs/2512.10411) | [PDF](https://arxiv.org/pdf/2512.10411.pdf)

**作者**: Yijiong Yu, Jiale Liu, Qingyun Wu, Huazheng Wang, Ji Pei

---

## 💡 一句话要点

**提出滑动窗口注意力适应方法，以低成本适配全注意力预训练模型至长上下文推理。**

**关键词**: `滑动窗口注意力` `长上下文推理` `注意力机制适配` `Transformer模型` `性能效率权衡`

## 📋 核心要点

1. 核心问题：全注意力预训练模型直接应用滑动窗口注意力导致长上下文性能下降。
2. 方法要点：结合五种策略，如仅预填充时应用滑动窗口、保留sink令牌、层间交错等。
3. 实验或效果：特定组合能有效恢复性能，提供不同场景的推荐配置。

## 📄 摘要（原文）

> The self-attention mechanism in Transformer-based Large Language Models (LLMs) scales quadratically with input length, making long-context inference expensive. Sliding window attention (SWA) reduces this cost to linear complexity, but naively enabling complete SWA at inference-time for models pretrained with full attention (FA) causes severe long-context performance degradation due to training-inference mismatch. This makes us wonder: Can FA-pretrained LLMs be well adapted to SWA without pretraining? We investigate this by proposing Sliding Window Attention Adaptation (SWAA), a set of practical recipes that combine five methods for better adaptation: (1) applying SWA only during prefilling; (2) preserving "sink" tokens; (3) interleaving FA/SWA layers; (4) chain-of-thought (CoT); and (5) fine-tuning. Our experiments show that SWA adaptation is feasible while non-trivial: no single method suffices, yet specific synergistic combinations effectively recover the original long-context performance. We further analyze the performance-efficiency trade-offs of different SWAA configurations and provide recommended recipes for diverse scenarios. Our code is available at https://github.com/yuyijiong/sliding-window-attention-adaptation

