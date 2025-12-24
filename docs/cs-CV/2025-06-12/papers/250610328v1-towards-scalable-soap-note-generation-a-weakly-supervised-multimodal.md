---
layout: default
title: "Towards Scalable SOAP Note Generation: A Weakly Supervised Multimodal Framework"
---

# Towards Scalable SOAP Note Generation: A Weakly Supervised Multimodal Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10328" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10328v1</a>
  <a href="https://arxiv.org/pdf/2506.10328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10328v1', 'Towards Scalable SOAP Note Generation: A Weakly Supervised Multimodal Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sadia Kamal, Tim Oates, Joy Wan

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-12

**备注**: Accepted at IEEE/CVF Computer Society Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)

---

## 💡 一句话要点

**提出弱监督多模态框架以生成SOAP笔记，解决临床文档负担问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SOAP笔记生成` `弱监督学习` `多模态框架` `临床文档` `医疗人工智能`

## 📋 核心要点

1. 现有的SOAP笔记生成方法依赖于大量手动标注，导致临床医生的工作负担加重，影响其工作效率。
2. 本文提出的弱监督多模态框架能够从有限的输入生成SOAP笔记，减少对人工标注的依赖，提升文档生成的可扩展性。
3. 实验结果表明，该方法在临床相关性指标上与现有先进模型相当，且引入的新评估指标有效评估了生成内容的临床质量。

## 📝 摘要（中文）

皮肤癌是全球最常见的癌症，每年医疗支出超过80亿美元。在临床环境中，医生使用SOAP（主观、客观、评估和计划）笔记记录患者就诊情况。然而，手动生成这些笔记耗时耗力，导致临床医生的职业倦怠。本文提出了一种弱监督多模态框架，从有限的输入（包括病变图像和稀疏临床文本）生成结构化的SOAP笔记。该方法减少了对手动标注的依赖，实现了可扩展的临床文档生成，同时减轻了临床医生的负担，并降低了对大量标注数据的需求。我们的研究在关键临床相关性指标上表现出与GPT-4o、Claude和DeepSeek Janus Pro相当的性能。为评估临床质量，我们引入了两个新指标MedConceptEval和临床一致性评分（CCS），分别评估与专家医学概念和输入特征的语义对齐。

## 🔬 方法详解

**问题定义**：本文旨在解决手动生成SOAP笔记所带来的高工作负担和对大量标注数据的依赖问题。现有方法通常需要大量人工标注，难以在临床环境中广泛应用。

**核心思路**：提出一种弱监督多模态框架，通过结合病变图像和稀疏临床文本，自动生成结构化的SOAP笔记，从而减轻临床医生的文档负担。

**技术框架**：该框架包括输入处理模块、特征提取模块和生成模块。输入处理模块负责接收病变图像和文本信息，特征提取模块利用深度学习技术提取关键特征，生成模块则根据提取的特征生成SOAP笔记。

**关键创新**：最重要的创新在于引入弱监督学习策略，减少对手动标注的依赖，同时通过多模态输入提高生成内容的质量和相关性。与现有方法相比，该框架在数据需求和生成效率上具有显著优势。

**关键设计**：在模型设计中，采用了特定的损失函数来优化生成内容的临床一致性，并通过引入MedConceptEval和CCS等新指标来评估生成结果的质量。

## 📊 实验亮点

实验结果显示，提出的方法在关键临床相关性指标上与GPT-4o、Claude和DeepSeek Janus Pro的性能相当，表明其在临床应用中的有效性。此外，通过引入MedConceptEval和CCS指标，能够更好地评估生成内容的临床质量。

## 🎯 应用场景

该研究的潜在应用领域包括医院信息系统、电子病历生成和临床决策支持系统。通过自动化SOAP笔记生成，可以显著提高临床文档的效率，减轻医生的工作负担，进而提升医疗服务质量。未来，该框架有望扩展到其他类型的临床文档生成任务中。

## 📄 摘要（原文）

> Skin carcinoma is the most prevalent form of cancer globally, accounting for over $8 billion in annual healthcare expenditures. In clinical settings, physicians document patient visits using detailed SOAP (Subjective, Objective, Assessment, and Plan) notes. However, manually generating these notes is labor-intensive and contributes to clinician burnout. In this work, we propose a weakly supervised multimodal framework to generate clinically structured SOAP notes from limited inputs, including lesion images and sparse clinical text. Our approach reduces reliance on manual annotations, enabling scalable, clinically grounded documentation while alleviating clinician burden and reducing the need for large annotated data. Our method achieves performance comparable to GPT-4o, Claude, and DeepSeek Janus Pro across key clinical relevance metrics. To evaluate clinical quality, we introduce two novel metrics MedConceptEval and Clinical Coherence Score (CCS) which assess semantic alignment with expert medical concepts and input features, respectively.

