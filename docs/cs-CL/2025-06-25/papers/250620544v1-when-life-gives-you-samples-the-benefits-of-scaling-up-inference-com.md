---
layout: default
title: "When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs"
---

# When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20544" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20544v1</a>
  <a href="https://arxiv.org/pdf/2506.20544.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20544v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20544v1', 'When Life Gives You Samples: The Benefits of Scaling up Inference Compute for Multilingual LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ammar Khairi, Daniel D'souza, Ye Shen, Julia Kreutzer, Sara Hooker

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出多语言LLM推理计算扩展策略以提升性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `推理计算` `采样策略` `选择策略` `开放式任务` `性能提升`

## 📋 核心要点

1. 现有的推理计算方法主要集中在英语和特定领域，缺乏对多语言和开放式任务的适应性。
2. 本研究提出了新的采样和选择策略，旨在针对多语言和多任务推理场景进行优化。
3. 实验结果显示，采用新策略后，模型在多个基准测试中胜率显著提升，尤其在多语言环境下表现突出。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展使得推理时计算的扩展成为研究重点，从而在不重新训练模型的情况下提升性能。现有研究主要集中在英语及少数领域，而本研究关注于开放式生成任务的多语言、多任务设置。研究表明，基于温度变化的采样策略和选择策略需适应多样化的领域和语言环境。我们提出了针对多语言和多任务推理场景的新型采样和选择策略，显著提升了不同语言和任务的表现，尤其在m-ArenaHard-v2.0基准上，8B模型的胜率提升了6.8个百分点，111B模型的胜率提升了9.0个百分点，显示出在低成本下实现显著性能提升的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有多语言LLM推理计算方法在开放式生成任务中的适应性不足，尤其是在不同语言和领域的表现不均衡问题。

**核心思路**：论文提出通过调整采样策略和选择策略，针对多语言和多任务环境进行优化，以提高模型在不同语言和任务上的表现。

**技术框架**：整体架构包括采样阶段和选择阶段，首先进行多样化的输出采样，然后根据特定策略选择最佳输出，确保适应不同语言和任务的需求。

**关键创新**：最重要的创新在于提出了针对多语言和多任务的专用采样和选择策略，这些策略能够有效提升模型在非英语环境中的表现，与现有方法相比具有更好的泛化能力。

**关键设计**：在参数设置上，采用了温度变化的采样策略，并在选择阶段引入了多样化的选择标准，以适应不同的语言和任务特性。

## 📊 实验亮点

实验结果显示，采用新提出的采样和选择策略后，8B模型在m-ArenaHard-v2.0基准测试中胜率提升了6.8个百分点，而111B模型在相同基准上胜率提升了9.0个百分点，表明在多语言环境下显著提高了模型的性能。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、跨文化内容生成和多任务学习等。通过提升多语言LLM的推理能力，可以更好地服务于全球用户，促进不同语言之间的交流与理解，具有重要的社会价值和商业潜力。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have shifted focus toward scaling inference-time compute, improving performance without retraining the model. A common approach is to sample multiple outputs in parallel, and select one of these as the final output. However, work to date has focused on English and a handful of domains such as math and code. In contrast, we are most interested in techniques that generalize across open-ended tasks, formally verifiable tasks, and across languages. In this work, we study how to robustly scale inference-time compute for open-ended generative tasks in a multilingual, multi-task setting.
>   Our findings show that both sampling strategy based on temperature variation and selection strategy must be adapted to account for diverse domains and varied language settings. We evaluate existing selection methods, revealing that strategies effective in English often fail to generalize across languages. We propose novel sampling and selection strategies specifically adapted for multilingual and multi-task inference scenarios, and show they yield notable gains across languages and tasks. In particular, our combined sampling and selection methods lead to an average +6.8 jump in win-rates for our 8B models on m-ArenaHard-v2.0 prompts, against proprietary models such as Gemini. At larger scale, Command-A (111B model) equipped with our methods, shows +9.0 improvement in win-rates on the same benchmark with just five samples against single-sample decoding, a substantial increase at minimal cost. Our results underscore the need for language- and task-aware approaches to inference-time compute, aiming to democratize performance improvements in underrepresented languages.

