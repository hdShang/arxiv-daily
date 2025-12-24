---
layout: default
title: REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Large Reasoning Models
---

# REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19862v1</a>
  <a href="https://arxiv.org/pdf/2505.19862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19862v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19862v1', 'REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hexuan Deng, Wenxiang Jiao, Xuebo Liu, Jun Rao, Min Zhang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-26

**备注**: Work in Progress

**🔗 代码/项目**: [GITHUB](https://github.com/hexuandeng/REA-RL)

---

## 💡 一句话要点

**提出REA-RL以解决大型推理模型的高推理成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `大型推理模型` `在线强化学习` `反思机制` `推理效率` `深度学习`

## 📋 核心要点

1. 现有方法在处理大型推理模型时，面临推理成本高和反思能力不足的挑战。
2. 本文提出REA-RL，通过引入小型反思模型，实现在线训练的高效扩展，结合并行采样与顺序修正。
3. 实验结果表明，REA-RL在保持性能的同时，推理成本降低了35%，有效提升了推理效率。

## 📝 摘要（中文）

大型推理模型（LRMs）在复杂任务中表现出色，但常常面临过度思考的问题，导致推理成本显著增加。现有方法通过合成较短的推理响应来进行学习，但在在线使用时效率低下。在线强化学习主要采用长度奖励来鼓励短推理响应，但容易失去反思能力，影响性能。为了解决这些问题，本文提出了REA-RL，引入了小型反思模型以实现在线训练的高效扩展，提供并行采样和顺序修正。此外，设计了反思奖励，以进一步防止LRMs偏向短而缺乏反思的响应。实验表明，这两种方法在显著提高推理效率的同时，保持或增强了性能。它们的结合在性能和效率之间达成了良好的平衡，推理成本降低了35%，而性能未受损。进一步分析显示，我们的方法在处理困难问题时有效保持反思频率，而在简单问题中适当降低反思频率，且不丧失反思能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在推理过程中面临的高成本和反思能力不足的问题。现有方法虽然能合成短响应，但在在线使用时效率低下，且容易导致反思能力的丧失。

**核心思路**：REA-RL的核心思路是引入一个小型反思模型，以实现在线训练的高效扩展。通过并行采样和顺序修正，确保模型在生成短响应的同时，仍能保持反思能力。

**技术框架**：该方法的整体架构包括反思模型和主推理模型。反思模型负责生成反思奖励，主推理模型则在此基础上进行推理响应的生成。整个流程包括数据采样、反思奖励计算和推理响应生成三个主要阶段。

**关键创新**：最重要的技术创新点在于引入反思奖励机制，旨在防止模型偏向短而缺乏深度的响应。这一设计与现有方法的本质区别在于，强调了反思能力的重要性，而不仅仅是响应的长度。

**关键设计**：在参数设置上，反思模型的结构经过优化，以确保其在生成反思奖励时的有效性。损失函数设计上，结合了反思奖励与传统的长度奖励，以平衡推理效率与反思能力。

## 📊 实验亮点

实验结果显示，REA-RL在推理效率上显著提升，推理成本降低了35%，同时保持或增强了模型性能。这一结果与基线方法相比，展示了明显的优势，证明了反思奖励机制的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动化决策支持等。通过提高大型推理模型的推理效率，REA-RL能够在实际应用中降低计算成本，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) demonstrate strong performance in complex tasks but often face the challenge of overthinking, leading to substantially high inference costs. Existing approaches synthesize shorter reasoning responses for LRMs to learn, but are inefficient for online usage due to the time-consuming data generation and filtering processes. Meanwhile, online reinforcement learning mainly adopts a length reward to encourage short reasoning responses, but tends to lose the reflection ability and harm the performance. To address these issues, we propose REA-RL, which introduces a small reflection model for efficient scaling in online training, offering both parallel sampling and sequential revision. Besides, a reflection reward is designed to further prevent LRMs from favoring short yet non-reflective responses. Experiments show that both methods maintain or enhance performance while significantly improving inference efficiency. Their combination achieves a good balance between performance and efficiency, reducing inference costs by 35% without compromising performance. Further analysis demonstrates that our methods are effective by maintaining reflection frequency for hard problems while appropriately reducing it for simpler ones without losing reflection ability. Codes are available at https://github.com/hexuandeng/REA-RL.

