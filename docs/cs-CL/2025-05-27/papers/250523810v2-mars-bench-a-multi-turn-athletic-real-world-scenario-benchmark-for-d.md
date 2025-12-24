---
layout: default
title: MARS-Bench: A Multi-turn Athletic Real-world Scenario Benchmark for Dialogue Evaluation
---

# MARS-Bench: A Multi-turn Athletic Real-world Scenario Benchmark for Dialogue Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23810" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23810v2</a>
  <a href="https://arxiv.org/pdf/2505.23810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23810v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23810v2', 'MARS-Bench: A Multi-turn Athletic Real-world Scenario Benchmark for Dialogue Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenghao Yang, Yinbo Luo, Zhoufutu Wen, Qi Chu, Tao Gong, Longxiang Liu, Kaiyuan Zhang, Jianpeng Jiao, Ge Zhang, Wenhao Huang, Nenghai Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-09-15)

**备注**: 29 pages, 13 figures, Accepted as EMNLP2025 Findings

---

## 💡 一句话要点

**提出MARS-Bench以解决LLMs在复杂对话中的鲁棒性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `大型语言模型` `对话评估` `鲁棒性` `动机转移` `跨轮依赖` `真实场景`

## 📋 核心要点

1. 现有的对话基准无法充分反映大型语言模型在处理复杂对话时的鲁棒性问题，尤其是在多轮对话中。
2. 本文提出MARS-Bench基准，旨在通过真实的对话场景评估LLMs在多轮对话中的表现，特别关注动机转移和跨轮依赖。
3. 实验结果显示，闭源LLMs在复杂对话任务中表现优异，且明确推理能显著提升其鲁棒性。

## 📝 摘要（中文）

大型语言模型（LLMs），如ChatGPT，已广泛应用于实际对话场景。然而，LLMs在处理长复杂对话时的鲁棒性受到批评，尤其是在频繁的动机转移和复杂的跨轮依赖方面。现有基准无法充分反映这些弱点。为此，本文提出了MARS-Bench，一个多轮运动真实场景对话基准，旨在填补这一空白。MARS-Bench基于逐步文本评论构建，专门设计用于评估多轮对话的三个关键方面：超多轮、互动多轮和跨轮任务。实验结果表明，闭源LLMs显著优于开源替代品，明确推理显著提升LLMs在处理长复杂对话时的鲁棒性，同时LLMs在处理动机转移和复杂跨轮依赖时面临重大挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长复杂对话中鲁棒性不足的问题，尤其是在动机转移和跨轮依赖方面的挑战。现有方法未能充分评估这些问题的影响。

**核心思路**：论文提出MARS-Bench基准，通过构建基于逐步文本评论的真实对话场景，专门设计用于评估多轮对话的关键方面，以填补现有基准的不足。

**技术框架**：MARS-Bench的整体架构包括三个主要模块：超多轮对话、互动多轮对话和跨轮任务，旨在全面评估LLMs在多轮对话中的表现。

**关键创新**：MARS-Bench的最大创新在于其真实场景的构建，能够有效评估LLMs在复杂对话中的表现，尤其是在动机转移和跨轮依赖方面的能力。

**关键设计**：在实验中，采用了注意力可视化技术，揭示了特殊标记导致的注意力沉没现象，从而影响LLMs在长对话中的表现。

## 📊 实验亮点

实验结果表明，闭源LLMs在MARS-Bench基准上显著优于开源替代品，且明确推理的引入使得LLMs在处理长复杂对话时的鲁棒性提升了显著水平。这些发现为未来的对话系统设计提供了重要的实验依据。

## 🎯 应用场景

MARS-Bench基准的提出为对话系统的研究提供了新的评估工具，能够帮助研究者更好地理解和改进大型语言模型在复杂对话场景中的表现。这一基准在智能客服、虚拟助手和社交机器人等领域具有广泛的应用潜力，未来可能推动对话系统的进一步发展与优化。

## 📄 摘要（原文）

> Large Language Models (\textbf{LLMs}), e.g. ChatGPT, have been widely adopted in real-world dialogue applications. However, LLMs' robustness, especially in handling long complex dialogue sessions, including frequent motivation transfer, sophisticated cross-turn dependency, is criticized all along. Nevertheless, no existing benchmarks can fully reflect these weaknesses. We present \textbf{MARS-Bench}, a \textbf{M}ulti-turn \textbf{A}thletic \textbf{R}eal-world \textbf{S}cenario Dialogue \textbf{Bench}mark, designed to remedy the gap. MARS-Bench is constructed from play-by-play text commentary so to feature realistic dialogues specifically designed to evaluate three critical aspects of multi-turn conversations: Ultra Multi-turn, Interactive Multi-turn, and Cross-turn Tasks. Extensive experiments on MARS-Bench also reveal that closed-source LLMs significantly outperform open-source alternatives, explicit reasoning significantly boosts LLMs' robustness on handling long complex dialogue sessions, and LLMs indeed face significant challenges when handling motivation transfer and sophisticated cross-turn dependency. Moreover, we provide mechanistic interpretability on how attention sinks due to special tokens lead to LLMs' performance degradation when handling long complex dialogue sessions based on attention visualization experiment in Qwen2.5-7B-Instruction.

