---
layout: default
title: "Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework"
---

# Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05007" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05007v2</a>
  <a href="https://arxiv.org/pdf/2509.05007.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05007v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05007v2', 'Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Chen, Jinhao Jiang, Yingqian Min, Zican Dong, Shijie Wang, Wayne Xin Zhao, Ji-Rong Wen

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-05 (更新: 2025-09-08)

**备注**: 11 pages, 1 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/RUCAIBox/Sticker-TTS)

---

## 💡 一句话要点

**提出Sticker-TTS，利用历史经验提升大模型在数学推理任务中的测试时性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `测试时扩展` `大语言模型` `数学推理` `历史经验利用` `模仿学习`

## 📋 核心要点

1. 现有测试时扩展方法依赖冗余采样，忽略历史经验，导致计算效率低下。
2. Sticker-TTS通过提炼关键条件（贴纸），驱动LRM迭代探索和改进解决方案。
3. Sticker-TTS在数学推理基准测试中超越了自洽性和强化学习等基线方法。

## 📝 摘要（中文）

大型推理模型(LRMs)在复杂的推理任务上表现出强大的性能，并且可以通过增加推理时的计算预算来进一步提高性能。然而，目前的测试时扩展方法主要依赖于冗余采样，忽略了历史经验的利用，从而限制了计算效率。为了克服这个限制，我们提出了Sticker-TTS，这是一种新颖的测试时扩展框架，它协调三个协作的LRM，在历史尝试的指导下迭代地探索和改进解决方案。我们框架的核心是提炼的关键条件——称为贴纸(sticker)——它驱动着跨多轮推理的关键信息的提取、改进和重用。为了进一步提高我们框架的效率和性能，我们引入了一种结合模仿学习和自我改进的两阶段优化策略，从而实现渐进式改进。在包括AIME-24、AIME-25和OlymMATH在内的三个具有挑战性的数学推理基准上的广泛评估表明，在可比的推理预算下，Sticker-TTS始终优于包括自洽性和高级强化学习方法在内的强大基线。这些结果突出了贴纸引导的历史经验利用的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型推理模型在测试时扩展中计算效率低下的问题。现有方法主要依赖于冗余采样，没有充分利用历史推理经验，导致计算资源的浪费和性能提升的瓶颈。特别是在数学推理等复杂任务中，如何有效利用历史信息来指导后续推理过程是一个关键挑战。

**核心思路**：论文的核心思路是利用“贴纸”（Sticker）来提炼和传递历史推理过程中的关键信息。通过将关键条件蒸馏成贴纸，可以指导后续的推理过程，避免重复探索，并促进知识的重用。这种方法模拟了人类解决问题时不断回顾和总结经验的过程，从而提高推理效率和准确性。

**技术框架**：Sticker-TTS框架包含三个协同工作的LRM：一个用于生成初始解，一个用于提取关键条件（贴纸），另一个用于基于贴纸改进解。整个流程是迭代的：首先，生成初始解；然后，提取贴纸；接着，利用贴纸改进解；重复这个过程直到达到预定的计算预算或满足收敛条件。框架采用两阶段优化策略：第一阶段使用模仿学习，让模型学习如何生成和利用贴纸；第二阶段使用自我改进，通过奖励机制鼓励模型探索更有效的推理路径。

**关键创新**：Sticker-TTS的关键创新在于引入了“贴纸”的概念，并设计了一个基于贴纸的迭代推理框架。与传统的冗余采样方法不同，Sticker-TTS能够有效地利用历史信息，避免重复计算，并促进知识的迁移和重用。此外，两阶段优化策略也提高了模型的学习效率和泛化能力。

**关键设计**：贴纸的具体内容是根据任务类型和模型特点设计的，可以包括中间步骤、关键变量或约束条件等。贴纸的提取和利用是通过特定的神经网络结构实现的，例如，可以使用注意力机制来选择与当前推理步骤相关的贴纸。损失函数包括模仿学习损失和强化学习奖励，用于指导模型的训练。两阶段优化策略中的超参数需要根据具体任务进行调整，以达到最佳性能。

## 📊 实验亮点

Sticker-TTS在AIME-24、AIME-25和OlymMATH三个数学推理基准测试中，在可比的推理预算下，始终优于包括自洽性和高级强化学习方法在内的强大基线。实验结果表明，Sticker-TTS能够有效地利用历史经验，提高推理效率和准确性，验证了贴纸引导的历史经验利用的有效性。

## 🎯 应用场景

Sticker-TTS框架具有广泛的应用前景，可应用于数学推理、代码生成、知识图谱推理等需要复杂推理和历史经验的任务。该方法可以提高推理效率，降低计算成本，并提升模型的准确性和可靠性。未来，该框架可以扩展到其他领域，例如自然语言处理和计算机视觉，以解决更复杂的推理问题。

## 📄 摘要（原文）

> Large reasoning models (LRMs) have exhibited strong performance on complex reasoning tasks, with further gains achievable through increased computational budgets at inference. However, current test-time scaling methods predominantly rely on redundant sampling, ignoring the historical experience utilization, thereby limiting computational efficiency. To overcome this limitation, we propose Sticker-TTS, a novel test-time scaling framework that coordinates three collaborative LRMs to iteratively explore and refine solutions guided by historical attempts. At the core of our framework are distilled key conditions-termed stickers-which drive the extraction, refinement, and reuse of critical information across multiple rounds of reasoning. To further enhance the efficiency and performance of our framework, we introduce a two-stage optimization strategy that combines imitation learning with self-improvement, enabling progressive refinement. Extensive evaluations on three challenging mathematical reasoning benchmarks, including AIME-24, AIME-25, and OlymMATH, demonstrate that Sticker-TTS consistently surpasses strong baselines, including self-consistency and advanced reinforcement learning approaches, under comparable inference budgets. These results highlight the effectiveness of sticker-guided historical experience utilization. Our code and data are available at https://github.com/RUCAIBox/Sticker-TTS.

