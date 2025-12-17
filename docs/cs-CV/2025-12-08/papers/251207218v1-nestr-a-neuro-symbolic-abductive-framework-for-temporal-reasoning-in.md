---
layout: default
title: NeSTR: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large Language Models
---

# NeSTR: A Neuro-Symbolic Abductive Framework for Temporal Reasoning in Large Language Models

**arXiv**: [2512.07218v1](https://arxiv.org/abs/2512.07218) | [PDF](https://arxiv.org/pdf/2512.07218.pdf)

**作者**: Feng Liang, Weixin Zeng, Runhao Zhao, Xiang Zhao

---

## 💡 一句话要点

**提出NeSTR框架以增强大语言模型在复杂时间约束下的推理能力**

**关键词**: `时间推理` `神经符号集成` `溯因反思` `零样本学习` `大语言模型` `问答基准`

## 📋 核心要点

1. 核心问题：大语言模型在复杂时间推理中易产生不一致或幻觉，现有方法未能充分利用其推理能力或缺乏结构化表示。
2. 方法要点：NeSTR整合符号编码与混合反思推理，通过符号表示保留时间关系、验证逻辑一致性、使用溯因反思修正错误。
3. 实验或效果：在多个时间问答基准上，NeSTR实现零样本性能提升，无需微调即增强时间推理，展示神经符号集成的优势。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of natural language processing tasks. However, temporal reasoning, particularly under complex temporal constraints, remains a major challenge. To this end, existing approaches have explored symbolic methods, which encode temporal structure explicitly, and reflective mechanisms, which revise reasoning errors through multi-step inference. Nonetheless, symbolic approaches often underutilize the reasoning capabilities of LLMs, while reflective methods typically lack structured temporal representations, which can result in inconsistent or hallucinated reasoning. As a result, even when the correct temporal context is available, LLMs may still misinterpret or misapply time-related information, leading to incomplete or inaccurate answers. To address these limitations, in this work, we propose Neuro-Symbolic Temporal Reasoning (NeSTR), a novel framework that integrates structured symbolic representations with hybrid reflective reasoning to enhance the temporal sensitivity of LLM inference. NeSTR preserves explicit temporal relations through symbolic encoding, enforces logical consistency via verification, and corrects flawed inferences using abductive reflection. Extensive experiments on diverse temporal question answering benchmarks demonstrate that NeSTR achieves superior zero-shot performance and consistently improves temporal reasoning without any fine-tuning, showcasing the advantage of neuro-symbolic integration in enhancing temporal understanding in large language models.

