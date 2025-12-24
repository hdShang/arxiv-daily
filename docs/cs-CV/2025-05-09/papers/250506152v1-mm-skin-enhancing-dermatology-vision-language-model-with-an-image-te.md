---
layout: default
title: MM-Skin: Enhancing Dermatology Vision-Language Model with an Image-Text Dataset Derived from Textbooks
---

# MM-Skin: Enhancing Dermatology Vision-Language Model with an Image-Text Dataset Derived from Textbooks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06152" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06152v1</a>
  <a href="https://arxiv.org/pdf/2505.06152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06152v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06152v1', 'MM-Skin: Enhancing Dermatology Vision-Language Model with an Image-Text Dataset Derived from Textbooks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqi Zeng, Yuqi Sun, Chenxi Ma, Weimin Tan, Bo Yan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-09

**🔗 代码/项目**: [GITHUB](https://github.com/ZwQ803/MM-Skin)

---

## 💡 一句话要点

**提出MM-Skin以解决皮肤科多模态数据不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `皮肤科` `多模态数据集` `视觉语言模型` `医学图像处理` `视觉问答` `深度学习` `临床应用`

## 📋 核心要点

1. 现有皮肤科视觉语言模型在专业诊断分析方面发展不足，缺乏高质量的多模态数据支持。
2. 提出MM-Skin数据集，包含多种成像方式和大量高质量图像-文本对，旨在提升皮肤科VLM的性能。
3. SkinVL在多个基准测试中表现优异，相较于现有模型在皮肤病解读上有显著提升，验证了方法的有效性。

## 📝 摘要（中文）

医学视觉语言模型（VLMs）在各个医疗领域作为临床助手展现出良好前景。然而，专门针对皮肤科的VLM尚未得到充分发展，主要原因是现有皮肤科多模态数据集中缺乏专业的文本描述。为了解决这一问题，本文提出了MM-Skin，这是第一个大规模的多模态皮肤科数据集，涵盖临床、皮肤镜和病理三种成像方式，收集了近1万对高质量的图像-文本对。此外，我们生成了超过2.7万条多样化的、遵循指令的视觉问答（VQA）样本，规模是当前最大皮肤科VQA数据集的9倍。基于公共数据集和MM-Skin，我们开发了SkinVL，这是一种专门针对皮肤病的VLM，旨在实现精确和细致的皮肤病解读。对SkinVL在8个数据集上的VQA、监督微调（SFT）和零-shot分类任务的全面基准评估显示，其在皮肤病方面的表现优于一般和医学VLM模型。MM-Skin和SkinVL的引入为推动临床皮肤科VLM助手的发展做出了重要贡献。

## 🔬 方法详解

**问题定义**：本文旨在解决现有皮肤科视觉语言模型在专业性和数据质量上的不足，尤其是缺乏高质量的多模态数据集。

**核心思路**：通过构建MM-Skin数据集，整合多种成像方式的图像和专业文本描述，提升皮肤科VLM的训练效果和诊断能力。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。MM-Skin数据集为模型提供了丰富的训练样本，而SkinVL则是基于该数据集训练的专用VLM。

**关键创新**：MM-Skin是首个大规模的多模态皮肤科数据集，包含多种成像方式的图像-文本对，且生成的VQA样本数量显著超过现有数据集，填补了领域内的空白。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，以确保模型能够有效理解和生成与皮肤病相关的复杂信息。

## 📊 实验亮点

SkinVL在8个数据集上的评估结果显示，其在视觉问答、监督微调和零-shot分类任务中的表现均优于现有的通用和医学VLM模型，尤其在皮肤病解读方面，性能提升显著，验证了MM-Skin数据集的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括临床皮肤科诊断、医学教育和远程医疗等。通过提供高质量的多模态数据和专用模型，MM-Skin和SkinVL可以帮助医生更准确地进行皮肤病诊断，提高医疗服务的效率和质量，未来可能对医学研究和临床实践产生深远影响。

## 📄 摘要（原文）

> Medical vision-language models (VLMs) have shown promise as clinical assistants across various medical fields. However, specialized dermatology VLM capable of delivering professional and detailed diagnostic analysis remains underdeveloped, primarily due to less specialized text descriptions in current dermatology multimodal datasets. To address this issue, we propose MM-Skin, the first large-scale multimodal dermatology dataset that encompasses 3 imaging modalities, including clinical, dermoscopic, and pathological and nearly 10k high-quality image-text pairs collected from professional textbooks. In addition, we generate over 27k diverse, instruction-following vision question answering (VQA) samples (9 times the size of current largest dermatology VQA dataset). Leveraging public datasets and MM-Skin, we developed SkinVL, a dermatology-specific VLM designed for precise and nuanced skin disease interpretation. Comprehensive benchmark evaluations of SkinVL on VQA, supervised fine-tuning (SFT) and zero-shot classification tasks across 8 datasets, reveal its exceptional performance for skin diseases in comparison to both general and medical VLM models. The introduction of MM-Skin and SkinVL offers a meaningful contribution to advancing the development of clinical dermatology VLM assistants. MM-Skin is available at https://github.com/ZwQ803/MM-Skin

