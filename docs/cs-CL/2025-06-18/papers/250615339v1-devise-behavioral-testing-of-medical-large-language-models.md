---
layout: default
title: "DeVisE: Behavioral Testing of Medical Large Language Models"
---

# DeVisE: Behavioral Testing of Medical Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15339" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15339v1</a>
  <a href="https://arxiv.org/pdf/2506.15339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15339v1', 'DeVisE: Behavioral Testing of Medical Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Camila Zurdo Tagliabue, Heloisa Oss Boll, Aykut Erdem, Erkut Erdem, Iacer Calixto

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出DeVisE框架以评估医疗大语言模型的行为表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `临床决策支持` `行为测试` `反事实推理` `公平性评估` `医疗AI` `MIMIC-IV` `细粒度理解`

## 📋 核心要点

1. 现有的评估方法无法有效区分大语言模型的真实医学推理与表面模式，导致临床决策支持的可靠性不足。
2. 本文提出DeVisE框架，通过构建包含人口统计和生命体征反事实的数据集，深入探测模型的临床理解能力。
3. 实验结果表明，零-shot模型在反事实推理上表现更佳，而微调模型则在稳定性上占优，强调了公平性在评估中的重要性。

## 📝 摘要（中文）

随着大语言模型（LLMs）在临床决策支持中的应用日益增加，现有评估方法往往无法有效区分真实的医学推理与表面模式。本文提出DeVisE（人口统计和生命体征评估），一个用于探测细粒度临床理解的行为测试框架。我们构建了一个来自MIMIC-IV的ICU出院记录数据集，生成了真实和基于模板的合成版本，控制单变量反事实，针对人口统计（年龄、性别、种族）和生命体征属性进行评估。我们在零-shot和微调设置下评估了五种LLM，结果显示零-shot模型表现出更连贯的反事实推理模式，而微调模型则更稳定但对临床变化反应较弱。人口统计因素对输出的影响微妙但一致，强调了公平性评估的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有评估方法无法有效区分大语言模型在医学推理中的真实表现与表面模式的问题，导致临床决策支持的可靠性不足。

**核心思路**：提出DeVisE框架，通过构建包含人口统计和生命体征反事实的数据集，深入探测模型的细粒度临床理解能力，以实现更公平和透明的评估。

**技术框架**：整体架构包括数据集构建、模型评估和行为分析三个主要模块。数据集构建阶段生成真实和合成的ICU出院记录，模型评估阶段测试不同LLM的表现，行为分析阶段则评估模型对反事实的敏感性和下游推理能力。

**关键创新**：最重要的技术创新在于通过控制单变量反事实，系统性地探测模型在不同人口统计和生命体征条件下的推理能力，与现有方法相比，提供了更细致的评估视角。

**关键设计**：在实验中，采用了零-shot和微调两种设置，评估模型在不同条件下的表现，重点关注输入级别的敏感性和下游推理的影响，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，零-shot模型在反事实推理上表现出更连贯的模式，而微调模型则在稳定性上占优。尤其是，人口统计因素对模型输出的影响微妙但一致，强调了公平性评估的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗AI系统的设计与评估，尤其是在临床决策支持工具中。通过提供更公平和透明的评估方法，DeVisE框架有助于提高医疗AI的安全性和可靠性，未来可能推动医疗行业对AI技术的更广泛接受与应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used in clinical decision support, yet current evaluation methods often fail to distinguish genuine medical reasoning from superficial patterns. We introduce DeVisE (Demographics and Vital signs Evaluation), a behavioral testing framework for probing fine-grained clinical understanding. We construct a dataset of ICU discharge notes from MIMIC-IV, generating both raw (real-world) and template-based (synthetic) versions with controlled single-variable counterfactuals targeting demographic (age, gender, ethnicity) and vital sign attributes. We evaluate five LLMs spanning general-purpose and medically fine-tuned variants, under both zero-shot and fine-tuned settings. We assess model behavior via (1) input-level sensitivity - how counterfactuals alter the likelihood of a note; and (2) downstream reasoning - how they affect predicted hospital length-of-stay. Our results show that zero-shot models exhibit more coherent counterfactual reasoning patterns, while fine-tuned models tend to be more stable yet less responsive to clinically meaningful changes. Notably, demographic factors subtly but consistently influence outputs, emphasizing the importance of fairness-aware evaluation. This work highlights the utility of behavioral testing in exposing the reasoning strategies of clinical LLMs and informing the design of safer, more transparent medical AI systems.

