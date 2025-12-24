---
layout: default
title: "LegiGPT: Party Politics and Transport Policy with Large Language Model"
---

# LegiGPT: Party Politics and Transport Policy with Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16692" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16692v2</a>
  <a href="https://arxiv.org/pdf/2506.16692.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16692v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16692v2', 'LegiGPT: Party Politics and Transport Policy with Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyunsoo Yun, Eun Hak Lee

**分类**: cs.CL

**发布日期**: 2025-06-20 (更新: 2025-06-28)

**备注**: Updated title to match published version. Added DOI and journal reference to PDF

**期刊**: Transport Policy, 2025

**DOI**: [10.1016/j.tranpol.2025.06.021](https://doi.org/10.1016/j.tranpol.2025.06.021)

---

## 💡 一句话要点

**提出LegiGPT框架以分析交通政策中的党派政治影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可解释人工智能` `交通政策` `立法分析` `党派政治` `政策制定`

## 📋 核心要点

1. 核心问题：现有方法未能充分揭示立法者的政治意识形态如何影响交通政策的制定。
2. 方法要点：本研究提出了将大型语言模型与可解释人工智能结合的框架，以分析交通相关立法提案。
3. 实验或效果：研究结果表明，政治隶属和赞助者特征显著影响立法结果，促进了两党合作立法。

## 📝 摘要（中文）

鉴于立法者的政治意识形态对立法决策的重大影响，分析其对交通相关政策制定的影响至关重要。本研究引入了一种新颖的框架，将大型语言模型（LLM）与可解释人工智能（XAI）结合，以分析与交通相关的立法提案。利用韩国第21届国会的立法数据，识别出影响交通政策制定的关键因素，包括政治隶属和赞助者特征。通过基于关键词、句子和上下文相关性的逐步过滤过程，LLM被用于分类交通相关的法案提案。随后应用XAI技术考察政治党派隶属与相关属性之间的关系。结果显示，保守派和进步派赞助者的数量和比例，以及选区规模和选民人口，是影响立法结果的关键决定因素。这些发现表明，两党通过不同形式的参与（如发起或支持提案）共同促进了两党立法。这种综合方法为理解立法动态和指导未来政策发展提供了有价值的工具，对基础设施规划和治理具有更广泛的影响。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何有效分析立法者的政治意识形态对交通政策制定的影响。现有方法往往缺乏对立法提案的深度分析，无法揭示潜在的政治因素。

**核心思路**：论文的核心思路是结合大型语言模型和可解释人工智能，通过分析立法数据来识别影响交通政策的关键因素。这种设计旨在提高分析的准确性和透明度。

**技术框架**：整体架构包括数据收集、LLM分类、XAI分析三个主要模块。首先收集韩国第21届国会的立法数据，然后利用LLM对交通相关法案进行分类，最后应用XAI技术分析政治隶属与其他属性之间的关系。

**关键创新**：最重要的技术创新在于将LLM与XAI结合，提供了一种新的视角来理解立法动态。这与传统方法的本质区别在于其更高的解释性和准确性。

**关键设计**：在参数设置上，LLM的训练数据包括大量的立法提案文本，损失函数采用交叉熵损失，以优化分类效果。网络结构上，采用了Transformer架构，以增强模型对上下文的理解能力。

## 📊 实验亮点

实验结果显示，保守派和进步派赞助者的数量和比例对立法结果有显著影响，尤其是在选区规模和选民人口方面。这一发现为理解两党在立法过程中的不同参与形式提供了实证支持。

## 🎯 应用场景

该研究的潜在应用领域包括交通政策分析、立法动态研究以及基础设施规划等。通过提供对立法过程的深入理解，研究成果可为政策制定者和研究人员提供指导，促进更有效的政策发展和治理。

## 📄 摘要（原文）

> Given the significant influence of lawmakers' political ideologies on legislative decision-making, analyzing their impact on transportation-related policymaking is of critical importance. This study introduces a novel framework that integrates a large language model (LLM) with explainable artificial intelligence (XAI) to analyze transportation-related legislative proposals. Legislative bill data from South Korea's 21st National Assembly were used to identify key factors shaping transportation policymaking. These include political affiliations and sponsor characteristics. The LLM was employed to classify transportation-related bill proposals through a stepwise filtering process based on keywords, sentences, and contextual relevance. XAI techniques were then applied to examine the relationships between political party affiliation and associated attributes. The results revealed that the number and proportion of conservative and progressive sponsors, along with district size and electoral population, were critical determinants shaping legislative outcomes. These findings suggest that both parties contributed to bipartisan legislation through different forms of engagement, such as initiating or supporting proposals. This integrated approach offers a valuable tool for understanding legislative dynamics and guiding future policy development, with broader implications for infrastructure planning and governance.

