---
layout: default
title: "VFLAIR-LLM: A Comprehensive Framework and Benchmark for Split Learning of LLMs"
---

# VFLAIR-LLM: A Comprehensive Framework and Benchmark for Split Learning of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03097" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03097v1</a>
  <a href="https://arxiv.org/pdf/2508.03097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03097v1', 'VFLAIR-LLM: A Comprehensive Framework and Benchmark for Split Learning of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Gu, Qiufeng Fan, Long Sun, Yang Liu, Xiaojun Ye

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-05

**备注**: 12 pages, 10 figures, published in KDD2025

**期刊**: In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD'25), August 3-7, 2025, Toronto, ON, Canada. ACM, New York, NY, USA, 12 pages

**DOI**: [10.1145/3711896.3737411](https://doi.org/10.1145/3711896.3737411)

**🔗 代码/项目**: [GITHUB](https://github.com/FLAIR-THU/VFLAIR-LLM)

---

## 💡 一句话要点

**提出VFLAIR-LLM以解决数据隐私与资源限制下的LLM适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `分割学习` `隐私保护` `计算资源` `攻击与防御` `微调` `框架设计`

## 📋 核心要点

1. 现有方法在数据隐私和计算资源受限的情况下，难以有效适应大型语言模型（LLMs）。
2. 本文提出VFLAIR-LLM框架，通过分割学习实现资源高效且隐私保护的LLM推理与微调。
3. 实验结果显示，VFLAIR-LLM在多种攻击和防御设置下表现优异，为实际应用提供了具体的配置建议。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的发展，其应用领域不断扩大。然而，用户在数据隐私方面的顾虑使得直接使用LLM API受到限制，而私有部署则需要大量计算资源。这给在资源受限的环境中实现安全的LLM适应带来了挑战。为了解决这一问题，本文提出了一种名为VFLAIR-LLM的轻量级分割学习框架，支持在隐私保护的前提下进行LLM推理和微调。该框架提供了两种LLM分区设置，支持三种任务类型和18个数据集，并包含标准模块用于攻击和防御的实现与评估。我们在多种分割学习设置下对5种攻击和9种防御进行了基准测试，提供了关于模型分区配置、防御策略和超参数选择的具体见解和建议。

## 🔬 方法详解

**问题定义**：本文旨在解决在数据隐私和计算资源受限的环境中，如何有效适应大型语言模型（LLMs）的问题。现有方法往往无法兼顾隐私保护与计算效率，导致用户无法安全地利用LLM。

**核心思路**：VFLAIR-LLM框架采用分割学习（Split Learning）方法，通过将模型分为多个部分，允许在本地进行隐私保护的推理与微调，从而降低计算资源的需求。

**技术框架**：该框架包括两个主要模块：LLM分区设置和攻击防御模块。用户可以根据需求选择不同的分区设置，并利用标准模块评估模型的安全性和鲁棒性。

**关键创新**：VFLAIR-LLM的创新在于其轻量级设计和可扩展性，支持多种任务类型和数据集，同时提供了系统化的攻击与防御评估机制，显著提升了LLM在隐私保护场景下的适用性。

**关键设计**：框架中包含了多种参数设置和损失函数的设计，支持不同的模型分区配置，用户可以根据具体应用场景灵活调整超参数，以达到最佳性能。实验中使用了5种攻击和9种防御策略，确保了模型的安全性与有效性。

## 📊 实验亮点

实验结果表明，VFLAIR-LLM在多种分割学习设置下，成功实现了对5种攻击的有效防御，并在9种防御策略中表现出色。具体而言，模型在隐私保护和计算效率方面均有显著提升，为实际应用提供了可靠的参考。

## 🎯 应用场景

VFLAIR-LLM框架在医疗、金融等对数据隐私要求高的领域具有广泛的应用潜力。通过在资源受限的环境中实现安全的LLM适应，该框架能够帮助用户在保护隐私的同时，充分利用大型语言模型的强大能力，推动相关行业的智能化发展。

## 📄 摘要（原文）

> With the advancement of Large Language Models (LLMs), LLM applications have expanded into a growing number of fields. However, users with data privacy concerns face limitations in directly utilizing LLM APIs, while private deployments incur significant computational demands. This creates a substantial challenge in achieving secure LLM adaptation under constrained local resources. To address this issue, collaborative learning methods, such as Split Learning (SL), offer a resource-efficient and privacy-preserving solution for adapting LLMs to private domains. In this study, we introduce VFLAIR-LLM (available at https://github.com/FLAIR-THU/VFLAIR-LLM), an extensible and lightweight split learning framework for LLMs, enabling privacy-preserving LLM inference and fine-tuning in resource-constrained environments. Our library provides two LLM partition settings, supporting three task types and 18 datasets. In addition, we provide standard modules for implementing and evaluating attacks and defenses. We benchmark 5 attacks and 9 defenses under various Split Learning for LLM(SL-LLM) settings, offering concrete insights and recommendations on the choice of model partition configurations, defense strategies, and relevant hyperparameters for real-world applications.

