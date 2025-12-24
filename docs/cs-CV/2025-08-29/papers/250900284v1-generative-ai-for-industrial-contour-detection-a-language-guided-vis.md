---
layout: default
title: "Generative AI for Industrial Contour Detection: A Language-Guided Vision System"
---

# Generative AI for Industrial Contour Detection: A Language-Guided Vision System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00284" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00284v1</a>
  <a href="https://arxiv.org/pdf/2509.00284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00284v1', 'Generative AI for Industrial Contour Detection: A Language-Guided Vision System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Gong, Tommy, Wang, Sara Chaker, Yanchen Dong, Fouad Bousetouane, Brenden Morton, Mark Mendez

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-29

**备注**: 20 pages, 5 figures

---

## 💡 一句话要点

**提出语言引导的生成视觉系统以解决工业轮廓检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工业视觉` `轮廓检测` `生成对抗网络` `视觉-语言建模` `多模态融合` `自动化检测` `质量控制`

## 📋 核心要点

1. 现有工业计算机视觉方法在噪声和材料变异下表现不佳，导致边缘检测效果有限。
2. 提出的系统通过条件GAN生成轮廓，并结合视觉-语言建模进行多模态精炼，提升检测精度。
3. 在FabTrack数据集上，系统显著提高了轮廓的保真度，减少了手动工作量，且GPT-image-1表现优于其他模型。

## 📝 摘要（中文）

工业计算机视觉系统常常受到噪声、材料变异和不受控成像条件的影响，限制了经典边缘检测器和手工管道的有效性。本文提出了一种语言引导的生成视觉系统，用于制造中的残余轮廓检测，旨在实现CAD级别的精度。该系统分为三个阶段：数据采集与预处理、使用条件生成对抗网络（GAN）进行轮廓生成，以及通过视觉-语言建模进行多模态轮廓精炼。在专有的FabTrack数据集上，所提系统提高了轮廓的保真度，增强了边缘连续性和几何对齐，同时减少了手动描绘。在精炼阶段，我们对多个视觉-语言模型进行了基准测试，包括谷歌的Gemini 2.0 Flash和集成在VLM引导工作流中的OpenAI的GPT-image-1。结果表明，在标准化条件下，GPT-image-1在结构准确性和感知质量上均优于Gemini 2.0 Flash。这些发现展示了VLM引导生成工作流在推动工业计算机视觉方面的潜力，超越了经典管道的局限。

## 🔬 方法详解

**问题定义**：本文旨在解决工业环境中轮廓检测的挑战，现有方法在噪声、材料变异和成像条件不稳定时效果不佳，导致边缘检测的准确性和一致性不足。

**核心思路**：论文提出了一种语言引导的生成视觉系统，通过条件GAN生成轮廓，并利用视觉-语言模型进行精炼，旨在实现高精度的轮廓检测。

**技术框架**：系统分为三个主要阶段：首先进行数据采集与预处理；其次使用条件GAN生成初步轮廓；最后通过视觉-语言建模进行多模态的轮廓精炼。

**关键创新**：最重要的创新在于引入了视觉-语言建模，使得系统能够在生成过程中结合自然语言提示，提升了轮廓检测的精度和一致性。

**关键设计**：在精炼阶段，采用了多种视觉-语言模型进行比较，特别是GPT-image-1在结构准确性和感知质量上表现优异，优化了模型的参数设置和损失函数以适应工业应用。

## 📊 实验亮点

实验结果显示，所提系统在FabTrack数据集上显著提高了轮廓的保真度，尤其是在边缘连续性和几何对齐方面。同时，GPT-image-1在结构准确性和感知质量上均优于Gemini 2.0 Flash，展示了VLM引导生成工作流的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括制造业中的自动化检测、质量控制和机器人视觉系统。通过提高轮廓检测的精度和效率，能够显著降低人工成本，并提升生产线的智能化水平，未来可能推动更多工业领域的智能化转型。

## 📄 摘要（原文）

> Industrial computer vision systems often struggle with noise, material variability, and uncontrolled imaging conditions, limiting the effectiveness of classical edge detectors and handcrafted pipelines. In this work, we present a language-guided generative vision system for remnant contour detection in manufacturing, designed to achieve CAD-level precision. The system is organized into three stages: data acquisition and preprocessing, contour generation using a conditional GAN, and multimodal contour refinement through vision-language modeling, where standardized prompts are crafted in a human-in-the-loop process and applied through image-text guided synthesis. On proprietary FabTrack datasets, the proposed system improved contour fidelity, enhancing edge continuity and geometric alignment while reducing manual tracing. For the refinement stage, we benchmarked several vision-language models, including Google's Gemini 2.0 Flash, OpenAI's GPT-image-1 integrated within a VLM-guided workflow, and open-source baselines. Under standardized conditions, GPT-image-1 consistently outperformed Gemini 2.0 Flash in both structural accuracy and perceptual quality. These findings demonstrate the promise of VLM-guided generative workflows for advancing industrial computer vision beyond the limitations of classical pipelines.

