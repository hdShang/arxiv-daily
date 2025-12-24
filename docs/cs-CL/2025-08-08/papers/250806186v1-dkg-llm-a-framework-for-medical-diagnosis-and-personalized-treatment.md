---
layout: default
title: "DKG-LLM : A Framework for Medical Diagnosis and Personalized Treatment Recommendations via Dynamic Knowledge Graph and Large Language Model Integration"
---

# DKG-LLM : A Framework for Medical Diagnosis and Personalized Treatment Recommendations via Dynamic Knowledge Graph and Large Language Model Integration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06186" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06186v1</a>
  <a href="https://arxiv.org/pdf/2508.06186.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06186v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06186v1', 'DKG-LLM : A Framework for Medical Diagnosis and Personalized Treatment Recommendations via Dynamic Knowledge Graph and Large Language Model Integration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Sarabadani, Maryam Abdollahi Shamami, Hamidreza Sadeghsalehi, Borhan Asadi, Saba Hesaraki

**分类**: cs.CL

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出DKG-LLM框架以解决医疗诊断与个性化治疗推荐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗诊断` `个性化治疗` `动态知识图` `大型语言模型` `自适应语义融合算法` `复杂多症状疾病` `噪声数据处理`

## 📋 核心要点

1. 现有医疗诊断方法在处理复杂多症状疾病和噪声数据时存在准确性不足的问题。
2. DKG-LLM框架通过动态知识图与大型语言模型的结合，提供了一种创新的医疗诊断与治疗推荐方案。
3. 实验结果显示，DKG-LLM在诊断和治疗推荐的准确率上均有显著提升，验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）自ChatGPT发布以来迅速发展，因其在多种语言处理任务中的卓越表现而受到关注。本研究提出DKG-LLM框架，通过将动态知识图（DKG）与Grok 3大型语言模型集成，创新性地解决医疗诊断和个性化治疗推荐问题。采用自适应语义融合算法（ASFA），动态生成包含15,964个节点和127,392条边的知识图，涵盖多种医疗数据。实验结果表明，DKG-LLM在诊断准确率上达到84.19%，治疗推荐准确率为89.63%，语义覆盖率为93.48%。该框架能够有效处理噪声数据和复杂多症状疾病，并具备基于医生反馈的学习能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决医疗诊断和个性化治疗推荐中的准确性不足问题，尤其是在面对复杂多症状疾病和噪声数据时，现有方法往往无法提供可靠的结果。

**核心思路**：DKG-LLM框架通过集成动态知识图和大型语言模型，利用自适应语义融合算法（ASFA）来动态生成和更新知识图，从而提升医疗数据的处理能力和诊断准确性。

**技术框架**：该框架主要包括数据收集、知识图构建、语义信息提取和模型训练四个模块。首先，收集异构医疗数据，然后通过ASFA生成知识图，最后利用大型语言模型进行诊断和治疗推荐。

**关键创新**：最重要的创新在于动态知识图的构建与更新机制，ASFA能够实时处理新数据并扩展知识图，这在现有方法中是较为少见的。

**关键设计**：在设计中，ASFA结合了先进的概率模型、贝叶斯推断和图优化技术，确保知识图的动态更新和扩展，支持高达987,654条边的可扩展性。

## 📊 实验亮点

实验结果表明，DKG-LLM在诊断准确率上达到84.19%，治疗推荐准确率为89.63%，语义覆盖率为93.48%。这些结果显著高于现有基线模型，展示了该框架在处理复杂医疗数据方面的优势。

## 🎯 应用场景

DKG-LLM框架在医疗领域具有广泛的应用潜力，能够为医生提供更准确的诊断和个性化治疗建议，提升患者的治疗效果。未来，该框架还可扩展至其他医疗相关领域，如公共卫生监测和健康管理，推动智能医疗的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have grown exponentially since the release of ChatGPT. These models have gained attention due to their robust performance on various tasks, including language processing tasks. These models achieve understanding and comprehension of tasks by training billions of parameters. The development of these models is a transformative force in enhancing natural language understanding and has taken a significant step towards artificial general intelligence (AGI). In this study, we aim to present the DKG-LLM framework. The DKG-LLM framework introduces a groundbreaking approach to medical diagnosis and personalized treatment recommendations by integrating a dynamic knowledge graph (DKG) with the Grok 3 large language model. Using the Adaptive Semantic Fusion Algorithm (ASFA), heterogeneous medical data (including clinical reports and PubMed articles) and patient records dynamically generate a knowledge graph consisting of 15,964 nodes in 13 distinct types (e.g., diseases, symptoms, treatments, patient profiles) and 127,392 edges in 26 relationship types (e.g., causal, therapeutic, association). ASFA utilizes advanced probabilistic models, Bayesian inference, and graph optimization to extract semantic information, dynamically updating the graph with approximately 150 new nodes and edges in each data category while maintaining scalability with up to 987,654 edges. Real-world datasets, including MIMIC-III and PubMed, were utilized to evaluate the proposed architecture. The evaluation results show that DKG-LLM achieves a diagnostic accuracy of 84.19%. The model also has a treatment recommendation accuracy of 89.63% and a semantic coverage of 93.48%. DKG-LLM is a reliable and transformative tool that handles noisy data and complex multi-symptom diseases, along with feedback-based learning from physician input.

