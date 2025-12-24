---
layout: default
title: "Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design"
---

# Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16659" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16659v1</a>
  <a href="https://arxiv.org/pdf/2508.16659.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16659v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16659v1', 'Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper

**分类**: cs.CY, cs.AI, cs.HC

**发布日期**: 2025-08-20

**备注**: under review for an [anonymized according to the conference policy] conference

---

## 💡 一句话要点

**将知识学习框架嵌入多智能体系统以提升教育内容设计质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `教学设计` `大型语言模型` `教育技术` `知识学习框架`

## 📋 核心要点

1. 现有的商业大型语言模型在教学设计中缺乏深厚的教育理论支持，导致生成的教学活动质量不高。
2. 本研究提出将知识-学习-教学框架嵌入多智能体系统中，以提升大型语言模型的教学设计能力。
3. 实验结果显示，教师对协作多智能体系统生成的教学活动评价更高，认为其在创造性和课堂适用性上有显著提升。

## 📝 摘要（中文）

K-12教育工作者越来越多地使用大型语言模型（LLMs）来创建教学材料。这些系统在生成流畅、连贯的内容方面表现出色，但往往缺乏高质量教学所需的支持。原因有二：首先，商业LLMs如ChatGPT和Gemini并未预装足够的教学理论；其次，尽管精细的提示工程可以弥补这一差距，但大多数教师缺乏时间或专业知识，难以将教学细节编码到请求中。本研究将教学专业知识从用户提示转移到LLM的内部架构中。我们将成熟的知识-学习-教学（KLI）框架嵌入多智能体系统（MAS），作为复杂的教学设计者。我们测试了三种生成中学数学和科学学习活动的系统，结果显示教师更偏好协作MAS-CMD生成的活动，认为其更具创造性、相关性和课堂适用性。我们的研究表明，将教学原则嵌入LLM系统为创造高质量教育内容提供了可扩展的路径。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有大型语言模型在教学活动设计中缺乏教育理论支持的问题。现有方法主要依赖教师的提示，但教师往往缺乏时间和专业知识，难以有效编码教学细节。

**核心思路**：本研究的核心思路是将教学专业知识嵌入到多智能体系统的内部架构中，从而使系统能够自动生成高质量的教学活动，而不完全依赖教师的提示。

**技术框架**：整体架构包括三个主要模块：单智能体基线系统、角色基础的多智能体系统（MAS）和协作多智能体系统（MAS-CMD）。单智能体系统模拟典型教师提示，角色基础系统中的智能体按顺序工作，而协作系统则通过讨论共同构建活动。

**关键创新**：最重要的技术创新在于将KLI框架嵌入多智能体系统，使其能够在生成教学活动时考虑到教育理论的深度和复杂性。这一设计与现有方法的本质区别在于将教学设计的责任从教师转移到系统内部。

**关键设计**：在系统设计中，采用了角色分配和协作讨论机制，以促进智能体之间的互动和信息共享。此外，系统的评估标准基于Quality Matters（QM） K-12标准，以确保生成内容的质量。

## 📊 实验亮点

实验结果显示，协作多智能体系统（MAS-CMD）生成的教学活动在教师评价中明显优于单智能体基线，教师认为其在创造性、相关性和课堂适用性上有显著提升。尽管系统之间的量化评分差异不大，但定性反馈表明协作系统更受欢迎。

## 🎯 应用场景

该研究的潜在应用领域包括K-12教育、在线学习平台和教育技术工具。通过将教学理论嵌入智能系统，教育工作者可以更高效地生成高质量的教学材料，从而提升学生的学习体验和效果。未来，这种方法可能会推动教育内容生成的自动化和个性化发展。

## 📄 摘要（原文）

> K-12 educators are increasingly using Large Language Models (LLMs) to create instructional materials. These systems excel at producing fluent, coherent content, but often lack support for high-quality teaching. The reason is twofold: first, commercial LLMs, such as ChatGPT and Gemini which are among the most widely accessible to teachers, do not come preloaded with the depth of pedagogical theory needed to design truly effective activities; second, although sophisticated prompt engineering can bridge this gap, most teachers lack the time or expertise and find it difficult to encode such pedagogical nuance into their requests. This study shifts pedagogical expertise from the user's prompt to the LLM's internal architecture. We embed the well-established Knowledge-Learning-Instruction (KLI) framework into a Multi-Agent System (MAS) to act as a sophisticated instructional designer. We tested three systems for generating secondary Math and Science learning activities: a Single-Agent baseline simulating typical teacher prompts; a role-based MAS where agents work sequentially; and a collaborative MAS-CMD where agents co-construct activities through conquer and merge discussion. The generated materials were evaluated by 20 practicing teachers and a complementary LLM-as-a-judge system using the Quality Matters (QM) K-12 standards. While the rubric scores showed only small, often statistically insignificant differences between the systems, the qualitative feedback from educators painted a clear and compelling picture. Teachers strongly preferred the activities from the collaborative MAS-CMD, describing them as significantly more creative, contextually relevant, and classroom-ready. Our findings show that embedding pedagogical principles into LLM systems offers a scalable path for creating high-quality educational content.

