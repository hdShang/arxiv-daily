---
layout: default
title: Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities
---

# Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities

**arXiv**: [2511.14631v1](https://arxiv.org/abs/2511.14631) | [PDF](https://arxiv.org/pdf/2511.14631.pdf)

**作者**: Kahaan Gandhi, Boris Bolliet, Inigo Zubeldia

---

## 💡 一句话要点

**提出基于视觉语言模型的多智能体系统，以增强自主科学发现能力**

**关键词**: `视觉语言模型` `多智能体系统` `自主科学发现` `实时纠错` `图表评估`

## 📋 核心要点

1. 核心问题：传统方法在自主科学发现中易出错，缺乏实时纠错机制。
2. 方法要点：使用VLM作为评判者，通过动态生成领域特定标准评估图表。
3. 实验或效果：在宇宙学和天体化学案例中，系统能自我纠正，基准测试得分显著提升。

## 📄 摘要（原文）

> We show that multi-agent systems guided by vision-language models (VLMs) improve end-to-end autonomous scientific discovery. By treating plots as verifiable checkpoints, a VLM-as-a-judge evaluates figures against dynamically generated domain-specific rubrics, enabling agents to correct their own errors and steer exploratory data analysis in real-time. Case studies in cosmology and astrochemistry demonstrate recovery from faulty reasoning paths and adaptation to new datasets without human intervention. On a 10-task benchmark for data-driven discovery, VLM-augmented systems achieve pass at 1 scores of 0.7-0.8, compared to 0.2-0.3 for code-only and 0.4-0.5 for code-and-text baselines, while also providing auditable reasoning traces that improve interpretability. Code available here: https://github.com/CMBAgents/cmbagent

