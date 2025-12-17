---
layout: default
title: RF-DETR: Neural Architecture Search for Real-Time Detection Transformers
---

# RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09554" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09554v1</a>
  <a href="https://arxiv.org/pdf/2511.09554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09554v1" onclick="toggleFavorite(this, '2511.09554v1', 'RF-DETR: Neural Architecture Search for Real-Time Detection Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Isaac Robinson, Peter Robicheaux, Matvei Popov, Deva Ramanan, Neehar Peri

**分类**: cs.CV

**发布日期**: 2025-11-12

**备注**: Project Page: https://rfdetr.roboflow.com/

**🔗 代码/项目**: [GITHUB](https://github.com/roboflow/rf-detr)

---

## 💡 一句话要点

**RF-DETR：面向实时目标检测Transformer的神经架构搜索**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `目标检测` `Transformer` `神经架构搜索` `实时检测` `模型优化`

## 📋 核心要点

1. 现有开放词汇检测器在COCO上表现出色，但在真实世界数据集上的泛化能力不足，尤其是在预训练中未包含的类别上。
2. RF-DETR通过神经架构搜索，在特定数据集上寻找精度和延迟之间的最佳平衡点，无需对每个架构进行单独训练。
3. RF-DETR在COCO和Roboflow100-VL数据集上显著优于现有实时方法，并在COCO上取得了超过60 AP的领先性能。

## 📝 摘要（中文）

本文提出RF-DETR，一种轻量级的专用检测Transformer，通过权重共享的神经架构搜索(NAS)为任何目标数据集发现精度-延迟帕累托曲线。该方法在目标数据集上微调预训练的基础网络，并在不重新训练的情况下评估数千种具有不同精度-延迟权衡的网络配置。此外，重新审视了NAS的“可调旋钮”，以提高DETR对不同目标领域的迁移能力。RF-DETR显著优于COCO和Roboflow100-VL上最先进的实时方法。RF-DETR (nano) 在COCO上实现了48.0 AP，以相似的延迟击败了D-FINE (nano) 5.3 AP，RF-DETR (2x-large) 在Roboflow100-VL上优于GroundingDINO (tiny) 1.2 AP，速度快了20倍。据我们所知，RF-DETR (2x-large) 是第一个在COCO上超过60 AP的实时检测器。

## 🔬 方法详解

**问题定义**：现有开放词汇目标检测器虽然在标准数据集（如COCO）上表现良好，但当应用于包含未见类别或分布差异较大的真实世界数据集时，性能会显著下降。简单地微调大型视觉-语言模型（VLM）计算成本高昂，且可能无法有效适应特定领域的需求。因此，需要一种更轻量级、更高效的方法，能够快速适应新的目标数据集，并在精度和延迟之间取得良好的平衡。

**核心思路**：RF-DETR的核心思路是利用神经架构搜索（NAS）自动发现针对特定目标数据集优化的检测器架构。通过在预训练的DETR基础上进行微调，并结合权重共享策略，可以在不重新训练的情况下评估大量不同的网络配置，从而快速找到精度和延迟之间的最佳平衡点。这种方法避免了对每个架构进行独立训练的巨大计算开销，提高了搜索效率。

**技术框架**：RF-DETR的技术框架主要包括以下几个阶段：1) 基于DETR构建基础检测器；2) 在目标数据集上微调基础检测器；3) 定义搜索空间，包括可调整的网络结构参数（如Transformer层数、头数等）；4) 使用权重共享的NAS策略，评估搜索空间中的不同架构；5) 根据精度和延迟指标，选择帕累托最优的架构。

**关键创新**：RF-DETR的关键创新在于将神经架构搜索应用于DETR，并针对目标检测任务的特点，重新审视了NAS的“可调旋钮”，即哪些网络结构参数对性能影响最大。通过优化这些参数，可以显著提高DETR在不同目标领域的迁移能力。此外，RF-DETR采用权重共享策略，避免了对每个架构进行独立训练，大大提高了搜索效率。

**关键设计**：RF-DETR的关键设计包括：1) 精心设计的搜索空间，涵盖了Transformer的多个关键参数；2) 基于精度和延迟的帕累托优化目标，旨在找到最佳的精度-延迟权衡；3) 权重共享的NAS策略，通过共享权重加速架构评估；4) 针对目标检测任务优化的损失函数和训练策略。

## 📊 实验亮点

RF-DETR在COCO数据集上取得了显著的性能提升，RF-DETR (nano) 达到了48.0 AP，超过了D-FINE (nano) 5.3 AP，且延迟相似。在Roboflow100-VL数据集上，RF-DETR (2x-large) 优于GroundingDINO (tiny) 1.2 AP，速度提升了20倍。值得注意的是，RF-DETR (2x-large) 是第一个在COCO上超过60 AP的实时检测器。

## 🎯 应用场景

RF-DETR具有广泛的应用前景，包括机器人视觉、自动驾驶、工业检测、安防监控等领域。其轻量级和高效的特性使其能够部署在资源受限的设备上，实现实时目标检测。通过针对特定领域的数据集进行优化，RF-DETR可以显著提高检测精度和效率，从而提升相关应用的性能和可靠性。未来，RF-DETR有望成为一种通用的目标检测解决方案，能够快速适应各种不同的应用场景。

## 📄 摘要（原文）

> Open-vocabulary detectors achieve impressive performance on COCO, but often fail to generalize to real-world datasets with out-of-distribution classes not typically found in their pre-training. Rather than simply fine-tuning a heavy-weight vision-language model (VLM) for new domains, we introduce RF-DETR, a light-weight specialist detection transformer that discovers accuracy-latency Pareto curves for any target dataset with weight-sharing neural architecture search (NAS). Our approach fine-tunes a pre-trained base network on a target dataset and evaluates thousands of network configurations with different accuracy-latency tradeoffs without re-training. Further, we revisit the "tunable knobs" for NAS to improve the transferability of DETRs to diverse target domains. Notably, RF-DETR significantly improves on prior state-of-the-art real-time methods on COCO and Roboflow100-VL. RF-DETR (nano) achieves 48.0 AP on COCO, beating D-FINE (nano) by 5.3 AP at similar latency, and RF-DETR (2x-large) outperforms GroundingDINO (tiny) by 1.2 AP on Roboflow100-VL while running 20x as fast. To the best of our knowledge, RF-DETR (2x-large) is the first real-time detector to surpass 60 AP on COCO. Our code is at https://github.com/roboflow/rf-detr

