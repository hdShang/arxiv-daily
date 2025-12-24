---
layout: default
title: "MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models"
---

# MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13148" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13148v2</a>
  <a href="https://arxiv.org/pdf/2508.13148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13148v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13148v2', 'MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu He, Katrin Renz, Yong Cao, Andreas Geiger

**分类**: cs.LG

**发布日期**: 2025-08-18 (更新: 2025-09-25)

**🔗 代码/项目**: [GITHUB](https://github.com/autonomousvision/mdpo) | [PROJECT_PAGE](https://cli212.github.io/MDPO/)

---

## 💡 一句话要点

**提出MDPO以解决掩码扩散语言模型训练与推理不一致问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `掩码扩散模型` `强化学习` `序列决策` `自然语言处理` `模型优化` `去噪策略` `性能提升`

## 📋 核心要点

1. 现有的掩码扩散语言模型在训练和推理阶段存在结构揭示不一致的问题，导致性能下降。
2. 本文提出了掩码扩散策略优化（MDPO），通过强化学习解决训练与推理阶段的差异，显式训练模型。
3. 实验结果表明，MDPO在减少梯度更新次数的同时，提升了模型在多个数据集上的性能，表现出显著的改进。

## 📝 摘要（中文）

掩码扩散语言模型（MDLMs）作为传统自回归模型的有力替代，能够更快生成文本并更丰富地进行双向上下文条件。然而，它们在训练和推理阶段存在关键差异：推理时逐步揭示生成序列的结构，而训练时随机掩码忽略了这一结构。为了解决这一问题，本文将有效去噪轨迹的学习框架视为一个序列决策问题，并应用强化学习。我们提出了一种新颖的掩码扩散策略优化（MDPO），在推理时使用相同的逐步精炼调度进行显式训练。MDPO在梯度更新次数减少60倍的情况下，达到了之前最先进方法的性能，并在MATH500和Countdown数据集上分别提高了9.6%和54.2%的准确率。此外，我们改进了MDLMs的重新掩码策略，提出了一种无训练方法——运行置信度重新掩码（RCR），进一步提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决掩码扩散语言模型在训练和推理阶段之间的结构揭示不一致问题。现有方法在训练时随机掩码，导致推理时的性能下降。

**核心思路**：我们将有效去噪轨迹的学习视为序列决策问题，利用强化学习框架进行显式训练，以匹配推理时的逐步精炼调度。

**技术框架**：整体架构包括MDPO的训练过程，利用马尔可夫性质进行模型优化。主要模块包括状态表示、动作选择和奖励反馈机制。

**关键创新**：MDPO的核心创新在于通过强化学习显式训练模型，克服了传统方法中训练与推理阶段的差异，显著提高了模型性能。

**关键设计**：在设计中，我们设置了特定的奖励函数以引导模型学习有效的去噪策略，并优化了网络结构以适应逐步精炼的过程。

## 📊 实验亮点

实验结果显示，MDPO在与之前最先进方法的比较中，减少了60倍的梯度更新次数，同时在MATH500和Countdown数据集上分别提高了9.6%和54.2%的性能，展现出显著的改进效果。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言生成、对话系统和文本补全等。通过提高掩码扩散语言模型的性能，能够在实际应用中实现更高效的文本生成和更准确的上下文理解，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Diffusion language models, as a promising alternative to traditional autoregressive (AR) models, enable faster generation and richer conditioning on bidirectional context. However, they suffer from a key discrepancy between training and inference: during inference, MDLMs progressively reveal the structure of the generated sequence by producing fewer and fewer masked tokens, whereas this structure is ignored in training as tokens are masked at random. Although this discrepancy between training and inference can lead to suboptimal performance, it has been largely overlooked by previous works, leaving closing this gap between the two stages an open problem. To address this, we frame the problem of learning effective denoising trajectories as a sequential decision-making problem and use the resulting framework to apply reinforcement learning. We propose a novel Masked Diffusion Policy Optimization (MDPO) to exploit the Markov property diffusion possesses and explicitly train the model under the same progressive refining schedule used at inference. MDPO matches the performance of the previous state-of-the-art (SOTA) method with 60x fewer gradient updates, while achieving average improvements of 9.6% on MATH500 and 54.2% on Countdown over SOTA when trained within the same number of weight updates. Additionally, we improve the remasking strategy of MDLMs as a plug-in inference replacement to overcome the limitation that the model cannot refine tokens flexibly. This training-free method, termed Running Confidence Remasking (RCR), consistently enhances performance and provides further improvements when used with MDPO. Our findings establish great potential for investigating the discrepancy between pre-training and inference of MDLMs. Code: https://github.com/autonomousvision/mdpo. Project Page: https://cli212.github.io/MDPO/.

