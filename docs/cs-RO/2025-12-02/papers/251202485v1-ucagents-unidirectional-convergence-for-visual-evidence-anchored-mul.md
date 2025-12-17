---
layout: default
title: UCAgents: Unidirectional Convergence for Visual Evidence Anchored Multi-Agent Medical Decision-Making
---

# UCAgents: Unidirectional Convergence for Visual Evidence Anchored Multi-Agent Medical Decision-Making

**arXiv**: [2512.02485v1](https://arxiv.org/abs/2512.02485) | [PDF](https://arxiv.org/pdf/2512.02485.pdf)

**作者**: Qianhan Feng, Zhongzhen Huang, Yakun Zhu, Xiaofan Zhang, Qi Dou

---

## 💡 一句话要点

**提出UCAgents框架以解决医学视觉问答中视觉证据与语言推理脱节的问题**

**关键词**: `医学视觉问答` `多智能体系统` `视觉证据锚定` `信息理论分析` `临床决策支持`

## 📋 核心要点

1. 核心问题：视觉语言模型在医学诊断中存在推理脱节，多智能体框架易产生文本噪声且未锚定视觉证据
2. 方法要点：采用分层多智能体结构，通过单向收敛和证据审计限制交互，抑制修辞漂移并增强视觉信号提取
3. 实验或效果：在四个医学VQA基准测试中实现更高准确率（如PathVQA上71.3%）和更低计算成本（令牌成本降低87.7%）

## 📄 摘要（原文）

> Vision-Language Models (VLMs) show promise in medical diagnosis, yet suffer from reasoning detachment, where linguistically fluent explanations drift from verifiable image evidence, undermining clinical trust. Recent multi-agent frameworks simulate Multidisciplinary Team (MDT) debates to mitigate single-model bias, but open-ended discussions amplify textual noise and computational cost while failing to anchor reasoning to visual evidence, the cornerstone of medical decision-making. We propose UCAgents, a hierarchical multi-agent framework enforcing unidirectional convergence through structured evidence auditing. Inspired by clinical workflows, UCAgents forbids position changes and limits agent interactions to targeted evidence verification, suppressing rhetorical drift while amplifying visual signal extraction. In UCAgents, a one-round inquiry discussion is introduced to uncover potential risks of visual-textual misalignment. This design jointly constrains visual ambiguity and textual noise, a dual-noise bottleneck that we formalize via information theory. Extensive experiments on four medical VQA benchmarks show UCAgents achieves superior accuracy (71.3% on PathVQA, +6.0% over state-of-the-art) with 87.7% lower token cost, the evaluation results further confirm that UCAgents strikes a balance between uncovering more visual evidence and avoiding confusing textual interference. These results demonstrate that UCAgents exhibits both diagnostic reliability and computational efficiency critical for real-world clinical deployment. Code is available at https://github.com/fqhank/UCAgents.

