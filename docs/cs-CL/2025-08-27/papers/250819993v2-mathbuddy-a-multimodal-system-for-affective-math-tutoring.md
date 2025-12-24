---
layout: default
title: "MathBuddy: A Multimodal System for Affective Math Tutoring"
---

# MathBuddy: A Multimodal System for Affective Math Tutoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19993" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19993v2</a>
  <a href="https://arxiv.org/pdf/2508.19993.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19993v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19993v2', 'MathBuddy: A Multimodal System for Affective Math Tutoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Maximilian Dennerlein, Nina Christine Hubig, Philipp Wintersberger, Yufang Hou

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-08-27 (更新: 2025-09-24)

**备注**: Accepted at EMNLP 2025 (Demo Track)

**🔗 代码/项目**: [GITHUB](https://github.com/ITU-NLP/MathBuddy)

---

## 💡 一句话要点

**提出MathBuddy以解决情感状态对数学学习影响的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感计算` `教育技术` `多模态系统` `个性化学习` `大型语言模型`

## 📋 核心要点

1. 现有的教育技术模型未能考虑学生的情感状态，导致学习效果不佳。
2. MathBuddy通过动态建模学生情感并映射到教学策略，提升了辅导的同理心。
3. 实验结果显示，模型在性能上提升了23点，整体得分提升了3点，验证了情感建模的有效性。

## 📝 摘要（中文）

随着基于大型语言模型（LLM）的对话系统的快速普及，教育技术的格局正在发生变化。然而，现有的学习模型未能考虑学生的情感状态。多项教育心理学研究表明，积极或消极的情感状态会影响学生的学习能力。为了解决这一问题，我们提出了MathBuddy，一个情感感知的LLM驱动数学辅导系统，它动态建模学生的情感，并将其映射到相关的教学策略，使辅导与学生的对话更加富有同理心。学生的情感通过对话文本和面部表情捕捉，并从这两种模态中聚合，以自信地提示我们的LLM辅导员做出情感意识的回应。我们在八个教学维度上使用自动评估指标和用户研究评估了我们的模型，报告了23点的性能提升和3点的整体提升，强有力地支持了通过建模学生情感来改善LLM辅导员教学能力的假设。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有教育技术模型忽视学生情感状态的问题。研究表明，情感状态对学习能力有显著影响，现有方法未能有效整合这一因素。

**核心思路**：论文提出的MathBuddy系统通过捕捉学生的情感状态，并将其与教学策略相结合，提供情感意识的辅导体验。这种设计旨在提升学生的学习动机和效果。

**技术框架**：MathBuddy的整体架构包括情感识别模块、对话生成模块和反馈调整模块。情感识别模块通过分析对话文本和面部表情来捕捉情感，生成模块则基于情感信息生成适当的教学内容。

**关键创新**：本研究的主要创新在于将情感识别与LLM结合，形成一个多模态的情感感知辅导系统。这与传统的基于文本的辅导方法有本质区别，后者通常忽视情感因素。

**关键设计**：在模型设计中，采用了多模态数据融合技术，结合了文本分析和面部表情识别。损失函数设计上，考虑了情感识别的准确性和教学效果的提升，确保模型在多维度上进行优化。

## 📊 实验亮点

实验结果显示，MathBuddy在八个教学维度上取得了显著的性能提升，使用胜率提升了23点，整体DAMR得分提升了3点。这些结果强有力地支持了情感建模对提升LLM辅导能力的有效性，展示了其在教育技术中的应用潜力。

## 🎯 应用场景

MathBuddy系统具有广泛的应用潜力，尤其在个性化教育和情感智能辅导领域。它可以被应用于在线学习平台、教育机器人以及其他需要情感交互的教育工具中，提升学生的学习体验和效果。未来，随着情感计算技术的发展，MathBuddy可能会在更多教育场景中发挥重要作用。

## 📄 摘要（原文）

> The rapid adoption of LLM-based conversational systems is already transforming the landscape of educational technology. However, the current state-of-the-art learning models do not take into account the student's affective states. Multiple studies in educational psychology support the claim that positive or negative emotional states can impact a student's learning capabilities. To bridge this gap, we present MathBuddy, an emotionally aware LLM-powered Math Tutor, which dynamically models the student's emotions and maps them to relevant pedagogical strategies, making the tutor-student conversation a more empathetic one. The student's emotions are captured from the conversational text as well as from their facial expressions. The student's emotions are aggregated from both modalities to confidently prompt our LLM Tutor for an emotionally-aware response. We have evaluated our model using automatic evaluation metrics across eight pedagogical dimensions and user studies. We report a massive 23 point performance gain using the win rate and a 3 point gain at an overall level using DAMR scores which strongly supports our hypothesis of improving LLM-based tutor's pedagogical abilities by modeling students' emotions. Our dataset and code are available at: https://github.com/ITU-NLP/MathBuddy .

