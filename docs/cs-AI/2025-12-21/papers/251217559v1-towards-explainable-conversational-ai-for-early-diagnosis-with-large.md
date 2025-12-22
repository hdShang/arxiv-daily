---
layout: default
title: Towards Explainable Conversational AI for Early Diagnosis with Large Language Models
---

# Towards Explainable Conversational AI for Early Diagnosis with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17559" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17559v1</a>
  <a href="https://arxiv.org/pdf/2512.17559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17559v1', 'Towards Explainable Conversational AI for Early Diagnosis with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maliha Tabassum, M Shamim Kaiser

**分类**: cs.AI

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出基于LLM的对话式AI，用于早期诊断并提升可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对话式AI` `早期诊断` `可解释AI` `检索增强生成` `医疗健康` `GPT-4o`

## 📋 核心要点

1. 现有AI诊断系统交互性和透明度不足，难以有效应用于以患者为中心的真实环境。
2. 利用GPT-4o、RAG和可解释AI技术构建对话式诊断系统，提升诊断透明度。
3. 实验表明，该系统在诊断准确率上显著优于传统机器学习模型，具有临床应用潜力。

## 📝 摘要（中文）

本文提出了一种基于大型语言模型（LLM）的诊断聊天机器人，旨在解决医疗系统中诊断效率低下、成本上升以及专家资源有限等问题。该聊天机器人利用GPT-4o、检索增强生成（RAG）和可解释AI技术，与患者进行动态对话，提取和规范化症状，并通过相似性匹配和自适应提问来确定潜在诊断的优先级。借助思维链（Chain-of-Thought）提示，该系统还提供了更透明的诊断推理过程。实验结果表明，与传统的机器学习模型（如朴素贝叶斯、逻辑回归、SVM、随机森林和KNN）相比，该基于LLM的系统表现出色，达到了90%的准确率和100%的Top-3准确率。这些发现为医疗领域中更透明、交互式和临床相关的AI应用提供了有希望的前景。

## 🔬 方法详解

**问题定义**：现有医疗诊断系统面临效率低、成本高、专家资源有限等问题，且缺乏足够的交互性和透明度，难以满足实际临床需求。传统的AI和深度学习诊断系统通常是黑盒模型，难以解释其诊断结果，导致医生和患者对其信任度不高。因此，如何构建一个交互式、透明且准确的AI诊断系统是亟待解决的问题。

**核心思路**：本文的核心思路是利用大型语言模型（LLM）的强大自然语言处理能力，构建一个能够与患者进行动态对话的诊断聊天机器人。通过对话式交互，系统能够更全面地收集患者的症状信息，并利用检索增强生成（RAG）技术，结合医学知识库进行诊断推理。同时，采用思维链（Chain-of-Thought）提示，使系统能够解释其诊断过程，提高透明度和可信度。

**技术框架**：该诊断聊天机器人的整体架构包含以下几个主要模块：1) 对话管理模块：负责与患者进行对话，收集症状信息。2) 症状规范化模块：将患者描述的症状进行规范化处理，以便进行后续的诊断推理。3) 诊断推理模块：利用RAG技术，结合医学知识库，根据患者的症状信息进行诊断推理，并给出潜在的诊断结果。4) 解释生成模块：采用思维链提示，生成诊断推理过程的解释，提高透明度。5) 优先级排序模块：对潜在的诊断结果进行优先级排序，以便医生进行参考。

**关键创新**：该论文的关键创新在于将大型语言模型（LLM）、检索增强生成（RAG）和可解释AI技术相结合，构建了一个交互式、透明且准确的AI诊断系统。与传统的机器学习模型相比，该系统具有更强的自然语言处理能力和知识推理能力，能够更好地理解患者的症状信息，并给出更准确的诊断结果。同时，通过思维链提示，该系统能够解释其诊断过程，提高透明度和可信度。

**关键设计**：在关键设计方面，该论文采用了GPT-4o作为底层LLM，并利用RAG技术，结合医学知识库进行诊断推理。为了提高诊断的准确性和透明度，该论文采用了思维链（Chain-of-Thought）提示，使系统能够解释其诊断过程。此外，该论文还设计了一种自适应提问策略，根据患者的回答，动态调整提问内容，以便更全面地收集症状信息。具体的参数设置和网络结构等技术细节在论文中未详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17559v1/figure1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17559v1/figure2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17559v1/figure3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于LLM的诊断聊天机器人达到了90%的准确率和100%的Top-3准确率，显著优于传统的机器学习模型（如朴素贝叶斯、逻辑回归、SVM、随机森林和KNN）。这表明LLM在医疗诊断领域具有巨大的潜力，能够提供更准确、更可靠的诊断结果。

## 🎯 应用场景

该研究成果可应用于远程医疗、在线健康咨询、基层医疗机构等场景，辅助医生进行早期诊断，提高诊断效率和准确性，降低医疗成本，并改善患者就医体验。未来，该技术有望与可穿戴设备、电子病历等系统集成，实现更智能化的健康管理。

## 📄 摘要（原文）

> Healthcare systems around the world are grappling with issues like inefficient diagnostics, rising costs, and limited access to specialists. These problems often lead to delays in treatment and poor health outcomes. Most current AI and deep learning diagnostic systems are not very interactive or transparent, making them less effective in real-world, patient-centered environments. This research introduces a diagnostic chatbot powered by a Large Language Model (LLM), using GPT-4o, Retrieval-Augmented Generation, and explainable AI techniques. The chatbot engages patients in a dynamic conversation, helping to extract and normalize symptoms while prioritizing potential diagnoses through similarity matching and adaptive questioning. With Chain-of-Thought prompting, the system also offers more transparent reasoning behind its diagnoses. When tested against traditional machine learning models like Naive Bayes, Logistic Regression, SVM, Random Forest, and KNN, the LLM-based system delivered impressive results, achieving an accuracy of 90% and Top-3 accuracy of 100%. These findings offer a promising outlook for more transparent, interactive, and clinically relevant AI in healthcare.

