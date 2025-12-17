---
layout: default
title: Mitigating Catastrophic Forgetting in Mathematical Reasoning Finetuning through Mixed Training
---

# Mitigating Catastrophic Forgetting in Mathematical Reasoning Finetuning through Mixed Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13706" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13706</a>
  <a href="https://arxiv.org/pdf/2512.13706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13706" onclick="toggleFavorite(this, '2512.13706', 'Mitigating Catastrophic Forgetting in Mathematical Reasoning Finetuning through Mixed Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: John Graham Reynolds

**分类**: cs.LG, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出混合训练策略，缓解数学推理微调中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `灾难性遗忘` `混合训练` `数学推理` `自然语言推理` `微调` `大型语言模型` `正则化`

## 📋 核心要点

1. 现有方法在微调大型语言模型进行数学推理时，会发生灾难性遗忘，导致模型失去原有的通用能力。
2. 论文提出混合训练策略，通过交错使用数学和NLI数据进行训练，以缓解灾难性遗忘问题。
3. 实验结果表明，混合训练能够完全消除灾难性遗忘，同时保持甚至提升数学推理性能。

## 📝 摘要（中文）

在对大型语言模型进行微调以执行诸如数学推理等特定任务时，模型会表现出灾难性遗忘，从而失去先前学习的能力。本文通过在DeepMind Mathematics数据集上微调Flan-T5-Base（2.5亿参数）并测量其在MultiNLI上的遗忘程度来研究这个问题。仅使用数学数据进行训练将数学准确率从3.1％提高到12.0％，但导致NLI准确率从81.0％下降到16.5％——在最初的1000个训练步骤中下降了64.5个百分点。为此，本文提出了一种混合训练策略，在训练过程中交错使用数学和NLI示例。结果表明，混合训练完全消除了灾难性遗忘，同时保持了相当的数学性能：平衡的1:1比例实现了12.0％的数学准确率（与仅数学训练相当），同时保持了86.2％的NLI准确率。系统地探索了从1:1到15:1的混合比例，发现即使是最小的NLI暴露（6.2％）也能提供有效的正则化。这些发现表明，专业化不需要以牺牲通用能力为代价，这对于扩展到更大的模型具有重要意义，在更大的模型中，混合训练除了防止遗忘之外，还可以带来额外的好处。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在微调以执行特定任务（如数学推理）时出现的灾难性遗忘问题。现有方法在专注于特定任务训练时，会显著降低模型在通用任务上的性能，限制了模型的泛化能力。

**核心思路**：核心思路是在微调过程中，同时使用特定任务（数学推理）的数据和通用任务（NLI）的数据进行混合训练。通过这种方式，模型可以在学习新知识的同时，保留已有的通用能力，从而缓解灾难性遗忘。

**技术框架**：整体框架包括：1）选择预训练语言模型（Flan-T5-Base）；2）构建数学推理数据集（DeepMind Mathematics）和自然语言推理数据集（MultiNLI）；3）设计混合训练策略，即在每个训练批次中，按照一定的比例混合数学推理和NLI数据；4）评估模型在数学推理和NLI任务上的性能，以衡量灾难性遗忘的程度。

**关键创新**：关键创新在于混合训练策略本身。与传统的仅使用特定任务数据进行微调的方法不同，该方法通过引入通用任务数据，实现了对模型参数的正则化，从而防止模型过度拟合特定任务，保留了通用能力。

**关键设计**：关键设计包括：1）混合比例的选择：论文系统地探索了从1:1到15:1的混合比例，以找到最佳的平衡点；2）数据集的选择：选择了DeepMind Mathematics作为数学推理数据集，MultiNLI作为自然语言推理数据集，这两个数据集分别代表了特定任务和通用任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13706/figures/training_dynamics_dual.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13706/figures/pareto_frontier.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，混合训练能够完全消除灾难性遗忘，同时保持甚至提升数学推理性能。例如，使用1:1的混合比例进行训练，数学准确率达到12.0%（与仅数学训练相当），同时NLI准确率保持在86.2%，显著优于仅使用数学数据训练的模型（NLI准确率仅为16.5%）。即使是最小的NLI暴露（6.2%），也能提供有效的正则化。

## 🎯 应用场景

该研究成果可应用于各种需要对大型语言模型进行微调的场景，例如特定领域的问答系统、代码生成、文本摘要等。通过混合训练，可以避免模型在学习新知识的同时忘记原有能力，从而提高模型的泛化性和实用性。该方法对于开发更强大、更可靠的AI系统具有重要意义。

## 📄 摘要（原文）

> When finetuning large language models for specialized tasks such as mathematical reasoning, models exhibit catastrophic forgetting, losing previously learned capabilities. We investigate this by finetuning Flan-T5-Base (250M parameters) on the DeepMind Mathematics dataset and measuring forgetting on MultiNLI. Math-only training improves mathematical accuracy from 3.1\% to 12.0\% but causes NLI accuracy to collapse from 81.0\% to 16.5\%--a 64.5 percentage point drop occurring within the first 1,000 training steps. We propose mixed training strategies that interleave mathematical and NLI examples during training. Our results demonstrate that mixed training completely eliminates catastrophic forgetting while maintaining equivalent mathematical performance: the balanced 1:1 ratio achieves 12.0\% math accuracy (matching math-only) while preserving 86.2\% NLI accuracy. We systematically explore mixing ratios from 1:1 to 15:1, finding that even minimal NLI exposure (6.2\%) provides effective regularization. These findings demonstrate that specialization need not require forgetting general capabilities, with implications for scaling to larger models where mixed training may confer additional benefits beyond forgetting prevention.

