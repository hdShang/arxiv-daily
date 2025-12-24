---
layout: default
title: "VLM-SlideEval: Evaluating VLMs on Structured Comprehension and Perturbation Sensitivity in PPT"
---

# VLM-SlideEval: Evaluating VLMs on Structured Comprehension and Perturbation Sensitivity in PPT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22045" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22045v1</a>
  <a href="https://arxiv.org/pdf/2510.22045.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22045v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22045v1', 'VLM-SlideEval: Evaluating VLMs on Structured Comprehension and Perturbation Sensitivity in PPT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyeonsu Kang, Emily Bao, Anjan Goswami

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-24

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Evaluating the Evolving LLM Lifecycle - Benchmarks, Emergent Abilities, and Scaling

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/Forceless)

---

## 💡 一句话要点

**VLM-SlideEval：评估VLM在PPT结构化理解和扰动敏感性上的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `幻灯片理解` `结构化文档` `扰动鲁棒性` `叙事结构` `评估框架`

## 📋 核心要点

1. 现有视觉语言模型在幻灯片理解方面存在不足，尤其是在元素提取、抗扰动性和叙事结构理解上。
2. VLM-SlideEval框架通过元素提取、扰动测试和叙事恢复三个维度，全面评估VLM的幻灯片理解能力。
3. 实验表明，VLM在精确元素提取和跨幻灯片叙事理解方面表现不佳，需进一步优化以提升幻灯片评估能力。

## 📝 摘要（中文）

视觉语言模型（VLM）越来越多地被用于评估多模态内容，包括演示文稿幻灯片，但它们对幻灯片特定内容的理解仍未得到充分探索。我们提出了VLM-SlideEval，一个评估框架，从三个维度探测VLM：（1）从幻灯片图像中提取元素级别的信息，并与真实标签对齐；（2）对几何、风格和文本中的受控扰动的鲁棒性；（3）更高层次的理解，例如从打乱的幻灯片中恢复演示文稿的叙述顺序。我们使用来自Zenodo的公开演示文稿，将PowerPoint XML和实时渲染中的真实元素元数据标准化为一个统一的可验证模式。实验结果表明，VLM在像素精确的提取方面表现不佳，在受控扰动下表现出不显著的一致性、保真度和一致性，但在单张幻灯片内容理解方面表现较好；然而，它们无法可靠地捕捉跨幻灯片的叙述结构。这些结果突出了当前VLM在幻灯片评估方面的局限性，并促使我们开发校准的、循环评估器，以驱动智能体管道中的迭代改进和选择。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在理解演示文稿幻灯片方面存在局限性，尤其是在元素级别的精确提取、对各种扰动的鲁棒性以及对幻灯片叙事结构的理解上。现有的评估方法缺乏针对幻灯片特定结构的细粒度分析，无法充分揭示VLM在处理此类任务时的不足。

**核心思路**：VLM-SlideEval的核心思路是构建一个全面的评估框架，该框架能够系统地测试VLM在幻灯片理解的各个方面。通过设计针对性的任务，例如元素提取、扰动测试和叙事恢复，可以更深入地了解VLM的优势和劣势，从而为未来的模型改进提供指导。

**技术框架**：VLM-SlideEval框架包含以下几个主要模块：1) 数据集构建：使用Zenodo的公开演示文稿数据集，并从PowerPoint XML和实时渲染中提取元素元数据，标准化为统一的可验证模式。2) 元素提取评估：评估VLM从幻灯片图像中提取元素级别信息（如文本、图像、形状）的准确性，并与真实标签进行比较。3) 扰动测试：通过引入几何、风格和文本上的受控扰动，评估VLM对幻灯片变化的鲁棒性。4) 叙事恢复评估：评估VLM从打乱的幻灯片中恢复演示文稿叙述顺序的能力。

**关键创新**：VLM-SlideEval的关键创新在于其针对幻灯片理解的全面评估体系。它不仅关注单张幻灯片的内容理解，还关注VLM对幻灯片之间关系的理解，例如叙事结构。此外，通过引入受控扰动，可以更深入地了解VLM对幻灯片变化的敏感性。与现有方法相比，VLM-SlideEval提供了一种更细粒度、更全面的VLM评估方法。

**关键设计**：在数据集构建方面，论文标准化了PowerPoint XML和实时渲染中的元素元数据，确保了评估的准确性和可验证性。在扰动测试方面，论文设计了多种类型的扰动，包括几何扰动（如旋转、缩放）、风格扰动（如颜色变化、字体变化）和文本扰动（如拼写错误、同义词替换）。在叙事恢复评估方面，论文使用排序指标来评估VLM恢复幻灯片顺序的准确性。具体的参数设置、损失函数和网络结构取决于所使用的VLM模型，论文主要关注评估框架的设计和实验结果的分析。

## 📊 实验亮点

实验结果表明，VLM在像素精确的元素提取方面表现不佳，在受控扰动下的一致性、保真度和一致性表现不佳，但在单张幻灯片内容理解方面表现较好。然而，VLM无法可靠地捕捉跨幻灯片的叙述结构。这些结果揭示了当前VLM在幻灯片理解方面的局限性，为未来的模型改进提供了方向。

## 🎯 应用场景

VLM-SlideEval的研究成果可应用于智能演示文稿生成、自动幻灯片评估与优化、教育内容创作等领域。通过更准确地理解幻灯片内容和结构，VLM可以辅助用户快速创建高质量的演示文稿，并自动评估幻灯片的质量，从而提高演示效果和沟通效率。未来，该研究可进一步扩展到其他类型的结构化文档理解任务。

## 📄 摘要（原文）

> Vision-language models (VLMs) are increasingly used to evaluate multimodal content, including presentation slides, yet their slide-specific understanding remains underexplored {despite their growing role as critics in agentic, model-forward pipelines}. We introduce VLM-SlideEval, an evaluation framework that probes VLMs along three axes: (1) element-level extraction from slide images aligned to ground truth; (2) robustness to controlled perturbations in geometry, style, and text; and (3) higher-level comprehension, such as recovering a deck's narrative order from shuffled slides. Using publicly available decks from Zenodo (https://huggingface.co/datasets/Forceless/Zenodo10K/viewer/default/pptx), we standardize ground-truth element metadata from PowerPoint XML and live renderings into a unified, verifiable schema. Empirically, VLMs underperform on pixel-accurate extraction and show non-trivial agreement, fidelity, and consistency under controlled perturbations, while performing better on single-slide content understanding; however, they do not reliably capture narrative structure across slides. These results highlight the limits of current VLMs for slide evaluation and motivate calibrated, critic-in-the-loop evaluators that drive iterative refinement and selection in agentic pipelines.

