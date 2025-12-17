---
layout: default
title: TOMCAT: Test-time Comprehensive Knowledge Accumulation for Compositional Zero-Shot Learning
---

# TOMCAT: Test-time Comprehensive Knowledge Accumulation for Compositional Zero-Shot Learning

**arXiv**: [2510.20162v1](https://arxiv.org/abs/2510.20162) | [PDF](https://arxiv.org/pdf/2510.20162.pdf)

**作者**: Xudong Yan, Songhe Feng

---

## 💡 一句话要点

**提出TOMCAT方法，通过测试时知识积累解决组合零样本学习中的分布偏移问题**

**关键词**: `组合零样本学习` `测试时适应` `多模态原型` `分布偏移` `动态优先级队列` `多模态对齐`

## 📋 核心要点

1. 核心问题：测试时标签空间分布偏移导致性能下降，源于未见属性-对象组合
2. 方法要点：利用无监督数据积累多模态知识，自适应更新原型并引入动态优先级队列
3. 实验或效果：在四个基准数据集上实现最先进性能，支持闭世界和开世界设置

## 📄 摘要（原文）

> Compositional Zero-Shot Learning (CZSL) aims to recognize novel
> attribute-object compositions based on the knowledge learned from seen ones.
> Existing methods suffer from performance degradation caused by the distribution
> shift of label space at test time, which stems from the inclusion of unseen
> compositions recombined from attributes and objects. To overcome the challenge,
> we propose a novel approach that accumulates comprehensive knowledge in both
> textual and visual modalities from unsupervised data to update multimodal
> prototypes at test time. Building on this, we further design an adaptive update
> weight to control the degree of prototype adjustment, enabling the model to
> flexibly adapt to distribution shift during testing. Moreover, a dynamic
> priority queue is introduced that stores high-confidence images to acquire
> visual knowledge from historical images for inference. Considering the semantic
> consistency of multimodal knowledge, we align textual and visual prototypes by
> multimodal collaborative representation learning. Extensive experiments
> indicate that our approach achieves state-of-the-art performance on four
> benchmark datasets under both closed-world and open-world settings. Code will
> be available at https://github.com/xud-yan/TOMCAT .

