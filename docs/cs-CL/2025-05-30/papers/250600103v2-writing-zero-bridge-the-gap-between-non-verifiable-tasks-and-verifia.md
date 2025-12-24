---
layout: default
title: "Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards"
---

# Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00103" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00103v2</a>
  <a href="https://arxiv.org/pdf/2506.00103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00103v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00103v2', 'Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruipeng Jia, Yunyi Yang, Yongbo Gai, Kai Luo, Shihao Huang, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-06-11)

---

## 💡 一句话要点

**提出Writing-Zero以解决非可验证任务与可验证奖励之间的差距问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `生成模型` `奖励机制` `自然语言处理` `创意写作` `开放式对话` `机器学习`

## 📋 核心要点

1. 现有方法在处理非可验证任务时面临主观评估的挑战，导致奖励模型的泛化能力不足。
2. 提出了一种基于写作原则的成对生成奖励模型（GenRM）和自举相对策略优化（BRPO）算法，旨在将主观评估转化为可靠的可验证奖励。
3. 实验结果表明，Writing-Zero在多个写作基准上表现出一致的改进，并且对奖励操控具有强抵抗力。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）使大型语言模型（LLMs）在数学和代码生成等具有客观真相答案的推理任务中取得了显著突破。然而，对于创意写作和开放式对话等非可验证任务，质量评估本质上是主观的，缺乏明确的参考。现有方法通常依赖于基于人类偏好的标量奖励模型，这些模型在泛化能力上有限，并容易受到奖励操控的影响。本文提出了一种统一的基于RLVR的训练范式，介绍了一种基于写作原则的成对生成奖励模型（GenRM）和一种新颖的自举相对策略优化（BRPO）算法。我们的研究表明，该方法在多个写作基准上表现出竞争力，且在抵抗奖励操控方面优于标量奖励基线。

## 🔬 方法详解

**问题定义**：本文旨在解决非可验证任务（如创意写作）中质量评估主观性的问题，现有方法依赖的标量奖励模型在泛化能力和奖励操控方面存在不足。

**核心思路**：通过引入基于写作原则的成对生成奖励模型（GenRM），将主观评估转化为可靠的可验证奖励，同时利用自举相对策略优化（BRPO）算法实现动态的无参考成对比较。

**技术框架**：整体架构包括GenRM和BRPO两个主要模块，GenRM负责生成可验证的奖励，BRPO则在RL训练过程中通过自举响应进行动态比较。

**关键创新**：最重要的创新在于将主观评估转化为可验证奖励的能力，以及通过自举方法实现无参考的动态比较，这与现有方法的静态标量奖励模型形成了本质区别。

**关键设计**：在GenRM中，采用了自我原则批评机制来增强奖励的可靠性；BRPO算法则通过在组回合中生成的自举响应作为临时参考，优化了策略更新过程。具体的损失函数和网络结构设计尚未详细披露。

## 📊 实验亮点

实验结果显示，Writing-Zero在多个内部和开源写作基准上取得了竞争力的结果，相较于标量奖励基线，表现出一致的性能提升，并且在抵抗奖励操控方面表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括创意写作、开放式对话生成等需要主观评估的任务。通过提供可靠的奖励机制，Writing-Zero能够帮助大型语言模型在这些领域中提升写作能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has enabled large language models (LLMs) to achieve remarkable breakthroughs in reasoning tasks with objective ground-truth answers, such as mathematics and code generation. However, a significant gap remains for non-verifiable tasks, like creative writing and open-ended dialogue, where quality assessment is inherently subjective and lacks definitive references. Existing approaches for these domains often rely on scalar reward models trained with human preferences, which suffer from limited generalization and are prone to reward hacking, such as over-explanation and length bias. In this work, we propose a unified RLVR-based training paradigm that bridges the gap between non-verifiable tasks and verifiable rewards. We introduce a writing-principle-based pairwise Generative Reward Model (GenRM) and a novel Bootstrapped Relative Policy Optimization (BRPO) algorithm. The pairwise writing GenRM leverages self-principled critique to transform subjective assessments into reliable, verifiable rewards, while BRPO enables dynamic, reference-free pairwise comparison by leveraging a bootstrapped response as temporary reference from within group rollouts during RL training. Our approach empowers LLMs to develop robust writing capabilities without supervised fine-tuning, as demonstrated by Writing-Zero, which shows consistent improvement and strong resistance to reward hacking compared to scalar reward baselines. Furthermore, our method achieves competitive results on both in-house and open-source writing benchmarks. Our findings suggest the potential to unify rule-based, reference-based, and reference-free reward modeling under the RLVR framework, thus paving the way for a comprehensive and scalable RL training paradigm applicable across all language tasks.

