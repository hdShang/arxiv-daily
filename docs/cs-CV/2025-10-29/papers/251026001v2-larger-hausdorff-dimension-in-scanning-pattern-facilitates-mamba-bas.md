---
layout: default
title: Larger Hausdorff Dimension in Scanning Pattern Facilitates Mamba-Based Methods in Low-Light Image Enhancement
---

# Larger Hausdorff Dimension in Scanning Pattern Facilitates Mamba-Based Methods in Low-Light Image Enhancement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26001" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26001v2</a>
  <a href="https://arxiv.org/pdf/2510.26001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26001v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26001v2', 'Larger Hausdorff Dimension in Scanning Pattern Facilitates Mamba-Based Methods in Low-Light Image Enhancement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhua Wang, Caibo Feng, Xiangjun Fu, Chunxiao Liu

**分类**: cs.CV

**发布日期**: 2025-10-29 (更新: 2025-10-31)

---

## 💡 一句话要点

**提出基于Hilbert扫描Mamba的低光图像增强方法，提升细节表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `低光图像增强` `Mamba` `Hilbert扫描` `Hausdorff维数` `选择性扫描` `图像细节恢复` `深度学习`

## 📋 核心要点

1. 现有低光图像增强方法难以兼顾细节捕捉和长程依赖，导致信息不一致和视觉效果不佳。
2. 通过Hilbert选择性扫描机制，增加Mamba框架扫描模式的Hausdorff维数，更有效地探索特征空间。
3. 实验表明，该方法在提升定量指标和视觉保真度的同时，降低了计算资源消耗和推理时间。

## 📝 摘要（中文）

本文提出了一种创新的Mamba框架增强方法，通过一种新颖的Hilbert选择性扫描机制，增加了其扫描模式的Hausdorff维数。该机制更有效地探索了特征空间，捕捉了复杂的精细尺度细节，并提高了整体覆盖率。因此，它减轻了信息不一致性，同时细化了空间局部性，从而更好地捕捉微妙的局部交互，而又不牺牲模型处理长程依赖关系的能力。在公开基准上的大量实验表明，我们的方法显著提高了现有基于Mamba的低光图像增强方法的定量指标和定性视觉保真度，同时降低了计算资源消耗并缩短了推理时间。我们相信，这种改进的策略不仅推进了低光图像增强的最新技术水平，而且在利用基于Mamba技术的领域中也具有广阔的应用前景。

## 🔬 方法详解

**问题定义**：低光图像增强旨在恢复在弱光条件下拍摄的图像的视觉质量。现有方法，特别是基于Transformer的方法，虽然在捕捉长程依赖方面表现出色，但在处理局部细节和保持信息一致性方面存在不足。Mamba虽然在效率上有所提升，但在低光增强任务中，其扫描方式仍有改进空间，尤其是在细节信息的捕捉上。

**核心思路**：论文的核心思路是通过改进Mamba的扫描模式，使其能够更有效地探索特征空间，从而更好地捕捉图像中的精细细节。具体来说，通过增加扫描模式的Hausdorff维数，提高其覆盖率和对局部信息的敏感度。

**技术框架**：该方法的核心是引入Hilbert选择性扫描机制。该机制利用Hilbert曲线的特性，以一种更密集和全局的方式扫描特征图。整体流程包括：输入低光图像，通过一个初始特征提取模块，然后应用改进的Mamba模块进行特征增强，最后通过一个重建模块恢复增强后的图像。改进的Mamba模块是整个框架的核心。

**关键创新**：最关键的创新在于使用Hilbert曲线来指导Mamba的扫描过程。传统的Mamba扫描方式可能无法充分利用特征空间的信息，而Hilbert曲线具有更高的Hausdorff维数，能够更有效地覆盖特征空间，从而捕捉到更多的细节信息。这种扫描方式的改进是与现有Mamba方法最本质的区别。

**关键设计**：Hilbert选择性扫描机制的具体实现可能涉及到对Mamba中选择机制的调整，使其能够根据Hilbert曲线的路径来选择性地关注不同的特征区域。具体的参数设置和损失函数选择可能需要根据具体的实验结果进行调整，以达到最佳的增强效果。网络结构方面，可能需要对Mamba模块进行微调，以更好地适应Hilbert扫描带来的信息流变化。

## 📊 实验亮点

实验结果表明，该方法在多个公开低光图像增强数据集上取得了显著的性能提升。与现有的Mamba-based方法相比，该方法在PSNR和SSIM等指标上均有明显提高，同时降低了计算资源消耗和推理时间。定性结果也显示，该方法能够更好地恢复图像的细节信息，并减少伪影。

## 🎯 应用场景

该研究成果可广泛应用于安防监控、自动驾驶、医学影像等领域，提升弱光环境下的图像识别和分析能力。例如，在夜间监控中，可以提高监控视频的清晰度，从而更准确地识别可疑行为。在自动驾驶中，可以增强车辆在夜间或隧道等弱光环境下的感知能力，提高驾驶安全性。在医学影像中，可以改善低剂量CT图像的质量，减少辐射剂量。

## 📄 摘要（原文）

> We propose an innovative enhancement to the Mamba framework by increasing the Hausdorff dimension of its scanning pattern through a novel Hilbert Selective Scan mechanism. This mechanism explores the feature space more effectively, capturing intricate fine-scale details and improving overall coverage. As a result, it mitigates information inconsistencies while refining spatial locality to better capture subtle local interactions without sacrificing the model's ability to handle long-range dependencies. Extensive experiments on publicly available benchmarks demonstrate that our approach significantly improves both the quantitative metrics and qualitative visual fidelity of existing Mamba-based low-light image enhancement methods, all while reducing computational resource consumption and shortening inference time. We believe that this refined strategy not only advances the state-of-the-art in low-light image enhancement but also holds promise for broader applications in fields that leverage Mamba-based techniques.

