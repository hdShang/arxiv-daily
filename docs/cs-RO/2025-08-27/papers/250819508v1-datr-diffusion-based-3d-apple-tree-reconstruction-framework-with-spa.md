---
layout: default
title: "DATR: Diffusion-based 3D Apple Tree Reconstruction Framework with Sparse-View"
---

# DATR: Diffusion-based 3D Apple Tree Reconstruction Framework with Sparse-View

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19508" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19508v1</a>
  <a href="https://arxiv.org/pdf/2508.19508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19508v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19508v1', 'DATR: Diffusion-based 3D Apple Tree Reconstruction Framework with Sparse-View')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tian Qiu, Alan Zoubi, Yiyuan Lin, Ruiming Du, Lailiang Cheng, Yu Jiang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出DATR框架以解决稀疏视图下的苹果树3D重建问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D重建` `数字双胞胎` `稀疏视图` `扩散模型` `农业应用` `隐式神经场` `机器人仿真`

## 📋 核心要点

1. 现有的3D重建方法在稀疏和遮挡视图下表现不佳，难以满足农业数字双胞胎的需求。
2. DATR框架通过两阶段流程，首先生成树木掩膜，然后利用扩散模型和重建模型进行3D重建，有效解决了稀疏视图问题。
3. 实验结果表明，DATR框架在多个数据集上均优于现有方法，且在特征估计上与激光扫描仪相当，吞吐量提升显著。

## 📝 摘要（中文）

数字双胞胎应用通过准确的物理资产虚拟复制，实现实时监控和机器人仿真，具有变革潜力。3D重建的关键在于高几何保真度。然而，现有方法在现场条件下，尤其是稀疏和遮挡视图下表现不佳。本研究开发了一个两阶段框架（DATR），用于从稀疏视图重建苹果树。第一阶段利用车载传感器和基础模型，从复杂的现场图像中半自动生成树木掩膜。树木掩膜用于过滤多模态数据中的背景信息，以便在第二阶段进行单图像到3D重建。第二阶段包括扩散模型和大型重建模型，分别用于多视图和隐式神经场生成。该框架在现场和合成数据集上进行了评估，结果显示DATR框架在两个数据集上均优于现有3D重建方法，并在领域特征估计上与工业级激光扫描仪相当，同时提高了约360倍的吞吐量，展示了其在可扩展农业数字双胞胎系统中的强大潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决在稀疏视图条件下苹果树的3D重建问题。现有方法在复杂的现场环境中，尤其是视图稀疏和遮挡情况下，重建效果不理想，无法满足数字双胞胎应用的需求。

**核心思路**：DATR框架的核心思路是通过两阶段的处理流程，首先利用车载传感器和基础模型生成树木掩膜，进而在第二阶段进行高质量的3D重建。这种设计能够有效过滤背景信息，提高重建的准确性和效率。

**技术框架**：DATR框架分为两个主要阶段：第一阶段是树木掩膜生成，使用车载传感器获取的复杂图像；第二阶段是3D重建，结合扩散模型和大型重建模型进行多视图和隐式神经场的生成。

**关键创新**：DATR框架的创新之处在于结合了扩散模型与大型重建模型，能够在稀疏视图下实现高质量的3D重建。这一方法与传统的重建技术相比，显著提高了重建的准确性和效率。

**关键设计**：在模型训练中，使用了由Real2Sim数据生成器生成的真实合成苹果树数据，确保了模型的泛化能力。框架中的损失函数和网络结构经过精心设计，以适应多模态数据的处理需求。具体的参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

DATR框架在多个数据集上的实验结果显示，其3D重建性能显著优于现有方法，特别是在稀疏视图条件下。与工业级激光扫描仪相比，其领域特征估计相当，同时吞吐量提升约360倍，展示了其在实际应用中的强大优势。

## 🎯 应用场景

该研究的DATR框架具有广泛的应用潜力，尤其是在农业领域的数字双胞胎系统中。通过实现高效的3D重建，能够为农作物监测、管理和机器人仿真提供支持，提升农业生产的智能化水平。未来，该技术还可扩展至其他领域，如林业、环境监测等，推动相关行业的数字化转型。

## 📄 摘要（原文）

> Digital twin applications offered transformative potential by enabling real-time monitoring and robotic simulation through accurate virtual replicas of physical assets. The key to these systems is 3D reconstruction with high geometrical fidelity. However, existing methods struggled under field conditions, especially with sparse and occluded views. This study developed a two-stage framework (DATR) for the reconstruction of apple trees from sparse views. The first stage leverages onboard sensors and foundation models to semi-automatically generate tree masks from complex field images. Tree masks are used to filter out background information in multi-modal data for the single-image-to-3D reconstruction at the second stage. This stage consists of a diffusion model and a large reconstruction model for respective multi view and implicit neural field generation. The training of the diffusion model and LRM was achieved by using realistic synthetic apple trees generated by a Real2Sim data generator. The framework was evaluated on both field and synthetic datasets. The field dataset includes six apple trees with field-measured ground truth, while the synthetic dataset featured structurally diverse trees. Evaluation results showed that our DATR framework outperformed existing 3D reconstruction methods across both datasets and achieved domain-trait estimation comparable to industrial-grade stationary laser scanners while improving the throughput by $\sim$360 times, demonstrating strong potential for scalable agricultural digital twin systems.

