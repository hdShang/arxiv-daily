---
layout: default
title: Towards Visuospatial Cognition via Hierarchical Fusion of Visual Experts
---

# Towards Visuospatial Cognition via Hierarchical Fusion of Visual Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12363" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12363v4</a>
  <a href="https://arxiv.org/pdf/2505.12363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12363v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12363v4', 'Towards Visuospatial Cognition via Hierarchical Fusion of Visual Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Feng

**分类**: cs.CV, cs.AI, cs.CL, cs.LG, cs.RO

**发布日期**: 2025-05-18 (更新: 2025-09-09)

**备注**: 26 pages, 19 figures, 4 tables

---

## 💡 一句话要点

**提出ViCA2以解决视觉空间认知问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉空间认知` `多模态大型语言模型` `空间推理` `SigLIP` `Hiera` `数据集ViCA-322K` `令牌比例控制` `VSI-Bench`

## 📋 核心要点

1. 现有的多模态大型语言模型在视觉空间认知任务中表现不足，缺乏必要的架构和训练数据。
2. ViCA2通过双视觉编码器架构，结合SigLIP和Hiera，提升空间推理能力，并引入令牌比例控制机制以提高效率。
3. ViCA2-7B模型在VSI-Bench基准测试中取得56.8的平均分，显著优于其他大型模型，展示了其在视觉空间智能方面的优势。

## 📝 摘要（中文）

尽管多模态大型语言模型（MLLMs）在一般的视觉-语言任务中表现出色，但视觉空间认知——关于空间布局、关系和动态的推理——仍然是一个重大挑战。现有模型往往缺乏必要的架构组件和专门的训练数据以实现细粒度的空间理解。我们提出了ViCA2（视觉空间认知助手2），这是一种新型的MLLM，旨在增强空间推理能力。ViCA2采用双视觉编码器架构，集成了SigLIP用于语义理解和Hiera用于空间结构，同时配备了令牌比例控制机制以提高效率。我们还开发了ViCA-322K，这是一个新的大规模数据集，包含超过322,000个空间基础的问题-答案对，用于针对性指令调优。在具有挑战性的VSI-Bench基准上，我们的ViCA2-7B模型取得了56.8的最新平均分，显著超越了更大的开源模型（如LLaVA-NeXT-Video-72B，40.9）和领先的专有模型（Gemini-1.5 Pro，45.4）。这证明了我们的方法在实现强大的视觉空间智能方面的有效性。我们发布了ViCA2、其代码库和ViCA-322K数据集，以促进进一步研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉空间认知中的推理问题，现有方法在空间布局和关系理解上存在显著不足，缺乏专门的架构和训练数据。

**核心思路**：ViCA2的核心思路是通过双视觉编码器架构，分别处理语义和空间结构，从而增强模型的空间推理能力。此设计旨在弥补现有模型在细粒度空间理解上的不足。

**技术框架**：ViCA2的整体架构包括两个主要模块：SigLIP用于语义理解，Hiera用于空间结构的解析。此外，模型还引入了令牌比例控制机制，以提高处理效率和模型性能。

**关键创新**：ViCA2的主要创新在于其双视觉编码器架构的设计，结合了语义和空间结构的处理能力，这与现有方法的单一处理方式形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的参数设置和损失函数，以优化空间推理的效果。同时，令牌比例控制机制的引入，确保了模型在处理复杂任务时的高效性。

## 📊 实验亮点

ViCA2-7B模型在VSI-Bench基准测试中取得56.8的平均分，显著超越了LLaVA-NeXT-Video-72B（40.9）和Gemini-1.5 Pro（45.4），展示了其在视觉空间智能方面的卓越性能，证明了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、增强现实等，能够帮助机器更好地理解和推理空间信息，从而提升人机交互的智能化水平。未来，ViCA2有望在多模态学习和视觉理解领域产生深远影响。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at general vision-language tasks, visuospatial cognition - reasoning about spatial layouts, relations, and dynamics - remains a significant challenge. Existing models often lack the necessary architectural components and specialized training data for fine-grained spatial understanding. We introduce ViCA2 (Visuospatial Cognitive Assistant 2), a novel MLLM designed to enhance spatial reasoning. ViCA2 features a dual vision encoder architecture integrating SigLIP for semantics and Hiera for spatial structure, coupled with a token ratio control mechanism for efficiency. We also developed ViCA-322K, a new large-scale dataset with over 322,000 spatially grounded question-answer pairs for targeted instruction tuning. On the challenging VSI-Bench benchmark, our ViCA2-7B model achieves a state-of-the-art average score of 56.8, significantly surpassing larger open-source models (e.g., LLaVA-NeXT-Video-72B, 40.9) and leading proprietary models (Gemini-1.5 Pro, 45.4). This demonstrates the effectiveness of our approach in achieving strong visuospatial intelligence with a compact model. We release ViCA2, its codebase, and the ViCA-322K dataset to facilitate further research.

