---
layout: default
title: "FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation"
---

# FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16201" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16201v1</a>
  <a href="https://arxiv.org/pdf/2506.16201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16201v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16201v1', 'FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sen Wang, Le Wang, Sanping Zhou, Jingyi Tian, Jiayi Li, Haowen Sun, Wei Tang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出FlowRAM以解决机器人高精度操作中的效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `高精度任务` `生成模型` `多模态信息处理` `条件流匹配` `动态半径调度` `状态空间模型` `RLBench基准测试`

## 📋 核心要点

1. 现有的扩散基策略学习方法在推理时效率低下，未能充分利用生成模型的潜力。
2. FlowRAM框架通过动态半径调度和条件流匹配实现区域感知和高效多模态信息处理。
3. 在RLBench基准测试中，FlowRAM在高精度任务中平均成功率提高了12.0%，显著提升了推理速度。

## 📝 摘要（中文）

在高精度任务中，机器人操作对工业和现实应用至关重要，要求高准确性和速度。然而，现有的基于扩散的策略学习方法由于推理过程中的迭代去噪，通常面临计算效率低下的问题。此外，这些方法未能充分利用生成模型在3D环境中增强信息探索的潜力。为此，本文提出FlowRAM，一个新颖的框架，通过生成模型实现区域感知，促进高效的多模态信息处理。我们设计了动态半径调度，允许自适应感知，促进从全局场景理解到细粒度几何细节的过渡。通过集成状态空间模型，我们在保持线性计算复杂度的同时整合多模态信息，并采用条件流匹配通过回归确定性向量场来学习动作姿态，简化学习过程并保持性能。实验结果表明，FlowRAM在RLBench基准测试中表现出色，特别是在高精度任务中，其平均成功率比之前的方法提高了12.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于扩散的策略学习方法在高精度机器人操作中的低计算效率和信息探索不足的问题。

**核心思路**：FlowRAM框架通过引入生成模型和动态半径调度，实现区域感知和自适应信息处理，提升了多模态信息的整合效率。

**技术框架**：FlowRAM的整体架构包括动态半径调度模块、状态空间模型集成模块和条件流匹配模块，分别负责自适应感知、信息整合和动作学习。

**关键创新**：FlowRAM的核心创新在于动态半径调度和条件流匹配的结合，使得信息处理在保持线性复杂度的同时，能够有效学习复杂的动作姿态。

**关键设计**：在设计中，动态半径调度允许根据场景复杂度调整感知范围，条件流匹配通过回归确定性向量场来简化学习过程，确保高效的计算和高性能输出。

## 📊 实验亮点

FlowRAM在RLBench基准测试中实现了12.0%的平均成功率提升，特别是在高精度任务中表现突出。此外，该框架在推理速度上也显著提高，能够在不到4个时间步内生成物理上合理的动作，极大地提升了实际应用的效率。

## 🎯 应用场景

FlowRAM框架在机器人操作领域具有广泛的应用潜力，尤其是在需要高精度和快速反应的工业自动化、服务机器人和医疗机器人等场景。其高效的信息处理能力和快速推理速度将推动智能机器人在复杂环境中的应用，提升生产效率和操作安全性。

## 📄 摘要（原文）

> Robotic manipulation in high-precision tasks is essential for numerous industrial and real-world applications where accuracy and speed are required. Yet current diffusion-based policy learning methods generally suffer from low computational efficiency due to the iterative denoising process during inference. Moreover, these methods do not fully explore the potential of generative models for enhancing information exploration in 3D environments. In response, we propose FlowRAM, a novel framework that leverages generative models to achieve region-aware perception, enabling efficient multimodal information processing. Specifically, we devise a Dynamic Radius Schedule, which allows adaptive perception, facilitating transitions from global scene comprehension to fine-grained geometric details. Furthermore, we integrate state space models to integrate multimodal information, while preserving linear computational complexity. In addition, we employ conditional flow matching to learn action poses by regressing deterministic vector fields, simplifying the learning process while maintaining performance. We verify the effectiveness of the FlowRAM in the RLBench, an established manipulation benchmark, and achieve state-of-the-art performance. The results demonstrate that FlowRAM achieves a remarkable improvement, particularly in high-precision tasks, where it outperforms previous methods by 12.0% in average success rate. Additionally, FlowRAM is able to generate physically plausible actions for a variety of real-world tasks in less than 4 time steps, significantly increasing inference speed.

