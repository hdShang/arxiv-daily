---
layout: default
title: Teaching by Failure: Counter-Example-Driven Curricula for Transformer Self-Improvement
---

# Teaching by Failure: Counter-Example-Driven Curricula for Transformer Self-Improvement

**arXiv**: [2512.01187v1](https://arxiv.org/abs/2512.01187) | [PDF](https://arxiv.org/pdf/2512.01187.pdf)

**作者**: Harshil Vejendla

---

## 💡 一句话要点

**提出反例驱动课程学习框架，以提升Transformer模型在复杂输入上的鲁棒性。**

**关键词**: `Transformer模型` `课程学习` `反例驱动` `鲁棒性提升` `长度外推` `自动验证`

## 📋 核心要点

1. Transformer模型在训练数据外的长或复杂输入上泛化能力弱。
2. CEDC通过迭代生成反例并微调模型，自动聚焦于失败案例。
3. 实验显示CEDC在算法和自然语言任务上显著提升长度外推和计算效率。

## 📄 摘要（原文）

> Transformer models often exhibit brittle extrapolation, failing on inputs that are longer or structurally more complex than those seen during training. We introduce Counter-Example-Driven Curricula (CEDC), an automated framework that improves model robustness by iteratively focusing on its own failures. At each step, CEDC uses the current model to generate a diverse set of candidate problems, employs a fast, executable verifier to identify incorrect predictions (counter-examples), and then fine-tunes the model on a dataset enriched with these discovered failures. We evaluate CEDC on a suite of algorithmic and natural language tasks, including integer addition, sorting, Dyck-2 language recognition, and three text classification benchmarks. Compared to static training and standard curriculum learning baselines, CEDC achieves up to 30x greater length extrapolation, is 3.75x more computationally efficient than uniform data augmentation, and requires no manual difficulty heuristics. We provide a detailed analysis of the counter-examples, showing how the curriculum naturally adapts to target progressively more complex error modes. Our findings establish verifier-guided, failure-driven learning as a simple, powerful, and efficient paradigm for enhancing the generalization capabilities of Transformer models.

