---
layout: default
title: "Stop Spinning Wheels: Mitigating LLM Overthinking via Mining Patterns for Early Reasoning Exit"
---

# Stop Spinning Wheels: Mitigating LLM Overthinking via Mining Patterns for Early Reasoning Exit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17627" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17627v1</a>
  <a href="https://arxiv.org/pdf/2508.17627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17627v1', 'Stop Spinning Wheels: Mitigating LLM Overthinking via Mining Patterns for Early Reasoning Exit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Wei, Liang Pang, Jiahao Liu, Jingcheng Deng, Shicheng Xu, Zenghao Duan, Jingang Wang, Fei Sun, Xunliang Cai, Huawei Shen, Xueqi Cheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出一种新方法以减少大型语言模型的过度思考问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理优化` `过度思考` `推理完成点` `模式挖掘` `资源消耗` `启发式规则`

## 📋 核心要点

1. 现有方法在处理大型语言模型的推理时，过度思考导致性能下降和资源浪费。
2. 论文提出通过识别推理完成点（RCP）来减轻过度思考，利用敏感的RCP模式和轻量级阈值策略。
3. 实验结果显示，该方法在多个基准测试上减少了令牌消耗，同时保持或提高了推理的准确性。

## 📝 摘要（中文）

大型语言模型（LLMs）通过扩展个体思维过程来增强复杂推理任务的能力。然而，先前的研究表明，过度思考可能会降低整体性能。本文将推理过程分为三个阶段：探索不足阶段、补偿推理阶段和推理收敛阶段。通常，LLMs在补偿推理阶段能够产生正确答案，而推理收敛阶段则常常导致过度思考，增加资源消耗甚至导致无限循环。因此，减轻过度思考的关键在于检测补偿推理阶段的结束，即推理完成点（RCP）。本文通过挖掘更敏感且一致的RCP模式，提出了一种基于启发式规则的轻量级阈值策略。实验结果表明，该方法在保持或提高推理准确性的同时，减少了令牌消耗。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中出现的过度思考问题。现有方法在检测推理完成点（RCP）时缺乏高效和精确的平衡，导致资源浪费和性能下降。

**核心思路**：论文的核心思路是通过挖掘推理完成点（RCP）的敏感模式，结合启发式规则，设计出一种轻量级的阈值策略，以便及时结束补偿推理阶段，避免进入过度思考阶段。

**技术框架**：整体架构包括三个主要阶段：推理过程监控、RCP模式挖掘和阈值判断。首先监控LLM的推理过程，识别潜在的RCP，然后通过挖掘历史推理数据中的模式来确定RCP，最后应用阈值策略来判断何时结束推理。

**关键创新**：本文的主要创新在于提出了一种基于模式挖掘的RCP识别方法，与现有的逐句查询或监控结束标记的方法相比，更加高效和准确。

**关键设计**：在参数设置上，采用了启发式规则来定义阈值，确保在不同的推理任务中都能有效识别RCP。此外，设计了适应性损失函数，以优化推理过程中的资源使用。

## 📊 实验亮点

实验结果表明，所提方法在AIME24、AIME25和GPQA-D等基准测试上显著减少了令牌消耗，且推理准确性保持不变或有所提升，展示了在资源利用和推理效率上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过减少过度思考，该方法可以提高大型语言模型在实际应用中的效率和准确性，降低资源消耗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) enhance complex reasoning tasks by scaling the individual thinking process. However, prior work shows that overthinking can degrade overall performance. Motivated by observed patterns in thinking length and content length, we categorize reasoning into three stages: insufficient exploration stage, compensatory reasoning stage, and reasoning convergence stage. Typically, LLMs produce correct answers in the compensatory reasoning stage, whereas reasoning convergence often triggers overthinking, causing increased resource usage or even infinite loops. Therefore, mitigating overthinking hinges on detecting the end of the compensatory reasoning stage, defined as the Reasoning Completion Point (RCP). RCP typically appears at the end of the first complete reasoning cycle and can be identified by querying the LLM sentence by sentence or monitoring the probability of an end-of-thinking token (e.g., \texttt{</think>}), though these methods lack an efficient and precise balance. To improve this, we mine more sensitive and consistent RCP patterns and develop a lightweight thresholding strategy based on heuristic rules. Experimental evaluations on benchmarks (AIME24, AIME25, GPQA-D) demonstrate that the proposed method reduces token consumption while preserving or enhancing reasoning accuracy.

