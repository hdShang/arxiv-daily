---
layout: default
title: "Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning"
---

# Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14684" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14684v3</a>
  <a href="https://arxiv.org/pdf/2505.14684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14684v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14684v3', 'Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haolei Xu, Yuchen Yan, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Shengpei Jiang, Kaitao Song, Weiming Lu, Jun Xiao, Yueting Zhuang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-11-27)

**备注**: Accepted to NeurIPS 2025. Camera ready version. Code: https://github.com/ZJU-REAL/Mind-the-Gap Project: https://zju-real.github.io/CoT-Bridge/

---

## 💡 一句话要点

**提出CoT思想跃迁桥接任务以解决数学推理中的中间步骤缺失问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式推理` `思想跃迁` `数学推理` `模型微调` `数据集构建` `自动推理` `深度学习`

## 📋 核心要点

1. 现有的数学CoT数据集因专家省略中间步骤而导致思想跃迁，影响模型的学习效果和泛化能力。
2. 本文提出CoT思想跃迁桥接任务，自动检测并生成缺失的中间推理步骤，以恢复推理的完整性。
3. 实验结果显示，基于桥接数据集微调的模型在多个基准测试中表现优异，NuminaMath的提升幅度达到5.87%。

## 📝 摘要（中文）

大型语言模型（LLMs）在数学任务中通过链式推理（CoT）取得了显著进展。然而，现有的数学CoT数据集常因专家省略中间步骤而导致思想跃迁，这对模型的学习和泛化产生负面影响。为此，本文提出了CoT思想跃迁桥接任务，旨在自动检测跃迁并生成缺失的中间推理步骤，以恢复CoT的完整性和连贯性。我们基于结构化的ScaleQuestMath数据集构建了专门的训练数据集ScaleQM+，并训练了CoT-Bridge以桥接思想跃迁。通过对数学推理基准的全面实验，我们证明了在桥接数据集上微调的模型在性能上始终优于原始数据集训练的模型，NuminaMath的提升幅度高达5.87%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学推理模型在训练中因中间步骤缺失而导致的思想跃迁问题。现有方法在数据集构建时常常省略关键的推理步骤，导致模型学习不完整，影响其泛化能力。

**核心思路**：论文提出了CoT思想跃迁桥接任务，通过自动检测思想跃迁并生成缺失的推理步骤，来恢复推理过程的完整性和连贯性。这种设计旨在提升模型的学习效果和推理能力。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。首先，构建专门的ScaleQM+数据集；其次，训练CoT-Bridge模型以桥接思想跃迁；最后，通过综合实验评估模型在数学推理任务中的表现。

**关键创新**：最重要的技术创新在于提出了CoT思想跃迁桥接任务，并构建了专门的数据集来支持这一任务。这与现有方法的本质区别在于，现有方法往往忽视中间步骤，而本研究则强调其重要性。

**关键设计**：在模型训练中，采用了特定的损失函数以优化推理步骤的生成质量，并设计了适应性强的网络结构，以便于与现有优化技术兼容。

## 📊 实验亮点

实验结果显示，基于桥接数据集微调的模型在NuminaMath基准上提升幅度高达5.87%，在蒸馏数据上提升3.02%，并为强化学习提供了更好的起始点，提升幅度为3.1%。这些结果表明，增强推理完整性能够带来广泛的应用收益。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能问答等。通过提升模型的推理完整性，能够在更广泛的逻辑推理任务中应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress on mathematical tasks through Chain-of-Thought (CoT) reasoning. However, existing mathematical CoT datasets often suffer from Thought Leaps due to experts omitting intermediate steps, which negatively impacts model learning and generalization. We propose the CoT Thought Leap Bridge Task, which aims to automatically detect leaps and generate missing intermediate reasoning steps to restore the completeness and coherence of CoT. To facilitate this, we constructed a specialized training dataset called ScaleQM+, based on the structured ScaleQuestMath dataset, and trained CoT-Bridge to bridge thought leaps. Through comprehensive experiments on mathematical reasoning benchmarks, we demonstrate that models fine-tuned on bridged datasets consistently outperform those trained on original datasets, with improvements of up to +5.87% on NuminaMath. Our approach effectively enhances distilled data (+3.02%) and provides better starting points for reinforcement learning (+3.1%), functioning as a plug-and-play module compatible with existing optimization techniques. Furthermore, CoT-Bridge demonstrate improved generalization to out-of-domain logical reasoning tasks, confirming that enhancing reasoning completeness yields broadly applicable benefits.

