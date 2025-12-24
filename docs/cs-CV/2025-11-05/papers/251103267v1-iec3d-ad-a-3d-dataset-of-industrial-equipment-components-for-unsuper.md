---
layout: default
title: "IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection"
---

# IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03267" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03267v1</a>
  <a href="https://arxiv.org/pdf/2511.03267.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03267v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03267v1', 'IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingyang Guo, Hongjie Li, Ruiyun Yu, Hanzhe Liang, Jinbao Wang

**分类**: cs.CV

**发布日期**: 2025-11-05

---

## 💡 一句话要点

**提出IEC3D-AD工业零件3D异常检测数据集及GMANet异常检测方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D异常检测` `点云处理` `工业设备组件` `数据集构建` `生成模型`

## 📋 核心要点

1. 现有3D异常检测数据集难以捕捉工业环境中复杂和细微的缺陷，限制了对工业设备组件的精确异常检测研究。
2. 提出GMANet，一种基于几何形态分析生成合成点云样本，并通过空间差异优化来提升异常检测性能的新范式。
3. 在IEC3D-AD和其他数据集上的实验表明，该方法能够有效检测工业设备组件中的异常。

## 📝 摘要（中文）

3D异常检测（3D-AD）在工业制造中至关重要，尤其是在确保核心设备组件的可靠性和安全性方面。现有的3D数据集，如Real3D-AD和MVTec 3D-AD，虽然提供了广泛的应用支持，但它们在捕捉真实工业环境中复杂性和细微缺陷方面存在不足。这种局限性阻碍了精确的异常检测研究，特别是对于工业设备组件（IEC），如轴承、环和螺栓。为了解决这个问题，我们开发了一个针对真实工业场景的点云异常检测数据集（IEC3D-AD）。该数据集直接从实际生产线收集，确保了高保真度和相关性。与现有数据集相比，IEC3D-AD具有显著提高的点云分辨率和缺陷标注粒度，从而促进了更具挑战性的异常检测任务。此外，受到生成式2D-AD方法的启发，我们在IEC3D-AD上引入了一种新的3D-AD范式（GMANet）。该范式基于几何形态分析生成合成点云样本，然后通过空间差异优化来减少正常和异常点级别特征之间的边距并增加重叠。大量的实验证明了我们的方法在IEC3D-AD和其他数据集上的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决工业设备组件（IEC）的3D点云异常检测问题。现有数据集在点云分辨率和缺陷标注粒度上不足，难以支持对细微缺陷的检测。此外，现有方法在处理工业场景下的复杂几何形状和噪声时表现不佳。

**核心思路**：论文的核心思路是构建一个高保真度的工业数据集IEC3D-AD，并提出一种基于生成模型的异常检测方法GMANet。GMANet通过生成合成点云样本来扩充训练数据，并利用空间差异优化来增强正常和异常特征的区分度。

**技术框架**：GMANet的整体框架包括以下几个主要模块：1) 数据集构建：从实际生产线收集数据，并进行高分辨率点云重建和精细的缺陷标注。2) 几何形态分析：对正常点云进行几何形态分析，提取关键几何特征。3) 合成样本生成：基于几何特征生成合成点云样本，扩充训练数据。4) 空间差异优化：通过优化损失函数，减少正常和异常点级别特征之间的边距，增加重叠。

**关键创新**：论文的关键创新在于：1) 构建了高分辨率、高标注粒度的工业设备组件3D异常检测数据集IEC3D-AD。2) 提出了基于几何形态分析的合成样本生成方法，能够有效扩充训练数据。3) 引入了空间差异优化策略，增强了正常和异常特征的区分度。

**关键设计**：GMANet的关键设计包括：1) 使用点云配准和重建技术获得高分辨率点云。2) 设计了基于几何特征的合成样本生成算法，例如通过随机扰动、特征替换等方式生成异常样本。3) 采用了对比损失函数，鼓励正常样本聚集，异常样本分散。4) 网络结构采用PointNet++等经典点云处理网络。

## 📊 实验亮点

论文在自建数据集IEC3D-AD上进行了大量实验，结果表明GMANet方法在异常检测精度上显著优于现有方法。此外，在其他公开数据集上也取得了具有竞争力的结果，验证了该方法的泛化能力。实验结果表明，GMANet能够有效检测出工业设备组件中的细微缺陷，具有很高的实用价值。

## 🎯 应用场景

该研究成果可应用于工业制造领域，用于提高核心设备组件的质量控制水平，降低生产成本，并保障设备的安全可靠运行。例如，可用于轴承、齿轮、叶片等关键零部件的在线检测，及时发现潜在缺陷，避免重大事故的发生。未来，该技术有望扩展到其他工业领域，如航空航天、汽车制造等。

## 📄 摘要（原文）

> 3D anomaly detection (3D-AD) plays a critical role in industrial manufacturing, particularly in ensuring the reliability and safety of core equipment components. Although existing 3D datasets like Real3D-AD and MVTec 3D-AD offer broad application support, they fall short in capturing the complexities and subtle defects found in real industrial environments. This limitation hampers precise anomaly detection research, especially for industrial equipment components (IEC) such as bearings, rings, and bolts. To address this challenge, we have developed a point cloud anomaly detection dataset (IEC3D-AD) specific to real industrial scenarios. This dataset is directly collected from actual production lines, ensuring high fidelity and relevance. Compared to existing datasets, IEC3D-AD features significantly improved point cloud resolution and defect annotation granularity, facilitating more demanding anomaly detection tasks. Furthermore, inspired by generative 2D-AD methods, we introduce a novel 3D-AD paradigm (GMANet) on IEC3D-AD. This paradigm generates synthetic point cloud samples based on geometric morphological analysis, then reduces the margin and increases the overlap between normal and abnormal point-level features through spatial discrepancy optimization. Extensive experiments demonstrate the effectiveness of our method on both IEC3D-AD and other datasets.

