---
layout: default
title: OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection
---

# OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection

**arXiv**: [2511.21064v1](https://arxiv.org/abs/2511.21064) | [PDF](https://arxiv.org/pdf/2511.21064.pdf)

**作者**: Chujie Wang, Jianyu Lu, Zhiyuan Luo, Xi Chen, Chu He

---

## 💡 一句话要点

**提出OVOD-Agent框架，通过主动视觉推理与自进化检测解决开放词汇目标检测的泛化问题**

**关键词**: `开放词汇目标检测` `弱马尔可夫决策过程` `Bandit探索` `视觉推理链` `自进化检测` `奖励模型优化`

## 📋 核心要点

1. 核心问题：开放词汇目标检测在推理时依赖固定类别名，导致多模态训练与单模态推理间存在差距
2. 方法要点：基于弱马尔可夫决策过程建模视觉上下文，结合Bandit模块探索不确定区域并优化奖励模型
3. 实验或效果：在COCO和LVIS数据集上验证，对稀有类别检测效果提升显著，兼容多种OVOD骨干网络

## 📄 摘要（原文）

> Open-Vocabulary Object Detection (OVOD) aims to enable detectors to generalize across categories by leveraging semantic information. Although existing methods are pretrained on large vision-language datasets, their inference is still limited to fixed category names, creating a gap between multimodal training and unimodal inference. Previous work has shown that improving textual representation can significantly enhance OVOD performance, indicating that the textual space is still underexplored. To this end, we propose OVOD-Agent, which transforms passive category matching into proactive visual reasoning and self-evolving detection. Inspired by the Chain-of-Thought (CoT) paradigm, OVOD-Agent extends the textual optimization process into an interpretable Visual-CoT with explicit actions. OVOD's lightweight nature makes LLM-based management unsuitable; instead, we model visual context transitions as a Weakly Markovian Decision Process (w-MDP) over eight state spaces, which naturally represents the agent's state, memory, and interaction dynamics. A Bandit module generates exploration signals under limited supervision, helping the agent focus on uncertain regions and adapt its detection policy. We further integrate Markov transition matrices with Bandit trajectories for self-supervised Reward Model (RM) optimization, forming a closed loop from Bandit exploration to RM learning. Experiments on COCO and LVIS show that OVOD-Agent provides consistent improvements across OVOD backbones, particularly on rare categories, confirming the effectiveness of the proposed framework.

