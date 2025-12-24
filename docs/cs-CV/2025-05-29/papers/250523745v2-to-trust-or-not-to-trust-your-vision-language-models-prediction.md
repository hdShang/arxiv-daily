---
layout: default
title: To Trust Or Not To Trust Your Vision-Language Model's Prediction
---

# To Trust Or Not To Trust Your Vision-Language Model's Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23745" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23745v2</a>
  <a href="https://arxiv.org/pdf/2505.23745.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23745v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23745v2', 'To Trust Or Not To Trust Your Vision-Language Model\'s Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Dong, Moru Liu, Jian Liang, Eleni Chatzi, Olga Fink

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-05-29 (更新: 2025-09-24)

**🔗 代码/项目**: [GITHUB](https://github.com/EPFL-IMOS/TrustVLM)

---

## 💡 一句话要点

**提出TrustVLM以解决视觉语言模型预测可信度问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `置信评分` `错误分类检测` `多模态学习` `安全关键应用`

## 📋 核心要点

1. 现有的视觉语言模型在安全关键领域的错误分类问题严重，导致自信但错误的预测，存在安全隐患。
2. 本文提出TrustVLM框架，通过引入新颖的置信评分函数，利用图像嵌入空间的模态差异来提高错误分类检测能力。
3. 在17个数据集上进行评估，TrustVLM在多个指标上表现出色，AURC提升达51.87%，AUROC提升9.14%，FPR95提升32.42%。

## 📝 摘要（中文）

视觉语言模型（VLMs）在对齐视觉和文本模态方面表现出色，广泛应用于多模态理解和生成。然而，VLMs在零样本和迁移学习场景中仍然容易出现错误分类，导致自信但错误的预测，这在安全关键领域可能带来严重后果。为此，本文提出了TrustVLM，一个无训练的框架，旨在估计VLM预测的可信度。我们提出了一种新颖的置信评分函数，利用图像嵌入空间中的模态差异来改善错误分类检测。通过在17个多样化数据集上评估，我们展示了该方法在AURC、AUROC和FPR95等指标上相较于现有基线的显著提升，最大提升达51.87%。TrustVLM的提出为VLM在实际应用中的安全部署铺平了道路。

## 🔬 方法详解

**问题定义**：本文解决的是视觉语言模型在预测时的可信度评估问题。现有方法在面对错误分类时，往往无法有效识别何时可以信任模型的预测，导致潜在的安全风险。

**核心思路**：TrustVLM的核心思路是通过引入一种新颖的置信评分函数，利用图像嵌入空间中的模态差异来改进错误分类的检测能力。这种方法不需要对模型进行重新训练，从而提高了模型的可靠性。

**技术框架**：TrustVLM的整体架构包括数据预处理、特征提取、置信评分计算和结果评估等主要模块。首先，从输入的图像和文本中提取特征，然后计算置信评分，最后通过评估指标来验证模型的性能。

**关键创新**：TrustVLM的关键创新在于其置信评分函数的设计，该函数利用了图像嵌入空间的特征，使得模型能够更准确地判断预测的可信度。这一方法与现有的基于训练的可信度评估方法有本质区别。

**关键设计**：在关键设计方面，TrustVLM采用了多种视觉语言模型架构，并在不同数据集上进行了广泛的实验。具体的参数设置和损失函数设计未在摘要中详细说明，可能需要参考原文以获取更多技术细节。

## 📊 实验亮点

TrustVLM在17个多样化数据集上的实验结果显示，其在AURC、AUROC和FPR95等指标上均显著优于现有基线，最大提升幅度分别达到51.87%、9.14%和32.42%。这些结果表明TrustVLM在提高视觉语言模型预测可信度方面的有效性和优越性。

## 🎯 应用场景

TrustVLM的研究成果具有广泛的应用潜力，尤其是在医疗影像分析、自动驾驶和安全监控等安全关键领域。通过提高视觉语言模型的预测可信度，能够有效降低错误决策的风险，提升系统的安全性和可靠性。未来，TrustVLM有望推动更多基于视觉和语言的智能应用的安全部署。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated strong capabilities in aligning visual and textual modalities, enabling a wide range of applications in multimodal understanding and generation. While they excel in zero-shot and transfer learning scenarios, VLMs remain susceptible to misclassification, often yielding confident yet incorrect predictions. This limitation poses a significant risk in safety-critical domains, where erroneous predictions can lead to severe consequences. In this work, we introduce TrustVLM, a training-free framework designed to address the critical challenge of estimating when VLM's predictions can be trusted. Motivated by the observed modality gap in VLMs and the insight that certain concepts are more distinctly represented in the image embedding space, we propose a novel confidence-scoring function that leverages this space to improve misclassification detection. We rigorously evaluate our approach across 17 diverse datasets, employing 4 architectures and 2 VLMs, and demonstrate state-of-the-art performance, with improvements of up to 51.87% in AURC, 9.14% in AUROC, and 32.42% in FPR95 compared to existing baselines. By improving the reliability of the model without requiring retraining, TrustVLM paves the way for safer deployment of VLMs in real-world applications. The code is available at https://github.com/EPFL-IMOS/TrustVLM.

