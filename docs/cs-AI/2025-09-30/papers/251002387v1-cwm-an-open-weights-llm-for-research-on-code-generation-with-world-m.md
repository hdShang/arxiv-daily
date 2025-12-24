---
layout: default
title: "CWM: An Open-Weights LLM for Research on Code Generation with World Models"
---

# CWM: An Open-Weights LLM for Research on Code Generation with World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02387" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02387v1</a>
  <a href="https://arxiv.org/pdf/2510.02387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02387v1', 'CWM: An Open-Weights LLM for Research on Code Generation with World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: FAIR CodeGen team, Jade Copet, Quentin Carbonneaux, Gal Cohen, Jonas Gehring, Jacob Kahn, Jannik Kossen, Felix Kreuk, Emily McMilin, Michel Meyer, Yuxiang Wei, David Zhang, Kunhao Zheng, Jordi Armengol-Estapé, Pedram Bashiri, Maximilian Beck, Pierre Chambon, Abhishek Charnalia, Chris Cummins, Juliette Decugis, Zacharias V. Fisches, François Fleuret, Fabian Gloeckle, Alex Gu, Michael Hassid, Daniel Haziza, Badr Youbi Idrissi, Christian Keller, Rahul Kindi, Hugh Leather, Gallil Maimon, Aram Markosyan, Francisco Massa, Pierre-Emmanuel Mazaré, Vegard Mella, Naila Murray, Keyur Muzumdar, Peter O'Hearn, Matteo Pagliardini, Dmitrii Pedchenko, Tal Remez, Volker Seeker, Marco Selvi, Oren Sultan, Sida Wang, Luca Wehrstedt, Ori Yoran, Lingming Zhang, Taco Cohen, Yossi Adi, Gabriel Synnaeve

**分类**: cs.SE, cs.AI, cs.LG

**发布日期**: 2025-09-30

**备注**: 58 pages

---

## 💡 一句话要点

**发布CWM：用于代码生成与世界模型研究的开源LLM**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `代码生成` `世界模型` `大型语言模型` `强化学习` `Python` `软件工程` `开源模型`

## 📋 核心要点

1. 现有代码生成模型难以有效利用环境反馈进行推理和规划，限制了其在复杂任务中的表现。
2. CWM通过在Python解释器和Docker环境中进行观察-行动轨迹训练，构建代码世界模型，提升模型对代码执行过程的理解。
3. CWM在SWE-bench Verified、LiveCodeBench、Math-500和AIME 2024等基准测试中取得了优异的性能，验证了其有效性。

## 📝 摘要（中文）

我们发布Code World Model (CWM)，一个拥有320亿参数的开源LLM，旨在推进基于世界模型的代码生成研究。为了提升代码理解能力，超越仅从静态代码训练所能获得的水平，我们对CWM进行了中期训练，使用了来自Python解释器和agentic Docker环境的大量观察-行动轨迹，并在可验证的编码、数学和多轮软件工程环境中进行了广泛的多任务推理强化学习。借助CWM，我们为研究人员提供了一个强大的测试平台，以探索世界建模为在计算环境中进行推理和规划的代码生成带来的机会。我们展示了世界模型如何有益于agentic编码，实现Python代码执行的逐步模拟，并展示了推理如何从后者中受益的早期结果。CWM是一个密集的、仅解码器的LLM，训练上下文大小高达131k个token。除了世界建模能力外，CWM在通用编码和数学任务上也表现出色：在SWE-bench Verified上达到65.8%的pass@1分数（使用测试时缩放），在LiveCodeBench上达到68.6%，在Math-500上达到96.6%，在AIME 2024上达到76.0%。为了支持对代码世界建模的进一步研究，我们发布了中期训练、SFT和RL后的模型检查点。

## 🔬 方法详解

**问题定义**：现有代码生成模型主要依赖静态代码数据进行训练，缺乏对代码执行环境的理解，难以进行有效的推理和规划。这限制了它们在需要与环境交互的复杂代码生成任务中的应用，例如调试、优化和多步骤问题解决。现有方法难以模拟代码执行过程，无法利用环境反馈来指导代码生成。

