---
layout: default
title: ERMoE: Eigen-Reparameterized Mixture-of-Experts for Stable Routing and Interpretable Specialization
---

# ERMoE: Eigen-Reparameterized Mixture-of-Experts for Stable Routing and Interpretable Specialization

**arXiv**: [2511.10971v1](https://arxiv.org/abs/2511.10971) | [PDF](https://arxiv.org/pdf/2511.10971.pdf)

**作者**: Anzhe Cheng, Shukai Duan, Shixuan Li, Chenzhong Yin, Mingxi Cheng, Heng Ping, Tamoghna Chattopadhyay, Sophia I Thomopoulos, Shahin Nazarian, Paul Thompson, Paul Bogdan

---

## 💡 一句话要点

**提出ERMoE以解决MoE路由不稳定和专家利用不足问题**

**关键词**: `混合专家模型` `稀疏激活` `路由稳定性` `特征向量基` `跨模态检索` `脑年龄预测`

## 📋 核心要点

1. MoE架构中路由器与专家结构不匹配导致路由不稳定和负载不均
2. 使用特征向量基重参数化专家，基于余弦相似度进行内容感知路由
3. 在ImageNet和跨模态检索中实现SOTA，提升脑年龄预测准确率超7%

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) architectures expand model capacity by sparsely activating experts but face two core challenges: misalignment between router logits and each expert's internal structure leads to unstable routing and expert underutilization, and load imbalances create straggler bottlenecks. Standard solutions, such as auxiliary load-balancing losses, can reduce load disparities but often weaken expert specialization and hurt downstream performance. To address these issues, we propose ERMoE, a sparse MoE transformer that reparameterizes each expert in a learned orthonormal eigenbasis and replaces learned gating logits with an "Eigenbasis Score", defined as the cosine similarity between input features and an expert's basis. This content-aware routing ties token assignments directly to experts' representation spaces, stabilizing utilization and promoting interpretable specialization without sacrificing sparsity. Crucially, ERMoE removes the need for explicit balancing losses and avoids the interfering gradients they introduce. We show that ERMoE achieves state-of-the-art accuracy on ImageNet classification and cross-modal image-text retrieval benchmarks (e.g., COCO, Flickr30K), while naturally producing flatter expert load distributions. Moreover, a 3D MRI variant (ERMoE-ba) improves brain age prediction accuracy by more than 7\% and yields anatomically interpretable expert specializations. ERMoE thus introduces a new architectural principle for sparse expert models that directly addresses routing instabilities and enables improved performance with scalable, interpretable specialization.

