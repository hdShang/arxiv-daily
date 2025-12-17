---
layout: default
title: Transmit Weights, Not Features: Orthogonal-Basis Aided Wireless Point-Cloud Transmission
---

# Transmit Weights, Not Features: Orthogonal-Basis Aided Wireless Point-Cloud Transmission

**arXiv**: [2512.03819v1](https://arxiv.org/abs/2512.03819) | [PDF](https://arxiv.org/pdf/2512.03819.pdf)

**作者**: Junlin Chang, Yubo Han, Hnag Yue, John S Thompson, Rongke Liu

---

## 💡 一句话要点

**提出基于正交基的无线点云语义传输框架，以在带宽受限下提升重建性能。**

**关键词**: `点云传输` `语义通信` `正交特征` `深度联合信源信道编码` `折叠解码器` `带宽效率`

## 📋 核心要点

1. 核心问题：无线传输3D点云时，带宽限制导致特征冗余和重建质量下降。
2. 方法要点：发送端预测接收端正交特征池的组合权重，而非原始特征，结合折叠解码器实现紧凑表示和几何保真。
3. 实验或效果：在ModelNet40上评估，高带宽下性能与SEPT相当，带宽受限时PSNR和CD指标均有提升，正交化和折叠先验有效。

## 📄 摘要（原文）

> The widespread adoption of depth sensors has substantially lowered the barrier to point-cloud acquisition. This letter proposes a semantic wireless transmission framework for three dimension (3D) point clouds built on Deep Joint Source - Channel Coding (DeepJSCC). Instead of sending raw features, the transmitter predicts combination weights over a receiver-side semantic orthogonal feature pool, enabling compact representations and robust reconstruction. A folding-based decoder deforms a 2D grid into 3D, enforcing manifold continuity while preserving geometric fidelity. Trained with Chamfer Distance (CD) and an orthogonality regularizer, the system is evaluated on ModelNet40 across varying Signal-to-Noise Ratios (SNRs) and bandwidths. Results show performance on par with SEmantic Point cloud Transmission (SEPT) at high bandwidth and clear gains in bandwidth-constrained regimes, with consistent improvements in both Peak Signal-to-Noise Ratio (PSNR) and CD. Ablation experiments confirm the benefits of orthogonalization and the folding prior.

