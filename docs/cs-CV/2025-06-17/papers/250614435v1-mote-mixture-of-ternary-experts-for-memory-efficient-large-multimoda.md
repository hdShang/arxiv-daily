---
layout: default
title: "MoTE: Mixture of Ternary Experts for Memory-efficient Large Multimodal Models"
---

# MoTE: Mixture of Ternary Experts for Memory-efficient Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14435" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14435v1</a>
  <a href="https://arxiv.org/pdf/2506.14435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14435v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14435v1', 'MoTE: Mixture of Ternary Experts for Memory-efficient Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Wang, Jiayu Xu, Ruiping Wang, Yan Feng, Yitao Zhai, Peng Pei, Xunliang Cai, Xilin Chen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-17

**备注**: Work in progress

---

## 💡 一句话要点

**提出MoTE以解决大规模多模态模型的内存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `三元专家` `内存效率` `多模态学习` `边缘计算` `量化方法`

## 📋 核心要点

1. 现有的多模态混合专家模型在使用全精度专家时，导致了较高的内存占用，限制了在边缘设备上的应用。
2. 本文提出MoTE，通过训练低精度的三元专家，利用共享的预训练前馈网络来降低内存消耗。
3. 实验结果显示，MoTE在内存占用更低的情况下，性能与全精度模型相当，并在特定条件下显著提升了准确率。

## 📝 摘要（中文）

大规模多模态混合专家模型（MoEs）在提升性能的同时，保持固定的活跃参数。然而，现有方法主要使用全精度专家进行稀疏上升，导致较高的内存占用，给边缘设备的部署带来挑战。本文提出MoTE，一种可扩展且内存高效的混合三元专家模型训练方法。我们通过训练更多低精度专家，利用预训练的前馈网络作为共享专家，训练参数为{-1, 0, 1}的三元路由专家。实验表明，MoTE在模型规模上具有良好的扩展趋势，其性能与全精度基线MoE-LLaVA相当，但内存占用更低。在相同的3.4GB专家内存占用下，结合后训练量化，MoTE在最终任务上比MoE-LLaVA提高了4.3%的平均准确率，展示了其在内存受限设备上的有效性和潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模多模态混合专家模型在稀疏上升过程中内存占用过高的问题。现有方法主要依赖全精度专家，导致在边缘设备上的部署面临挑战。

**核心思路**：我们提出MoTE，通过训练更多低精度的三元专家来替代高精度专家，利用预训练的前馈网络作为共享专家，从而降低内存占用并保持性能。

**技术框架**：MoTE的整体架构包括预训练的前馈网络作为共享专家，和多个参数为{-1, 0, 1}的三元路由专家。训练过程中，低精度专家的数量显著增加，以提升模型的表达能力。

**关键创新**：MoTE的核心创新在于引入了三元专家的概念，通过低精度参数的使用，显著降低了内存占用，同时保持了与全精度模型相当的性能。这一设计与现有方法形成了本质区别。

**关键设计**：在模型设计中，采用了三元量化的参数设置，损失函数经过调整以适应低精度训练，同时确保了模型的收敛性和性能表现。

## 📊 实验亮点

实验结果显示，MoTE在相同的3.4GB专家内存占用下，较全精度基线MoE-LLaVA提高了4.3%的平均准确率，展现了其在内存受限条件下的优越性能和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括边缘计算、移动设备和资源受限环境中的人工智能应用。通过降低内存占用，MoTE能够使得大规模多模态模型在更广泛的设备上得到应用，推动智能设备的普及和功能提升。

## 📄 摘要（原文）

> Large multimodal Mixture-of-Experts (MoEs) effectively scale the model size to boost performance while maintaining fixed active parameters. However, previous works primarily utilized full-precision experts during sparse up-cycling. Despite they show superior performance on end tasks, the large amount of experts introduces higher memory footprint, which poses significant challenges for the deployment on edge devices. In this work, we propose MoTE, a scalable and memory-efficient approach to train Mixture-of-Ternary-Experts models from dense checkpoint. Instead of training fewer high-precision experts, we propose to train more low-precision experts during up-cycling. Specifically, we use the pre-trained FFN as a shared expert and train ternary routed experts with parameters in {-1, 0, 1}. Extensive experiments show that our approach has promising scaling trend along model size. MoTE achieves comparable performance to full-precision baseline MoE-LLaVA while offering lower memory footprint. Furthermore, our approach is compatible with post-training quantization methods and the advantage further amplifies when memory-constraint goes lower. Given the same amount of expert memory footprint of 3.4GB and combined with post-training quantization, MoTE outperforms MoE-LLaVA by a gain of 4.3% average accuracy on end tasks, demonstrating its effectiveness and potential for memory-constrained devices.

