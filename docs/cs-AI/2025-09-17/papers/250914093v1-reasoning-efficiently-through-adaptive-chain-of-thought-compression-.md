---
layout: default
title: "Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework"
---

# Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14093" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14093v1</a>
  <a href="https://arxiv.org/pdf/2509.14093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14093v1', 'Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kerui Huang, Shuhan Liu, Xing Hu, Tongtong Xu, Lingfeng Bao, Xin Xia

**分类**: cs.SE, cs.AI, cs.CL

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出SEER自优化框架，通过自适应压缩CoT推理链提升LLM在软件工程任务中的效率与准确率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Chain-of-Thought` `大型语言模型` `软件工程` `自适应推理` `效率优化`

## 📋 核心要点

1. 现有CoT推理方法在软件工程等任务中存在计算成本高、冗余推理导致性能下降等问题。
2. SEER框架通过Best-of-N采样和任务感知自适应过滤，动态压缩CoT推理链，降低计算开销。
3. 实验表明，SEER在软件工程和数学任务中，平均缩短CoT 42.1%，提高准确率，并减少无限循环。

## 📝 摘要（中文）

Chain-of-Thought (CoT) 推理通过引入中间步骤来增强大型语言模型 (LLM)，从而提高其在算术、逻辑和常识任务中的准确性和鲁棒性。然而，这种优势伴随着高昂的计算成本：更长的输出会增加延迟、内存使用和 KV-cache 需求。这些问题在需要简洁和确定性输出的软件工程任务中尤为关键。为了研究这些权衡，我们基于代码生成基准进行了实证研究。结果表明，更长的 CoT 并非总是有帮助。过度的推理通常会导致截断、准确率下降以及高达五倍的延迟，并且失败的输出始终比成功的输出更长。这些发现挑战了更长的推理本质上更好的假设，并强调了自适应 CoT 控制的必要性。受此启发，我们提出了 SEER (Self-Enhancing Efficient Reasoning)，这是一个自适应框架，可以在保持准确性的同时压缩 CoT。SEER 结合了 Best-of-N 采样与任务感知自适应过滤，动态调整基于预推理输出的阈值，以减少冗长和计算开销。然后，我们在三个软件工程任务和一个数学任务上评估了 SEER。平均而言，SEER 将 CoT 缩短了 42.1%，通过减少截断提高了准确率，并消除了大多数无限循环。这些结果表明，SEER 是一种实用的方法，可以使 CoT 增强的 LLM 更加高效和鲁棒，即使在资源受限的情况下也是如此。

## 🔬 方法详解

**问题定义**：论文旨在解决CoT推理在软件工程等任务中效率低下的问题。现有方法中，过长的推理链会导致计算成本增加，同时冗余信息反而会降低准确率，甚至出现无限循环。尤其是在资源受限的场景下，CoT推理的实用性受到限制。

**核心思路**：论文的核心思路是自适应地压缩CoT推理链，在保证准确率的前提下，减少不必要的推理步骤和冗余信息。通过预先分析推理过程中的信息，动态调整推理的长度和详细程度，从而提高效率并避免过度推理带来的负面影响。

**技术框架**：SEER框架主要包含以下几个阶段：1) Best-of-N采样：生成多个CoT推理链的候选结果。2) 任务感知自适应过滤：根据预推理输出，动态调整阈值，过滤掉冗余或无效的推理步骤。3) 选择最优结果：从过滤后的候选推理链中选择最优的结果作为最终输出。整个框架通过自适应地调整CoT的长度，在效率和准确率之间取得平衡。

**关键创新**：SEER的关键创新在于任务感知的自适应过滤机制。该机制能够根据具体的任务和预推理的结果，动态地调整过滤阈值，从而更有效地压缩CoT推理链。与传统的固定长度CoT或简单的截断方法相比，SEER能够更好地保留关键信息，同时去除冗余信息，从而提高效率和准确率。

**关键设计**：在Best-of-N采样阶段，需要选择合适的N值，以保证候选推理链的多样性。在任务感知自适应过滤阶段，需要设计合适的阈值调整策略，例如可以根据预推理输出的置信度或相关性来动态调整阈值。此外，还需要设计合适的选择策略，从过滤后的候选推理链中选择最优的结果，例如可以根据模型的置信度或与任务的相关性来选择。

## 📊 实验亮点

实验结果表明，SEER在三个软件工程任务和一个数学任务上，平均缩短CoT 42.1%，显著提高了推理效率。同时，SEER通过减少截断和消除无限循环，提高了准确率。例如，在代码生成任务中，SEER能够生成更简洁、更准确的代码，并减少了因推理链过长导致的错误。

## 🎯 应用场景

SEER框架可应用于各种需要高效和准确推理的软件工程任务，例如代码生成、代码修复、程序理解等。该方法能够降低计算成本，提高开发效率，并增强LLM在资源受限环境下的应用能力。未来，SEER还可扩展到其他需要CoT推理的领域，如自然语言处理、知识图谱推理等。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by prompting intermediate steps, improving accuracy and robustness in arithmetic, logic, and commonsense tasks. However, this benefit comes with high computational costs: longer outputs increase latency, memory usage, and KV-cache demands. These issues are especially critical in software engineering tasks where concise and deterministic outputs are required. To investigate these trade-offs, we conduct an empirical study based on code generation benchmarks. The results reveal that longer CoT does not always help. Excessive reasoning often causes truncation, accuracy drops, and latency up to five times higher, with failed outputs consistently longer than successful ones. These findings challenge the assumption that longer reasoning is inherently better and highlight the need for adaptive CoT control. Motivated by this, we propose SEER (Self-Enhancing Efficient Reasoning), an adaptive framework that compresses CoT while preserving accuracy. SEER combines Best-of-N sampling with task-aware adaptive filtering, dynamically adjusting thresholds based on pre-inference outputs to reduce verbosity and computational overhead. We then evaluate SEER on three software engineering tasks and one math task. On average, SEER shortens CoT by 42.1%, improves accuracy by reducing truncation, and eliminates most infinite loops. These results demonstrate SEER as a practical method to make CoT-enhanced LLMs more efficient and robust, even under resource constraints.

