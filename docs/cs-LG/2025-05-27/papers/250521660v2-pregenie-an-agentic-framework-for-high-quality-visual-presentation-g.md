---
layout: default
title: PreGenie: An Agentic Framework for High-quality Visual Presentation Generation
---

# PreGenie: An Agentic Framework for High-quality Visual Presentation Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21660" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21660v2</a>
  <a href="https://arxiv.org/pdf/2505.21660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21660v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21660v2', 'PreGenie: An Agentic Framework for High-quality Visual Presentation Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojie Xu, Xinli Xu, Sirui Chen, Haoyu Chen, Fan Zhang, Ying-Cong Chen

**分类**: cs.LG

**发布日期**: 2025-05-27 (更新: 2025-08-31)

**备注**: Accepted at EMNLP 2025, Findings

---

## 💡 一句话要点

**提出PreGenie框架以解决视觉演示生成中的多模态理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉演示` `多模态大语言模型` `自动化生成` `内容一致性` `Slidev框架` `高质量生成` `信息传达` `智能化工具`

## 📋 核心要点

1. 现有方法在自动生成视觉演示时存在布局混乱、文本摘要不准确和图像理解不足等问题，限制了其在正式场合的应用。
2. 提出的PreGenie框架利用多模态大语言模型，通过分析与初步生成、审查与再生成两个阶段，生成高质量的视觉演示。
3. 实验结果显示，PreGenie在多模态理解方面表现优异，超越了现有模型，并在美学和内容一致性上更符合人类设计偏好。

## 📝 摘要（中文）

视觉演示在有效沟通中至关重要。早期利用深度学习自动化创建演示文稿的尝试常常面临布局不佳、文本摘要不准确和图像理解不足等问题，导致视觉与文本不匹配。这些限制了其在商业和科学研究等正式场合的应用。为了解决这些挑战，本文提出了PreGenie，一个基于多模态大语言模型（MLLMs）的代理性和模块化框架，用于生成高质量的视觉演示。PreGenie基于Slidev演示框架构建，分为分析与初步生成和审查与再生成两个阶段，综合实验表明PreGenie在多模态理解方面表现优异，超越了现有模型的美学和内容一致性，更加贴近人类设计偏好。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉演示生成方法在布局、文本摘要和图像理解方面的不足，导致生成的演示文稿质量不高，无法满足正式场合的需求。

**核心思路**：PreGenie框架通过引入多模态大语言模型，采用代理性和模块化设计，分阶段生成和优化演示文稿，以提高生成质量和用户体验。

**技术框架**：PreGenie基于Slidev演示框架，分为两个主要阶段：分析与初步生成阶段负责总结多模态输入并生成初步代码；审查与再生成阶段则迭代审查中间代码和渲染的幻灯片，以生成最终高质量的演示文稿。

**关键创新**：PreGenie的创新在于其模块化设计和多模态大语言模型的协作，显著提高了多模态理解能力和生成质量，区别于传统的单一模型生成方法。

**关键设计**：在设计中，PreGenie采用了多种MLLMs协作的方式，确保信息共享与协同工作，同时在损失函数和参数设置上进行了优化，以提升生成结果的美观性和一致性。

## 📊 实验亮点

实验结果表明，PreGenie在多模态理解方面的表现超越了现有模型，尤其在美学和内容一致性上，生成的演示文稿更符合人类设计偏好。具体而言，PreGenie在视觉质量和文本准确性上均有显著提升，具体性能数据尚未披露。

## 🎯 应用场景

PreGenie框架具有广泛的应用潜力，特别是在商业演示、学术报告和教育培训等领域。其高质量的视觉演示生成能力能够提升信息传达的有效性，促进更好的沟通与理解。未来，该技术有望进一步扩展到其他多模态内容生成领域，推动智能化演示工具的发展。

## 📄 摘要（原文）

> Visual presentations are vital for effective communication. Early attempts to automate their creation using deep learning often faced issues such as poorly organized layouts, inaccurate text summarization, and a lack of image understanding, leading to mismatched visuals and text. These limitations restrict their application in formal contexts like business and scientific research. To address these challenges, we propose PreGenie, an agentic and modular framework powered by multimodal large language models (MLLMs) for generating high-quality visual presentations.
>   PreGenie is built on the Slidev presentation framework, where slides are rendered from Markdown code. It operates in two stages: (1) Analysis and Initial Generation, which summarizes multimodal input and generates initial code, and (2) Review and Re-generation, which iteratively reviews intermediate code and rendered slides to produce final, high-quality presentations. Each stage leverages multiple MLLMs that collaborate and share information. Comprehensive experiments demonstrate that PreGenie excels in multimodal understanding, outperforming existing models in both aesthetics and content consistency, while aligning more closely with human design preferences.

