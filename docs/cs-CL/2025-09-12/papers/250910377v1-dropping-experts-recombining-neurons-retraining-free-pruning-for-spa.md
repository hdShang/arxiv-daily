---
layout: default
title: "Dropping Experts, Recombining Neurons: Retraining-Free Pruning for Sparse Mixture-of-Experts LLMs"
---

# Dropping Experts, Recombining Neurons: Retraining-Free Pruning for Sparse Mixture-of-Experts LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10377" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10377v1</a>
  <a href="https://arxiv.org/pdf/2509.10377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10377v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10377v1', 'Dropping Experts, Recombining Neurons: Retraining-Free Pruning for Sparse Mixture-of-Experts LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixiao Zhou, Ziyu Zhao, Dongzhou Cheng, zhiliang wu, Jie Gui, Yi Yang, Fei Wu, Yu Cheng, Hehe Fan

**分类**: cs.CL

**发布日期**: 2025-09-12

**备注**: Accepted to EMNLP2025

---

## 💡 一句话要点

**提出DERN：一种免训练的专家剪枝与神经元重组框架，提升稀疏MoE LLM性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏混合专家模型` `模型剪枝` `神经元重组` `免训练` `大型语言模型`

## 📋 核心要点

1. SMoE模型虽高效，但需加载所有专家参数，导致高内存占用，限制了部署。
2. DERN通过剪枝冗余专家，并将剩余专家分解为神经元片段，再重组优化。
3. 实验表明，DERN在50%稀疏度下，无需额外训练，性能提升超5%，并显著降低内存占用。

## 📝 摘要（中文）

稀疏混合专家(SMoE)架构因其计算效率而被广泛应用于大型语言模型(LLMs)中。然而，尽管每个token只激活少数专家，SMoE仍然需要加载所有专家参数，导致高内存占用和部署挑战。先前的工作主要集中在专家级别的剪枝和合并，而忽略了神经元级别的结构。我们提出了DERN（Dropping Experts, Recombining Neurons），一个任务无关且免训练的专家剪枝和重构框架。我们观察到专家在神经元级别上经常不对齐，并包含语义冲突，这对直接合并提出了挑战。为了解决这个问题，DERN分三个步骤工作：首先，它使用路由统计信息剪枝冗余专家；然后，它将它们分解为神经元级别的专家片段，并将每个片段分配给其最兼容的保留专家；最后，它合并每个保留专家内的片段，以构建紧凑的表示。在Mixtral、Qwen和DeepSeek SMoE模型上的实验表明，在50%的专家稀疏性下，DERN在常识推理和MMLU基准测试中提高了5%以上的性能，而无需额外的训练。它还大大减少了专家数量和内存使用，使SMoE LLM在实践中更容易部署。

## 🔬 方法详解

**问题定义**：现有稀疏混合专家模型（SMoE LLMs）虽然在计算上高效，但由于需要加载所有专家的参数，因此内存占用仍然很高，这给模型的部署带来了挑战。以往的研究主要集中在专家层面的剪枝和合并，而忽略了神经元层面的结构，导致优化效果受限。此外，直接合并专家可能会因为神经元级别的不对齐和语义冲突而导致性能下降。

**核心思路**：DERN的核心思路是通过细粒度的神经元级别的操作来实现更有效的专家剪枝和重构。它首先剪枝冗余的专家，然后将剩余的专家分解成神经元级别的片段，并将这些片段重新分配给最合适的保留专家。通过这种方式，DERN能够避免直接合并专家带来的语义冲突问题，并构建更紧凑的模型表示。

**技术框架**：DERN框架包含三个主要步骤：1) **专家剪枝**：使用路由统计信息来识别和剪枝冗余的专家。2) **神经元片段分解与分配**：将剪枝的专家分解为神经元级别的片段，并将每个片段分配给最兼容的保留专家。兼容性通过某种相似度度量来衡量。3) **片段合并**：在每个保留专家内部，合并分配给它的神经元片段，以构建一个更紧凑的专家表示。

**关键创新**：DERN的关键创新在于其神经元级别的专家重构方法。与以往的专家层面操作不同，DERN能够更精细地控制模型的结构，并避免了直接合并专家可能带来的语义冲突。此外，DERN是一个免训练的框架，这意味着它可以在不进行额外训练的情况下直接应用于现有的SMoE模型。

**关键设计**：DERN的关键设计包括：1) 使用路由统计信息进行专家剪枝，例如可以基于专家被激活的频率来判断其冗余程度。2) 定义神经元片段之间的兼容性度量，例如可以使用余弦相似度或其他的神经元激活模式相似度度量。3) 设计片段合并策略，例如可以简单地将分配给同一专家的神经元片段进行拼接或加权平均。

## 📊 实验亮点

DERN在Mixtral、Qwen和DeepSeek等SMoE模型上进行了实验，结果表明，在50%的专家稀疏性下，DERN在常识推理和MMLU基准测试中实现了超过5%的性能提升，而无需额外的训练。此外，DERN还显著减少了专家数量和内存使用，验证了其在模型压缩和性能提升方面的有效性。

## 🎯 应用场景

DERN框架可应用于各种基于SMoE架构的大型语言模型，尤其适用于资源受限的部署环境，如移动设备或边缘计算设备。通过降低内存占用和模型大小，DERN可以使这些模型更容易部署和运行，从而加速LLM在实际应用中的普及。此外，DERN还可以作为一种模型压缩和加速的通用技术，应用于其他类型的神经网络。

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (SMoE) architectures are widely used in large language models (LLMs) due to their computational efficiency. However, though only a few experts are activated for each token, SMoE still requires loading all expert parameters, leading to high memory usage and challenges in deployment. Previous work has tried to reduce the overhead by pruning and merging experts, but primarily focused on expert-level operations, leaving neuron-level structure underexplored. We propose DERN (Dropping Experts, Recombining Neurons), a task-agnostic and retraining-free framework for expert pruning and reconstruction. We observe that experts are often misaligned and contain semantic conflicts at the neuron level, which poses challenges for direct merging. To solve this, DERN works in three steps: it first prunes redundant experts using router statistics; then it decomposes them into neuron-level expert segments, assigning each segment to its most compatible retained expert; and finally, it merges segments within each retained expert to build a compact representation. Experiments on Mixtral, Qwen, and DeepSeek SMoE models show that DERN improves performance by more than 5% on commonsense reasoning and MMLU benchmarks under 50% expert sparsity, without extra training. It also greatly reduces the number of experts and memory usage, making SMoE LLMs easier to deploy in practice.

