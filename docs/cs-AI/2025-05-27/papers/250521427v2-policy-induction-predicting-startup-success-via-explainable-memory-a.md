---
layout: default
title: "Policy Induction: Predicting Startup Success via Explainable Memory-Augmented In-Context Learning"
---

# Policy Induction: Predicting Startup Success via Explainable Memory-Augmented In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21427" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21427v2</a>
  <a href="https://arxiv.org/pdf/2505.21427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21427v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21427v2', 'Policy Induction: Predicting Startup Success via Explainable Memory-Augmented In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianling Mu, Joseph Ternasky, Fuat Alican, Yigit Ihlamur

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-06-04)

---

## 💡 一句话要点

**提出基于记忆增强的上下文学习框架以预测初创企业成功**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `初创企业投资` `记忆增强` `上下文学习` `透明决策` `机器学习` `风险投资` `自然语言处理`

## 📋 核心要点

1. 现有的机器学习方法在初创企业投资中面临数据稀缺和结果不确定的挑战，难以提供透明的决策过程。
2. 本文提出了一种基于记忆增强的大型语言模型的投资决策框架，利用上下文学习实现透明和高效的决策。
3. 实验结果表明，该方法的预测准确率比随机猜测高出20倍，且比顶级风险投资公司的成功率高出7.1倍。

## 📝 摘要（中文）

早期初创企业投资是一项高风险的事业，面临数据稀缺和结果不确定的挑战。传统机器学习方法通常需要大量标注数据和广泛的调优，且难以被领域专家理解和改进。本文提出了一种透明且数据高效的投资决策框架，利用记忆增强的大型语言模型（LLMs）和上下文学习（ICL）。我们的方法将自然语言策略直接嵌入LLM提示中，使模型能够应用明确的推理模式，便于人类专家理解、审计和迭代优化逻辑。通过结合少量学习和上下文学习循环的轻量级训练过程，我们的系统在仅需最小监督且无基于梯度的优化情况下，能够比现有基准更准确地预测初创企业的成功。

## 🔬 方法详解

**问题定义**：本文旨在解决早期初创企业投资中数据稀缺和决策不透明的问题。现有方法往往依赖大量标注数据，且难以被领域专家理解和改进。

**核心思路**：本研究提出了一种透明的投资决策框架，利用记忆增强的大型语言模型，通过上下文学习实现高效的决策过程。自然语言策略的嵌入使得模型的推理过程更易于理解和优化。

**技术框架**：整体架构包括一个大型语言模型，结合少量学习和上下文学习循环。模型通过接收结构化反馈不断更新决策策略，形成一个迭代优化的过程。

**关键创新**：最重要的创新在于将自然语言策略直接嵌入模型提示中，使得推理过程透明化，便于人类专家进行审计和优化。这一设计与传统方法的黑箱特性形成鲜明对比。

**关键设计**：该方法采用轻量级训练过程，无需梯度优化，依赖于少量的监督信息。模型的参数设置和损失函数设计旨在支持上下文学习的高效性和透明性。整体结构简化了传统机器学习模型的复杂性。

## 📊 实验亮点

实验结果显示，该方法在预测初创企业成功率方面表现优异，准确率超过随机猜测的20倍，达到1.9%的成功率，且比顶级风险投资公司的5.6%成功率高出7.1倍，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括风险投资、创业孵化器和金融科技等，能够为投资决策提供更为透明和高效的支持。通过提高预测准确性，帮助投资者降低风险并优化投资组合，未来可能在创业生态系统中产生深远影响。

## 📄 摘要（原文）

> Early-stage startup investment is a high-risk endeavor characterized by scarce data and uncertain outcomes. Traditional machine learning approaches often require large, labeled datasets and extensive fine-tuning, yet remain opaque and difficult for domain experts to interpret or improve. In this paper, we propose a transparent and data-efficient investment decision framework powered by memory-augmented large language models (LLMs) using in-context learning (ICL). Central to our method is a natural language policy embedded directly into the LLM prompt, enabling the model to apply explicit reasoning patterns and allowing human experts to easily interpret, audit, and iteratively refine the logic. We introduce a lightweight training process that combines few-shot learning with an in-context learning loop, enabling the LLM to update its decision policy iteratively based on structured feedback. With only minimal supervision and no gradient-based optimization, our system predicts startup success far more accurately than existing benchmarks. It is over 20x more precise than random chance, which succeeds 1.9% of the time. It is also 7.1x more precise than the typical 5.6% success rate of top-tier venture capital (VC) firms.

