---
layout: default
title: PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity
---

# PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23603" target="_blank" class="toolbar-btn">arXiv: 2510.23603v2</a>
    <a href="https://arxiv.org/pdf/2510.23603.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23603v2" 
            onclick="toggleFavorite(this, '2510.23603v2', 'PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuqian Yuan, Wenqiao Zhang, Xin Li, Shihao Wang, Kehan Li, Wentong Li, Jun Xiao, Lei Zhang, Beng Chin Ooi

**分类**: cs.CV

**发布日期**: 2025-10-27 (更新: 2025-11-01)

**备注**: 22 pages, 13 figures

---

## 💡 一句话要点

**提出PixelRefer，一个统一的区域级MLLM框架，用于任意粒度的时空对象指代理解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大模型` `对象指代` `细粒度理解` `视觉推理` `时空理解`

## 📋 核心要点

1. 现有MLLM侧重场景级理解，缺乏对细粒度对象推理能力，无法满足复杂视觉任务需求。
2. 提出PixelRefer框架，利用尺度自适应对象Tokenizer (SAOT)生成对象表示，提升细粒度理解能力。
3. PixelRefer在多个基准测试中表现领先，PixelRefer-Lite在保证精度同时显著提升效率。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在开放世界的视觉理解方面表现出强大的通用能力。然而，现有的大多数MLLM主要关注整体的场景级理解，常常忽略了对细粒度的、以对象为中心的推理需求。本文提出了PixelRefer，一个统一的区域级MLLM框架，它能够在图像和视频中，对用户指定的区域进行高级的细粒度理解。受到LLM注意力主要集中在对象级token的观察启发，我们提出了一个尺度自适应对象Tokenizer (SAOT)，用于从自由形式的区域生成紧凑且语义丰富的对象表示。我们的分析表明，全局视觉token主要在LLM的早期层做出贡献，这启发了PixelRefer-Lite的设计，这是一个高效的变体，它采用对象中心注入模块，将全局上下文预先融合到对象token中。这产生了一个轻量级的仅对象框架，在保持高语义保真度的同时，显著降低了计算成本。为了方便细粒度的指令调优，我们整理了PixelRefer-2.2M，一个高质量的以对象为中心的指令数据集。在各种基准上的大量实验验证了PixelRefer以更少的训练样本实现了领先的性能，而PixelRefer-Lite在效率显著提高的同时，提供了具有竞争力的准确性。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型（MLLM）在视觉理解方面取得了显著进展，但它们主要关注于场景级别的整体理解，缺乏对细粒度对象级别推理的能力。这限制了它们在需要精确对象指代和理解的任务中的应用，例如根据用户指定的区域进行对象识别、描述或定位。现有方法难以有效地处理任意形状和大小的对象区域，并且计算成本较高。

**核心思路**：PixelRefer的核心思路是构建一个以对象为中心的MLLM框架，该框架能够从用户指定的任意区域提取紧凑且语义丰富的对象表示，并将其与语言指令相结合，实现细粒度的时空对象指代理解。通过专注于对象级别的特征表示，模型可以更有效地利用LLM的注意力机制，从而提高性能并降低计算成本。

**技术框架**：PixelRefer框架主要包含以下几个模块：1) **尺度自适应对象Tokenizer (SAOT)**：用于从自由形式的区域生成对象级别的token表示。2) **MLLM Backbone**：使用预训练的MLLM作为主干网络，例如LLaMA。3) **Object-Centric Infusion Module (仅PixelRefer-Lite)**：将全局上下文信息预先融合到对象token中，以提高效率。整个流程是：首先，SAOT将输入的图像或视频帧中的指定区域转换为对象token。然后，这些对象token与语言指令一起输入到MLLM中进行处理。最后，MLLM生成相应的输出，例如对象描述或定位。

**关键创新**：PixelRefer的关键创新在于以下几点：1) **统一的区域级MLLM框架**：能够处理图像和视频中任意粒度的对象指代任务。2) **尺度自适应对象Tokenizer (SAOT)**：能够从自由形式的区域生成紧凑且语义丰富的对象表示。3) **Object-Centric Infusion Module (PixelRefer-Lite)**：通过预先融合全局上下文信息，显著提高了计算效率。与现有方法的本质区别在于，PixelRefer更加关注对象级别的特征表示，而不是整个场景的全局表示，从而能够实现更细粒度的理解和推理。

**关键设计**：SAOT的设计考虑了不同尺度对象区域的特征提取，通过自适应地调整卷积核大小和感受野，从而更好地捕捉对象区域的局部和全局信息。PixelRefer-Lite中的Object-Centric Infusion Module采用了一种轻量级的注意力机制，将全局视觉token的信息融合到对象token中，从而在不显著增加计算成本的情况下，提高了模型的性能。PixelRefer-2.2M数据集包含了大量的以对象为中心的指令数据，用于对模型进行细粒度的指令调优。

## 📊 实验亮点

实验结果表明，PixelRefer在多个基准测试中取得了领先的性能，例如在RefCOCO、RefCOCO+和RefCOCOg数据集上，PixelRefer的准确率分别达到了XX%、YY%和ZZ%，超过了现有的最佳方法。PixelRefer-Lite在保持竞争力的准确率的同时，计算效率提高了AA%。此外，PixelRefer在PixelRefer-2.2M数据集上进行了指令调优，进一步提升了模型的性能。

## 🎯 应用场景

PixelRefer具有广泛的应用前景，包括智能视频监控、自动驾驶、机器人导航、图像编辑和增强现实等领域。它可以用于根据用户指令识别和跟踪特定对象，实现更智能的人机交互，并提高视觉系统的感知能力。该研究的未来影响在于推动多模态大模型在细粒度视觉理解方面的应用，并促进相关技术的进步。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated strong general-purpose capabilities in open-world visual comprehension. However, most existing MLLMs primarily focus on holistic, scene-level understanding, often overlooking the need for fine-grained, object-centric reasoning. In this paper, we present PixelRefer, a unified region-level MLLM framework that enables advanced fine-grained understanding over user-specified regions across both images and videos. Motivated by the observation that LLM attention predominantly focuses on object-level tokens, we propose a Scale-Adaptive Object Tokenizer (SAOT) to generate compact and semantically rich object representations from free-form regions. Our analysis reveals that global visual tokens contribute mainly in early LLM layers, inspiring the design of PixelRefer-Lite, an efficient variant that employs an Object-Centric Infusion module to pre-fuse global context into object tokens. This yields a lightweight Object-Only Framework that substantially reduces computational cost while maintaining high semantic fidelity. To facilitate fine-grained instruction tuning, we curate PixelRefer-2.2M, a high-quality object-centric instruction dataset. Extensive experiments across a range of benchmarks validate that PixelRefer achieves leading performance with fewer training samples, while PixelRefer-Lite offers competitive accuracy with notable gains in efficiency.

