---
layout: default
title: Understanding and Harnessing Sparsity in Unified Multimodal Models
---

# Understanding and Harnessing Sparsity in Unified Multimodal Models

**arXiv**: [2512.02351v1](https://arxiv.org/abs/2512.02351) | [PDF](https://arxiv.org/pdf/2512.02351.pdf)

**作者**: Shwai He, Chaorui Deng, Ang Li, Shen Yan

---

## 💡 一句话要点

**提出MoE适应方法以解决统一多模态模型生成组件压缩敏感性问题**

**关键词**: `统一多模态模型` `稀疏激活` `混合专家` `模型压缩` `推理效率`

## 📋 核心要点

1. 核心问题：统一多模态模型在理解与生成任务中存在推理效率低下，生成组件对压缩高度敏感
2. 方法要点：通过训练无关剪枝分析模型组件，引入稀疏激活的MoE适应以恢复生成质量
3. 实验或效果：BAGEL模型激活约半数参数即可达到全模型性能，代码已开源

## 📄 摘要（原文）

> Large multimodal models have achieved remarkable progress in both understanding and generation. Recent efforts pursue unified multimodal models that integrate heterogeneous components to support both capabilities within a single framework. However, such unification introduces inference inefficiencies, e.g., specific tasks or samples may not require the full knowledge or capacity of the unified model. Yet, a systematic understanding of how these inefficiencies manifest across different components remains limited. In this work, we first conduct a systematic analysis of unified multimodal model components using training-free pruning as a probing methodology, considering both depth pruning and width reduction. Our study reveals that the understanding component exhibits notable compressibility in both understanding and generation tasks, which is more pronounced in the latter. In contrast, the generation components are highly sensitive to compression, with performance deteriorating sharply even under moderate compression ratios. To address this limitation, we propose the Mixture-of-Experts (MoE) Adaptation, inspired by the dynamic activation patterns observed across different samples. This approach partitions the generation module into multiple experts and enables sparse activation to restore generation quality. We validate the effectiveness of sparse activation through expert-frozen tuning and further demonstrate that a fully trainable adaptation delivers additional gains. As a result, the adapted BAGEL model achieves performance comparable to the full model while activating only about half of its parameters. The code is released at \href{https://github.com/Shwai-He/SparseUnifiedModel}{this link}.

