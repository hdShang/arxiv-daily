---
layout: default
title: "Enigmata: Scaling Logical Reasoning in Large Language Models with Synthetic Verifiable Puzzles"
---

# Enigmata: Scaling Logical Reasoning in Large Language Models with Synthetic Verifiable Puzzles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19914" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19914v2</a>
  <a href="https://arxiv.org/pdf/2505.19914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19914v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19914v2', 'Enigmata: Scaling Logical Reasoning in Large Language Models with Synthetic Verifiable Puzzles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiangjie Chen, Qianyu He, Siyu Yuan, Aili Chen, Zhicheng Cai, Weinan Dai, Hongli Yu, Qiying Yu, Xuefeng Li, Jiaze Chen, Hao Zhou, Mingxuan Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出Enigmata以提升大语言模型的逻辑推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `大型语言模型` `强化学习` `生成器-验证器` `多任务学习` `数学推理` `基准评估`

## 📋 核心要点

1. 现有的大语言模型在无需领域知识的谜题推理任务上表现不佳，限制了其应用范围。
2. Enigmata通过提供一个生成器和验证器的组合，构建了一个可扩展的多任务强化学习框架，以提升模型的推理能力。
3. 经过训练的Qwen2.5-32B-Enigmata在多个谜题推理基准上超越了现有模型，并在数学推理任务中展现了良好的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs），如OpenAI的o1和DeepSeek的R1，在数学和编程等高级推理任务中表现出色，但在无需领域知识的人类可解谜题上仍然存在困难。本文介绍了Enigmata，这是第一个全面的工具套件，旨在提升LLMs的谜题推理能力。它包含36个任务，涵盖七个类别，每个任务都有一个生成器，可以生成具有可控难度的无限示例，以及一个基于规则的验证器，用于自动评估。这种生成器-验证器设计支持可扩展的多任务强化学习训练、细粒度分析和无缝的可验证奖励集成。我们还提出了Enigmata-Eval，一个严格的基准，并开发了优化的多任务强化学习策略。经过训练的模型Qwen2.5-32B-Enigmata在Enigmata-Eval、ARC-AGI和ARC-AGI 2等谜题推理基准上表现优于o3-mini-high和o1。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在无需领域知识的谜题推理任务中的不足，现有方法在此类任务上表现不佳，限制了其应用潜力。

**核心思路**：Enigmata通过设计一个生成器和验证器的组合，提供了一个全面的工具套件，旨在提升LLMs的逻辑推理能力，支持可扩展的多任务强化学习训练。

**技术框架**：整体架构包括生成器模块（用于生成具有可控难度的谜题示例）和验证器模块（用于自动评估生成的示例），并结合多任务强化学习策略进行训练。

**关键创新**：最重要的创新在于生成器-验证器设计，使得模型能够在多任务环境中进行有效的训练和评估，显著提升了推理能力。

**关键设计**：在参数设置上，模型使用了优化的多任务强化学习策略，损失函数设计考虑了推理准确性和生成示例的多样性，网络结构则针对逻辑推理进行了优化。

## 📊 实验亮点

实验结果显示，Qwen2.5-32B-Enigmata在Enigmata-Eval、ARC-AGI和ARC-AGI 2等基准上均超越了o3-mini-high和o1，具体提升幅度分别为32.8%和0.6%。此外，该模型在更大规模的模型上训练后，进一步提升了在高级数学和STEM推理任务中的表现，展现了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、游戏设计和人工智能助手等，能够帮助开发更智能的系统，提升其在复杂推理任务中的表现。未来，Enigmata可能会推动更广泛的逻辑推理研究，促进LLMs在多领域的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs), such as OpenAI's o1 and DeepSeek's R1, excel at advanced reasoning tasks like math and coding via Reinforcement Learning with Verifiable Rewards (RLVR), but still struggle with puzzles solvable by humans without domain knowledge. We introduce Enigmata, the first comprehensive suite tailored for improving LLMs with puzzle reasoning skills. It includes 36 tasks across seven categories, each with 1) a generator that produces unlimited examples with controllable difficulty and 2) a rule-based verifier for automatic evaluation. This generator-verifier design supports scalable, multi-task RL training, fine-grained analysis, and seamless RLVR integration. We further propose Enigmata-Eval, a rigorous benchmark, and develop optimized multi-task RLVR strategies. Our trained model, Qwen2.5-32B-Enigmata, consistently surpasses o3-mini-high and o1 on the puzzle reasoning benchmarks like Enigmata-Eval, ARC-AGI (32.8%), and ARC-AGI 2 (0.6%). It also generalizes well to out-of-domain puzzle benchmarks and mathematical reasoning, with little multi-tasking trade-off. When trained on larger models like Seed1.5-Thinking (20B activated parameters and 200B total parameters), puzzle data from Enigmata further boosts SoTA performance on advanced math and STEM reasoning tasks such as AIME (2024-2025), BeyondAIME and GPQA (Diamond), showing nice generalization benefits of Enigmata. This work offers a unified, controllable framework for advancing logical reasoning in LLMs. Resources of this work can be found at https://seed-enigmata.github.io.

