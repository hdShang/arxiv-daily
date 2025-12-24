---
layout: default
title: "Improving Crash Data Quality with Large Language Models: Evidence from Secondary Crash Narratives in Kentucky"
---

# Improving Crash Data Quality with Large Language Models: Evidence from Secondary Crash Narratives in Kentucky

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04399" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04399v1</a>
  <a href="https://arxiv.org/pdf/2508.04399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04399v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04399v1', 'Improving Crash Data Quality with Large Language Models: Evidence from Secondary Crash Narratives in Kentucky')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Zhang, Mei Chen

**分类**: cs.CL, cs.AI, cs.IR, cs.LG

**发布日期**: 2025-08-06

**备注**: 19 pages, 2 figures

---

## 💡 一句话要点

**利用大型语言模型提升肯塔基州事故数据质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `事故数据分析` `大型语言模型` `微调变换器` `交通安全` `数据质量提升`

## 📋 核心要点

1. 现有的事故数据处理方法在数据质量和效率上存在不足，尤其是在二次事故的识别上。
2. 本研究提出利用大型语言模型和微调的变换器模型来挖掘和分析事故叙述，以提升数据质量。
3. 实验结果显示，微调的RoBERTa模型在F1-score和准确率上均优于传统逻辑回归，且处理速度显著提高。

## 📝 摘要（中文）

本研究评估了先进的自然语言处理技术，通过挖掘事故叙述来提高事故数据质量，以肯塔基州的二次事故识别为案例。研究基于2015-2022年间手动审查的16,656条叙述，比较了三类模型：零样本开源大型语言模型（LLMs）、微调的变换器模型和传统的逻辑回归作为基线。微调的变换器模型表现优异，其中RoBERTa的F1-score达到0.90，准确率为95%。尽管LLMs在某些变体的召回率上表现出色，但计算成本较高，而微调模型在经过简短训练后能在几秒内处理测试集。研究结果强调了准确性、效率和数据需求之间的权衡，提供了一个可复制的方案以利用先进的NLP提升事故数据质量。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有事故数据处理方法在数据质量和效率上的不足，尤其是二次事故的识别困难。传统方法往往依赖于手动审查，效率低下且容易出错。

**核心思路**：论文的核心解决思路是利用大型语言模型和微调的变换器模型，通过自然语言处理技术自动化分析事故叙述，从而提高数据质量和处理效率。

**技术框架**：整体架构包括数据收集、模型训练和测试三个主要阶段。首先收集2015-2022年的事故叙述数据，然后对不同模型进行训练，最后在2022年的数据上进行测试和评估。

**关键创新**：最重要的技术创新点在于比较了多种模型，包括零样本大型语言模型和微调的变换器模型，发现微调模型在准确性和效率上具有显著优势，尤其是在处理速度上。

**关键设计**：在模型训练中，采用了多种变换器架构（如RoBERTa、BERT等）进行微调，设置了适当的超参数以优化模型性能，损失函数选择了适合分类任务的交叉熵损失。

## 📊 实验亮点

实验结果显示，微调的RoBERTa模型在F1-score上达到0.90，准确率为95%，显著优于传统逻辑回归（F1:0.66）。零样本LLaMA3:70B模型的F1-score为0.86，但推理时间长达139分钟，而微调模型则在几秒内完成测试，展现出更高的效率。

## 🎯 应用场景

该研究的潜在应用领域包括交通安全管理、事故数据分析和公共政策制定。通过提升事故数据的质量，相关部门能够更有效地识别事故原因，制定针对性的安全措施，从而减少交通事故的发生率，提升公共安全水平。

## 📄 摘要（原文）

> This study evaluates advanced natural language processing (NLP) techniques to enhance crash data quality by mining crash narratives, using secondary crash identification in Kentucky as a case study. Drawing from 16,656 manually reviewed narratives from 2015-2022, with 3,803 confirmed secondary crashes, we compare three model classes: zero-shot open-source large language models (LLMs) (LLaMA3:70B, DeepSeek-R1:70B, Qwen3:32B, Gemma3:27B); fine-tuned transformers (BERT, DistilBERT, RoBERTa, XLNet, Longformer); and traditional logistic regression as baseline. Models were calibrated on 2015-2021 data and tested on 1,771 narratives from 2022. Fine-tuned transformers achieved superior performance, with RoBERTa yielding the highest F1-score (0.90) and accuracy (95%). Zero-shot LLaMA3:70B reached a comparable F1 of 0.86 but required 139 minutes of inference; the logistic baseline lagged well behind (F1:0.66). LLMs excelled in recall for some variants (e.g., GEMMA3:27B at 0.94) but incurred high computational costs (up to 723 minutes for DeepSeek-R1:70B), while fine-tuned models processed the test set in seconds after brief training. Further analysis indicated that mid-sized LLMs (e.g., DeepSeek-R1:32B) can rival larger counterparts in performance while reducing runtime, suggesting opportunities for optimized deployments. Results highlight trade-offs between accuracy, efficiency, and data requirements, with fine-tuned transformer models balancing precision and recall effectively on Kentucky data. Practical deployment considerations emphasize privacy-preserving local deployment, ensemble approaches for improved accuracy, and incremental processing for scalability, providing a replicable scheme for enhancing crash-data quality with advanced NLP.

