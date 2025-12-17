---
layout: default
title: Mem-MLP: Real-Time 3D Human Motion Generation from Sparse Inputs
---

# Mem-MLP: Real-Time 3D Human Motion Generation from Sparse Inputs

**arXiv**: [2511.16264v1](https://arxiv.org/abs/2511.16264) | [PDF](https://arxiv.org/pdf/2511.16264.pdf)

**作者**: Sinan Mutlu, Georgios F. Angelis, Savas Ozkan, Paul Wisbey, Anastasios Drosou, Mete Ozay

---

## 💡 一句话要点

**提出Mem-MLP方法，从稀疏输入实时生成3D人体运动以提升AR/VR沉浸感**

**关键词**: `3D人体运动生成` `稀疏输入处理` `实时MLP模型` `AR/VR应用` `多任务学习`

## 📋 核心要点

1. AR/VR中仅跟踪头手导致全身运动不完整，需从稀疏传感器数据生成完整运动
2. 方法基于MLP骨干，引入Memory-Block和残差连接，利用可训练码向量补全缺失数据
3. 实验显示预测误差显著降低，在移动HMD上达72 FPS，优化精度与运行时间权衡

## 📄 摘要（原文）

> Realistic and smooth full-body tracking is crucial for immersive AR/VR applications. Existing systems primarily track head and hands via Head Mounted Devices (HMDs) and controllers, making the 3D full-body reconstruction in-complete. One potential approach is to generate the full-body motions from sparse inputs collected from limited sensors using a Neural Network (NN) model. In this paper, we propose a novel method based on a multi-layer perceptron (MLP) backbone that is enhanced with residual connections and a novel NN-component called Memory-Block. In particular, Memory-Block represents missing sensor data with trainable code-vectors, which are combined with the sparse signals from previous time instances to improve the temporal consistency. Furthermore, we formulate our solution as a multi-task learning problem, allowing our MLP-backbone to learn robust representations that boost accuracy. Our experiments show that our method outperforms state-of-the-art baselines by substantially reducing prediction errors. Moreover, it achieves 72 FPS on mobile HMDs that ultimately improves the accuracy-running time tradeoff.

