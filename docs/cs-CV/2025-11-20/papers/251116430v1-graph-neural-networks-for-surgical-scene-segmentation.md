---
layout: default
title: Graph Neural Networks for Surgical Scene Segmentation
---

# Graph Neural Networks for Surgical Scene Segmentation

**arXiv**: [2511.16430v1](https://arxiv.org/abs/2511.16430) | [PDF](https://arxiv.org/pdf/2511.16430.pdf)

**作者**: Yihan Li, Nikhil Churamani, Maria Robu, Imanol Luengo, Danail Stoyanov

---

## 💡 一句话要点

**提出图神经网络方法以提升手术场景分割的准确性和解剖一致性**

**关键词**: `图神经网络` `手术场景分割` `Vision Transformer` `长程依赖建模` `解剖一致性`

## 📋 核心要点

1. 核心问题：深度学习模型在遮挡、长程依赖和精细几何结构分割中表现不佳
2. 方法要点：结合Vision Transformer编码器和图神经网络，建模解剖区域空间关系
3. 实验或效果：在基准测试中mIoU和mDice分别提升7-8%和6%，改善稀有结构分割

## 📄 摘要（原文）

> Purpose: Accurate identification of hepatocystic anatomy is critical to preventing surgical complications during laparoscopic cholecystectomy. Deep learning models often struggle with occlusions, long-range dependencies, and capturing the fine-scale geometry of rare structures. This work addresses these challenges by introducing graph-based segmentation approaches that enhance spatial and semantic understanding in surgical scene analyses.
>   Methods: We propose two segmentation models integrating Vision Transformer (ViT) feature encoders with Graph Neural Networks (GNNs) to explicitly model spatial relationships between anatomical regions. (1) A static k Nearest Neighbours (k-NN) graph with a Graph Convolutional Network with Initial Residual and Identity Mapping (GCNII) enables stable long-range information propagation. (2) A dynamic Differentiable Graph Generator (DGG) with a Graph Attention Network (GAT) supports adaptive topology learning. Both models are evaluated on the Endoscapes-Seg50 and CholecSeg8k benchmarks.
>   Results: The proposed approaches achieve up to 7-8% improvement in Mean Intersection over Union (mIoU) and 6% improvement in Mean Dice (mDice) scores over state-of-the-art baselines. It produces anatomically coherent predictions, particularly on thin, rare and safety-critical structures.
>   Conclusion: The proposed graph-based segmentation methods enhance both performance and anatomical consistency in surgical scene segmentation. By combining ViT-based global context with graph-based relational reasoning, the models improve interpretability and reliability, paving the way for safer laparoscopic and robot-assisted surgery through a precise identification of critical anatomical features.

