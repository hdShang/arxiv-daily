---
layout: default
title: JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14620" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14620</a>
  <a href="https://arxiv.org/pdf/2512.14620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14620" onclick="toggleFavorite(this, '2512.14620', 'JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, Kiyoharu Aizawa

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出JMMMU-Pro基准测试，用于评估日语多学科多模态理解能力，并提出Vibe基准构建方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `视觉问答` `日语处理` `基准测试` `图像生成模型` `大型语言模型` `Vibe构建方法`

## 📋 核心要点

1. 现有基准测试在评估大型语言模型（LMM）的日语多模态理解能力方面存在不足，尤其是在视觉-文本集成理解方面。
2. 提出Vibe基准构建方法，利用图像生成模型生成候选视觉问题，并通过人工验证和调整提示来保证基准质量。
3. 实验表明，开源LMM在JMMMU-Pro基准测试上表现不佳，验证了该基准的挑战性，并为未来研究提供了方向。

## 📝 摘要（中文）

本文介绍了JMMMU-Pro，一个基于图像的日语多学科多模态理解基准测试，以及Vibe基准构建方法，一种可扩展的构建方法。JMMMU-Pro延续了从MMMU到MMMU-Pro的演进，通过将问题图像和问题文本组合成单个图像来扩展JMMMU，从而创建一个需要通过视觉感知进行综合视觉-文本理解的基准。为了构建JMMMU-Pro，我们提出了Vibe基准构建方法，该方法利用图像生成模型（例如Nano Banana Pro）生成候选视觉问题，然后由人工验证输出，并在必要时使用调整后的提示重新生成，以确保质量。通过利用Nano Banana Pro的高度逼真的图像生成能力及其嵌入清晰日语文本的能力，我们以低成本构建了一个高质量的基准，涵盖了广泛的背景和布局设计。实验结果表明，所有开源LMM在JMMMU-Pro上都表现不佳，这突显了JMMMU-Pro作为指导开源社区未来工作的重要基准。我们相信JMMMU-Pro为评估LMM的日语能力提供了一个更严格的评估工具，并且我们的Vibe基准构建方法也为未来基于图像的VQA基准的开发提供了有效的指导。

## 🔬 方法详解

**问题定义**：论文旨在解决现有日语多模态理解基准测试的不足，特别是缺乏对视觉和文本信息进行深度融合理解的评估。现有方法难以生成高质量、多样化的测试用例，并且成本较高。

**核心思路**：论文的核心思路是利用图像生成模型（如Nano Banana Pro）自动生成候选的视觉问题，然后通过人工验证和调整提示来确保生成高质量的基准测试。这种方法旨在降低基准测试的构建成本，并提高其多样性和质量。

**技术框架**：Vibe基准构建方法包含以下主要阶段：1) 使用图像生成模型生成候选视觉问题，包括图像和嵌入图像中的日语文本。2) 人工验证生成的视觉问题，评估其质量和相关性。3) 如果需要，调整图像生成模型的提示，重新生成视觉问题，直到满足质量要求。4) 将验证通过的视觉问题添加到基准测试中。

**关键创新**：该方法最重要的技术创新点在于利用图像生成模型自动生成视觉问题，并结合人工验证和调整提示的反馈机制。这与传统的人工标注方法相比，大大降低了成本，并提高了基准测试的多样性和可扩展性。

**关键设计**：关键设计包括选择合适的图像生成模型（Nano Banana Pro），该模型需要能够生成高质量的图像，并且能够嵌入清晰的日语文本。此外，人工验证过程需要制定明确的质量标准，并提供有效的反馈机制，以便调整图像生成模型的提示。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有的开源LMM在JMMMU-Pro基准测试上表现显著不足，这表明JMMMU-Pro是一个具有挑战性的基准，能够有效评估LMM的日语多模态理解能力。该基准的构建方法Vibe，为低成本、高质量地构建图像相关的VQA基准提供了新的思路。

## 🎯 应用场景

JMMMU-Pro基准测试可用于评估和提升大型语言模型在日语环境下的多模态理解能力，尤其是在需要视觉和文本信息深度融合的场景中。该研究成果可应用于智能客服、教育、医疗等领域，提升人机交互的智能化水平。

## 📄 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

