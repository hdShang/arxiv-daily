---
layout: default
title: "HierMoE: Accelerating MoE Training with Hierarchical Token Deduplication and Expert Swap"
---

# HierMoE: Accelerating MoE Training with Hierarchical Token Deduplication and Expert Swap

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09591" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09591v1</a>
  <a href="https://arxiv.org/pdf/2508.09591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09591v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09591v1', 'HierMoE: Accelerating MoE Training with Hierarchical Token Deduplication and Expert Swap')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxiang Lin, Xinglin Pan, Lin Zhang, Shaohuai Shi, Xuan Wang, Xiaowen Chu

**分类**: cs.DC, cs.LG

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出HierMoE以解决MoE模型训练中的通信与负载不均问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `专家混合模型` `稀疏激活` `分布式训练` `GPU负载均衡` `通信优化`

## 📋 核心要点

1. 现有MoE模型在动态激活专家时，导致GPU间通信和负载不均，影响训练效率。
2. 本文提出HierMoE，通过令牌去重和专家交换技术，优化MoE模型的训练过程。
3. 实验结果显示，HierMoE在通信速度和端到端训练上均显著优于现有的MoE训练系统。

## 📝 摘要（中文）

稀疏激活的专家混合（MoE）变换器因其稀疏性而成为大型语言模型（LLMs）的常见架构，能够在较低计算需求下轻松扩展模型规模。然而，MoE模型在动态选择激活特定专家时，可能导致通信和负载不均衡，阻碍了分布式系统的可扩展性。为此，本文提出HierMoE，通过两种拓扑感知技术加速MoE模型训练：1）令牌去重以减少通信流量，2）专家交换以平衡GPU间的工作负载。我们在不同模型配置和硬件环境下建立理论模型，以实现最佳的令牌去重和专家交换策略。实验结果表明，HierMoE在32-GPU集群上实现了1.55倍至3.32倍的通信加速，并且端到端训练速度提升了1.18倍至1.27倍，相较于现有的MoE训练系统表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决MoE模型训练中由于动态激活专家导致的通信负担和负载不均的问题。现有方法在GPU集群中面临显著的通信延迟和负载不平衡，影响训练效率。

**核心思路**：HierMoE的核心思路是通过令牌去重和专家交换来减少通信流量和均衡GPU负载。这种设计旨在提高MoE模型的训练效率，尤其是在大规模分布式环境中。

**技术框架**：HierMoE系统基于Megatron-LM构建，主要包括两个模块：令牌去重模块负责减少重复令牌的通信，专家交换模块则在不同GPU间动态调整负载。

**关键创新**：本文的主要创新在于提出了拓扑感知的令牌去重和专家交换策略，这与现有方法的静态负载分配和简单通信策略有本质区别。

**关键设计**：在实现中，HierMoE对令牌的去重策略和专家的交换策略进行了理论建模，以适应不同的模型配置和硬件环境，确保在各种条件下的最佳性能。具体的参数设置和损失函数设计也经过精心调整，以优化训练效果。

## 📊 实验亮点

实验结果表明，HierMoE在32-GPU集群上实现了1.55倍至3.32倍的通信加速，端到端训练速度提升了1.18倍至1.27倍，显著优于现有的MoE训练系统，如Tutel-2DH、SmartMoE和Megatron-LM，展示了其在性能上的显著提升。

## 🎯 应用场景

HierMoE的研究成果可广泛应用于大型语言模型的训练，尤其是在需要高效分布式计算的场景中，如自然语言处理、机器翻译和对话系统等领域。其优化的训练效率将推动更大规模模型的开发与应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The sparsely activated mixture-of-experts (MoE) transformer has become a common architecture for large language models (LLMs) due to its sparsity, which requires fewer computational demands while easily scaling the model size. In MoE models, each MoE layer requires to dynamically choose tokens to activate particular experts for computation while the activated experts may not be located in the same device or GPU as the token. However, this leads to substantial communication and load imbalances across all GPUs, which obstructs the scalability of distributed systems within a GPU cluster. To this end, we introduce HierMoE to accelerate the training of MoE models by two topology-aware techniques: 1) token deduplication to reduce the communication traffic, and 2) expert swap to balance the workloads among all GPUs. To enable the above two proposed approaches to be more general, we build theoretical models aimed at achieving the best token duplication and expert swap strategy under different model configurations and hardware environments. We implement our prototype HierMoE system atop Megatron-LM and conduct experiments on a 32-GPU cluster with DeepSeek-V3 and Qwen3-30B-A3B models. Experimental results show that our HierMoE achieves $1.55\times$ to $3.32\times$ faster communication and delivers $1.18\times$ to $1.27\times$ faster end-to-end training compared to state-of-the-art MoE training systems, Tutel-2DH, SmartMoE, and Megatron-LM.

