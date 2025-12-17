---
layout: default
title: From Features to Reference Points: Lightweight and Adaptive Fusion for Cooperative Autonomous Driving
---

# From Features to Reference Points: Lightweight and Adaptive Fusion for Cooperative Autonomous Driving

**arXiv**: [2511.18757v1](https://arxiv.org/abs/2511.18757) | [PDF](https://arxiv.org/pdf/2511.18757.pdf)

**作者**: Yongqi Zhu, Morui Zhu, Qi Chen, Deyuan Qu, Song Fu, Qing Yang

---

## 💡 一句话要点

**提出RefPtsFusion框架，通过交换参考点实现轻量级协同自动驾驶。**

**关键词**: `协同自动驾驶` `轻量级融合` `参考点交换` `通信优化` `异构感知`

## 📋 核心要点

1. 核心问题：传统协同感知方法通信开销大，难以适应异构车辆模型。
2. 方法要点：车辆交换对象位置等参考点，并采用选择性Top-K查询融合。
3. 实验效果：在M3CAD数据集上，通信开销降低五个数量级，性能稳定。

## 📄 摘要（原文）

> We present RefPtsFusion, a lightweight and interpretable framework for cooperative autonomous driving. Instead of sharing large feature maps or query embeddings, vehicles exchange compact reference points, e.g., objects' positions, velocities, and size information. This approach shifts the focus from "what is seen" to "where to see", creating a sensor- and model-independent interface that works well across vehicles with heterogeneous perception models while greatly reducing communication bandwidth. To enhance the richness of shared information, we further develop a selective Top-K query fusion that selectively adds high-confidence queries from the sender. It thus achieves a strong balance between accuracy and communication cost. Experiments on the M3CAD dataset show that RefPtsFusion maintains stable perception performance while reducing communication overhead by five orders of magnitude, dropping from hundreds of MB/s to only a few KB/s at 5 FPS (frame per second), compared to traditional feature-level fusion methods. Extensive experiments also demonstrate RefPtsFusion's strong robustness and consistent transmission behavior, highlighting its potential for scalable, real-time cooperative driving systems.

