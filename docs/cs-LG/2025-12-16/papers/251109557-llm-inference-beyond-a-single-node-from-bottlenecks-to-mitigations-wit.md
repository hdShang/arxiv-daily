---
layout: default
title: LLM Inference Beyond a Single Node: From Bottlenecks to Mitigations with Fast All-Reduce Communication
---

# LLM Inference Beyond a Single Node: From Bottlenecks to Mitigations with Fast All-Reduce Communication

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09557" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09557</a>
  <a href="https://arxiv.org/pdf/2511.09557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09557" onclick="toggleFavorite(this, '2511.09557', 'LLM Inference Beyond a Single Node: From Bottlenecks to Mitigations with Fast All-Reduce Communication')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prajwal Singhania, Siddharth Singh, Lannie Dalton Hough, Akarsh Srivastava, Harshitha Menon, Charles Fredrick Jekel, Abhinav Bhatele

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对LLM多节点推理瓶颈，提出基于快速All-Reduce通信的NVRAR算法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `分布式推理` `模型并行` `All-Reduce` `NVSHMEM` `高性能计算` `通信优化`

## 📋 核心要点

1. 现有LLM推理引擎在多节点扩展时面临通信瓶颈，特别是All-Reduce操作的延迟问题。
2. 论文提出NVRAR算法，利用NVSHMEM实现分层All-Reduce，旨在降低通信延迟，提升整体推理性能。
3. 实验表明，NVRAR在特定消息大小下显著降低了All-Reduce延迟，并最终提升了LLM推理的端到端性能。

## 📝 摘要（中文）

随着大型语言模型（LLM）规模的持续增长，分布式推理变得越来越重要。模型并行策略现在不仅需要有效地跨多个GPU扩展，还需要跨多个节点扩展。本文对基于GPU的超级计算机上使用LLM进行多节点分布式推理进行了详细的性能研究。我们使用几种最先进的推理引擎以及YALIS（一个面向研究的原型引擎，专为受控实验而设计）进行了实验。我们分析了不同模型并行方案的强扩展行为，并确定了关键瓶颈。由于all-reduce操作是一个常见的性能瓶颈，我们开发了NVRAR，这是一种基于递归倍增和NVSHMEM的分层all-reduce算法。在HPE Slingshot和InfiniBand互连上，对于128 KB到2 MB之间的消息大小，NVRAR实现了比NCCL低1.9倍-3.6倍的延迟。集成到YALIS后，对于使用张量并行的多节点解码密集型工作负载中的Llama 3.1 405B模型，NVRAR实现了高达1.72倍的端到端批处理延迟降低。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在多节点分布式推理中遇到的性能瓶颈问题。现有的模型并行策略在跨多个GPU和节点扩展时，由于通信开销，特别是All-Reduce操作的延迟，导致整体推理效率降低。现有的All-Reduce实现，如NCCL，在某些互连网络和消息大小下可能不是最优的。

**核心思路**：论文的核心思路是优化All-Reduce通信，通过设计一种新的分层All-Reduce算法NVRAR，利用NVSHMEM提供的低延迟通信能力，减少节点间的通信开销。NVRAR基于递归倍增的思想，并针对GPU集群的特性进行了优化，从而降低了All-Reduce操作的延迟。

**技术框架**：整体框架包括：1）使用模型并行策略（如张量并行）将LLM模型分布到多个GPU和节点上；2）在推理过程中，需要进行All-Reduce操作来同步各个GPU上的计算结果；3）使用NVRAR算法替换传统的All-Reduce实现，以降低通信延迟；4）通过YALIS引擎进行实验和性能评估。YALIS作为一个研究平台，允许对不同的All-Reduce算法进行灵活的集成和测试。

**关键创新**：论文的关键创新在于提出了NVRAR算法，这是一种基于递归倍增和NVSHMEM的分层All-Reduce算法。与传统的All-Reduce实现（如NCCL）相比，NVRAR能够更好地利用NVSHMEM提供的低延迟通信能力，从而降低All-Reduce操作的延迟。分层结构允许在节点内和节点间使用不同的通信策略，进一步优化性能。

**关键设计**：NVRAR算法的关键设计包括：1）使用递归倍增的方式进行All-Reduce操作，减少通信轮数；2）利用NVSHMEM提供的共享内存通信能力，在节点内进行高效的All-Reduce操作；3）针对不同的消息大小和互连网络，优化通信策略；4）将NVRAR集成到YALIS引擎中，方便进行实验和性能评估。论文中没有明确提及具体的参数设置或损失函数，因为重点在于All-Reduce算法的优化，而不是模型训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.09557/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.09557/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.09557/x7.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，NVRAR算法在HPE Slingshot和InfiniBand互连网络上，对于128 KB到2 MB之间的消息大小，实现了比NCCL低1.9倍-3.6倍的延迟。集成到YALIS后，对于Llama 3.1 405B模型，在多节点解码密集型工作负载中，NVRAR实现了高达1.72倍的端到端批处理延迟降低。

## 🎯 应用场景

该研究成果可应用于大规模分布式LLM推理服务，例如在线对话机器人、文本生成、机器翻译等。通过降低推理延迟，可以提升用户体验，并降低部署成本。未来，该技术可以推广到其他需要高性能All-Reduce通信的分布式计算场景，例如科学计算、金融建模等。

## 📄 摘要（原文）

> As large language models (LLMs) continue to grow in size, distributed inference has become increasingly important. Model-parallel strategies must now efficiently scale not only across multiple GPUs but also across multiple nodes. In this work, we present a detailed performance study of multi-node distributed inference using LLMs on GPU-based supercomputers. We conduct experiments with several state-of-the-art inference engines alongside YALIS, a research-oriented prototype engine designed for controlled experimentation. We analyze the strong-scaling behavior of different model-parallel schemes and identify key bottlenecks. Since all-reduce operations are a common performance bottleneck, we develop NVRAR, a hierarchical all-reduce algorithm based on recursive doubling with NVSHMEM. NVRAR achieves up to 1.9x-3.6x lower latency than NCCL for message sizes between 128 KB and 2 MB on HPE Slingshot and InfiniBand interconnects. Integrated into YALIS, NVRAR achieves up to a 1.72x reduction in end-to-end batch latency for the Llama 3.1 405B model in multi-node decode-heavy workloads using tensor parallelism.

