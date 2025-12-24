---
layout: default
title: "Asking the Right Questions: Benchmarking Large Language Models in the Development of Clinical Consultation Templates"
---

# Asking the Right Questions: Benchmarking Large Language Models in the Development of Clinical Consultation Templates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01159" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01159v2</a>
  <a href="https://arxiv.org/pdf/2508.01159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01159v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01159v2', 'Asking the Right Questions: Benchmarking Large Language Models in the Development of Clinical Consultation Templates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liam G. McCoy, Fateme Nateghi Haredasht, Kanav Chopra, David Wu, David JH Wu, Abass Conteh, Sarita Khemani, Saloni Kumar Maharaj, Vishnu Ravi, Arth Pahwa, Yingjie Weng, Leah Rosengaus, Lena Giang, Kelvin Zhenghao Li, Olivia Jee, Daniel Shirvani, Ethan Goh, Jonathan H. Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-02 (更新: 2025-11-12)

---

## 💡 一句话要点

**评估大型语言模型在临床咨询模板生成中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `临床咨询` `模板生成` `信息优先级` `医疗信息系统`

## 📋 核心要点

1. 现有方法在生成临床咨询模板时，常常无法有效优先考虑最重要的问题，导致信息传递不够高效。
2. 本研究提出了一种多代理管道，结合提示优化、语义自动评分和优先级分析，以提升LLMs生成临床咨询模板的能力。
3. 实验结果显示，尽管某些模型在全面性上表现良好，但在叙述驱动的领域如精神病学和疼痛医学中，性能显著下降。

## 📝 摘要（中文）

本研究评估了大型语言模型（LLMs）生成结构化临床咨询模板的能力，使用了145个由斯坦福eConsult团队开发的专家模板。我们对包括o3、GPT-4o、Kimi K2等前沿模型进行了评估，发现尽管o3在全面性上表现出色（高达92.2%），但在长度限制下，模型生成的模板往往过长，且未能正确优先考虑最重要的临床问题。研究结果表明，LLMs能够增强医生之间的结构化信息交流，但需要更强的评估方法来捕捉模型在实际沟通中的优先级能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在生成临床咨询模板时的优先级排序和信息过载问题。现有方法在生成模板时常常忽视临床重要性，导致信息传递效率低下。

**核心思路**：通过构建一个多代理管道，结合提示优化和语义自动评分，论文旨在提升模型生成的临床问题模板的结构化和优先级排序能力。这样的设计可以更好地适应医生在实际沟通中的需求。

**技术框架**：整体架构包括多个模块：首先是提示优化模块，旨在生成更有效的输入提示；其次是语义自动评分模块，用于评估生成模板的质量；最后是优先级分析模块，确保生成的问题按照临床重要性排序。

**关键创新**：本研究的创新点在于引入了多代理管道的概念，结合了不同的评估方法，以更全面地评估模型在临床场景中的表现。这与传统方法的单一评估方式形成了鲜明对比。

**关键设计**：在参数设置上，研究使用了多种模型进行对比，特别关注了生成模板的长度和内容的优先级。损失函数设计上，强调了临床问题的优先级，以确保生成的模板不仅全面而且简洁。

## 📊 实验亮点

实验结果显示，o3模型在模板的全面性上达到了92.2%的高分，但在长度限制下生成的模板过长，且未能优先考虑最重要的临床问题。尤其在精神病学和疼痛医学等叙述驱动的领域，模型性能显著下降，提示了在这些领域应用LLMs的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括电子医疗咨询、临床决策支持系统和医疗信息系统等。通过提升大型语言模型在生成临床咨询模板方面的能力，可以有效改善医生之间的信息交流，提高医疗服务的效率和质量，未来可能对医疗行业产生深远影响。

## 📄 摘要（原文）

> This study evaluates the capacity of large language models (LLMs) to generate structured clinical consultation templates for electronic consultation. Using 145 expert-crafted templates developed and routinely used by Stanford's eConsult team, we assess frontier models -- including o3, GPT-4o, Kimi K2, Claude 4 Sonnet, Llama 3 70B, and Gemini 2.5 Pro -- for their ability to produce clinically coherent, concise, and prioritized clinical question schemas. Through a multi-agent pipeline combining prompt optimization, semantic autograding, and prioritization analysis, we show that while models like o3 achieve high comprehensiveness (up to 92.2\%), they consistently generate excessively long templates and fail to correctly prioritize the most clinically important questions under length constraints. Performance varies across specialties, with significant degradation in narrative-driven fields such as psychiatry and pain medicine. Our findings demonstrate that LLMs can enhance structured clinical information exchange between physicians, while highlighting the need for more robust evaluation methods that capture a model's ability to prioritize clinically salient information within the time constraints of real-world physician communication.

