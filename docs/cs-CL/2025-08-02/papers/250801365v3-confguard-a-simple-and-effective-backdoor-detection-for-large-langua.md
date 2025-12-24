---
layout: default
title: "ConfGuard: A Simple and Effective Backdoor Detection for Large Language Models"
---

# ConfGuard: A Simple and Effective Backdoor Detection for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01365" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01365v3</a>
  <a href="https://arxiv.org/pdf/2508.01365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01365v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01365v3', 'ConfGuard: A Simple and Effective Backdoor Detection for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Rui Zhang, Hongwei Li, Wenshu Fan, Wenbo Jiang, Qingchuan Zhao, Guowen Xu

**分类**: cs.CR, cs.CL

**发布日期**: 2025-08-02 (更新: 2025-11-11)

**备注**: This is an extended version of the copyrighted publication at AAAI

---

## 💡 一句话要点

**提出ConfGuard以解决大语言模型的后门检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门检测` `大语言模型` `序列锁` `置信度监控` `安全防护`

## 📋 核心要点

1. 现有的后门检测方法主要针对分类任务，无法有效应对大语言模型的自回归特性，导致性能低下和延迟高。
2. 论文提出了一种新的检测方法ConfGuard，通过监控令牌置信度的滑动窗口来识别后门模型的序列锁现象。
3. 实验结果显示，ConfGuard在绝大多数情况下实现了接近100%的真正阳性率和极低的假阳性率，且几乎没有额外延迟。

## 📝 摘要（中文）

后门攻击对大语言模型（LLMs）构成了重大威胁，攻击者可以嵌入隐藏触发器来操控LLM的输出。现有的防御方法主要针对分类任务，无法有效应对LLMs的自回归特性和广泛的输出空间，导致性能差和延迟高。为了解决这些局限性，我们研究了良性和后门LLMs在输出空间中的行为差异，发现了一种关键现象——序列锁：后门模型生成目标序列时的置信度异常高且一致。基于这一洞察，我们提出了ConfGuard，这是一种轻量级且有效的检测方法，通过监控令牌置信度的滑动窗口来识别序列锁。大量实验表明，ConfGuard在绝大多数情况下实现了接近100%的真正阳性率和微不足道的假阳性率，且几乎没有额外延迟，成为现实世界LLM部署的实用后门防御方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型中的后门攻击检测问题。现有方法在处理自回归特性和广泛输出空间时表现不佳，导致检测效果差和延迟高。

**核心思路**：论文的核心思路是通过识别良性和后门LLMs在输出空间中的行为差异，特别是序列锁现象，后者表现为后门模型生成目标序列时的置信度异常高且一致。

**技术框架**：ConfGuard的整体架构包括一个监控模块，该模块使用滑动窗口技术来跟踪生成令牌的置信度，并通过分析这些置信度来判断是否存在后门攻击。

**关键创新**：最重要的技术创新点在于识别并利用序列锁现象，提供了一种新的检测机制，与现有方法相比，能够更有效地应对大语言模型的特性。

**关键设计**：在设计中，ConfGuard采用了滑动窗口的参数设置，以便实时监控令牌生成的置信度，并通过设定阈值来判断是否触发后门检测。

## 📊 实验亮点

实验结果表明，ConfGuard在绝大多数情况下实现了接近100%的真正阳性率和极低的假阳性率，几乎没有额外延迟，显示出其在实际应用中的高效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和自动生成内容等场景。ConfGuard能够为这些领域中的大语言模型提供有效的安全防护，确保模型输出的可靠性和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Backdoor attacks pose a significant threat to Large Language Models (LLMs), where adversaries can embed hidden triggers to manipulate LLM's outputs. Most existing defense methods, primarily designed for classification tasks, are ineffective against the autoregressive nature and vast output space of LLMs, thereby suffering from poor performance and high latency. To address these limitations, we investigate the behavioral discrepancies between benign and backdoored LLMs in output space. We identify a critical phenomenon which we term sequence lock: a backdoored model generates the target sequence with abnormally high and consistent confidence compared to benign generation. Building on this insight, we propose ConfGuard, a lightweight and effective detection method that monitors a sliding window of token confidences to identify sequence lock. Extensive experiments demonstrate ConfGuard achieves a near 100\% true positive rate (TPR) and a negligible false positive rate (FPR) in the vast majority of cases. Crucially, the ConfGuard enables real-time detection almost without additional latency, making it a practical backdoor defense for real-world LLM deployments.

