---
layout: default
title: Revisiting Model Inversion Evaluation: From Misleading Standards to Reliable Privacy Assessment
---

# Revisiting Model Inversion Evaluation: From Misleading Standards to Reliable Privacy Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03519" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03519v4</a>
  <a href="https://arxiv.org/pdf/2505.03519.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03519v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03519v4', 'Revisiting Model Inversion Evaluation: From Misleading Standards to Reliable Privacy Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sy-Tuyen Ho, Koh Jun Hao, Ngoc-Bao Nguyen, Alexander Binder, Ngai-Man Cheung

**分类**: cs.LG

**发布日期**: 2025-05-06 (更新: 2025-11-20)

**备注**: To support future work, we release our MLLM-based MI evaluation framework and benchmarking suite at https://github.com/hosytuyen/MI-Eval-MLLM

**🔗 代码/项目**: [GITHUB](https://github.com/hosytuyen/MI-Eval-MLLM)

---

## 💡 一句话要点

**提出新评估框架以解决模型反演攻击的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型反演攻击` `隐私评估` `多模态大型语言模型` `对抗样本` `机器学习安全` `评估框架` `隐私保护`

## 📋 核心要点

1. 现有的模型反演攻击评估框架存在类型-I对抗样本问题，导致假阳性率高，影响评估的可靠性。
2. 本文提出了一种新的评估框架，利用多模态大型语言模型（MLLM），不再依赖于与任务设计相同的评估模型。
3. 通过对27种MI攻击设置的重新评估，发现标准框架下的假阳性率普遍较高，实际隐私泄露程度被低估。

## 📝 摘要（中文）

模型反演（MI）攻击旨在通过利用机器学习模型的访问权限重建私有训练数据的信息。现有的评估框架依赖于与任务设计相同的评估模型，这导致了类型-I对抗样本的问题，即重建结果未能捕捉到私有训练数据的视觉特征，却仍被视为成功。本文首次深入研究了这一评估框架，提出了基于多模态大型语言模型（MLLM）的新评估框架，显著降低了类型-I 转移性，并提供了更真实的重建成功评估。通过对27种不同MI攻击设置的重新评估，发现标准评估框架下的假阳性率普遍较高，许多先进的MI方法报告的攻击准确率被夸大，实际隐私泄露远低于先前的估计。

## 🔬 方法详解

**问题定义**：本文解决的是现有模型反演攻击评估框架的可靠性问题，特别是类型-I对抗样本导致的假阳性现象，这使得评估结果不准确。

**核心思路**：论文的核心思路是引入多模态大型语言模型（MLLM）作为新的评估模型，利用其通用的视觉理解能力，避免依赖于与任务设计相同的训练模型，从而减少假阳性率。

**技术框架**：新框架的整体架构包括数据输入、MLLM处理、重建结果评估等主要模块。首先，输入私有训练数据，然后通过MLLM进行分析，最后评估重建结果的成功率。

**关键创新**：最重要的技术创新在于使用MLLM替代传统的评估模型，这一设计使得评估不再依赖于特定任务的训练，显著提高了评估的准确性和可靠性。

**关键设计**：在技术细节上，关键设计包括MLLM的选择与训练策略，损失函数的定义，以及如何有效地处理多模态数据以提高评估的全面性。具体参数设置和网络结构的细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，使用新评估框架后，27种MI攻击设置的假阳性率显著降低，许多先进MI方法的攻击准确率被重新评估，实际隐私泄露程度远低于先前的估计。这一发现对MI研究的进展具有重要影响。

## 🎯 应用场景

该研究的潜在应用领域包括机器学习模型的安全性评估、隐私保护技术的开发以及相关法规的制定。通过提供更可靠的评估标准，研究成果能够帮助研究人员和从业者更准确地理解模型反演攻击的风险，从而制定更有效的防护措施。

## 📄 摘要（原文）

> Model Inversion (MI) attacks aim to reconstruct information from private training data by exploiting access to machine learning models T. To evaluate such attacks, the standard evaluation framework relies on an evaluation model E, trained under the same task design as T. This framework has become the de facto standard for assessing progress in MI research, used across nearly all recent MI studies without question. In this paper, we present the first in-depth study of this evaluation framework. In particular, we identify a critical issue of this standard framework: Type-I adversarial examples. These are reconstructions that do not capture the visual features of private training data, yet are still deemed successful by T and ultimately transferable to E. Such false positives undermine the reliability of the standard MI evaluation framework. To address this issue, we introduce a new MI evaluation framework that replaces the evaluation model E with advanced Multimodal Large Language Models (MLLMs). By leveraging their general-purpose visual understanding, our MLLM-based framework does not depend on training of shared task design as in T, thus reducing Type-I transferability and providing more faithful assessments of reconstruction success. Using our MLLM-based evaluation framework, we reevaluate 27 diverse MI attack setups and empirically reveal consistently high false positive rates under the standard evaluation framework. Importantly, we demonstrate that many state-of-the-art (SOTA) MI methods report inflated attack accuracy, indicating that actual privacy leakage is significantly lower than previously believed. By uncovering this critical issue and proposing a robust solution, our work enables a reassessment of progress in MI research and sets a new standard for reliable and robust evaluation. Code can be found in https://github.com/hosytuyen/MI-Eval-MLLM

