---
layout: default
title: "SPAZER: Spatial-Semantic Progressive Reasoning Agent for Zero-shot 3D Visual Grounding"
---

# SPAZER: Spatial-Semantic Progressive Reasoning Agent for Zero-shot 3D Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21924" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21924v1</a>
  <a href="https://arxiv.org/pdf/2506.21924.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21924v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21924v1', 'SPAZER: Spatial-Semantic Progressive Reasoning Agent for Zero-shot 3D Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhao Jin, Rong-Cheng Tu, Jingyi Liao, Wenhao Sun, Xiao Luo, Shunyu Liu, Dacheng Tao

**分类**: cs.CV

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出SPAZER以解决零-shot 3D视觉定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `零-shot学习` `多模态推理` `空间理解` `语义理解` `进阶推理` `视觉语言模型` `深度学习`

## 📋 核心要点

1. 现有的零-shot 3D视觉定位方法往往只关注空间或语义理解，导致在复杂场景中的效果不佳。
2. SPAZER通过结合空间和语义推理，采用进阶推理框架，首先进行全局场景分析并生成3D渲染。
3. 在ScanRefer和Nr3D基准测试中，SPAZER的准确率分别提升了9.0%和10.9%，显著优于之前的最先进方法。

## 📝 摘要（中文）

3D视觉定位（3DVG）旨在根据自然语言查询在3D场景中定位目标对象。为减少对昂贵3D训练数据的依赖，近期研究探索了通过预训练的语言模型和视觉语言模型实现零-shot 3DVG。然而，现有方法往往侧重于空间或语义理解，限制了其在复杂现实应用中的有效性。本文提出SPAZER，一个结合空间和语义理解的进阶推理框架，能够在未使用3D标注数据的情况下实现稳健的零-shot定位。实验结果表明，SPAZER在ScanRefer和Nr3D基准测试中显著超越了现有的零-shot方法，准确率提升分别达到9.0%和10.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决零-shot 3D视觉定位中的空间与语义理解不足的问题。现有方法往往在复杂场景中表现不佳，无法有效结合3D和2D信息。

**核心思路**：SPAZER通过结合空间和语义推理，采用进阶推理框架，首先进行全局场景分析并生成3D渲染，以实现更准确的目标定位。

**技术框架**：SPAZER的整体架构包括三个主要模块：全局场景分析、锚点引导候选筛选和3D-2D联合决策。首先，系统从最佳视角生成3D渲染，然后进行粗略定位，最后结合相关的2D图像进行精确匹配。

**关键创新**：SPAZER的创新在于其能够无缝结合空间和语义推理，形成一个统一的推理框架，克服了现有方法的局限性。

**关键设计**：在设计中，SPAZER使用了锚点引导的候选筛选机制，并通过检索相关的2D图像进行3D-2D联合决策，确保了高效的目标匹配。

## 📊 实验亮点

SPAZER在ScanRefer和Nr3D基准测试中表现出色，准确率分别提升了9.0%和10.9%，显著超越了现有的零-shot方法，展示了其在复杂场景中的有效性和鲁棒性。

## 🎯 应用场景

SPAZER的研究成果在智能机器人、增强现实和自动驾驶等领域具有广泛的应用潜力。通过实现高效的3D视觉定位，SPAZER能够提升机器对复杂环境的理解能力，推动相关技术的进步与应用落地。

## 📄 摘要（原文）

> 3D Visual Grounding (3DVG) aims to localize target objects within a 3D scene based on natural language queries. To alleviate the reliance on costly 3D training data, recent studies have explored zero-shot 3DVG by leveraging the extensive knowledge and powerful reasoning capabilities of pre-trained LLMs and VLMs. However, existing paradigms tend to emphasize either spatial (3D-based) or semantic (2D-based) understanding, limiting their effectiveness in complex real-world applications. In this work, we introduce SPAZER - a VLM-driven agent that combines both modalities in a progressive reasoning framework. It first holistically analyzes the scene and produces a 3D rendering from the optimal viewpoint. Based on this, anchor-guided candidate screening is conducted to perform a coarse-level localization of potential objects. Furthermore, leveraging retrieved relevant 2D camera images, 3D-2D joint decision-making is efficiently performed to determine the best-matching object. By bridging spatial and semantic reasoning neural streams, SPAZER achieves robust zero-shot grounding without training on 3D-labeled data. Extensive experiments on ScanRefer and Nr3D benchmarks demonstrate that SPAZER significantly outperforms previous state-of-the-art zero-shot methods, achieving notable gains of 9.0% and 10.9% in accuracy.

