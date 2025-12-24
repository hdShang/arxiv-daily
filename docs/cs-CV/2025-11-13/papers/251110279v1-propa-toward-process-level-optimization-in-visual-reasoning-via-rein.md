---
layout: default
title: "PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning"
---

# PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10279" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10279v1</a>
  <a href="https://arxiv.org/pdf/2511.10279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10279v1', 'PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbei Jiang, Chao Lei, Yihao Ding, Krista Ehinger, Jey Han Lau

**分类**: cs.CV

**发布日期**: 2025-11-13

**🔗 代码/项目**: [GITHUB](https://github.com/YanbeiJiang/PROPA)

---

## 💡 一句话要点

**提出PROPA框架，通过强化学习优化视觉推理中的过程级依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉推理` `强化学习` `蒙特卡洛树搜索` `过程级优化` `视觉语言模型`

## 📋 核心要点

1. 视觉语言模型在复杂推理中易出错，原因是多步依赖导致早期错误累积。
2. PROPA利用MCTS与GRPO结合，生成密集过程奖励，无需人工标注即可优化中间步骤。
3. PROPA通过交错GRPO和SFT更新，并训练PRM，显著提升了视觉推理的性能和泛化能力。

## 📝 摘要（中文）

视觉语言模型(VLM)在复杂视觉推理中面临挑战，多步依赖关系导致早期错误在推理链中累积。现有的后训练方法存在局限：监督微调(SFT)依赖于昂贵的步骤级标注，而基于可验证奖励的强化学习(RLVR)方法，如GRPO，仅提供稀疏的结果级反馈，阻碍了稳定优化。我们提出了PROPA（具有交错策略对齐的过程级推理优化），该框架集成了蒙特卡洛树搜索(MCTS)与GRPO，以生成密集的、过程级的奖励，并在没有人工标注的情况下优化每个中间步骤的推理。为了克服冷启动问题，PROPA将GRPO更新与SFT交错进行，使模型能够从成功和失败的推理轨迹中学习。进一步训练过程奖励模型(PRM)以指导推理时的搜索，使测试时搜索与训练信号对齐。在七个基准测试和四个VLM骨干网络上，PROPA始终优于基于SFT和RLVR的基线，在领域内任务上实现了高达17.0%的增益，在领域外任务上实现了高达21.0%的增益，为视觉推理任务建立了强大的推理和泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉推理任务中，视觉语言模型由于多步依赖关系导致的早期错误累积问题。现有方法，如监督微调(SFT)，需要昂贵的步骤级标注，而基于结果奖励的强化学习(RLVR)方法，如GRPO，提供的反馈过于稀疏，难以进行有效的过程级优化。

**核心思路**：PROPA的核心思路是通过强化学习，对视觉推理过程中的每一步进行优化，而无需人工标注。它利用蒙特卡洛树搜索(MCTS)来探索不同的推理路径，并结合GRPO来学习策略。通过MCTS生成密集的、过程级的奖励信号，从而克服了传统RLVR方法中奖励稀疏的问题。

**技术框架**：PROPA框架主要包含以下几个模块：1) 视觉语言模型(VLM)：作为推理的主体；2) 蒙特卡洛树搜索(MCTS)：用于探索不同的推理路径，并生成过程级的奖励信号；3) GRPO：用于更新VLM的策略；4) 过程奖励模型(PRM)：用于指导推理时的搜索，使测试时搜索与训练信号对齐。整体流程是：首先使用SFT进行预训练，然后交错进行GRPO更新和SFT更新，同时训练PRM。在推理时，使用PRM指导MCTS搜索，并选择最优的推理路径。

**关键创新**：PROPA的关键创新在于：1) 提出了过程级推理优化的概念，通过强化学习对推理过程中的每一步进行优化；2) 将MCTS与GRPO结合，生成密集的、过程级的奖励信号，克服了传统RLVR方法中奖励稀疏的问题；3) 提出了交错更新策略，将GRPO更新与SFT更新交错进行，克服了冷启动问题；4) 训练PRM来指导推理时的搜索，使测试时搜索与训练信号对齐。

**关键设计**：PROPA的关键设计包括：1) 奖励函数的设计：奖励函数综合考虑了推理的正确性和效率，鼓励模型选择更短、更正确的推理路径；2) MCTS的搜索策略：MCTS使用UCT算法进行搜索，平衡了探索和利用；3) PRM的网络结构：PRM是一个Transformer模型，输入是推理步骤的上下文，输出是该步骤的奖励预测；4) 交错更新的比例：论文中实验了不同的GRPO更新和SFT更新的比例，最终选择了一个最优的比例。

## 📊 实验亮点

PROPA在七个基准测试和四个VLM骨干网络上进行了评估，结果表明PROPA始终优于基于SFT和RLVR的基线。在领域内任务上，PROPA实现了高达17.0%的增益，在领域外任务上实现了高达21.0%的增益。这些结果表明，PROPA具有强大的推理和泛化能力，能够有效地解决视觉推理中的过程级依赖问题。

## 🎯 应用场景

PROPA框架可应用于各种需要复杂视觉推理的场景，例如视觉问答、图像描述生成、机器人导航等。通过优化推理过程，可以提高视觉语言模型在这些任务中的性能和可靠性，具有广泛的应用前景和实际价值。未来，该方法可以进一步扩展到其他多模态推理任务中。

## 📄 摘要（原文）

> Despite significant progress, Vision-Language Models (VLMs) still struggle with complex visual reasoning, where multi-step dependencies cause early errors to cascade through the reasoning chain. Existing post-training paradigms are limited: Supervised Fine-Tuning (SFT) relies on costly step-level annotations, while Reinforcement Learning with Verifiable Rewards (RLVR) methods like GRPO provide only sparse, outcome-level feedback, hindering stable optimization. We introduce PROPA (Process-level Reasoning Optimization with interleaved Policy Alignment), a novel framework that integrates Monte Carlo Tree Search (MCTS) with GRPO to generate dense, process-level rewards and optimize reasoning at each intermediate step without human annotations. To overcome the cold-start problem, PROPA interleaves GRPO updates with SFT, enabling the model to learn from both successful and failed reasoning trajectories. A Process Reward Model (PRM) is further trained to guide inference-time search, aligning the test-time search with the training signal. Across seven benchmarks and four VLM backbones, PROPA consistently outperforms both SFT- and RLVR-based baselines. It achieves up to 17.0% gains on in-domain tasks and 21.0% gains on out-of-domain tasks compared to existing state-of-the-art, establishing a strong reasoning and generalization capability for visual reasoning tasks. The code isavailable at: https://github.com/YanbeiJiang/PROPA.

