---
layout: default
title: "EXPERT: An Explainable Image Captioning Evaluation Metric with Structured Explanations"
---

# EXPERT: An Explainable Image Captioning Evaluation Metric with Structured Explanations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24016" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24016v1</a>
  <a href="https://arxiv.org/pdf/2506.24016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24016v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24016v1', 'EXPERT: An Explainable Image Captioning Evaluation Metric with Structured Explanations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyunjong Kim, Sangyeop Kim, Jongheon Jeong, Yeongjae Cho, Sungzoon Cho

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-06-30

**备注**: Accepted at ACL 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/hjkim811/EXPERT)

---

## 💡 一句话要点

**提出EXPERT以解决图像描述评估标准化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像描述` `可解释性评估` `视觉-语言模型` `结构化解释` `无参考评估`

## 📋 核心要点

1. 现有图像描述评估指标缺乏标准化的解释生成标准，导致生成的解释质量不一。
2. 本文提出EXPERT，通过流畅性、相关性和描述性三个标准提供结构化解释，解决了现有方法的不足。
3. EXPERT在基准数据集上实现了最先进的结果，并在解释质量上显著优于现有评估指标。

## 📝 摘要（中文）

近年来，随着大型语言模型和视觉-语言模型的进展，图像描述的可解释评估指标引起了越来越多的关注。然而，现有指标生成的解释缺乏标准化的标准，且生成解释的整体质量尚未得到验证。本文提出了EXPERT，这是一种无参考的评估指标，基于流畅性、相关性和描述性三个基本标准提供结构化解释。通过构建高质量结构化解释的大规模数据集，我们开发了一个两阶段评估模板，有效监督视觉-语言模型进行评分和解释生成。EXPERT在基准数据集上取得了最先进的结果，并通过全面的人类评估验证了其生成的解释质量显著高于现有指标。我们的代码和数据集可在https://github.com/hjkim811/EXPERT获取。

## 🔬 方法详解

**问题定义**：本文旨在解决图像描述评估中缺乏标准化解释生成的问题。现有方法往往未能提供一致和高质量的解释，影响了评估的可靠性。

**核心思路**：EXPERT的核心思路是基于流畅性、相关性和描述性三个基本标准构建结构化解释，确保评估的客观性和一致性。通过这种方式，EXPERT能够有效地评估图像描述的质量。

**技术框架**：EXPERT的整体架构包括两个主要阶段：首先，构建高质量结构化解释的数据集；其次，利用该数据集监督视觉-语言模型进行评分和解释生成。

**关键创新**：EXPERT的最大创新在于其无参考评估机制和结构化解释生成，这与现有方法依赖于参考描述的评估方式有本质区别。

**关键设计**：在设计中，EXPERT采用了特定的损失函数来优化模型的评分和解释生成能力，并通过大规模数据集的构建确保了训练的有效性。

## 📊 实验亮点

在实验中，EXPERT在多个基准数据集上达到了最先进的结果，生成的解释质量显著高于现有评估指标。具体而言，EXPERT在流畅性、相关性和描述性方面的评分均表现出显著提升，验证了其有效性和优越性。

## 🎯 应用场景

EXPERT的研究成果在图像描述生成、视觉问答和多模态学习等领域具有广泛的应用潜力。通过提供高质量的评估标准，EXPERT能够帮助研究人员和开发者更好地理解和改进视觉-语言模型的性能，推动相关技术的发展。

## 📄 摘要（原文）

> Recent advances in large language models and vision-language models have led to growing interest in explainable evaluation metrics for image captioning. However, these metrics generate explanations without standardized criteria, and the overall quality of the generated explanations remains unverified. In this paper, we propose EXPERT, a reference-free evaluation metric that provides structured explanations based on three fundamental criteria: fluency, relevance, and descriptiveness. By constructing large-scale datasets of high-quality structured explanations, we develop a two-stage evaluation template to effectively supervise a vision-language model for both scoring and explanation generation. EXPERT achieves state-of-the-art results on benchmark datasets while providing significantly higher-quality explanations than existing metrics, as validated through comprehensive human evaluation. Our code and datasets are available at https://github.com/hjkim811/EXPERT.

