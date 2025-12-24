---
layout: default
title: "RLMR: Reinforcement Learning with Mixed Rewards for Creative Writing"
---

# RLMR: Reinforcement Learning with Mixed Rewards for Creative Writing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18642" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18642v2</a>
  <a href="https://arxiv.org/pdf/2508.18642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18642v2', 'RLMR: Reinforcement Learning with Mixed Rewards for Creative Writing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianxing Liao, Tian Zhang, Xiao Feng, Yusong Zhang, Rui Yang, Haorui Wang, Bosi Wen, Ziying Wang, Runzhi Shi

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-26 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出RLMR以解决创意写作中的主观与客观平衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `创意写作` `强化学习` `混合奖励` `主观评估` `客观约束` `自动化评估` `语言模型`

## 📋 核心要点

1. 现有方法在创意写作中难以平衡主观质量与客观约束，导致效果不佳。
2. 提出RLMR，通过动态混合奖励系统结合主观与客观评估，优化写作质量与约束遵循。
3. 实验表明，RLMR在指令遵循和写作质量上均有显著提升，手动评估中胜率达到72.75%。

## 📝 摘要（中文）

大型语言模型在创意写作应用中被广泛使用。创意写作需要在主观写作质量（如文学性和情感表达）与客观约束遵循（如格式要求和字数限制）之间取得平衡。现有方法难以同时提升这两方面：单一奖励策略无法同时改善两种能力，而固定权重的混合奖励方法缺乏适应不同写作场景的能力。为了解决这一问题，我们提出了混合奖励强化学习（RLMR），利用动态混合奖励系统，结合评估主观写作质量的写作奖励模型和评估客观约束遵循的约束验证模型。通过动态调整约束遵循奖励权重，确保违反约束的样本在训练中受到惩罚。实验结果表明，我们的方法在指令遵循和写作质量上均有显著提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决创意写作中主观写作质量与客观约束遵循之间的平衡问题。现有方法往往无法同时提升这两方面的能力，导致写作效果不理想。

**核心思路**：我们提出的RLMR方法通过动态混合奖励系统，结合主观写作质量评估与客观约束验证，能够根据写作质量动态调整奖励权重，从而实现更好的写作效果。

**技术框架**：RLMR的整体架构包括两个主要模块：写作奖励模型和约束验证模型。写作奖励模型评估文本的主观质量，约束验证模型则检查文本是否符合预设的客观约束。两者的输出通过动态权重结合，形成最终的奖励信号。

**关键创新**：RLMR的核心创新在于动态调整约束遵循奖励权重，确保违反约束的样本在训练中受到惩罚。这一设计使得模型能够在不同写作场景中自适应调整，显著提升了写作质量与约束遵循的平衡。

**关键设计**：在模型训练中，我们设计了特定的损失函数以平衡主观与客观评估，同时采用了动态权重调整机制，确保在训练过程中能够实时反馈写作质量的变化。

## 📊 实验亮点

实验结果显示，RLMR在指令遵循评估中从83.36%提升至86.65%，在手动专家对比评估中，写作质量的胜率达到72.75%。这些结果表明RLMR在创意写作优化方面的显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括自动化创意写作、内容生成和教育等。通过优化写作质量与约束遵循，RLMR能够为创意写作提供更高效的工具，提升写作效果，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models are extensively utilized in creative writing applications. Creative writing requires a balance between subjective writing quality (e.g., literariness and emotional expression) and objective constraint following (e.g., format requirements and word limits). Existing methods find it difficult to balance these two aspects: single reward strategies fail to improve both abilities simultaneously, while fixed-weight mixed-reward methods lack the ability to adapt to different writing scenarios. To address this problem, we propose Reinforcement Learning with Mixed Rewards (RLMR), utilizing a dynamically mixed reward system from a writing reward model evaluating subjective writing quality and a constraint verification model assessing objective constraint following. The constraint following reward weight is adjusted dynamically according to the writing quality within sampled groups, ensuring that samples violating constraints get negative advantage in GRPO and thus penalized during training, which is the key innovation of this proposed method. We conduct automated and manual evaluations across diverse model families from 8B to 72B parameters. Additionally, we construct a real-world writing benchmark named WriteEval for comprehensive evaluation. Results illustrate that our method achieves consistent improvements in both instruction following (IFEval from 83.36% to 86.65%) and writing quality (72.75% win rate in manual expert pairwise evaluations on WriteEval). To the best of our knowledge, RLMR is the first work to combine subjective preferences with objective verification in online RL training, providing an effective solution for multi-dimensional creative writing optimization.

