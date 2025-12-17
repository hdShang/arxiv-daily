---
layout: default
title: DART: Difficulty-Adaptive Reasoning Truncation for Efficient Large Language Models
---

# DART: Difficulty-Adaptive Reasoning Truncation for Efficient Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01170" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01170</a>
  <a href="https://arxiv.org/pdf/2511.01170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01170" onclick="toggleFavorite(this, '2511.01170', 'DART: Difficulty-Adaptive Reasoning Truncation for Efficient Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruofan Zhang, Bin Xia, Zhen Cheng, Cairen Jian, Minglun Yang, Ngai Wong, Yuan Cheng

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DART：面向高效大语言模型的难度自适应推理截断框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理效率` `自适应推理` `思维链` `知识蒸馏`

## 📋 核心要点

1. 现有思维链方法生成冗长解释导致效率低下，而强化学习方法又不稳定且依赖奖励。
2. DART通过模仿学习从强模型中提炼简洁推理模式，并学习何时停止思考。
3. 实验表明DART在保持或提高准确性的同时，显著提升了推理效率，实现了推理截断和计算加速。

## 📝 摘要（中文）

自适应推理对于使大型语言模型（LLM）的计算量与问题的内在难度相匹配至关重要。现有的思维链方法虽然增强了推理能力，但会不加区分地生成冗长的解释，导致明显的效率低下。然而，现有的自适应思维强化学习方法仍然不稳定，并且严重依赖奖励。本文提出了DART，一个监督的难度自适应推理截断框架，它根据问题的难度调整思维长度。通过从更强的模型中提炼简洁的推理模式，将它们内插到连续的推理风格中，并精心策划平衡正确性和紧凑性的最佳训练数据，DART学会了何时“停止思考”。在多个数学基准测试中，实验结果表明了其显著的效率，同时保持或提高了准确性，实现了显著的81.2%的推理截断（DeepSeek-R1-Distill-Qwen-7B在GSM8K数据集上），并实现了5.33倍的计算加速。DART为高效推理提供了一个稳定和通用的范例，推动了LLM中自适应智能的发展。

## 🔬 方法详解

**问题定义**：现有的大语言模型推理方法，特别是思维链方法，在解决问题时会生成冗长的推理过程，导致计算效率低下。即使对于简单的问题，模型也会产生不必要的推理步骤，浪费计算资源。现有的基于强化学习的自适应推理方法，虽然可以动态调整推理长度，但训练过程不稳定，且对奖励函数的设计高度敏感。

**核心思路**：DART的核心思路是通过模仿学习，让小模型学习大模型在不同难度问题上的推理模式，特别是学习何时停止推理。通过将大模型的推理过程提炼成一系列不同长度的推理风格，并构建平衡正确性和紧凑性的训练数据集，使小模型能够根据问题的难度自适应地调整推理长度。

**技术框架**：DART框架主要包含三个阶段：1) **推理风格蒸馏**：从一个更强大的教师模型中提取不同长度的推理链，形成一个推理风格的连续谱。2) **数据策展**：构建一个训练数据集，该数据集包含不同长度的推理链，并根据正确性和紧凑性对这些推理链进行加权。3) **模型训练**：使用策展的数据集训练一个较小的学生模型，使其能够根据问题的难度自适应地选择合适的推理长度。

**关键创新**：DART的关键创新在于其难度自适应的推理截断机制。与传统的思维链方法不同，DART能够根据问题的难度动态调整推理长度，避免了不必要的计算开销。与基于强化学习的方法相比，DART采用监督学习的方式，训练过程更加稳定，且不需要复杂的奖励函数设计。

**关键设计**：DART的关键设计包括：1) 使用插值方法生成连续的推理风格，允许模型在不同的推理长度之间平滑过渡。2) 设计了一种数据策展策略，平衡了推理的正确性和紧凑性，确保模型既能正确解决问题，又能尽可能地减少计算量。3) 使用标准的Transformer架构作为学生模型，并采用交叉熵损失函数进行训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.01170/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.01170/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.01170/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DART在GSM8K数据集上实现了81.2%的推理截断，同时保持了与原始模型相当的准确率。在DeepSeek-R1-Distill-Qwen-7B模型上，DART实现了5.33倍的计算加速。实验结果表明，DART在多个数学基准测试中都取得了显著的效率提升，并且在某些情况下甚至超过了原始模型的性能。

## 🎯 应用场景

DART框架可应用于各种需要高效推理的大语言模型应用场景，例如移动设备上的智能助手、资源受限的边缘计算设备以及对延迟敏感的在线服务。通过减少推理所需的计算量，DART可以降低模型的部署成本，提高响应速度，并扩展大语言模型在资源有限环境中的应用范围。

## 📄 摘要（原文）

> Adaptive reasoning is essential for aligning the computational effort of large language models (LLMs) with the intrinsic difficulty of problems. Current chain-of-thought methods boost reasoning ability but indiscriminately generate long explanations, leading to evident inefficiency. However, existing reinforcement learning approaches to adaptive thinking remain unstable and heavily reward-dependent. Here we propose \textbf{DART}, a supervised \textbf{D}ifficulty-\textbf{A}daptive \textbf{R}easoning \textbf{T}runcation framework that adjusts thinking length according to problem difficulty. By distilling concise reasoning patterns from stronger models, interpolating them into a continuum of reasoning styles, and curating optimal training data that balances correctness and compactness, DART learns when to ``stop thinking''. Across multiple mathematical benchmarks, experimental results demonstrate its remarkable efficiency while preserving or improving accuracy, achieving a significant 81.2\% reasoning truncation (DeepSeek-R1-Distill-Qwen-7B on GSM8K dataset) with 5.33$\times$ computational acceleration. DART provides a stable and general paradigm for efficient reasoning, advancing the development of adaptive intelligence in LLMs.

