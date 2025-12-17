---
layout: default
title: Revisiting the Data Sampling in Multimodal Post-training from a Difficulty-Distinguish View
---

# Revisiting the Data Sampling in Multimodal Post-training from a Difficulty-Distinguish View

**arXiv**: [2511.06722v1](https://arxiv.org/abs/2511.06722) | [PDF](https://arxiv.org/pdf/2511.06722.pdf)

**作者**: Jianyu Qi, Ding Zou, Wenrui Yan, Rui Ma, Jiaxu Li, Zhijie Zheng, Zhiguo Yang, Rongchang Zhao

---

## 💡 一句话要点

**提出难度感知采样策略以优化多模态后训练中的样本选择**

**关键词**: `多模态大语言模型` `后训练优化` `难度感知采样` `强化学习` `注意力机制` `图像语义掩码`

## 📋 核心要点

1. 现有后训练范式缺乏量化难度指标，无法策略性筛选样本
2. 引入PISM和CMAB方法，分别通过图像退化和注意力分析评估样本难度
3. 实验显示GRPO应用于难度分层样本优于传统SFT+GRPO，提升模型精度

## 📄 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have spurred
> significant progress in Chain-of-Thought (CoT) reasoning. Building on the
> success of Deepseek-R1, researchers extended multimodal reasoning to
> post-training paradigms based on reinforcement learning (RL), focusing
> predominantly on mathematical datasets. However, existing post-training
> paradigms tend to neglect two critical aspects: (1) The lack of quantifiable
> difficulty metrics capable of strategically screening samples for post-training
> optimization. (2) Suboptimal post-training paradigms that fail to jointly
> optimize perception and reasoning capabilities. To address this gap, we propose
> two novel difficulty-aware sampling strategies: Progressive Image Semantic
> Masking (PISM) quantifies sample hardness through systematic image degradation,
> while Cross-Modality Attention Balance (CMAB) assesses cross-modal interaction
> complexity via attention distribution analysis. Leveraging these metrics, we
> design a hierarchical training framework that incorporates both GRPO-only and
> SFT+GRPO hybrid training paradigms, and evaluate them across six benchmark
> datasets. Experiments demonstrate consistent superiority of GRPO applied to
> difficulty-stratified samples compared to conventional SFT+GRPO pipelines,
> indicating that strategic data sampling can obviate the need for supervised
> fine-tuning while improving model accuracy. Our code will be released at
> https://github.com/qijianyu277/DifficultySampling.

