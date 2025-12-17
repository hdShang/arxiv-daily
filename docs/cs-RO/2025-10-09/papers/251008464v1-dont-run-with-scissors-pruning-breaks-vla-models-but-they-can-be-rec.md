---
layout: default
title: Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered
---

# Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08464" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08464v1</a>
  <a href="https://arxiv.org/pdf/2510.08464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08464v1" onclick="toggleFavorite(this, '2510.08464v1', 'Don\'t Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-09

**🔗 代码/项目**: [PROJECT_PAGE](https://gluestick-vla.github.io/)

---

## 💡 一句话要点

**提出GLUESTICK，用于恢复剪枝后VLA模型性能，提升机器人操作和导航安全性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `模型剪枝` `模型恢复` `机器人` `权重插值` `资源受限设备` `安全导航`

## 📋 核心要点

1. VLA模型在机器人领域潜力巨大，但模型体积大，难以在资源受限设备上部署。
2. GLUESTICK通过在权重空间中插值计算校正项，无需额外训练即可恢复剪枝模型的性能。
3. 实验表明，GLUESTICK在保持内存效率的同时，显著提升了VLA模型在操作和导航任务中的成功率，并降低了安全风险。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型提升了机器人能力，但部署在资源受限的硬件上仍然具有挑战性。剪枝已成为压缩大型语言模型（LLM）的有效方法，但在机器人领域的研究还不够充分。令人惊讶的是，我们观察到剪枝VLA模型会导致性能急剧下降，并增加安全违规。我们提出了GLUESTICK，一种剪枝后恢复方法，可以在保持稀疏性的同时恢复原始模型的大部分功能。我们的方法在权重空间中执行密集模型和剪枝模型之间的一次性插值，以计算校正项。在推理过程中，每个剪枝层使用此校正来恢复损失的能力，且开销最小。GLUESTICK不需要额外的训练，与剪枝算法无关，并引入了一个超参数来控制效率和准确性之间的权衡。在操作和导航中，针对不同的VLA架构和任务，GLUESTICK实现了具有竞争力的内存效率，同时显著提高了成功率并减少了安全违规。

## 🔬 方法详解

**问题定义**：论文旨在解决VLA模型剪枝后性能大幅下降的问题。现有方法在压缩LLM方面取得了进展，但直接应用于VLA模型会导致严重的性能损失，甚至增加安全风险，使得剪枝后的模型无法有效部署在机器人应用中。

**核心思路**：GLUESTICK的核心思路是在剪枝后，通过对原始密集模型和剪枝模型的权重进行插值，计算出一个校正项。这个校正项可以补偿剪枝过程中丢失的信息，从而恢复模型的性能。这种方法无需重新训练，且计算开销小，适合在线部署。

**技术框架**：GLUESTICK是一个后处理方法，可以应用于任何剪枝算法。其主要流程包括：1) 使用某种剪枝算法对VLA模型进行剪枝；2) 在权重空间中，对原始密集模型的权重和剪枝模型的权重进行插值，得到一个校正项；3) 在推理过程中，将该校正项添加到剪枝模型的每一层，以恢复其性能。

**关键创新**：GLUESTICK的关键创新在于提出了一种简单有效的后处理方法，可以在不重新训练的情况下恢复剪枝模型的性能。它通过权重插值的方式，弥补了剪枝过程中丢失的信息，从而在保持模型稀疏性的同时，提高了模型的准确性和安全性。

**关键设计**：GLUESTICK引入了一个超参数，用于控制密集模型和剪枝模型权重之间的插值比例。这个超参数可以根据具体的任务和模型进行调整，以达到最佳的性能和效率平衡。校正项的计算公式为：`W_corrected = W_pruned + α * (W_dense - W_pruned)`，其中`W_corrected`是校正后的权重，`W_pruned`是剪枝后的权重，`W_dense`是原始密集模型的权重，`α`是插值系数（超参数）。

## 📊 实验亮点

实验结果表明，GLUESTICK能够显著恢复剪枝后VLA模型的性能。在多个操作和导航任务中，GLUESTICK在保持与剪枝模型相近的内存效率的同时，显著提高了成功率，并减少了安全违规。例如，在某些任务中，GLUESTICK可以将成功率提高到接近原始密集模型的水平，同时保持了较高的稀疏度。

## 🎯 应用场景

GLUESTICK具有广泛的应用前景，可以应用于各种需要部署在资源受限设备上的机器人应用，例如移动机器人、无人机和协作机器人。通过对VLA模型进行剪枝和使用GLUESTICK进行恢复，可以在保持模型性能的同时，显著降低模型的计算和存储成本，从而实现更高效、更安全的机器人操作和导航。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

