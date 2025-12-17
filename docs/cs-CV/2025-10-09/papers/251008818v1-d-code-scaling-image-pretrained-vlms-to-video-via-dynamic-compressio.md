---
layout: default
title: D-CoDe: Scaling Image-Pretrained VLMs to Video via Dynamic Compression and Question Decomposition
---

# D-CoDe: Scaling Image-Pretrained VLMs to Video via Dynamic Compression and Question Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08818" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08818v1</a>
  <a href="https://arxiv.org/pdf/2510.08818.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08818v1" onclick="toggleFavorite(this, '2510.08818v1', 'D-CoDe: Scaling Image-Pretrained VLMs to Video via Dynamic Compression and Question Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyang Huang, Yizhou Wang, Yun Fu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-09

**备注**: This paper has been accepted to EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/hukcc/D-CoDe)

---

## 💡 一句话要点

**D-CoDe：通过动态压缩和问题分解，将图像预训练的VLM扩展到视频领域**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `视觉语言模型` `动态压缩` `问题分解` `长视频处理` `训练自由` `自适应框架`

## 📋 核心要点

1. 图像预训练的VLM扩展到视频领域面临感知瓶颈和token过载的挑战，限制了模型性能。
2. D-CoDe通过动态压缩自适应选择关键帧并聚合空间token，同时利用问题分解将复杂问题拆解为子问题。
3. 实验表明，D-CoDe在多个视频理解基准测试中表现出色，尤其在长视频任务上展现了巨大潜力。

## 📝 摘要（中文）

本文提出了一种名为D-CoDe的训练自由框架，旨在将图像预训练的视觉语言模型（VLM）有效扩展到视频领域。现有方法在处理密集和时序长的视频输入时面临感知瓶颈和token过载的挑战。D-CoDe通过动态压缩缓解感知瓶颈，自适应地选择代表性帧，并进行内容感知的空间token聚合，从而减少冗余并保留信息内容。同时，通过问题分解缓解token过载，将原始查询分解为子问题，引导模型关注视频的不同方面，实现更全面的理解。实验结果表明，D-CoDe有效地提升了各种基准测试中的视频理解能力。在具有挑战性的长视频基准测试中表现出色，突显了D-CoDe在处理复杂视频语言任务方面的潜力。

## 🔬 方法详解

**问题定义**：现有的视频语言模型（Vid-LLM）构建方法通常基于图像预训练的视觉语言模型（VLM）。然而，直接将图像VLM应用于视频时，由于视频数据量大、时序长，导致模型面临两个主要问题：一是感知瓶颈，即模型难以从大量帧中提取关键信息；二是token过载，即过多的视觉token超过了模型的处理能力，影响理解效果。

**核心思路**：D-CoDe的核心思路是通过动态压缩和问题分解来解决上述问题。动态压缩旨在减少输入视频的冗余信息，保留关键帧和重要区域，从而缓解感知瓶颈。问题分解则将复杂的视频理解问题分解为多个子问题，引导模型逐步理解视频内容，减轻token过载的影响。

**技术框架**：D-CoDe框架主要包含两个模块：动态压缩模块和问题分解模块。动态压缩模块首先对视频帧进行重要性评估，选择代表性帧。然后，对选定的帧进行内容感知的空间token聚合，减少冗余信息。问题分解模块将原始问题分解为多个子问题，每个子问题关注视频的不同方面。最后，模型根据子问题的答案综合理解视频内容。

**关键创新**：D-CoDe的关键创新在于其训练自由的自适应框架。与需要大量训练数据的传统方法不同，D-CoDe无需额外训练即可应用于现有的图像预训练VLM。动态压缩模块和问题分解模块的设计能够有效地缓解感知瓶颈和token过载问题，提升模型在视频理解任务上的性能。

**关键设计**：动态压缩模块使用注意力机制来评估视频帧的重要性，并选择top-k个帧。空间token聚合采用内容感知的池化操作，根据token的重要性进行加权平均。问题分解模块使用预定义的模板将原始问题分解为多个子问题。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

D-CoDe在多个视频理解基准测试中取得了显著的性能提升。尤其在长视频基准测试中，D-CoDe表现出强大的处理能力，证明了其在复杂视频语言任务中的潜力。实验结果表明，D-CoDe能够有效地缓解感知瓶颈和token过载问题，提升视频理解的准确性和效率。

## 🎯 应用场景

D-CoDe具有广泛的应用前景，可用于视频内容理解、智能监控、视频检索、视频摘要生成等领域。该方法能够提升视频语言模型在处理长视频和复杂问题时的性能，为开发更智能的视频分析系统提供技术支持，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> Video large language models (Vid-LLMs), which excel in diverse video-language tasks, can be effectively constructed by adapting image-pretrained vision-language models (VLMs). However, this adaptation remains challenging, as it requires processing dense and temporally extended visual inputs that exceed the capacity of image-based models. This paper identifies the perception bottleneck and token overload as key challenges in extending image-based VLMs to the video domain. To address these issues, we propose D-CoDe, a training-free adaptation framework that incorporates dynamic compression and question decomposition. Specifically, dynamic compression alleviates the perception bottleneck through adaptive selection of representative frames and content-aware aggregation of spatial tokens, thereby reducing redundancy while preserving informative content. In parallel, question decomposition mitigates token overload by reformulating the original query into sub-questions, guiding the model to focus on distinct aspects of the video and enabling more comprehensive understanding. Experiments demonstrate that D-CoDe effectively improves video understanding across various benchmarks. Furthermore, strong performance on the challenging long-video benchmark highlights the potential of D-CoDe in handling complex video-language tasks. Code is available at https://github.com/hukcc/D-CoDe.

