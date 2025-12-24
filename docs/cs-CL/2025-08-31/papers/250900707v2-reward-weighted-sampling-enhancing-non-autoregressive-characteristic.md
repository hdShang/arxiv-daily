---
layout: default
title: "Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs"
---

# Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00707" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00707v2</a>
  <a href="https://arxiv.org/pdf/2509.00707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00707v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00707v2', 'Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daehoon Gwak, Minseo Jung, Junwoo Park, Minho Park, ChaeHun Park, Junha Hyung, Jaegul Choo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-31 (更新: 2025-09-20)

**备注**: EMNLP 2025 Main Paper (Long)

---

## 💡 一句话要点

**提出奖励加权采样以增强掩蔽扩散模型的非自回归特性**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `掩蔽扩散模型` `非自回归建模` `奖励加权采样` `序列生成` `自然语言处理`

## 📋 核心要点

1. 现有的掩蔽扩散模型在解码时采用独立令牌选择，导致生成顺序类似于自回归过程，限制了非自回归建模的优势。
2. 本文提出奖励加权采样（RWS），利用外部奖励模型在每个扩散步骤中评估整个序列的质量，以增强生成的全局一致性。
3. 实验结果显示，RWS显著促进了非自回归生成顺序，并在多个评估指标上取得了显著提升。

## 📝 摘要（中文）

掩蔽扩散模型（MDMs）为大型语言建模提供了有前景的非自回归替代方案。现有的解码方法如基于置信度的采样，通常独立选择每个令牌，导致生成顺序类似于自回归过程，限制了非自回归建模的优势。为此，本文提出了一种新颖的解码策略——奖励加权采样（RWS），通过外部奖励模型在迭代扩散过程中提供全局信号。RWS在每个扩散步骤中评估整个中间序列的质量，并相应地调整令牌的logits，从而促进更非自回归的生成顺序。实验结果表明，RWS显著提升了非自回归生成顺序，并在多个评估指标上取得了改善。

## 🔬 方法详解

**问题定义**：本文旨在解决掩蔽扩散模型在解码过程中令牌独立选择导致的生成顺序类似于自回归过程的问题。这种现象限制了非自回归建模的优势，影响了生成质量和效率。

**核心思路**：论文提出的奖励加权采样（RWS）策略，通过引入外部奖励模型，在每个扩散步骤中评估整个序列的质量，从而调整令牌的选择过程，促进更非自回归的生成顺序。

**技术框架**：RWS的整体架构包括三个主要阶段：首先，在每个扩散步骤中评估当前生成序列的质量；其次，根据评估结果调整令牌的logits；最后，基于调整后的logits进行令牌选择，确保生成的序列具有更好的全局一致性。

**关键创新**：RWS的核心创新在于引入外部奖励模型进行全局序列质量评估，并通过logits的加权调整实现令牌选择的全局优化。这与传统的独立令牌选择方法形成了本质区别。

**关键设计**：在RWS中，关键参数包括奖励模型的设计、logits的加权策略以及生成序列的评估标准。这些设计确保了生成过程中的全局一致性和非自回归特性。

## 📊 实验亮点

实验结果表明，RWS显著促进了非自回归生成顺序，提升幅度在多个评估指标上均有显著改善。例如，相较于基线方法，RWS在生成质量和一致性上均有明显提升，具体数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、对话系统以及机器翻译等。通过提升非自回归模型的生成质量，RWS能够在实际应用中提高生成效率和用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Masked diffusion models (MDMs) offer a promising non-autoregressive alternative for large language modeling. Standard decoding methods for MDMs, such as confidence-based sampling, select tokens independently based on individual token confidences at each diffusion step. However, we observe that this independent token selection often results in generation orders resembling sequential autoregressive processes, limiting the advantages of non-autoregressive modeling. To mitigate this pheonomenon, we propose Reward-Weighted Sampling (RWS), a novel decoding strategy that leverages an external reward model to provide a principled global signal during the iterative diffusion process. Specifically, at each diffusion step, RWS evaluates the quality of the entire intermediate sequence and scales token logits accordingly, guiding token selection by integrating global sequence-level coherence. This method selectively increases the confidence of tokens that initially have lower scores, thereby promoting a more non-autoregressive generation order. Furthermore, we provide theoretical justification showing that reward-weighted logit scaling induces beneficial rank reversals in token selection and consistently improves expected reward. Experiments demonstrate that RWS significantly promotes non-autoregressive generation orders, leading to improvements across multiple evaluation metrics. These results highlight the effectiveness of integrating global signals in enhancing both the non-autoregressive properties and overall performance of MDMs.

