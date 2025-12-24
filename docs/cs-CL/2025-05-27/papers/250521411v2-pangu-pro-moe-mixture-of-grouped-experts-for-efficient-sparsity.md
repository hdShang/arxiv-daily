---
layout: default
title: Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity
---

# Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21411" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21411v2</a>
  <a href="https://arxiv.org/pdf/2505.21411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21411v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21411v2', 'Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yehui Tang, Xiaosong Li, Fangcheng Liu, Wei Guo, Hang Zhou, Yaoyuan Wang, Kai Han, Xianzhi Yu, Jinpeng Li, Hui Zang, Fei Mi, Xiaojun Meng, Zhicheng Liu, Hanting Chen, Binfan Zheng, Can Chen, Youliang Yan, Ruiming Tang, Peifeng Qin, Xinghao Chen, Dacheng Tao, Yunhe Wang

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-05-28)

---

## 💡 一句话要点

**提出混合分组专家模型以解决专家负载不均问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `分组专家` `负载均衡` `Ascend NPU` `大规模语言模型` `推理性能` `计算效率`

## 📋 核心要点

1. 现有的混合专家模型在专家激活时存在负载不均的问题，导致系统效率低下。
2. 本文提出混合分组专家（MoGE），通过分组选择专家，确保每组专家的激活数量均衡，从而优化计算负载。
3. 实验结果表明，Pangu Pro MoE在Ascend NPUs上推理性能显著提升，达到每卡1148个token/s，超越同类模型。

## 📝 摘要（中文）

混合专家模型（MoE）在大规模语言模型中的应用，能够以较低的执行成本实现更大的模型参数和学习能力。然而，现有方法中某些专家被频繁激活，导致系统效率低下。为此，本文提出了混合分组专家（MoGE），通过在选择过程中对专家进行分组，平衡专家的工作负载。该设计确保在多设备分布式执行时，计算负载均衡，从而显著提升推理阶段的吞吐量。基于MoGE构建的Pangu Pro MoE在Ascend NPUs上表现出色，推理性能达到每卡1148个token/s，并可通过推测加速提升至1528个token/s，超越同类密集模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有混合专家模型中专家激活不均导致的系统效率低下问题。现有方法中，某些专家被频繁激活，而其他专家则很少被使用，造成资源浪费和计算负载不均。

**核心思路**：提出混合分组专家（MoGE），通过将专家分组并在选择时限制每组激活的专家数量，从而实现更均衡的负载分配。这样的设计能够在多设备环境中优化计算资源的使用，提高整体性能。

**技术框架**：Pangu Pro MoE的整体架构基于MoGE，包含多个专家组，每组内的专家在处理输入token时被均匀激活。该模型在Ascend NPUs上进行优化，确保在推理和训练阶段均能高效执行。

**关键创新**：最重要的创新在于引入了专家分组机制，使得在多设备并行处理时，能够有效平衡各设备的计算负载。这一设计与传统的MoE方法相比，显著提升了系统的执行效率。

**关键设计**：在模型配置上，Pangu Pro MoE总参数量为720亿，其中每个token激活160亿参数。通过对Ascend 300I Duo和800I A2进行系统模拟，优化了模型的执行性能。

## 📊 实验亮点

实验结果显示，Pangu Pro MoE在Ascend NPUs上的推理性能达到每卡1148个token/s，经过推测加速可提升至1528个token/s，显著优于同类32B和72B密集模型，展现出卓越的性价比。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提高模型的推理效率，Pangu Pro MoE能够在实际应用中提供更快的响应时间和更高的处理能力，具有广泛的商业价值和社会影响。

## 📄 摘要（原文）

> The surgence of Mixture of Experts (MoE) in Large Language Models promises a small price of execution cost for a much larger model parameter count and learning capacity, because only a small fraction of parameters are activated for each input token. However, it is commonly observed that some experts are activated far more often than others, leading to system inefficiency when running the experts on different devices in parallel. Therefore, we introduce Mixture of Grouped Experts (MoGE), which groups the experts during selection and balances the expert workload better than MoE in nature. It constrains tokens to activate an equal number of experts within each predefined expert group. When a model execution is distributed on multiple devices, this architectural design ensures a balanced computational load across devices, significantly enhancing throughput, particularly for the inference phase. Further, we build Pangu Pro MoE on Ascend NPUs, a sparse model based on MoGE with 72 billion total parameters, 16 billion of which are activated for each token. The configuration of Pangu Pro MoE is optimized for Ascend 300I Duo and 800I A2 through extensive system simulation studies. Our experiments indicate that MoGE indeed leads to better expert load balancing and more efficient execution for both model training and inference on Ascend NPUs. The inference performance of Pangu Pro MoE achieves 1148 tokens/s per card and can be further improved to 1528 tokens/s per card by speculative acceleration, outperforming comparable 32B and 72B Dense models. Furthermore, we achieve an excellent cost-to-performance ratio for model inference on Ascend 300I Duo. Our studies show that Ascend NPUs are capable of training Pangu Pro MoE with massive parallelization to make it a leading model within the sub-100B total parameter class, outperforming prominent open-source models like GLM-Z1-32B and Qwen3-32B.

