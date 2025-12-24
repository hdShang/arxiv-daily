---
layout: default
title: Synthesizing Images on Perceptual Boundaries of ANNs for Uncovering and Manipulating Human Perceptual Variability
---

# Synthesizing Images on Perceptual Boundaries of ANNs for Uncovering and Manipulating Human Perceptual Variability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03641" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03641v1</a>
  <a href="https://arxiv.org/pdf/2505.03641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03641v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03641v1', 'Synthesizing Images on Perceptual Boundaries of ANNs for Uncovering and Manipulating Human Perceptual Variability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Wei, Chi Zhang, Jiachen Zou, Haotian Deng, Dietmar Heinke, Quanying Liu

**分类**: cs.AI

**发布日期**: 2025-05-06

**备注**: accepted at ICML 2025

---

## 💡 一句话要点

**提出BAM框架以揭示和操控人类感知变异性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `感知变异性` `决策机制` `个性化分析` `人工神经网络` `行为实验` `数据集生成` `心理学研究`

## 📋 核心要点

1. 现有方法未能充分揭示人类在决策过程中的感知变异性，缺乏系统性研究。
2. 提出BAM框架，通过感知边界采样与人类行为实验结合，深入探讨个体差异。
3. 通过246名参与者的实验，验证了方法的有效性，生成了丰富的variMNIST数据集。

## 📝 摘要（中文）

人类在认知任务和日常生活中的决策表现出显著的变异性，这种变异性受到任务难度、个人偏好和经历等因素的影响。理解这种个体间的变异性对于揭示人类在面对不确定性和模糊性时所依赖的感知和决策机制至关重要。本文提出了一种计算框架BAM（边界对齐与操控框架），结合了人工神经网络（ANNs）的感知边界采样和人类行为实验，系统性地研究这一现象。我们的感知边界采样算法生成沿ANN决策边界的刺激，内在地诱发显著的感知变异性。通过246名参与者的大规模行为实验进行实证验证，最终形成了包含19,943幅系统标注图像的variMNIST数据集。

## 🔬 方法详解

**问题定义**：本研究旨在解决人类在决策过程中感知变异性缺乏系统性理解的问题。现有方法未能有效捕捉个体差异，导致对决策机制的理解不足。

**核心思路**：论文提出的BAM框架结合了感知边界的采样与行为实验，通过生成刺激来诱发感知变异性，从而更好地理解个体决策差异。

**技术框架**：BAM框架包含两个主要模块：感知边界采样模块和行为实验模块。前者生成沿ANN决策边界的刺激，后者通过实验收集参与者的反应数据。

**关键创新**：最重要的创新在于通过个性化模型对齐和对抗生成，建立了一种可靠的方法来同时预测和操控参与者的感知决策，与现有方法相比，提供了更深层次的个体差异分析。

**关键设计**：在技术细节上，采用了特定的损失函数来优化刺激生成过程，并设计了适应性网络结构以提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，246名参与者在116,715次试验中，使用BAM框架生成的刺激显著提高了对感知变异性的理解，验证了该方法的有效性，并生成了包含19,943幅图像的variMNIST数据集，为后续研究提供了丰富的资源。

## 🎯 应用场景

该研究的潜在应用领域包括个性化教育、心理学研究和人机交互等。通过理解和操控人类的感知变异性，可以为个性化决策支持系统提供新的思路，提升用户体验和决策质量。

## 📄 摘要（原文）

> Human decision-making in cognitive tasks and daily life exhibits considerable variability, shaped by factors such as task difficulty, individual preferences, and personal experiences. Understanding this variability across individuals is essential for uncovering the perceptual and decision-making mechanisms that humans rely on when faced with uncertainty and ambiguity. We present a computational framework BAM (Boundary Alignment & Manipulation framework) that combines perceptual boundary sampling in ANNs and human behavioral experiments to systematically investigate this phenomenon. Our perceptual boundary sampling algorithm generates stimuli along ANN decision boundaries that intrinsically induce significant perceptual variability. The efficacy of these stimuli is empirically validated through large-scale behavioral experiments involving 246 participants across 116,715 trials, culminating in the variMNIST dataset containing 19,943 systematically annotated images. Through personalized model alignment and adversarial generation, we establish a reliable method for simultaneously predicting and manipulating the divergent perceptual decisions of pairs of participants. This work bridges the gap between computational models and human individual difference research, providing new tools for personalized perception analysis.

