---
layout: default
title: EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards
---

# EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards

**arXiv**: [2511.16672v1](https://arxiv.org/abs/2511.16672) | [PDF](https://arxiv.org/pdf/2511.16672.pdf)

**作者**: Omkat Thawakar, Shravan Venkatraman, Ritesh Thawkar, Abdelrahman Shaker, Hisham Cholakkal, Rao Muhammad Anwer, Salman Khan, Fahad Khan

---

## 💡 一句话要点

**提出EvoLMM框架以无监督方式提升大型多模态模型推理能力**

**关键词**: `大型多模态模型` `无监督学习` `自我进化` `推理能力` `连续奖励` `多模态数学推理`

## 📋 核心要点

1. 核心问题：现有大型多模态模型训练依赖人工数据或外部奖励，限制自主性和可扩展性。
2. 方法要点：使用提议者和求解者双代理，通过内部一致性和连续自奖励实现自我进化。
3. 实验或效果：在ChartQA等基准上，推理准确率提升约3%，仅使用原始训练图像。

## 📄 摘要（原文）

> Recent advances in large multimodal models (LMMs) have enabled impressive reasoning and perception abilities, yet most existing training pipelines still depend on human-curated data or externally verified reward models, limiting their autonomy and scalability. In this work, we strive to improve LMM reasoning capabilities in a purely unsupervised fashion (without any annotated data or reward distillation). To this end, we propose a self-evolving framework, named EvoLMM, that instantiates two cooperative agents from a single backbone model: a Proposer, which generates diverse, image-grounded questions, and a Solver, which solves them through internal consistency, where learning proceeds through a continuous self-rewarding process. This dynamic feedback encourages both the generation of informative queries and the refinement of structured reasoning without relying on ground-truth or human judgments. When using the popular Qwen2.5-VL as the base model, our EvoLMM yields consistent gains upto $\sim$3\% on multimodal math-reasoning benchmarks, including ChartQA, MathVista, and MathVision, using only raw training images. We hope our simple yet effective approach will serve as a solid baseline easing future research in self-improving LMMs in a fully-unsupervised fashion. Our code and models are available at https://github.com/mbzuai-oryx/EvoLMM.

