---
layout: default
title: Multi-Modal Feature Fusion for Spatial Morphology Analysis of Traditional Villages via Hierarchical Graph Neural Networks
---

# Multi-Modal Feature Fusion for Spatial Morphology Analysis of Traditional Villages via Hierarchical Graph Neural Networks

**arXiv**: [2510.27208v1](https://arxiv.org/abs/2510.27208) | [PDF](https://arxiv.org/pdf/2510.27208.pdf)

**作者**: Jiaxin Zhang, Zehong Zhu, Junye Deng, Yunqin Li, and Bowen Wang

---

## 💡 一句话要点

**提出分层图神经网络融合多源数据以分析传统村落空间形态**

**关键词**: `图神经网络` `多模态融合` `空间形态分析` `传统村落` `分类任务` `联合训练`

## 📋 核心要点

1. 核心问题：村落空间特征消失与景观同质化，现有方法依赖定性分析且数据不足。
2. 方法要点：构建分层图神经网络，结合GCN和GAT，集成多模态特征与关系池机制。
3. 实验效果：联合训练17亚型，平均准确率/F1从0.71/0.83提升至0.82/0.90。

## 📄 摘要（原文）

> Villages areas hold significant importance in the study of human-land
> relationships. However, with the advancement of urbanization, the gradual
> disappearance of spatial characteristics and the homogenization of landscapes
> have emerged as prominent issues. Existing studies primarily adopt a
> single-disciplinary perspective to analyze villages spatial morphology and its
> influencing factors, relying heavily on qualitative analysis methods. These
> efforts are often constrained by the lack of digital infrastructure and
> insufficient data. To address the current research limitations, this paper
> proposes a Hierarchical Graph Neural Network (HGNN) model that integrates
> multi-source data to conduct an in-depth analysis of villages spatial
> morphology. The framework includes two types of nodes-input nodes and
> communication nodes-and two types of edges-static input edges and dynamic
> communication edges. By combining Graph Convolutional Networks (GCN) and Graph
> Attention Networks (GAT), the proposed model efficiently integrates multimodal
> features under a two-stage feature update mechanism. Additionally, based on
> existing principles for classifying villages spatial morphology, the paper
> introduces a relational pooling mechanism and implements a joint training
> strategy across 17 subtypes. Experimental results demonstrate that this method
> achieves significant performance improvements over existing approaches in
> multimodal fusion and classification tasks. Additionally, the proposed joint
> optimization of all sub-types lifts mean accuracy/F1 from 0.71/0.83
> (independent models) to 0.82/0.90, driven by a 6% gain for parcel tasks. Our
> method provides scientific evidence for exploring villages spatial patterns and
> generative logic.

