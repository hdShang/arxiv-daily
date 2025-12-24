---
layout: default
title: "Grove MoE: Towards Efficient and Superior MoE LLMs with Adjugate Experts"
---

# Grove MoE: Towards Efficient and Superior MoE LLMs with Adjugate Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07785" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07785v1</a>
  <a href="https://arxiv.org/pdf/2508.07785.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07785v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07785v1', 'Grove MoE: Towards Efficient and Superior MoE LLMs with Adjugate Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyuan Wu, Haoxing Chen, Xiaodong Chen, Zhanchao Zhou, Tieyuan Chen, Yihong Zhuang, Guoshan Lu, Zenan Huang, Junbo Zhao, Lin Liu, Zhenzhong Lan, Bei Yu, Jianguo Li

**分类**: cs.CL

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出Grove MoE以解决传统MoE模型的计算效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `大规模语言模型` `动态激活` `计算效率` `模型扩展性`

## 📋 核心要点

1. 现有的MoE模型在处理不同复杂度输入时，固定激活参数数量，导致计算效率低下。
2. Grove MoE通过引入不同大小的专家和动态激活机制，提升了模型的计算效率和灵活性。
3. GroveMoE模型在动态激活参数的基础上，性能与同类或更大规模的开源模型相当，展示了显著的效率提升。

## 📝 摘要（中文）

混合专家（MoE）架构是现代大型语言模型（LLMs）的重要基础，能够通过稀疏参数激活实现可扩展性。然而，传统MoE架构使用均匀大小的专家，固定激活参数数量，限制了计算效率。为此，本文提出Grove MoE，一种新颖的架构，结合了不同大小的专家，灵感来源于异构big.LITTLE CPU架构。该架构引入了动态激活机制的伴随专家，扩展了模型容量，同时保持可控的计算开销。基于此架构，本文展示了GroveMoE-Base和GroveMoE-Inst两个33B参数的LLMs，采用了中期训练和后期训练的升级策略，动态激活3.14-3.28B参数，性能与同类或更大规模的开源模型相当。

## 🔬 方法详解

**问题定义**：传统的混合专家（MoE）模型使用均匀大小的专家，固定激活参数数量，无法根据输入复杂度动态调整，导致计算效率低下。

**核心思路**：Grove MoE通过引入不同大小的专家和动态激活机制，灵感来源于big.LITTLE CPU架构，旨在根据输入复杂度灵活激活参数，从而提升计算效率。

**技术框架**：Grove MoE架构包括多个模块，其中伴随专家负责动态激活，模型容量可以根据输入复杂度进行扩展，整体架构设计注重在保持计算开销可控的同时提升性能。

**关键创新**：Grove MoE的最大创新在于引入了伴随专家的动态激活机制，使得模型能够根据输入的复杂性灵活调整激活的参数数量，这与传统的固定激活机制形成了鲜明对比。

**关键设计**：在模型设计中，采用了33B参数的GroveMoE-Base和GroveMoE-Inst，结合中期和后期训练的升级策略，动态激活3.14-3.28B参数，确保在不同输入条件下的高效计算。

## 📊 实验亮点

Grove MoE模型在动态激活参数的基础上，成功激活3.14-3.28B参数，性能与同类或更大规模的开源模型相当，展示了显著的计算效率提升，证明了其在实际应用中的有效性。

## 🎯 应用场景

Grove MoE的研究成果具有广泛的应用潜力，尤其在自然语言处理、对话系统和智能助手等领域。通过提升计算效率，该模型能够在资源受限的环境中实现更高的性能，推动智能应用的普及与发展。

## 📄 摘要（原文）

> The Mixture of Experts (MoE) architecture is a cornerstone of modern state-of-the-art (SOTA) large language models (LLMs). MoE models facilitate scalability by enabling sparse parameter activation. However, traditional MoE architecture uses homogeneous experts of a uniform size, activating a fixed number of parameters irrespective of input complexity and thus limiting computational efficiency. To overcome this limitation, we introduce Grove MoE, a novel architecture incorporating experts of varying sizes, inspired by the heterogeneous big.LITTLE CPU architecture. This architecture features novel adjugate experts with a dynamic activation mechanism, enabling model capacity expansion while maintaining manageable computational overhead. Building on this architecture, we present GroveMoE-Base and GroveMoE-Inst, 33B-parameter LLMs developed by applying an upcycling strategy to the Qwen3-30B-A3B-Base model during mid-training and post-training. GroveMoE models dynamically activate 3.14-3.28B parameters based on token complexity and achieve performance comparable to SOTA open-source models of similar or even larger size.

