---
layout: default
title: "GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling"
---

# GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22049" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22049v2</a>
  <a href="https://arxiv.org/pdf/2506.22049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22049v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22049v2', 'GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianhao Chen, Xin Xu, Zijing Liu, Pengxiang Li, Xinyuan Song, Ajay Kumar Jaiswal, Fan Zhang, Jishan Hu, Yang Wang, Hao Chen, Shizhe Diao, Shiwei Liu, Yu Li, Lu Yin, Can Yang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-27 (更新: 2025-07-03)

**🔗 代码/项目**: [GITHUB](https://github.com/dandingsky/GPAS)

---

## 💡 一句话要点

**提出GPAS以解决大语言模型预训练中的激活方差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `预训练` `激活方差` `梯度保持` `深度学习` `Transformer` `模型优化`

## 📋 核心要点

1. 现有的预层归一化Transformer在预训练过程中激活方差呈指数增长，限制了深层学习能力。
2. GPAS通过缩小中间激活值而保持其梯度不变，解决了激活方差问题，避免了梯度消失。
3. 在71M到1B的模型规模上，GPAS均取得了显著的性能提升，并适用于多种架构。

## 📝 摘要（中文）

现代大语言模型，如LLaMA、Qwen和DeepSeek系列，主要采用预层归一化（Pre-LN）Transformer架构。尽管Pre-LN在预训练过程中稳定且可扩展至大模型，但其激活方差在层间呈指数增长，导致快捷连接主导子层输出，从而限制了深层的学习能力。为此，本文提出了一种简单的技术——梯度保持激活缩放（GPAS），通过缩小中间激活值而保持其梯度不变，避免了梯度消失问题。大量实验表明，GPAS在71M到1B的不同模型规模上均取得了显著的性能提升，且在其他架构如Sandwich-LN和DeepNorm中也展现了良好的适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型预训练中激活方差的指数增长问题，现有的预层归一化Transformer架构在此方面表现不佳，导致深层的学习能力受限。

**核心思路**：GPAS的核心思路是通过缩小中间激活值，同时保持其梯度不变，从而避免激活信息的丢失和梯度消失的问题。这种设计使得模型在训练过程中能够更好地保持信息流动。

**技术框架**：GPAS的整体架构包括激活缩放模块，该模块在每一层的前向传播中应用，具体流程为：计算中间激活值，进行缩放处理，然后传递至后续层，同时保持梯度的原始状态。

**关键创新**：GPAS的主要创新在于其梯度保持机制，这与传统的激活缩放方法有本质区别，后者通常会导致梯度消失，从而影响模型的学习能力。

**关键设计**：在实现GPAS时，关键参数包括激活缩放比例的选择，以及如何在不同模型规模下调整该比例以获得最佳效果。此外，损失函数和网络结构的设计也需与GPAS相适应，以确保其在训练过程中的有效性。

## 📊 实验亮点

实验结果显示，GPAS在不同规模的模型（从71M到1B）上均实现了性能提升，尤其在深层网络中表现尤为突出。与基线模型相比，GPAS在训练稳定性和收敛速度上均有显著改善，证明了其在多种架构中的有效性和适用性。

## 🎯 应用场景

GPAS的研究成果具有广泛的应用潜力，尤其是在大语言模型的预训练和微调阶段。通过改善激活方差问题，GPAS能够提升模型的学习能力，进而在自然语言处理、对话系统和文本生成等领域发挥重要作用。未来，GPAS也可能被应用于其他深度学习模型的训练优化中，推动更高效的模型开发。

## 📄 摘要（原文）

> Modern Large Language Models, such as the LLaMA, Qwen and DeepSeek series, predominantly adopt the Pre-LayerNorm (Pre-LN) Transformer architecture. While being stable during pretraining and scalable to large model sizes, Pre-LN suffers from an exponential growth in activation variance across layers, causing the shortcut to dominate over sub-layer outputs in the residual connection and limiting the learning capacity of deeper layers. To mitigate this issue, we propose Gradient-Preserving Activation Scaling (GPAS), a simple technique that can be used in combination with existing approaches. GPAS works by scaling down the intermediate activations while keeping their gradients unchanged. This leaves information in the activations intact, and avoids the gradient vanishing problem associated with gradient downscaling. Extensive experiments across various model sizes from 71M to 1B show that GPAS achieves consistent performance gains. Beyond enhancing Pre-LN Transformers, GPAS also shows promise in improving alternative architectures such as Sandwich-LN and DeepNorm, demonstrating its versatility and potential for improving training dynamics in a wide range of settings. Our code is available at https://github.com/dandingsky/GPAS.

