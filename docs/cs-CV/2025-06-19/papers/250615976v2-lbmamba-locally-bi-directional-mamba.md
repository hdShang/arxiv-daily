---
layout: default
title: "LBMamba: Locally Bi-directional Mamba"
---

# LBMamba: Locally Bi-directional Mamba

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15976" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15976v2</a>
  <a href="https://arxiv.org/pdf/2506.15976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15976v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15976v2', 'LBMamba: Locally Bi-directional Mamba')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingwei Zhang, Xi Han, Hong Qin, Mahdi S. Hosseini, Dimitris Samaras

**分类**: cs.CV

**发布日期**: 2025-06-19 (更新: 2025-11-11)

**备注**: Accepted to TMLR

**🔗 代码/项目**: [GITHUB](https://github.com/cvlab-stonybrook/LBMamba)

---

## 💡 一句话要点

**提出LBMamba以提升Mamba模型的计算效率与准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `计算机视觉` `图像分类` `语义分割` `目标检测` `深度学习` `高效计算`

## 📋 核心要点

1. 现有的Mamba模型由于其单向特性，无法有效利用后续状态的信息，限制了其性能。
2. LBMamba通过在前向扫描中嵌入局部反向扫描，避免了全局反向扫描带来的额外计算负担。
3. 在ImageNet-1K、ADE20K和COCO等多个数据集上，LBMamba显著提高了模型的准确性和性能，且在病理图像分类任务中也取得了显著提升。

## 📝 摘要（中文）

Mamba是一种状态空间模型（SSM），通过将递归重构为并行扫描来加速训练，成为自注意力的线性扩展替代方案。然而，Mamba的单向特性限制了其信息获取能力。为了解决这一问题，当前的Mamba计算机视觉方法通常通过增加全局反向扫描来实现双向扫描，但这会导致计算负担加重。为此，本文提出了LBMamba，一种局部双向SSM模块，能够在前向扫描中嵌入轻量级的局部反向扫描，从而消除额外的计算负担。实验结果表明，LBMamba在多个数据集上均表现出优越的性能与吞吐量平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决Mamba模型的单向特性所导致的信息获取不足问题，现有方法通过全局反向扫描来弥补这一缺陷，但增加了计算负担。

**核心思路**：LBMamba的核心思想是在前向扫描中嵌入局部反向扫描，以实现双向信息获取，同时避免全局反向扫描的额外计算开销。

**技术框架**：LBMamba的整体架构包括前向扫描和局部反向扫描两个主要模块，前向扫描负责获取当前状态的信息，而局部反向扫描则在每个线程寄存器中执行，以提高计算效率。

**关键创新**：LBMamba的主要创新在于其局部双向设计，能够在不增加计算负担的情况下恢复全局感受野，这一设计与传统的全局双向扫描方法本质上不同。

**关键设计**：在LBMamba中，关键参数设置包括局部反向扫描的范围和前向扫描的步幅，损失函数采用交叉熵损失以优化分类性能，网络结构则通过交替扫描方向的方式来增强模型的表达能力。

## 📊 实验亮点

在多个数据集上，LBMamba在相同的吞吐量下实现了0.8%至1.6%的ImageNet-1K分类准确率提升，0.6%至2.7%的ADE20K语义分割mIoU提升，以及0.9%和1.1%的COCO检测APb和APm提升。此外，LBMamba还提升了四个SOTA Mamba模型的性能，增幅为0.5%至3.4%。

## 🎯 应用场景

LBMamba的研究成果在计算机视觉领域具有广泛的应用潜力，特别是在图像分类、语义分割和目标检测等任务中。其高效的计算性能和准确性提升使其适用于实时处理和大规模数据集的分析，未来可望在医疗图像分析等领域发挥重要作用。

## 📄 摘要（原文）

> Mamba, a State Space Model (SSM) that accelerates training by recasting recurrence as a parallel scan, has recently emerged as a linearly-scaling alternative to self-attention. Because of its unidirectional nature, each state in Mamba only has information of its previous states and is blind to states after. Current Mamba-based computer-vision methods typically overcome this by augmenting Mamba's global forward scan with a global backward scan, forming a bi-directional scan to restore a full receptive field. However, this operation doubles the computational load, eroding much of the efficiency advantage that originally Mamba have. To eliminate this extra scans, we introduce LBMamba, a locally bi-directional SSM block that embeds a lightweight locally backward scan inside the forward scan and executes it in per-thread registers. Building on LBMamba, we present LBVim, a backbone that alternates scan directions every two layers to recover a global receptive field without extra backward sweeps. We validate our approach on both natural images and whole slide images (WSIs) and show that it constantly offers a superior performance-throughput trade-off. Under the same throughput, LBVim achieves 0.8% to 1.6% higher top-1 accuracy on the ImageNet-1K classification dataset, 0.6% to 2.7% higher mIoU on the ADE20K semantic segmentation dataset, 0.9% higher APb and 1.1% higher APm on the COCO detection dataset. Our method also boosts the accuracy of four SOTA Mamba models, namely VMamba, LocalVim, PlainMamba and Adventurer, by 0.5% to 3.4%. We integrate LBMamba into the SOTA pathology multiple instance learning (MIL) model, MambaMIL, which is unidirectional. Experiments on 3 public WSI classification datasets show that our method achieves a relative improvement of up to 3.06% better AUC, 3.39% better F1, 1.67% better accuracy. Our code is available at https://github.com/cvlab-stonybrook/LBMamba.

