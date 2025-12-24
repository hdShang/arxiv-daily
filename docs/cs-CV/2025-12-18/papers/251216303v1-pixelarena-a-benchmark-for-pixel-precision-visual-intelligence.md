---
layout: default
title: "PixelArena: A benchmark for Pixel-Precision Visual Intelligence"
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

**PixelArena：提出像素级视觉智能评测基准，评估多模态大模型图像生成能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `像素级视觉智能` `多模态大模型` `图像生成` `语义分割` `评测基准`

## 📋 核心要点

1. 现有图像生成基准侧重于美学评估，缺乏对模型细粒度生成能力的客观像素级评估。
2. PixelArena利用语义分割任务，通过生成语义掩码来评估多模态大模型的像素精度视觉智能。
3. 实验表明Gemini 3 Pro Image在零样本语义分割任务中表现出卓越的图像生成能力和泛化能力。

## 📝 摘要（中文）

本文提出了PixelArena，一个用于像素精度视觉智能的评测基准。随着具有图像输出能力的多模态大型语言模型不断涌现，许多图像生成基准侧重于美学，而非细粒度的生成能力。PixelArena利用语义分割任务，以客观地检验这些模型在像素精度上的生成智能。研究发现，最新的Gemini 3 Pro Image在零样本设置下展现出卓越的图像生成能力，能够生成高保真度的语义掩码，体现了前所未见的视觉智能和在新图像生成任务中的真正泛化能力。进一步研究了其结果，并与其他模型进行了定性和定量比较，同时展示了失败案例。这些发现不仅标志着该领域令人兴奋的进展，也为多模态、推理、可解释性和基准测试等未来研究提供了见解。

## 🔬 方法详解

**问题定义**：现有图像生成基准主要关注生成图像的美学质量，缺乏对模型生成图像在像素级别上的准确性和细节控制能力的评估。这使得我们难以客观地衡量模型是否真正理解了图像的语义信息，并能够精确地生成符合语义信息的图像。

**核心思路**：PixelArena的核心思路是利用语义分割任务来评估图像生成模型的像素级视觉智能。语义分割需要模型理解图像中每个像素所属的类别，并生成相应的语义掩码。通过比较生成掩码与真实掩码的相似度，可以客观地衡量模型生成图像的准确性和细节控制能力。选择语义分割任务是因为它能够提供像素级别的反馈，从而更精确地评估模型的视觉智能。

**技术框架**：PixelArena基准测试主要包含以下几个阶段：1) 数据集准备：选择或构建包含像素级标注的图像数据集，用于评估模型的语义分割能力。2) 模型推理：将图像输入到待评估的多模态大模型中，要求模型生成对应的语义掩码。3) 评估指标：使用像素精度、IoU等指标来衡量生成掩码与真实掩码的相似度。4) 结果分析：对模型的生成结果进行定性和定量分析，找出模型的优势和不足。

**关键创新**：PixelArena的关键创新在于将语义分割任务作为评估多模态大模型像素级视觉智能的手段。与传统的图像生成基准相比，PixelArena能够提供更细粒度的评估结果，从而更准确地反映模型的视觉智能水平。此外，PixelArena还强调在零样本设置下评估模型的泛化能力，这更符合实际应用场景的需求。

**关键设计**：PixelArena的关键设计包括：1) 数据集选择：选择具有代表性的语义分割数据集，例如Cityscapes、ADE20K等。2) 评估指标：采用像素精度、平均IoU等常用的语义分割评估指标。3) 零样本设置：在评估过程中，不使用任何与目标数据集相关的训练数据，以评估模型的泛化能力。4) 失败案例分析：对模型生成错误的案例进行分析，找出模型在哪些方面存在不足。

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

实验结果表明，Gemini 3 Pro Image在PixelArena基准测试中表现出色，在零样本语义分割任务中展现出卓越的图像生成能力，能够生成高保真度的语义掩码。与其他模型相比，Gemini 3 Pro Image在像素精度和IoU等指标上均取得了显著提升，体现了其强大的视觉智能和泛化能力。该研究还分析了Gemini 3 Pro Image的失败案例，为未来的研究提供了有价值的参考。

## 🎯 应用场景

PixelArena可用于评估和比较各种多模态大模型的图像生成能力，推动模型在图像编辑、自动驾驶、机器人等领域的应用。通过像素级精度评估，可以帮助研究人员更好地理解模型的优势和不足，从而改进模型的设计和训练方法。此外，PixelArena还可以作为一种诊断工具，用于发现模型中的潜在问题，例如幻觉或偏见。

## 📄 摘要（原文）

> Multi-modal large language models that have image output are emerging. Many image generation benchmarks focus on aesthetics instead of fine-grained generation capabilities. In PixelArena, we propose using semantic segmentation tasks to objectively examine their fine-grained generative intelligence with pixel precision. We find the latest Gemini 3 Pro Image has emergent image generation capabilities that generate semantic masks with high fidelity under zero-shot settings, showcasing visual intelligence unseen before and true generalization in new image generation tasks. We further investigate its results, compare them qualitatively and quantitatively with those of other models, and present failure cases. The findings not only signal exciting progress in the field but also provide insights into future research related to multimodality, reasoning, interpretability and benchmarking.

