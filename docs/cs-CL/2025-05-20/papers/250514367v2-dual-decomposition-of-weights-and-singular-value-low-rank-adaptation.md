---
layout: default
title: Dual Decomposition of Weights and Singular Value Low Rank Adaptation
---

# Dual Decomposition of Weights and Singular Value Low Rank Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14367" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14367v2</a>
  <a href="https://arxiv.org/pdf/2505.14367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14367v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14367v2', 'Dual Decomposition of Weights and Singular Value Low Rank Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialong Han, Si Zhang, Ke Zhang

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-21)

---

## 💡 一句话要点

**提出DuDe以解决LoRA方法的训练不稳定和知识转移效率低的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `低秩适应` `奇异值分解` `知识转移` `训练稳定性` `大型语言模型` `领域特定任务`

## 📋 核心要点

1. 现有的LoRA方法在训练过程中表现出不稳定性，并且从预训练模型中转移知识的效率较低。
2. 本文提出的DuDe方法通过将权重矩阵分解为幅度和方向分量，利用奇异值分解进行初始化，从而提高了训练的稳定性。
3. 实验结果显示，DuDe在MMLU和GSM8K任务上分别达到了48.35%和62.53%的准确率，显著优于现有方法。

## 📝 摘要（中文）

参数高效微调（PEFT）已成为适应大型语言模型（LLMs）于下游任务的重要范式，其中低秩适应（LoRA）是最广泛采用的方法之一。然而，现有的LoRA方法存在两个基本局限性：训练动态不稳定和从预训练模型中知识转移效率低，这主要源于适配器参数的随机初始化。为了解决这些挑战，本文提出了DuDe，一种新颖的方法，通过将权重矩阵分解为幅度和方向分量，并采用奇异值分解（SVD）进行原则性初始化。综合评估表明，DuDe在MMLU上达到了48.35%的准确率，在GSM8K上达到了62.53%（±1.59）的准确率。理论分析和实证验证共同表明，DuDe的分解策略增强了优化的稳定性，并更好地保留了预训练表示，尤其适用于需要专业知识的领域特定任务。DuDe的稳健实证表现和严谨理论基础使其成为PEFT方法论在LLMs领域的重要贡献。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LoRA方法在训练动态不稳定和知识转移效率低的问题，这些问题主要源于适配器参数的随机初始化。

**核心思路**：DuDe方法通过将权重矩阵分解为幅度和方向分量，采用奇异值分解（SVD）进行初始化，从而实现更稳定的训练过程和更有效的知识保留。

**技术框架**：DuDe的整体架构包括权重分解模块、SVD初始化模块和适配器训练模块。首先，通过SVD对权重进行分解，然后基于分解结果进行适配器的训练。

**关键创新**：DuDe的主要创新在于其权重分解策略，这一策略与传统的随机初始化方法本质上不同，能够显著提高优化的稳定性和知识转移的效率。

**关键设计**：在参数设置上，DuDe采用了基于SVD的初始化方法，损失函数设计上则考虑了适应性调整，以确保在训练过程中能够有效保留预训练模型的知识。具体的网络结构细节和参数设置在实验部分进行了详细描述。

## 📊 实验亮点

DuDe在MMLU任务上达到了48.35%的准确率，在GSM8K任务上达到了62.53%（±1.59）的准确率，显著优于现有LoRA方法，展示了其在训练稳定性和知识转移效率方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和领域特定的知识应用等。通过提高大型语言模型的适应能力，DuDe能够在多种下游任务中实现更高的性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) has emerged as a critical paradigm for adapting Large Language Models (LLMs) to downstream tasks, among which Low-rank Adaptation (LoRA) represents one of the most widely adopted methodologies. However, existing LoRA-based approaches exhibit two fundamental limitations: unstable training dynamics and inefficient knowledge transfer from pre-trained models, both stemming from random initialization of adapter parameters. To overcome these challenges, we propose DuDe, a novel approach that decomposes weight matrices into magnitude and direction components, employing Singular Value Decomposition (SVD) for principled initialization. Our comprehensive evaluation demonstrates DuDe's superior performance and robustness, achieving up to 48.35\% accuracy on MMLU and 62.53\% ($\pm$ 1.59) accuracy on GSM8K. Our theoretical analysis and empirical validation collectively demonstrate that DuDe's decomposition strategy enhances optimization stability and better preserves pre-trained representations, particularly for domain-specific tasks requiring specialized knowledge. The combination of robust empirical performance and rigorous theoretical foundations establishes DuDe as a significant contribution to PEFT methodologies for LLMs.

