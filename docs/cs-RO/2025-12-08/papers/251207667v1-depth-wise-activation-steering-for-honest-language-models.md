---
layout: default
title: Depth-Wise Activation Steering for Honest Language Models
---

# Depth-Wise Activation Steering for Honest Language Models

**arXiv**: [2512.07667v1](https://arxiv.org/abs/2512.07667) | [PDF](https://arxiv.org/pdf/2512.07667.pdf)

**作者**: Gracjan Góral, Marysia Winkels, Steven Basart

---

## 💡 一句话要点

**提出深度激活导向方法以提升语言模型的诚实性**

**关键词**: `激活导向` `诚实性评估` `高斯调度` `训练免费方法` `深度加权`

## 📋 核心要点

1. 核心问题：大型语言模型有时内部知道正确答案却输出错误，属于诚实性而非准确性失败。
2. 方法要点：使用高斯调度在深度上加权激活导向强度，无需训练或微调。
3. 实验或效果：在MASK基准上，高斯调度在七分之六模型中提升诚实性，优于单层和均匀分配基线。

## 📄 摘要（原文）

> Large language models sometimes assert falsehoods despite internally representing the correct answer, failures of honesty rather than accuracy, which undermines auditability and safety. Existing approaches largely optimize factual correctness or depend on retraining and brittle single-layer edits, offering limited leverage over truthful reporting. We present a training-free activation steering method that weights steering strength across network depth using a Gaussian schedule. On the MASK benchmark, which separates honesty from knowledge, we evaluate seven models spanning the LLaMA, Qwen, and Mistral families and find that Gaussian scheduling improves honesty over no-steering and single-layer baselines in six of seven models. Equal-budget ablations on LLaMA-3.1-8B-Instruct and Qwen-2.5-7B-Instruct show the Gaussian schedule outperforms random, uniform, and box-filter depth allocations, indicating that how intervention is distributed across depth materially affects outcomes beyond total strength. The method is simple, model-agnostic, requires no finetuning, and provides a low-cost control knob for eliciting truthful reporting from models' existing capabilities.

