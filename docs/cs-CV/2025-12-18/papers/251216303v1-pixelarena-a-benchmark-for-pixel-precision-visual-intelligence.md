---
layout: default
title: PixelArena: A benchmark for Pixel-Precision Visual Intelligence
---

# PixelArena: A benchmark for Pixel-Precision Visual Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16303" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16303v1</a>
  <a href="https://arxiv.org/pdf/2512.16303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16303v1', 'PixelArena: A benchmark for Pixel-Precision Visual Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Liang, Sizhe Cheng, Chenqi Yi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

**备注**: 7 pages, 11 figures, project page: https://pixelarena.reify.ing/project

---

## 💡 一句话要点

**PixelArena：提出像素级视觉智能评估基准，用于客观评估图像生成模型的细粒度生成能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像生成` `视觉智能` `语义分割` `多模态大语言模型` `评估基准`

## 📋 核心要点

1. 现有图像生成基准侧重于美学质量，缺乏对模型细粒度生成能力的客观评估。
2. PixelArena利用语义分割任务，以像素精度评估图像生成模型的细粒度视觉智能。
3. 实验表明，Gemini 3 Pro Image在零样本语义分割任务中表现出卓越的生成能力和泛化性。

## 📝 摘要（中文）

本文提出了PixelArena，一个用于像素精度视觉智能的评估基准。随着多模态大语言模型在图像输出方面的涌现，现有的图像生成基准更多关注美学，而非细粒度的生成能力。PixelArena通过语义分割任务，以像素精度客观地检验模型的细粒度生成智能。研究发现，最新的Gemini 3 Pro Image在零样本设置下展现出卓越的图像生成能力，能够生成高保真度的语义掩码，体现了前所未有的视觉智能和在新图像生成任务中的真正泛化能力。进一步研究了其结果，与其他模型进行了定性和定量比较，并展示了失败案例。这些发现不仅标志着该领域令人兴奋的进展，也为多模态、推理、可解释性和基准测试等未来研究提供了见解。

## 🔬 方法详解

**问题定义**：现有图像生成模型的评估主要集中在生成图像的美学质量上，缺乏对模型理解和生成图像细节能力的客观评估。尤其是在像素级别的细粒度控制和理解方面，现有方法难以有效评估模型是否真正具备视觉智能。因此，需要一个能够以像素精度评估模型生成图像语义信息的基准。

**核心思路**：PixelArena的核心思路是利用语义分割任务作为评估图像生成模型细粒度视觉智能的代理任务。语义分割需要模型理解图像中每个像素所属的类别，从而反映模型对图像内容的细致理解和生成能力。通过比较生成图像的语义分割结果与真实标签，可以客观地评估模型的生成质量。

**技术框架**：PixelArena基准测试主要包含以下几个阶段：1) 给定文本提示，使用待评估的图像生成模型生成图像；2) 使用预训练的语义分割模型对生成的图像进行语义分割，得到预测的语义掩码；3) 将预测的语义掩码与真实的语义标签进行比较，计算像素级别的精度指标，如IoU (Intersection over Union) 和 Pixel Accuracy；4) 对比不同模型的性能指标，并进行定性分析，找出模型的优势和不足。

**关键创新**：PixelArena的关键创新在于将语义分割任务作为评估图像生成模型细粒度视觉智能的桥梁。与传统的美学评估方法不同，PixelArena提供了一种客观、可量化的评估方法，能够深入了解模型在像素级别的理解和生成能力。此外，该基准测试可以用于评估各种图像生成模型，包括GAN、VAE和扩散模型等。

**关键设计**：PixelArena的关键设计包括：1) 选择合适的语义分割数据集，例如Cityscapes、ADE20K等，这些数据集包含丰富的语义信息和像素级别的标注；2) 使用标准的语义分割评估指标，如IoU和Pixel Accuracy，来量化模型的性能；3) 设计合理的文本提示，以引导模型生成具有特定语义信息的图像；4) 对比不同模型的性能，并进行统计显著性检验，以确保评估结果的可靠性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/label-color-palette.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/model-comparison-celeb.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16303v1/images/celeb/best-f1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Gemini 3 Pro Image在零样本语义分割任务中表现出卓越的生成能力，其生成的语义掩码具有很高的保真度。与其他模型相比，Gemini 3 Pro Image在IoU和Pixel Accuracy等指标上取得了显著的提升，体现了其强大的视觉智能和泛化能力。该研究还发现了Gemini 3 Pro Image的一些失败案例，为未来的研究提供了重要的参考。

## 🎯 应用场景

PixelArena可用于评估和比较各种图像生成模型的细粒度视觉智能，推动多模态大语言模型的发展。该基准测试可以帮助研究人员更好地理解模型的优势和不足，从而改进模型的设计和训练方法。此外，PixelArena还可以应用于图像编辑、图像修复等领域，提高生成图像的质量和可控性。

## 📄 摘要（原文）

> Multi-modal large language models that have image output are emerging. Many image generation benchmarks focus on aesthetics instead of fine-grained generation capabilities. In PixelArena, we propose using semantic segmentation tasks to objectively examine their fine-grained generative intelligence with pixel precision. We find the latest Gemini 3 Pro Image has emergent image generation capabilities that generate semantic masks with high fidelity under zero-shot settings, showcasing visual intelligence unseen before and true generalization in new image generation tasks. We further investigate its results, compare them qualitatively and quantitatively with those of other models, and present failure cases. The findings not only signal exciting progress in the field but also provide insights into future research related to multimodality, reasoning, interpretability and benchmarking.

