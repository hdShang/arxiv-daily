---
layout: default
title: JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14620" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14620v1</a>
  <a href="https://arxiv.org/pdf/2512.14620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14620v1" onclick="toggleFavorite(this, '2512.14620v1', 'JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction')" title="添加到收藏夹">☆ 收藏</button>
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

**关键词**: `多模态理解` `视觉问答` `日语` `基准构建` `图像生成模型` `语言模型` `人工智能`

## 📋 核心要点

1. 现有LMM在日语多学科多模态理解方面存在不足，缺乏高质量的日语视觉问答基准。
2. 提出Vibe基准构建方法，利用图像生成模型和人工验证，高效构建高质量的JMMMU-Pro基准。
3. 实验表明，开源LMM在JMMMU-Pro上表现不佳，验证了该基准的挑战性和重要性。

## 📝 摘要（中文）

本文介绍了JMMMU-Pro，一个基于图像的日语多学科多模态理解基准，以及Vibe基准构建方法，一种可扩展的构建方法。JMMMU-Pro延续了从MMMU到MMMU-Pro的演进，通过将问题图像和问题文本组合成单个图像来扩展JMMMU，从而创建了一个需要通过视觉感知进行综合视觉-文本理解的基准。为了构建JMMMU-Pro，我们提出了Vibe基准构建方法，该方法利用图像生成模型（例如Nano Banana Pro）生成候选视觉问题，然后由人工验证输出，并在必要时使用调整后的提示重新生成，以确保质量。通过利用Nano Banana Pro的高度逼真的图像生成能力及其嵌入清晰日语文本的能力，我们以低成本构建了一个高质量的基准，涵盖了广泛的背景和布局设计。实验结果表明，所有开源LMM在JMMMU-Pro上都表现不佳，这突显了JMMMU-Pro作为指导开源社区未来工作的重要基准。我们相信JMMMU-Pro为评估LMM的日语能力提供了一个更严格的评估工具，并且我们的Vibe基准构建方法也为未来基于图像的VQA基准的开发提供了有效的指导。

## 🔬 方法详解

**问题定义**：论文旨在解决现有日语多模态理解基准的不足，特别是缺乏高质量、具有挑战性的图像-文本融合理解的基准。现有方法要么数据量不足，要么质量不高，难以有效评估LMM在日语环境下的视觉-文本综合理解能力。

**核心思路**：论文的核心思路是利用图像生成模型（如Nano Banana Pro）自动生成候选的视觉问答对，然后通过人工验证和修正来保证数据的质量。这种方法可以显著降低构建大规模高质量基准的成本和时间。

**技术框架**：Vibe基准构建方法主要包含以下几个阶段：1) 使用图像生成模型（Nano Banana Pro）生成候选视觉问题，该模型能够生成包含清晰日语文本的逼真图像；2) 人工验证生成的图像和问题，判断其质量和相关性；3) 如果图像或问题质量不佳，则调整生成模型的提示词，重新生成；4) 重复上述过程，直到获得足够数量的高质量视觉问答对。最终构建成JMMMU-Pro基准。

**关键创新**：该方法最重要的创新在于利用图像生成模型来自动化基准构建过程，并结合人工验证来保证数据质量。这种方法相比于传统的人工标注方法，可以显著提高效率并降低成本。此外，JMMMU-Pro基准本身也是一个创新，它专注于日语多学科多模态理解，更具挑战性。

**关键设计**：Vibe方法的关键设计包括：1) 选择合适的图像生成模型，要求其能够生成包含清晰日语文本的逼真图像；2) 设计有效的提示词，引导生成模型生成多样化的视觉问题；3) 制定清晰的质量评估标准，指导人工验证过程；4) 迭代优化提示词和评估标准，不断提高数据质量。

## 📊 实验亮点

实验结果表明，现有的开源LMM在JMMMU-Pro基准上的表现远低于预期，这表明JMMMU-Pro是一个具有挑战性的基准，可以有效区分不同LMM的日语多模态理解能力。该基准的发布将促进开源社区在该领域的研究。

## 🎯 应用场景

该研究成果可应用于提升LMM在日语环境下的多模态理解能力，例如智能客服、教育辅助、信息检索等领域。高质量的JMMMU-Pro基准可以促进相关算法的研发，推动日语LMM的实际应用。

## 📄 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

