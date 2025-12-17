---
layout: default
title: JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction

**arXiv**: [2512.14620v1](https://arxiv.org/abs/2512.14620) | [PDF](https://arxiv.org/pdf/2512.14620.pdf)

**作者**: Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, Kiyoharu Aizawa

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://mmmu-japanese-benchmark.github.io/JMMMU_Pro/

---

## 💡 一句话要点

**提出JMMMU-Pro基准和Vibe Benchmark Construction方法，以低成本构建高质量日语多学科多模态理解评估工具。**

**关键词**: `日语多模态理解` `基准构建` `图像生成模型` `视觉问答` `多学科评估` `开源LMM` `人工验证` `低成本构建`

## 📋 核心要点

1. 现有日语多模态基准在集成视觉-文本理解方面存在不足，难以全面评估LMM的日语能力。
2. 提出Vibe Benchmark Construction方法，结合图像生成模型和人工验证，低成本构建高质量视觉问题图像。
3. 实验显示开源LMM在JMMMU-Pro上表现显著困难，验证了基准的严格性和指导价值。

## 📝 摘要（中文）

本文介绍了JMMMU-Pro，一个基于图像的日语多学科多模态理解基准，以及Vibe Benchmark Construction，一种可扩展的构建方法。继从MMMU到MMMU-Pro的演进后，JMMMU-Pro通过将问题图像和问题文本组合成单一图像来扩展JMMMU，从而创建一个需要通过视觉感知进行集成视觉-文本理解的基准。为了构建JMMMU-Pro，我们提出了Vibe Benchmark Construction方法，其中图像生成模型（如Nano Banana Pro）生成候选视觉问题，人类验证输出并在必要时通过调整提示重新生成以确保质量。通过利用Nano Banana Pro的高度真实图像生成能力及其嵌入清晰日语文本的能力，我们以低成本构建了一个高质量的基准，覆盖广泛的背景和布局设计。实验结果表明，所有开源LMM在JMMMU-Pro上都面临显著困难，突显了JMMMU-Pro作为指导开源社区未来努力的重要基准。我们相信，JMMMU-Pro为评估LMM的日语能力提供了更严格的评估工具，而我们的Vibe Benchmark Construction也为未来基于图像的VQA基准开发提供了高效指南。

## 🔬 方法详解

论文的核心方法是Vibe Benchmark Construction，整体框架包括使用图像生成模型（如Nano Banana Pro）自动生成候选视觉问题图像，然后通过人工验证和调整提示进行质量控制和迭代优化。关键技术创新点在于利用Nano Banana Pro的高真实感图像生成和日语文本嵌入能力，结合人类反馈循环，实现高效、低成本的基准构建。与现有方法的主要区别在于，传统基准构建通常依赖手动设计或简单合成，而该方法通过生成式AI自动化部分流程，同时保持人类监督以确保多样性和准确性，从而扩展了基准的规模和覆盖范围。

## 📊 实验亮点

最重要的实验结果是所有开源LMM在JMMMU-Pro基准上都表现出显著困难，突显了该基准的挑战性和评估有效性，为未来LMM的日语能力改进提供了明确方向。

## 🎯 应用场景

该研究主要应用于评估大型多模态模型（LMM）的日语多模态理解能力，为开源社区提供严格的基准测试工具。潜在应用领域包括日语教育、跨语言AI系统开发、以及多模态人机交互，实际价值在于推动日语AI技术的标准化和性能提升。

## 📄 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

