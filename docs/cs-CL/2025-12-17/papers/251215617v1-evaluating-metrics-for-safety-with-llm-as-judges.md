---
layout: default
title: Evaluating Metrics for Safety with LLM-as-Judges
---

# Evaluating Metrics for Safety with LLM-as-Judges

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15617" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15617v1</a>
  <a href="https://arxiv.org/pdf/2512.15617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15617v1" onclick="toggleFavorite(this, '2512.15617v1', 'Evaluating Metrics for Safety with LLM-as-Judges')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kester Clegg, Richard Hawkins, Ibrahim Habli, Tom Lawton

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出基于LLM-as-Judges的加权指标评估方法，提升LLM在安全关键任务中的可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性评估` `LLM-as-Judges` `加权指标` `上下文敏感性`

## 📋 核心要点

1. 现有方法难以保证LLM在安全关键任务中的可靠性，存在潜在风险。
2. 提出基于LLM-as-Judges的评估框架，通过加权指标降低评估风险。
3. 通过上下文敏感性定义错误严重程度，并设置置信度阈值触发人工审查。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地应用于文本处理流程中，以智能地响应各种输入和生成任务。这使得取代现有信息流中因人员不足或流程复杂性而受限的人工角色成为可能。然而，LLM会犯错，并且某些处理角色对安全性至关重要。例如，根据医院转诊信对术后护理患者进行分类，或更新核设施中工作组的现场访问计划。如果我们要将LLM引入以前由人工执行的关键信息流中，我们如何才能使其安全可靠？本文认为，安全论证应侧重于从LLM流程的评估点获得的证据类型，特别是采用LLM-as-Judges（LaJ）评估器的框架。本文认为，尽管我们无法从许多自然语言处理任务中获得确定性评估，但通过采用一系列加权指标，可以降低评估中出错的风险，使用上下文敏感性来定义错误严重程度，并设计置信度阈值，当评估者之间的一致性较低时，触发对关键LaJ判断的人工审查。

## 🔬 方法详解

**问题定义**：论文旨在解决如何评估和提高LLM在安全关键任务中的可靠性的问题。现有方法在评估LLM的安全性时，往往缺乏细粒度的风险控制和上下文敏感性，难以保证LLM在实际应用中的安全性，尤其是在需要高可靠性的场景下。

**核心思路**：论文的核心思路是采用LLM-as-Judges (LaJ) 的评估框架，并结合加权指标来更全面地评估LLM的安全性。通过对不同指标赋予不同的权重，可以更准确地反映LLM在特定任务中的风险水平。此外，论文还强调了上下文敏感性的重要性，并提出了根据上下文定义错误严重程度的方法。

**技术框架**：该框架主要包含以下几个阶段：1. 使用LLM执行目标任务，例如文本分类或信息提取。2. 使用多个LLM-as-Judges评估器对LLM的输出进行评估，每个评估器关注不同的安全指标。3. 对各个评估器的结果进行加权汇总，得到最终的安全性评估结果。4. 根据评估结果，如果置信度低于预设阈值，则触发人工审查。

**关键创新**：该论文的关键创新在于：1. 提出了基于加权指标的LLM安全性评估方法，可以更准确地反映LLM在特定任务中的风险水平。2. 强调了上下文敏感性的重要性，并提出了根据上下文定义错误严重程度的方法。3. 设计了置信度阈值，当评估者之间的一致性较低时，触发人工审查，从而进一步提高了LLM的安全性。

**关键设计**：论文的关键设计包括：1. 如何选择合适的安全指标，并为每个指标赋予合理的权重。2. 如何定义上下文敏感的错误严重程度。3. 如何设置置信度阈值，以平衡自动化评估的效率和人工审查的成本。这些设计需要根据具体的应用场景进行调整和优化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15617v1/clinicalworkflow.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15617v1/gpt5anesthetist.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15617v1/dashboard.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文重点在于提出了一种评估框架，并没有提供具体的实验数据。其亮点在于强调了加权指标和上下文敏感性在LLM安全评估中的重要性，并提出了相应的解决方案。该框架为后续研究提供了有益的参考，并有望推动LLM在安全关键领域的应用。

## 🎯 应用场景

该研究成果可应用于各种安全关键领域，例如医疗诊断、金融风控、核电站安全管理等。通过提高LLM在这些领域的可靠性，可以降低人为错误的风险，提高工作效率，并最终保障人民生命财产安全。未来，该研究还可以扩展到其他类型的AI系统，例如自动驾驶汽车和机器人。

## 📄 摘要（原文）

> LLMs (Large Language Models) are increasingly used in text processing pipelines to intelligently respond to a variety of inputs and generation tasks. This raises the possibility of replacing human roles that bottleneck existing information flows, either due to insufficient staff or process complexity. However, LLMs make mistakes and some processing roles are safety critical. For example, triaging post-operative care to patients based on hospital referral letters, or updating site access schedules in nuclear facilities for work crews. If we want to introduce LLMs into critical information flows that were previously performed by humans, how can we make them safe and reliable? Rather than make performative claims about augmented generation frameworks or graph-based techniques, this paper argues that the safety argument should focus on the type of evidence we get from evaluation points in LLM processes, particularly in frameworks that employ LLM-as-Judges (LaJ) evaluators. This paper argues that although we cannot get deterministic evaluations from many natural language processing tasks, by adopting a basket of weighted metrics it may be possible to lower the risk of errors within an evaluation, use context sensitivity to define error severity and design confidence thresholds that trigger human review of critical LaJ judgments when concordance across evaluators is low.

