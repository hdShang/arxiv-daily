---
layout: default
title: DynaSolidGeo: A Dynamic Benchmark for Genuine Spatial Mathematical Reasoning of VLMs in Solid Geometry
---

# DynaSolidGeo: A Dynamic Benchmark for Genuine Spatial Mathematical Reasoning of VLMs in Solid Geometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22340" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22340v2</a>
  <a href="https://arxiv.org/pdf/2510.22340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22340v2" onclick="toggleFavorite(this, '2510.22340v2', 'DynaSolidGeo: A Dynamic Benchmark for Genuine Spatial Mathematical Reasoning of VLMs in Solid Geometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changti Wu, Shijie Lian, Zihao Liu, Lei Zhang, Laurence Tianruo Yang, Kai Chen

**分类**: cs.AI, cs.CL, cs.CV, cs.LG

**发布日期**: 2025-10-25 (更新: 2025-11-11)

**备注**: The code and dataset are available at \href{https://zgca-ai4edu.github.io/DynaSolidGeo/}{DynaSolidGeo}

**🔗 代码/项目**: [PROJECT_PAGE](https://zgca-ai4edu.github.io/DynaSolidGeo/)

---

## 💡 一句话要点

**提出DynaSolidGeo以解决空间数学推理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间数学推理` `多模态学习` `动态基准` `视觉-语言模型` `固体几何` `推理链评估` `专家注释` `数据生成`

## 📋 核心要点

1. 现有的多模态数学推理基准主要集中在二维几何，缺乏对固体几何的有效评估，且容易受到数据污染和记忆化的影响。
2. DynaSolidGeo通过半自动注释管道构建，能够动态生成多样的文本-视觉实例，并引入推理链评估以衡量逻辑有效性。
3. 实验结果显示，现有VLMs在动态设置下性能显著下降，尤其是在需要高水平空间智能的任务上表现不佳。

## 📝 摘要（中文）

固体几何问题的解决需要结合空间智能和符号推理的空间数学推理能力。然而，现有的多模态数学推理基准主要集中在二维平面几何，依赖于静态数据集，容易导致数据污染和记忆化，同时仅通过最终答案评估模型，忽视推理过程。为了解决这些问题，本文提出了DynaSolidGeo，这是第一个动态基准，用于评估视觉-语言模型（VLMs）在固体几何中的真实空间推理能力。DynaSolidGeo通过半自动注释管道构建，包含503个专家策划的种子问题，能够动态生成无限多样的多模态文本-视觉实例。除了答案准确性外，我们还引入基于专家注释的推理链的过程评估，以测量逻辑有效性和因果一致性。实验表明，在动态设置下，模型性能显著下降，特别是在需要高水平空间智能的任务上表现不佳。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态数学推理基准在固体几何问题上的不足，特别是静态数据集导致的性能限制和推理过程缺失的问题。

**核心思路**：DynaSolidGeo的核心思路是通过半自动注释生成动态数据集，支持无限多样的文本-视觉实例生成，并引入推理链的评估方法，以全面评估模型的推理能力。

**技术框架**：DynaSolidGeo的整体架构包括数据生成模块、专家注释模块和评估模块。数据生成模块负责动态生成多模态实例，专家注释模块提供推理链的标注，评估模块则对模型的推理过程进行分析。

**关键创新**：DynaSolidGeo的关键创新在于其动态生成能力和推理链评估方法，这与现有静态数据集和单一答案评估方法形成鲜明对比，能够更真实地反映模型的推理能力。

**关键设计**：在设计中，采用了专家策划的种子问题，确保生成实例的多样性和复杂性，同时在评估中引入逻辑有效性和因果一致性的指标，以全面评估模型的推理过程。

## 📊 实验亮点

实验结果显示，现有的开源和闭源VLMs在DynaSolidGeo基准下表现出显著的性能差距，尤其在动态设置中性能严重下降。在需要高水平空间智能的任务（如心理旋转和可视化）上，模型的表现普遍较差，显示出该领域的研究潜力和挑战。

## 🎯 应用场景

DynaSolidGeo的研究成果可广泛应用于教育、机器人导航、计算机辅助设计等领域，帮助提升模型在复杂空间推理任务中的表现，推动相关技术的发展。未来，随着更多动态数据集的出现，可能会进一步促进多模态学习和推理能力的提升。

## 📄 摘要（原文）

> Solid geometry problem solving demands spatial mathematical reasoning that integrates spatial intelligence and symbolic reasoning. However, most existing multimodal mathematical reasoning benchmarks focus primarily on 2D plane geometry, rely on static datasets prone to data contamination and memorization, and evaluate models solely by final answers, overlooking the reasoning process. To address these limitations, we introduce DynaSolidGeo, the first dynamic benchmark for evaluating genuine spatial reasoning in Vision-Language Models (VLMs). Constructed through a semi-automatic annotation pipeline, DynaSolidGeo contains 503 expert-curated seed questions that can, in principle, dynamically generate an unbounded number of diverse multimodal text-visual instances. Beyond answer accuracy, we incorporate process evaluation based on expert-annotated reasoning chains to measure logical validity and causal coherence. Experiments across representative open-source and closed-source VLMs reveal large performance gaps, severe degradation in dynamic settings, and poor performance on tasks requiring high-level spatial intelligence, such as mental rotation and visualization. The code and dataset are available at \href{https://zgca-ai4edu.github.io/DynaSolidGeo/}{DynaSolidGeo}.

