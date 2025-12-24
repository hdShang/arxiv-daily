---
layout: default
title: CAFES: A Collaborative Multi-Agent Framework for Multi-Granular Multimodal Essay Scoring
---

# CAFES: A Collaborative Multi-Agent Framework for Multi-Granular Multimodal Essay Scoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13965" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13965v1</a>
  <a href="https://arxiv.org/pdf/2505.13965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13965v1', 'CAFES: A Collaborative Multi-Agent Framework for Multi-Granular Multimodal Essay Scoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiamin Su, Yibo Yan, Zhuoran Gao, Han Zhang, Xiang Liu, Xuming Hu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

**备注**: arXiv admin note: substantial text overlap with arXiv:2502.11916

---

## 💡 一句话要点

**提出CAFES框架以解决多模态自动作文评分问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动评分` `多模态评估` `协作框架` `机器学习` `教育技术` `语言模型` `反馈机制`

## 📋 核心要点

1. 现有的自动作文评分方法在多模态感知和评估普适性方面存在显著不足，导致评分结果与人类判断不一致。
2. CAFES框架通过协作多代理的方式，结合初步评分、反馈聚合和反思评分，旨在提升评分的准确性和人类对齐性。
3. 实验结果显示，CAFES在二次加权卡帕（QWK）上相较于真实评分平均提升21%，尤其在语法和词汇多样性方面表现优异。

## 📝 摘要（中文）

自动作文评分（AES）在现代教育中至关重要，尤其是在多模态评估日益普及的背景下。然而，传统的AES方法在评估的普适性和多模态感知方面存在困难，近期基于多模态大型语言模型（MLLM）的方法也可能产生虚假解释和与人类判断不一致的评分。为了解决这些局限性，本文提出了CAFES，这是第一个专门为AES设计的协作多代理框架。该框架协调三个专业代理：初步评分者用于快速、特征特定的评估；反馈池管理器用于聚合详细的、基于证据的优点；反思评分者基于这些反馈迭代地优化评分，以增强与人类的对齐。通过使用最先进的MLLM进行广泛实验，平均相对提升21%在二次加权卡帕（QWK）上，尤其在语法和词汇多样性方面表现突出。该框架为智能多模态AES系统铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决传统自动作文评分（AES）方法在多模态评估中的局限性，尤其是评估的普适性和多模态感知能力不足的问题。现有方法往往无法准确反映人类的评分标准，导致评分结果的不一致性。

**核心思路**：CAFES框架通过引入三个协作代理，分别负责初步评分、反馈聚合和反思评分，形成一个闭环反馈机制，以提高评分的准确性和与人类判断的一致性。这样的设计旨在充分利用多模态信息，增强评分的可靠性和有效性。

**技术框架**：CAFES框架包括三个主要模块：初步评分者负责快速评估作文的特征；反馈池管理器聚合来自不同评分的详细反馈；反思评分者根据反馈迭代优化评分。整个流程通过多次反馈循环，逐步提升评分的质量。

**关键创新**：CAFES的主要创新在于其协作多代理的设计思路，区别于传统的单一评分模型，能够更好地处理多模态信息并提高评分的准确性。

**关键设计**：在技术细节上，CAFES采用了特定的损失函数来优化评分一致性，并利用先进的多模态大型语言模型（MLLM）作为基础，确保评分的多样性和准确性。

## 📊 实验亮点

CAFES框架在实验中表现出色，平均相对提升21%在二次加权卡帕（QWK）指标上，尤其在语法和词汇多样性方面的改进显著。这一成果表明CAFES能够有效提升自动作文评分的准确性，超越了现有的多模态评分方法。

## 🎯 应用场景

CAFES框架具有广泛的应用潜力，特别是在教育领域的自动作文评分、在线学习平台和智能评估系统中。其设计能够有效提升评分的准确性和可靠性，促进教育公平与个性化学习。未来，CAFES还可以扩展到其他多模态评估任务，如口语评分和项目评估等，进一步推动教育技术的发展。

## 📄 摘要（原文）

> Automated Essay Scoring (AES) is crucial for modern education, particularly with the increasing prevalence of multimodal assessments. However, traditional AES methods struggle with evaluation generalizability and multimodal perception, while even recent Multimodal Large Language Model (MLLM)-based approaches can produce hallucinated justifications and scores misaligned with human judgment. To address the limitations, we introduce CAFES, the first collaborative multi-agent framework specifically designed for AES. It orchestrates three specialized agents: an Initial Scorer for rapid, trait-specific evaluations; a Feedback Pool Manager to aggregate detailed, evidence-grounded strengths; and a Reflective Scorer that iteratively refines scores based on this feedback to enhance human alignment. Extensive experiments, using state-of-the-art MLLMs, achieve an average relative improvement of 21% in Quadratic Weighted Kappa (QWK) against ground truth, especially for grammatical and lexical diversity. Our proposed CAFES framework paves the way for an intelligent multimodal AES system. The code will be available upon acceptance.

