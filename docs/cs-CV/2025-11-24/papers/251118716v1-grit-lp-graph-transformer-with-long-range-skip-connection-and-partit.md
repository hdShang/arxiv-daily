---
layout: default
title: GRIT-LP: Graph Transformer with Long-Range Skip Connection and Partitioned Spatial Graphs for Accurate Ice Layer Thickness Prediction
---

# GRIT-LP: Graph Transformer with Long-Range Skip Connection and Partitioned Spatial Graphs for Accurate Ice Layer Thickness Prediction

**arXiv**: [2511.18716v1](https://arxiv.org/abs/2511.18716) | [PDF](https://arxiv.org/pdf/2511.18716.pdf)

**作者**: Zesheng Liu, Maryam Rahnemoonfar

---

## 💡 一句话要点

**提出GRIT-LP图变换器，结合分区空间图与长程跳跃连接，以提升极地冰层厚度预测精度**

**关键词**: `图变换器` `冰层厚度预测` `长程跳跃连接` `分区空间图` `时空模式建模` `极地雷达图像`

## 📋 核心要点

1. 核心问题：图变换器在深度建模中易出现过平滑和长程依赖弱化，影响冰层厚度估计。
2. 方法要点：采用分区空间图构建策略和长程跳跃连接机制，增强空间一致性和信息流动。
3. 实验或效果：在根均方误差上优于现有方法24.92%，验证了模型在时空模式建模中的有效性。

## 📄 摘要（原文）

> Graph transformers have demonstrated remarkable capability on complex spatio-temporal tasks, yet their depth is often limited by oversmoothing and weak long-range dependency modeling. To address these challenges, we introduce GRIT-LP, a graph transformer explicitly designed for polar ice-layer thickness estimation from polar radar imagery. Accurately estimating ice layer thickness is critical for understanding snow accumulation, reconstructing past climate patterns and reducing uncertainties in projections of future ice sheet evolution and sea level rise. GRIT-LP combines an inductive geometric graph learning framework with self-attention mechanism, and introduces two major innovations that jointly address challenges in modeling the spatio-temporal patterns of ice layers: a partitioned spatial graph construction strategy that forms overlapping, fully connected local neighborhoods to preserve spatial coherence and suppress noise from irrelevant long-range links, and a long-range skip connection mechanism within the transformer that improves information flow and mitigates oversmoothing in deeper attention layers. We conducted extensive experiments, demonstrating that GRIT-LP outperforms current state-of-the-art methods with a 24.92\% improvement in root mean squared error. These results highlight the effectiveness of graph transformers in modeling spatiotemporal patterns by capturing both localized structural features and long-range dependencies across internal ice layers, and demonstrate their potential to advance data-driven understanding of cryospheric processes.

