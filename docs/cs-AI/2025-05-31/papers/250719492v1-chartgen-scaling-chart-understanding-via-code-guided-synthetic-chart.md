---
layout: default
title: ChartGen: Scaling Chart Understanding Via Code-Guided Synthetic Chart Generation
---

# ChartGen: Scaling Chart Understanding Via Code-Guided Synthetic Chart Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.19492" class="toolbar-btn" target="_blank">📄 arXiv: 2507.19492v1</a>
  <a href="https://arxiv.org/pdf/2507.19492.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.19492v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.19492v1', 'ChartGen: Scaling Chart Understanding Via Code-Guided Synthetic Chart Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jovana Kondic, Pengyuan Li, Dhiraj Joshi, Zexue He, Shafiq Abedin, Jennifer Sun, Ben Wiesel, Eli Schwartz, Ahmed Nassar, Bo Wu, Assaf Arbelle, Aude Oliva, Dan Gutfreund, Leonid Karlinsky, Rogerio Feris

**分类**: cs.HC, cs.AI, cs.CV

**发布日期**: 2025-05-31

**🔗 代码/项目**: [GITHUB](https://github.com/SD122025/ChartGen/)

---

## 💡 一句话要点

**提出ChartGen以解决图表理解中的合成数据生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图表理解` `合成数据生成` `视觉-语言模型` `大语言模型` `数据可视化` `机器学习`

## 📋 核心要点

1. 现有的多模态基准主要集中在图表问题回答和总结，缺乏针对图表到代码重建的研究。
2. 本文提出ChartGen，通过视觉-语言模型和大语言模型的结合，实现从图表图像到可执行代码的自动化生成。
3. 实验中生成了222.5K个图表图像-代码对，并评估了六个开放权重的视觉-语言模型，显示出显著的改进空间。

## 📝 摘要（中文）

图表到代码重建是从图表图像中恢复可执行绘图脚本的任务，这对于模型将数据可视化转化为精确的机器可读形式至关重要。然而，现有的多模态基准主要集中在回答图表相关问题或对其进行总结。为了解决这一问题，本文提出了ChartGen，一个全自动的代码引导合成图表生成管道。ChartGen从种子图表图像出发，利用视觉-语言模型重建图像为Python脚本，并通过代码导向的大语言模型迭代增强该脚本。通过ChartGen，我们从13K种子图表图像生成了222.5K个独特的图表图像-代码对，并创建了一个涵盖27种图表类型、11个绘图库和多种数据模态的开源合成图表数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决从图表图像中恢复可执行绘图脚本的挑战。现有方法在图表理解和生成方面存在局限，无法有效地将图表转化为机器可读的代码。

**核心思路**：论文的核心思路是通过ChartGen管道，结合视觉-语言模型和代码导向的大语言模型，实现图表图像到Python脚本的自动重建与增强。这种设计旨在提高图表理解的准确性和效率。

**技术框架**：ChartGen的整体架构包括两个主要模块：首先，使用视觉-语言模型将图表图像重建为初步的Python脚本；其次，利用大语言模型对该脚本进行迭代增强。该流程确保生成的代码不仅可执行，还能准确反映图表的特征。

**关键创新**：最重要的技术创新在于将视觉-语言模型与代码导向的大语言模型结合使用，形成了一个闭环的生成过程。这一方法与现有的图表理解方法相比，显著提高了生成代码的质量和多样性。

**关键设计**：在参数设置上，使用了多种图表类型和绘图库的组合，以确保生成数据的多样性。此外，损失函数的设计考虑了代码的可执行性和与图表的对应关系，确保生成的代码能够正确反映图表的内容。

## 📊 实验亮点

实验结果显示，使用ChartGen生成的222.5K个图表图像-代码对，涵盖了27种图表类型和11个绘图库。对六个开放权重的视觉-语言模型的评估表明，当前模型在图表理解上仍有显著的提升空间，尤其是在生成代码的准确性和多样性方面。

## 🎯 应用场景

该研究的潜在应用领域包括数据可视化工具的自动化开发、教育领域的图表生成与分析，以及商业智能中的数据报告生成。通过提供高质量的图表到代码的转换，ChartGen能够加速数据分析和可视化的工作流程，提升用户体验和效率。

## 📄 摘要（原文）

> Chart-to-code reconstruction -- the task of recovering executable plotting scripts from chart images -- provides important insights into a model's ability to ground data visualizations in precise, machine-readable form. Yet many existing multimodal benchmarks largely focus primarily on answering questions about charts or summarizing them. To bridge this gap, we present ChartGen, a fully-automated pipeline for code-guided synthetic chart generation. Starting from seed chart images, ChartGen (i) prompts a vision-language model (VLM) to reconstruct each image into a python script, and (ii) iteratively augments that script with a code-oriented large language model (LLM). Using ChartGen, we create 222.5K unique chart-image code pairs from 13K seed chart images, and present an open-source synthetic chart dataset covering 27 chart types, 11 plotting libraries, and multiple data modalities (image, code, text, CSV, DocTags). From this corpus, we curate a held-out chart-to-code evaluation subset of 4.3K chart image-code pairs, and evaluate six open-weight VLMs (3B - 26B parameters), highlighting substantial room for progress. We release the pipeline, prompts, and the dataset to help accelerate efforts towards robust chart understanding and vision-conditioned code generation: https://github.com/SD122025/ChartGen/

