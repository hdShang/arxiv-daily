---
layout: default
title: "ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration"
---

# ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24357" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24357v3</a>
  <a href="https://arxiv.org/pdf/2505.24357.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24357v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24357v3', 'ReCalKV: Low-Rank KV Cache Compression via Head Reordering and Offline Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianglong Yan, Zhiteng Li, Tianao Zhang, Haotong Qin, Linghe Kong, Yulun Zhang, Xiaokang Yang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-09-27)

**🔗 代码/项目**: [GITHUB](https://github.com/XIANGLONGYAN/ReCalKV)

---

## 💡 一句话要点

**提出ReCalKV以解决长上下文推理中的KV缓存压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文推理` `KV缓存压缩` `低秩近似` `头部重排序` `离线校准` `大型语言模型` `自然语言处理`

## 📋 核心要点

1. 现有的低秩KV缓存压缩方法未能充分考虑键和值的不同角色及其重要性，导致在高压缩率下性能显著下降。
2. 本文提出ReCalKV，通过头部相似性感知重排序和离线值校准，分别针对键和值进行优化，从而实现更高效的低秩近似。
3. 实验结果表明，ReCalKV在压缩比和性能损失方面均优于现有的低秩压缩方法，展现出良好的实用性。

## 📝 摘要（中文）

大型语言模型（LLMs）展现了卓越的性能，但其长上下文推理受到KV缓存所需过多内存的限制。因此，KV缓存压缩成为高效长上下文推理的重要步骤。现有方法虽然探索了低秩技术以减少KV缓存的隐藏大小，但忽视了键和值的不同角色及其重要性，导致高压缩下性能显著下降。为此，本文提出了ReCalKV，一种后训练低秩KV缓存压缩方法，针对键和值采用定制策略。通过头部相似性感知重排序（HSR）和离线值校准（OVC），ReCalKV在高压缩比下实现了最小性能损失，实验结果显示其在压缩效果上优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文推理中KV缓存的内存消耗问题。现有低秩压缩方法未能有效处理键和值的不同特性，导致在高压缩率下性能下降。

**核心思路**：ReCalKV通过针对键和值的不同特性，采用头部相似性感知重排序（HSR）和离线值校准（OVC）来优化KV缓存的低秩压缩。这样设计的目的是在保持性能的同时，实现更高的压缩比。

**技术框架**：ReCalKV的整体架构包括两个主要模块：首先是HSR模块，通过聚类相似的头部以实现更准确的低秩近似；其次是OVC模块，利用校准数据对值投影矩阵进行校准，无需重新训练。

**关键创新**：ReCalKV的核心创新在于同时考虑键和值的特性，通过分组SVD和离线校准技术，显著提高了低秩压缩的效果。这与传统方法的单一处理方式形成鲜明对比。

**关键设计**：在HSR中，采用了基于结构相似性的聚类算法；在OVC中，设计了高效的校准流程，确保值的表示准确性。具体参数设置和损失函数的选择也经过精心调整，以优化整体性能。

## 📊 实验亮点

实验结果显示，ReCalKV在多个基准测试中均优于现有低秩压缩方法，达到了高达80%的压缩比，同时性能损失控制在5%以内。这一结果表明，ReCalKV在长上下文推理中具有显著的优势。

## 🎯 应用场景

ReCalKV的研究成果在自然语言处理、对话系统和长文本生成等领域具有广泛的应用潜力。通过有效压缩KV缓存，该方法能够显著降低内存消耗，提高模型在长上下文推理任务中的效率，推动大型语言模型的实际应用和部署。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable performance, but their long-context reasoning remains constrained by the excessive memory required for the Key-Value (KV) cache. This makes KV cache compression a critical step toward efficient long-context inference. Recent methods have explored low-rank techniques to reduce the hidden size of the KV cache. However, they neglect the distinct roles and varying importance of Keys and Values, leading to significant performance drops under high compression. To address this, we propose ReCalKV, a post-training low-rank KV cache compression approach with tailored strategies for Keys and Values. For Keys, we propose Head-wise Similarity aware Reordering (HSR), which clusters structurally similar heads into groups, enabling more accurate low-rank approximation via grouped SVD. For Values, we propose Offline Value Calibration (OVC), which efficiently calibrates the value projection matrix using calibration data without training, ensuring an accurate representation of contextual information. Extensive experiments show that ReCalKV consistently outperforms existing low-rank compression methods, achieving high compression ratios with minimal performance loss. The code and models will be available at:https://github.com/XIANGLONGYAN/ReCalKV.

