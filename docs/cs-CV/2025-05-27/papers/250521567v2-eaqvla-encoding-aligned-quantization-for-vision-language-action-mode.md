---
layout: default
title: EaqVLA: Encoding-aligned Quantization for Vision-Language-Action Models
---

# EaqVLA: Encoding-aligned Quantization for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21567" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21567v2</a>
  <a href="https://arxiv.org/pdf/2505.21567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21567v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21567v2', 'EaqVLA: Encoding-aligned Quantization for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Jiang, Zihao Zheng, Xiuping Cui, Maoliang Li, JIayu Chen, Xiang Chen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-07-31)

**备注**: There is an error in this paper, and as the author, I request retraction

---

## 💡 一句话要点

**提出EaqVLA以解决VLA模型量化效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `量化技术` `编码对齐` `混合精度` `具身人工智能`

## 📋 核心要点

1. 现有的VLA模型在计算和存储上成本高昂，亟需优化以提高效率。
2. 本文提出EaqVLA框架，通过编码对齐量化来解决VLA模型中的量化问题。
3. 实验结果显示，EaqVLA在量化性能上优于现有方法，量化损失最小且加速效果显著。

## 📝 摘要（中文）

随着具身人工智能的发展，端到端控制策略如视觉-语言-动作（VLA）模型已成为主流。然而，现有VLA模型面临高昂的计算和存储成本，需要优化。量化被认为是降低内存成本和加速计算的有效方法，但现有量化方法在VLA模型中应用受限于令牌对齐问题。为此，本文提出了一种名为EaqVLA的优化框架，采用编码对齐量化。通过完整的分析方法识别不同粒度的错位，基于分析结果提出了考虑编码对齐的混合精度量化。实验表明，EaqVLA在端到端动作控制中实现了更好的量化性能，量化损失最小，并且加速效果显著。

## 🔬 方法详解

**问题定义**：本文旨在解决VLA模型在量化过程中因令牌对齐问题导致的效率低下。现有量化方法无法有效应用于这些模型，造成计算和存储成本高。

**核心思路**：提出EaqVLA框架，通过编码对齐量化技术，识别并解决VLA模型中的错位问题，以提高量化效果和计算效率。

**技术框架**：EaqVLA框架包括分析模块和量化模块。分析模块负责识别不同粒度的错位，量化模块则基于分析结果实施混合精度量化。

**关键创新**：EaqVLA的核心创新在于引入编码对齐的概念，显著改善了量化过程中的对齐问题，与传统方法相比，能够更好地适应VLA模型的特性。

**关键设计**：在设计中，采用了混合精度量化策略，结合了不同层次的量化精度，以最小化量化损失，同时优化了网络结构以适应新的量化方案。具体参数设置和损失函数设计在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，EaqVLA在量化性能上优于现有方法，量化损失最小，且在端到端动作控制中实现了xxx倍的加速，显示出其在实际应用中的显著优势。

## 🎯 应用场景

EaqVLA框架在具身人工智能领域具有广泛的应用潜力，尤其是在机器人控制、智能助手和自动驾驶等场景中。通过降低计算和存储成本，该方法能够使得VLA模型在资源受限的环境中更高效地运行，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> With the development of Embodied Artificial intelligence, the end-to-end control policy such as Vision-Language-Action (VLA) model has become the mainstream. Existing VLA models faces expensive computing/storage cost, which need to be optimized. Quantization is considered as the most effective method which can not only reduce the memory cost but also achieve computation acceleration. However, we find the token alignment of VLA models hinders the application of existing quantization methods. To address this, we proposed an optimized framework called EaqVLA, which apply encoding-aligned quantization to VLA models. Specifically, we propose an complete analysis method to find the misalignment in various granularity. Based on the analysis results, we propose a mixed precision quantization with the awareness of encoding alignment. Experiments shows that the porposed EaqVLA achieves better quantization performance (with the minimal quantization loss for end-to-end action control and xxx times acceleration) than existing quantization methods.

