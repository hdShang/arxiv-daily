---
layout: default
title: SpatialThinker: Reinforcing 3D Reasoning in Multimodal LLMs via Spatial Rewards
---

# SpatialThinker: Reinforcing 3D Reasoning in Multimodal LLMs via Spatial Rewards

**arXiv**: [2511.07403v1](https://arxiv.org/abs/2511.07403) | [PDF](https://arxiv.org/pdf/2511.07403.pdf)

**作者**: Hunar Batra, Haoqin Tu, Hardy Chen, Yuanze Lin, Cihang Xie, Ronald Clark

---

## 💡 一句话要点

**提出SpatialThinker以增强多模态大语言模型的三维空间推理能力**

**关键词**: `多模态大语言模型` `三维空间推理` `强化学习` `空间奖励` `场景图构建` `视觉问答`

## 📋 核心要点

1. 多模态大语言模型在空间理解方面存在不足，依赖显式3D输入或特定架构修改
2. 通过构建场景图和密集空间奖励，结合强化学习实现结构化空间接地与多步推理
3. 在空间理解和真实世界VQA基准上超越基线模型和GPT-4o，提升基础模型增益

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable progress in
> vision-language tasks, but they continue to struggle with spatial
> understanding. Existing spatial MLLMs often rely on explicit 3D inputs or
> architecture-specific modifications, and remain constrained by large-scale
> datasets or sparse supervision. To address these limitations, we introduce
> SpatialThinker, a 3D-aware MLLM trained with RL to integrate structured spatial
> grounding with multi-step reasoning. The model simulates human-like spatial
> perception by constructing a scene graph of task-relevant objects and spatial
> relations, and reasoning towards an answer via dense spatial rewards.
> SpatialThinker consists of two key contributions: (1) a data synthesis pipeline
> that generates STVQA-7K, a high-quality spatial VQA dataset, and (2) online RL
> with a multi-objective dense spatial reward enforcing spatial grounding.
> SpatialThinker-7B outperforms supervised fine-tuning and the sparse RL baseline
> on spatial understanding and real-world VQA benchmarks, nearly doubling the
> base-model gain compared to sparse RL, and surpassing GPT-4o. These results
> showcase the effectiveness of combining spatial supervision with reward-aligned
> reasoning in enabling robust 3D spatial understanding with limited data and
> advancing MLLMs towards human-level visual reasoning.

