---
layout: default
title: "FADRM: Fast and Accurate Data Residual Matching for Dataset Distillation"
---

# FADRM: Fast and Accurate Data Residual Matching for Dataset Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24125" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24125v1</a>
  <a href="https://arxiv.org/pdf/2506.24125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24125v1', 'FADRM: Fast and Accurate Data Residual Matching for Dataset Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Cui, Xinyue Bi, Yaxin Luo, Xiaohan Zhao, Jiacheng Liu, Zhiqiang Shen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-30

**备注**: Code at: https://github.com/Jiacheng8/FADRM

**🔗 代码/项目**: [GITHUB](https://github.com/Jiacheng8/FADRM)

---

## 💡 一句话要点

**提出FADRM以解决数据蒸馏中的信息消失问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据蒸馏` `残差连接` `深度学习` `计算机视觉` `模型压缩` `信息保留` `优化算法`

## 📋 核心要点

1. 现有的数据蒸馏方法在处理数据时容易出现信息消失，导致模型性能下降。
2. 本文提出数据残差匹配（FADRM），利用数据级跳跃连接来优化数据生成过程。
3. 在ImageNet-1K数据集上，FADRM在单模型和多模型蒸馏中分别达到了47.7%和50.0%的测试准确率，超越了现有方法。

## 📝 摘要（中文）

残差连接在模型架构层面得到了广泛研究和应用，但在数据中心方法中的潜力尚未被探索。本文首次引入数据残差匹配的概念，通过数据级跳跃连接促进数据生成并减轻数据信息消失。该方法在像素空间优化中平衡新知识的获取与原始数据模态中的核心局部信息识别，专注于数据集蒸馏任务。此外，通过优化级别的改进，我们的方法显著提高了计算效率，训练时间和峰值GPU内存使用量减少了50%。因此，FADRM方法在多个数据集基准上建立了新的最先进水平，在效率和有效性上均表现出显著改善。

## 🔬 方法详解

**问题定义**：本文旨在解决数据蒸馏过程中信息消失的问题，现有方法在数据处理时未能有效保留重要信息，导致模型性能受限。

**核心思路**：提出数据残差匹配（FADRM），通过数据级跳跃连接来促进数据生成，平衡新知识的获取与原始数据中的核心信息识别。

**技术框架**：FADRM的整体架构包括数据级跳跃连接、像素空间优化和优化级别的改进，旨在提高数据蒸馏的效率和效果。

**关键创新**：FADRM的核心创新在于首次将数据残差匹配引入数据蒸馏任务，显著提高了计算效率和模型性能。

**关键设计**：在参数设置上，使用ResNet-18作为学生模型，设定0.8%的压缩比，采用特定的损失函数以优化数据生成过程。通过优化算法的改进，减少了训练时间和GPU内存使用。

## 📊 实验亮点

FADRM在ImageNet-1K数据集上实现了47.7%的单模型蒸馏准确率和50.0%的多模型蒸馏准确率，分别超越了RDED方法5.7%和现有多模型方法EDC与CV-DD的1.4%和4.0%。该方法在训练时间和GPU内存使用上减少了50%，展现出显著的效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、深度学习模型压缩和高效数据处理等。FADRM方法可以在资源受限的环境中实现高效的数据蒸馏，具有重要的实际价值和广泛的应用前景，尤其是在移动设备和边缘计算场景中。

## 📄 摘要（原文）

> Residual connection has been extensively studied and widely applied at the model architecture level. However, its potential in the more challenging data-centric approaches remains unexplored. In this work, we introduce the concept of Data Residual Matching for the first time, leveraging data-level skip connections to facilitate data generation and mitigate data information vanishing. This approach maintains a balance between newly acquired knowledge through pixel space optimization and existing core local information identification within raw data modalities, specifically for the dataset distillation task. Furthermore, by incorporating optimization-level refinements, our method significantly improves computational efficiency, achieving superior performance while reducing training time and peak GPU memory usage by 50%. Consequently, the proposed method Fast and Accurate Data Residual Matching for Dataset Distillation (FADRM) establishes a new state-of-the-art, demonstrating substantial improvements over existing methods across multiple dataset benchmarks in both efficiency and effectiveness. For instance, with ResNet-18 as the student model and a 0.8% compression ratio on ImageNet-1K, the method achieves 47.7% test accuracy in single-model dataset distillation and 50.0% in multi-model dataset distillation, surpassing RDED by +5.7% and outperforming state-of-the-art multi-model approaches, EDC and CV-DD, by +1.4% and +4.0%. Code is available at: https://github.com/Jiacheng8/FADRM.

