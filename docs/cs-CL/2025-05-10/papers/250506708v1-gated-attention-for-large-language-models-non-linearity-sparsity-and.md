---
layout: default
title: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
---

# Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06708" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06708v1</a>
  <a href="https://arxiv.org/pdf/2505.06708.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06708v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06708v1', 'Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin

**分类**: cs.CL

**发布日期**: 2025-05-10

**🔗 代码/项目**: [GITHUB](https://github.com/qiuzh20/gated_attention) | [HUGGINGFACE](https://huggingface.co/QwQZh/gated_attention)

---

## 💡 一句话要点

**提出门控注意力机制以提升大语言模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `门控机制` `大语言模型` `注意力机制` `长上下文` `性能提升` `稀疏性` `非线性`

## 📋 核心要点

1. 现有的门控机制在大语言模型中的具体效果尚未得到充分研究，导致性能提升的潜力未被完全挖掘。
2. 本文提出在缩放点积注意力后应用头特定的sigmoid门控，以引入非线性和稀疏性，从而提升模型性能和稳定性。
3. 实验结果表明，门控机制显著改善了模型的训练稳定性和扩展性，尤其在长上下文处理上表现优异。

## 📝 摘要（中文）

门控机制在早期模型（如LSTM和高速公路网络）及近期的状态空间模型、线性注意力和softmax注意力中得到了广泛应用。然而，现有文献很少探讨门控的具体效果。本文通过对30种15B混合专家（MoE）模型和1.7B稠密模型进行全面比较，系统研究了增强softmax注意力的门控变体。研究发现，在缩放点积注意力（SDPA）后应用特定头的sigmoid门控可以持续提升性能，同时增强训练稳定性，容忍更大的学习率，并改善扩展性。通过比较不同的门控位置和计算变体，归因于引入非线性和查询依赖的稀疏门控分数的调制效果。值得注意的是，稀疏门控机制减轻了“注意力沉没”现象，并提升了长上下文外推性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大语言模型中门控机制应用不足的问题，尤其是如何有效利用门控提升模型性能和稳定性。现有方法在处理长上下文时容易出现“注意力沉没”现象，影响模型的表现。

**核心思路**：论文提出在缩放点积注意力（SDPA）后引入头特定的sigmoid门控，通过非线性映射和稀疏门控分数来调节输出，从而提升模型的性能和训练稳定性。

**技术框架**：整体架构包括对15B混合专家模型和1.7B稠密模型的比较实验，采用3.5万亿标记的数据集进行训练，重点分析不同门控位置和计算变体的效果。

**关键创新**：最重要的技术创新在于引入了门控机制，尤其是通过稀疏门控分数来调节SDPA输出，这一设计有效缓解了注意力沉没问题，并提升了模型在长上下文的外推能力。

**关键设计**：在模型设计中，采用了sigmoid门控作为非线性激活函数，设置了不同的门控位置，并进行了大量实验以优化参数设置和损失函数，确保模型在训练过程中的稳定性和扩展性。

## 📊 实验亮点

实验结果显示，应用门控机制后，模型在长上下文处理上的性能显著提升，尤其在与基线模型的对比中，性能提升幅度达到X%（具体数据未知），并且训练稳定性得到了有效改善。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理、对话系统和文本生成等领域。通过提升大语言模型的性能和稳定性，能够更好地处理复杂的语言任务，推动智能助手和自动化内容生成的进步，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Gating mechanisms have been widely utilized, from early models like LSTMs and Highway Networks to recent state space models, linear attention, and also softmax attention. Yet, existing literature rarely examines the specific effects of gating. In this work, we conduct comprehensive experiments to systematically investigate gating-augmented softmax attention variants. Specifically, we perform a comprehensive comparison over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5 trillion token dataset. Our central finding is that a simple modification-applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)-consistently improves performance. This modification also enhances training stability, tolerates larger learning rates, and improves scaling properties. By comparing various gating positions and computational variants, we attribute this effectiveness to two key factors: (1) introducing non-linearity upon the low-rank mapping in the softmax attention, and (2) applying query-dependent sparse gating scores to modulate the SDPA output. Notably, we find this sparse gating mechanism mitigates 'attention sink' and enhances long-context extrapolation performance, and we also release related $\href{https://github.com/qiuzh20/gated_attention}{codes}$ and $\href{https://huggingface.co/QwQZh/gated_attention}{models}$ to facilitate future research.

