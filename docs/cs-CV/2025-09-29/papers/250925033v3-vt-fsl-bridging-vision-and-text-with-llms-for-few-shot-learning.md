---
layout: default
title: "VT-FSL: Bridging Vision and Text with LLMs for Few-Shot Learning"
---

# VT-FSL: Bridging Vision and Text with LLMs for Few-Shot Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25033" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25033v3</a>
  <a href="https://arxiv.org/pdf/2509.25033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25033v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25033v3', 'VT-FSL: Bridging Vision and Text with LLMs for Few-Shot Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhao Li, Qiangchang Wang, Xianjing Meng, Zhibin Wu, Yilong Yin

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-29 (更新: 2025-10-23)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/peacelwh/VT-FSL)

---

## 💡 一句话要点

**提出VT-FSL框架，利用LLM桥接视觉与文本，提升小样本学习性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小样本学习` `大型语言模型` `跨模态学习` `视觉文本融合` `几何对齐` `迭代提示` `图像合成`

## 📋 核心要点

1. 现有小样本学习方法依赖语义信息增强支持特征，但易产生与视觉证据矛盾的语义幻觉，导致噪声指导和高昂的修正成本。
2. VT-FSL框架利用LLM生成精确的类描述和合成图像，分别作为文本和视觉提示，弥补有限支持数据带来的不足。
3. 通过跨模态几何对齐，VT-FSL框架能够捕获全局和非线性关系，实现结构化和一致的多模态信息融合，显著提升性能。

## 📝 摘要（中文）

本文提出了一种新颖的框架，即利用LLM桥接视觉与文本的小样本学习（VT-FSL）。该框架构建了基于大型语言模型（LLM）和支持图像的精确跨模态提示，并通过几何感知对齐无缝集成它们。VT-FSL主要由跨模态迭代提示（CIP）和跨模态几何对齐（CGA）组成。具体而言，CIP以类名和支持图像为条件，使LLM在单个结构化推理过程中迭代生成精确的类描述。这些描述不仅丰富了对新类的语义理解，还实现了语义一致图像的零样本合成。描述和合成图像分别作为互补的文本和视觉提示，提供高层次的类语义和低层次的类内多样性，以弥补有限的支持数据。此外，CGA通过最小化它们所跨越的三维平行多面体的核化体积，联合对齐融合的文本、支持和合成视觉表示。它捕获所有表示之间的全局和非线性关系，从而实现结构化和一致的多模态集成。所提出的VT-FSL方法在包括标准、跨域和细粒度小样本学习场景在内的十个不同的基准测试中，建立了新的最先进的性能。

## 🔬 方法详解

**问题定义**：现有小样本学习方法在利用语义信息增强支持特征时，容易产生与实际视觉证据相悖的语义幻觉，从而导致噪声指导，需要付出高昂的修正成本。这些方法缺乏对实际实例的有效 grounding，难以准确捕捉新类别的本质特征。

**核心思路**：VT-FSL的核心思路是利用大型语言模型（LLM）的强大语义理解和生成能力，生成更精确的类描述和合成图像，从而弥补小样本学习中支持数据不足的问题。通过将视觉信息和文本信息有效结合，提供更全面和准确的类别信息，提升模型的泛化能力。

**技术框架**：VT-FSL框架主要包含两个核心模块：跨模态迭代提示（CIP）和跨模态几何对齐（CGA）。CIP模块首先利用LLM，以类名和支持图像为条件，迭代生成精确的类描述和合成图像。这些描述和图像分别作为文本和视觉提示，提供高层次的类语义和低层次的类内多样性。CGA模块则负责将融合的文本、支持图像和合成图像表示进行对齐，通过最小化它们所跨越的三维平行多面体的核化体积，实现结构化和一致的多模态集成。

**关键创新**：VT-FSL的关键创新在于利用LLM进行跨模态迭代提示，生成高质量的文本描述和合成图像，从而有效增强了小样本学习中的类别表示。与现有方法相比，VT-FSL能够更好地利用LLM的语义理解能力，生成更精确和一致的类别信息，避免了语义幻觉问题。此外，CGA模块通过几何对齐的方式，实现了多模态信息的有效融合，进一步提升了模型的性能。

**关键设计**：CIP模块的关键设计在于迭代提示策略，通过多轮迭代，逐步完善类描述和合成图像的质量。CGA模块的关键设计在于利用核化体积最小化来实现多模态对齐，这种方法能够捕获全局和非线性关系，从而实现更有效的多模态融合。具体的损失函数设计和网络结构细节在论文中有详细描述，但摘要中未明确提及具体参数设置。

## 📊 实验亮点

VT-FSL方法在十个不同的基准测试中取得了最先进的性能，包括标准、跨域和细粒度小样本学习场景。具体性能数据和对比基线在论文中详细给出，但摘要中未提供具体数值。代码已开源，方便研究者复现和进一步研究。

## 🎯 应用场景

VT-FSL框架具有广泛的应用前景，可应用于图像识别、目标检测、图像分类等领域，尤其适用于数据稀缺的场景。例如，在医疗影像分析中，罕见疾病的病例数据通常非常有限，VT-FSL可以帮助医生更准确地诊断这些疾病。此外，该框架还可以应用于新产品识别、野生动物保护等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Few-shot learning (FSL) aims to recognize novel concepts from only a few labeled support samples. Recent studies enhance support features by incorporating additional semantic information or designing complex semantic fusion modules. However, they still suffer from hallucinating semantics that contradict the visual evidence due to the lack of grounding in actual instances, resulting in noisy guidance and costly corrections. To address these issues, we propose a novel framework, bridging Vision and Text with LLMs for Few-Shot Learning (VT-FSL), which constructs precise cross-modal prompts conditioned on Large Language Models (LLMs) and support images, seamlessly integrating them through a geometry-aware alignment. It mainly consists of Cross-modal Iterative Prompting (CIP) and Cross-modal Geometric Alignment (CGA). Specifically, the CIP conditions an LLM on both class names and support images to generate precise class descriptions iteratively in a single structured reasoning pass. These descriptions not only enrich the semantic understanding of novel classes but also enable the zero-shot synthesis of semantically consistent images. The descriptions and synthetic images act respectively as complementary textual and visual prompts, providing high-level class semantics and low-level intra-class diversity to compensate for limited support data. Furthermore, the CGA jointly aligns the fused textual, support, and synthetic visual representations by minimizing the kernelized volume of the 3-dimensional parallelotope they span. It captures global and nonlinear relationships among all representations, enabling structured and consistent multimodal integration. The proposed VT-FSL method establishes new state-of-the-art performance across ten diverse benchmarks, including standard, cross-domain, and fine-grained few-shot learning scenarios. Code is available at https://github.com/peacelwh/VT-FSL.

