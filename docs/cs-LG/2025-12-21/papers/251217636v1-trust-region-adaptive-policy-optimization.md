---
layout: default
title: Trust-Region Adaptive Policy Optimization
---

# Trust-Region Adaptive Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17636" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17636v1</a>
  <a href="https://arxiv.org/pdf/2512.17636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17636v1', 'Trust-Region Adaptive Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyu Su, Jian Guan, Yuxian Gu, Minlie Huang, Hongning Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出TRAPO，交错SFT与RL优化LLM推理能力，显著提升数学推理性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `监督式微调` `推理能力` `信任区域优化`

## 📋 核心要点

1. 现有SFT-then-RL两阶段训练流程存在SFT抑制探索和导致遗忘的问题，限制了RL的改进潜力。
2. TRAPO交错SFT和RL，统一外部监督和自我探索，并引入Trust-Region SFT稳定训练。
3. 实验表明，TRAPO在数学推理任务上超越了SFT、RL以及SFT-then-RL等基线方法。

## 📝 摘要（中文）

本文提出Trust-Region Adaptive Policy Optimization (TRAPO)，旨在解决大型语言模型(LLMs)在复杂推理能力提升中，监督式微调(SFT)和强化学习(RL)两阶段训练流程的不一致性问题。传统SFT强制模仿，抑制探索并导致遗忘，限制了RL的改进潜力。TRAPO是一种混合框架，通过在每个训练实例中交错SFT和RL，优化专家前缀上的SFT损失和模型自身补全上的RL损失，从而统一外部监督和自我探索。为了稳定训练，引入Trust-Region SFT (TrSFT)，在信任区域内最小化前向KL散度，并在区域外衰减优化，有效转向反向KL，产生稳定的、模式寻求的更新，有利于RL。自适应前缀选择机制进一步根据测量的效用分配专家指导。在五个数学推理基准上的实验表明，TRAPO始终优于标准SFT、RL和SFT-then-RL流程，以及最近的state-of-the-art方法，为增强LLM推理能力建立了一个强大的新范式。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型通过监督微调（SFT）和强化学习（RL）进行后训练时，SFT阶段对RL阶段的负面影响。具体来说，SFT过度模仿专家数据，限制了模型后续在RL阶段的探索能力，并可能导致模型遗忘先前学习到的知识。这种两阶段训练流程的不一致性阻碍了模型推理能力的进一步提升。

**核心思路**：TRAPO的核心思路是在训练过程中交错进行SFT和RL，从而将外部监督和自我探索结合起来。通过在每个训练实例中同时优化专家前缀上的SFT损失和模型自身补全上的RL损失，模型可以在模仿专家行为的同时，探索新的解决方案。此外，引入Trust-Region SFT (TrSFT) 来稳定训练过程，避免模型在RL阶段发生剧烈变化。

**技术框架**：TRAPO的整体框架包含以下几个关键部分：1) 交错SFT和RL：在每个训练步骤中，模型首先根据专家前缀生成补全，然后计算SFT损失和RL损失。2) Trust-Region SFT (TrSFT)：通过限制SFT的更新幅度，防止模型过度拟合专家数据。3) 自适应前缀选择：根据模型在当前状态下的表现，动态选择合适的专家前缀进行学习。整个训练流程旨在平衡模仿学习和强化学习，从而提高模型的推理能力。

**关键创新**：TRAPO的关键创新在于其混合训练框架，它打破了传统的SFT-then-RL两阶段训练模式，实现了SFT和RL的无缝集成。通过交错SFT和RL，TRAPO能够更好地利用专家知识，同时鼓励模型进行自我探索。此外，Trust-Region SFT的引入有效地稳定了训练过程，避免了模型在RL阶段出现不稳定的情况。

**关键设计**：TrSFT的关键设计在于使用信任区域来约束SFT的更新。具体来说，TrSFT最小化信任区域内的前向KL散度，并在区域外衰减优化，从而有效地转向反向KL散度。这种设计使得模型能够更稳定地学习专家知识，并避免过度拟合。此外，自适应前缀选择机制根据模型在当前状态下的表现，动态调整专家指导的强度，从而进一步提高了训练效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17636v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17636v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17636v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TRAPO在五个数学推理基准上均优于标准SFT、RL和SFT-then-RL流程，以及最近的state-of-the-art方法。例如，在某些基准测试中，TRAPO的性能提升超过了10%。这些结果表明，TRAPO是一种有效的增强LLM推理能力的方法。

## 🎯 应用场景

TRAPO方法可广泛应用于需要复杂推理能力的大型语言模型，例如数学问题求解、代码生成、逻辑推理等领域。该方法通过结合模仿学习和强化学习，能够有效提升模型的推理能力和泛化性能，具有重要的实际应用价值。未来，该方法可以进一步扩展到其他类型的任务和模型，例如多模态推理和对话生成。

## 📄 摘要（原文）

> Post-training methods, especially Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), play an important role in improving large language models' (LLMs) complex reasoning abilities. However, the dominant two-stage pipeline (SFT then RL) suffers from a key inconsistency: SFT enforces rigid imitation that suppresses exploration and induces forgetting, limiting RL's potential for improvements. We address this inefficiency with TRAPO (\textbf{T}rust-\textbf{R}egion \textbf{A}daptive \textbf{P}olicy \textbf{O}ptimization), a hybrid framework that interleaves SFT and RL within each training instance by optimizing SFT loss on expert prefixes and RL loss on the model's own completions, unifying external supervision and self-exploration. To stabilize training, we introduce Trust-Region SFT (TrSFT), which minimizes forward KL divergence inside a trust region but attenuates optimization outside, effectively shifting toward reverse KL and yielding stable, mode-seeking updates favorable for RL. An adaptive prefix-selection mechanism further allocates expert guidance based on measured utility. Experiments on five mathematical reasoning benchmarks show that TRAPO consistently surpasses standard SFT, RL, and SFT-then-RL pipelines, as well as recent state-of-the-art approaches, establishing a strong new paradigm for reasoning-enhanced LLMs.

