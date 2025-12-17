---
layout: default
title: Explainable reinforcement learning from human feedback to improve alignment
---

# Explainable reinforcement learning from human feedback to improve alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13837" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13837</a>
  <a href="https://arxiv.org/pdf/2512.13837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13837" onclick="toggleFavorite(this, '2512.13837', 'Explainable reinforcement learning from human feedback to improve alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shicheng Liu, Siyuan Xu, Wenjie Qiu, Hangfan Zhang, Minghui Zhu

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于人类反馈的可解释强化学习方法，提升语言模型对齐效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可解释强化学习` `人类反馈` `语言模型对齐` `事后解释` `非学习`

## 📋 核心要点

1. 现有RLHF调优的语言模型仍可能产生不理想的回复，缺乏有效改进机制。
2. 提出一种可解释的RLHF方法，通过识别并纠正导致不良回复的训练数据来优化模型。
3. 实验结果表明，该方法能够有效改进RLHF，提升语言模型的对齐效果。

## 📝 摘要（中文）

本文研究了如何将人类改进策略应用于从人类反馈中进行强化学习(RLHF)，以提升语言模型(LM)的对齐效果。观察到RLHF调优的LM仍然会产生不令人满意的回复。本文提出一种通过纠正原因来改进这些回复的方法。该方法包含两部分：首先，提出一种事后解释方法，通过识别导致不满意回复的训练数据来解释其生成原因。这被建模为一个约束组合优化问题，目标是在特征表示空间中找到与提示-回复对最接近的训练数据集，约束是提示-回复对可以分解为该数据集在特征空间中的凸组合。提出了一种高效的迭代数据选择算法来解决这个问题。其次，提出一种非学习方法，通过非学习导致这些不满意回复的训练数据来改进某些提示的不满意回复，同时不会显著降低其他提示的满意回复。实验结果表明，该算法可以改进RLHF。

## 🔬 方法详解

**问题定义**：论文旨在解决RLHF训练的语言模型仍然会生成不令人满意的回复的问题。现有方法缺乏对不良回复原因的解释，难以针对性地进行改进。因此，如何找到导致不良回复的根本原因，并在此基础上进行优化，是本文要解决的关键问题。

**核心思路**：论文的核心思路是模仿人类改进问题的方式：首先找到问题的原因，然后纠正原因。具体而言，对于语言模型生成的不良回复，首先通过可解释性方法找到导致该回复的训练数据，然后通过“非学习”这些数据来改进模型，使其不再生成类似的不良回复。

**技术框架**：该方法包含两个主要模块：1) **事后解释模块**：该模块的目标是找到导致不良回复的训练数据。它将该问题建模为一个约束组合优化问题，目标是在特征空间中找到与当前提示-回复对最接近的训练数据子集，约束是该提示-回复对可以表示为该子集的凸组合。使用迭代数据选择算法来解决该优化问题。2) **非学习模块**：该模块的目标是通过“非学习”导致不良回复的训练数据来改进模型。该模块在更新模型参数时，会降低这些训练数据的影响，从而减少模型生成类似不良回复的可能性。

**关键创新**：该方法最重要的创新点在于将可解释性引入RLHF，通过解释不良回复的原因，从而能够针对性地进行改进。与传统的RLHF方法相比，该方法不仅关注模型的整体性能，还关注模型在特定情况下的表现，并能够通过纠正错误的原因来提升性能。

**关键设计**：在事后解释模块中，关键的设计包括：1) 特征表示空间的选择，需要能够有效捕捉提示和回复之间的语义关系。2) 约束组合优化问题的定义，需要保证找到的训练数据子集能够合理地解释当前提示-回复对。3) 迭代数据选择算法的设计，需要保证算法的效率和准确性。在非学习模块中，关键的设计包括：1) 如何确定需要“非学习”的训练数据。2) 如何在更新模型参数时降低这些数据的影响，同时避免对其他数据的性能产生负面影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13837/post_training_structure.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13837/explanation_example.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13837/dialogue_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该算法能够有效改进RLHF，提升语言模型的对齐效果。具体而言，通过“非学习”导致不良回复的训练数据，模型在生成类似回复的可能性显著降低，同时对其他回复的性能影响较小。具体的性能提升数据在论文中给出，与基线方法相比，该方法在特定指标上取得了显著的提升。

## 🎯 应用场景

该研究成果可应用于各种需要从人类反馈中进行学习的语言模型应用场景，例如对话系统、文本生成、代码生成等。通过提升模型对齐效果，可以提高用户满意度，减少模型产生有害或不当回复的风险。未来，该方法可以扩展到其他类型的机器学习模型，并应用于更广泛的领域。

## 📄 摘要（原文）

> A common and effective strategy for humans to improve an unsatisfactory outcome in daily life is to find a cause of this outcome and correct the cause. In this paper, we investigate whether this human improvement strategy can be applied to improving reinforcement learning from human feedback (RLHF) for alignment of language models (LMs). In particular, it is observed in the literature that LMs tuned by RLHF can still output unsatisfactory responses. This paper proposes a method to improve the unsatisfactory responses by correcting their causes. Our method has two parts. The first part proposes a post-hoc explanation method to explain why an unsatisfactory response is generated to a prompt by identifying the training data that lead to this response. We formulate this problem as a constrained combinatorial optimization problem where the objective is to find a set of training data closest to this prompt-response pair in a feature representation space, and the constraint is that the prompt-response pair can be decomposed as a convex combination of this set of training data in the feature space. We propose an efficient iterative data selection algorithm to solve this problem. The second part proposes an unlearning method that improves unsatisfactory responses to some prompts by unlearning the training data that lead to these unsatisfactory responses and, meanwhile, does not significantly degrade satisfactory responses to other prompts. Experimental results demonstrate that our algorithm can improve RLHF.

