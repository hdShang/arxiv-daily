---
layout: default
title: "DecoDINO: 3D Human-Scene Contact Prediction with Semantic Classification"
---

# DecoDINO: 3D Human-Scene Contact Prediction with Semantic Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23203" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23203v1</a>
  <a href="https://arxiv.org/pdf/2510.23203.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23203v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23203v1', 'DecoDINO: 3D Human-Scene Contact Prediction with Semantic Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lukas Bierling, Davide Pasero, Fleur Dolmans, Helia Ghasemi, Angelo Broere

**分类**: cs.CV

**发布日期**: 2025-10-27

**🔗 代码/项目**: [GITHUB](https://github.com/DavidePasero/deco/tree)

---

## 💡 一句话要点

**提出DecoDINO以解决人类与场景接触预测问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `接触预测` `三分支网络` `DINOv2` `语义标签` `机器人技术` `增强现实` `虚拟现实`

## 📋 核心要点

1. 现有方法DECO在处理人类与物体的接触预测时存在局限，尤其在软表面和遮挡物的情况下表现不佳。
2. DecoDINO通过引入三分支网络结构和DINOv2编码器，结合平衡损失和交叉注意力机制，提升了接触预测的精度。
3. 在DAMON基准测试中，DecoDINO的二元接触F1分数提高了7%，几何误差减半，并增强了对象级语义标签的预测能力。

## 📝 摘要（中文）

准确的顶点级接触预测是高保真人体与物体交互模型的前提，广泛应用于机器人、增强现实/虚拟现实和行为模拟等领域。DECO是首个用于此任务的野外估计器，但存在局限性，如只能生成二元接触图、对软表面和遮挡物的处理不佳，以及在儿童和假阳性脚接触方面的挑战。为了解决这些问题，本文提出了DecoDINO，一个基于DECO框架的三分支网络，采用了两个DINOv2 ViT-g/14编码器、平衡损失加权以减少偏差，并通过补丁级交叉注意力来改善局部推理。最终，顶点特征通过轻量级多层感知机（MLP）和softmax分配语义接触标签。实验结果表明，DecoDINO在DAMON基准上显著提升了接触预测的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决人类与周围物体之间的顶点级接触预测问题。现有方法DECO在处理软表面、遮挡物和儿童等情况时存在显著不足，导致假阳性接触的产生。

**核心思路**：DecoDINO通过引入三分支网络结构，利用DINOv2 ViT-g/14编码器进行特征提取，并采用平衡损失加权来减少模型偏差，从而提升接触预测的准确性。

**技术框架**：整体架构包括三个主要模块：两个DINOv2编码器用于特征提取，一个轻量级多层感知机（MLP）用于语义标签的分配。补丁级交叉注意力机制用于增强局部推理能力。

**关键创新**：DecoDINO的主要创新在于其三分支网络结构和使用的DINOv2编码器，这使得模型在处理复杂场景时表现更为优越，尤其是在软表面和遮挡物的情况下。

**关键设计**：在损失函数设计上，采用了平衡损失加权策略，以减少模型在不同类别上的偏差。此外，LoRA微调和双编码器的设计被证明是提升模型性能的关键因素。

## 📊 实验亮点

DecoDINO在DAMON基准测试中表现出色，二元接触F1分数提升了7%，几何误差减半，并且成功增强了对象级语义标签的预测能力，超越了挑战基线的表现。

## 🎯 应用场景

该研究的潜在应用领域包括机器人技术、增强现实和虚拟现实等场景，能够显著提升人机交互的自然性和准确性。通过准确的接触预测，能够改善虚拟环境中的物体交互体验，推动行为模拟和智能机器人技术的发展。

## 📄 摘要（原文）

> Accurate vertex-level contact prediction between humans and surrounding objects is a prerequisite for high fidelity human object interaction models used in robotics, AR/VR, and behavioral simulation. DECO was the first in the wild estimator for this task but is limited to binary contact maps and struggles with soft surfaces, occlusions, children, and false-positive foot contacts. We address these issues and introduce DecoDINO, a three-branch network based on DECO's framework. It uses two DINOv2 ViT-g/14 encoders, class-balanced loss weighting to reduce bias, and patch-level cross-attention for improved local reasoning. Vertex features are finally passed through a lightweight MLP with a softmax to assign semantic contact labels. We also tested a vision-language model (VLM) to integrate text features, but the simpler architecture performed better and was used instead. On the DAMON benchmark, DecoDINO (i) raises the binary-contact F1 score by 7$\%$, (ii) halves the geodesic error, and (iii) augments predictions with object-level semantic labels. Ablation studies show that LoRA fine-tuning and the dual encoders are key to these improvements. DecoDINO outperformed the challenge baseline in both tasks of the DAMON Challenge. Our code is available at https://github.com/DavidePasero/deco/tree/main.

