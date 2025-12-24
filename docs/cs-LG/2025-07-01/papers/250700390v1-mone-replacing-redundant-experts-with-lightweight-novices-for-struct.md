---
layout: default
title: "MoNE: Replacing Redundant Experts with Lightweight Novices for Structured Pruning of MoE"
---

# MoNE: Replacing Redundant Experts with Lightweight Novices for Structured Pruning of MoE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00390" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00390v1</a>
  <a href="https://arxiv.org/pdf/2507.00390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00390v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00390v1', 'MoNE: Replacing Redundant Experts with Lightweight Novices for Structured Pruning of MoE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Geng Zhang, Yuxuan Han, Yuxuan Lou, Wangbo Zhao, Yiqi Zhang, Yang You

**分类**: cs.LG

**发布日期**: 2025-07-01

**🔗 代码/项目**: [GITHUB](https://github.com/zxgx/mode-pd)

---

## 💡 一句话要点

**提出MoNE以解决MoE模型冗余专家带来的内存开销问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `模型压缩` `结构化剪枝` `轻量级模型` `深度学习`

## 📋 核心要点

1. 现有的MoE模型在部署时由于需要保留所有专家，导致显著的内存开销，且结构化剪枝方法在性能上存在不稳定性。
2. 本文提出MoNE方法，通过用轻量级新手替换冗余专家，基于访问频率和输出方差评估专家的冗余性，从而实现有效的模型压缩。
3. 实验结果显示，在25%剪枝率下，MoNE在九个下游任务上的平均零-shot准确率提高了2.71，在50%剪枝率下提高了3.61，验证了其优越性。

## 📝 摘要（中文）

混合专家模型（MoE）通过对每个输入令牌激活部分专家，实现了大规模语言模型的高效扩展。然而，MoE模型的部署会因需要保留所有专家而导致显著的内存开销。尽管结构化剪枝有望降低内存成本，但现有方法在模型架构、校准数据源和校准样本大小等三个维度上表现不佳且不稳定。本文提出了一种新颖的专家剪枝方法——混合新手与专家（MoNE），通过用轻量级新手替换冗余专家，实现有效且稳健的模型压缩。MoNE基于访问频率和输出方差两个指标评估专家冗余，修剪低使用率且输出稳定的专家，并用轻量级新手替代，最大限度地减少性能下降。大量实验表明，MoNE在三个维度上均优于基线方法，且准确率下降最小，确认了其有效性和稳健性。

## 🔬 方法详解

**问题定义**：本文旨在解决混合专家模型（MoE）在部署时的内存开销问题，现有的结构化剪枝方法在模型架构、校准数据源和样本大小等方面表现不佳，导致性能不稳定。

**核心思路**：提出混合新手与专家（MoNE）方法，通过评估专家的访问频率和输出方差，识别并修剪冗余专家，用轻量级新手替代，以减少内存占用并保持模型性能。

**技术框架**：MoNE的整体架构包括三个主要模块：冗余专家评估模块、轻量级新手生成模块和模型压缩模块。首先评估专家的冗余性，然后生成新手并替换冗余专家，最后进行模型的整体压缩与优化。

**关键创新**：MoNE的主要创新在于通过引入轻量级新手替代冗余专家，解决了传统剪枝方法在性能下降方面的不足，确保了模型压缩的有效性和稳健性。

**关键设计**：在参数设置上，MoNE通过设定访问频率和输出方差的阈值来识别冗余专家，损失函数设计上确保了新手输出与原专家输出的一致性，网络结构上采用轻量级模型以降低计算复杂度。

## 📊 实验亮点

实验结果表明，MoNE在九个下游任务上，平均零-shot准确率在25%剪枝率下提高了2.71，在50%剪枝率下提高了3.61，且在三个维度上均优于基线方法，验证了其有效性和稳健性。

## 🎯 应用场景

该研究的潜在应用领域包括大规模语言模型的部署和优化，尤其是在资源受限的环境中，如移动设备和边缘计算。通过有效的模型压缩，MoNE能够在保证性能的同时显著降低内存开销，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) enables efficient scaling of large language models by activating only a subset of experts per input token. However, deploying MoE-based models incurs significant memory overhead due to the need to retain all experts in memory. While structured pruning is promising to reduce memory costs, existing methods often show suboptimal performance and unstable degradation in three dimensions: model architectures, calibration data sources, and calibration sample sizes. This paper proposes Mixture-of-Novices-and-Experts (MoNE), a novel expert pruning method that replaces redundant experts with lightweight novices to achieve effective and robust model compression. MoNE evaluates expert redundancy based on two metrics: access frequency and output variance. Experts exhibiting low usage and stable outputs are pruned and replaced with lightweight novices-unbiased estimations of their original outputs-minimizing performance degradation. Extensive experiments demonstrate that MoNE consistently outperforms baseline methods with minimal accuracy degradation across the three dimensions, confirming its effectiveness and robustness. Notably, it improves the average zero shot accuracy across nine downstream tasks by up to 2.71 under 25\% pruning ratio and 3.61 under 50\% pruning. The code is available at https://github.com/zxgx/mode-pd.

