---
layout: default
title: Temporal Zoom Networks: Distance Regression and Continuous Depth for Efficient Action Localization
---

# Temporal Zoom Networks: Distance Regression and Continuous Depth for Efficient Action Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03943" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03943v3</a>
  <a href="https://arxiv.org/pdf/2511.03943.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03943v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03943v3', 'Temporal Zoom Networks: Distance Regression and Continuous Depth for Efficient Action Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma

**分类**: cs.CV

**发布日期**: 2025-11-06 (更新: 2025-11-13)

---

## 💡 一句话要点

**提出边界距离回归与自适应时间细化以提升动作定位效率**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `时间动作定位` `边界检测` `深度学习` `自适应计算` `视频理解` `变换器` `信息论` `效率提升`

## 📋 核心要点

1. 现有的时间动作定位方法在处理模糊边界时效率低下，导致计算资源浪费。
2. 本文提出边界距离回归（BDR）和自适应时间细化（ATR）两种创新方法，提升了边界检测的精度和计算效率。
3. 在THUMOS14数据集上，本文方法在减少FLOPs的同时，提升了mAP@0.7的性能，尤其在短动作检测上表现突出。

## 📝 摘要（中文）

时间动作定位需要精确的边界检测和计算效率。现有方法在所有时间位置上均匀计算，导致在简单边界上浪费资源，而在模糊边界上却难以处理。本文提出了两项互补创新：边界距离回归（BDR），用有符号距离回归替代基于分类的边界检测，降低了3.3至16.7倍的方差；自适应时间细化（ATR），在困难边界附近连续分配变换器深度。实验结果表明，本文方法在THUMOS14数据集上实现了56.5%的mAP@0.7，使用151G FLOPs，比ActionFormer++减少36%的FLOPs，同时在短动作上获得显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决时间动作定位中的边界检测精度和计算效率问题。现有方法在所有时间位置均匀分配计算资源，导致在简单边界上浪费，而在模糊边界上却难以取得良好效果。

**核心思路**：论文提出边界距离回归（BDR）和自适应时间细化（ATR）两种方法。BDR通过有符号距离回归替代分类方法，减少了边界检测的方差；ATR则根据困难边界的需要，动态调整变换器的深度分配。

**技术框架**：整体架构包括两个主要模块：边界距离回归模块和自适应时间细化模块。BDR模块负责边界的精确定位，而ATR模块则根据边界的复杂性动态调整计算资源。

**关键创新**：最重要的创新在于提出了一种理论基础的距离公式，并通过信息论分析展示了最佳方差缩放。此外，ATR机制避免了离散路由的复杂性，实现了计算资源的有效分配。

**关键设计**：训练过程中，BDR采用了特定的损失函数以优化距离回归的精度；ATR则通过动态调整参数，确保在困难边界附近分配更多的计算资源。

## 📊 实验亮点

实验结果显示，本文方法在THUMOS14数据集上实现了56.5%的mAP@0.7，使用151G FLOPs，较ActionFormer++减少36%的FLOPs。同时，相较于均匀基线，本文方法提升了2.9%的mAP@0.7，且在短动作检测上表现尤为突出，提升幅度达到4.2%。

## 🎯 应用场景

该研究在视频理解、监控系统和人机交互等领域具有广泛的应用潜力。通过提升动作定位的效率和精度，可以更好地支持实时监控、行为识别和智能分析等任务，进而推动相关技术的发展与应用。

## 📄 摘要（原文）

> Temporal action localization requires both precise boundary detection and computational efficiency. Current methods apply uniform computation across all temporal positions, wasting resources on easy boundaries while struggling with ambiguous ones. We address this through two complementary innovations: Boundary Distance Regression (BDR), which replaces classification-based boundary detection with signed-distance regression achieving 3.3--16.7$\times$ lower variance; and Adaptive Temporal Refinement (ATR), which allocates transformer depth continuously ($τ\in[0,1]$) to concentrate computation near difficult boundaries. On THUMOS14, our method achieves 56.5\% mAP@0.7 and 58.2\% average mAP@[0.3:0.7] with 151G FLOPs, using 36\% fewer FLOPs than ActionFormer++ (55.7\% mAP@0.7 at 235G). Compared to uniform baselines, we achieve +2.9\% mAP@0.7 (+1.8\% avg mAP, 5.4\% relative) with 24\% fewer FLOPs and 29\% lower latency, with particularly strong gains on short actions (+4.2\%, 8.6\% relative). Training requires 1.29$\times$ baseline FLOPs, but this one-time cost is amortized over many inference runs; knowledge distillation further reduces this to 1.1$\times$ while retaining 99.5\% accuracy. Our contributions include: (i) a theoretically-grounded distance formulation with information-theoretic analysis showing optimal variance scaling; (ii) a continuous depth allocation mechanism avoiding discrete routing complexity; and (iii) consistent improvements across four datasets with gains correlating with boundary heterogeneity.

