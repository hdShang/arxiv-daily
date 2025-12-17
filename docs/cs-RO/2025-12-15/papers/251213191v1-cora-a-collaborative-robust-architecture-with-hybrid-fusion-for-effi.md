---
layout: default
title: CoRA: A Collaborative Robust Architecture with Hybrid Fusion for Efficient Perception
---

# CoRA: A Collaborative Robust Architecture with Hybrid Fusion for Efficient Perception

**arXiv**: [2512.13191v1](https://arxiv.org/abs/2512.13191) | [PDF](https://arxiv.org/pdf/2512.13191.pdf)

**作者**: Gong Chen, Chaokun Zhang, Pengcheng Lv, Xiaohui Xie

---

## 💡 一句话要点

**提出CoRA架构，通过混合融合解决协作感知在恶劣通信下的性能下降问题。**

**关键词**: `协作感知` `混合融合` `鲁棒性` `通信效率` `特征融合` `对象校正`

## 📋 核心要点

1. 核心问题：现有协作感知方法在通信条件不佳时性能下降，因数据传输导致特征错位。
2. 方法要点：结合中间融合和后期融合优势，设计特征级融合分支和对象级校正分支。
3. 实验或效果：在极端场景下，AP@0.7提升约19%，通信量减少5倍以上。

## 📄 摘要（原文）

> Collaborative perception has garnered significant attention as a crucial technology to overcome the perceptual limitations of single-agent systems. Many state-of-the-art (SOTA) methods have achieved communication efficiency and high performance via intermediate fusion. However, they share a critical vulnerability: their performance degrades under adverse communication conditions due to the misalignment induced by data transmission, which severely hampers their practical deployment. To bridge this gap, we re-examine different fusion paradigms, and recover that the strengths of intermediate and late fusion are not a trade-off, but a complementary pairing. Based on this key insight, we propose CoRA, a novel collaborative robust architecture with a hybrid approach to decouple performance from robustness with low communication. It is composed of two components: a feature-level fusion branch and an object-level correction branch. Its first branch selects critical features and fuses them efficiently to ensure both performance and scalability. The second branch leverages semantic relevance to correct spatial displacements, guaranteeing resilience against pose errors. Experiments demonstrate the superiority of CoRA. Under extreme scenarios, CoRA improves upon its baseline performance by approximately 19% in AP@0.7 with more than 5x less communication volume, which makes it a promising solution for robust collaborative perception.

