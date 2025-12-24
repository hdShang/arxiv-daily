---
layout: default
title: Enhancing Thyroid Cytology Diagnosis with RAG-Optimized LLMs and Pa-thology Foundation Models
---

# Enhancing Thyroid Cytology Diagnosis with RAG-Optimized LLMs and Pa-thology Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08590" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08590v1</a>
  <a href="https://arxiv.org/pdf/2505.08590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08590v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08590v1', 'Enhancing Thyroid Cytology Diagnosis with RAG-Optimized LLMs and Pa-thology Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hussien Al-Asi, Jordan P Reynolds, Shweta Agarwal, Bryan J Dangott, Aziza Nassar, Zeynettin Akkus

**分类**: cs.CL, q-bio.QM

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出RAG优化的LLMs与病理基础模型以提升甲状腺细胞学诊断**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `甲状腺细胞学` `检索增强生成` `大型语言模型` `病理基础模型` `人工智能辅助诊断`

## 📋 核心要点

1. 现有的甲状腺细胞学诊断方法在细胞学解读和标准化方面存在挑战，导致诊断准确性不足。
2. 本研究提出了结合RAG增强的LLMs与病理基础模型的创新方法，以动态检索相关信息，提升诊断能力。
3. 实验结果显示，整合RAG与病理特定LLMs显著提高了诊断效率，基础模型UNI在预测准确性上表现优异。

## 📝 摘要（中文）

人工智能（AI）的进步正在通过将大型语言模型（LLMs）与检索增强生成（RAG）和特定领域基础模型相结合，改变病理学。本研究探讨了RAG增强的LLMs与病理基础模型在甲状腺细胞学诊断中的应用，解决了细胞学解读、标准化和诊断准确性等挑战。通过利用策划的知识库，RAG促进了相关案例研究、诊断标准和专家解读的动态检索，从而改善了LLMs的上下文理解。同时，经过高分辨率病理图像训练的病理基础模型，提升了特征提取和分类能力。这些AI驱动的方法融合增强了诊断一致性，减少了变异性，并支持病理学家区分良性与恶性甲状腺病变。我们的结果表明，将RAG与病理特定LLMs结合显著提高了诊断效率和可解释性，为AI辅助的甲状腺细胞病理学铺平了道路，基础模型UNI在甲状腺细胞学样本的外科病理诊断正确预测中实现了AUC 0.73-0.93。

## 🔬 方法详解

**问题定义**：本研究旨在解决甲状腺细胞学诊断中的细胞学解读、标准化及诊断准确性不足的问题。现有方法在处理复杂病例时，往往缺乏动态信息检索能力，导致诊断结果的变异性较大。

**核心思路**：论文提出将RAG增强的LLMs与病理基础模型相结合，通过动态检索相关案例和标准，提升模型的上下文理解能力，从而提高诊断的准确性和一致性。

**技术框架**：整体架构包括三个主要模块：1) RAG模块，负责从知识库中动态检索相关信息；2) LLM模块，基于检索结果进行细胞学诊断；3) 病理基础模型，专注于高分辨率图像的特征提取与分类。

**关键创新**：本研究的创新点在于将RAG与病理特定LLMs结合，形成了一种新的AI辅助诊断框架，显著提升了模型的诊断能力和可解释性，与传统方法相比，减少了诊断过程中的主观性和变异性。

**关键设计**：在模型设计中，采用了高分辨率病理图像进行训练，优化了特征提取网络结构，并设置了适应性损失函数，以提高模型在不同病理图像上的表现。

## 📊 实验亮点

实验结果表明，整合RAG与病理特定LLMs显著提高了甲状腺细胞学的诊断效率，基础模型UNI在外科病理诊断的正确预测中实现了AUC值在0.73到0.93之间，显示出良好的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断、病理学研究和AI辅助决策系统。通过提升甲状腺细胞学的诊断效率和准确性，能够为临床医生提供更可靠的支持，进而改善患者的治疗效果。未来，该方法也可能扩展到其他类型的细胞学和病理学诊断中，推动AI在医疗领域的广泛应用。

## 📄 摘要（原文）

> Advancements in artificial intelligence (AI) are transforming pathology by integrat-ing large language models (LLMs) with retrieval-augmented generation (RAG) and domain-specific foundation models. This study explores the application of RAG-enhanced LLMs coupled with pathology foundation models for thyroid cytology diagnosis, addressing challenges in cytological interpretation, standardization, and diagnostic accuracy. By leveraging a curated knowledge base, RAG facilitates dy-namic retrieval of relevant case studies, diagnostic criteria, and expert interpreta-tion, improving the contextual understanding of LLMs. Meanwhile, pathology foun-dation models, trained on high-resolution pathology images, refine feature extrac-tion and classification capabilities. The fusion of these AI-driven approaches en-hances diagnostic consistency, reduces variability, and supports pathologists in dis-tinguishing benign from malignant thyroid lesions. Our results demonstrate that integrating RAG with pathology-specific LLMs significantly improves diagnostic efficiency and interpretability, paving the way for AI-assisted thyroid cytopathology, with foundation model UNI achieving AUC 0.73-0.93 for correct prediction of surgi-cal pathology diagnosis from thyroid cytology samples.

