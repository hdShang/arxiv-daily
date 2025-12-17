---
layout: default
title: What really matters for person re-identification? A Mixture-of-Experts Framework for Semantic Attribute Importance
---

# What really matters for person re-identification? A Mixture-of-Experts Framework for Semantic Attribute Importance

**arXiv**: [2512.08697v1](https://arxiv.org/abs/2512.08697) | [PDF](https://arxiv.org/pdf/2512.08697.pdf)

**作者**: Athena Psalta, Vasileios Tsironis, Konstantinos Karantzalos

---

## 💡 一句话要点

**提出MoSAIC-ReID框架以量化行人重识别中语义属性的重要性**

**关键词**: `行人重识别` `属性重要性分析` `专家混合框架` `可解释性` `语义属性`

## 📋 核心要点

1. 核心问题：现有行人重识别模型依赖哪些高层语义属性不透明
2. 方法要点：基于LoRA的专家混合框架，每个专家关联单一属性，通过路由控制分析
3. 实验或效果：在Market-1501和DukeMTMC上实现竞争性能，量化分析属性重要性，揭示服装颜色等关键属性

## 📄 摘要（原文）

> State-of-the-art person re-identification methods achieve impressive accuracy but remain largely opaque, leaving open the question: which high-level semantic attributes do these models actually rely on? We propose MoSAIC-ReID, a Mixture-of-Experts framework that systematically quantifies the importance of pedestrian attributes for re-identification. Our approach uses LoRA-based experts, each linked to a single attribute, and an oracle router that enables controlled attribution analysis. While MoSAIC-ReID achieves competitive performance on Market-1501 and DukeMTMC under the assumption that attribute annotations are available at test time, its primary value lies in providing a large-scale, quantitative study of attribute importance across intrinsic and extrinsic cues. Using generalized linear models, statistical tests, and feature-importance analyses, we reveal which attributes, such as clothing colors and intrinsic characteristics, contribute most strongly, while infrequent cues (e.g. accessories) have limited effect. This work offers a principled framework for interpretable ReID and highlights the requirements for integrating explicit semantic knowledge in practice. Code is available at https://github.com/psaltaath/MoSAIC-ReID

