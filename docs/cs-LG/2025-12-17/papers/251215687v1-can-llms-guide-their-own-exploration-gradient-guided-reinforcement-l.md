---
layout: default
title: Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning
---

# Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15687" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15687v1</a>
  <a href="https://arxiv.org/pdf/2512.15687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15687v1" onclick="toggleFavorite(this, '2512.15687v1', 'Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenwen Liang, Sidi Lu, Wenhao Yu, Kishan Panaganti, Yujun Zhou, Haitao Mi, Dong Yu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出G2RL：利用梯度引导强化学习提升LLM推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `梯度引导` `探索策略` `推理能力`

## 📋 核心要点

1. 现有强化学习方法在探索LLM推理能力时，依赖熵奖励等外部启发式方法，与模型实际学习方式脱节。
2. G2RL通过模型自身梯度信息引导探索，奖励带来新梯度方向的轨迹，抑制冗余更新，实现自引用探索。
3. 实验表明，G2RL在数学和通用推理任务上，显著提升了Qwen3模型的pass@1等指标，优于现有方法。

## 📝 摘要（中文）

强化学习对于增强大型语言模型的推理能力至关重要，但现有的探索机制与模型的实际学习方式存在根本上的不一致。熵奖励和外部语义比较器鼓励表面层次的变化，但不能保证抽样的轨迹在塑造优化的更新方向上有所不同。我们提出了G2RL，一个梯度引导的强化学习框架，其中探索不是由外部启发式方法驱动，而是由模型自身的一阶更新几何驱动。对于每个响应，G2RL从模型最后一层的敏感性构建一个序列级别的特征（可以通过标准前向传递以忽略不计的成本获得），并通过比较抽样组内的这些特征来衡量每个轨迹将如何重塑策略。引入新梯度方向的轨迹会收到有界的乘法奖励缩放，而冗余或偏离流形的更新则被弱化，从而产生一个自引用的探索信号，该信号自然地与PPO风格的稳定性和KL控制对齐。在Qwen3 base 1.7B和4B模型上，针对数学和通用推理基准测试（MATH500、AMC、AIME24、AIME25、GPQA、MMLUpro），G2RL始终优于基于熵的GRPO和外部嵌入方法，在pass@1、maj@16和pass@k指标上均有提升。通过分析诱导几何，我们发现G2RL将探索扩展到更多正交且通常相反的梯度方向，同时保持语义连贯性，这表明策略自身的更新空间为指导大型语言模型强化学习中的探索提供了一个更忠实和有效的依据。

## 🔬 方法详解

**问题定义**：现有强化学习方法在训练LLM进行推理时，其探索策略（如熵奖励）与LLM的实际学习过程不匹配。这些方法鼓励表面的多样性，但无法保证探索的轨迹能够有效地改变模型的优化方向。因此，如何设计一种与LLM学习方式更契合的探索策略，是本文要解决的核心问题。

**核心思路**：G2RL的核心思路是利用LLM自身的梯度信息来引导探索。具体来说，G2RL通过分析模型最后一层的敏感性，提取序列级别的特征，并基于这些特征来评估每个轨迹对策略更新的影响。奖励那些能够引入新的梯度方向的轨迹，同时抑制那些冗余或偏离流形的更新。这种自引用的探索信号能够更好地与PPO等强化学习算法的稳定性和KL散度控制相配合。

**技术框架**：G2RL的整体框架如下：1) 对于每个LLM的响应，计算其最后一层的敏感性，得到序列级别的特征表示。2) 在一个抽样组内，比较不同轨迹的特征表示，评估它们对策略更新的影响。3) 根据轨迹引入的梯度方向的新颖性，给予相应的奖励缩放。引入新梯度方向的轨迹获得正向奖励，而冗余或偏离流形的轨迹则受到惩罚。4) 使用PPO等强化学习算法，基于调整后的奖励信号来更新LLM的策略。

**关键创新**：G2RL最关键的创新在于其探索策略是基于模型自身的梯度信息，而不是外部的启发式方法。这种自引用的探索方式能够更好地与LLM的学习过程相匹配，从而更有效地提升模型的推理能力。与现有方法相比，G2RL能够探索到更多正交且通常相反的梯度方向，从而更全面地覆盖模型的解空间。

**关键设计**：G2RL的关键设计包括：1) 使用模型最后一层的敏感性作为序列级别的特征表示，这可以通过标准的前向传播以很低的成本获得。2) 使用有界的乘法奖励缩放来调整轨迹的奖励，以保证训练的稳定性。3) 将G2RL与PPO等强化学习算法相结合，利用PPO的稳定性和KL散度控制来约束策略的更新。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15687v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15687v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15687v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，G2RL在MATH500、AMC、AIME24、AIME25、GPQA、MMLUpro等多个数学和通用推理基准测试上，显著优于基于熵的GRPO和外部嵌入方法。例如，在Qwen3 base 1.7B和4B模型上，G2RL在pass@1、maj@16和pass@k等指标上均有提升，证明了其有效性。

## 🎯 应用场景

G2RL具有广泛的应用前景，可以应用于各种需要LLM进行复杂推理的任务，例如数学问题求解、代码生成、知识问答等。该方法能够提升LLM的推理能力和泛化性能，使其在实际应用中更加可靠和有效。此外，G2RL的自引用探索思想也可以推广到其他类型的模型和任务中。

## 📄 摘要（原文）

> Reinforcement learning has become essential for strengthening the reasoning abilities of large language models, yet current exploration mechanisms remain fundamentally misaligned with how these models actually learn. Entropy bonuses and external semantic comparators encourage surface level variation but offer no guarantee that sampled trajectories differ in the update directions that shape optimization. We propose G2RL, a gradient guided reinforcement learning framework in which exploration is driven not by external heuristics but by the model own first order update geometry. For each response, G2RL constructs a sequence level feature from the model final layer sensitivity, obtainable at negligible cost from a standard forward pass, and measures how each trajectory would reshape the policy by comparing these features within a sampled group. Trajectories that introduce novel gradient directions receive a bounded multiplicative reward scaler, while redundant or off manifold updates are deemphasized, yielding a self referential exploration signal that is naturally aligned with PPO style stability and KL control. Across math and general reasoning benchmarks (MATH500, AMC, AIME24, AIME25, GPQA, MMLUpro) on Qwen3 base 1.7B and 4B models, G2RL consistently improves pass@1, maj@16, and pass@k over entropy based GRPO and external embedding methods. Analyzing the induced geometry, we find that G2RL expands exploration into substantially more orthogonal and often opposing gradient directions while maintaining semantic coherence, revealing that a policy own update space provides a far more faithful and effective basis for guiding exploration in large language model reinforcement learning.

