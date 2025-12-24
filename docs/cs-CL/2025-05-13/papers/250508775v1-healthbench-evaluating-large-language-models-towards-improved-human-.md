---
layout: default
title: HealthBench: Evaluating Large Language Models Towards Improved Human Health
---

# HealthBench: Evaluating Large Language Models Towards Improved Human Health

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08775" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08775v1</a>
  <a href="https://arxiv.org/pdf/2505.08775.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08775v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08775v1', 'HealthBench: Evaluating Large Language Models Towards Improved Human Health')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela, Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, Johannes Heidecke, Karan Singhal

**分类**: cs.CL

**发布日期**: 2025-05-13

**备注**: Blog: https://openai.com/index/healthbench/ Code: https://github.com/openai/simple-evals

---

## 💡 一句话要点

**提出HealthBench以评估大型语言模型在医疗健康中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗健康` `开放式评估` `对话系统` `性能基准` `多维度评分` `人工智能应用`

## 📋 核心要点

1. 现有的医疗对话评估方法多为选择题或简答题，缺乏真实的开放式评估，难以全面反映模型的实际表现。
2. HealthBench通过5000个多轮对话和48562个评分标准，提供了一种新的评估框架，能够更真实地反映模型在医疗场景中的表现。
3. 实验结果显示，较小的模型（如GPT-4.1 nano）在成本和性能上均优于更大的模型，展现出显著的提升。

## 📝 摘要（中文）

我们提出了HealthBench，这是一个开源基准，用于测量大型语言模型在医疗领域的性能和安全性。HealthBench包含5000个多轮对话，涉及模型与用户或医疗专业人员的互动。响应评估采用262名医生创建的特定对话评分标准。与以往的多项选择或简答基准不同，HealthBench通过48562个独特的评分标准，涵盖多个健康情境（如紧急情况、临床数据转化、全球健康）和行为维度（如准确性、指令遵循、沟通）实现了现实的开放式评估。过去两年中，HealthBench的表现显示出稳步的初步进展（例如，GPT-3.5 Turbo的得分为16%，而GPT-4o为32%），以及更快速的近期改进（o3得分为60%）。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有医疗对话评估方法的不足，尤其是缺乏开放式评估的真实场景，导致模型性能评估不全面。

**核心思路**：HealthBench的核心思路是通过构建一个包含多轮对话的开放式评估框架，结合医生的专业评分标准，全面评估大型语言模型在医疗健康领域的表现。

**技术框架**：HealthBench的整体架构包括数据收集、对话生成、评分标准制定和性能评估四个主要模块。数据收集阶段通过与用户和医疗专业人员的互动生成对话，评分标准则由医生团队制定。

**关键创新**：HealthBench的主要创新在于其开放式评估机制和多维度评分标准，能够涵盖更广泛的健康情境和行为维度，与传统的选择题或简答题评估方法本质上不同。

**关键设计**：在设计上，HealthBench采用了48562个独特的评分标准，涵盖了准确性、指令遵循和沟通等多个维度，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，HealthBench的引入使得模型评估的准确性和全面性显著提升。GPT-3.5 Turbo的得分为16%，而GPT-4o的得分为32%，更小的GPT-4.1 nano模型在性能上超越了GPT-4o，且成本降低了25倍，显示出显著的性价比优势。

## 🎯 应用场景

HealthBench的研究成果可广泛应用于医疗健康领域，尤其是在大型语言模型的开发和评估中。通过提供一个标准化的评估框架，HealthBench能够帮助开发者优化模型性能，提升医疗服务质量，最终造福人类健康。此外，该基准还可为未来的研究提供参考，推动医疗AI技术的进步。

## 📄 摘要（原文）

> We present HealthBench, an open-source benchmark measuring the performance and safety of large language models in healthcare. HealthBench consists of 5,000 multi-turn conversations between a model and an individual user or healthcare professional. Responses are evaluated using conversation-specific rubrics created by 262 physicians. Unlike previous multiple-choice or short-answer benchmarks, HealthBench enables realistic, open-ended evaluation through 48,562 unique rubric criteria spanning several health contexts (e.g., emergencies, transforming clinical data, global health) and behavioral dimensions (e.g., accuracy, instruction following, communication). HealthBench performance over the last two years reflects steady initial progress (compare GPT-3.5 Turbo's 16% to GPT-4o's 32%) and more rapid recent improvements (o3 scores 60%). Smaller models have especially improved: GPT-4.1 nano outperforms GPT-4o and is 25 times cheaper. We additionally release two HealthBench variations: HealthBench Consensus, which includes 34 particularly important dimensions of model behavior validated via physician consensus, and HealthBench Hard, where the current top score is 32%. We hope that HealthBench grounds progress towards model development and applications that benefit human health.

