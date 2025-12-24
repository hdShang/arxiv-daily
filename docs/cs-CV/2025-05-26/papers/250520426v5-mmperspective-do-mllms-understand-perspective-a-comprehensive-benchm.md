---
layout: default
title: MMPerspective: Do MLLMs Understand Perspective? A Comprehensive Benchmark for Perspective Perception, Reasoning, and Robustness
---

# MMPerspective: Do MLLMs Understand Perspective? A Comprehensive Benchmark for Perspective Perception, Reasoning, and Robustness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20426" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20426v5</a>
  <a href="https://arxiv.org/pdf/2505.20426.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20426v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20426v5', 'MMPerspective: Do MLLMs Understand Perspective? A Comprehensive Benchmark for Perspective Perception, Reasoning, and Robustness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yolo Y. Tang, Pinxin Liu, Zhangyun Tan, Mingqian Feng, Rui Mao, Chao Huang, Jing Bi, Yunzhong Xiao, Susan Liang, Hang Hua, Ali Vosoughi, Luchuan Song, Zeliang Zhang, Chenliang Xu

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-11-25)

**备注**: Accepted to NeurIPS 2025 DB Track. Rating: 5,5,5,5

**🔗 代码/项目**: [PROJECT_PAGE](https://yunlong10.github.io/MMPerspective/)

---

## 💡 一句话要点

**提出MMPerspective以评估多模态大语言模型的视角理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视角理解` `空间推理` `鲁棒性评估` `计算机视觉`

## 📋 核心要点

1. 现有多模态大语言模型在理解视角几何方面存在显著不足，尤其是在组合推理和空间一致性方面。
2. MMPerspective基准通过10个任务系统评估MLLMs的视角理解，涵盖感知、推理和鲁棒性三个维度。
3. 对43个MLLMs的评估显示，尽管在表面任务上表现良好，但在复杂推理和扰动下的表现仍有待提升。

## 📝 摘要（中文）

理解视角是人类视觉感知的基础，但多模态大语言模型（MLLMs）在视角几何方面的理解程度尚不明确。我们引入了MMPerspective，这是第一个专门设计的基准，系统评估MLLMs对视角的理解，涵盖10个精心设计的任务，涉及视角感知、推理和鲁棒性三个维度。基准包含2,711个真实和合成图像实例及5,083个问答对，探讨了消失点感知、视角类型推理、3D空间中的线关系理解等关键能力。通过对43个最先进的MLLMs的全面评估，我们发现模型在表面感知任务上表现良好，但在组合推理和扰动下保持空间一致性方面存在显著局限性。我们的分析揭示了模型架构、规模与视角能力之间的有趣模式，突显了鲁棒性瓶颈和链式思维提示的优势。MMPerspective为诊断和推动视觉-语言系统的空间理解提供了宝贵的测试平台。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型在视角理解方面的不足，尤其是它们在组合推理和空间一致性方面的挑战。现有方法未能系统评估这些模型的视角能力。

**核心思路**：通过引入MMPerspective基准，论文设计了10个任务，涵盖视角感知、推理和鲁棒性，以全面评估MLLMs的视角理解能力。这样的设计能够更好地揭示模型的潜在局限性。

**技术框架**：MMPerspective基准包括2,711个图像实例和5,083个问答对，任务分为三个主要模块：视角感知、推理和鲁棒性评估。每个模块针对特定能力进行设计，以确保全面性和系统性。

**关键创新**：MMPerspective是第一个专门针对MLLMs视角理解的基准，提供了系统的评估框架，揭示了模型在不同任务上的表现差异，尤其是在复杂推理方面的局限性。

**关键设计**：在设计中，任务包括消失点感知、视角类型推理和3D空间线关系理解等，采用了多样化的图像实例和问答对，以确保评估的全面性和有效性。

## 📊 实验亮点

实验结果显示，43个MLLMs在表面感知任务上表现良好，但在组合推理和扰动下的空间一致性方面存在显著不足。具体而言，模型在复杂任务中的表现提升幅度有限，揭示了鲁棒性瓶颈和链式思维提示的潜在优势。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人导航和增强现实等。通过提升多模态大语言模型的视角理解能力，可以增强这些系统在复杂环境中的表现，推动智能系统的实际应用和发展。

## 📄 摘要（原文）

> Understanding perspective is fundamental to human visual perception, yet the extent to which multimodal large language models (MLLMs) internalize perspective geometry remains unclear. We introduce MMPerspective, the first benchmark specifically designed to systematically evaluate MLLMs' understanding of perspective through 10 carefully crafted tasks across three complementary dimensions: Perspective Perception, Reasoning, and Robustness. Our benchmark comprises 2,711 real-world and synthetic image instances with 5,083 question-answer pairs that probe key capabilities, such as vanishing point perception and counting, perspective type reasoning, line relationship understanding in 3D space, invariance to perspective-preserving transformations, etc. Through a comprehensive evaluation of 43 state-of-the-art MLLMs, we uncover significant limitations: while models demonstrate competence on surface-level perceptual tasks, they struggle with compositional reasoning and maintaining spatial consistency under perturbations. Our analysis further reveals intriguing patterns between model architecture, scale, and perspective capabilities, highlighting both robustness bottlenecks and the benefits of chain-of-thought prompting. MMPerspective establishes a valuable testbed for diagnosing and advancing spatial understanding in vision-language systems. Resources available at: https://yunlong10.github.io/MMPerspective/

