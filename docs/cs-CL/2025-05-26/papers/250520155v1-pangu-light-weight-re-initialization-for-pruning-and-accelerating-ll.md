---
layout: default
title: "Pangu Light: Weight Re-Initialization for Pruning and Accelerating LLMs"
---

# Pangu Light: Weight Re-Initialization for Pruning and Accelerating LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20155" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20155v1</a>
  <a href="https://arxiv.org/pdf/2505.20155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20155v1', 'Pangu Light: Weight Re-Initialization for Pruning and Accelerating LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanting Chen, Jiarui Qin, Jialong Guo, Tao Yuan, Yichun Yin, Huiling Zhen, Yasheng Wang, Jinpeng Li, Xiaojun Meng, Meng Zhang, Rongju Ruan, Zheyuan Bai, Yehui Tang, Can Chen, Xinghao Chen, Fisher Yu, Ruiming Tang, Yunhe Wang

**分类**: cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出Pangu Light以解决大语言模型压缩与加速问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `结构化剪枝` `权重重初始化` `模型压缩` `Ascend NPU` `性能优化` `深度学习`

## 📋 核心要点

1. 现有的结构化剪枝方法在宽度和深度的激进减少中，常导致模型性能显著下降，难以有效部署。
2. Pangu Light框架通过引入权重重初始化技术，改善了剪枝后模型的训练起点，从而提升了模型的准确性。
3. 在Ascend NPU上，Pangu Light-32B的平均得分为81.6，吞吐量为2585 tokens/s，超越了Qwen3-32B的80.9得分和2225 tokens/s吞吐量。

## 📝 摘要（中文）

大语言模型（LLMs）在众多任务中展现了卓越的能力，但其庞大的规模和推理成本为实际部署带来了显著的计算挑战。尽管结构化剪枝为模型压缩提供了有希望的途径，但现有方法在宽度和深度的激进同时减少时，常常面临性能显著下降的问题。本文提出Pangu Light框架，通过结构化剪枝和新颖的权重重初始化技术，解决了这一关键问题，显著提升了模型的训练准确性。实验结果表明，Pangu Light在Ascend NPU上表现出优越的准确性和效率，超越了现有的基线剪枝方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在进行结构化剪枝时，因宽度和深度的激进减少而导致的性能下降问题。现有方法往往忽视了剪枝后权重的重初始化，导致模型训练准确性不足。

**核心思路**：Pangu Light框架的核心思想是通过战略性地重初始化和调整剩余权重，改善剪枝后模型的训练起点，从而提升模型的性能。

**技术框架**：该框架系统性地针对模型的多个维度进行优化，包括宽度、深度、注意力头和RMSNorm，结合新颖的重初始化方法如跨层注意力剪枝（CLAP）和稳定层归一化剪枝（SLNP）。

**关键创新**：Pangu Light的主要创新在于引入了权重重初始化技术，特别是CLAP和SLNP，这些方法有效减轻了剪枝带来的性能下降，与现有方法相比，提供了更好的训练起点。

**关键设计**：在设计中，Pangu Light吸收了后RMSNorm计算，并根据Ascend NPU的特性量身定制了优化策略，确保了高效的模型推理和训练。具体的参数设置和损失函数设计未在摘要中详细说明，待进一步研究。

## 📊 实验亮点

Pangu Light在Ascend NPU上实现了81.6的平均得分和2585 tokens/s的吞吐量，显著超越了Qwen3-32B的80.9得分和2225 tokens/s吞吐量，展示了其在准确性和效率上的优越性。

## 🎯 应用场景

Pangu Light框架具有广泛的应用潜力，特别是在需要高效推理和低延迟响应的大语言模型部署场景中。其优化策略可为实际应用提供更高的准确性和效率，推动智能对话系统、自动翻译和内容生成等领域的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) deliver state-of-the-art capabilities across numerous tasks, but their immense size and inference costs pose significant computational challenges for practical deployment. While structured pruning offers a promising avenue for model compression, existing methods often struggle with the detrimental effects of aggressive, simultaneous width and depth reductions, leading to substantial performance degradation. This paper argues that a critical, often overlooked, aspect in making such aggressive joint pruning viable is the strategic re-initialization and adjustment of remaining weights to improve the model post-pruning training accuracies. We introduce Pangu Light, a framework for LLM acceleration centered around structured pruning coupled with novel weight re-initialization techniques designed to address this ``missing piece''. Our framework systematically targets multiple axes, including model width, depth, attention heads, and RMSNorm, with its effectiveness rooted in novel re-initialization methods like Cross-Layer Attention Pruning (CLAP) and Stabilized LayerNorm Pruning (SLNP) that mitigate performance drops by providing the network a better training starting point. Further enhancing efficiency, Pangu Light incorporates specialized optimizations such as absorbing Post-RMSNorm computations and tailors its strategies to Ascend NPU characteristics. The Pangu Light models consistently exhibit a superior accuracy-efficiency trade-off, outperforming prominent baseline pruning methods like Nemotron and established LLMs like Qwen3 series. For instance, on Ascend NPUs, Pangu Light-32B's 81.6 average score and 2585 tokens/s throughput exceed Qwen3-32B's 80.9 average score and 2225 tokens/s.

