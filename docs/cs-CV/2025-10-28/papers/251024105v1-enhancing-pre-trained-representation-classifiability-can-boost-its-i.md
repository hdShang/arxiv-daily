---
layout: default
title: Enhancing Pre-trained Representation Classifiability can Boost its Interpretability
---

# Enhancing Pre-trained Representation Classifiability can Boost its Interpretability

**arXiv**: [2510.24105v1](https://arxiv.org/abs/2510.24105) | [PDF](https://arxiv.org/pdf/2510.24105.pdf)

**作者**: Shufan Shen, Zhaobo Qi, Junshu Sun, Qingming Huang, Qi Tian, Shuhui Wang

---

## 💡 一句话要点

**提出Inherent Interpretability Score以量化预训练视觉模型的表示可解释性与可分类性正相关**

**关键词**: `预训练视觉模型` `表示可解释性` `可分类性` `Inherent Interpretability Score` `语义量化` `微调优化`

## 📋 核心要点

1. 核心问题：预训练视觉模型的表示能否同时实现高可解释性和高可分类性
2. 方法要点：基于信息损失定义Inherent Interpretability Score，量化表示中可解释语义的比例
3. 实验或效果：发现可解释性与可分类性正相关，并通过微调提升两者性能

## 📄 摘要（原文）

> The visual representation of a pre-trained model prioritizes the
> classifiability on downstream tasks, while the widespread applications for
> pre-trained visual models have posed new requirements for representation
> interpretability. However, it remains unclear whether the pre-trained
> representations can achieve high interpretability and classifiability
> simultaneously. To answer this question, we quantify the representation
> interpretability by leveraging its correlation with the ratio of interpretable
> semantics within the representations. Given the pre-trained representations,
> only the interpretable semantics can be captured by interpretations, whereas
> the uninterpretable part leads to information loss. Based on this fact, we
> propose the Inherent Interpretability Score (IIS) that evaluates the
> information loss, measures the ratio of interpretable semantics, and quantifies
> the representation interpretability. In the evaluation of the representation
> interpretability with different classifiability, we surprisingly discover that
> the interpretability and classifiability are positively correlated, i.e.,
> representations with higher classifiability provide more interpretable
> semantics that can be captured in the interpretations. This observation further
> supports two benefits to the pre-trained representations. First, the
> classifiability of representations can be further improved by fine-tuning with
> interpretability maximization. Second, with the classifiability improvement for
> the representations, we obtain predictions based on their interpretations with
> less accuracy degradation. The discovered positive correlation and
> corresponding applications show that practitioners can unify the improvements
> in interpretability and classifiability for pre-trained vision models. Codes
> are available at https://github.com/ssfgunner/IIS.

