---
layout: default
title: "Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study"
---

# Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17410" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17410v1</a>
  <a href="https://arxiv.org/pdf/2506.17410.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17410v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17410v1', 'Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, Kenneth R. Koedinger

**分类**: cs.CL, cs.CY

**发布日期**: 2025-06-20

**备注**: Short research paper accepted at EC-TEL 2025

---

## 💡 一句话要点

**利用大型语言模型评估真实对话中的辅导行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育评估` `辅导行为` `生成性人工智能` `数学辅导` `自动化评估` `真实对话分析`

## 📋 核心要点

1. 现有方法在大规模分析辅导行为与学生学习成果之间的关系时面临挑战，尤其是基于音频转录的分析。
2. 本研究提出利用大型语言模型（LLMs）来识别和评估辅导者在真实数学辅导中的具体行为，特别是有效表扬和错误回应。
3. 实验结果显示，模型在识别辅导者行为方面具有高准确率，且与人类判断高度一致，展示了LLMs在教育评估中的潜力。

## 📝 摘要（中文）

辅导能够提升学生的学习成就，但基于音频转录识别和研究哪些辅导行为与学生学习最相关仍是一个开放的研究问题。本研究探讨了使用生成性人工智能识别和评估真实数学辅导中具体辅导行为的可行性和可扩展性。我们分析了50份随机选择的大学生远程辅导中学数学的转录文本。通过使用GPT-4等模型，我们评估了辅导者在有效表扬和回应学生数学错误方面的应用。所有模型都可靠地检测到相关情况，并有效评估了辅导者对最佳实践的遵循程度。我们提出了一种具有成本效益的提示策略，并讨论了在真实环境中使用大型语言模型支持可扩展评估的实际意义。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何有效识别和评估辅导者在真实对话中所采取的具体辅导行为的问题。现有方法在大规模分析辅导行为与学生学习成果之间的关系时存在局限，尤其是依赖于音频转录的分析。

**核心思路**：本研究的核心思路是利用大型语言模型（LLMs）来自动化识别和评估辅导者的行为，特别是有效表扬和回应学生错误的能力。通过这种方式，可以在大规模的真实教育环境中进行有效的评估。

**技术框架**：整体架构包括数据收集、模型选择、行为识别和评估四个主要模块。首先，随机选择50份转录文本作为数据集；然后，使用GPT-4等模型进行行为识别；最后，评估模型的表现与人类判断的对比。

**关键创新**：本研究的关键创新在于提出了一种利用LLMs进行教育评估的新方法，特别是在真实场景中应用的可行性和有效性。这与传统的手动分析方法形成了鲜明对比，显著提高了效率和准确性。

**关键设计**：在模型选择上，使用了多种LLMs（如GPT-4、GPT-4o等），并通过设计特定的提示策略来优化模型的表现。模型的评估标准包括准确率和与人类判断的一致性，确保了评估结果的可靠性。

## 📊 实验亮点

实验结果显示，模型在识别辅导者提供表扬的准确率高达94-98%，而识别学生数学错误的准确率为82-88%。此外，模型在评估辅导者遵循最佳实践方面与人类判断的相似度达到了83-89%和73-77%，展示了其在教育评估中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线辅导平台和教师培训等。通过自动化评估辅导行为，教育工作者可以更好地理解和优化辅导策略，从而提升学生的学习效果。未来，该方法可能推动教育评估的标准化和智能化进程。

## 📄 摘要（原文）

> Tutoring improves student achievement, but identifying and studying what tutoring actions are most associated with student learning at scale based on audio transcriptions is an open research problem. This present study investigates the feasibility and scalability of using generative AI to identify and evaluate specific tutor moves in real-life math tutoring. We analyze 50 randomly selected transcripts of college-student remote tutors assisting middle school students in mathematics. Using GPT-4, GPT-4o, GPT-4-turbo, Gemini-1.5-pro, and LearnLM, we assess tutors' application of two tutor skills: delivering effective praise and responding to student math errors. All models reliably detected relevant situations, for example, tutors providing praise to students (94-98% accuracy) and a student making a math error (82-88% accuracy) and effectively evaluated the tutors' adherence to tutoring best practices, aligning closely with human judgments (83-89% and 73-77%, respectively). We propose a cost-effective prompting strategy and discuss practical implications for using large language models to support scalable assessment in authentic settings. This work further contributes LLM prompts to support reproducibility and research in AI-supported learning.

