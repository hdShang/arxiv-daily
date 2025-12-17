---
layout: default
title: SCOPE: Language Models as One-Time Teacher for Hierarchical Planning in Text Environments
---

# SCOPE: Language Models as One-Time Teacher for Hierarchical Planning in Text Environments

**arXiv**: [2512.09897v1](https://arxiv.org/abs/2512.09897) | [PDF](https://arxiv.org/pdf/2512.09897.pdf)

**作者**: Haoye Lu, Pavan Seshadri, Kaheer Suleman

---

## 💡 一句话要点

**提出SCOPE方法，利用LLM生成子目标一次性预训练轻量模型，以高效解决文本环境中的分层规划问题。**

**关键词**: `分层规划` `文本环境` `语言模型蒸馏` `子目标生成` `高效推理` `预训练模型`

## 📋 核心要点

1. 核心问题：文本环境中长期规划面临开放动作空间、模糊观察和稀疏反馈，现有方法依赖重复查询LLM，计算成本高且缺乏适应性。
2. 方法要点：SCOPE通过LLM生成子目标仅用于初始化，预训练学生模型，避免训练和推理中的重复查询，提升效率但可能牺牲解释性和子目标最优性。
3. 实验或效果：在TextCraft环境中，SCOPE达到0.56成功率，优于ADaPT的0.52，推理时间从164.4秒降至3.0秒，显著提升效率。

## 📄 摘要（原文）

> Long-term planning in complex, text-based environments presents significant challenges due to open-ended action spaces, ambiguous observations, and sparse feedback. Recent research suggests that large language models (LLMs) encode rich semantic knowledge about the world, which can be valuable for guiding agents in high-level reasoning and planning across both embodied and purely textual settings. However, existing approaches often depend heavily on querying LLMs during training and inference, making them computationally expensive and difficult to deploy efficiently. In addition, these methods typically employ a pretrained, unaltered LLM whose parameters remain fixed throughout training, providing no opportunity for adaptation to the target task. To address these limitations, we introduce SCOPE (Subgoal-COnditioned Pretraining for Efficient planning), a one-shot hierarchical planner that leverages LLM-generated subgoals only at initialization to pretrain a lightweight student model. Unlike prior approaches that distill LLM knowledge by repeatedly prompting the model to adaptively generate subgoals during training, our method derives subgoals directly from example trajectories. This design removes the need for repeated LLM queries, significantly improving efficiency, though at the cost of reduced explainability and potentially suboptimal subgoals. Despite their suboptimality, our results on the TextCraft environment show that LLM-generated subgoals can still serve as a strong starting point for hierarchical goal decomposition in text-based planning tasks. Compared to the LLM-based hierarchical agent ADaPT (Prasad et al., 2024), which achieves a 0.52 success rate, our method reaches 0.56 and reduces inference time from 164.4 seconds to just 3.0 seconds.

