---
layout: default
title: "Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot"
---

# Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14641" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14641v2</a>
  <a href="https://arxiv.org/pdf/2506.14641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14641v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14641v2', 'Revisiting Chain-of-Thought Prompting: Zero-shot Can Be Stronger than Few-shot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiang Cheng, Chengyan Pan, Minjun Zhao, Deyang Li, Fangchao Liu, Xinyu Zhang, Xiao Zhang, Yong Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-17 (更新: 2025-10-13)

**备注**: EMNLP25-findings camera_ready, 19 pages,22 figures

---

## 💡 一句话要点

**重新审视链式思维提示：零-shot优于少量示例**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思维` `情境学习` `大语言模型` `推理能力` `数学任务` `示例有效性`

## 📋 核心要点

1. 现有的链式思维示例在强模型中未能有效提升推理性能，显示出其局限性。
2. 论文通过系统实验探讨了传统CoT示例与零-shot CoT的效果差异，提出了对ICL范式的重新审视。
3. 实验结果表明，增强的CoT示例未能改善推理能力，模型更关注指令而非示例。

## 📝 摘要（中文）

在大语言模型（LLMs）中，情境学习（ICL）是一种重要的突现能力。近期研究引入了链式思维（CoT）作为ICL的示例，以增强推理能力，尤其是在数学任务中。然而，随着模型能力的不断提升，传统CoT示例是否仍能为强模型带来益处尚不明确。通过系统实验，我们发现对于如Qwen2.5系列的强模型，添加传统CoT示例并未提升推理性能，反而主要用于与人类期望的输出格式对齐。进一步分析显示，模型倾向于忽视示例，专注于指令，导致推理能力没有明显提升。这些发现突显了当前ICL+CoT框架在数学推理中的局限性，呼吁对ICL范式及示例定义进行重新审视。

## 🔬 方法详解

**问题定义**：本论文旨在解决在强大的大语言模型中，传统链式思维示例对推理性能的影响问题。现有方法未能有效提升模型的推理能力，尤其是在数学任务中。

**核心思路**：论文提出通过系统实验比较传统CoT示例与零-shot CoT的效果，探讨增强CoT示例的有效性，旨在重新审视ICL的定义和应用。

**技术框架**：研究采用实验对比的方法，主要模块包括传统CoT示例、零-shot CoT示例和增强CoT示例，分析其对模型推理性能的影响。

**关键创新**：最重要的创新在于发现对于强模型，传统CoT示例并未提升推理能力，且模型更倾向于关注指令而非示例，这与现有方法的假设存在本质区别。

**关键设计**：实验中使用了不同的示例构建方法，包括从先进模型（如Qwen2.5-Max和DeepSeek-R1）获取的答案，分析其对推理性能的影响。

## 📊 实验亮点

实验结果显示，传统的链式思维示例对强模型的推理性能没有显著提升，零-shot CoT的表现反而更佳。这一发现挑战了以往对示例有效性的假设，提示研究者在设计模型时需重新考虑示例的作用。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能问答等。通过优化大语言模型的推理能力，可以提升其在复杂任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In-Context Learning (ICL) is an essential emergent ability of Large Language Models (LLMs), and recent studies introduce Chain-of-Thought (CoT) to exemplars of ICL to enhance the reasoning capability, especially in mathematics tasks. However, given the continuous advancement of model capabilities, it remains unclear whether CoT exemplars still benefit recent, stronger models in such tasks. Through systematic experiments, we find that for recent strong models such as the Qwen2.5 series, adding traditional CoT exemplars does not improve reasoning performance compared to Zero-Shot CoT. Instead, their primary function is to align the output format with human expectations. We further investigate the effectiveness of enhanced CoT exemplars, constructed using answers from advanced models such as \texttt{Qwen2.5-Max} and \texttt{DeepSeek-R1}. Experimental results indicate that these enhanced exemplars still fail to improve the model's reasoning performance. Further analysis reveals that models tend to ignore the exemplars and focus primarily on the instructions, leading to no observable gain in reasoning ability. Overall, our findings highlight the limitations of the current ICL+CoT framework in mathematical reasoning, calling for a re-examination of the ICL paradigm and the definition of exemplars.

