---
layout: default
title: "SlimPack: Fine-Grained Asymmetric Packing for Balanced and Efficient Variable-Length LLM Training"
---

# SlimPack: Fine-Grained Asymmetric Packing for Balanced and Efficient Variable-Length LLM Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26246" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26246v1</a>
  <a href="https://arxiv.org/pdf/2509.26246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26246v1', 'SlimPack: Fine-Grained Asymmetric Packing for Balanced and Efficient Variable-Length LLM Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuliang Liu, Guohao Wu, Shenglong Zhang, Wei Zhang, Qianchao Zhu, Zhouyang Li, Chenyu Wang

**分类**: cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**SlimPack：面向变长LLM训练的细粒度非对称数据打包，提升平衡性和效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `分布式训练` `数据打包` `负载均衡` `非对称计算` `细粒度切片` `训练效率`

## 📋 核心要点

1. 现有LLM训练方法在处理变长上下文时，由于数据异构性和非对称计算成本，导致负载不均衡和硬件利用率低。
2. SlimPack将样本分解为细粒度切片，并采用非对称分区策略，为前向和后向传递优化平衡的调度单元。
3. 实验结果表明，SlimPack相比基线方法，训练吞吐量提升高达2.8倍，在平衡性和资源效率上均有显著优势。

## 📝 摘要（中文）

大规模语言模型（LLM）的高效分布式训练受到上下文长度极端差异的严重阻碍。这种数据异构性，被传统打包策略和非对称的前向-后向成本放大，导致了严重的低效率，例如级联式的工作负载不平衡和严重的硬件利用率不足。现有的解决方案试图缓解这些挑战，但往往以牺牲内存或通信效率为代价。为了解决这些挑战，我们引入了SlimPack，一个通过将样本分解为细粒度切片来从根本上重新思考数据打包和调度的框架。这种切片级别的分解立即缓解了关键的内存和通信瓶颈，通过将大型、易变的工作负载转换为更小、可管理的单元流。这种灵活性被用于我们的核心创新，即非对称分区，它组装了专门为前向和后向传递的不同需求而优化的平衡调度单元。在两阶段求解器和高保真模拟器的协调下，SlimPack全面解决了所有并行维度上的不平衡问题。大量的实验表明，SlimPack实现了高达2.8倍于基线的训练吞吐量提升，打破了传统的权衡，实现了卓越的平衡性和高资源效率。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模语言模型（LLM）分布式训练中，由于输入文本长度差异大（变长上下文）以及前向和后向计算量不对称，导致的训练效率低下问题。现有方法在数据打包时，无法有效平衡各个计算节点的负载，造成资源浪费和训练速度瓶颈。

**核心思路**：SlimPack的核心思路是将输入样本分解成细粒度的切片，然后根据前向和后向计算的不同需求，采用非对称分区策略，将这些切片打包成平衡的调度单元。通过这种方式，可以最大限度地减少负载不平衡，提高硬件利用率。

**技术框架**：SlimPack框架包含以下几个主要模块：1) **细粒度切片**：将输入样本分解成更小的切片，以便更灵活地进行调度。2) **非对称分区**：根据前向和后向计算的不同需求，设计不同的分区策略，以实现负载平衡。3) **两阶段求解器**：用于优化切片的打包和调度，第一阶段快速生成初始方案，第二阶段进行精细调整。4) **高保真模拟器**：用于评估不同调度方案的性能，并指导优化过程。

**关键创新**：SlimPack的关键创新在于其细粒度的非对称数据打包策略。与传统的静态或启发式打包方法不同，SlimPack能够根据前向和后向计算的实际需求，动态地调整切片的分配，从而实现更精确的负载平衡。这种方法打破了传统方法在平衡性和资源效率之间的权衡。

**关键设计**：SlimPack的关键设计包括：1) **切片大小的选择**：需要根据硬件特性和模型结构进行调整，以获得最佳性能。2) **非对称分区策略的设计**：需要考虑前向和后向计算的比例，以及不同计算节点的性能差异。3) **两阶段求解器的优化目标**：需要综合考虑负载平衡、通信开销和内存占用等因素。4) **高保真模拟器的精度**：需要尽可能准确地模拟实际训练过程，以便有效地评估不同调度方案的性能。

## 📊 实验亮点

SlimPack在实验中表现出色，相较于基线方法，训练吞吐量提升高达2.8倍。实验结果表明，SlimPack能够有效地平衡各个计算节点的负载，显著提高硬件利用率，并在平衡性和资源效率之间取得了突破性的进展。该方法在不同规模的模型和数据集上均表现出良好的性能。

## 🎯 应用场景

SlimPack适用于大规模语言模型的分布式训练，尤其是在处理变长文本数据时。它可以显著提高训练效率，降低训练成本，并加速LLM的迭代和部署。该技术还可以推广到其他具有类似数据异构性和计算非对称性的机器学习任务中，例如语音识别、机器翻译等。

## 📄 摘要（原文）

> The efficient distributed training of Large Language Models (LLMs) is severely hampered by the extreme variance in context lengths. This data heterogeneity, amplified by conventional packing strategies and asymmetric forward-backward costs, leads to critical inefficiencies such as cascading workload imbalances and severe hardware underutilization. Existing solutions attempt to mitigate these challenges, but often at the expense of memory or communication efficiency.
>   To address these challenges, we introduce SlimPack, a framework that fundamentally rethinks data packing and scheduling by decomposing samples into fine-grained slices. This slice-level decomposition immediately mitigates critical memory and communication bottlenecks by transforming large, volatile workloads into a stream of smaller, manageable units. This flexibility is then harnessed for our core innovation, Asymmetric Partitioning, which assembles balanced scheduling units uniquely optimized for the different demands of the forward and backward passes. Orchestrated by a two-phase solver and a high-fidelity simulator, SlimPack holistically resolves imbalances across all parallel dimensions. Extensive experiments demonstrate that SlimPack achieves up to a $2.8\times$ training throughput improvement over baselines, breaking the conventional trade-off by delivering both superior balance and high resource efficiency.

