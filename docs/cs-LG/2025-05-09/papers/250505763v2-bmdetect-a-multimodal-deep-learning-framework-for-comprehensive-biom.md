---
layout: default
title: BMDetect: A Multimodal Deep Learning Framework for Comprehensive Biomedical Misconduct Detection
---

# BMDetect: A Multimodal Deep Learning Framework for Comprehensive Biomedical Misconduct Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05763" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05763v2</a>
  <a href="https://arxiv.org/pdf/2505.05763.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05763v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05763v2', 'BMDetect: A Multimodal Deep Learning Framework for Comprehensive Biomedical Misconduct Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yize Zhou, Jie Zhang, Meijie Wang, Lun Yu

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-09 (更新: 2025-07-15)

---

## 💡 一句话要点

**提出BMDetect以解决生物医学研究中的学术不端检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态深度学习` `学术不端检测` `生物医学研究` `特征融合` `数据异常识别` `BioMCD数据集` `模型迁移性`

## 📋 核心要点

1. 现有的学术不端检测方法在算法上存在局限性，且分析流程往往碎片化，导致检测效果不佳。
2. BMDetect通过整合多种数据源和深度学习技术，提供了一种全面的手稿评估方法，旨在提高检测的准确性和可靠性。
3. BMDetect在实验中取得了74.33%的AUC，超越了单模态基线8.6%，并展示了在不同生物医学子领域的迁移能力。

## 📝 摘要（中文）

生物医学研究中的学术不端检测面临着现有方法算法狭窄和分析流程碎片化的挑战。本文提出BMDetect，一个多模态深度学习框架，整合期刊元数据（如SJR、机构数据）、语义嵌入（如PubMedBERT）和GPT-4挖掘的文本属性（如方法统计、数据异常），实现全面的手稿评估。主要创新包括：多模态特征融合以减少检测偏差；定量评估特征重要性，识别期刊权威指标和文本异常作为主要预测因子；以及BioMCD数据集，包含13,160篇撤回文章和53,411篇对照文章。BMDetect的AUC达到74.33%，比单模态基线提高8.6%，并在生物医学子领域中表现出良好的迁移性。这项工作推动了可扩展、可解释的工具的发展，以维护研究诚信。

## 🔬 方法详解

**问题定义**：本文旨在解决生物医学研究中的学术不端检测问题，现有方法存在算法狭窄和分析流程碎片化的痛点，导致检测效果不理想。

**核心思路**：BMDetect的核心思路是通过多模态融合不同类型的数据（如期刊元数据、语义嵌入和文本属性），以减少检测偏差并提高检测的全面性和准确性。

**技术框架**：BMDetect的整体架构包括三个主要模块：数据预处理模块、特征提取模块和模型训练模块。数据预处理模块负责整合不同来源的数据，特征提取模块利用深度学习模型提取有用特征，模型训练模块则基于提取的特征进行学术不端检测。

**关键创新**：BMDetect的关键创新在于多模态特征的融合和定量评估特征重要性，特别是识别出期刊权威指标和文本异常作为主要预测因子，这在现有方法中尚未得到充分重视。

**关键设计**：在模型设计上，BMDetect采用了深度学习网络结构，结合了损失函数的优化和特征选择的策略，以确保模型的高效性和准确性。

## 📊 实验亮点

BMDetect在实验中取得了74.33%的AUC，相较于单模态基线提高了8.6%。此外，该框架展示了在不同生物医学子领域的良好迁移能力，表明其在实际应用中的有效性和可靠性。

## 🎯 应用场景

BMDetect的研究成果在生物医学领域具有广泛的应用潜力，可以用于期刊编辑、科研机构和学术界的学术不端检测，帮助维护研究的诚信与质量。未来，该框架还可扩展到其他学科的学术不端检测中，推动学术研究的健康发展。

## 📄 摘要（原文）

> Academic misconduct detection in biomedical research remains challenging due to algorithmic narrowness in existing methods and fragmented analytical pipelines. We present BMDetect, a multimodal deep learning framework that integrates journal metadata (SJR, institutional data), semantic embeddings (PubMedBERT), and GPT-4o-mined textual attributes (methodological statistics, data anomalies) for holistic manuscript evaluation. Key innovations include: (1) multimodal fusion of domain-specific features to reduce detection bias; (2) quantitative evaluation of feature importance, identifying journal authority metrics (e.g., SJR-index) and textual anomalies (e.g., statistical outliers) as dominant predictors; and (3) the BioMCD dataset, a large-scale benchmark with 13,160 retracted articles and 53,411 controls. BMDetect achieves 74.33% AUC, outperforming single-modality baselines by 8.6%, and demonstrates transferability across biomedical subfields. This work advances scalable, interpretable tools for safeguarding research integrity.

