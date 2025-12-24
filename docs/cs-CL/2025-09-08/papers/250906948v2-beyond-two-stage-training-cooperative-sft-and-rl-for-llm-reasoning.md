---
layout: default
title: "Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning"
---

# Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06948" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06948v2</a>
  <a href="https://arxiv.org/pdf/2509.06948.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06948v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06948v2', 'Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Chen, Xueting Han, Li Shen, Jing Bai, Kam-Fai Wong

**分类**: cs.CL

**发布日期**: 2025-09-08 (更新: 2025-10-16)

---

## 💡 一句话要点

**提出协同SFT与RL训练框架，解决LLM推理中灾难性遗忘与效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `监督微调` `推理能力` `双层优化`

## 📋 核心要点

1. 现有两阶段SFT和RL训练LLM推理能力的方法存在灾难性遗忘问题，导致RL训练效率低下。
2. 论文提出一种协同SFT和RL的训练框架，通过双层优化，使SFT能够指导RL的优化过程。
3. 实验结果表明，该方法在多个推理基准上优于现有方法，并在效率和性能之间取得平衡。

## 📝 摘要（中文）

强化学习(RL)已被证明能有效激励大型语言模型(LLM)的推理能力，但由于其试错性质，面临严重的效率挑战。常见的做法是采用监督微调(SFT)作为RL的预热阶段，但这种解耦的两阶段方法存在灾难性遗忘问题：第二阶段的RL逐渐丢失SFT习得的行为，并低效地探索新的模式。本研究提出了一种新的推理模型学习方法，该方法采用双层优化来促进这些训练范式之间更好的合作。通过将SFT目标建立在最优RL策略的基础上，我们的方法使SFT能够元学习如何指导RL的优化过程。在训练过程中，下层执行RL更新，同时接受SFT监督，上层显式地最大化协同增益——联合SFT-RL训练相对于单独RL的性能优势。在五个推理基准上的实证评估表明，我们的方法始终优于基线，并在有效性和效率之间实现了更好的平衡。

## 🔬 方法详解

**问题定义**：现有方法通常采用两阶段训练策略，先使用SFT进行预训练，然后使用RL进行微调。这种方法的主要问题在于，RL训练过程中会逐渐遗忘SFT阶段学习到的知识，导致训练效率降低，最终性能受限。因此，需要一种能够有效结合SFT和RL优势，避免灾难性遗忘的训练方法。

**核心思路**：论文的核心思路是通过双层优化，将SFT和RL训练过程紧密结合。具体来说，SFT的目标是帮助RL更好地进行探索，而RL的目标是提升整体性能。通过这种协同训练的方式，SFT可以元学习如何指导RL的优化过程，从而避免灾难性遗忘，提高训练效率。

**技术框架**：该方法采用双层优化框架。下层优化器执行RL更新，同时接受SFT的监督。上层优化器则显式地最大化协同增益，即联合SFT-RL训练相对于单独RL训练的性能提升。这种框架允许SFT和RL相互协作，共同提升模型的推理能力。

**关键创新**：该方法最重要的创新在于将SFT和RL训练过程解耦，通过双层优化框架将二者紧密结合，使得SFT能够指导RL的优化过程，从而避免灾难性遗忘，提高训练效率。这种协同训练的方式是与现有两阶段训练方法最本质的区别。

**关键设计**：该方法的关键设计包括：1) 将SFT目标建立在最优RL策略的基础上，使得SFT能够学习如何指导RL的优化；2) 上层优化器显式地最大化协同增益，鼓励SFT和RL之间的合作；3) 使用合适的损失函数来平衡SFT和RL的训练目标。

## 📊 实验亮点

在五个推理基准上的实验结果表明，该方法始终优于现有基线方法，并在有效性和效率之间实现了更好的平衡。具体性能数据未知，但论文强调了该方法在避免灾难性遗忘和提高训练效率方面的优势。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的大型语言模型应用场景，例如智能问答、对话系统、代码生成等。通过提高模型的推理能力和训练效率，可以降低模型部署成本，提升用户体验，并推动相关人工智能技术的进步。

## 📄 摘要（原文）

> Reinforcement learning (RL) has proven effective in incentivizing the reasoning abilities of large language models (LLMs), but suffers from severe efficiency challenges due to its trial-and-error nature. While the common practice employs supervised fine-tuning (SFT) as a warm-up stage for RL, this decoupled two-stage approach suffers from catastrophic forgetting: second-stage RL gradually loses SFT-acquired behaviors and inefficiently explores new patterns. This study introduces a novel method for learning reasoning models that employs bilevel optimization to facilitate better cooperation between these training paradigms. By conditioning the SFT objective on the optimal RL policy, our approach enables SFT to meta-learn how to guide RL's optimization process. During training, the lower level performs RL updates while simultaneously receiving SFT supervision, and the upper level explicitly maximizes the cooperative gain-the performance advantage of joint SFT-RL training over RL alone. Empirical evaluations on five reasoning benchmarks demonstrate that our method consistently outperforms baselines and achieves a better balance between effectiveness and efficiency.

