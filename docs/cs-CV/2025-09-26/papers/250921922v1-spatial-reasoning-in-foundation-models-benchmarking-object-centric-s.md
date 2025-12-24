---
layout: default
title: "Spatial Reasoning in Foundation Models: Benchmarking Object-Centric Spatial Understanding"
---

# Spatial Reasoning in Foundation Models: Benchmarking Object-Centric Spatial Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21922" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21922v1</a>
  <a href="https://arxiv.org/pdf/2509.21922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21922v1', 'Spatial Reasoning in Foundation Models: Benchmarking Object-Centric Spatial Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vahid Mirjalili, Ramin Giahi, Sriram Kollipara, Akshay Kekuda, Kehui Yao, Kai Zhao, Jianpeng Xu, Kaushiki Nag, Sinduja Subramaniam, Topojoy Biswas, Evren Korpeoglu, Kannan Achan

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: 4 pages, NeurIPS Workshop SpaVLE

---

## 💡 一句话要点

**提出系统基准以解决视觉模型空间理解不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间理解` `视觉模型` `基准测试` `物体推理` `视觉语言模型` `深度学习` `合成数据集`

## 📋 核心要点

1. 现有的视觉模型在空间理解方面存在不足，尤其是在物体关系和相对位置的推理上。
2. 本文提出了一个系统的基准，专注于物体中心的空间推理能力，利用合成数据集进行评估。
3. 实验结果显示，检测器在定位精度上表现优异，但在空间推理上存在局限，强调了对空间感知模型的需求。

## 📝 摘要（中文）

空间理解是视觉基础模型的重要能力。尽管近年来大型视觉模型和视觉语言模型的识别能力有所提升，但大多数基准测试强调定位精度，而忽视了模型是否能够捕捉场景中物体的排列和关系。有效的场景理解不仅需要识别物体，还需要推理它们的相对位置、分组和深度。本文提出了一个系统的基准，用于评估基础模型的物体中心空间推理能力。通过使用受控的合成数据集，我们评估了多种最先进的视觉模型和大型视觉语言模型在空间定位、空间推理和下游检索任务中的表现。研究发现，检测器如GroundingDINO和OWLv2提供了精确的边界框，但在关系推理方面有限，而像SmolVLM和GPT-4o这样的视觉语言模型则提供了粗略的布局线索和流畅的描述，但在细粒度空间上下文方面表现不佳。我们的研究突显了定位与真实空间理解之间的差距，并指向了社区对空间感知基础模型的需求。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉模型在空间理解方面的不足，特别是物体之间关系的推理能力不足。现有方法多集中于定位精度，忽视了物体的相对位置和深度关系。

**核心思路**：论文通过建立一个系统的基准来评估基础模型的空间推理能力，强调物体中心的空间关系，而不仅仅是物体的识别。

**技术框架**：研究使用了一个受控的合成数据集，评估了多种最先进的视觉模型和视觉语言模型，任务包括空间定位、空间推理和下游检索。

**关键创新**：最重要的创新在于提出了一个系统的基准，填补了现有方法在空间理解方面的空白，强调了空间推理在视觉任务中的重要性。

**关键设计**：在实验中，使用了多种模型进行对比，设置了不同的任务和评估指标，以全面评估模型在空间理解方面的能力。

## 📊 实验亮点

实验结果表明，GroundingDINO和OWLv2在空间定位任务中表现优异，提供了高精度的边界框，但在空间推理方面表现有限。相比之下，SmolVLM和GPT-4o在生成流畅描述方面表现良好，但在细粒度空间上下文的理解上存在困难。这些发现强调了空间理解能力的提升需求。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航、增强现实等需要深度空间理解的场景。通过提升模型的空间推理能力，可以显著改善这些领域的智能系统表现，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Spatial understanding is a critical capability for vision foundation models. While recent advances in large vision models or vision-language models (VLMs) have expanded recognition capabilities, most benchmarks emphasize localization accuracy rather than whether models capture how objects are arranged and related within a scene. This gap is consequential; effective scene understanding requires not only identifying objects, but reasoning about their relative positions, groupings, and depth. In this paper, we present a systematic benchmark for object-centric spatial reasoning in foundation models. Using a controlled synthetic dataset, we evaluate state-of-the-art vision models (e.g., GroundingDINO, Florence-2, OWLv2) and large VLMs (e.g., InternVL, LLaVA, GPT-4o) across three tasks: spatial localization, spatial reasoning, and downstream retrieval tasks. We find a stable trade-off: detectors such as GroundingDINO and OWLv2 deliver precise boxes with limited relational reasoning, while VLMs like SmolVLM and GPT-4o provide coarse layout cues and fluent captions but struggle with fine-grained spatial context. Our study highlights the gap between localization and true spatial understanding, and pointing toward the need for spatially-aware foundation models in the community.

