---
layout: default
title: Multimodal Integrated Knowledge Transfer to Large Language Models through Preference Optimization with Biomedical Applications
---

# Multimodal Integrated Knowledge Transfer to Large Language Models through Preference Optimization with Biomedical Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05736" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05736v1</a>
  <a href="https://arxiv.org/pdf/2505.05736.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05736v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05736v1', 'Multimodal Integrated Knowledge Transfer to Large Language Models through Preference Optimization with Biomedical Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Da Wu, Zhanliang Wang, Quan Nguyen, Zhuoran Xu, Kai Wang

**分类**: q-bio.QM, cs.CL, cs.CV, cs.LG

**发布日期**: 2025-05-09

**备注**: First Draft

---

## 💡 一句话要点

**提出MINT框架以解决生物医学多模态数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态集成` `知识转移` `偏好优化` `生物医学应用` `大型语言模型` `罕见疾病预测` `组织类型分类`

## 📋 核心要点

1. 现有方法在生物医学领域面临高质量多模态数据稀缺的问题，限制了模型的微调效果。
2. 本文提出MINT框架，通过偏好优化将单模态模型与多模态数据中的决策模式对齐，从而提升模型性能。
3. 实验结果表明，MINT在罕见遗传疾病预测和组织类型分类任务中均显著优于传统方法，展示了其有效性。

## 📝 摘要（中文）

生物医学领域高质量多模态数据的稀缺限制了预训练大型语言模型（LLMs）在专业任务中的有效微调。为了解决这一挑战，本文提出了MINT（多模态集成知识转移）框架，通过偏好优化将单模态大型解码器模型与多模态生物医学数据中的领域特定决策模式对齐。MINT主要采用赔率比偏好优化（ORPO）框架作为其核心，支持文本或图像输入的预测任务，同时保留从多模态数据中学习的知识。通过两个关键应用展示了其有效性：1）基于文本的罕见遗传疾病预测，MINT利用多模态编码器模型生成偏好数据集，显著超越了传统训练方法的模型；2）细胞核图像的组织类型分类，MINT通过视觉-语言基础模型对下游图像模型进行对齐，显著提升了分类性能。

## 🔬 方法详解

**问题定义**：本文旨在解决生物医学领域中高质量多模态数据稀缺的问题，现有方法在微调大型语言模型时效果不佳，无法充分利用多模态数据的优势。

**核心思路**：MINT框架通过偏好优化将单模态解码器模型与多模态数据中的领域特定决策模式对齐，使得模型能够在仅使用文本或图像输入的情况下，依然保留从多模态数据中学习的知识。

**技术框架**：MINT的整体架构包括一个上游多模态机器学习模型，该模型在高质量的多模态数据上训练，生成偏好数据集以对齐下游的文本或图像模型。主要模块包括偏好优化模块和多模态编码器模型。

**关键创新**：MINT的核心创新在于引入了赔率比偏好优化（ORPO）作为对齐机制，使得单模态模型能够有效利用多模态数据的知识，显著提升了模型的预测能力。

**关键设计**：在模型设计中，MINT使用了多模态编码器生成偏好数据集，并通过轻量级的Llama 3.2-3B-Instruct进行对齐，确保了模型在仅使用文本输入时的高效性和准确性。

## 📊 实验亮点

在实验中，MINT在罕见遗传疾病预测任务中，使用文本输入的模型超越了传统的SFT、RAG和DPO方法，甚至超过了Llama 3.1-405B-Instruct。而在组织类型分类任务中，MINT显著提升了Llama 3.2-Vision-11B-Instruct的性能，展示了其优越性。

## 🎯 应用场景

MINT框架在生物医学领域具有广泛的应用潜力，特别是在罕见疾病预测和组织分类等任务中。通过有效整合多模态数据，MINT能够提升模型的预测能力，为临床决策提供更为精准的支持，未来可能在医疗影像分析和个性化医疗等领域产生深远影响。

## 📄 摘要（原文）

> The scarcity of high-quality multimodal biomedical data limits the ability to effectively fine-tune pretrained Large Language Models (LLMs) for specialized biomedical tasks. To address this challenge, we introduce MINT (Multimodal Integrated kNowledge Transfer), a framework that aligns unimodal large decoder models with domain-specific decision patterns from multimodal biomedical data through preference optimization. While MINT supports different optimization techniques, we primarily implement it with the Odds Ratio Preference Optimization (ORPO) framework as its backbone. This strategy enables the aligned LLMs to perform predictive tasks using text-only or image-only inputs while retaining knowledge learnt from multimodal data. MINT leverages an upstream multimodal machine learning (MML) model trained on high-quality multimodal data to transfer domain-specific insights to downstream text-only or image-only LLMs. We demonstrate its effectiveness through two key applications: (1) Rare genetic disease prediction from texts, where MINT uses a multimodal encoder model, trained on facial photos and clinical notes, to generate a preference dataset for aligning a lightweight Llama 3.2-3B-Instruct. Despite relying on text input only, the MINT-derived model outperforms models trained with SFT, RAG, or DPO, and even outperforms Llama 3.1-405B-Instruct. (2) Tissue type classification using cell nucleus images, where MINT uses a vision-language foundation model as the preference generator, containing knowledge learnt from both text and histopathological images to align downstream image-only models. The resulting MINT-derived model significantly improves the performance of Llama 3.2-Vision-11B-Instruct on tissue type classification. In summary, MINT provides an effective strategy to align unimodal LLMs with high-quality multimodal expertise through preference optimization.

