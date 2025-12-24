---
layout: default
title: "Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training"
---

# Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25758" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25758v1</a>
  <a href="https://arxiv.org/pdf/2509.25758.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25758v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25758v1', 'Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yein Park, Minbyul Jeong, Jaewoo Kang

**分类**: cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**揭示推理模型后训练中涌现的注意力头及其对复杂推理的影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `大型语言模型` `后训练` `电路分析` `注意力机制` `推理能力` `监督微调` `强化学习` `模型蒸馏`

## 📋 核心要点

1. 现有大型推理模型缺乏对其后训练改进机制的深入理解，阻碍了模型优化。
2. 通过电路分析，揭示后训练过程中涌现出功能专用的注意力头，支持结构化推理。
3. 研究发现不同训练方法（SFT、蒸馏、强化学习）导致注意力头演化方式不同，并影响性能。

## 📝 摘要（中文）

现代大型推理模型的能力主要通过监督微调和强化学习等后训练技术解锁。然而，这些改进背后的架构机制在很大程度上仍然不透明。本文利用电路分析表明，复杂推理的后训练会激发新型、功能专用的注意力头的涌现。这些注意力头共同支持结构化推理和计算。通过对Qwen系列和DeepSeek-distilled模型的比较分析，揭示了这些涌现的注意力头在不同训练机制下以不同的方式演化。蒸馏和SFT促进了稳定推理头的累积增加。相比之下，群体相对策略优化以动态搜索模式运行：相对较少的注意力头被迭代激活、评估和修剪，它们的存活与任务奖励信号的波动密切相关。此外，可控的think on/off模型不具备专用的思考头。相反，关闭显式推理会触发更广泛但效率较低的补偿头集合。通过消融和定性分析，将这些电路层面的动态与一个关键的性能权衡联系起来：强化的注意力头能够为难题提供复杂的解决策略，但也可能引入过度思考的失败模式，例如简单任务上的计算错误或逻辑循环。这些发现将电路层面的动态与宏观层面的性能联系起来，识别出一种固有的张力，即复杂推理的代价是基本计算。更广泛地说，这项工作为训练策略设计指明了未来的方向，强调需要平衡有效推理策略的开发与可靠、完美执行的保证。

## 🔬 方法详解

**问题定义**：论文旨在解决大型推理模型在后训练阶段能力提升的机制不明确的问题。现有方法难以解释模型内部结构如何支持复杂推理，以及不同训练策略如何影响模型性能。这种不透明性阻碍了对模型行为的理解和进一步优化。

**核心思路**：论文的核心思路是通过电路分析方法，研究模型内部注意力头的行为，揭示在后训练过程中涌现的、功能专用的注意力头。通过比较不同训练策略（如监督微调、蒸馏、强化学习）下注意力头的演化模式，理解不同训练方法对模型推理能力的影响。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 选择Qwen系列和DeepSeek-distilled模型作为研究对象。2) 使用电路分析技术，识别模型中涌现的注意力头。3) 对比不同训练策略（SFT、蒸馏、强化学习）下注意力头的演化模式。4) 通过消融实验和定性分析，研究注意力头对模型性能的影响，特别是复杂推理和简单计算之间的权衡。

**关键创新**：论文最重要的技术创新点在于：1) 首次使用电路分析方法研究大型推理模型后训练阶段的内部机制。2) 揭示了在后训练过程中涌现的功能专用的注意力头，并阐明了它们在结构化推理中的作用。3) 发现了不同训练策略对注意力头演化的不同影响，以及由此带来的性能权衡。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的Qwen系列和DeepSeek-distilled模型，保证研究结果的泛化性。2) 使用消融实验，验证特定注意力头对模型性能的关键作用。3) 通过定性分析，深入理解注意力头在不同任务中的行为模式。4) 关注复杂推理和简单计算之间的性能权衡，揭示模型优化的潜在挑战。

## 📊 实验亮点

研究发现，蒸馏和SFT训练促进了稳定推理头的累积增加，而群体相对策略优化则采用动态搜索模式，迭代激活、评估和修剪注意力头。可控的think on/off模型不具备专用的思考头，关闭显式推理会触发更广泛但效率较低的补偿头集合。强化后的注意力头虽然能解决难题，但也可能导致简单任务上的计算错误或逻辑循环。

## 🎯 应用场景

该研究成果可应用于改进大型语言模型的训练策略，例如通过有针对性地训练特定类型的注意力头来提升模型的推理能力。此外，该研究有助于开发更可靠、更高效的推理模型，应用于智能问答、自动编程、科学研究等领域。未来的研究可以探索如何平衡复杂推理和简单计算，避免模型在简单任务上出现过度思考的错误。

## 📄 摘要（原文）

> The remarkable capabilities of modern large reasoning models are largely unlocked through post-training techniques such as supervised fine-tuning and reinforcement learning. However, the architectural mechanisms behind such improvements remain largely opaque. In this work, we use circuit analysis to demonstrate that post-training for complex reasoning sparks the emergence of novel, functionally specialized attention heads. These heads collectively support structured reasoning and computation. Our comparative analysis across Qwen families and DeepSeek-distilled model reveals that these emergent heads evolve differently under different training regimes. Distillation and SFT foster a cumulative addition of stable reasoning heads. In contrast, group relative policy optimization operates in a dynamic search mode: relatively few attention heads are iteratively activated, evaluated, and pruned, with their survival closely tracking fluctuations in the task reward signal. Furthermore, we find that controllable think on/off models do not possess dedicated thinking heads. Instead, turning off explicit reasoning triggers a broader-but less efficient-set of compensatory heads. Through ablation and qualitative analyses, we connect these circuit-level dynamics to a crucial performance trade-off: strengthened heads enable sophisticated problem-solving strategies for difficult problems but can also introduce over-thinking failure modes, such as calculation errors or logical loops on simpler tasks. These findings connect circuit-level dynamics to macro-level performance, identifying an inherent tension where complex reasoning comes at the cost of elementary computations. More broadly, our work points to future directions for training policy design, emphasizing the need to balance the development of effective reasoning strategies with the assurance of reliable, flawless execution.

