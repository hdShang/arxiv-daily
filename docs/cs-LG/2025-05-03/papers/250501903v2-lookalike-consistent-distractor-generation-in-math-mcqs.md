---
layout: default
title: LookAlike: Consistent Distractor Generation in Math MCQs
---

# LookAlike: Consistent Distractor Generation in Math MCQs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01903" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01903v2</a>
  <a href="https://arxiv.org/pdf/2505.01903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01903v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01903v2', 'LookAlike: Consistent Distractor Generation in Math MCQs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nisarg Parikh, Nigel Fernandez, Alexander Scarlatos, Simon Woodhead, Andrew Lan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-03 (更新: 2025-06-07)

---

## 💡 一句话要点

**提出LookAlike以解决数学选择题干扰项生成一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学教育` `多项选择题` `干扰项生成` `偏好优化` `模型不一致性` `教育技术` `智能辅导系统`

## 📋 核心要点

1. 现有方法在生成数学选择题的干扰项时，难以确保与学生常见错误的一致性，影响了教育效果。
2. 本文提出LookAlike，通过挖掘模型不一致性生成偏好对，并结合监督微调与直接偏好优化，提升干扰项生成的准确性。
3. 在对1400多个数学MCQs的评估中，LookAlike在干扰项和错误生成的准确率上分别达到了51.6%和57.2%，显著优于现有方法。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成多项选择题（MCQs）的干扰项方面应用日益广泛，尤其是在数学教育领域。然而，现有方法在确保生成的干扰项与常见学生错误一致性方面存在局限。本文提出LookAlike，通过偏好优化提高错误与干扰项的一致性。我们的两项主要创新是：从模型不一致性中挖掘合成偏好对，以及交替使用监督微调（SFT）与直接偏好优化（DPO）来稳定训练。与依赖启发式或手动标注偏好数据的先前工作不同，LookAlike利用自身生成的不一致性作为不偏好样本，从而实现可扩展和稳定的训练。在对1400多个数学MCQs的真实数据集进行评估时，LookAlike在干扰项生成中取得了51.6%的准确率，在错误生成中取得了57.2%的准确率，超越了现有的最先进方法（45.6% / 47.7%）。这些改进突显了基于偏好的正则化和不一致性挖掘在大规模生成一致的数学MCQ干扰项方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在生成数学选择题干扰项时，无法确保与学生常见错误一致性的问题。现有方法多依赖启发式或手动标注数据，缺乏可扩展性和稳定性。

**核心思路**：LookAlike通过挖掘模型生成的不一致性，形成合成偏好对，并结合监督微调与直接偏好优化，旨在提高干扰项生成的准确性和一致性。

**技术框架**：整体架构包括两个主要阶段：首先，利用模型的不一致性生成偏好对；其次，交替进行监督微调和直接偏好优化，以稳定训练过程。

**关键创新**：最重要的创新在于利用自身生成的不一致性作为不偏好样本，避免了对手动标注数据的依赖，从而实现了更高的训练效率和准确性。

**关键设计**：在训练过程中，采用了特定的损失函数来优化偏好对的生成，并设计了适合的网络结构以支持高效的训练和推理。

## 📊 实验亮点

实验结果显示，LookAlike在干扰项生成的准确率上达到了51.6%，在错误生成中达到了57.2%，相比现有最先进方法（45.6% / 47.7%）有显著提升，验证了偏好优化和不一致性挖掘的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和在线学习平台。通过生成更一致的干扰项，能够提升学生的学习体验和评估效果，未来可能在其他学科的MCQs生成中也具有广泛的应用价值。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used to generate distractors for multiple-choice questions (MCQs), especially in domains like math education. However, existing approaches are limited in ensuring that the generated distractors are consistent with common student errors. We propose LookAlike, a method that improves error-distractor consistency via preference optimization. Our two main innovations are: (a) mining synthetic preference pairs from model inconsistencies, and (b) alternating supervised fine-tuning (SFT) with Direct Preference Optimization (DPO) to stabilize training. Unlike prior work that relies on heuristics or manually annotated preference data, LookAlike uses its own generation inconsistencies as dispreferred samples, thus enabling scalable and stable training. Evaluated on a real-world dataset of 1,400+ math MCQs, LookAlike achieves 51.6% accuracy in distractor generation and 57.2% in error generation under LLM-as-a-judge evaluation, outperforming an existing state-of-the-art method (45.6% / 47.7%). These improvements highlight the effectiveness of preference-based regularization and inconsistency mining for generating consistent math MCQ distractors at scale.

