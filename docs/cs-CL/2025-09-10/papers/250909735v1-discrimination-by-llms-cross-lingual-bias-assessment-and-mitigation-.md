---
layout: default
title: "Discrimination by LLMs: Cross-lingual Bias Assessment and Mitigation in Decision-Making and Summarisation"
---

# Discrimination by LLMs: Cross-lingual Bias Assessment and Mitigation in Decision-Making and Summarisation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09735" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09735v1</a>
  <a href="https://arxiv.org/pdf/2509.09735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09735v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09735v1', 'Discrimination by LLMs: Cross-lingual Bias Assessment and Mitigation in Decision-Making and Summarisation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Willem Huijzer, Jieying Chen

**分类**: cs.CL

**发布日期**: 2025-09-10

**备注**: 7 pages

---

## 💡 一句话要点

**评估并缓解LLM在决策和摘要任务中的跨语言偏见，关注背景、性别和年龄歧视。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见评估` `跨语言分析` `决策任务` `摘要任务`

## 📋 核心要点

1. 现有LLM在决策和摘要任务中存在偏见，尤其是在涉及不同背景、性别和年龄的人群时，可能导致不公平的结果。
2. 该研究通过构建包含多种人口统计变量和指令的提示，系统地评估了GPT-3.5和GPT-4o在决策和摘要任务中的偏见。
3. 实验结果表明，LLM在决策任务中存在显著偏见，且偏见模式在不同语言间具有相似性，提示指导的缓解策略能够部分减少偏见。

## 📝 摘要（中文）

大型语言模型（LLM）快速融入各个领域，引发了对社会不平等和信息偏见的担忧。本研究考察了LLM中与背景、性别和年龄相关的偏见，重点关注其对决策和摘要任务的影响。此外，该研究还检验了这些偏见的跨语言传播，并评估了提示指导缓解策略的有效性。我们使用Tamkin等人（2023）数据集的改编版本（翻译成荷兰语），为决策任务创建了151,200个独特的提示，为摘要任务创建了176,400个。在GPT-3.5和GPT-4o上测试了各种人口统计变量、指令、显著性水平和语言。分析表明，两种模型在决策过程中都存在显著偏见，偏向于女性、年轻年龄和某些背景（如非裔美国人背景）。相比之下，摘要任务显示出极少的偏见证据，但GPT-3.5在英语中出现了显著的年龄相关差异。跨语言分析表明，英语和荷兰语之间的偏见模式大致相似，但在特定人口统计类别中观察到显著差异。新提出的缓解指令虽然无法完全消除偏见，但显示出减少偏见的潜力。最有效的指令平均减少了27%的最有利和最不利人口统计数据之间的差距。值得注意的是，与GPT-3.5相反，GPT-4o在英语的所有提示中都显示出偏见减少，表明了新模型中基于提示的缓解的特定潜力。这项研究强调了谨慎采用LLM和特定于上下文的偏见测试的重要性，突出了持续开发有效缓解策略以确保负责任地部署AI的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在量化和减轻大型语言模型（LLM）在决策和摘要任务中存在的偏见。现有方法缺乏对跨语言偏见传播的系统性评估，并且缓解策略的效果有待验证。LLM的偏见可能导致对特定人群的不公平待遇，因此需要深入研究并提出有效的缓解方案。

**核心思路**：核心思路是通过构建包含不同人口统计变量（背景、性别、年龄）和指令的提示，系统性地评估LLM在决策和摘要任务中的偏见。同时，通过将提示翻译成多种语言，研究偏见的跨语言传播。此外，设计基于提示的缓解策略，旨在减少LLM的偏见输出。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据集构建：基于Tamkin等人(2023)的数据集，构建包含多种人口统计变量和指令的提示，并翻译成荷兰语。2) 模型评估：使用GPT-3.5和GPT-4o对构建的提示进行评估，分析其在决策和摘要任务中的偏见。3) 跨语言分析：比较英语和荷兰语的偏见模式，研究偏见的跨语言传播。4) 缓解策略：设计基于提示的缓解策略，并评估其效果。

**关键创新**：该研究的关键创新点在于：1) 系统性地评估了LLM在决策和摘要任务中的跨语言偏见。2) 提出了基于提示的缓解策略，并验证了其在减少偏见方面的潜力。3) 揭示了GPT-4o在减少偏见方面优于GPT-3.5的特性，表明了新模型在偏见缓解方面的潜力。

**关键设计**：该研究的关键设计包括：1) 构建包含多种人口统计变量（背景、性别、年龄）和指令的提示，以全面评估LLM的偏见。2) 使用决策和摘要两种任务，以研究偏见在不同任务中的表现。3) 将提示翻译成荷兰语，以研究偏见的跨语言传播。4) 设计基于提示的缓解策略，例如，指示模型考虑公平性或提供更平衡的输出。

## 📊 实验亮点

实验结果表明，GPT-3.5和GPT-4o在决策任务中存在显著偏见，偏向于女性、年轻年龄和某些背景。跨语言分析表明，英语和荷兰语之间的偏见模式大致相似。提出的缓解指令能够部分减少偏见，最有效的指令平均减少了27%的最有利和最不利人口统计数据之间的差距。GPT-4o在减少偏见方面优于GPT-3.5。

## 🎯 应用场景

该研究成果可应用于各种需要使用LLM进行决策或内容生成的领域，例如招聘、信贷评估、新闻摘要等。通过识别和缓解LLM中的偏见，可以提高决策的公平性和透明度，避免对特定人群造成歧视。未来的研究可以进一步探索更有效的缓解策略，并将其应用于更广泛的LLM和任务中。

## 📄 摘要（原文）

> The rapid integration of Large Language Models (LLMs) into various domains raises concerns about societal inequalities and information bias. This study examines biases in LLMs related to background, gender, and age, with a focus on their impact on decision-making and summarization tasks. Additionally, the research examines the cross-lingual propagation of these biases and evaluates the effectiveness of prompt-instructed mitigation strategies. Using an adapted version of the dataset by Tamkin et al. (2023) translated into Dutch, we created 151,200 unique prompts for the decision task and 176,400 for the summarisation task. Various demographic variables, instructions, salience levels, and languages were tested on GPT-3.5 and GPT-4o. Our analysis revealed that both models were significantly biased during decision-making, favouring female gender, younger ages, and certain backgrounds such as the African-American background. In contrast, the summarisation task showed minimal evidence of bias, though significant age-related differences emerged for GPT-3.5 in English. Cross-lingual analysis showed that bias patterns were broadly similar between English and Dutch, though notable differences were observed across specific demographic categories. The newly proposed mitigation instructions, while unable to eliminate biases completely, demonstrated potential in reducing them. The most effective instruction achieved a 27\% mean reduction in the gap between the most and least favorable demographics. Notably, contrary to GPT-3.5, GPT-4o displayed reduced biases for all prompts in English, indicating the specific potential for prompt-based mitigation within newer models. This research underscores the importance of cautious adoption of LLMs and context-specific bias testing, highlighting the need for continued development of effective mitigation strategies to ensure responsible deployment of AI.

