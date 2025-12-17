---
layout: default
title: NeuCLIP: Efficient Large-Scale CLIP Training with Neural Normalizer Optimization
---

# NeuCLIP: Efficient Large-Scale CLIP Training with Neural Normalizer Optimization

**arXiv**: [2511.08417v1](https://arxiv.org/abs/2511.08417) | [PDF](https://arxiv.org/pdf/2511.08417.pdf)

**作者**: Xiyuan Wei, Chih-Jen Lin, Tianbao Yang

---

## 💡 一句话要点

**提出NeuCLIP以优化CLIP训练中的归一化项估计，提升大规模数据集效率**

**关键词**: `对比学习` `归一化优化` `CLIP训练` `大规模数据集` `神经网络估计`

## 📋 核心要点

1. 核心问题：CLIP对比损失中归一化项估计依赖大批次，计算资源需求高
2. 方法要点：通过凸分析和变分分析，将归一化项估计转化为神经网络优化问题
3. 实验或效果：在大规模数据集上优于先前方法，提升训练性能

## 📄 摘要（原文）

> Accurately estimating the normalization term (also known as the partition function) in the contrastive loss is a central challenge for training Contrastive Language-Image Pre-training (CLIP) models. Conventional methods rely on large batches for approximation, demanding substantial computational resources. To mitigate this issue, prior works introduced per-sample normalizer estimators, which are updated at each epoch in a blockwise coordinate manner to keep track of updated encoders. However, this scheme incurs optimization error that scales with the ratio of dataset size to batch size, limiting effectiveness for large datasets or small batches. To overcome this limitation, we propose NeuCLIP, a novel and elegant optimization framework based on two key ideas: (i) $\textbf{reformulating}$ the contrastive loss for each sample $\textbf{via convex analysis}$ into a minimization problem with an auxiliary variable representing its log-normalizer; and (ii) $\textbf{transforming}$ the resulting minimization over $n$ auxiliary variables (where $n$ is the dataset size) via $\textbf{variational analysis}$ into the minimization over a compact neural network that predicts the log-normalizers. We design an alternating optimization algorithm that jointly trains the CLIP model and the auxiliary network. By employing a tailored architecture and acceleration techniques for the auxiliary network, NeuCLIP achieves more accurate normalizer estimation, leading to improved performance compared with previous methods. Extensive experiments on large-scale CLIP training, spanning datasets from millions to billions of samples, demonstrate that NeuCLIP outperforms previous methods.

