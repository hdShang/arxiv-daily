---
layout: default
title: HFS: Holistic Query-Aware Frame Selection for Efficient Video Reasoning
---

# HFS: Holistic Query-Aware Frame Selection for Efficient Video Reasoning

**arXiv**: [2512.11534v1](https://arxiv.org/abs/2512.11534) | [PDF](https://arxiv.org/pdf/2512.11534.pdf)

**作者**: Yiqing Yang, Kin-Man Lam

---

## 💡 一句话要点

**提出端到端可训练的任务自适应框架HFS，通过整体优化解决视频推理中关键帧选择问题。**

**关键词**: `视频理解` `关键帧选择` `端到端训练` `任务自适应` `师生互学习` `整体优化`

## 📋 核心要点

1. 核心问题：传统独立评分方法导致帧选择冗余且无法整体优化，离线伪标签训练限制任务适应性。
2. 方法要点：结合链式思维生成任务特定查询向量，定义连续集级目标函数，通过师生互学习实现端到端优化。
3. 实验或效果：在多个基准测试中显著优于现有方法，验证了框架的有效性。

## 📄 摘要（原文）

> Key frame selection in video understanding presents significant challenges. Traditional top-K selection methods, which score frames independently, often fail to optimize the selection as a whole. This independent scoring frequently results in selecting frames that are temporally clustered and visually redundant. Additionally, training lightweight selectors using pseudo labels generated offline by Multimodal Large Language Models (MLLMs) prevents the supervisory signal from dynamically adapting to task objectives. To address these limitations, we propose an end-to-end trainable, task-adaptive framework for frame selection. A Chain-of-Thought approach guides a Small Language Model (SLM) to generate task-specific implicit query vectors, which are combined with multimodal features to enable dynamic frame scoring. We further define a continuous set-level objective function that incorporates relevance, coverage, and redundancy, enabling differentiable optimization via Gumbel-Softmax to select optimal frame combinations at the set level. Finally, student-teacher mutual learning is employed, where the student selector (SLM) and teacher reasoner (MLLM) are trained to align their frame importance distributions via KL divergence. Combined with cross-entropy loss, this enables end-to-end optimization, eliminating reliance on static pseudo labels. Experiments across various benchmarks, including Video-MME, LongVideoBench, MLVU, and NExT-QA, demonstrate that our method significantly outperforms existing approaches.

