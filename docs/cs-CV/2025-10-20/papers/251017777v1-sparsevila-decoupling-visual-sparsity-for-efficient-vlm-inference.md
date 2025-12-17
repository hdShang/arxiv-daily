---
layout: default
title: SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference
---

# SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17777" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17777v1</a>
  <a href="https://arxiv.org/pdf/2510.17777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17777v1" onclick="toggleFavorite(this, '2510.17777v1', 'SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, Zhijian Liu

**分类**: cs.CV

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**SparseVILA：解耦视觉稀疏性，加速高效VLM推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `VLM` `视觉稀疏性` `推理加速` `长视频理解`

## 📋 核心要点

1. 现有VLM推理受限于视觉token数量庞大，导致延迟高，扩展性受限。
2. SparseVILA解耦预填充和解码阶段的视觉稀疏性，实现高效VLM推理。
3. SparseVILA在长视频任务上加速2.6倍，并提升文档理解和推理准确性。

## 📝 摘要（中文）

视觉语言模型(VLM)在集成视觉和文本推理方面取得了快速进展，推动了高分辨率图像理解、长视频分析和多轮对话等应用。然而，视觉token数量的增长限制了其可扩展性，并主导了推理延迟。我们提出了SparseVILA，一种高效VLM推理的新范式，它解耦了预填充和解码阶段的视觉稀疏性。SparseVILA通过在预填充期间剪枝冗余视觉token，并在解码期间仅检索与查询相关的token，从而在各个阶段分配稀疏性。这种解耦设计与领先的预填充剪枝方法相匹配，同时通过保留大部分视觉缓存来保持多轮保真度，以便可以在每个对话轮次检索感知查询的token。SparseVILA建立在AWQ优化的推理管道之上，在长上下文视频任务上实现了高达4.0倍的预填充加速、2.5倍的解码加速以及2.6倍的端到端加速，同时提高了文档理解和推理任务的准确性。通过解耦与查询无关的剪枝和与查询相关的检索，SparseVILA为高效多模态推理建立了一个新方向，提供了一个无需训练、架构无关的框架，用于加速大型VLM，而不会牺牲能力。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在处理高分辨率图像、长视频等任务时，需要处理大量的视觉token，这导致了巨大的计算开销和推理延迟，限制了VLM的实际应用。现有的方法通常难以在效率和性能之间取得平衡，尤其是在多轮对话等需要长期上下文的任务中。

**核心思路**：SparseVILA的核心思路是将视觉信息的稀疏化过程解耦为两个阶段：预填充阶段的与查询无关的剪枝，以及解码阶段的与查询相关的检索。通过这种解耦，可以在预填充阶段去除冗余的视觉token，减少计算量，同时在解码阶段只关注与当前查询相关的token，提高推理效率和准确性。

**技术框架**：SparseVILA的整体框架包含两个主要阶段：预填充阶段和解码阶段。在预填充阶段，使用剪枝算法去除冗余的视觉token，生成稀疏的视觉表示。在解码阶段，根据当前查询，从稀疏的视觉表示中检索相关的token，并将其与文本信息融合，进行推理。该框架可以与现有的VLM架构相结合，无需重新训练。

**关键创新**：SparseVILA的关键创新在于解耦了视觉稀疏性，将剪枝和检索过程分离。这种解耦使得可以在预填充阶段进行全局的、与查询无关的剪枝，减少计算量，同时在解码阶段进行局部的、与查询相关的检索，提高推理效率和准确性。与现有方法相比，SparseVILA能够在保持性能的同时，显著降低计算开销。

**关键设计**：SparseVILA的关键设计包括：1) 使用AWQ进行量化，进一步加速推理；2) 设计了合适的剪枝策略，在预填充阶段去除冗余的视觉token；3) 设计了高效的检索算法，在解码阶段快速找到与查询相关的token。具体的剪枝策略和检索算法的选择取决于具体的应用场景和VLM架构。

## 📊 实验亮点

SparseVILA在长上下文视频任务上实现了高达4.0倍的预填充加速、2.5倍的解码加速以及2.6倍的端到端加速。同时，SparseVILA在文档理解和推理任务上提高了准确性。这些结果表明，SparseVILA能够在显著提高推理效率的同时，保持甚至提高VLM的性能。

## 🎯 应用场景

SparseVILA适用于需要处理大量视觉信息的视觉语言模型应用，例如长视频理解、高分辨率图像分析、多轮对话等。该方法可以显著降低计算开销和推理延迟，提高VLM的实际应用价值，并推动VLM在资源受限设备上的部署。未来，SparseVILA可以进一步扩展到其他多模态任务，例如视觉问答、图像描述等。

## 📄 摘要（原文）

> Vision Language Models (VLMs) have rapidly advanced in integrating visual and textual reasoning, powering applications across high-resolution image understanding, long-video analysis, and multi-turn conversation. However, their scalability remains limited by the growing number of visual tokens that dominate inference latency. We present SparseVILA, a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding. This decoupled design matches leading prefill pruning methods while preserving multi-turn fidelity by retaining most of the visual cache so that query-aware tokens can be retrieved at each conversation round. Built on an AWQ-optimized inference pipeline, SparseVILA achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup on long-context video tasks -- while improving accuracy on document-understanding and reasoning tasks. By decoupling query-agnostic pruning and query-aware retrieval, SparseVILA establishes a new direction for efficient multimodal inference, offering a training-free, architecture-agnostic framework for accelerating large VLMs without sacrificing capability.

