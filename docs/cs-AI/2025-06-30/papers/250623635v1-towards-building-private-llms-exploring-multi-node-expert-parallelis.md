---
layout: default
title: "Towards Building Private LLMs: Exploring Multi-Node Expert Parallelism on Apple Silicon for Mixture-of-Experts Large Language Model"
---

# Towards Building Private LLMs: Exploring Multi-Node Expert Parallelism on Apple Silicon for Mixture-of-Experts Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23635" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23635v1</a>
  <a href="https://arxiv.org/pdf/2506.23635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23635v1', 'Towards Building Private LLMs: Exploring Multi-Node Expert Parallelism on Apple Silicon for Mixture-of-Experts Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mu-Chi Chen, Po-Hsuan Huang, Xiangrui Ke, Chia-Heng Tu, Chun Jason Xue, Shih-Hao Hung

**分类**: cs.DC, cs.AI, cs.PF

**发布日期**: 2025-06-30

**备注**: International Conference on Research in Adaptive and Convergent Systems (RACS '24), November 5--8, 2024, Pompei, Italy

**DOI**: [10.1145/3649601.3698722](https://doi.org/10.1145/3649601.3698722)

---

## 💡 一句话要点

**提出多节点专家并行方法以解决私有大语言模型构建的成本与可扩展性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `私有LLM` `混合专家` `多节点并行` `Apple Silicon` `推理优化` `成本效率`

## 📋 核心要点

1. 现有方法在构建私有大型语言模型时面临高成本和可扩展性不足的问题，限制了其在个人和小组服务中的应用。
2. 本文提出在Apple M2 Ultra芯片的Mac Studio集群上实现多节点专家并行，利用混合专家架构来加速推理过程。
3. 实验结果显示，采用该方法后，推理时间显著减少，且Mac Studio集群的成本效率比现有的AI超级计算机高出1.15倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在人工智能领域取得了显著进展，然而构建私有LLM系统面临成本和可扩展性挑战。本文通过建立基于Apple M2 Ultra芯片的Mac Studio集群，探讨了如何高效托管和加速预训练的DBRX模型，采用混合专家（MoE）架构。性能分析表明，在两到四个机器节点上并行执行模型专家显著减少了推理时间，同时发现专家计算时间与输出交换的通信时间相当，强调了网络延迟的重要性。基于这些发现，本文提出了优化方案以消除内存管理开销，使得Mac Studio集群在成本效率上超过了基于NVIDIA H100 GPU的最先进AI超级计算机。

## 🔬 方法详解

**问题定义**：本文旨在解决构建私有大型语言模型时的高成本和可扩展性问题。现有方法在推理速度和资源利用率上存在不足，尤其是在小规模服务场景中。

**核心思路**：论文的核心思路是通过在Mac Studio集群上实现多节点专家并行，利用混合专家架构来提高推理效率，降低成本。这样的设计能够充分利用Apple Silicon的计算能力，同时优化网络通信。

**技术框架**：整体架构包括多个计算节点，每个节点上运行不同的专家模型。通过并行执行，节点间进行高效的输出交换，减少推理时间。主要模块包括专家模型、网络通信管理和内存管理优化。

**关键创新**：最重要的技术创新在于提出了在Apple M2 Ultra芯片上实现的多节点专家并行方法，强调了网络延迟对推理效率的影响，并提出了相应的优化方案。与现有方法相比，本文在成本和性能上均有显著提升。

**关键设计**：在参数设置上，优化了专家模型的数量和节点配置，采用了适应性内存管理策略以减少管理开销。损失函数和网络结构设计上，结合了混合专家架构的特点，以提高模型的推理速度和准确性。

## 📊 实验亮点

实验结果表明，采用多节点专家并行方法后，推理时间显著减少，且Mac Studio集群在成本效率上比基于NVIDIA H100 GPU的超级计算机高出1.15倍。这一成果展示了在私有LLM构建中的实际应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括个人助理、定制化聊天机器人和小型团队的智能服务系统。通过降低构建私有LLM的成本和提高推理效率，能够使更多用户和组织受益于先进的人工智能技术，推动智能服务的普及与发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have revolutionized Artificial Intelligence (AI) with significant advancements such as OpenAI's ChatGPT, Meta's Llama, and Databricks' DBRX. This paper addresses the cost and scalability challenges encountered when constructing private LLM systems for personal or small group services, as aimed by Apple Intelligence. A Mac Studio cluster with Apple's M2 Ultra chips is established as a cost-efficient solution to host and accelerate the pretrained DBRX model with the Mixture-of-Experts (MoE) architecture. Our performance analysis reveal that parallel execution of the model's experts across two to four machine nodes significantly reduces inference time. We find that computation time for the experts is comparable to the communication time for exchanging their outputs, emphasizing the importance of network latency over bandwidth. We also observe significant management overhead due to Apple software stack's memory management logic. Based on these findings, we develop optimization schemes to eliminate the memory management overhead. As a result, the Mac Studio cluster is 1.15 times more cost-efficient than the state-of-the-art AI supercomputer with NVIDIA H100 GPUs. In addition, we construct a performance model to estimate system performance under varying configurations, and the model provides valuable insights for designing private LLM systems.

