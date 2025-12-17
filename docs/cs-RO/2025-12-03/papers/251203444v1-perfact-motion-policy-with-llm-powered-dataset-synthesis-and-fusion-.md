---
layout: default
title: PerFACT: Motion Policy with LLM-Powered Dataset Synthesis and Fusion Action-Chunking Transformers
---

# PerFACT: Motion Policy with LLM-Powered Dataset Synthesis and Fusion Action-Chunking Transformers

**arXiv**: [2512.03444v1](https://arxiv.org/abs/2512.03444) | [PDF](https://arxiv.org/pdf/2512.03444.pdf)

**作者**: Davood Soleymanzadeh, Xiao Liang, Minghui Zheng

---

## 💡 一句话要点

**提出PerFACT方法，结合LLM生成多样化工作空间和融合动作分块Transformer，以提升机器人运动规划的泛化性和效率。**

**关键词**: `机器人运动规划` `大语言模型` `数据集合成` `Transformer网络` `动作分块` `泛化性提升`

## 📋 核心要点

1. 核心问题：现有神经运动规划器依赖小规模手动生成数据集，泛化能力有限，且网络架构难以编码关键规划信息。
2. 方法要点：引入MotionGeneralizer，利用LLM生成语义可行工作空间以合成大规模数据集；设计MpiNetsFusion，采用融合动作分块Transformer编码多模态特征。
3. 实验或效果：收集350万轨迹训练MpiNetsFusion，相比先进规划器，在评估任务中规划速度提升数倍。

## 📄 摘要（原文）

> Deep learning methods have significantly enhanced motion planning for robotic manipulators by leveraging prior experiences within planning datasets. However, state-of-the-art neural motion planners are primarily trained on small datasets collected in manually generated workspaces, limiting their generalizability to out-of-distribution scenarios. Additionally, these planners often rely on monolithic network architectures that struggle to encode critical planning information. To address these challenges, we introduce Motion Policy with Dataset Synthesis powered by large language models (LLMs) and Fusion Action-Chunking Transformers (PerFACT), which incorporates two key components. Firstly, a novel LLM-powered workspace generation method, MotionGeneralizer, enables large-scale planning data collection by producing a diverse set of semantically feasible workspaces. Secondly, we introduce Fusion Motion Policy Networks (MpiNetsFusion), a generalist neural motion planner that uses a fusion action-chunking transformer to better encode planning signals and attend to multiple feature modalities. Leveraging MotionGeneralizer, we collect 3.5M trajectories to train and evaluate MpiNetsFusion against state-of-the-art planners, which shows that the proposed MpiNetsFusion can plan several times faster on the evaluated tasks.

