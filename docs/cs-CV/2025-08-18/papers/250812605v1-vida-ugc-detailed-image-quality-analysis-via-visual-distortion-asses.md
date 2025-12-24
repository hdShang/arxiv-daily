---
layout: default
title: "ViDA-UGC: Detailed Image Quality Analysis via Visual Distortion Assessment for UGC Images"
---

# ViDA-UGC: Detailed Image Quality Analysis via Visual Distortion Assessment for UGC Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12605" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12605v1</a>
  <a href="https://arxiv.org/pdf/2508.12605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12605v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12605v1', 'ViDA-UGC: Detailed Image Quality Analysis via Visual Distortion Assessment for UGC Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Liao, Jieyu Yuan, Yifang Xu, Chunle Guo, Zilong Zhang, Jihong Li, Jiachen Fu, Haotian Fan, Tao Li, Junhui Cui, Chongyi Li

**分类**: cs.CV

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出ViDA-UGC以解决UGC图像质量评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像质量评估` `用户生成内容` `视觉失真评估` `多模态大语言模型` `链式思维` `数据集构建` `质量控制`

## 📋 核心要点

1. 现有的可解释图像质量评估方法未能有效评估UGC和AIGC图像，缺乏详细的质量分析。
2. 本研究提出ViDA-UGC数据集，通过失真导向的流程和CoT框架，提供细粒度的UGC图像质量评估。
3. 实验结果显示，ViDA-UGC及其框架在多个基准上显著提升了图像质量分析能力，超越了GPT-4o。

## 📝 摘要（中文）

近年来，多模态大语言模型（MLLMs）的进展使得图像质量评估（IQA）从不可解释的图像质量评分转向可解释的IQA，展现出在质量控制和优化指导等实际应用中的潜力。然而，现有的可解释IQA方法在评估用户生成内容（UGC）和人工智能生成内容（AIGC）图像时，未能充分利用相同的失真标准，且缺乏对图像质量的详细分析。本研究建立了第一个大规模的UGC图像视觉失真评估指令调优数据集ViDA-UGC，包含11K张图像及其细粒度质量基础、详细质量感知和推理质量描述数据。该数据集通过失真导向的流程构建，结合人类标注和链式思维（CoT）评估框架，帮助捕捉与失真模式相关的丰富低级视觉特征。实验结果表明，ViDA-UGC及CoT框架在多个基础MLLMs上显著提升了图像质量分析能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有可解释图像质量评估方法在UGC和AIGC图像评估中的不足，特别是缺乏详细的质量分析和失真标准的有效应用。

**核心思路**：通过构建ViDA-UGC数据集，结合人类标注和链式思维框架，系统性地评估UGC图像的视觉失真，进而实现细粒度的质量分析。

**技术框架**：整体架构包括数据集构建、失真导向的标注流程和CoT评估框架。数据集包含11K张图像及其质量描述，CoT框架则引导模型生成质量分析。

**关键创新**：ViDA-UGC数据集的构建及其失真导向的评估方法是本研究的核心创新，显著提高了UGC图像质量评估的准确性和细致度。

**关键设计**：在数据集构建中，采用了人类标注和专业团队的审核，确保了数据的准确性和质量；同时，选择了476张图像及其6149个问答对进行深入分析，提升了模型生成信息的可靠性。

## 📊 实验亮点

实验结果表明，ViDA-UGC及其CoT框架在ViDA-UGC-Bench和Q-Bench上显著提升了图像质量分析能力，尤其在多个基准测试中超越了GPT-4o，展示了其在UGC图像评估中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括图像质量控制、内容创作优化和社交媒体平台的UGC监测等。通过提供更准确的图像质量评估，ViDA-UGC可以帮助内容创作者和平台运营者提升用户体验，优化内容质量，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have introduced a paradigm shift for Image Quality Assessment (IQA) from unexplainable image quality scoring to explainable IQA, demonstrating practical applications like quality control and optimization guidance. However, current explainable IQA methods not only inadequately use the same distortion criteria to evaluate both User-Generated Content (UGC) and AI-Generated Content (AIGC) images, but also lack detailed quality analysis for monitoring image quality and guiding image restoration. In this study, we establish the first large-scale Visual Distortion Assessment Instruction Tuning Dataset for UGC images, termed ViDA-UGC, which comprises 11K images with fine-grained quality grounding, detailed quality perception, and reasoning quality description data. This dataset is constructed through a distortion-oriented pipeline, which involves human subject annotation and a Chain-of-Thought (CoT) assessment framework. This framework guides GPT-4o to generate quality descriptions by identifying and analyzing UGC distortions, which helps capturing rich low-level visual features that inherently correlate with distortion patterns. Moreover, we carefully select 476 images with corresponding 6,149 question answer pairs from ViDA-UGC and invite a professional team to ensure the accuracy and quality of GPT-generated information. The selected and revised data further contribute to the first UGC distortion assessment benchmark, termed ViDA-UGC-Bench. Experimental results demonstrate the effectiveness of the ViDA-UGC and CoT framework for consistently enhancing various image quality analysis abilities across multiple base MLLMs on ViDA-UGC-Bench and Q-Bench, even surpassing GPT-4o.

