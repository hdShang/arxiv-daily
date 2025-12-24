---
layout: default
title: High-Fidelity Pseudo-label Generation by Large Language Models for Training Robust Radiology Report Classifiers
---

# High-Fidelity Pseudo-label Generation by Large Language Models for Training Robust Radiology Report Classifiers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01693" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01693v1</a>
  <a href="https://arxiv.org/pdf/2505.01693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01693v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01693v1', 'High-Fidelity Pseudo-label Generation by Large Language Models for Training Robust Radiology Report Classifiers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brian Wong, Kaito Tanaka

**分类**: cs.CL

**发布日期**: 2025-05-03

---

## 💡 一句话要点

**提出DeBERTa-RAD以解决胸部X光报告自动标注问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `伪标签生成` `知识蒸馏` `胸部X光` `自然语言处理` `医疗影像分析` `高通量应用`

## 📋 核心要点

1. 现有的自然语言处理方法在自动标注胸部X光报告时面临高变异性和复杂性等挑战，尤其是在处理否定和不确定性时。
2. 论文提出的DeBERTa-RAD框架通过结合大型语言模型的伪标签生成和DeBERTa知识蒸馏，实现了高效且准确的报告标注。
3. 在MIMIC-500基准测试中，DeBERTa-RAD取得了0.9120的宏F1分数，显著优于传统方法，且推理速度适合高通量应用。

## 📝 摘要（中文）

自动标注胸部X光报告对于训练基于图像的诊断模型、进行人群健康研究和临床决策支持至关重要。然而，传统自然语言处理方法在处理这些自由文本报告时面临高变异性、复杂性以及否定和不确定性等挑战。本文提出了一种新颖的两阶段框架DeBERTa-RAD，结合了先进的大型语言模型伪标签生成与高效的DeBERTa知识蒸馏，以实现准确快速的胸部X光报告标注。在MIMIC-500基准测试中，DeBERTa-RAD达到了0.9120的宏F1分数，显著优于现有的基于规则的系统、微调的变换器模型和直接的LLM推理，同时保持适合高通量应用的推理速度。我们的分析显示该方法在处理不确定发现方面表现尤为出色。

## 🔬 方法详解

**问题定义**：本文旨在解决胸部X光报告的自动标注问题。现有方法在处理复杂的自由文本报告时，常常受到高变异性和不确定性影响，导致标注效果不佳。

**核心思路**：论文的核心思路是通过DeBERTa-RAD框架，利用大型语言模型生成高质量的伪标签，并结合知识蒸馏技术，提升标注的准确性和效率。

**技术框架**：该框架分为两个主要阶段：第一阶段使用大型语言模型生成伪标签，包括确定性状态；第二阶段则使用DeBERTa-Base模型在伪标注数据上进行训练，采用定制的知识蒸馏策略。

**关键创新**：最重要的技术创新在于将大型语言模型的伪标签生成与高效的知识蒸馏相结合，显著提高了标注的准确性和处理速度，克服了传统方法的局限性。

**关键设计**：在设计中，采用了特定的损失函数和网络结构，以优化知识蒸馏过程，并确保生成的伪标签具有高质量和一致性。

## 📊 实验亮点

在MIMIC-500基准测试中，DeBERTa-RAD实现了0.9120的宏F1分数，显著优于传统的基于规则的系统和微调的变换器模型，提升幅度明显，同时保持了适合高通量应用的推理速度。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、临床决策支持系统以及大规模人群健康研究。通过提高胸部X光报告的自动标注效率，可以加速医学研究和临床应用，降低人工标注的成本和时间，推动医疗智能化的发展。

## 📄 摘要（原文）

> Automated labeling of chest X-ray reports is essential for enabling downstream tasks such as training image-based diagnostic models, population health studies, and clinical decision support. However, the high variability, complexity, and prevalence of negation and uncertainty in these free-text reports pose significant challenges for traditional Natural Language Processing methods. While large language models (LLMs) demonstrate strong text understanding, their direct application for large-scale, efficient labeling is limited by computational cost and speed. This paper introduces DeBERTa-RAD, a novel two-stage framework that combines the power of state-of-the-art LLM pseudo-labeling with efficient DeBERTa-based knowledge distillation for accurate and fast chest X-ray report labeling. We leverage an advanced LLM to generate high-quality pseudo-labels, including certainty statuses, for a large corpus of reports. Subsequently, a DeBERTa-Base model is trained on this pseudo-labeled data using a tailored knowledge distillation strategy. Evaluated on the expert-annotated MIMIC-500 benchmark, DeBERTa-RAD achieves a state-of-the-art Macro F1 score of 0.9120, significantly outperforming established rule-based systems, fine-tuned transformer models, and direct LLM inference, while maintaining a practical inference speed suitable for high-throughput applications. Our analysis shows particular strength in handling uncertain findings. This work demonstrates a promising path to overcome data annotation bottlenecks and achieve high-performance medical text processing through the strategic combination of LLM capabilities and efficient student models trained via distillation.

