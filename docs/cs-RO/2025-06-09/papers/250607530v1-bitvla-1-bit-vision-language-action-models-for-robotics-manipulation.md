---
layout: default
title: "BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation"
---

# BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07530" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07530v1</a>
  <a href="https://arxiv.org/pdf/2506.07530.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07530v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07530v1', 'BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Wang, Chuyan Xiong, Ruiping Wang, Xilin Chen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-09

**备注**: Work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/ustcwhy/BitVLA)

---

## 💡 一句话要点

**提出BitVLA以解决机器人操作中的模型部署问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `机器人操作` `1位模型` `蒸馏训练` `内存优化` `边缘计算` `模型压缩`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在规模不断增大的情况下，难以在资源受限的机器人系统上进行有效部署。
2. 本文提出的BitVLA模型通过将参数压缩为三元组形式，显著降低了内存占用，同时保持了模型性能。
3. 实验结果表明，BitVLA在LIBERO基准测试中表现出与OpenVLA-OFT相当的性能，内存消耗仅为29.8%。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在机器人操作任务中展现出令人印象深刻的能力。然而，模型规模的不断扩大给资源受限的机器人系统的部署带来了重大挑战。尽管1位预训练在提升大型语言模型推理效率方面已被证明有效，但其在VLA模型中的应用仍未得到充分探索。本文提出了BitVLA，这是首个用于机器人操作的1位VLA模型，其中每个参数为三元组{-1, 0, 1}。为了进一步减少视觉编码器的内存占用，我们提出了蒸馏感知训练策略，将全精度编码器压缩至1.58位权重。尽管缺乏大规模的机器人预训练，BitVLA在LIBERO基准测试中实现了与最先进模型OpenVLA-OFT相当的性能，同时仅消耗29.8%的内存。这些结果突显了BitVLA在内存受限边缘设备上的部署潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在资源受限的机器人系统中部署困难的问题。随着模型规模的增大，传统方法在内存和计算效率上面临挑战。

**核心思路**：论文提出的BitVLA模型通过将每个参数压缩为三元组{-1, 0, 1}，实现了1位VLA模型的构建，从而在保持性能的同时显著降低内存占用。

**技术框架**：BitVLA的整体架构包括一个视觉编码器和一个语言-动作解码器。视觉编码器通过蒸馏感知训练策略进行优化，使用全精度编码器作为教师模型来对齐潜在表示。

**关键创新**：BitVLA的主要创新在于首次将1位预训练应用于视觉-语言-动作模型，且通过蒸馏训练策略有效压缩了视觉编码器的权重，显著降低了内存需求。

**关键设计**：在模型设计中，采用了三元组参数表示，损失函数设计上注重对齐潜在表示的准确性，同时在训练过程中引入了教师模型以提升压缩效果。整体模型的内存占用仅为传统模型的29.8%。

## 📊 实验亮点

在LIBERO基准测试中，BitVLA模型的性能与最先进的OpenVLA-OFT模型相当，且内存消耗仅为29.8%。这一结果表明，BitVLA在资源受限的边缘设备上具有显著的应用潜力。

## 🎯 应用场景

BitVLA模型的潜在应用领域包括智能机器人、自动化生产线以及边缘计算设备等。其在内存受限环境中的高效性能使其适用于实时操作和决策场景，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have shown impressive capabilities across a wide range of robotics manipulation tasks. However, their growing model size poses significant challenges for deployment on resource-constrained robotic systems. While 1-bit pretraining has proven effective for enhancing the inference efficiency of large language models with minimal performance loss, its application to VLA models remains underexplored. In this work, we present BitVLA, the first 1-bit VLA model for robotics manipulation, in which every parameter is ternary, i.e., {-1, 0, 1}. To further reduce the memory footprint of the vision encoder, we propose the distillation-aware training strategy that compresses the full-precision encoder to 1.58-bit weights. During this process, a full-precision encoder serves as a teacher model to better align latent representations. Despite the lack of large-scale robotics pretraining, BitVLA achieves performance comparable to the state-of-the-art model OpenVLA-OFT with 4-bit post-training quantization on the LIBERO benchmark, while consuming only 29.8% of the memory. These results highlight BitVLA's promise for deployment on memory-constrained edge devices. We release the code and model weights in https://github.com/ustcwhy/BitVLA.

