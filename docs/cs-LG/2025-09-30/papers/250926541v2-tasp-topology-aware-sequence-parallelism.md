---
layout: default
title: "TASP: Topology-aware Sequence Parallelism"
---

# TASP: Topology-aware Sequence Parallelism

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26541" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26541v2</a>
  <a href="https://arxiv.org/pdf/2509.26541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26541v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26541v2', 'TASP: Topology-aware Sequence Parallelism')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yida Wang, Ke Hong, Xiuhong Li, Yuanchao Xu, Wenxun Wang, Guohao Dai, Yu Wang

**分类**: cs.LG, cs.DC

**发布日期**: 2025-09-30 (更新: 2025-10-09)

**🔗 代码/项目**: [GITHUB](https://github.com/infinigence/HamiltonAttention)

---

## 💡 一句话要点

**TASP：一种拓扑感知的序列并行方法，提升长文本LLM在现代加速器上的通信效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `序列并行` `长文本LLM` `拓扑感知` `通信优化` `AlltoAll拓扑`

## 📋 核心要点

1. Ring Attention在长文本LLM中通信效率低，原因是其Ring AllGather通信原语与现代加速器的AlltoAll拓扑结构不匹配。
2. TASP通过拓扑分解和原语分解，将加速器拓扑分解为多个正交环形数据路径，并发传输数据，充分利用通信能力。
3. 实验表明，TASP在NVIDIA H100和AMD MI300X系统上比Ring Attention及其变体实现了更高的通信效率和显著的加速。

## 📝 摘要（中文）

长上下文大型语言模型（LLMs）由于自注意力机制的二次复杂度而面临约束。主流的序列并行（SP）方法Ring Attention试图通过将query分发到多个加速器上的query块，并通过Ring AllGather通信原语使每个Q张量能够访问来自其他加速器的所有KV张量来解决这个问题。然而，它表现出较低的通信效率，限制了其在实际中的应用。这种低效率源于它所采用的Ring AllGather通信原语与现代加速器的AlltoAll拓扑结构之间的不匹配。Ring AllGather原语由迭代的环形数据传输组成，这只能利用AlltoAll拓扑结构中非常有限的一部分。受完整有向图的哈密顿分解的启发，我们发现现代加速器拓扑可以分解为多个正交的环形数据路径，这些路径可以并发地传输数据而不会相互干扰。基于此，我们进一步观察到Ring AllGather原语也可以在每次迭代中分解为相同数量的并发环形数据传输。基于这些见解，我们提出了一种用于长上下文LLM的拓扑感知SP方法TASP，该方法通过拓扑分解和原语分解充分利用了现代加速器的通信能力。在单节点和多节点NVIDIA H100系统以及单节点AMD MI300X系统上的实验结果表明，TASP在这些现代加速器拓扑上实现了比Ring Attention更高的通信效率，并且比Ring Attention及其变体Zigzag-Ring Attention实现了高达3.58倍的加速。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本LLM中，由于自注意力机制的二次复杂度，导致序列并行方法（如Ring Attention）在现代加速器上通信效率低下的问题。Ring Attention采用的Ring AllGather通信原语与现代加速器的AlltoAll拓扑结构不匹配，造成通信瓶颈。

**核心思路**：论文的核心思路是充分利用现代加速器的AlltoAll拓扑结构。通过将加速器拓扑分解为多个正交的环形数据路径，并同时分解Ring AllGather原语，实现并发的数据传输，从而提高通信效率。这种设计基于完整有向图的哈密顿分解，确保数据传输不会相互干扰。

**技术框架**：TASP方法主要包含两个关键步骤：1) 拓扑分解：将现代加速器的AlltoAll拓扑分解为多个正交的环形数据路径。2) 原语分解：将Ring AllGather原语分解为相同数量的并发环形数据传输。这两个步骤协同工作，使得数据可以在多个环形路径上并行传输，从而充分利用加速器的通信带宽。

**关键创新**：TASP最重要的技术创新点在于其拓扑感知的设计。它不再简单地使用传统的Ring AllGather原语，而是根据现代加速器的实际拓扑结构进行优化，通过拓扑分解和原语分解，实现了更高的通信效率。与Ring Attention相比，TASP能够更好地适应现代加速器的AlltoAll拓扑结构。

**关键设计**：TASP的关键设计在于如何进行拓扑分解和原语分解。具体来说，需要根据加速器的互联结构，找到一组正交的环形数据路径，并设计相应的通信调度算法，以确保数据在这些路径上高效地传输。论文中可能包含关于如何选择这些环形路径，以及如何进行数据分片和聚合的细节。

## 📊 实验亮点

实验结果表明，TASP在单节点和多节点NVIDIA H100系统以及单节点AMD MI300X系统上均优于Ring Attention及其变体Zigzag-Ring Attention。TASP实现了高达3.58倍的加速，证明了其在现代加速器上具有更高的通信效率和性能优势。这些结果表明TASP是一种有效的长文本LLM序列并行方法。

## 🎯 应用场景

TASP的潜在应用领域包括长文本生成、对话系统、文档摘要等需要处理长序列数据的LLM应用。通过提高通信效率，TASP可以加速这些应用的训练和推理过程，降低计算成本，并支持更大规模的模型训练。未来，TASP可以进一步推广到其他类型的并行计算框架和加速器架构上。

## 📄 摘要（原文）

> Long-context large language models (LLMs) face constraints due to the quadratic complexity of the self-attention mechanism. The mainstream sequence parallelism (SP) method, Ring Attention, attempts to solve this by distributing the query into multiple query chunks across accelerators and enable each Q tensor to access all KV tensors from other accelerators via the Ring AllGather communication primitive. However, it exhibits low communication efficiency, restricting its practical applicability. This inefficiency stems from the mismatch between the Ring AllGather communication primitive it adopts and the AlltoAll topology of modern accelerators. A Ring AllGather primitive is composed of iterations of ring-styled data transfer, which can only utilize a very limited fraction of an AlltoAll topology.
>   Inspired by the Hamiltonian decomposition of complete directed graphs, we identify that modern accelerator topology can be decomposed into multiple orthogonal ring datapaths which can concurrently transfer data without interference. Based on this, we further observe that the Ring AllGather primitive can also be decomposed into the same number of concurrent ring-styled data transfer at every iteration. Based on these insights, we propose TASP, a topology-aware SP method for long-context LLMs that fully utilizes the communication capacity of modern accelerators via topology decomposition and primitive decomposition. Experimental results on both single-node and multi-node NVIDIA H100 systems and a single-node AMD MI300X system demonstrate that TASP achieves higher communication efficiency than Ring Attention on these modern accelerator topologies and achieves up to 3.58 speedup than Ring Attention and its variant Zigzag-Ring Attention. The code is available at https://github.com/infinigence/HamiltonAttention.

