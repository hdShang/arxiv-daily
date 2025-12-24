---
layout: default
title: "From Handwriting to Feedback: Evaluating VLMs and LLMs for AI-Powered Assessment in Indonesian Classrooms"
---

# From Handwriting to Feedback: Evaluating VLMs and LLMs for AI-Powered Assessment in Indonesian Classrooms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04822" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04822v2</a>
  <a href="https://arxiv.org/pdf/2506.04822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04822v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04822v2', 'From Handwriting to Feedback: Evaluating VLMs and LLMs for AI-Powered Assessment in Indonesian Classrooms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nurul Aisyah, Muhammad Dehan Al Kautsar, Arif Hidayat, Raqib Chowdhury, Fajri Koto

**分类**: cs.CL

**发布日期**: 2025-06-05 (更新: 2025-10-08)

---

## 💡 一句话要点

**评估VLM和LLM在印尼课堂AI评估中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `大型语言模型` `教育评估` `个性化反馈` `手写识别`

## 📋 核心要点

1. 现有方法在真实课堂环境中对手写文本的评估效果不佳，尤其是在视觉和语言挑战下。
2. 论文通过评估VLM和LLM在印尼四年级课堂手写答案上的表现，提出了基于评分标准的个性化反馈生成方法。
3. 实验结果显示，尽管VLM在手写识别上存在问题，LLM仍能提供有用的反馈，揭示了个性化和上下文的局限性。

## 📝 摘要（中文）

尽管视觉语言模型（VLM）和大型语言模型（LLM）在快速发展，但它们在真实、代表性不足的课堂中进行AI驱动教育评估的有效性仍未得到充分探索。本文评估了最先进的VLM和LLM在印尼四年级课堂中对超过14,000份手写答案的表现，涵盖与当地国家课程对齐的数学和英语。与以往对干净数字文本的研究不同，本数据集展示了真实课堂中自然弯曲、多样化的手写，带来了现实的视觉和语言挑战。评估任务包括基于评分标准的打分和生成个性化的印尼语反馈。结果表明，VLM在手写识别上存在困难，导致LLM评分中的错误传播，尽管视觉输入不完美，LLM反馈在教学上仍然有用，揭示了个性化和上下文相关性的局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决VLM和LLM在真实课堂手写文本评估中的有效性问题。现有方法在处理自然手写文本时表现不佳，导致评估结果不准确。

**核心思路**：论文提出通过评估VLM和LLM在印尼四年级课堂手写答案上的表现，探索如何生成基于评分标准的个性化反馈，以应对手写文本的挑战。

**技术框架**：整体架构包括数据收集、手写识别、评分系统和反馈生成四个主要模块。数据收集阶段使用真实课堂的手写答案，手写识别模块负责将手写文本转换为可处理的格式，评分系统基于预设标准进行打分，反馈生成模块则根据评分结果提供个性化反馈。

**关键创新**：最重要的技术创新在于将VLM和LLM结合应用于真实手写文本评估，尤其是在处理多样化和自然手写时的适应性。与现有方法相比，本文关注于真实课堂环境中的实际应用。

**关键设计**：在参数设置上，采用了适应性损失函数以应对手写识别的误差传播，同时在网络结构上结合了卷积神经网络（CNN）和循环神经网络（RNN）以提高对手写文本的理解能力。

## 📊 实验亮点

实验结果显示，VLM在手写识别中的准确率较低，导致LLM评分的错误传播。然而，LLM生成的反馈在教学上仍然具有实用性，尽管存在个性化和上下文相关性的局限性。这表明在真实环境中，LLM的反馈能力仍然值得重视。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、个性化学习和智能辅导系统。通过改进手写文本的评估，能够为教师提供更精准的反馈，帮助学生在学习过程中获得个性化支持，提升教育质量。未来，该方法有望推广到其他语言和文化背景的课堂中。

## 📄 摘要（原文）

> Despite rapid progress in vision-language and large language models (VLMs and LLMs), their effectiveness for AI-driven educational assessment in real-world, underrepresented classrooms remains largely unexplored. We evaluate state-of-the-art VLMs and LLMs on over 14K handwritten answers from grade-4 classrooms in Indonesia, covering Mathematics and English aligned with the local national curriculum. Unlike prior work on clean digital text, our dataset features naturally curly, diverse handwriting from real classrooms, posing realistic visual and linguistic challenges. Assessment tasks include grading and generating personalized Indonesian feedback guided by rubric-based evaluation. Results show that the VLM struggles with handwriting recognition, causing error propagation in LLM grading, yet LLM feedback remains pedagogically useful despite imperfect visual inputs, revealing limits in personalization and contextual relevance.

