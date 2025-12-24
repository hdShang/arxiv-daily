---
layout: default
title: Characterizing the Investigative Methods of Fictional Detectives with Large Language Models
---

# Characterizing the Investigative Methods of Fictional Detectives with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07601" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07601v1</a>
  <a href="https://arxiv.org/pdf/2505.07601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07601v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07601v1', 'Characterizing the Investigative Methods of Fictional Detectives with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Edirlei Soares de Lima, Marco A. Casanova, Bruno Feijó, Antonio L. Furtado

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出AI驱动的方法系统化分析虚构侦探的调查手法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算叙事学` `虚构侦探` `大型语言模型` `调查手法分析` `自动化叙事生成`

## 📋 核心要点

1. 现有的文学分析方法通常集中于少数虚构侦探，缺乏可扩展性，难以提取独特特征以指导叙事生成。
2. 本文提出了一种多阶段的AI驱动工作流程，利用大型语言模型提取、综合和验证虚构侦探的调查特征。
3. 在七位经典侦探的测试中，方法实现了91.43%的准确率，证明了其在捕捉侦探调查方法上的有效性。

## 📝 摘要（中文）

侦探小说作为一种复杂叙事结构和以角色驱动的故事讲述的文学类型，为计算叙事学带来了独特挑战。尽管传统文学研究对虚构侦探的手法和原型提供了深刻见解，但这些分析往往局限于少数角色，缺乏可扩展性。本文提出了一种AI驱动的方法，系统性地表征虚构侦探的调查手法。通过对15种大型语言模型的多阶段工作流程进行探索，本文验证了七位经典侦探的独特调查风格，最终实现了91.43%的准确率，展示了该方法在捕捉侦探独特调查方式方面的有效性。这项工作为计算叙事学提供了可扩展的角色分析框架，具有在AI驱动的互动叙事和自动化叙事生成中的潜在应用。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文学分析方法对虚构侦探的研究局限，尤其是缺乏可扩展性和系统性的问题。现有方法往往只关注少数角色，无法全面提取调查特征。

**核心思路**：论文的核心思路是利用大型语言模型的能力，通过多阶段工作流程系统化地分析虚构侦探的调查手法，以实现对不同角色特征的全面捕捉和验证。

**技术框架**：整体架构包括数据收集、特征提取、特征综合和验证四个主要阶段。首先，收集经典侦探的文本数据；其次，利用15种大型语言模型提取调查特征；然后，综合这些特征并进行验证。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于虚构侦探的调查手法分析，提供了一种可扩展的框架，区别于传统的基于文本的分析方法。

**关键设计**：在特征提取阶段，采用了多种大型语言模型以确保特征的多样性和准确性，验证阶段则通过与现有文学分析结果对比，确保了结果的可靠性。

## 📊 实验亮点

实验结果显示，所提出的方法在七位经典侦探的调查手法分析中实现了91.43%的准确率，验证了其有效性。与传统方法相比，该方法在特征提取和验证的系统性和可扩展性上有显著提升，展示了AI技术在文学分析中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括AI驱动的互动叙事和自动化叙事生成，能够为创作者提供丰富的角色分析工具，提升故事创作的深度和复杂性。未来，该方法还可能扩展到其他文学类型的分析中，推动计算叙事学的发展。

## 📄 摘要（原文）

> Detective fiction, a genre defined by its complex narrative structures and character-driven storytelling, presents unique challenges for computational narratology, a research field focused on integrating literary theory into automated narrative generation. While traditional literary studies have offered deep insights into the methods and archetypes of fictional detectives, these analyses often focus on a limited number of characters and lack the scalability needed for the extraction of unique traits that can be used to guide narrative generation methods. In this paper, we present an AI-driven approach for systematically characterizing the investigative methods of fictional detectives. Our multi-phase workflow explores the capabilities of 15 Large Language Models (LLMs) to extract, synthesize, and validate distinctive investigative traits of fictional detectives. This approach was tested on a diverse set of seven iconic detectives - Hercule Poirot, Sherlock Holmes, William Murdoch, Columbo, Father Brown, Miss Marple, and Auguste Dupin - capturing the distinctive investigative styles that define each character. The identified traits were validated against existing literary analyses and further tested in a reverse identification phase, achieving an overall accuracy of 91.43%, demonstrating the method's effectiveness in capturing the distinctive investigative approaches of each detective. This work contributes to the broader field of computational narratology by providing a scalable framework for character analysis, with potential applications in AI-driven interactive storytelling and automated narrative generation.

