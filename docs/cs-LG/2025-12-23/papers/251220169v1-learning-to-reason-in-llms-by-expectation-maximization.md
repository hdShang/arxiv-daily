---
layout: default
title: Learning to Reason in LLMs by Expectation Maximization
---

# Learning to Reason in LLMs by Expectation Maximization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20169" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20169v1</a>
  <a href="https://arxiv.org/pdf/2512.20169.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20169v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20169v1', 'Learning to Reason in LLMs by Expectation Maximization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junghyun Lee, Branislav Kveton, Sunav Choudhary, Subhojyoti Mukherjee, Anup Rao, Ryan A. Rossi, Alexa Siu

**分类**: cs.LG, cs.CL, stat.ML

**发布日期**: 2025-12-23

**备注**: 12 pages, 3 figures, 1 table

---

## 💡 一句话要点

**提出基于期望最大化的LLM推理学习框架，提升复杂推理任务性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理学习` `期望最大化` `隐变量模型` `提示后验采样`

## 📋 核心要点

1. 现有LLM推理方法依赖生成理由再回答，但缺乏对理由生成过程的有效优化。
2. 论文提出基于期望最大化的框架，将推理视为隐变量模型，优化理由生成分布。
3. 实验表明，简单的提示后验采样（PPS）策略在多个数据集上优于其他复杂采样方法。

## 📝 摘要（中文）

本文将大型语言模型（LLM）的推理过程形式化为一个隐变量模型，并推导出一个用于学习推理的期望最大化（EM）目标函数。该视角连接了EM和现代基于奖励的优化方法，并表明主要挑战在于设计一个能够生成合理化正确答案的理由的采样分布。论文实例化并比较了几种采样方案：带预算的拒绝采样、自学推理器（STaR）以及仅保留STaR推理阶段的提示后验采样（PPS）。在Llama和Qwen模型上，对ARC、MMLU和OpenBookQA数据集的实验表明，采样方案可以显著影响学习到的推理模型的准确性。尽管PPS很简单，但观察到它优于其他采样方案。

## 🔬 方法详解

**问题定义**：论文旨在提升大型语言模型在复杂推理任务中的表现。现有方法通常是先让LLM生成一个理由（rationale），然后再根据这个理由给出答案。然而，如何有效地学习和优化理由的生成过程是一个挑战，现有的方法往往缺乏理论基础和有效的优化策略。

**核心思路**：论文的核心思路是将LLM的推理过程建模为一个隐变量模型，其中理由是隐变量，答案是观测变量。然后，利用期望最大化（EM）算法来学习理由的生成分布。EM算法通过迭代E步（期望步）和M步（最大化步）来优化模型参数，从而使得生成的理由能够更好地支持正确的答案。

**技术框架**：整体框架包含两个主要阶段：理由生成阶段和答案预测阶段。在训练过程中，首先使用不同的采样策略（如拒绝采样、STaR、PPS）生成多个理由。然后，根据生成的理由和对应的答案，使用EM算法来更新模型的参数。具体来说，E步计算在给定答案的情况下，每个理由的后验概率；M步则根据后验概率来最大化模型的似然函数。

**关键创新**：论文的关键创新在于将推理过程形式化为隐变量模型，并利用EM算法进行优化。这种方法提供了一个统一的理论框架，可以将不同的理由生成策略纳入其中。此外，论文还提出了提示后验采样（PPS）策略，该策略仅保留STaR的理由生成阶段，避免了STaR中的一些复杂操作，从而提高了效率和性能。

**关键设计**：论文比较了几种不同的采样策略，包括：1) 带预算的拒绝采样：生成多个理由，然后选择能够给出正确答案的理由。2) 自学推理器（STaR）：使用强化学习来优化理由的生成过程。3) 提示后验采样（PPS）：仅使用LLM生成理由，并根据答案的正确性来调整理由的概率。损失函数采用交叉熵损失，用于优化模型的参数。实验中使用了Llama和Qwen等大型语言模型，并在ARC、MMLU和OpenBookQA等数据集上进行了评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20169v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20169v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于期望最大化的学习框架可以显著提升LLM在推理任务中的性能。特别地，简单的提示后验采样（PPS）策略在ARC、MMLU和OpenBookQA数据集上优于其他更复杂的采样策略，例如STaR。这表明，有效的理由生成策略对于提升LLM的推理能力至关重要，并且简单的策略有时也能取得很好的效果。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如智能问答、知识图谱推理、代码生成等。通过提升LLM的推理能力，可以提高这些应用场景的准确性和可靠性。未来，该方法可以进一步扩展到其他类型的推理任务，并与其他技术（如知识图谱、符号推理）相结合，从而构建更加强大的智能系统。

## 📄 摘要（原文）

> Large language models (LLMs) solve reasoning problems by first generating a rationale and then answering. We formalize reasoning as a latent variable model and derive an expectation-maximization (EM) objective for learning to reason. This view connects EM and modern reward-based optimization, and shows that the main challenge lies in designing a sampling distribution that generates rationales that justify correct answers. We instantiate and compare several sampling schemes: rejection sampling with a budget, self-taught reasoner (STaR), and prompt posterior sampling (PPS), which only keeps the rationalization stage of STaR. Our experiments on the ARC, MMLU, and OpenBookQA datasets with the Llama and Qwen models show that the sampling scheme can significantly affect the accuracy of learned reasoning models. Despite its simplicity, we observe that PPS outperforms the other sampling schemes.