**核心思路**：CWM的核心思路是通过引入“世界模型”的概念，让模型学习代码执行环境的动态特性。具体来说，模型通过观察代码执行过程中的状态变化（例如变量值、程序输出），并预测执行动作对环境的影响，从而建立对代码行为的更深入理解。这种理解能力可以帮助模型更好地进行推理和规划，从而生成更准确、更有效的代码。

**技术框架**：CWM的整体框架包括以下几个主要阶段：1) **预训练**：使用大规模代码数据集进行预训练，学习代码的基本语法和语义。2) **中期训练**：在Python解释器和agentic Docker环境中进行训练，模型观察代码执行过程中的状态变化，并学习预测执行动作对环境的影响。3) **监督微调 (SFT)**：使用高质量的代码生成数据集进行微调，提升模型在特定任务上的性能。4) **强化学习 (RL)**：使用强化学习算法，根据环境反馈优化模型的代码生成策略。模型是一个decoder-only的LLM，上下文长度高达131k tokens。

**关键创新**：CWM的关键创新在于将世界模型引入代码生成领域。通过在代码执行环境中进行训练，模型能够学习代码的动态特性，从而更好地进行推理和规划。这与传统的静态代码训练方法形成了鲜明对比，后者主要关注代码的语法和语义，而忽略了代码的执行过程。此外，CWM还采用了大规模的观察-行动轨迹数据进行训练，这使得模型能够学习到更丰富的环境信息。

**关键设计**：CWM的关键设计包括：1) **观察-行动轨迹数据**：模型使用来自Python解释器和agentic Docker环境的大量观察-行动轨迹数据进行训练。这些数据包含了代码执行过程中的状态变化和执行动作，为模型学习世界模型提供了基础。2) **多任务推理强化学习**：模型在可验证的编码、数学和多轮软件工程环境中进行多任务推理强化学习，以提升模型的推理和规划能力。3) **长上下文窗口**：模型采用高达131k tokens的上下文窗口，这使得模型能够处理更长的代码序列和更复杂的任务。

## 📊 实验亮点

CWM在多个代码生成和数学基准测试中取得了优异的性能。例如，在SWE-bench Verified上，CWM达到了65.8%的pass@1分数（使用测试时缩放），在LiveCodeBench上达到了68.6%，在Math-500上达到了96.6%，在AIME 2024上达到了76.0%。这些结果表明CWM在代码生成和数学推理方面具有强大的能力。

## 🎯 应用场景

CWM在代码自动生成、程序调试、软件测试和智能编程助手等领域具有广泛的应用前景。它可以帮助开发者更高效地编写代码，减少错误，并提高软件质量。未来，CWM有望应用于更复杂的软件工程任务，例如自动化软件开发和维护。

## 📄 摘要（原文）

> We release Code World Model (CWM), a 32-billion-parameter open-weights LLM, to advance research on code generation with world models. To improve code understanding beyond what can be learned from training on static code alone, we mid-train CWM on a large amount of observation-action trajectories from Python interpreter and agentic Docker environments, and perform extensive multi-task reasoning RL in verifiable coding, math, and multi-turn software engineering environments. With CWM, we provide a strong testbed for researchers to explore the opportunities world modeling affords for improving code generation with reasoning and planning in computational environments. We present first steps of how world models can benefit agentic coding, enable step-by-step simulation of Python code execution, and show early results of how reasoning can benefit from the latter. CWM is a dense, decoder-only LLM trained with a context size of up to 131k tokens. Independent of its world modeling capabilities, CWM offers strong performance on general coding and math tasks: it reaches pass@1 scores of 65.8% on SWE-bench Verified (with test-time scaling), 68.6% on LiveCodeBench, 96.6% on Math-500, and 76.0% on AIME 2024. To support further research on code world modeling, we release model checkpoints after mid-training, SFT, and RL.

