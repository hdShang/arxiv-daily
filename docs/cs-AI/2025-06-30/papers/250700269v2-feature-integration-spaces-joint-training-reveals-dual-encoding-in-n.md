---
layout: default
title: "Feature Integration Spaces: Joint Training Reveals Dual Encoding in Neural Network Representations"
---

# Feature Integration Spaces: Joint Training Reveals Dual Encoding in Neural Network Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00269" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00269v2</a>
  <a href="https://arxiv.org/pdf/2507.00269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00269v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00269v2', 'Feature Integration Spaces: Joint Training Reveals Dual Encoding in Neural Network Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omar Claflin

**分类**: q-bio.NC, cs.AI

**发布日期**: 2025-06-30 (更新: 2025-12-09)

---

## 💡 一句话要点

**提出双重编码机制以提升神经网络可解释性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `神经网络` `稀疏自编码器` `可解释性` `双重编码` `特征整合` `深度学习` `模型优化`

## 📋 核心要点

1. 现有稀疏自编码器方法在消除多义性和行为错误方面存在显著不足，影响了神经网络的可解释性。
2. 本文提出双重编码机制，利用联合训练架构同时捕捉特征身份和整合模式，以提升模型的重建能力和可解释性。
3. 实验结果显示，联合训练实现41.3%的重建改进和51.6%的KL散度减少，且小型非线性组件显著提升模型性能。

## 📝 摘要（中文）

当前的稀疏自编码器(SAE)方法在神经网络可解释性方面假设激活可以通过线性叠加分解为稀疏、可解释的特征。尽管重建精度高，SAE仍然无法消除多义性，并表现出病态的行为错误。本文提出神经网络在同一基质中以两种互补空间编码信息：特征身份和特征整合。为验证这一双重编码假设，开发了顺序和联合训练架构以同时捕捉身份和整合模式。联合训练实现了41.3%的重建改进和51.6%的KL散度错误减少。该架构自发发展出双模态特征组织，低平方范数特征贡献于整合路径，其余特征直接贡献于残差。小型非线性组件（占参数的3%）实现了16.5%的独立改进，展示了参数高效捕捉对行为至关重要的计算关系的能力。干预实验表明，整合特征对实验操控表现出选择性敏感性，并对模型输出产生系统性行为效应。

## 🔬 方法详解

**问题定义**：本文旨在解决现有稀疏自编码器在神经网络可解释性方面的不足，尤其是多义性和行为错误的问题。

**核心思路**：提出双重编码机制，认为神经网络在同一基质中同时编码特征身份和特征整合，通过联合训练来捕捉这两种模式。

**技术框架**：整体架构包括顺序训练和联合训练两个阶段，分别用于捕捉特征身份和整合模式。联合训练阶段通过优化损失函数来实现特征的有效整合。

**关键创新**：最重要的创新在于提出了双重编码的概念，并通过联合训练架构实现了特征的双模态组织，这与传统的线性叠加假设形成鲜明对比。

**关键设计**：在网络结构中引入小型非线性组件，参数占比仅为3%，通过优化损失函数和特征整合策略，实现了显著的性能提升。具体的损失函数设计和参数设置在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，联合训练实现了41.3%的重建精度提升和51.6%的KL散度减少。此外，3%的小型非线性组件独立实现了16.5%的性能提升，展示了其在参数效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括深度学习模型的可解释性提升、计算机视觉任务中的特征提取和整合、以及机器人决策系统中的行为优化。通过提供更清晰的特征理解，未来可以推动智能系统在复杂环境中的应用和发展。

## 📄 摘要（原文）

> Current sparse autoencoder (SAE) approaches to neural network interpretability assume that activations can be decomposed through linear superposition into sparse, interpretable features. Despite high reconstruction fidelity, SAEs consistently fail to eliminate polysemanticity and exhibit pathological behavioral errors. We propose that neural networks encode information in two complementary spaces compressed into the same substrate: feature identity and feature integration. To test this dual encoding hypothesis, we develop sequential and joint-training architectures to capture identity and integration patterns simultaneously. Joint training achieves 41.3% reconstruction improvement and 51.6% reduction in KL divergence errors. This architecture spontaneously develops bimodal feature organization: low squared norm features contributing to integration pathways and the rest contributing directly to the residual. Small nonlinear components (3% of parameters) achieve 16.5% standalone improvements, demonstrating parameter-efficient capture of computational relationships crucial for behavior. Additionally, intervention experiments using 2x2 factorial stimulus designs demonstrated that integration features exhibit selective sensitivity to experimental manipulations and produce systematic behavioral effects on model outputs, including significant statistical interaction effects across semantic dimensions. This work provides systematic evidence for (1) dual encoding in neural representations, (2) meaningful nonlinearly encoded feature interactions, and (3) introduces an architectural paradigm shift from post-hoc feature analysis to integrated computational design, establishing foundations for next-generation SAEs.

