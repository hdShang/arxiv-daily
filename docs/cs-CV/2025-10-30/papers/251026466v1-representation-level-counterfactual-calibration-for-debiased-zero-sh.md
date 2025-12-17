---
layout: default
title: Representation-Level Counterfactual Calibration for Debiased Zero-Shot Recognition
---

# Representation-Level Counterfactual Calibration for Debiased Zero-Shot Recognition

**arXiv**: [2510.26466v1](https://arxiv.org/abs/2510.26466) | [PDF](https://arxiv.org/pdf/2510.26466.pdf)

**作者**: Pei Peng, MingKun Xie, Hang Hao, Tong Jin, ShengJun Huang

---

## 💡 一句话要点

**提出表示级反事实校准方法以解决零样本识别中的对象-上下文偏见问题**

**关键词**: `零样本识别` `反事实校准` `视觉语言模型` `因果推理` `表示学习` `偏见缓解`

## 📋 核心要点

1. 核心问题：视觉语言模型在零样本识别中因对象-上下文捷径而不可靠，测试场景与训练共现不同时性能下降
2. 方法要点：在CLIP表示空间中估计对象和背景期望，合成反事实嵌入以模拟对象在不同环境中的预测
3. 实验或效果：无需重训练或提示设计，在上下文敏感基准上显著提升最差组和平均准确率

## 📄 摘要（原文）

> Object-context shortcuts remain a persistent challenge in vision-language
> models, undermining zero-shot reliability when test-time scenes differ from
> familiar training co-occurrences. We recast this issue as a causal inference
> problem and ask: Would the prediction remain if the object appeared in a
> different environment? To answer this at inference time, we estimate object and
> background expectations within CLIP's representation space, and synthesize
> counterfactual embeddings by recombining object features with diverse
> alternative contexts sampled from external datasets, batch neighbors, or
> text-derived descriptions. By estimating the Total Direct Effect and simulating
> intervention, we further subtract background-only activation, preserving
> beneficial object-context interactions while mitigating hallucinated scores.
> Without retraining or prompt design, our method substantially improves both
> worst-group and average accuracy on context-sensitive benchmarks, establishing
> a new zero-shot state of the art. Beyond performance, our framework provides a
> lightweight representation-level counterfactual approach, offering a practical
> causal avenue for debiased and reliable multimodal reasoning.

