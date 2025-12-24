---
layout: default
title: "Perceive Anything: Recognize, Explain, Caption, and Segment Anything in Images and Videos"
---

# Perceive Anything: Recognize, Explain, Caption, and Segment Anything in Images and Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05302" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05302v1</a>
  <a href="https://arxiv.org/pdf/2506.05302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05302v1', 'Perceive Anything: Recognize, Explain, Caption, and Segment Anything in Images and Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weifeng Lin, Xinyu Wei, Ruichuan An, Tianhe Ren, Tingwei Chen, Renrui Zhang, Ziyu Guo, Wentao Zhang, Lei Zhang, Hongsheng Li

**分类**: cs.CV

**发布日期**: 2025-06-05

**备注**: 19 pages, 13 figures, Website: https://Perceive-Anything.github.io

---

## 💡 一句话要点

**提出Perceive Anything模型以解决图像和视频的区域理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `区域理解` `多模态输出` `大型语言模型` `视觉特征转化` `数据增强`

## 📋 核心要点

1. 现有方法在区域级视觉理解中存在效率低下和多模态输出不足的问题。
2. 论文提出的PAM模型通过整合LLMs与SAM 2，实现了高效的对象分割和多样化语义输出。
3. PAM在多种区域理解任务中表现优异，运行速度提升1.2-2.4倍，内存消耗显著降低。

## 📝 摘要（中文）

我们提出了Perceive Anything Model（PAM），这是一个概念上简单且高效的框架，旨在实现图像和视频的全面区域级视觉理解。该方法通过整合大型语言模型（LLMs），扩展了强大的分割模型SAM 2，实现了对象分割与多样化区域特定语义输出的生成，包括类别、标签定义、功能解释和详细描述。引入的语义感知器有效地将SAM 2的丰富视觉特征转化为LLM可理解的多模态标记。为了支持稳健的多粒度理解，我们还开发了专门的数据精炼和增强管道，生成了150万张图像和60万段视频的区域语义注释数据集。PAM设计轻量高效，在多种区域理解任务中表现出色，运行速度比以往方法快1.2-2.4倍，GPU内存消耗更少，为实际应用提供了有效解决方案。

## 🔬 方法详解

**问题定义**：本论文旨在解决图像和视频中的区域级视觉理解问题，现有方法在处理多模态输出和效率方面存在不足。

**核心思路**：PAM模型通过结合大型语言模型（LLMs）与现有的分割模型SAM 2，能够同时进行对象分割和生成丰富的语义信息，从而提升理解能力。

**技术框架**：PAM的整体架构包括语义感知器模块，该模块将SAM 2的视觉特征转化为多模态标记，支持与LLMs的有效交互。此外，论文还设计了数据精炼和增强管道，以生成高质量的区域语义注释数据。

**关键创新**：PAM的关键创新在于引入了语义感知器，使得视觉特征能够高效转化为LLMs可理解的格式，这一设计显著提升了多模态理解的能力。

**关键设计**：在模型设计中，采用了优化的损失函数和网络结构，确保了模型在处理复杂视觉任务时的高效性和准确性。

## 📊 实验亮点

PAM模型在多种区域理解任务中表现出色，运行速度比以往方法快1.2-2.4倍，且GPU内存消耗显著降低。这些实验结果表明，PAM在实际应用中具有更高的效率和更低的资源需求。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、增强现实和人机交互等。PAM模型的高效性和多模态理解能力使其在实际应用中具有重要价值，能够推动相关领域的技术进步和创新。

## 📄 摘要（原文）

> We present Perceive Anything Model (PAM), a conceptually straightforward and efficient framework for comprehensive region-level visual understanding in images and videos. Our approach extends the powerful segmentation model SAM 2 by integrating Large Language Models (LLMs), enabling simultaneous object segmentation with the generation of diverse, region-specific semantic outputs, including categories, label definition, functional explanations, and detailed captions. A key component, Semantic Perceiver, is introduced to efficiently transform SAM 2's rich visual features, which inherently carry general vision, localization, and semantic priors into multi-modal tokens for LLM comprehension. To support robust multi-granularity understanding, we also develop a dedicated data refinement and augmentation pipeline, yielding a high-quality dataset of 1.5M image and 0.6M video region-semantic annotations, including novel region-level streaming video caption data. PAM is designed for lightweightness and efficiency, while also demonstrates strong performance across a diverse range of region understanding tasks. It runs 1.2-2.4x faster and consumes less GPU memory than prior approaches, offering a practical solution for real-world applications. We believe that our effective approach will serve as a strong baseline for future research in region-level visual understanding.

