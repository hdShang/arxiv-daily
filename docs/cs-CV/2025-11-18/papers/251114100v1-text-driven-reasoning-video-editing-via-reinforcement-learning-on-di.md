---
layout: default
title: Text-Driven Reasoning Video Editing via Reinforcement Learning on Digital Twin Representations
---

# Text-Driven Reasoning Video Editing via Reinforcement Learning on Digital Twin Representations

**arXiv**: [2511.14100v1](https://arxiv.org/abs/2511.14100) | [PDF](https://arxiv.org/pdf/2511.14100.pdf)

**作者**: Yiqing Shen, Chenjia Li, Mathias Unberath

---

## 💡 一句话要点

**提出RIVER模型以解决基于文本推理的视频编辑任务**

**关键词**: `推理视频编辑` `数字孪生表示` `强化学习训练` `隐式查询处理` `多跳推理` `扩散模型编辑`

## 📋 核心要点

1. 核心问题：现有方法需显式描述编辑目标，无法处理基于语义属性或对象关系的隐式查询
2. 方法要点：使用数字孪生表示和大型语言模型进行多跳推理，指导扩散模型执行像素级编辑
3. 实验或效果：在RVEBenchmark和两个额外基准上表现最佳，超越六个基线方法

## 📄 摘要（原文）

> Text-driven video editing enables users to modify video content only using text queries. While existing methods can modify video content if explicit descriptions of editing targets with precise spatial locations and temporal boundaries are provided, these requirements become impractical when users attempt to conceptualize edits through implicit queries referencing semantic properties or object relationships. We introduce reasoning video editing, a task where video editing models must interpret implicit queries through multi-hop reasoning to infer editing targets before executing modifications, and a first model attempting to solve this complex task, RIVER (Reasoning-based Implicit Video Editor). RIVER decouples reasoning from generation through digital twin representations of video content that preserve spatial relationships, temporal trajectories, and semantic attributes. A large language model then processes this representation jointly with the implicit query, performing multi-hop reasoning to determine modifications, then outputs structured instructions that guide a diffusion-based editor to execute pixel-level changes. RIVER training uses reinforcement learning with rewards that evaluate reasoning accuracy and generation quality. Finally, we introduce RVEBenchmark, a benchmark of 100 videos with 519 implicit queries spanning three levels and categories of reasoning complexity specifically for reasoning video editing. RIVER demonstrates best performance on the proposed RVEBenchmark and also achieves state-of-the-art performance on two additional video editing benchmarks (VegGIE and FiVE), where it surpasses six baseline methods.

