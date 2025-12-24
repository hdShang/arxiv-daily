---
layout: default
title: "FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation"
---

# FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24714" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24714v1</a>
  <a href="https://arxiv.org/pdf/2505.24714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24714v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24714v1', 'FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyu Luo, Zhizhuo Kou, Liming Yang, Xiao Luo, Jinsheng Huang, Zhiping Xiao, Jingshu Peng, Chengzhong Liu, Jiaming Ji, Xuanzhe Liu, Sirui Han, Ming Zhang, Yike Guo

**分类**: cs.CL

**发布日期**: 2025-05-30

**备注**: ACL 2025 Main Conference

**🔗 代码/项目**: [GITHUB](https://github.com/luo-junyu/FinMME) | [HUGGINGFACE](https://huggingface.co/datasets/luojunyu)

---

## 💡 一句话要点

**提出FinMME数据集以解决金融领域多模态评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态评估` `金融数据集` `大型语言模型` `数据质量` `评估系统`

## 📋 核心要点

1. 现有金融领域的多模态评估数据集缺乏有效性和专业性，限制了多模态大型语言模型的进一步发展。
2. 本文提出FinMME数据集，包含丰富的金融研究样本和多样的评估机制，以提升金融领域的多模态模型评估能力。
3. 实验结果显示，当前最先进的模型在FinMME上的表现不佳，数据集的预测变化率低于1%，展现出高鲁棒性。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）近年来发展迅速，但在金融领域缺乏有效的专门评估数据集。为推动金融领域MLLMs的发展，本文介绍了FinMME数据集，涵盖超过11,000个高质量金融研究样本，涉及18个金融领域和6种资产类别，包含10种主要图表类型和21种子类型。通过20名注释员和精心设计的验证机制确保数据质量。此外，开发了FinScore评估系统，结合幻觉惩罚和多维能力评估，提供无偏评估。实验结果表明，即使是最先进的模型如GPT-4o在FinMME上的表现也不尽如人意，突显了该数据集的挑战性。

## 🔬 方法详解

**问题定义**：本文旨在解决金融领域缺乏有效多模态评估数据集的问题，现有方法在评估金融多模态模型时存在不足，无法满足实际需求。

**核心思路**：通过构建FinMME数据集，整合多种金融领域的高质量样本，提供全面的评估机制，推动金融多模态模型的发展。

**技术框架**：FinMME数据集由超过11,000个样本组成，涵盖18个金融领域和6种资产类别，包含多种图表类型。评估系统FinScore则结合了幻觉惩罚和多维能力评估，确保评估的全面性和公正性。

**关键创新**：FinMME数据集的构建和FinScore评估系统是本文的主要创新，与现有数据集相比，提供了更高的样本质量和评估维度。

**关键设计**：数据集通过20名注释员进行标注，采用严格的验证机制确保数据质量；评估系统设计了多维度的能力评估和幻觉惩罚机制，以提高评估的准确性和可靠性。

## 📊 实验亮点

实验结果表明，当前最先进的模型如GPT-4o在FinMME数据集上的表现不理想，显示出该数据集的挑战性。同时，FinMME在不同提示下的预测变化率低于1%，展现出其高鲁棒性和可靠性。

## 🎯 应用场景

FinMME数据集及其评估系统可广泛应用于金融领域的多模态模型开发和评估，帮助研究人员和从业者更好地理解和应用多模态技术，提升金融决策的智能化水平。未来，该数据集有望推动金融科技的进一步创新与发展。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have experienced rapid development in recent years. However, in the financial domain, there is a notable lack of effective and specialized multimodal evaluation datasets. To advance the development of MLLMs in the finance domain, we introduce FinMME, encompassing more than 11,000 high-quality financial research samples across 18 financial domains and 6 asset classes, featuring 10 major chart types and 21 subtypes. We ensure data quality through 20 annotators and carefully designed validation mechanisms. Additionally, we develop FinScore, an evaluation system incorporating hallucination penalties and multi-dimensional capability assessment to provide an unbiased evaluation. Extensive experimental results demonstrate that even state-of-the-art models like GPT-4o exhibit unsatisfactory performance on FinMME, highlighting its challenging nature. The benchmark exhibits high robustness with prediction variations under different prompts remaining below 1%, demonstrating superior reliability compared to existing datasets. Our dataset and evaluation protocol are available at https://huggingface.co/datasets/luojunyu/FinMME and https://github.com/luo-junyu/FinMME.

