---
layout: default
title: "SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From"
---

# SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26404" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26404v1</a>
  <a href="https://arxiv.org/pdf/2509.26404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26404v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26404v1', 'SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Tong, Haonan Wang, Siquan Li, Kenji Kawaguchi, Tianyang Hu

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出SeedPrints以解决大语言模型归属验证问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `指纹识别` `模型归属` `随机初始化` `身份验证` `统计检测` `鲁棒性`

## 📋 核心要点

1. 现有指纹识别方法在模型收敛前不可靠，且对数据分布变化敏感，难以进行有效的模型归属验证。
2. 本文提出SeedPrints方法，利用随机初始化偏差作为种子依赖的标识符，能够在训练前就识别模型的身份。
3. 实验表明，SeedPrints在LLaMA和Qwen模型上实现了高效的种子级别区分，能够提供从出生到生命周期的身份验证。

## 📝 摘要（中文）

指纹识别大语言模型（LLMs）对于来源验证和模型归属至关重要。现有方法通常依赖于训练动态、数据暴露或超参数等后验特征，这些特征在训练开始后才会显现。本文提出了一种更强大且内在的LLM指纹识别方法：SeedPrints，该方法利用随机初始化偏差作为持久的、依赖于种子的标识符，甚至在训练之前就存在。我们展示了未训练模型在初始化时仅基于其参数表现出可重复的标记选择偏差。这些偏差在整个训练过程中稳定且可测量，使我们的统计检测方法能够高置信度地恢复模型的血统。与之前的技术不同，SeedPrints在所有训练阶段都有效，并且在领域转移或参数修改下具有鲁棒性。实验结果表明，SeedPrints实现了种子级别的可区分性，能够提供类似生物特征指纹的身份验证。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型指纹识别中的归属验证问题，现有方法在模型训练初期不可靠，且对数据分布变化敏感，导致无法有效识别模型来源。

**核心思路**：提出SeedPrints方法，通过利用模型初始化时的随机偏差，作为持久的、种子依赖的标识符，能够在训练前就实现模型身份的识别。

**技术框架**：该方法的整体框架包括初始化阶段的参数设置、训练过程中的偏差测量，以及后续的统计检测模块，确保在不同训练阶段均能有效识别模型。

**关键创新**：SeedPrints的核心创新在于其利用了模型初始化的随机性，形成了一种稳定且可测量的指纹，与传统方法相比，SeedPrints在训练初期就能提供可靠的身份验证。

**关键设计**：在技术细节上，SeedPrints关注于初始化参数的选择和偏差的统计分析，确保在不同模型架构和训练条件下均能保持其有效性。

## 📊 实验亮点

实验结果显示，SeedPrints在LLaMA和Qwen模型上实现了种子级别的可区分性，能够在不同训练阶段保持高效的身份验证能力。与传统方法相比，SeedPrints在模型训练初期的有效性显著提升，确保了在领域转移和参数修改下的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括模型监管、版权保护和安全审计等，能够为大语言模型的来源验证提供可靠的技术支持，提升模型使用的透明度和可追溯性。未来，SeedPrints可能在多种AI应用中发挥重要作用，确保模型的合法性和可信度。

## 📄 摘要（原文）

> Fingerprinting Large Language Models (LLMs) is essential for provenance verification and model attribution. Existing methods typically extract post-hoc signatures based on training dynamics, data exposure, or hyperparameters -- properties that only emerge after training begins. In contrast, we propose a stronger and more intrinsic notion of LLM fingerprinting: SeedPrints, a method that leverages random initialization biases as persistent, seed-dependent identifiers present even before training. We show that untrained models exhibit reproducible token selection biases conditioned solely on their parameters at initialization. These biases are stable and measurable throughout training, enabling our statistical detection method to recover a model's lineage with high confidence. Unlike prior techniques, unreliable before convergence and vulnerable to distribution shifts, SeedPrints remains effective across all training stages and robust under domain shifts or parameter modifications. Experiments on LLaMA-style and Qwen-style models show that SeedPrints achieves seed-level distinguishability and can provide birth-to-lifecycle identity verification akin to a biometric fingerprint. Evaluations on large-scale pretrained models and fingerprinting benchmarks further confirm its effectiveness under practical deployment scenarios. These results suggest that initialization itself imprints a unique and persistent identity on neural language models, forming a true ''Galtonian'' fingerprint.

