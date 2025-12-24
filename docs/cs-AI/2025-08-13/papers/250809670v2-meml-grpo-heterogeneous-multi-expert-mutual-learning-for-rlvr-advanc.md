---
layout: default
title: "MEML-GRPO: Heterogeneous Multi-Expert Mutual Learning for RLVR Advancement"
---

# MEML-GRPO: Heterogeneous Multi-Expert Mutual Learning for RLVR Advancement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09670" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09670v2</a>
  <a href="https://arxiv.org/pdf/2508.09670.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09670v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09670v2', 'MEML-GRPO: Heterogeneous Multi-Expert Mutual Learning for RLVR Advancement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weitao Jia, Jinghui Lu, Haiyang Yu, Siqi Wang, Guozhi Tang, An-Lan Wang, Weijie Yin, Dingkang Yang, Yuxiang Nie, Bin Shan, Hao Feng, Irene Li, Kun Yang, Han Wang, Jingqun Tang, Teng Fu, Changhong Jin, Chao Feng, Xiaohui Lv, Can Huang

**分类**: cs.AI

**发布日期**: 2025-08-13 (更新: 2025-12-18)

---

## 💡 一句话要点

**提出MEML-GRPO以解决RLVR中的奖励稀疏问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `可验证奖励` `多专家学习` `知识共享` `推理能力提升`

## 📋 核心要点

1. 现有的标准RLVR方法在面对奖励稀疏问题时表现不佳，尤其是在错误候选答案频繁出现的情况下，无法提供有效的学习信号。
2. 本文提出的MEML-GRPO框架通过多专家互学习机制，利用多样化的专家提示生成更广泛的响应，从而提高正确答案的识别率。
3. 实验结果表明，MEML-GRPO在多个推理基准上取得了显著提升，Qwen的平均性能提升为4.89%，Llama的提升幅度达到11.33%。

## 📝 摘要（中文）

近年来的研究表明，具有可验证奖励的强化学习（RLVR）显著提升了大型语言模型（LLMs）的推理能力。然而，标准RLVR面临奖励稀疏的挑战，尤其是在困难任务中，错误候选答案的零奖励无法提供学习信号。为此，本文提出了多专家互学习GRPO（MEML-GRPO）框架，利用多样化的专家提示生成更广泛的响应，从而显著提高识别正确解决方案的可能性。此外，本文引入了专家间的互学习机制，促进知识共享与转移，进一步提升模型在RLVR中的表现。通过在多个推理基准上的广泛实验，MEML-GRPO显示出显著的改进，Qwen的平均性能提升为4.89%，Llama为11.33%，有效克服了传统RLVR方法的核心局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决标准RLVR方法在奖励稀疏情况下的学习信号缺失问题，尤其是在复杂任务中，错误候选答案导致的零奖励无法有效指导学习。

**核心思路**：MEML-GRPO框架的核心思路是通过多专家互学习机制，利用多样化的专家提示生成更广泛的响应，从而增加识别正确答案的机会。这样的设计旨在通过知识共享和转移，提升模型的整体性能。

**技术框架**：MEML-GRPO的整体架构包括多个专家模型，每个专家生成不同的响应，并通过互学习机制进行知识共享。该框架分为专家提示生成、响应生成和互学习三个主要模块。

**关键创新**：本文的主要创新在于引入了多专家互学习机制，使得不同专家之间能够有效共享知识，克服了传统RLVR方法的局限性，特别是在奖励稀疏的情况下。

**关键设计**：在技术细节上，本文设置了多个专家模型，每个模型使用不同的提示生成策略，并设计了特定的损失函数以促进互学习过程中的知识共享与转移。

## 📊 实验亮点

实验结果显示，MEML-GRPO在多个推理基准上显著提升了模型性能，Qwen的平均性能提升为4.89%，而Llama的提升幅度更是达到11.33%。这些结果表明，该方法有效克服了传统RLVR方法的核心局限性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动化推理等。通过提升大型语言模型的推理能力，MEML-GRPO能够在复杂任务中提供更准确的答案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances demonstrate that reinforcement learning with verifiable rewards (RLVR) significantly enhances the reasoning capabilities of large language models (LLMs). However, standard RLVR faces challenges with reward sparsity, where zero rewards from consistently incorrect candidate answers provide no learning signal, particularly in challenging tasks. To address this, we propose Multi-Expert Mutual Learning GRPO (MEML-GRPO), an innovative framework that utilizes diverse expert prompts as system prompts to generate a broader range of responses, substantially increasing the likelihood of identifying correct solutions. Additionally, we introduce an inter-expert mutual learning mechanism that facilitates knowledge sharing and transfer among experts, further boosting the model's performance through RLVR. Extensive experiments across multiple reasoning benchmarks show that MEML-GRPO delivers significant improvements, achieving an average performance gain of 4.89% with Qwen and 11.33% with Llama, effectively overcoming the core limitations of traditional RLVR methods.

