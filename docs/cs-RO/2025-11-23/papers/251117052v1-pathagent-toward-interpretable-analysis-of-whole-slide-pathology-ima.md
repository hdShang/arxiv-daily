---
layout: default
title: PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning
---

# PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning

**arXiv**: [2511.17052v1](https://arxiv.org/abs/2511.17052) | [PDF](https://arxiv.org/pdf/2511.17052.pdf)

**作者**: Jingyun Chen, Linghan Cai, Zhikang Wang, Yi Huang, Songhan Jiang, Shenjin Huang, Hongpeng Wang, Yongbing Zhang

---

## 💡 一句话要点

**提出PathAgent框架，通过大语言模型代理推理实现全切片病理图像的可解释分析**

**关键词**: `全切片图像分析` `大语言模型代理` `可解释推理` `零样本泛化` `病理诊断辅助`

## 📋 核心要点

1. 核心问题：现有全切片图像分析缺乏显式推理轨迹，导致预测不透明且不可解释。
2. 方法要点：使用无训练LLM代理框架，模拟专家逐步分析，包括导航、感知和执行模块。
3. 实验或效果：在五个数据集上零样本泛化强，超越基线，并获人类病理学家协作评估认可。

## 📄 摘要（原文）

> Analyzing whole-slide images (WSIs) requires an iterative, evidence-driven reasoning process that parallels how pathologists dynamically zoom, refocus, and self-correct while collecting the evidence. However, existing computational pipelines often lack this explicit reasoning trajectory, resulting in inherently opaque and unjustifiable predictions. To bridge this gap, we present PathAgent, a training-free, large language model (LLM)-based agent framework that emulates the reflective, stepwise analytical approach of human experts. PathAgent can autonomously explore WSI, iteratively and precisely locating significant micro-regions using the Navigator module, extracting morphology visual cues using the Perceptor, and integrating these findings into the continuously evolving natural language trajectories in the Executor. The entire sequence of observations and decisions forms an explicit chain-of-thought, yielding fully interpretable predictions. Evaluated across five challenging datasets, PathAgent exhibits strong zero-shot generalization, surpassing task-specific baselines in both open-ended and constrained visual question-answering tasks. Moreover, a collaborative evaluation with human pathologists confirms PathAgent's promise as a transparent and clinically grounded diagnostic assistant.

