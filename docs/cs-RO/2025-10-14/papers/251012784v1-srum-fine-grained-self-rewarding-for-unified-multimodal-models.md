---
layout: default
title: SRUM: Fine-Grained Self-Rewarding for Unified Multimodal Models
---

# SRUM: Fine-Grained Self-Rewarding for Unified Multimodal Models

**arXiv**: [2510.12784v1](https://arxiv.org/abs/2510.12784) | [PDF](https://arxiv.org/pdf/2510.12784.pdf)

**作者**: Weiyang Jin, Yuwei Niu, Jiaqi Liao, Chengqi Duan, Aoxue Li, Shenghua Gao, Xihui Liu

---

## 💡 一句话要点

**提出SRUM自奖励框架以解决统一多模态模型中视觉理解与生成能力不匹配问题**

**关键词**: `统一多模态模型` `自奖励学习` `视觉生成` `理解-生成对齐` `多尺度奖励` `后训练框架`

## 📋 核心要点

1. 核心问题：统一多模态模型中视觉理解能力无法有效迁移到视觉生成，导致生成图像不忠实
2. 方法要点：设计全局-局部双奖励系统，利用理解模块作为内部评估器提供多尺度反馈信号
3. 实验或效果：在T2I-CompBench和T2I-ReasonBench基准上性能显著提升，无需额外人工标注数据

## 📄 摘要（原文）

> Recently, remarkable progress has been made in Unified Multimodal Models
> (UMMs), which integrate vision-language generation and understanding
> capabilities within a single framework. However, a significant gap exists where
> a model's strong visual understanding often fails to transfer to its visual
> generation. A model might correctly understand an image based on user
> instructions, yet be unable to generate a faithful image from text prompts.
> This phenomenon directly raises a compelling question: Can a model achieve
> self-improvement by using its understanding module to reward its generation
> module? To bridge this gap and achieve self-improvement, we introduce SRUM, a
> self-rewarding post-training framework that can be directly applied to existing
> UMMs of various designs. SRUM creates a feedback loop where the model's own
> understanding module acts as an internal ``evaluator'', providing corrective
> signals to improve its generation module, without requiring additional
> human-labeled data. To ensure this feedback is comprehensive, we designed a
> global-local dual reward system. To tackle the inherent structural complexity
> of images, this system offers multi-scale guidance: a \textbf{global reward}
> ensures the correctness of the overall visual semantics and layout, while a
> \textbf{local reward} refines fine-grained, object-level fidelity. SRUM leads
> to powerful capabilities and shows strong generalization, boosting performance
> on T2I-CompBench from 82.18 to \textbf{88.37} and on T2I-ReasonBench from 43.82
> to \textbf{46.75}. Overall, our work establishes a powerful new paradigm for
> enabling a UMMs' understanding module to guide and enhance its own generation
> via self-rewarding.

