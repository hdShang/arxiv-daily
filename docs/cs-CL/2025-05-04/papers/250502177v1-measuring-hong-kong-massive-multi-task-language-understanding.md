---
layout: default
title: Measuring Hong Kong Massive Multi-Task Language Understanding
---

# Measuring Hong Kong Massive Multi-Task Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02177" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02177v1</a>
  <a href="https://arxiv.org/pdf/2505.02177.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02177v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02177v1', 'Measuring Hong Kong Massive Multi-Task Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuxue Cao, Zhenghao Zhu, Junqi Zhu, Guoying Lu, Siyu Peng, Juntao Dai, Weijie Shi, Sirui Han, Yike Guo

**分类**: cs.CL

**发布日期**: 2025-05-04

---

## 💡 一句话要点

**提出HKMMLU基准以解决香港多语言理解评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言理解` `大型语言模型` `评估基准` `香港语言` `文化知识` `翻译任务` `社会科学` `人文学科`

## 📋 核心要点

1. 现有的评估基准未能充分考虑香港的语言和文化特点，导致LLMs在该地区的表现不足。
2. 论文提出HKMMLU基准，包含多任务评估和翻译任务，旨在全面评估香港的语言理解能力。
3. 实验结果显示，当前最佳模型在HKMMLU上的表现远低于其他基准，表明需要针对香港特定的语言能力进行改进。

## 📝 摘要（中文）

多语言理解对于大型语言模型（LLMs）的跨文化适用性至关重要。然而，针对香港独特语言环境的评估基准尚未充分开发。为此，本文提出HKMMLU，一个多任务语言理解基准，评估香港的语言能力和社会文化知识。HKMMLU包含26,698道多选题，涵盖科学、技术、工程、数学（STEM）、社会科学、人文学科及其他四个类别。此外，还包括90,550个普通话-粤语翻译任务。通过对GPT-4o、Claude 3.7 Sonnet及18个不同规模的开源LLMs进行全面实验，结果显示最佳模型DeepSeek-V3的准确率仅为75%，显著低于MMLU和CMMLU。这一表现差距凸显了提升LLMs在香港特定语言和知识领域能力的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决香港特有的语言和文化背景下，现有大型语言模型评估基准不足的问题。现有方法未能充分反映香港的语言复杂性和文化知识，导致LLMs在该地区的应用效果不佳。

**核心思路**：论文提出HKMMLU基准，设计了多任务评估框架，结合多种语言和文化背景的任务，以全面评估LLMs在香港的语言理解能力。通过引入普通话-粤语翻译任务，增强了评估的多样性和实用性。

**技术框架**：HKMMLU基准包括26,698道多选题，分为科学、技术、工程、数学、社会科学、人文学科及其他四个类别。此外，增加了90,550个翻译任务，形成一个多层次的评估体系，涵盖不同领域的知识和语言能力。

**关键创新**：HKMMLU的最大创新在于其针对香港特定的语言和文化背景进行的设计，填补了现有评估基准的空白，使得LLMs的评估更加全面和精准。

**关键设计**：在实验中，采用了多种模型，包括GPT-4o和Claude 3.7 Sonnet，评估了不同模型规模、提示策略及问题和推理令牌长度对模型表现的影响，确保了评估的全面性和科学性。

## 📊 实验亮点

实验结果显示，最佳模型DeepSeek-V3在HKMMLU上的准确率仅为75%，远低于MMLU和CMMLU的表现。这一结果强调了在香港特定语言和知识领域提升LLMs能力的紧迫性，表明当前模型在多语言理解方面仍有显著提升空间。

## 🎯 应用场景

该研究的潜在应用领域包括教育、文化交流和人工智能助手等。HKMMLU基准的建立将推动LLMs在香港及其他多语言环境中的应用，提升其在跨文化交流中的有效性和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multilingual understanding is crucial for the cross-cultural applicability of Large Language Models (LLMs). However, evaluation benchmarks designed for Hong Kong's unique linguistic landscape, which combines Traditional Chinese script with Cantonese as the spoken form and its cultural context, remain underdeveloped. To address this gap, we introduce HKMMLU, a multi-task language understanding benchmark that evaluates Hong Kong's linguistic competence and socio-cultural knowledge. The HKMMLU includes 26,698 multi-choice questions across 66 subjects, organized into four categories: Science, Technology, Engineering, and Mathematics (STEM), Social Sciences, Humanities, and Other. To evaluate the multilingual understanding ability of LLMs, 90,550 Mandarin-Cantonese translation tasks were additionally included. We conduct comprehensive experiments on GPT-4o, Claude 3.7 Sonnet, and 18 open-source LLMs of varying sizes on HKMMLU. The results show that the best-performing model, DeepSeek-V3, struggles to achieve an accuracy of 75\%, significantly lower than that of MMLU and CMMLU. This performance gap highlights the need to improve LLMs' capabilities in Hong Kong-specific language and knowledge domains. Furthermore, we investigate how question language, model size, prompting strategies, and question and reasoning token lengths affect model performance. We anticipate that HKMMLU will significantly advance the development of LLMs in multilingual and cross-cultural contexts, thereby enabling broader and more impactful applications.

