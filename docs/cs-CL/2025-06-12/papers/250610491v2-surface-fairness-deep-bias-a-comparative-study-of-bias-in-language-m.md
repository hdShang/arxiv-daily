---
layout: default
title: "Surface Fairness, Deep Bias: A Comparative Study of Bias in Language Models"
---

# Surface Fairness, Deep Bias: A Comparative Study of Bias in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10491" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10491v2</a>
  <a href="https://arxiv.org/pdf/2506.10491.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10491v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10491v2', 'Surface Fairness, Deep Bias: A Comparative Study of Bias in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksandra Sorokovikova, Pavel Chizhov, Iuliia Eremenko, Ivan P. Yamshchikov

**分类**: cs.CL

**发布日期**: 2025-06-12 (更新: 2025-09-01)

---

## 💡 一句话要点

**研究语言模型中的偏见问题及其影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `偏见研究` `个性化技术` `人机交互` `公平性评估`

## 📋 核心要点

1. 核心问题：现有大型语言模型在处理用户个性化时，可能会表现出偏见，影响结果的公平性。
2. 方法要点：通过对比不同的偏见测量方法，探讨模型在不同任务下的偏见表现，尤其是在评分和薪资建议场景中。
3. 实验或效果：研究发现，模型在用户回答评分时表现出显著偏见，而在薪资谈判建议中偏见更为明显。

## 📝 摘要（中文）

现代语言模型在大量数据上进行训练，这些数据不可避免地包含争议性和刻板印象内容，涉及性别、出身、年龄等各种偏见。因此，模型可能表达偏见观点或根据用户的个性产生不同结果。本文研究了大型语言模型中的各种偏见代理测量，发现通过预设个性进行评估的模型在多主题基准（MMLU）上的得分差异微乎其微且大多随机。然而，当要求模型对用户的回答进行评分时，偏见的迹象更为明显。最后，在要求模型提供薪资谈判建议时，答案中表现出明显的偏见。随着大型语言模型助手记忆和个性化的趋势，这些问题从不同角度显现：现代用户无需预设个性描述，因为模型已经了解他们的社会人口特征。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中存在的偏见问题，尤其是在个性化和用户交互时表现出的偏见。现有方法在评估模型偏见时，往往未能揭示其在特定任务下的真实表现。

**核心思路**：通过重新设计任务，特别是让模型对用户的回答进行评分，来揭示模型潜在的偏见。这种方法能够更清晰地反映出模型在实际应用中的偏见表现。

**技术框架**：研究采用多主题基准（MMLU）进行评估，分为预设个性评估和用户回答评分两种主要任务。通过对比这两种任务的结果，分析模型在不同场景下的偏见表现。

**关键创新**：论文的创新在于通过任务重构，揭示了模型在用户交互中的偏见表现，尤其是在薪资谈判建议中，显示出与现有评估方法的本质区别。

**关键设计**：在实验中，采用了多种评估指标，关注模型在不同个性化场景下的表现，特别是薪资谈判建议的偏见分析。

## 📊 实验亮点

实验结果显示，在多主题基准（MMLU）上，预设个性评估的得分差异微乎其微，而在用户回答评分任务中，模型表现出显著的偏见。特别是在薪资谈判建议中，模型的偏见表现尤为明显，表明个性化对结果的影响不容忽视。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、智能助手和教育技术等。通过识别和减轻语言模型中的偏见，可以提高这些系统的公平性和用户体验，促进更为公正的技术应用。未来，随着个性化技术的发展，理解和管理模型偏见将变得愈加重要。

## 📄 摘要（原文）

> Modern language models are trained on large amounts of data. These data inevitably include controversial and stereotypical content, which contains all sorts of biases related to gender, origin, age, etc. As a result, the models express biased points of view or produce different results based on the assigned personality or the personality of the user. In this paper, we investigate various proxy measures of bias in large language models (LLMs). We find that evaluating models with pre-prompted personae on a multi-subject benchmark (MMLU) leads to negligible and mostly random differences in scores. However, if we reformulate the task and ask a model to grade the user's answer, this shows more significant signs of bias. Finally, if we ask the model for salary negotiation advice, we see pronounced bias in the answers. With the recent trend for LLM assistant memory and personalization, these problems open up from a different angle: modern LLM users do not need to pre-prompt the description of their persona since the model already knows their socio-demographics.

