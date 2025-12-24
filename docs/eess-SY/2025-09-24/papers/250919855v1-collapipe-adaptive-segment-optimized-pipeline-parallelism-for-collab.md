---
layout: default
title: "CollaPipe: Adaptive Segment-Optimized Pipeline Parallelism for Collaborative LLM Training in Heterogeneous Edge Networks"
---

# CollaPipe: Adaptive Segment-Optimized Pipeline Parallelism for Collaborative LLM Training in Heterogeneous Edge Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19855" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19855v1</a>
  <a href="https://arxiv.org/pdf/2509.19855.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19855v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19855v1', 'CollaPipe: Adaptive Segment-Optimized Pipeline Parallelism for Collaborative LLM Training in Heterogeneous Edge Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiewei Chen, Xiumei Deng, Zehui Xiong, Shaoyong Guo, Xuesong Qiu, Ping Wang, Dusit Niyato

**分类**: eess.SY, cs.AI, cs.NI

**发布日期**: 2025-09-24

**备注**: Submitted to IEEE for review

---

## 💡 一句话要点

**CollaPipe：异构边缘网络中面向协同LLM训练的自适应分段优化流水线并行**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `边缘计算` `联邦学习` `流水线并行` `大语言模型` `异构网络` `模型训练` `资源分配`

## 📋 核心要点

1. 现有方法难以在异构边缘网络中高效训练大型语言模型，面临计算量大、延迟高和泛化性不足等挑战。
2. CollaPipe通过协同流水线并行和联邦聚合，自适应地分割模型并在边缘设备上进行分布式训练，从而优化资源利用。
3. 实验结果表明，CollaPipe显著提升了计算效率（15.09%），降低了端到端延迟（48.98%），并减少了设备内存占用。

## 📝 摘要（中文）

为了满足智能移动应用日益增长的需求，基于Transformer的大语言模型(LLM)的多智能体协作在移动边缘计算(MEC)网络中至关重要。然而，在此类环境中训练LLM仍然具有挑战性，因为计算量大、端到端延迟高且模型泛化能力有限。我们提出了CollaPipe，一个混合分布式学习框架，它集成了协同流水线并行和联邦聚合，以支持自进化的智能网络。在CollaPipe中，编码器部分被自适应地划分为可变大小的段，并部署在移动设备上进行流水线并行训练，而解码器则部署在边缘服务器上以处理生成任务。然后，我们通过联邦聚合执行全局模型更新。为了提高训练效率，我们制定了一个联合优化问题，自适应地分配模型段、微批次、带宽和传输功率。我们推导并使用一个闭式收敛界来设计一个基于Lyapunov优化的动态分段调度和资源分配(DSSDA)算法，确保系统在长期约束下的稳定性。对Transformer和BERT模型进行的下游任务的大量实验表明，CollaPipe将计算效率提高了高达15.09%，将端到端延迟降低了至少48.98%，并将单个设备的内存使用量减少了一半以上，从而能够在异构和动态通信环境中进行在线学习。

## 🔬 方法详解

**问题定义**：论文旨在解决在异构边缘网络中训练大型语言模型（LLM）时面临的计算资源受限、通信延迟高以及模型泛化能力不足的问题。现有方法，如传统的联邦学习，难以有效利用边缘设备的异构计算能力，并且容易受到通信瓶颈的影响，导致训练效率低下。

**核心思路**：CollaPipe的核心思路是将LLM的编码器部分进行分段，并在不同的边缘设备上进行流水线并行训练，同时将解码器部署在边缘服务器上。通过这种方式，可以充分利用边缘设备的计算资源，减少单个设备的计算负担，并降低端到端延迟。此外，采用联邦聚合进行全局模型更新，以提高模型的泛化能力。

**技术框架**：CollaPipe框架主要包含以下几个模块：1) 模型分段模块：将LLM的编码器部分自适应地划分为可变大小的段。2) 边缘设备部署模块：将不同的模型段部署到不同的边缘设备上进行流水线并行训练。3) 边缘服务器部署模块：将解码器部署在边缘服务器上，负责生成任务。4) 联邦聚合模块：通过联邦聚合算法，将边缘设备上的模型更新聚合到全局模型中。5) 资源分配模块：自适应地分配模型段、微批次、带宽和传输功率。

**关键创新**：CollaPipe的关键创新在于：1) 提出了协同流水线并行与联邦聚合相结合的混合分布式学习框架，充分利用边缘设备的异构计算能力。2) 设计了动态分段调度和资源分配（DSSDA）算法，基于Lyapunov优化，确保系统在长期约束下的稳定性。3) 提出了自适应的模型分段策略，根据边缘设备的计算能力和通信状况，动态调整模型段的大小。

**关键设计**：论文的关键设计包括：1) 使用闭式收敛界来指导DSSDA算法的设计，确保算法的收敛性。2) 采用Lyapunov优化来解决联合优化问题，实现模型段、微批次、带宽和传输功率的自适应分配。3) 设计了损失函数，用于优化模型分段策略，平衡计算负载和通信开销。

## 📊 实验亮点

实验结果表明，CollaPipe在Transformer和BERT模型上，相比于传统方法，计算效率提高了高达15.09%，端到端延迟降低了至少48.98%，并且单个设备的内存使用量减少了一半以上。这些结果验证了CollaPipe在异构边缘网络中进行LLM训练的有效性。

## 🎯 应用场景

CollaPipe适用于需要大规模语言模型支持的智能移动应用，例如智能助手、机器翻译、情感分析等。该研究成果可以有效降低模型训练的成本和延迟，提高模型的泛化能力，从而推动边缘计算在人工智能领域的应用，并为未来的智能网络发展提供技术支持。

## 📄 摘要（原文）

> The increasing demand for intelligent mobile applications has made multi-agent collaboration with Transformer-based large language models (LLMs) essential in mobile edge computing (MEC) networks. However, training LLMs in such environments remains challenging due to heavy computation, high end-to-end latency, and limited model generalization. We introduce CollaPipe, a hybrid distributed learning framework that integrates collaborative pipeline parallelism with federated aggregation to support self-evolving intelligent networks. In CollaPipe, the encoder part is adaptively partitioned into variable-sized segments and deployed across mobile devices for pipeline-parallel training, while the decoder is deployed on edge servers to handle generative tasks. Then we perform global model update via federated aggregation. To enhance training efficiency, we formulate a joint optimization problem that adaptively allocates model segments, micro-batches, bandwidth, and transmission power. We derive and use a closed-form convergence bound to design an Dynamic Segment Scheduling and Resource Allocation (DSSDA) algorithm based on Lyapunov optimization, ensuring system stability under long-term constraints. Extensive experiments on downstream tasks with Transformer and BERT models show that CollaPipe improves computation efficiency by up to 15.09%, reduces end-to-end latency by at least 48.98%, and cuts single device memory usage by more than half, enabling online learning in heterogeneous and dynamic communication environments.

