---
layout: default
title: "VISOR: Visual Input-based Steering for Output Redirection in Vision-Language Models"
---

# VISOR: Visual Input-based Steering for Output Redirection in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08521" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08521v1</a>
  <a href="https://arxiv.org/pdf/2508.08521.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08521v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08521v1', 'VISOR: Visual Input-based Steering for Output Redirection in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mansi Phute, Ravikumar Balakrishnan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出VISOR以解决视觉输入引导输出重定向问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `行为控制` `输出重定向` `多模态模型` `安全性` `引导图像` `激活模式`

## 📋 核心要点

1. 现有的行为控制方法如系统提示易被检测且效果不佳，且基于激活的引导向量需要对模型内部进行侵入式访问，限制了其应用。
2. 本文提出VISOR，通过优化视觉输入实现复杂的行为控制，能够在不接触模型内部的情况下进行有效的输出重定向。
3. 实验结果表明，VISOR在多个任务上表现优异，尤其在负向引导上效果显著，提供了比传统方法更强的控制能力。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多种应用中日益普及，安全性和行为控制问题变得尤为重要。现有的行为控制方法，如系统提示，容易被检测且效果有限，而基于激活的引导向量需要对模型内部进行侵入式访问，不适合API服务和闭源部署。本文提出VISOR（基于视觉输入的输出重定向引导），通过优化视觉输入实现复杂的行为控制。VISOR通过制作通用引导图像诱导目标激活模式，能够在所有VLM服务模式中进行实用部署，并且相较于显式文本指令更为隐蔽。我们在LLaVA-1.5-7B上验证了VISOR在拒绝、谄媚和生存本能三个关键对齐任务上的表现。单个150KB的引导图像在正向行为转变上与引导向量的表现相差仅1-2%，而在负向引导上则显著超过，引导效果达到基线的25%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在行为控制和输出重定向方面的不足，尤其是现有方法的可检测性和对模型内部的侵入式要求。

**核心思路**：VISOR的核心思路是通过优化视觉输入，制作通用引导图像来诱导目标激活模式，从而实现复杂的行为控制，而无需直接访问模型内部。

**技术框架**：VISOR的整体架构包括三个主要模块：视觉输入生成模块、激活模式诱导模块和行为控制模块。视觉输入生成模块负责创建引导图像，激活模式诱导模块用于分析和优化激活模式，行为控制模块则实现输出重定向。

**关键创新**：VISOR的关键创新在于其通过视觉输入实现行为控制的能力，避免了传统方法的侵入式访问需求，并且在隐蔽性上优于文本指令。

**关键设计**：在设计中，VISOR使用了特定的损失函数来优化引导图像的生成，同时确保其在不同任务中的有效性。引导图像的大小和复杂度经过精心调整，以确保在保持高效性的同时不影响模型的整体性能。

## 📊 实验亮点

实验结果显示，VISOR在正向行为转变上与引导向量的表现相差仅1-2%，而在负向引导上则显著超过，引导效果达到基线的25%。与传统的系统提示方法相比，VISOR提供了更强的双向控制能力，同时在14,000个无关MMLU任务上保持了99.9%的性能。

## 🎯 应用场景

VISOR的研究成果在多个领域具有潜在应用价值，包括安全性增强、用户行为引导和人机交互等。通过优化视觉输入，VISOR能够在不干扰模型内部的情况下实现有效的行为控制，适用于API服务和闭源部署的场景。未来，VISOR可能会推动多模态模型控制的研究进展，并促使相关防御机制的发展。

## 📄 摘要（原文）

> Vision Language Models (VLMs) are increasingly being used in a broad range of applications, bringing their security and behavioral control to the forefront. While existing approaches for behavioral control or output redirection, like system prompting in VLMs, are easily detectable and often ineffective, activation-based steering vectors require invasive runtime access to model internals--incompatible with API-based services and closed-source deployments. We introduce VISOR (Visual Input-based Steering for Output Redirection), a novel method that achieves sophisticated behavioral control through optimized visual inputs alone. By crafting universal steering images that induce target activation patterns, VISOR enables practical deployment across all VLM serving modalities while remaining imperceptible compared to explicit textual instructions. We validate VISOR on LLaVA-1.5-7B across three critical alignment tasks: refusal, sycophancy and survival instinct. A single 150KB steering image matches steering vector performance within 1-2% for positive behavioral shifts while dramatically exceeding it for negative steering--achieving up to 25% shifts from baseline compared to steering vectors' modest changes. Unlike system prompting (3-4% shifts), VISOR provides robust bidirectional control while maintaining 99.9% performance on 14,000 unrelated MMLU tasks. Beyond eliminating runtime overhead and model access requirements, VISOR exposes a critical security vulnerability: adversaries can achieve sophisticated behavioral manipulation through visual channels alone, bypassing text-based defenses. Our work fundamentally re-imagines multimodal model control and highlights the urgent need for defenses against visual steering attacks.

