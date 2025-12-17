---
layout: default
title: Why Reinforcement Fine-Tuning Enables MLLMs Preserve Prior Knowledge Better: A Data Perspective
---

# Why Reinforcement Fine-Tuning Enables MLLMs Preserve Prior Knowledge Better: A Data Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23508" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23508</a>
  <a href="https://arxiv.org/pdf/2506.23508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23508" onclick="toggleFavorite(this, '2506.23508', 'Why Reinforcement Fine-Tuning Enables MLLMs Preserve Prior Knowledge Better: A Data Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Zhang, Qiaole Dong, Qi Zhang, Jun Zhao, Enyu Zhou, Zhiheng Xi, Senjie Jin, Xiaoran Fan, Yuhao Zhou, Mingqi Wu, Yanwei Fu, Tao Ji, Tao Gui, Xuanjing Huang, Kai Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**研究表明强化微调(RFT)通过数据分布优化，能更好保持多模态大语言模型的先验知识。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `强化微调` `监督微调` `灾难性遗忘` `持续学习` `数据分布` `先验知识` `拼图游戏`

## 📋 核心要点

1. 多模态大语言模型微调面临任务适配与先验知识保持的难题，SFT易遗忘，RFT学习慢。
2. 论文核心在于分析SFT和RFT训练数据对先验知识的影响，揭示数据分布是关键因素。
3. 实验表明，RFT模拟数据能使SFT在快速学习新任务的同时，更好地保持先验知识。

## 📝 摘要（中文）

监督微调(SFT)和强化微调(RFT)等后训练算法被广泛用于将多模态大语言模型适配到下游任务。虽然它们在任务适配方面很有效，但它们对先验知识的影响仍不清楚。本文引入了拼图游戏作为现有预训练语料库中不存在的新任务，并系统地研究了SFT和RFT在开源多模态模型Qwen2.5-VL系列上的行为。实验揭示了一个明显的权衡：SFT能够快速获取任务，但会导致灾难性遗忘，而RFT学习速度较慢，但能保持先验知识。通过检查训练数据如何影响先验知识的大小和方向，研究了学习动态。分析表明，RFT主要强化与基础模型的概率分布自然对齐的正确样本，从而减少对先验知识的干扰。此外，在RFT模拟的rollout上进行训练，这些rollout对先验知识的影响较小，并且在方向上与先验知识良好对齐，这使得SFT能够在快速学习新任务的同时更好地保持先验知识。这些发现表明，训练数据的分布，而不是算法差异，在遗忘中起着核心作用，并突出了RFT在多模态大语言模型中稳定持续学习的潜力。

## 🔬 方法详解

**问题定义**：多模态大语言模型在进行下游任务微调时，如何在快速适应新任务的同时，避免灾难性遗忘，保持模型原有的先验知识？现有方法如SFT虽然能快速学习新任务，但容易导致对原有知识的遗忘，而RFT虽然能较好地保持先验知识，但学习速度较慢。

**核心思路**：论文的核心思路是通过分析SFT和RFT训练数据的分布特性，以及这些数据对模型先验知识的影响，来理解为什么RFT能更好地保持先验知识。作者认为，训练数据的分布，特别是数据对模型参数更新的方向和大小，是导致遗忘现象的关键因素。

**技术框架**：论文主要通过实验分析来研究SFT和RFT的行为。首先，作者设计了一个新的拼图游戏任务，该任务在现有的预训练语料库中不存在，用于评估模型在学习新任务时的表现。然后，作者使用Qwen2.5-VL系列模型，分别进行SFT和RFT训练，并分析训练过程中模型参数的变化，以及模型对先验知识的保持程度。最后，作者通过模拟RFT的rollout数据，并使用这些数据进行SFT训练，观察模型在保持先验知识方面的表现。

**关键创新**：论文的关键创新在于从数据分布的角度解释了RFT能够更好保持先验知识的原因。作者发现，RFT训练数据倾向于强化与模型原有知识对齐的样本，从而减少了对原有知识的干扰。此外，作者还发现，使用RFT模拟的rollout数据进行SFT训练，可以使模型在快速学习新任务的同时，更好地保持先验知识。

**关键设计**：论文的关键设计包括：1) 使用拼图游戏作为评估模型学习新任务和保持先验知识的基准；2) 分析训练数据对模型参数更新的方向和大小，以理解数据对先验知识的影响；3) 通过模拟RFT的rollout数据，并使用这些数据进行SFT训练，来验证数据分布对模型性能的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23508/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23508/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23508/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RFT在学习新任务时，能够更好地保持先验知识，而SFT则容易导致灾难性遗忘。更重要的是，使用RFT模拟的rollout数据进行SFT训练，可以使模型在快速学习新任务的同时，显著提高先验知识的保持能力，验证了数据分布在模型学习过程中的重要作用。

## 🎯 应用场景

该研究成果可应用于多模态大语言模型的持续学习和终身学习场景，例如在机器人、智能助手等领域，模型需要不断学习新的技能，同时保持已有的知识。通过优化训练数据的分布，可以提高模型在持续学习过程中的稳定性和可靠性，避免灾难性遗忘。

## 📄 摘要（原文）

> Post-training algorithms such as Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT) are widely used to adapt multimodal large language models to downstream tasks. While effective at task adaptation, their impact on prior knowledge remains unclear. In this paper, we introduce jigsaw puzzles as a novel task absent from existing pretraining corpora and systematically study the behavior of SFT and RFT on open-source multimodal model, Qwen2.5-VL series. Our experiments reveal a sharp trade-off: SFT enables rapid task acquisition but leads to catastrophic forgetting, whereas RFT learns more slowly but maintains prior knowledge. We study this phenomenon through learning dynamics by examining both the magnitude and direction of how training data influence prior knowledge. Our analysis shows that RFT mainly reinforces correct samples naturally aligned with the base model's probability landscape, leading to weaker interference with prior knowledge. Moreover, training on RFT-simulated rollouts, which exert a small magnitude of influence and are well aligned in direction to prior knowledge, allows SFT to preserve prior knowledge better while rapidly learning new tasks. These findings suggest that distribution of training data, rather than algorithmic differences, plays a central role in forgetting, and highlight RFT's potential for stable continual learning in multimodal large language models.

