---
layout: default
title: "Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models"
---

# Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00373" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00373v1</a>
  <a href="https://arxiv.org/pdf/2509.00373.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00373v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00373v1', 'Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sihao Wu, Gaojie Jin, Wei Huang, Jianhong Wang, Xiaowei Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出SPO-VLM以解决视觉语言模型的对抗攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `对抗攻击` `激活引导` `偏好优化` `模型鲁棒性` `多模态学习` `文本生成`

## 📋 核心要点

1. 现有的视觉语言模型在对抗攻击下表现脆弱，且依赖特定任务的对比提示导致性能下降。
2. 提出的SPO-VLM框架通过两阶段流程结合激活引导和偏好优化，提升模型的鲁棒性。
3. 实验结果表明，SPO-VLM在对抗攻击防御上显著增强，同时在无害任务中保持强劲的视觉理解能力。

## 📝 摘要（中文）

视觉语言模型（VLM）在整合视觉和文本信息方面展现出卓越的能力，但仍然对对抗攻击高度脆弱。尽管激活引导作为一种有前景的防御手段出现，现有方法往往依赖于特定任务的对比提示来提取有害方向，导致性能不佳并可能降低视觉定位性能。为了解决这些局限性，本文提出了序列级偏好优化（SPO-VLM），一个结合激活级干预与策略级优化的两阶段防御框架，以增强模型的鲁棒性。通过广泛的实验，SPO-VLM在攻击防御方面表现出色，同时在无害任务上保持强劲性能。我们将发布代码、模型权重和评估工具包，以支持可重复性和未来研究。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在对抗攻击下的脆弱性，现有方法依赖特定任务的对比提示，导致性能不佳和视觉定位能力下降。

**核心思路**：SPO-VLM框架通过两阶段的防御机制，第一阶段计算自适应层级引导向量，第二阶段通过序列级偏好优化来精炼这些向量，从而增强模型的鲁棒性。

**技术框架**：SPO-VLM包括两个主要阶段：第一阶段是从多样化数据源计算层级特定的引导向量，以抑制有害行为；第二阶段则通过自动化的毒性评估和基于图像-文本对齐的视觉一致性奖励来优化这些引导向量。

**关键创新**：SPO-VLM的创新在于结合了激活级干预与策略级优化，解决了现有方法在特定任务依赖性和性能下降的问题。

**关键设计**：在第一阶段，采用多样化数据源计算引导向量；在第二阶段，设计了自动化毒性评估机制和视觉一致性奖励，以确保生成文本的安全性和语义一致性。

## 📊 实验亮点

实验结果显示，SPO-VLM在对抗攻击防御方面表现优异，相较于基线方法，安全性提升显著，同时在无害任务上保持强劲的性能，确保视觉理解能力不受损害。

## 🎯 应用场景

该研究的潜在应用领域包括安全的文本生成、对抗性内容过滤以及多模态系统的安全性提升。通过增强视觉语言模型的鲁棒性，SPO-VLM可在社交媒体、在线内容审核和自动化客服等场景中发挥重要作用，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> Vision Language Models (VLMs) have demonstrated impressive capabilities in integrating visual and textual information for understanding and reasoning, but remain highly vulnerable to adversarial attacks. While activation steering has emerged as a promising defence, existing approaches often rely on task-specific contrastive prompts to extract harmful directions, which exhibit suboptimal performance and can degrade visual grounding performance. To address these limitations, we propose \textit{Sequence-Level Preference Optimization} for VLM (\textit{SPO-VLM}), a novel two-stage defense framework that combines activation-level intervention with policy-level optimization to enhance model robustness. In \textit{Stage I}, we compute adaptive layer-specific steering vectors from diverse data sources, enabling generalized suppression of harmful behaviors during inference. In \textit{Stage II}, we refine these steering vectors through a sequence-level preference optimization process. This stage integrates automated toxicity assessment, as well as visual-consistency rewards based on caption-image alignment, to achieve safe and semantically grounded text generation. The two-stage structure of SPO-VLM balances efficiency and effectiveness by combining a lightweight mitigation foundation in Stage I with deeper policy refinement in Stage II. Extensive experiments shown SPO-VLM enhances safety against attacks via activation steering and preference optimization, while maintaining strong performance on benign tasks without compromising visual understanding capabilities. We will release our code, model weights, and evaluation toolkit to support reproducibility and future research. \textcolor{red}{Warning: This paper may contain examples of offensive or harmful text and images.}

