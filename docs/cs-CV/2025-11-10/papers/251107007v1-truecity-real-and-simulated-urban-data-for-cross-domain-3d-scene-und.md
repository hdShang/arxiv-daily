---
layout: default
title: TrueCity: Real and Simulated Urban Data for Cross-Domain 3D Scene Understanding
---

# TrueCity: Real and Simulated Urban Data for Cross-Domain 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07007" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07007v1</a>
  <a href="https://arxiv.org/pdf/2511.07007.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07007v1" onclick="toggleFavorite(this, '2511.07007v1', 'TrueCity: Real and Simulated Urban Data for Cross-Domain 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duc Nguyen, Yan-Ling Lai, Qilin Zhang, Prabin Gyawali, Benedikt Schwab, Olaf Wysocki, Thomas H. Kolbe

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-11-10

**备注**: The paper accepted for 3DV 2026 (International Conference on 3D Vision 2026)

**🔗 代码/项目**: [PROJECT_PAGE](https://tum-gis.github.io/TrueCity/)

---

## 💡 一句话要点

**TrueCity：提出城市三维场景理解的真实与模拟跨域数据集**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维场景理解` `语义分割` `领域自适应` `合成数据` `真实数据` `城市建模` `点云数据`

## 📋 核心要点

1. 现有三维语义场景理解方法受限于真实世界标注数据的匮乏，难以实现模型的泛化能力。
2. TrueCity数据集提供真实与模拟同步点云，并对齐国际三维城市建模标准，用于量化领域偏移。
3. 实验结果表明，TrueCity数据集可用于评估领域迁移策略，并提升真实世界三维场景理解性能。

## 📝 摘要（中文）

三维语义场景理解是三维计算机视觉领域长期存在的挑战。关键问题之一是缺乏带标注的真实世界数据，以促进模型泛化。常见的做法是模拟新数据。虽然合成数据集提供了可扩展性和完美的标签，但其设计者构建的场景未能捕捉到真实世界的复杂性和传感器噪声，导致了合成到真实的领域差距。此外，没有基准提供同步的真实和模拟点云，用于面向分割的领域偏移分析。我们引入TrueCity，这是第一个城市语义分割基准，具有厘米级精度的带标注的真实世界点云、语义三维城市模型和代表同一城市的带标注的模拟点云。TrueCity提出了与国际三维城市建模标准对齐的分割类别，从而能够一致地评估合成到真实的差距。我们在常见基线上进行的广泛实验量化了领域偏移，并强调了利用合成数据来增强真实世界三维场景理解的策略。我们相信TrueCity数据集将促进sim-to-real差距量化的进一步发展，并支持可泛化的数据驱动模型。数据、代码和三维模型可在线获取：https://tum-gis.github.io/TrueCity/

## 🔬 方法详解

**问题定义**：三维语义场景理解面临真实数据不足和合成数据与真实数据存在领域差异的问题。现有方法难以在真实场景中取得良好的泛化性能，且缺乏统一的基准来评估和解决合成到真实的领域偏移问题。

**核心思路**：TrueCity的核心思路是构建一个包含真实世界点云、语义三维城市模型和模拟点云的综合数据集，这些数据代表同一城市，并且具有对齐的语义标注。通过提供同步的真实和模拟数据，可以更好地研究和解决领域偏移问题。

**技术框架**：TrueCity数据集包含三个主要组成部分：1) 厘米级精度的真实世界点云，通过激光扫描获取并进行人工标注；2) 语义三维城市模型，符合国际标准，提供详细的城市结构信息；3) 基于三维城市模型生成的模拟点云，带有自动生成的语义标签。该数据集提供了一套完整的工具和评估指标，用于比较不同算法在真实和模拟数据上的性能，并量化领域偏移。

**关键创新**：TrueCity的关键创新在于其同步的真实和模拟数据，以及与国际三维城市建模标准对齐的语义类别。这使得研究人员能够更有效地研究合成到真实的领域偏移，并开发更具泛化能力的模型。此外，TrueCity是首个提供此类同步数据的城市语义分割基准。

**关键设计**：TrueCity数据集的标注遵循国际三维城市建模标准，确保了语义类别的一致性和可比性。模拟点云的生成过程考虑了传感器噪声和真实世界的复杂性，以减少与真实数据的领域差异。数据集还提供了一系列评估指标，用于量化不同算法在真实和模拟数据上的性能，例如总体精度、平均IoU等。

## 📊 实验亮点

论文在TrueCity数据集上对常见的三维语义分割基线进行了评估，结果表明，合成数据与真实数据之间存在显著的领域偏移。通过使用领域自适应方法，可以有效地利用合成数据来提高真实数据的分割精度。实验结果还表明，TrueCity数据集可以作为评估不同领域自适应算法的有效平台。

## 🎯 应用场景

TrueCity数据集可广泛应用于自动驾驶、城市规划、机器人导航等领域。通过利用该数据集，研究人员可以开发更鲁棒的三维场景理解算法，提高自动驾驶系统的安全性，优化城市规划决策，并提升机器人在复杂城市环境中的导航能力。该数据集还有助于推动三维城市建模技术的发展。

## 📄 摘要（原文）

> 3D semantic scene understanding remains a long-standing challenge in the 3D computer vision community. One of the key issues pertains to limited real-world annotated data to facilitate generalizable models. The common practice to tackle this issue is to simulate new data. Although synthetic datasets offer scalability and perfect labels, their designer-crafted scenes fail to capture real-world complexity and sensor noise, resulting in a synthetic-to-real domain gap. Moreover, no benchmark provides synchronized real and simulated point clouds for segmentation-oriented domain shift analysis. We introduce TrueCity, the first urban semantic segmentation benchmark with cm-accurate annotated real-world point clouds, semantic 3D city models, and annotated simulated point clouds representing the same city. TrueCity proposes segmentation classes aligned with international 3D city modeling standards, enabling consistent evaluation of synthetic-to-real gap. Our extensive experiments on common baselines quantify domain shift and highlight strategies for exploiting synthetic data to enhance real-world 3D scene understanding. We are convinced that the TrueCity dataset will foster further development of sim-to-real gap quantification and enable generalizable data-driven models. The data, code, and 3D models are available online: https://tum-gis.github.io/TrueCity/

