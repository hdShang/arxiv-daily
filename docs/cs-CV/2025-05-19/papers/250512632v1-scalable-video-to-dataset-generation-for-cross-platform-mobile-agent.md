---
layout: default
title: Scalable Video-to-Dataset Generation for Cross-Platform Mobile Agents
---

# Scalable Video-to-Dataset Generation for Cross-Platform Mobile Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12632" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12632v1</a>
  <a href="https://arxiv.org/pdf/2505.12632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12632v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12632v1', 'Scalable Video-to-Dataset Generation for Cross-Platform Mobile Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunseok Jang, Yeda Song, Sungryull Sohn, Lajanugen Logeswaran, Tiange Luo, Dong-Ki Kim, Kyunghoon Bae, Honglak Lee

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-19

**备注**: CVPR 2025

---

## 💡 一句话要点

**提出MONDAY数据集以解决跨平台移动操作系统导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动操作系统` `数据集生成` `跨平台学习` `自动化框架` `视觉代理`

## 📋 核心要点

1. 现有的移动操作系统导航数据集通常局限于单一平台，缺乏跨平台的泛化能力，限制了模型的应用范围。
2. 论文提出了MONDAY数据集和自动化框架，通过利用YouTube视频生成多样化的移动操作系统导航数据，解决了数据收集的效率问题。
3. 实验结果表明，使用MONDAY数据集进行预训练的模型在未见过的移动操作系统平台上平均性能提升18.11%，显示出显著的跨平台适应能力。

## 📝 摘要（中文）

随着大型语言模型（LLMs）和视觉-语言模型（VLMs）的进步，开发图形用户界面（GUI）视觉代理的兴趣显著增加。我们介绍了MONDAY（来自YouTube的移动操作系统导航任务数据集），这是一个包含来自20,000个教学视频的313,000个注释帧的大规模数据集，捕捉了多平台的真实世界移动操作系统导航。将MONDAY纳入预训练阶段的模型展现出强大的跨平台泛化能力，相比于仅在单一操作系统数据集上训练的模型，平均性能提升达18.11%。为了支持数据集的持续扩展，我们提出了一种自动化框架，利用公开视频内容创建全面的任务数据集，无需手动注释。该框架包括强大的基于OCR的场景检测（F1分数95.04%）、几乎完美的用户界面元素检测（命中率99.87%）和新颖的多步骤动作识别，以提取不同界面配置下的可靠动作序列。我们贡献了MONDAY数据集和自动化收集框架，以促进未来在移动操作系统导航领域的研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有移动操作系统导航数据集的局限性，尤其是其在跨平台泛化能力上的不足。现有方法通常依赖于单一操作系统的数据，导致模型在新平台上的表现不佳。

**核心思路**：论文的核心思路是通过构建一个大规模的多平台数据集（MONDAY），并结合自动化框架，利用公开视频内容生成高质量的导航任务数据，减少人工标注的需求。

**技术框架**：整体架构包括三个主要模块：1) 基于OCR的场景检测，2) 用户界面元素检测，3) 多步骤动作识别。该框架能够自动从视频中提取导航任务数据，形成完整的数据集。

**关键创新**：最重要的技术创新在于提出了一个自动化的数据集生成框架，结合了高效的OCR技术和精确的UI元素检测，显著提高了数据收集的效率和准确性。

**关键设计**：在技术细节上，框架采用了高达95.04%的F1分数的OCR场景检测和99.87%的UI元素检测命中率，确保了数据的高质量。此外，设计了多步骤动作识别机制，以提取复杂的用户交互序列。

## 📊 实验亮点

实验结果显示，使用MONDAY数据集进行预训练的模型在未见过的移动操作系统平台上，平均性能提升达18.11个百分点，显著优于仅在单一操作系统数据集上训练的模型。这一结果表明，MONDAY数据集在跨平台泛化能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括移动应用开发、用户体验研究和人机交互设计等。通过提供丰富的导航任务数据，研究人员和开发者可以更好地训练和评估跨平台的智能代理，提升用户在不同操作系统上的操作体验。未来，该框架还可以扩展到其他领域，如自动驾驶和机器人导航等。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs) and Vision-Language Models (VLMs) have sparked significant interest in developing GUI visual agents. We introduce MONDAY (Mobile OS Navigation Task Dataset for Agents from YouTube), a large-scale dataset of 313K annotated frames from 20K instructional videos capturing diverse real-world mobile OS navigation across multiple platforms. Models that include MONDAY in their pre-training phases demonstrate robust cross-platform generalization capabilities, consistently outperforming models trained on existing single OS datasets while achieving an average performance gain of 18.11%p on an unseen mobile OS platform. To enable continuous dataset expansion as mobile platforms evolve, we present an automated framework that leverages publicly available video content to create comprehensive task datasets without manual annotation. Our framework comprises robust OCR-based scene detection (95.04% F1score), near-perfect UI element detection (99.87% hit ratio), and novel multi-step action identification to extract reliable action sequences across diverse interface configurations. We contribute both the MONDAY dataset and our automated collection framework to facilitate future research in mobile OS navigation.

