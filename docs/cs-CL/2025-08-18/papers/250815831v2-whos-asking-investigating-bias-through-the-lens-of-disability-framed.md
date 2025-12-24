---
layout: default
title: "Who's Asking? Investigating Bias Through the Lens of Disability Framed Queries in LLMs"
---

# Who's Asking? Investigating Bias Through the Lens of Disability Framed Queries in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15831" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15831v2</a>
  <a href="https://arxiv.org/pdf/2508.15831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15831v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15831v2', 'Who\'s Asking? Investigating Bias Through the Lens of Disability Framed Queries in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vishnu Hari, Kalpana Panda, Srikant Panda, Amit Agarwal, Hitesh Laxmichand Patel

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-18 (更新: 2025-10-22)

**备注**: Accepted at ICCV 2025

---

## 💡 一句话要点

**系统审计残疾条件下的LLMs偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见推断` `残疾研究` `社会公平` `人工智能伦理` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在推断用户人口特征时存在偏见，尤其是在缺乏明确信息的情况下，残疾线索的影响尚未被充分研究。
2. 本文通过系统审计八种指令调优的LLMs，探讨残疾条件下的人口偏见，提出使用平衡模板语料库进行评估的方法。
3. 实验结果显示，模型在97%的情况下做出明确人口属性猜测，揭示了残疾背景对预测结果的显著影响，并指出大模型在偏见推理上的脆弱性。

## 📝 摘要（中文）

大型语言模型（LLMs）通常仅通过措辞推断用户的人口特征，这可能导致偏见响应，尤其是在没有明确人口信息的情况下。本文首次系统审计了八种最先进的指令调优LLMs在残疾条件下的人口偏见。通过使用平衡的模板语料库，结合九个残疾类别和六个实际商业领域，研究者促使每个模型在中性和残疾意识条件下预测五个人口属性。结果显示，模型在97%的情况下做出明确的人口猜测，表明其在缺乏明确依据的情况下倾向于做出任意推断。残疾背景显著改变了预测属性的分布，而领域背景进一步放大了这些偏差。研究发现，较大的模型对残疾线索更敏感，但也更容易产生偏见推理，揭示了当前对齐策略中的盲点。研究者建议整合避免校准和反事实微调，以减少不必要的人口推断。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在缺乏明确人口信息时，如何通过残疾线索推断用户人口特征的问题。现有方法未能充分考虑残疾背景对推断结果的影响，导致潜在的偏见和不准确性。

**核心思路**：研究者通过系统审计八种不同规模的指令调优LLMs，使用平衡模板语料库，结合残疾类别与商业领域，探讨残疾条件下的偏见推断。这样的设计旨在揭示模型在不同背景下的推断差异。

**技术框架**：研究采用了一个多阶段的评估框架，包括数据收集、模型推断和结果分析。首先构建包含九个残疾类别和六个商业领域的模板语料库，然后对每个模型进行推断，最后分析不同条件下的预测结果。

**关键创新**：本文的创新在于首次系统审计残疾条件下的偏见推断，揭示了残疾背景对模型推断的显著影响，并指出大模型在偏见推理方面的脆弱性。与现有方法相比，强调了残疾线索的重要性。

**关键设计**：研究中使用了平衡的模板语料库，确保每个残疾类别与商业领域的组合都得到充分覆盖。模型的推断过程包括对五个人口属性的预测，采用了中性和残疾意识两种条件进行对比分析。

## 📊 实验亮点

实验结果显示，模型在97%的情况下做出明确的人口属性猜测，表明其在缺乏明确依据的情况下倾向于做出任意推断。较大的模型对残疾线索更敏感，但也更容易产生偏见推理，揭示了当前对齐策略中的盲点。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能伦理、社会科学研究和大型语言模型的开发。通过揭示残疾条件下的偏见，研究为模型的公平性和包容性提供了重要的指导，促进了对残疾人群体的理解与支持，未来可能影响政策制定和技术标准。

## 📄 摘要（原文）

> Large Language Models (LLMs) routinely infer users demographic traits from phrasing alone, which can result in biased responses, even when no explicit demographic information is provided. The role of disability cues in shaping these inferences remains largely uncharted. Thus, we present the first systematic audit of disability-conditioned demographic bias across eight state-of-the-art instruction-tuned LLMs ranging from 3B to 72B parameters. Using a balanced template corpus that pairs nine disability categories with six real-world business domains, we prompt each model to predict five demographic attributes - gender, socioeconomic status, education, cultural background, and locality - under both neutral and disability-aware conditions.
>   Across a varied set of prompts, models deliver a definitive demographic guess in up to 97\% of cases, exposing a strong tendency to make arbitrary inferences with no clear justification. Disability context heavily shifts predicted attribute distributions, and domain context can further amplify these deviations. We observe that larger models are simultaneously more sensitive to disability cues and more prone to biased reasoning, indicating that scale alone does not mitigate stereotype amplification.
>   Our findings reveal persistent intersections between ableism and other demographic stereotypes, pinpointing critical blind spots in current alignment strategies. We release our evaluation framework and results to encourage disability-inclusive benchmarking and recommend integrating abstention calibration and counterfactual fine-tuning to curb unwarranted demographic inference. Code and data will be released on acceptance.

