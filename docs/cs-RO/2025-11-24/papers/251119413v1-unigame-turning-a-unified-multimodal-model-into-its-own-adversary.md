---
layout: default
title: UniGame: Turning a Unified Multimodal Model Into Its Own Adversary
---

# UniGame: Turning a Unified Multimodal Model Into Its Own Adversary

**arXiv**: [2511.19413v1](https://arxiv.org/abs/2511.19413) | [PDF](https://arxiv.org/pdf/2511.19413.pdf)

**作者**: Zhaolong Su, Wang Lu, Hao Chen, Sharon Li, Jindong Wang

---

## 💡 一句话要点

**提出UniGame自对抗后训练框架以解决统一多模态模型中的不一致性问题**

**关键词**: `统一多模态模型` `自对抗训练` `多模态一致性` `后训练框架` `鲁棒性增强`

## 📋 核心要点

1. 核心问题：统一多模态模型在理解与生成间存在嵌入表示不一致，导致决策边界错位和鲁棒性下降
2. 方法要点：在共享令牌接口应用轻量扰动器，使生成分支主动挑战理解分支以提升一致性
3. 实验或效果：显著提升一致性、理解、生成及分布外和对抗鲁棒性，参数增加小于1%

## 📄 摘要（原文）

> Unified Multimodal Models (UMMs) have shown impressive performance in both understanding and generation with a single architecture. However, UMMs still exhibit a fundamental inconsistency: understanding favors compact embeddings, whereas generation favors reconstruction-rich representations. This structural trade-off produces misaligned decision boundaries, degraded cross-modal coherence, and heightened vulnerability under distributional and adversarial shifts. In this paper, we present UniGame, a self-adversarial post-training framework that directly targets the inconsistencies. By applying a lightweight perturber at the shared token interface, UniGame enables the generation branch to actively seek and challenge fragile understanding, turning the model itself into its own adversary. Experiments demonstrate that UniGame significantly improves the consistency (+4.6%). Moreover, it also achieves substantial improvements in understanding (+3.6%), generation (+0.02), out-of-distribution and adversarial robustness (+4.8% and +6.2% on NaturalBench and AdVQA). The framework is architecture-agnostic, introduces less than 1% additional parameters, and is complementary to existing post-training methods. These results position adversarial self-play as a general and effective principle for enhancing the coherence, stability, and unified competence of future multimodal foundation models. The official code is available at: https://github.com/AIFrontierLab/UniGame

