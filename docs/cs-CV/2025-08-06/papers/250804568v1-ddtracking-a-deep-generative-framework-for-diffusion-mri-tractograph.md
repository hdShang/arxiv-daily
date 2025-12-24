---
layout: default
title: "DDTracking: A Deep Generative Framework for Diffusion MRI Tractography with Streamline Local-Global Spatiotemporal Modeling"
---

# DDTracking: A Deep Generative Framework for Diffusion MRI Tractography with Streamline Local-Global Spatiotemporal Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04568" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04568v1</a>
  <a href="https://arxiv.org/pdf/2508.04568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04568v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04568v1', 'DDTracking: A Deep Generative Framework for Diffusion MRI Tractography with Streamline Local-Global Spatiotemporal Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijie Li, Wei Zhang, Xi Zhu, Ye Wu, Yogesh Rathi, Lauren J. O'Donnell, Fan Zhang

**分类**: cs.CV

**发布日期**: 2025-08-06

**备注**: Preprint version. The content may be updated in the future

**🔗 代码/项目**: [GITHUB](https://github.com/yishengpoxiao/DDtracking.git)

---

## 💡 一句话要点

**提出DDTracking以解决扩散MRI轨迹重建问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `扩散MRI` `轨迹重建` `深度生成模型` `条件去噪` `空间时间建模` `医学影像` `神经科学`

## 📋 核心要点

1. 现有的扩散MRI轨迹重建方法在处理复杂结构和长距离一致性方面存在不足，难以准确捕捉细微的解剖特征。
2. DDTracking通过双路径编码网络，联合建模局部和全局信息，提出了一种条件去噪扩散过程来优化流线传播。
3. 在ISMRM Challenge和TractoInferno等基准测试中，DDTracking的表现显著优于现有方法，展现出强大的适应性和泛化能力。

## 📝 摘要（中文）

本文提出了DDTracking，一个新颖的深度生成框架，用于扩散MRI轨迹重建，将流线传播公式化为条件去噪扩散过程。DDTracking引入了双路径编码网络，联合建模局部空间编码和全局时间依赖性。此外，设计了条件扩散模型模块，利用学习到的局部和全局嵌入预测轨迹传播方向。通过对多样化的独立获取的dMRI数据集进行全面评估，实验结果表明DDTracking在多个基准测试中显著优于当前最先进的轨迹重建方法，展示了其在异质数据集上的强泛化能力。整体而言，DDTracking提供了符合解剖学的稳健轨迹重建，适用于广泛的dMRI应用。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散MRI轨迹重建中的流线传播问题，现有方法在捕捉细微结构和保持长距离一致性方面存在挑战。

**核心思路**：DDTracking的核心思路是将流线传播视为条件去噪扩散过程，通过双路径编码网络同时建模局部空间和全局时间依赖性，以提高轨迹重建的准确性。

**技术框架**：DDTracking的整体架构包括双路径编码网络和条件扩散模型模块。双路径网络负责提取局部和全局特征，而条件扩散模型则利用这些特征预测流线的传播方向。

**关键创新**：DDTracking的主要创新在于其双路径编码网络的设计，使得局部和全局信息的融合更加高效，显著提高了轨迹重建的准确性和一致性。

**关键设计**：在网络结构上，采用了特定的损失函数来优化流线的传播方向，并通过端到端的训练方式提升模型的学习能力。

## 📊 实验亮点

在ISMRM Challenge和TractoInferno基准测试中，DDTracking的表现显著优于现有最先进的轨迹重建方法，具体提升幅度达到XX%（具体数据待补充），展示了其在不同健康状况、年龄组和成像协议下的强泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、神经科学研究和临床诊断等。DDTracking能够提供更为准确的脑白质轨迹重建，帮助医生更好地理解脑部结构和功能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper presents DDTracking, a novel deep generative framework for diffusion MRI tractography that formulates streamline propagation as a conditional denoising diffusion process. In DDTracking, we introduce a dual-pathway encoding network that jointly models local spatial encoding (capturing fine-scale structural details at each streamline point) and global temporal dependencies (ensuring long-range consistency across the entire streamline). Furthermore, we design a conditional diffusion model module, which leverages the learned local and global embeddings to predict streamline propagation orientations for tractography in an end-to-end trainable manner. We conduct a comprehensive evaluation across diverse, independently acquired dMRI datasets, including both synthetic and clinical data. Experiments on two well-established benchmarks with ground truth (ISMRM Challenge and TractoInferno) demonstrate that DDTracking largely outperforms current state-of-the-art tractography methods. Furthermore, our results highlight DDTracking's strong generalizability across heterogeneous datasets, spanning varying health conditions, age groups, imaging protocols, and scanner types. Collectively, DDTracking offers anatomically plausible and robust tractography, presenting a scalable, adaptable, and end-to-end learnable solution for broad dMRI applications. Code is available at: https://github.com/yishengpoxiao/DDtracking.git

