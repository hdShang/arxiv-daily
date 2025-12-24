---
layout: default
title: "Modern Neural Networks for Small Tabular Datasets: The New Default for Field-Scale Digital Soil Mapping?"
---

# Modern Neural Networks for Small Tabular Datasets: The New Default for Field-Scale Digital Soil Mapping?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09888" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09888v1</a>
  <a href="https://arxiv.org/pdf/2508.09888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09888v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09888v1', 'Modern Neural Networks for Small Tabular Datasets: The New Default for Field-Scale Digital Soil Mapping?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Viacheslav Barkov, Jonas Schmidinger, Robin Gebbers, Martin Atzmueller

**分类**: cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出现代神经网络以解决小型表格数据集的土壤属性预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `土壤属性预测` `人工神经网络` `小型数据集` `数字土壤制图` `机器学习` `深度学习` `模型评估`

## 📋 核心要点

1. 传统机器学习方法在小样本和高特征比的土壤预测任务中表现不佳，限制了其应用。
2. 本文提出了一系列现代ANN架构的基准评估，展示其在田间尺度土壤属性预测中的有效性。
3. 实验结果显示，现代ANN在大多数任务中超越传统方法，TabPFN在不同条件下表现最为稳健。

## 📝 摘要（中文）

在土壤计量学领域，表格机器学习是从遥感和近感土壤数据预测土壤属性的主要方法。由于小样本量和高特征-样本比的限制，传统深度学习方法在田间尺度的预测土壤建模任务中面临挑战。本文引入了对现代人工神经网络（ANN）架构的全面基准评估，结果表明现代ANN在大多数任务中优于传统方法，尤其是TabPFN表现出色，建议将其作为田间尺度土壤属性预测的新标准选择。

## 🔬 方法详解

**问题定义**：本文旨在解决在小型表格数据集上进行土壤属性预测时，传统深度学习方法因样本量小和特征比高而面临的挑战。现有的经典机器学习算法如随机森林和线性模型在这些条件下表现不佳。

**核心思路**：论文通过引入现代人工神经网络（ANN）架构，特别是多层感知器和注意力机制变体，来提升土壤属性预测的性能，旨在证明这些新方法在小样本情况下的有效性。

**技术框架**：研究评估了多种ANN架构，包括TabM、RealMLP、FT-Transformer等，使用31个包含30到460个样本的田间和农场规模数据集，关注土壤有机质、pH值和粘土含量等关键属性。

**关键创新**：最重要的创新在于通过全面基准测试，展示了现代ANN在田间尺度土壤属性预测中的优势，特别是TabPFN在多种条件下的稳健性，挑战了传统方法的主导地位。

**关键设计**：在模型设计上，采用了多层感知器、注意力机制和检索增强的方法，优化了网络结构和损失函数设置，以适应小样本数据集的特性。

## 📊 实验亮点

实验结果表明，现代ANN在大多数任务中超越了传统机器学习方法，尤其是TabPFN在不同条件下表现出色，显示出其在小型数据集上的强大适应性和稳健性，建议将其作为田间尺度土壤属性预测的新标准。

## 🎯 应用场景

该研究的潜在应用领域包括农业、环境监测和土壤管理等，能够为土壤属性的快速准确预测提供新的工具，进而推动数字土壤制图的发展，提升农业生产效率和可持续性。

## 📄 摘要（原文）

> In the field of pedometrics, tabular machine learning is the predominant method for predicting soil properties from remote and proximal soil sensing data, forming a central component of digital soil mapping. At the field-scale, this predictive soil modeling (PSM) task is typically constrained by small training sample sizes and high feature-to-sample ratios in soil spectroscopy. Traditionally, these conditions have proven challenging for conventional deep learning methods. Classical machine learning algorithms, particularly tree-based models like Random Forest and linear models such as Partial Least Squares Regression, have long been the default choice for field-scale PSM. Recent advances in artificial neural networks (ANN) for tabular data challenge this view, yet their suitability for field-scale PSM has not been proven. We introduce a comprehensive benchmark that evaluates state-of-the-art ANN architectures, including the latest multilayer perceptron (MLP)-based models (TabM, RealMLP), attention-based transformer variants (FT-Transformer, ExcelFormer, T2G-Former, AMFormer), retrieval-augmented approaches (TabR, ModernNCA), and an in-context learning foundation model (TabPFN). Our evaluation encompasses 31 field- and farm-scale datasets containing 30 to 460 samples and three critical soil properties: soil organic matter or soil organic carbon, pH, and clay content. Our results reveal that modern ANNs consistently outperform classical methods on the majority of tasks, demonstrating that deep learning has matured sufficiently to overcome the long-standing dominance of classical machine learning for PSM. Notably, TabPFN delivers the strongest overall performance, showing robustness across varying conditions. We therefore recommend the adoption of modern ANNs for field-scale PSM and propose TabPFN as the new default choice in the toolkit of every pedometrician.

