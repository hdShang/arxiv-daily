---
layout: default
title: DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning
---

# DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23754" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23754v2</a>
  <a href="https://arxiv.org/pdf/2505.23754.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23754v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23754v2', 'DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyin Zhang, Jiahao Xu, Zhiwei He, Tian Liang, Qiuzhi Liu, Yansi Li, Linfeng Song, Zhenwen Liang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, Dong Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出DeepTheorem以提升大语言模型的定理证明能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `定理证明` `大语言模型` `强化学习` `自然语言处理` `数学推理` `数据集构建` `自动化证明`

## 📋 核心要点

1. 现有的自动定理证明方法过于依赖正式证明系统，难以充分利用大语言模型的自然语言推理能力。
2. DeepTheorem框架通过引入非正式定理和强化学习策略，旨在提升大语言模型在数学推理中的表现。
3. 实验结果显示，DeepTheorem在定理证明任务上显著超越现有数据集和监督微调协议，取得了最佳的准确性和推理质量。

## 📝 摘要（中文）

定理证明是评估大语言模型（LLMs）复杂推理能力的重要测试平台。然而，传统的自动定理证明（ATP）方法过于依赖正式的证明系统，这与LLMs在预训练过程中获得的非正式自然语言知识的优势不匹配。本文提出了DeepTheorem，一个综合性的非正式定理证明框架，利用自然语言增强LLM的数学推理能力。DeepTheorem包含一个大规模基准数据集，涵盖121K个高质量的IMO级非正式定理和证明，经过严格的正确性、难度和主题类别注释，并配有系统构建的可验证定理变体。我们设计了一种新颖的强化学习策略（RL-Zero），专门针对非正式定理证明，利用已验证的定理变体来激励稳健的数学推理。实验结果表明，DeepTheorem显著提升了LLM的定理证明性能，达到了最先进的准确性和推理质量。

## 🔬 方法详解

**问题定义**：本文旨在解决传统自动定理证明方法与大语言模型在自然语言推理能力上的不匹配问题。现有方法依赖于正式的证明系统，无法有效利用LLMs在非正式知识上的优势。

**核心思路**：DeepTheorem通过构建一个包含非正式定理的框架，结合强化学习策略（RL-Zero），旨在提升LLMs的数学推理能力。该设计利用自然语言的灵活性来增强推理过程。

**技术框架**：DeepTheorem的整体架构包括数据集构建、定理变体生成和强化学习训练三个主要模块。数据集包含121K个非正式定理，经过严格注释，确保其质量和多样性。

**关键创新**：最重要的创新在于RL-Zero策略，它专门针对非正式定理证明进行设计，利用可验证的定理变体来激励模型进行稳健的推理。这一方法与传统的监督学习方法有本质区别。

**关键设计**：在模型训练中，采用了特定的损失函数来优化推理步骤的质量，并通过系统构建的定理变体来增强模型的学习效果。

## 📊 实验亮点

实验结果表明，DeepTheorem在定理证明任务中达到了最先进的准确率，较现有基线提升了显著的性能，具体提升幅度未知。这一成果展示了DeepTheorem在非正式定理证明领域的巨大潜力。

## 🎯 应用场景

DeepTheorem的研究成果在数学教育、自动化定理证明和智能辅导系统等领域具有广泛的应用潜力。通过提升大语言模型的推理能力，该框架可以帮助学生更好地理解复杂的数学概念，并为研究人员提供更强大的工具进行数学探索。

## 📄 摘要（原文）

> Theorem proving serves as a major testbed for evaluating complex reasoning abilities in large language models (LLMs). However, traditional automated theorem proving (ATP) approaches rely heavily on formal proof systems that poorly align with LLMs' strength derived from informal, natural language knowledge acquired during pre-training. In this work, we propose DeepTheorem, a comprehensive informal theorem-proving framework exploiting natural language to enhance LLM mathematical reasoning. DeepTheorem includes a large-scale benchmark dataset consisting of 121K high-quality IMO-level informal theorems and proofs spanning diverse mathematical domains, rigorously annotated for correctness, difficulty, and topic categories, accompanied by systematically constructed verifiable theorem variants. We devise a novel reinforcement learning strategy (RL-Zero) explicitly tailored to informal theorem proving, leveraging the verified theorem variants to incentivize robust mathematical inference. Additionally, we propose comprehensive outcome and process evaluation metrics examining proof correctness and the quality of reasoning steps. Extensive experimental analyses demonstrate DeepTheorem significantly improves LLM theorem-proving performance compared to existing datasets and supervised fine-tuning protocols, achieving state-of-the-art accuracy and reasoning quality. Our findings highlight DeepTheorem's potential to fundamentally advance automated informal theorem proving and mathematical exploration.

