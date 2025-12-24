---
layout: default
title: "MobiEdit: Resource-efficient Knowledge Editing for Personalized On-device LLMs"
---

# MobiEdit: Resource-efficient Knowledge Editing for Personalized On-device LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13772" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13772v1</a>
  <a href="https://arxiv.org/pdf/2506.13772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13772v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13772v1', 'MobiEdit: Resource-efficient Knowledge Editing for Personalized On-device LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyan Lu, Daliang Xu, Dongqi Cai, Zexi Li, Wei Liu, Fangming Liu, Shangguang Wang, Mengwei Xu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出MobiEdit以解决移动设备上个性化LLM知识编辑问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识编辑` `移动设备` `个性化LLM` `量化计算` `神经处理单元` `实时编辑` `能效优化`

## 📋 核心要点

1. 现有知识编辑方法在移动设备上运行时，因反向传播过程资源消耗过大而难以实现个性化调整。
2. MobiEdit通过量化前向梯度估计替代全精度反向传播，兼容移动NPU，并引入早停机制和前缀缓存以提高效率。
3. 实验结果表明，MobiEdit在COTS移动设备上实现了对3B参数模型的实时编辑，显著降低了内存、能耗和延迟。

## 📝 摘要（中文）

大型语言模型（LLMs）在移动设备上被广泛应用于智能助手等应用中。然而，基于通用语料库预训练的LLMs在处理个性化或未见过的查询时，常常会出现幻觉现象，导致错误或过时的响应。知识编辑通过识别和调整模型权重中的小部分来解决这一问题，但现有方法因反向传播（BP）资源消耗过大而难以在本地设备上运行。本文提出了MobiEdit，这是首个在商业现成移动设备上实现高效LLM个性化的知识编辑框架。MobiEdit用量化的前向梯度估计替代全精度的反向传播，使其与能效高的移动神经处理单元（NPU）兼容。通过引入自适应早停机制和前缀缓存，进一步提高了梯度估计的效率。我们的方案使得在COTS移动设备上对3B参数模型（Qwen2.5-3B-Instruct）进行实时编辑时，内存消耗减少7.6倍，能耗减少14.7倍，延迟减少3.6倍。

## 🔬 方法详解

**问题定义**：本文旨在解决在移动设备上进行个性化LLM知识编辑时，现有方法因反向传播资源消耗过大而无法有效运行的问题。

**核心思路**：MobiEdit的核心思路是用量化的前向梯度估计替代全精度反向传播，从而降低计算资源需求，同时保持知识编辑的有效性。

**技术框架**：MobiEdit的整体架构包括前向梯度估计模块、早停机制和前缀缓存。前向梯度估计模块负责计算梯度，早停机制在成功时自适应终止编辑，而前缀缓存则用于重用计算结果以提高效率。

**关键创新**：MobiEdit的关键创新在于其量化前向梯度估计方法，这一方法与传统的全精度反向传播相比，显著降低了内存和能耗，同时保持了知识编辑的准确性。

**关键设计**：MobiEdit在参数设置上进行了优化，采用了适应性早停机制以减少不必要的计算，并设计了前缀缓存以提高计算效率，确保在移动设备上实现实时编辑。

## 📊 实验亮点

实验结果显示，MobiEdit在COTS移动设备上对3B参数模型的实时编辑实现了7.6倍的内存节省、14.7倍的能耗降低和3.6倍的延迟减少，相较于以往的知识编辑方法，表现出显著的性能提升。

## 🎯 应用场景

MobiEdit的研究具有广泛的应用潜力，尤其是在智能助手、个性化推荐系统和移动应用中。通过在移动设备上实现高效的知识编辑，用户能够获得更准确和及时的响应，从而提升用户体验。未来，该技术可能推动更多基于LLM的个性化应用的发展。

## 📄 摘要（原文）

> Large language models (LLMs) are deployed on mobile devices to power killer applications such as intelligent assistants. LLMs pre-trained on general corpora often hallucinate when handling personalized or unseen queries, leading to incorrect or outdated responses. Knowledge editing addresses this by identifying and adjusting a small crucial portion of model weights, without compromising the general knowledge. However, prior knowledge editing methods are impractical to run on local devices due to the resource-heavy backpropagation (BP) needed for updates. We present MobiEdit, the first mobile knowledge editing framework that enables efficient LLM personalization on commercial off-the-shelf (COTS) mobile devices. MobiEdit replaces full-precision BP with quantized forward-only gradient estimation, thus compatible with the energy-efficient mobile neural processing units (NPUs). MobiEdit replaces full-precision backpropagation with quantized forward-only gradient estimation, making it compatible with energy-efficient mobile NPUs. To further improve gradient estimation efficiency, we introduce two optimizations: an early stoping mechanism that adaptively terminates editing upon success and a prefix cache that reuses computation across steps. Our approach enables real-time editing of a 3B-parameter model (Qwen2.5-3B-Instruct) on COTS mobile devices with 7.6$\times$ less memory, 14.7 $\times$ less energy and 3.6$\times$ less latency compared to previous knowledge editing methods.

