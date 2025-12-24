---
layout: default
title: "Layer as Puzzle Pieces: Compressing Large Language Models through Layer Concatenation"
---

# Layer as Puzzle Pieces: Compressing Large Language Models through Layer Concatenation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15304" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15304v1</a>
  <a href="https://arxiv.org/pdf/2510.15304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15304v1', 'Layer as Puzzle Pieces: Compressing Large Language Models through Layer Concatenation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Wang, Li Shen, Liang Ding, Chao Xue, Ye Liu, Changxing Ding

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-17

**🔗 代码/项目**: [GITHUB](https://github.com/MPI-Lab/CoMe)

---

## 💡 一句话要点

**提出CoMe：通过层拼接压缩大语言模型，在显著剪枝的同时保持性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型压缩` `结构化剪枝` `层拼接` `知识蒸馏` `模型优化`

## 📋 核心要点

1. 现有大模型剪枝方法直接移除层或简单聚合权重，导致性能显著下降，且缺乏有效的后训练恢复机制。
2. CoMe通过通道敏感度指标选择重要通道，利用层拼接融合相邻层，并采用分层蒸馏进行知识迁移。
3. 实验表明，CoMe在剪枝LLaMA-2-7b 30%参数后，仍能保持原始模型83%的平均准确率，达到SOTA性能。

## 📝 摘要（中文）

大型语言模型在自然语言处理任务中表现出色，但其庞大的规模导致了高昂的计算和存储需求。目前的工作试图通过逐层结构化剪枝来减小模型尺寸，但往往忽略了保留被剪枝部分的能力。本文重新审视了结构化剪枝范式，揭示了几个关键限制：1) 直接移除层导致显著的性能下降；2) 线性权重层聚合能力不足；3) 缺乏有效的后训练恢复机制。为了解决这些限制，我们提出了CoMe，包括一个渐进式层剪枝框架，该框架具有基于拼接的合并技术和分层蒸馏后训练过程。具体来说，我们引入了一种通道敏感度指标，该指标利用激活强度和权重范数进行细粒度的通道选择。随后，我们采用基于拼接的层合并方法来融合相邻层中最关键的通道，从而实现模型尺寸的逐步减小。最后，我们提出了一种分层蒸馏协议，该协议利用在剪枝期间建立的原始模型和剪枝模型层之间的对应关系，从而实现有效的知识转移。在七个基准测试上的实验表明，CoMe 实现了最先进的性能；当剪枝 LLaMA-2-7b 的 30% 参数时，剪枝后的模型保留了其原始平均准确率的 83%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）体积过大，导致计算和存储成本高昂的问题。现有的结构化剪枝方法，如直接移除层或使用简单的线性权重聚合，会导致严重的性能下降，并且缺乏有效的后训练恢复机制，无法充分利用被剪枝部分蕴含的知识。

**核心思路**：论文的核心思路是通过渐进式的层剪枝和拼接合并，以及分层蒸馏，在减小模型尺寸的同时，尽可能保留原始模型的性能。通过通道敏感度指标选择重要的通道，并将其拼接合并到相邻层，从而实现模型的压缩。分层蒸馏则用于将原始模型的知识迁移到压缩后的模型，弥补剪枝带来的性能损失。

**技术框架**：CoMe框架包含三个主要阶段：1) **渐进式层剪枝**：使用通道敏感度指标选择要剪枝的通道。2) **基于拼接的层合并**：将相邻层中选择出的重要通道进行拼接合并，减少模型参数量。3) **分层蒸馏**：利用原始模型和剪枝模型层之间的对应关系，进行知识迁移，提升剪枝后模型的性能。

**关键创新**：CoMe的关键创新在于：1) **基于拼接的层合并方法**：不同于传统的权重聚合方法，CoMe通过拼接通道来融合相邻层，能够更有效地保留被剪枝部分的信息。2) **分层蒸馏协议**：利用剪枝过程中建立的原始模型和剪枝模型层之间的对应关系，进行更有效的知识迁移。

**关键设计**：通道敏感度指标结合了激活强度和权重范数，用于细粒度的通道选择。拼接合并操作将相邻层的重要通道在通道维度上进行拼接。分层蒸馏损失函数包括了中间层特征的蒸馏损失，以及最终输出的蒸馏损失。具体的损失函数权重和训练epoch等超参数需要根据具体模型和数据集进行调整。

## 📊 实验亮点

CoMe在七个基准测试上取得了SOTA性能。在剪枝LLaMA-2-7b模型30%的参数后，剪枝后的模型仍然保留了原始模型83%的平均准确率。相较于其他剪枝方法，CoMe在相同剪枝比例下，能够更好地保持模型的性能。

## 🎯 应用场景

该研究成果可应用于各种需要部署大型语言模型的场景，例如移动设备、边缘计算设备等资源受限的环境。通过压缩模型尺寸，可以降低计算和存储成本，提高推理速度，从而使LLM能够在更广泛的领域得到应用。此外，该方法还可以用于模型加速和模型安全等领域。

## 📄 摘要（原文）

> Large Language Models excel at natural language processing tasks, but their massive size leads to high computational and storage demands. Recent works have sought to reduce their model size through layer-wise structured pruning. However, they tend to ignore retaining the capabilities in the pruned part. In this work, we re-examine structured pruning paradigms and uncover several key limitations: 1) notable performance degradation due to direct layer removal, 2) incompetent linear weight layer aggregation, and 3) the lack of effective post-training recovery mechanisms. To address these limitations, we propose CoMe, including a progressive layer pruning framework with a Concatenation-based Merging technology and a hierarchical distillation post-training process. Specifically, we introduce a channel sensitivity metric that utilizes activation intensity and weight norms for fine-grained channel selection. Subsequently, we employ a concatenation-based layer merging method to fuse the most critical channels across adjacent layers, enabling progressive model size reduction. Finally, we propose a hierarchical distillation protocol that leverages the correspondences between the original and pruned model layers established during pruning, thereby enabling efficient knowledge transfer. Experiments on seven benchmarks show that CoMe achieves state-of-the-art performance; when pruning 30% of LLaMA-2-7b's parameters, the pruned model retains 83% of its original average accuracy. Our code is available at https://github.com/MPI-Lab/CoMe.

