---
layout: default
title: EfficientXpert: Efficient Domain Adaptation for Large Language Models via Propagation-Aware Pruning
---

# EfficientXpert: Efficient Domain Adaptation for Large Language Models via Propagation-Aware Pruning

**arXiv**: [2511.19935v1](https://arxiv.org/abs/2511.19935) | [PDF](https://arxiv.org/pdf/2511.19935.pdf)

**作者**: Songlin Zhao, Michael Pitts, Zhuwei Qin

---

## 💡 一句话要点

**提出EfficientXpert框架，通过传播感知剪枝和高效适配器更新，实现大语言模型在资源受限环境下的领域自适应。**

**关键词**: `大语言模型` `领域自适应` `模型剪枝` `LoRA微调` `稀疏模型` `传播感知`

## 📋 核心要点

1. 大语言模型在专业领域部署时面临模型过大和现有压缩方法跨领域泛化差的问题。
2. 结合传播感知剪枝准则和高效适配器更新算法，集成到LoRA微调中，一步生成稀疏领域专家模型。
3. 在健康和法律任务中，40%稀疏度下保持98%性能，优于现有方法，揭示领域依赖结构变化。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has increased the demand for domain-specialized variants in areas such as law, healthcare, and finance. However, their large size remains a barrier to deployment in resource-constrained environments, and existing compression methods either generalize poorly across domains or incur high overhead. In this work, we propose \textbf{EfficientXpert}, a lightweight domain-pruning framework that combines a propagation-aware pruning criterion (Foresight Mask) with an efficient adapter-update algorithm (Partial Brain Surgeon). Integrated into the LoRA fine-tuning process, EfficientXpert enables a one-step transformation of general pretrained models into sparse, domain-adapted experts. Across health and legal tasks, it retains up to 98% of dense-model performance at 40% sparsity, outperforming state-of-the-art methods. Further analysis reveals substantial domain-dependent structural shifts that degrade the effectiveness of general pruning masks, underscoring the need for adaptive, domain-aware pruning strategies tailored to each domain.

