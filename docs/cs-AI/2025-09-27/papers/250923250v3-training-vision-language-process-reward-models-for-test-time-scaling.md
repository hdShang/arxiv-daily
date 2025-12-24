---
layout: default
title: "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned"
---

# Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23250" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23250v3</a>
  <a href="https://arxiv.org/pdf/2509.23250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23250v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23250v3', 'Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brandon Ong, Tej Deep Pala, Vernon Toh, William Chandra Tjhi, Soujanya Poria

**分类**: cs.AI, cs.CV

**发布日期**: 2025-09-27 (更新: 2025-10-07)

---

## 💡 一句话要点

**提出混合数据合成框架和感知聚焦监督，提升视觉语言模型多模态推理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `过程奖励模型` `多模态推理` `测试时缩放` `数据合成` `感知聚焦监督`

## 📋 核心要点

1. 现有视觉语言过程奖励模型依赖MCTS，易产生噪声监督信号，限制了模型在不同任务上的泛化能力。
2. 提出混合数据合成框架，结合MCTS和VLM判断，生成更准确的步骤级标签，并引入感知聚焦监督。
3. 实验表明，该方法在多个多模态基准测试中，能够有效提升视觉语言模型的推理能力，并揭示了潜在的推理能力。

## 📝 摘要（中文）

本文旨在探索视觉语言过程奖励模型（VL-PRM）的设计空间，以提升大型语言模型中推理的可靠性。现有VL-PRM依赖蒙特卡洛树搜索（MCTS）构建数据，产生噪声监督信号并限制跨任务泛化。本文提出一种混合数据合成框架，结合MCTS和强大VLM的判断，生成更准确的步骤级标签。此外，提出感知聚焦监督，使PRM能够显式检测视觉基础阶段的错误。系统评估多种测试时缩放策略，表明PRM能够可靠地引导VLM获得更准确的解决方案。实验涵盖五个多模态基准（MMMU、PuzzleVQA、AlgoPuzzleVQA、MathVista和MathVision），揭示了VL-PRM作为结果奖励模型（ORM）在测试时缩放（TTS）中优于VL-PRM引导的过程步骤选择，较小的VL-PRM在检测过程错误方面可以匹配甚至超过较大的VL-PRM，VL-PRM揭示了更强VLM骨干网络中的潜在推理能力，感知级别监督显著提高了测试时缩放效果，以及不同策略的TTS性能在高级数学推理数据集上有所提高，尽管没有在这些数据集上训练VL-PRM。

## 🔬 方法详解

**问题定义**：现有视觉语言过程奖励模型（VL-PRM）依赖蒙特卡洛树搜索（MCTS）进行数据构建，这会导致产生带有噪声的监督信号，并且限制了模型在不同任务上的泛化能力。因此，如何构建更准确、更有效的VL-PRM训练数据，并提升其在测试时的推理能力，是本文要解决的核心问题。

**核心思路**：本文的核心思路是通过结合MCTS和强大的视觉语言模型（VLM）的判断，来生成更准确的步骤级标签，从而改进VL-PRM的训练数据质量。此外，引入感知聚焦监督，使PRM能够显式地检测视觉基础阶段的错误，从而提升模型对视觉信息的理解和利用能力。

**技术框架**：整体框架包含数据合成、模型训练和测试时缩放三个主要阶段。数据合成阶段，采用混合策略，结合MCTS和VLM的判断，生成步骤级的奖励信号。模型训练阶段，使用合成的数据训练VL-PRM，并引入感知聚焦监督。测试时缩放阶段，评估不同的策略，利用训练好的VL-PRM引导VLM进行推理。

**关键创新**：本文的关键创新在于混合数据合成框架和感知聚焦监督。混合数据合成框架通过结合MCTS和VLM的判断，有效降低了数据中的噪声，提升了数据质量。感知聚焦监督则使PRM能够显式地检测视觉基础阶段的错误，从而提升了模型对视觉信息的理解和利用能力。

**关键设计**：在数据合成阶段，MCTS用于探索可能的推理路径，而VLM则用于评估这些路径的质量，并提供更准确的奖励信号。感知聚焦监督通过引入额外的损失函数，促使PRM关注视觉基础阶段的错误。在测试时缩放阶段，评估了多种策略，包括使用VL-PRM作为结果奖励模型（ORM）和使用VL-PRM引导的过程步骤选择。

## 📊 实验亮点

实验结果表明，VL-PRM作为结果奖励模型（ORM）在测试时缩放（TTS）中优于VL-PRM引导的过程步骤选择。较小的VL-PRM在检测过程错误方面可以匹配甚至超过较大的VL-PRM。感知级别监督显著提高了测试时缩放效果。在高级数学推理数据集上，不同策略的TTS性能有所提高，即使没有在这些数据集上训练VL-PRM。

## 🎯 应用场景

该研究成果可应用于需要多模态推理的场景，例如智能问答、视觉导航、机器人操作等。通过提升视觉语言模型的推理能力，可以提高这些应用在复杂环境下的可靠性和准确性，具有重要的实际应用价值和潜在的商业前景。

## 📄 摘要（原文）

> Process Reward Models (PRMs) provide step-level supervision that improves the reliability of reasoning in large language models. While PRMs have been extensively studied in text-based domains, their extension to Vision Language Models (VLMs) remains limited. Existing Vision-Language PRMs (VL-PRMs) rely on Monte Carlo Tree Search (MCTS) for data construction, which can often produce noisy supervision signals and limit generalization across tasks. In this work, we aim to elucidate the design space of VL-PRMs by exploring diverse strategies for dataset construction, training, and test-time scaling. First, we introduce a hybrid data synthesis framework that combines MCTS with judgments from a strong VLM, producing more accurate step-level labels. Second, we propose perception-focused supervision, enabling our PRM to explicitly detect errors at the visual grounding stage of reasoning. Third, we systematically evaluate multiple test-time scaling strategies, showing that our PRMs can reliably guide VLMs toward more accurate solutions. Our experiments covering five diverse multimodal benchmarks (MMMU, PuzzleVQA, AlgoPuzzleVQA, MathVista, and MathVision) reveal several key insights: (i) VL-PRMs when used as Outcome Reward Models (ORMs) during test-time scaling (TTS) can outperform VL-PRM guided process step selection, (ii) smaller VL-PRMs can match or even surpass larger ones in detecting process errors, (iii) VL-PRMs uncover latent reasoning abilities in stronger VLM backbones, (iv) perception-level supervision leads to significant gains in test-time scaling, and (v) TTS performance of different policies improve on advanced math reasoning datasets despite not training VL-PRMs on such datasets. We hope our work will motivate further research and support the advancement of VLMs.

