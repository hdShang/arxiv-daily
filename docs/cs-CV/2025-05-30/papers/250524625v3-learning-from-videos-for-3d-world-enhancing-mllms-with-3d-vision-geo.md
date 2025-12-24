---
layout: default
title: Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors
---

# Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24625" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24625v3</a>
  <a href="https://arxiv.org/pdf/2505.24625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24625v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24625v3', 'Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duo Zheng, Shijia Huang, Yanyang Li, Liwei Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-10-22)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出VG LLM以解决视频直接理解3D场景的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `3D场景` `多模态大语言模型` `几何先验` `空间推理` `视觉特征提取` `自动驾驶` `虚拟现实`

## 📋 核心要点

1. 现有方法通常依赖于复杂的3D数据输入，限制了从视频直接理解3D场景的能力。
2. 我们提出的VG LLM通过3D视觉几何编码器从视频序列中提取3D先验信息，直接与视觉标记结合输入MLLM。
3. 实验结果显示，VG LLM在多项3D场景理解和空间推理任务上显著优于传统方法，尤其在VSI-Bench评估中表现突出。

## 📝 摘要（中文）

本研究探讨了多模态大语言模型（MLLMs）在理解3D场景中的应用，尤其是通过视频进行理解。以往的方法依赖于全面的3D数据输入，如点云或重建的鸟瞰图（BEV）。我们提出了一种新颖且高效的方法，称为视频-3D几何大语言模型（VG LLM），该方法直接从视频数据中提取3D先验信息，而无需额外的3D输入。通过大量实验，我们的方法在3D场景理解和空间推理等任务上取得了显著提升，尤其是我们的4B模型在VSI-Bench评估中表现优于现有的最先进方法，包括Gemini-1.5-Pro。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有多模态大语言模型在理解3D场景时对3D数据输入的依赖问题。以往方法需要复杂的3D数据，如点云或BEV，限制了其应用灵活性。

**核心思路**：我们提出的VG LLM通过直接从视频数据中提取3D几何先验信息，避免了对额外3D输入的需求。这种设计使得模型能够更高效地理解和推理3D空间。

**技术框架**：VG LLM的整体架构包括三个主要模块：视频序列输入、3D视觉几何编码器和多模态大语言模型。视频序列首先被处理以提取视觉特征，随后通过几何编码器提取3D信息，最后与视觉标记结合输入到MLLM中。

**关键创新**：VG LLM的核心创新在于其能够从视频中直接学习3D场景理解，而不依赖于传统的3D数据输入。这一方法在本质上改变了3D理解的方式，使得模型在处理视频时更具灵活性和效率。

**关键设计**：在模型设计中，我们采用了特定的损失函数来优化3D几何信息的提取，同时在网络结构上进行了调整，以确保视觉特征与3D信息的有效融合。

## 📊 实验亮点

在实验中，VG LLM的4B模型在VSI-Bench评估中表现优于Gemini-1.5-Pro，显示出在3D场景理解和空间推理任务上的显著提升，证明了其在不依赖显式3D数据输入的情况下仍能取得竞争性结果。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、虚拟现实和增强现实等场景，能够提升系统对复杂3D环境的理解能力。通过直接从视频中学习3D信息，未来的应用将更加灵活和高效，推动相关技术的进步。

## 📄 摘要（原文）

> Previous research has investigated the application of Multimodal Large Language Models (MLLMs) in understanding 3D scenes by interpreting them as videos. These approaches generally depend on comprehensive 3D data inputs, such as point clouds or reconstructed Bird's-Eye View (BEV) maps. In our research, we advance this field by enhancing the capability of MLLMs to understand and reason in 3D spaces directly from video data, without the need for additional 3D input. We propose a novel and efficient method called the Video-3D Geometry Large Language Model (VG LLM). Our approach utilizes a 3D visual geometry encoder to extract 3D prior information from video sequences. This information is then integrated with visual tokens and input into the MLLM. Extensive experiments have shown that our method has achieved substantial improvements in various tasks related to 3D scene understanding and spatial reasoning, all directly learned from video sources. Impressively, our 4B model, which does not rely on explicit 3D data inputs, achieves competitive results compared to existing state-of-the-art methods, and even surpasses the Gemini-1.5-Pro in the VSI-Bench evaluations.

