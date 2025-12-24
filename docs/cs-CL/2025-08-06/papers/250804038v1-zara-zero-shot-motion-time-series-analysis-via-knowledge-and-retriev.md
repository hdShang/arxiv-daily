---
layout: default
title: "ZARA: Zero-shot Motion Time-Series Analysis via Knowledge and Retrieval Driven LLM Agents"
---

# ZARA: Zero-shot Motion Time-Series Analysis via Knowledge and Retrieval Driven LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04038" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04038v1</a>
  <a href="https://arxiv.org/pdf/2508.04038.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04038v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04038v1', 'ZARA: Zero-shot Motion Time-Series Analysis via Knowledge and Retrieval Driven LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zechen Li, Baiyu Chen, Hao Xue, Flora D. Salim

**分类**: cs.CL, cs.CV

**发布日期**: 2025-08-06

**🔗 代码/项目**: [GITHUB](https://github.com/zechenli03/ZARA)

---

## 💡 一句话要点

**提出ZARA框架以解决零-shot人类活动识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零-shot学习` `人类活动识别` `运动时间序列` `可解释人工智能` `多传感器融合` `代理驱动框架` `知识库` `智能设备`

## 📋 核心要点

1. 现有HAR方法通常需要针对固定活动集进行训练，面对新行为时需昂贵的再训练，缺乏灵活性。
2. ZARA框架通过集成知识库和多传感器检索模块，实现了从原始时间序列进行零-shot的可解释HAR。
3. 在8个HAR基准上，ZARA的宏观F1分数超过最强基线2.53倍，展现出优越的性能和清晰的推理能力。

## 📝 摘要（中文）

运动传感器时间序列在人体活动识别（HAR）中至关重要，广泛应用于健康、体育和智能设备。然而，现有方法通常针对固定的活动集进行训练，面对新行为或传感器设置时需要昂贵的再训练。本文提出ZARA，这是第一个基于代理的框架，能够直接从原始运动时间序列进行零-shot、可解释的HAR。ZARA集成了自动生成的成对特征知识库、多传感器检索模块和分层代理管道，能够灵活且可解释地进行HAR，而无需任何微调或任务特定的分类器。在8个HAR基准上的广泛实验表明，ZARA在零-shot性能上达到了SOTA，宏观F1分数超过最强基线2.53倍。消融研究进一步确认了每个模块的必要性，标志着ZARA在可信赖的即插即用运动时间序列分析方面的有希望的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有HAR方法在面对新活动或传感器设置时的灵活性不足和高昂的再训练成本。现有方法通常依赖于固定的活动集，限制了其适用性和扩展性。

**核心思路**：ZARA框架的核心思想是通过构建一个自动生成的成对特征知识库和多传感器检索模块，直接从原始运动时间序列进行零-shot的可解释HAR。这种设计使得系统能够在不需要微调的情况下，灵活应对新活动。

**技术框架**：ZARA的整体架构包括三个主要模块：成对特征知识库、检索模块和分层代理管道。成对特征知识库捕捉每对活动的判别统计信息，检索模块提供相关证据，而分层代理管道引导LLM迭代选择特征并生成活动预测和自然语言解释。

**关键创新**：ZARA的主要创新在于其代理驱动的框架设计，能够实现零-shot的可解释性，区别于传统方法需要针对特定任务进行训练的局限性。

**关键设计**：ZARA的设计中，成对特征知识库的构建和多传感器检索模块的实现是关键，确保了系统能够有效地提取和利用运动时间序列中的信息。

## 📊 实验亮点

ZARA在8个HAR基准测试中表现出色，宏观F1分数超过最强基线2.53倍，展现出其在零-shot人类活动识别中的领先性能。此外，ZARA提供清晰的推理过程，增强了系统的可解释性，标志着在运动时间序列分析领域的重要进展。

## 🎯 应用场景

ZARA框架在健康监测、智能家居和体育分析等领域具有广泛的应用潜力。通过实现零-shot的活动识别，ZARA能够快速适应新环境和新活动，降低了系统部署和维护的成本，提升了用户体验。未来，该框架可能推动更多智能设备的普及与应用，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Motion sensor time-series are central to human activity recognition (HAR), with applications in health, sports, and smart devices. However, existing methods are trained for fixed activity sets and require costly retraining when new behaviours or sensor setups appear. Recent attempts to use large language models (LLMs) for HAR, typically by converting signals into text or images, suffer from limited accuracy and lack verifiable interpretability. We propose ZARA, the first agent-based framework for zero-shot, explainable HAR directly from raw motion time-series. ZARA integrates an automatically derived pair-wise feature knowledge base that captures discriminative statistics for every activity pair, a multi-sensor retrieval module that surfaces relevant evidence, and a hierarchical agent pipeline that guides the LLM to iteratively select features, draw on this evidence, and produce both activity predictions and natural-language explanations. ZARA enables flexible and interpretable HAR without any fine-tuning or task-specific classifiers. Extensive experiments on 8 HAR benchmarks show that ZARA achieves SOTA zero-shot performance, delivering clear reasoning while exceeding the strongest baselines by 2.53x in macro F1. Ablation studies further confirm the necessity of each module, marking ZARA as a promising step toward trustworthy, plug-and-play motion time-series analysis. Our codes are available at https://github.com/zechenli03/ZARA.

