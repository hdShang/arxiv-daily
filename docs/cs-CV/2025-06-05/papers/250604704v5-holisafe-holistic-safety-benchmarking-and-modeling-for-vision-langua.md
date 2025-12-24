---
layout: default
title: "HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model"
---

# HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04704" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04704v5</a>
  <a href="https://arxiv.org/pdf/2506.04704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04704v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04704v5', 'HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youngwan Lee, Kangsan Kim, Kwanyong Park, Ilcahe Jung, Soojin Jang, Seanie Lee, Yong-Ju Lee, Sung Ju Hwang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-11-25)

**备注**: Project page: https://youngwanlee.github.io/holisafe

---

## 💡 一句话要点

**提出HoliSafe以解决视觉语言模型安全性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `安全性评估` `多模态对齐` `数据集构建` `模块化设计` `有害内容识别` `深度学习`

## 📋 核心要点

1. 现有视觉语言模型的安全性面临两大挑战，现有方法未能全面考虑图像-文本交互的潜在危害。
2. 本文提出HoliSafe数据集和基准，涵盖所有五种安全/不安全的图像-文本组合，并引入视觉保护模块（VGM）以增强模型安全性。
3. 实验结果显示，使用VGM的Safe-VLM在多个基准上实现了最先进的安全性能，同时揭示了现有模型的关键脆弱性。

## 📝 摘要（中文）

尽管已有努力增强视觉语言模型（VLMs）的安全性，但现有方法存在两大不足：一是现有安全调优数据集和基准仅部分考虑图像-文本交互可能产生的有害内容，忽视了看似无害的组合可能导致的上下文不安全结果；二是以数据为中心的调优方法缺乏架构创新，无法从根本上增强安全性。为此，本文提出了一个全面的安全数据集和基准HoliSafe，涵盖所有五种安全/不安全的图像-文本组合，并提出了一种新颖的模块化框架，通过视觉保护模块（VGM）增强VLM的安全性。实验表明，基于HoliSafe训练的Safe-VLM在多个基准上达到了最先进的安全性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在安全性方面的不足，现有方法主要依赖于数据调优，缺乏对潜在有害内容的全面考虑，导致模型在未见配置下易受攻击。

**核心思路**：提出HoliSafe数据集和基准，全面涵盖安全与不安全的图像-文本组合，并设计视觉保护模块（VGM）来评估输入图像的有害性，从而增强模型的安全性和可解释性。

**技术框架**：整体架构包括HoliSafe数据集、HoliSafe-Bench基准和VGM模块。HoliSafe提供了丰富的训练和评估数据，而VGM作为插件模块，能够与多种预训练的VLM无缝集成。

**关键创新**：HoliSafe和VGM的最大创新在于其模块化设计，VGM不仅提升了模型生成安全响应的能力，还提供了可解释的有害性分类，帮助模型做出拒绝决策。

**关键设计**：VGM模块的设计允许灵活集成，具体参数设置和损失函数尚未详细披露，但其核心在于通过视觉信息评估输入的潜在危害性。

## 📊 实验亮点

实验结果表明，基于HoliSafe训练的Safe-VLM在多个视觉语言模型基准上达到了最先进的安全性能，显著提升了模型的安全性，具体性能数据尚未披露，但相较于现有模型显示出关键脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性要求高的多模态系统，如自动内容审核、社交媒体平台的内容过滤和智能助手等。通过提升视觉语言模型的安全性，HoliSafe和VGM能够在实际应用中减少有害内容的生成，增强用户信任，推动多模态对齐的进一步研究。

## 📄 摘要（原文）

> Despite emerging efforts to enhance the safety of Vision-Language Models (VLMs), current approaches face two main shortcomings. 1) Existing safety-tuning datasets and benchmarks only partially consider how image-text interactions can yield harmful content, often overlooking contextually unsafe outcomes from seemingly benign pairs. This narrow coverage leaves VLMs vulnerable to jailbreak attacks in unseen configurations. 2) Prior methods rely primarily on data-centric tuning, with limited architectural innovations to intrinsically strengthen safety. We address these gaps by introducing a holistic safety dataset and benchmark, \textbf{HoliSafe}, that spans all five safe/unsafe image-text combinations, providing a more robust basis for both training and evaluation (HoliSafe-Bench). We further propose a novel modular framework for enhancing VLM safety with a visual guard module (VGM) designed to assess the harmfulness of input images for VLMs. This module endows VLMs with a dual functionality: they not only learn to generate safer responses but can also provide an interpretable harmfulness classification to justify their refusal decisions. A significant advantage of this approach is its modularity; the VGM is designed as a plug-in component, allowing for seamless integration with diverse pre-trained VLMs across various scales. Experiments show that Safe-VLM with VGM, trained on our HoliSafe, achieves state-of-the-art safety performance across multiple VLM benchmarks. Additionally, the HoliSafe-Bench itself reveals critical vulnerabilities in existing VLM models. We hope that HoliSafe and VGM will spur further research into robust and interpretable VLM safety, expanding future avenues for multimodal alignment.

