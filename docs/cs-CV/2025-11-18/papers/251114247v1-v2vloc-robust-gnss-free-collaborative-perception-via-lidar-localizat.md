---
layout: default
title: "V2VLoc: Robust GNSS-Free Collaborative Perception via LiDAR Localization"
---

# V2VLoc: Robust GNSS-Free Collaborative Perception via LiDAR Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14247" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14247v1</a>
  <a href="https://arxiv.org/pdf/2511.14247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14247v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14247v1', 'V2VLoc: Robust GNSS-Free Collaborative Perception via LiDAR Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenkai Lin, Qiming Xia, Wen Li, Xun Huang, Chenglu Wen

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: AAAI2026

---

## 💡 一句话要点

**提出V2VLoc框架，通过激光雷达定位实现GNSS拒止环境下的鲁棒协同感知。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `协同感知` `激光雷达定位` `GNSS拒止` `Transformer` `多智能体系统`

## 📋 核心要点

1. 现有协同感知方法依赖GNSS定位，但在GNSS拒止环境下性能显著下降，限制了应用场景。
2. 提出V2VLoc框架，利用激光雷达定位，并设计PASTAT模块进行位姿误差校正和时空对齐。
3. 在V2VLoc数据集上验证了方法的有效性，并在真实数据集V2V4Real上验证了泛化能力。

## 📝 摘要（中文）

多智能体依赖于精确的位姿来共享和对齐观测信息，从而实现对环境的协同感知。然而，传统的基于GNSS的定位在GNSS拒止环境中经常失效，使得协同中的特征对齐变得困难。为了解决这一挑战，我们提出了一种基于激光雷达定位的鲁棒GNSS-free协同感知框架。具体来说，我们提出了一个轻量级的带置信度的位姿生成器（PGC）来估计紧凑的位姿和置信度表示。为了减轻定位误差的影响，我们进一步开发了位姿感知时空对齐Transformer（PASTAT），它执行置信度感知的空间对齐，同时捕获必要的时间上下文。此外，我们提出了一个新的模拟数据集V2VLoc，它可以适用于激光雷达定位和协同检测任务。V2VLoc包含三个子集：Town1Loc、Town4Loc和V2VDet。Town1Loc和Town4Loc为定位任务中的训练提供多轨迹序列，而V2VDet专门用于协同检测任务。在V2VLoc数据集上进行的大量实验表明，我们的方法在GNSS拒止条件下实现了最先进的性能。我们进一步在真实世界的V2V4Real数据集上进行了扩展实验，以验证PASTAT的有效性和泛化性。

## 🔬 方法详解

**问题定义**：论文旨在解决GNSS拒止环境下多智能体协同感知中，由于定位不准确导致的特征对齐困难问题。现有方法依赖GNSS，在无GNSS信号时失效，无法保证协同感知的性能。

**核心思路**：核心思路是利用激光雷达进行定位，摆脱对GNSS的依赖。同时，设计位姿感知的时空对齐模块，减轻定位误差对协同感知的影响。通过置信度机制，降低错误位姿的影响，提升整体鲁棒性。

**技术框架**：整体框架包含三个主要模块：1) 位姿生成器（PGC）：用于估计每个智能体的位姿和置信度。2) 位姿感知时空对齐Transformer（PASTAT）：用于对齐不同智能体的特征，并融合时间上下文信息。3) 协同感知模块：利用对齐后的特征进行协同感知任务，例如目标检测。

**关键创新**：关键创新在于PASTAT模块，它将位姿信息和置信度融入到Transformer架构中，实现了对时空信息的有效对齐。PGC模块提供了一种轻量级的位姿估计方法，并引入了置信度评估，增强了系统的鲁棒性。

**关键设计**：PGC模块采用轻量级网络结构，输出位姿和置信度。PASTAT模块使用Transformer结构，注意力机制的权重受到位姿置信度的调节。损失函数包括定位损失和协同感知损失，共同优化整个框架。

## 📊 实验亮点

论文提出的V2VLoc框架在GNSS拒止环境下取得了state-of-the-art的性能。在V2VLoc数据集上的实验结果表明，该方法能够有效提高协同感知的精度和鲁棒性。在真实数据集V2V4Real上的实验验证了PASTAT模块的有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于自动驾驶、无人配送、矿区作业等GNSS信号受限或不可靠的场景。通过多智能体协同感知，可以提高环境感知范围和精度，增强系统的安全性和可靠性，为复杂环境下的智能体协作提供技术支撑。

## 📄 摘要（原文）

> Multi-agents rely on accurate poses to share and align observations, enabling a collaborative perception of the environment. However, traditional GNSS-based localization often fails in GNSS-denied environments, making consistent feature alignment difficult in collaboration. To tackle this challenge, we propose a robust GNSS-free collaborative perception framework based on LiDAR localization. Specifically, we propose a lightweight Pose Generator with Confidence (PGC) to estimate compact pose and confidence representations. To alleviate the effects of localization errors, we further develop the Pose-Aware Spatio-Temporal Alignment Transformer (PASTAT), which performs confidence-aware spatial alignment while capturing essential temporal context. Additionally, we present a new simulation dataset, V2VLoc, which can be adapted for both LiDAR localization and collaborative detection tasks. V2VLoc comprises three subsets: Town1Loc, Town4Loc, and V2VDet. Town1Loc and Town4Loc offer multi-traversal sequences for training in localization tasks, whereas V2VDet is specifically intended for the collaborative detection task. Extensive experiments conducted on the V2VLoc dataset demonstrate that our approach achieves state-of-the-art performance under GNSS-denied conditions. We further conduct extended experiments on the real-world V2V4Real dataset to validate the effectiveness and generalizability of PASTAT.

