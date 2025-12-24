---
layout: default
title: The Impact of Disability Disclosure on Fairness and Bias in LLM-Driven Candidate Selection
---

# The Impact of Disability Disclosure on Fairness and Bias in LLM-Driven Candidate Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00256" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00256v1</a>
  <a href="https://arxiv.org/pdf/2506.00256.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00256v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00256v1', 'The Impact of Disability Disclosure on Fairness and Bias in LLM-Driven Candidate Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahammed Kamruzzaman, Gene Louis Kim

**分类**: cs.CL

**发布日期**: 2025-05-30

**备注**: Accepted at The 38th International FLAIRS Conference (FLAIRS 2025)(main)

---

## 💡 一句话要点

**探讨残疾信息披露对LLM驱动候选人选择的公平性影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `招聘公平性` `残疾信息披露` `候选人选择` `偏见分析`

## 📋 核心要点

1. 现有研究多聚焦于残疾对简历筛选的影响，但缺乏对自愿披露信息的具体研究，导致对LLM驱动候选人选择的理解不足。
2. 本研究通过分析候选人在相同条件下的选择结果，探讨残疾信息披露对LLM选择偏见的影响，旨在揭示潜在的公平性问题。
3. 实验结果表明，LLMs在选择候选人时更倾向于选择未披露残疾的候选人，显示出明显的偏见，提示招聘过程中的公平性亟待改善。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在招聘过程中的广泛应用，公平性问题日益受到关注。公司在招聘时通常要求提供包括性别、种族及残疾或退伍军人身份等人口统计信息。这些数据旨在支持多样性和包容性倡议，但在提供给LLMs时，尤其是与残疾相关的信息，可能引发候选人选择结果中的潜在偏见。尽管已有研究指出残疾对简历筛选的影响，但关于自愿披露信息对LLM驱动候选人选择的具体影响研究较少。本研究旨在填补这一空白。研究发现，在性别、种族、资格、经验和背景相同的情况下，LLMs更倾向于选择未披露残疾的候选人，即使在候选人选择不披露残疾状态的情况下，LLMs的选择也不如明确表示没有残疾的候选人。

## 🔬 方法详解

**问题定义**：本研究旨在探讨自愿披露残疾信息对LLM驱动候选人选择的影响，现有方法未能充分考虑这一因素，导致潜在的选择偏见。

**核心思路**：通过控制性别、种族、资格和经验等变量，分析候选人披露与不披露残疾信息对LLM选择结果的影响，揭示信息披露的公平性问题。

**技术框架**：研究采用实验设计，选取多个职位（如收银员、软件开发者），在相同条件下对比不同残疾信息披露的候选人选择结果，分析LLMs的偏见表现。

**关键创新**：本研究首次系统性地探讨了自愿披露残疾信息对LLM候选人选择的影响，填补了现有文献的空白，揭示了招聘过程中的潜在偏见。

**关键设计**：实验中控制了候选人的性别、种族、资格和经验等因素，确保结果的有效性和可靠性，采用定量分析方法评估LLMs的选择偏见。

## 📊 实验亮点

实验结果显示，在相同条件下，LLMs更倾向于选择未披露残疾的候选人，选择率显著高于选择不披露残疾状态的候选人。这一发现揭示了LLMs在候选人选择中存在的偏见，强调了招聘过程中的公平性问题。

## 🎯 应用场景

该研究的结果对招聘行业具有重要的实际价值，能够帮助企业在使用LLMs进行候选人筛选时，识别和减少潜在的偏见，从而促进更公平的招聘实践。此外，研究结果也为政策制定者提供了参考，推动多样性和包容性倡议的实施。

## 📄 摘要（原文）

> As large language models (LLMs) become increasingly integrated into hiring processes, concerns about fairness have gained prominence. When applying for jobs, companies often request/require demographic information, including gender, race, and disability or veteran status. This data is collected to support diversity and inclusion initiatives, but when provided to LLMs, especially disability-related information, it raises concerns about potential biases in candidate selection outcomes. Many studies have highlighted how disability can impact CV screening, yet little research has explored the specific effect of voluntarily disclosed information on LLM-driven candidate selection. This study seeks to bridge that gap. When candidates shared identical gender, race, qualifications, experience, and backgrounds, and sought jobs with minimal employment rate gaps between individuals with and without disabilities (e.g., Cashier, Software Developer), LLMs consistently favored candidates who disclosed that they had no disability. Even in cases where candidates chose not to disclose their disability status, the LLMs were less likely to select them compared to those who explicitly stated they did not have a disability.

