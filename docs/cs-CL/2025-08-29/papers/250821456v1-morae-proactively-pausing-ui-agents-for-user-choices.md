---
layout: default
title: "Morae: Proactively Pausing UI Agents for User Choices"
---

# Morae: Proactively Pausing UI Agents for User Choices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21456" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21456v1</a>
  <a href="https://arxiv.org/pdf/2508.21456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21456v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21456v1', 'Morae: Proactively Pausing UI Agents for User Choices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Hao Peng, Dingzeyu Li, Jeffrey P. Bigham, Amy Pavel

**分类**: cs.HC, cs.CL, cs.CV

**发布日期**: 2025-08-29

**备注**: ACM UIST 2025

---

## 💡 一句话要点

**提出Morae以解决盲人及低视力用户的UI选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户界面代理` `盲人辅助技术` `多模态模型` `用户自主性` `决策支持`

## 📋 核心要点

1. 现有UI代理在执行任务时未能有效地让用户参与关键选择，导致用户自主性降低。
2. Morae通过自动识别决策点并暂停，允许用户在任务执行中做出选择，从而增强用户的参与感。
3. 在针对BLV用户的实证研究中，Morae显著提高了任务完成率和用户选择的满意度。

## 📝 摘要（中文）

用户界面（UI）代理旨在为盲人和低视力（BLV）用户提供更易访问的界面。然而，现有的UI代理通常在执行任务时不涉及用户的关键选择，降低了用户的自主性。为了解决这一问题，本文提出了Morae，一个能够自动识别任务执行中的决策点并暂停以便用户做出选择的UI代理。Morae利用大型多模态模型解读用户查询、UI代码和截图，并在需要做出选择时提示用户进行澄清。在对BLV参与者进行的真实网页任务研究中，Morae帮助用户完成更多任务，并选择更符合其偏好的选项，相较于基线代理（如OpenAI Operator）表现更佳。

## 🔬 方法详解

**问题定义**：本文旨在解决现有UI代理在执行任务时未能让盲人和低视力用户参与关键选择的问题。现有方法往往忽视用户的偏好和选择，导致用户体验不佳。

**核心思路**：Morae的核心思路是通过自动识别任务中的决策点并暂停，促使用户参与选择。该设计旨在提高用户的自主性和满意度。

**技术框架**：Morae的整体架构包括用户查询解析、UI代码和截图的多模态解读，以及在决策点时的用户提示模块。该系统能够实时分析用户输入并与UI状态进行交互。

**关键创新**：Morae的最大创新在于其混合主动性的方法，用户不仅能享受自动化带来的便利，还能在关键时刻表达自己的偏好。这与传统的全自动代理形成了鲜明对比。

**关键设计**：Morae采用了大型多模态模型，结合用户查询、UI元素和上下文信息进行分析。具体的参数设置和损失函数设计尚未详细披露，可能为未知。

## 📊 实验亮点

在与基线代理（如OpenAI Operator）的对比实验中，Morae显著提高了BLV用户的任务完成率和选择满意度，具体数据表明用户完成的任务数量增加，选择的选项更符合其个人偏好。

## 🎯 应用场景

Morae的研究成果可广泛应用于无障碍技术、智能助手和其他需要用户参与决策的交互系统中。通过增强用户的选择权，Morae有潜力改善盲人和低视力用户的日常生活体验，并推动相关领域的技术进步。

## 📄 摘要（原文）

> User interface (UI) agents promise to make inaccessible or complex UIs easier to access for blind and low-vision (BLV) users. However, current UI agents typically perform tasks end-to-end without involving users in critical choices or making them aware of important contextual information, thus reducing user agency. For example, in our field study, a BLV participant asked to buy the cheapest available sparkling water, and the agent automatically chose one from several equally priced options, without mentioning alternative products with different flavors or better ratings. To address this problem, we introduce Morae, a UI agent that automatically identifies decision points during task execution and pauses so that users can make choices. Morae uses large multimodal models to interpret user queries alongside UI code and screenshots, and prompt users for clarification when there is a choice to be made. In a study over real-world web tasks with BLV participants, Morae helped users complete more tasks and select options that better matched their preferences, as compared to baseline agents, including OpenAI Operator. More broadly, this work exemplifies a mixed-initiative approach in which users benefit from the automation of UI agents while being able to express their preferences.

