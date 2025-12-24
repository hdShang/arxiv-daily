---
layout: default
title: "VRPRM: Process Reward Modeling via Visual Reasoning"
---

# VRPRM: Process Reward Modeling via Visual Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03556" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03556v2</a>
  <a href="https://arxiv.org/pdf/2508.03556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03556v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03556v2', 'VRPRM: Process Reward Modeling via Visual Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinquan Chen, Bangwei Liu, Xuhong Wang, Yingchun Wang, Chaochao Lu

**分类**: cs.LG

**发布日期**: 2025-08-05 (更新: 2025-08-28)

**备注**: 13 pages, 5 figures

---

## 💡 一句话要点

**提出VRPRM以解决PRM在长远推理中的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `过程奖励模型` `视觉推理` `长远推理` `链式思维` `强化学习`

## 📋 核心要点

1. 现有的过程奖励模型（PRM）在长远推理和深度思考能力上存在明显不足，限制了其应用效果。
2. 本文提出VRPRM，通过视觉推理来增强PRM的推理能力，并设计了高效的两阶段训练策略以降低数据标注成本。
3. 实验结果显示，VRPRM在使用较少数据的情况下，性能显著提升，证明了其在数据利用效率上的优势。

## 📝 摘要（中文）

过程奖励模型（PRM）在大语言模型（LLM）的后训练中广泛应用，能够对生成内容的推理步骤进行细致评估。然而，大多数PRM缺乏长远推理和深度思考能力。虽然已有少数研究尝试将链式思维能力引入PRM，但CoT-PRM数据的标注成本过高，难以在各种任务中发挥稳定作用。为了解决这些挑战，本文提出了VRPRM，通过视觉推理进行过程奖励建模，并设计了一种高效的两阶段训练策略。实验结果表明，使用仅3.6K的CoT-PRM SFT数据和50K的非CoT PRM RL训练数据，VRPRM的性能超越了数据量达到400K的非思考PRM，在BoN实验中相较基础模型实现了高达118%的相对性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有过程奖励模型（PRM）在长远推理和深度思考能力不足的问题。现有方法在处理复杂推理任务时表现不佳，且数据标注成本高昂。

**核心思路**：论文提出的VRPRM通过引入视觉推理的机制，增强了PRM的推理能力。通过设计高效的两阶段训练策略，降低了对大量标注数据的依赖，提升了模型的推理质量。

**技术框架**：VRPRM的整体架构分为两个主要阶段：第一阶段为使用少量的CoT-PRM SFT数据进行初步训练，第二阶段则利用大量的非CoT PRM RL数据进行强化学习，以进一步提升模型性能。

**关键创新**：VRPRM的核心创新在于结合视觉推理与过程奖励建模，突破了传统PRM在推理深度和长远思考上的局限。这种结合使得模型在处理复杂任务时表现出更强的适应性和准确性。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡推理质量与数据利用效率，同时在网络结构上进行了优化，以适应视觉信息的处理需求。

## 📊 实验亮点

实验结果表明，VRPRM在仅使用3.6K的CoT-PRM SFT数据和50K的非CoT PRM RL训练数据的情况下，性能超越了数据量达到400K的非思考PRM。在BoN实验中，VRPRM实现了高达118%的相对性能提升，显示出其在数据利用效率和推理能力上的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和机器人决策等。通过提升过程奖励模型的推理能力，VRPRM能够在更复杂的任务中提供更高质量的输出，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Process Reward Model (PRM) is widely used in the post-training of Large Language Model (LLM) because it can perform fine-grained evaluation of the reasoning steps of generated content. However, most PRMs lack long-term reasoning and deep thinking capabilities. On the other hand, although a few works have tried to introduce Chain-of-Thought capability into PRMs, the annotation cost of CoT-PRM data is too expensive to play a stable role in various tasks. To address the above challenges, we propose VRPRM, a process reward model via visual reasoning, and design an efficient two-stage training strategy. Experimental results show that using only 3.6K CoT-PRM SFT data and 50K non-CoT PRM RL training data, VRPRM can surpass the non-thinking PRM with a total data volume of 400K and achieved a relative performance improvement of up to 118\% over the base model in the BoN experiment. This result confirms that the proposed combined training strategy can achieve higher quality reasoning capabilities at a lower data annotation cost, thus providing a new paradigm for PRM training with more efficient data utilization.

