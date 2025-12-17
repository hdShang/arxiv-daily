---
layout: default
title: System Report for CCL25-Eval Task 10: Prompt-Driven Large Language Model Merge for Fine-Grained Chinese Hate Speech Detection
---

# System Report for CCL25-Eval Task 10: Prompt-Driven Large Language Model Merge for Fine-Grained Chinese Hate Speech Detection

**arXiv**: [2512.09563v1](https://arxiv.org/abs/2512.09563) | [PDF](https://arxiv.org/pdf/2512.09563.pdf)

**作者**: Binglin Wu, Jiaxiu Zou, Xianneng Li

---

## 💡 一句话要点

**提出基于提示工程、监督微调和模型合并的三阶段LLM框架，以提升中文细粒度仇恨言论检测性能。**

**关键词**: `仇恨言论检测` `大语言模型` `提示工程` `模型合并` `细粒度分类`

## 📋 核心要点

1. 核心问题：中文社交媒体仇恨言论泛滥，传统系统难以处理语境依赖的修辞策略和演变俚语。
2. 方法要点：设计上下文感知提示引导LLM提取隐含仇恨模式，通过监督微调集成任务特征，合并微调模型增强鲁棒性。
3. 实验或效果：在STATE-ToxiCN基准上验证框架有效性，性能优于基线方法。

## 📄 摘要（原文）

> The proliferation of hate speech on Chinese social media poses urgent societal risks, yet traditional systems struggle to decode context-dependent rhetorical strategies and evolving slang. To bridge this gap, we propose a novel three-stage LLM-based framework: Prompt Engineering, Supervised Fine-tuning, and LLM Merging. First, context-aware prompts are designed to guide LLMs in extracting implicit hate patterns. Next, task-specific features are integrated during supervised fine-tuning to enhance domain adaptation. Finally, merging fine-tuned LLMs improves robustness against out-of-distribution cases. Evaluations on the STATE-ToxiCN benchmark validate the framework's effectiveness, demonstrating superior performance over baseline methods in detecting fine-grained hate speech.

