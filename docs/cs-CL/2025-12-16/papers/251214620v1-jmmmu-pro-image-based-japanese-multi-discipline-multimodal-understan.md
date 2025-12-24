---
layout: default
title: "JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction"
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14620" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14620v1</a>
  <a href="https://arxiv.org/pdf/2512.14620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14620v1', 'JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, Kiyoharu Aizawa

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://mmmu-japanese-benchmark.github.io/JMMMU_Pro/

---

## 💡 一句话要点

**提出JMMMU-Pro日语多学科多模态理解基准，并提出Vibe基准构建方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `视觉问答` `日语基准` `图像生成` `人工验证` `语言模型` `基准构建` `多学科`

## 📋 核心要点

1. 现有LMM在日语多模态理解方面存在不足，缺乏高质量的日语图像-文本综合理解基准。
2. 提出Vibe基准构建方法，利用图像生成模型和人工验证相结合的方式，高效构建高质量的JMMMU-Pro基准。
3. 实验表明，开源LMM在JMMMU-Pro基准上表现显著不足，验证了该基准的挑战性和重要性。

## 📝 摘要（中文）

本文介绍了JMMMU-Pro，一个基于图像的日语多学科多模态理解基准，以及Vibe基准构建方法，一种可扩展的构建方法。JMMMU-Pro在MMMU的基础上进行了扩展，通过将问题图像和问题文本组合成单个图像，从而创建了一个需要通过视觉感知进行综合视觉-文本理解的基准。为了构建JMMMU-Pro，我们提出了Vibe基准构建方法，该方法利用图像生成模型（例如Nano Banana Pro）生成候选视觉问题，然后由人工验证输出，并在必要时使用调整后的提示重新生成，以确保质量。通过利用Nano Banana Pro的高度逼真的图像生成能力及其嵌入清晰日语文本的能力，我们以低成本构建了一个高质量的基准，涵盖了广泛的背景和布局设计。实验结果表明，所有开源LMM在JMMMU-Pro上都表现不佳，这突显了JMMMU-Pro作为指导开源社区未来工作的重要基准。我们相信JMMMU-Pro为评估LMM的日语能力提供了一个更严格的评估工具，并且我们的Vibe基准构建方法也为未来基于图像的VQA基准的开发提供了有效的指导。

## 🔬 方法详解

**问题定义**：论文旨在解决现有日语多模态理解基准不足的问题，特别是缺乏能够有效评估LMM在日语环境下图像-文本综合理解能力的基准。现有方法或者数据量不足，或者质量不高，难以充分评估LMM的性能。

**核心思路**：论文的核心思路是利用图像生成模型自动生成候选的视觉问题，然后通过人工验证和调整来保证基准的质量。这种方法可以显著降低构建高质量基准的成本，并提高构建效率。同时，将问题图像和问题文本组合成单个图像，增加了模型理解的难度，更贴近实际应用场景。

**技术框架**：Vibe基准构建方法主要包含以下几个阶段：1) 使用图像生成模型（如Nano Banana Pro）生成候选视觉问题，包括图像和问题文本。2) 人工审核生成的结果，验证图像和文本的质量，以及问题与图像的相关性。3) 如果生成结果不符合要求，则调整生成模型的提示词，重新生成。4) 重复以上步骤，直到生成足够数量的高质量视觉问题。最终，将所有问题组合成JMMMU-Pro基准。

**关键创新**：该论文的关键创新在于提出了Vibe基准构建方法，该方法结合了图像生成模型和人工验证，能够高效地构建高质量的多模态理解基准。与传统的人工标注方法相比，Vibe方法可以显著降低成本，并提高构建效率。此外，将问题图像和问题文本组合成单个图像，增加了模型理解的难度，更符合实际应用场景。

**关键设计**：在Vibe基准构建方法中，关键的设计包括：1) 选择合适的图像生成模型，如Nano Banana Pro，该模型需要具备生成高质量图像和嵌入清晰文本的能力。2) 设计有效的提示词，以控制生成图像和文本的内容和风格。3) 建立完善的人工审核流程，确保基准的质量。4) 针对不同的学科领域，设计不同的问题类型，以全面评估LMM的理解能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14620v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有的开源LMM在JMMMU-Pro基准上表现不佳，这突显了该基准的挑战性和重要性。具体来说，所有测试的LMM在JMMMU-Pro上的准确率都远低于人类水平，表明LMM在日语多模态理解方面仍有很大的提升空间。这一结果也验证了JMMMU-Pro作为评估LMM日语能力的重要工具的价值。

## 🎯 应用场景

JMMMU-Pro基准可用于评估和提升LMM在日语多模态理解方面的能力，尤其是在需要图像-文本综合理解的场景中，例如智能客服、教育辅助、视觉问答等。该基准的构建方法Vibe也可推广到其他语言和领域，加速多模态理解技术的发展。

## 📄 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

