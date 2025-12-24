---
layout: default
title: Large Language Model-Driven Dynamic Assessment of Grammatical Accuracy in English Language Learner Writing
---

# Large Language Model-Driven Dynamic Assessment of Grammatical Accuracy in English Language Learner Writing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00931" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00931v1</a>
  <a href="https://arxiv.org/pdf/2505.00931.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00931v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00931v1', 'Large Language Model-Driven Dynamic Assessment of Grammatical Accuracy in English Language Learner Writing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timur Jaganov, John Blake, Julián Villegas, Nicholas Carr

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-02

**备注**: 15 pages, 8 Figures. This work has been submitted to the IEEE for possible publication

**期刊**: IEEE ACCESS, 2025, Volume 13, pp. 151538-151550

**DOI**: [10.1109/ACCESS.2025.3603191](https://doi.org/10.1109/ACCESS.2025.3603191)

---

## 💡 一句话要点

**提出基于大型语言模型的动态评估方法以提升英语写作准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态评估` `大型语言模型` `英语学习` `语法辅导` `实时反馈` `教育技术` `智能辅导`

## 📋 核心要点

1. 现有的动态评估方法在大规模英语学习者中实施时面临效率和反馈质量的挑战。
2. 本研究提出DynaWrite应用，通过整合多种大型语言模型，提供实时的语法反馈以提升学习效果。
3. 实验结果显示，GPT-4o在语法错误识别和反馈质量上优于其他模型，具备良好的实时响应性和系统稳定性。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在动态评估（DA）中的应用潜力。为此，我们开发了DynaWrite，一个模块化的语法辅导应用，支持多种LLM生成动态反馈。初步测试显示，GPT-4o和神经聊天模型在语言学习课堂中具有较高的DA扩展潜力。进一步测试发现，两者在识别用户句子中的语法错误方面表现相似，但GPT-4o在DA质量上始终优于神经聊天，能够生成清晰、一致且逐步明确的提示。通过详细的性能测试，确认了实时响应性和系统稳定性，GPT-4o展现出足够的速度和稳定性。本研究表明，LLMs可以用于扩展动态评估，从而使其能够在比传统教师-学习者环境中更大规模地实施。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统动态评估在大规模英语学习者中实施的效率低下和反馈质量不足的问题。现有方法往往依赖教师的个别指导，难以满足大规模学习需求。

**核心思路**：通过开发DynaWrite应用，结合多种大型语言模型，提供实时、动态的语法反馈，旨在提高学习者的写作准确性和学习体验。这样的设计使得反馈能够更具个性化和及时性。

**技术框架**：DynaWrite的整体架构包括多个模块：用户输入模块、LLM选择模块、反馈生成模块和用户反馈模块。用户输入模块接收学习者的写作内容，LLM选择模块根据需求选择合适的模型，反馈生成模块提供实时反馈，用户反馈模块用于收集学习者的反馈以优化系统。

**关键创新**：本研究的主要创新在于将多种大型语言模型整合到动态评估中，尤其是GPT-4o在反馈质量上的显著提升，使其在语法辅导中表现优于传统方法。

**关键设计**：在模型选择上，重点测试了21种LLM，最终选择GPT-4o和神经聊天模型。GPT-4o在生成反馈时，采用了逐步明确的提示设计，确保学习者能够理解和应用反馈。

## 📊 实验亮点

实验结果表明，GPT-4o在语法错误识别和反馈质量上均优于神经聊天模型，能够生成清晰且一致的提示。具体而言，GPT-4o在动态评估中的表现稳定，实时响应速度快，适合大规模应用。

## 🎯 应用场景

该研究的潜在应用领域包括英语语言学习、在线教育平台和智能辅导系统。通过利用大型语言模型，教育机构可以为更多学习者提供个性化的语法辅导，提升学习效果，降低教师负担，促进教育公平。未来，随着技术的进步，该方法有望扩展到其他语言学习和写作领域。

## 📄 摘要（原文）

> This study investigates the potential for Large Language Models (LLMs) to scale-up Dynamic Assessment (DA). To facilitate such an investigation, we first developed DynaWrite-a modular, microservices-based grammatical tutoring application which supports multiple LLMs to generate dynamic feedback to learners of English. Initial testing of 21 LLMs, revealed GPT-4o and neural chat to have the most potential to scale-up DA in the language learning classroom. Further testing of these two candidates found both models performed similarly in their ability to accurately identify grammatical errors in user sentences. However, GPT-4o consistently outperformed neural chat in the quality of its DA by generating clear, consistent, and progressively explicit hints. Real-time responsiveness and system stability were also confirmed through detailed performance testing, with GPT-4o exhibiting sufficient speed and stability. This study shows that LLMs can be used to scale-up dynamic assessment and thus enable dynamic assessment to be delivered to larger groups than possible in traditional teacher-learner settings.

