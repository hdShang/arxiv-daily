---
layout: default
title: OpenREAD: Reinforced Open-Ended Reasoing for End-to-End Autonomous Driving with LLM-as-Critic
---

# OpenREAD: Reinforced Open-Ended Reasoing for End-to-End Autonomous Driving with LLM-as-Critic

**arXiv**: [2512.01830v1](https://arxiv.org/abs/2512.01830) | [PDF](https://arxiv.org/pdf/2512.01830.pdf)

**作者**: Songyan Zhang, Wenhui Huang, Zhan Chen, Chua Jiahao Collister, Qihang Huang, Chen Lv

---

## 💡 一句话要点

**提出OpenREAD框架，通过LLM作为评判者实现端到端强化微调，以解决自动驾驶中开放端推理的量化难题。**

**关键词**: `自动驾驶` `强化微调` `开放端推理` `大语言模型` `端到端学习` `思维链标注`

## 📋 核心要点

1. 核心问题：现有两阶段微调方法在自动驾驶中，监督微调泛化有限，强化微调难以量化开放端推理的奖励。
2. 方法要点：构建大规模思维链标注，利用Qwen3大语言模型作为评判者，量化开放端问题的推理质量进行奖励建模。
3. 实验或效果：端到端强化微调在上下游任务中显著提升，在推理和规划基准上达到最先进性能。

## 📄 摘要（原文）

> Recently, two-stage fine-tuning strategies, e.g., acquiring essential driving knowledge through supervised fine-tuning (SFT) and further enhancing decision-making and planning via reinforcement fine-tuning (RFT), have shown strong potential in advancing the knowledge-driven autonomous driving (AD) paradigm. However, the learning nature of SFT still limits the generalization of reasoning, thereby constraining the full potential of driving performance. Meanwhile, current RFT approaches are primarily applied to downstream tasks, since scene understanding is an open-ended problem where corresponding rewards are difficult to quantify. To address these limitations, we propose OpenREAD, an OPEN-ended REasoning reinforced vision-language model (VLM)-based autonomous driving (AD) framework that enables end-to-end RFT across the full spectrum from high-level reasoning to low-level trajectory planning. Specifically, we begin by constructing large-scale Chain-of-Thought (CoT) annotations on open-source driving-related knowledge datasets, and employ the powerful Qwen3 large language model (LLM) as the critic in RFT to quantify reasoning quality for open-ended questions during reward modeling. Extensive experiments confirm that joint end-to-end RFT yields substantial improvements in both upstream and downstream tasks, enabling OpenREAD to achieve state-of-the-art performance on reasoning and planning benchmarks.

