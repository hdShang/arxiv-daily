---
layout: default
title: LongCat-Video Technical Report
---

# LongCat-Video Technical Report

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22200" target="_blank" class="toolbar-btn">arXiv: 2510.22200v2</a>
    <a href="https://arxiv.org/pdf/2510.22200.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22200v2" 
            onclick="toggleFavorite(this, '2510.22200v2', 'LongCat-Video Technical Report')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Meituan LongCat Team, Xunliang Cai, Qilong Huang, Zhuoliang Kang, Hongyu Li, Shijun Liang, Liya Ma, Siyu Ren, Xiaoming Wei, Rixu Xie, Tong Zhang

**分类**: cs.CV

**发布日期**: 2025-10-25 (更新: 2025-10-28)

---

## 💡 一句话要点

**LongCat-Video：基于扩散Transformer的高效长视频生成模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长视频生成` `扩散Transformer` `视频延续` `粗到精生成` `块稀疏注意力` `多任务学习` `强化学习` `视频生成`

## 📋 核心要点

1. 现有视频生成模型难以兼顾长时序一致性和高效推理，限制了其在实际应用中的潜力。
2. LongCat-Video采用扩散Transformer架构，并结合粗到精的生成策略，实现高效高质量的长视频生成。
3. 通过多奖励强化学习训练，LongCat-Video在多个视频生成任务上取得了与领先模型相当的性能。

## 📝 摘要（中文）

LongCat-Video是一个拥有136亿参数的基础视频生成模型，在多个视频生成任务中表现出色，尤其擅长高效、高质量的长视频生成，代表着我们迈向世界模型的第一步。其关键特性包括：统一的多任务架构，基于扩散Transformer（DiT）框架，支持文本到视频、图像到视频和视频延续任务；长视频生成能力，通过在视频延续任务上的预训练，能够保持数分钟长视频生成的高质量和时间一致性；高效推理，采用时空粗到精的生成策略，在几分钟内生成720p、30fps的视频，块稀疏注意力进一步提高了效率，尤其是在高分辨率下；以及通过多奖励RLHF训练实现的强大性能，与最新的闭源和领先的开源模型相媲美。代码和模型权重已公开。

## 🔬 方法详解

**问题定义**：现有视频生成模型在生成长视频时，往往面临时间一致性难以保持和计算复杂度过高的问题。尤其是在高分辨率下，计算效率成为瓶颈。此外，很多模型只能处理单一任务，缺乏通用性。

**核心思路**：LongCat-Video的核心思路是利用扩散Transformer (DiT) 的强大生成能力，并通过粗到精的生成策略以及块稀疏注意力机制来提升效率。通过在视频延续任务上的预训练，增强模型对时间序列的建模能力，从而保证长视频的时间一致性。多奖励强化学习则用于提升生成视频的质量和多样性。

**技术框架**：LongCat-Video基于扩散Transformer (DiT) 框架，采用统一的架构支持文本到视频、图像到视频和视频延续等多种任务。整体流程包括：首先，通过粗糙的时空分辨率生成视频的整体结构；然后，逐步细化时空分辨率，生成高清晰度的视频细节。块稀疏注意力机制用于降低高分辨率下的计算复杂度。

**关键创新**：LongCat-Video的关键创新在于：1) 统一的多任务架构，能够处理多种视频生成任务；2) 粗到精的时空生成策略，显著提升了长视频生成的效率；3) 块稀疏注意力机制，进一步降低了高分辨率下的计算复杂度；4) 多奖励强化学习训练，提升了生成视频的质量和多样性。

**关键设计**：LongCat-Video采用扩散Transformer作为核心生成模块，并针对视频生成任务进行了优化。粗到精的生成策略具体实现为：首先生成低分辨率、低帧率的视频，然后逐步提升分辨率和帧率。块稀疏注意力机制通过只关注重要的像素块来降低计算量。多奖励强化学习训练则通过设计多个奖励函数来引导模型生成高质量、多样化的视频。

## 📊 实验亮点

LongCat-Video通过在视频延续任务上的预训练，能够生成数分钟的高质量、时间一致的视频。采用粗到精的生成策略和块稀疏注意力机制，能够在几分钟内生成720p、30fps的视频。通过多奖励RLHF训练，LongCat-Video在多个视频生成任务上取得了与最新的闭源和领先的开源模型相媲美的性能，具体性能数据未知。

## 🎯 应用场景

LongCat-Video在内容创作、游戏开发、虚拟现实等领域具有广泛的应用前景。它可以用于生成电影片段、游戏场景、虚拟人物动画等。其高效的推理能力使得实时视频生成成为可能，为互动式娱乐和虚拟现实体验提供了新的可能性。未来，LongCat-Video有望成为构建通用世界模型的重要组成部分。

## 📄 摘要（原文）

> Video generation is a critical pathway toward world models, with efficient long video inference as a key capability. Toward this end, we introduce LongCat-Video, a foundational video generation model with 13.6B parameters, delivering strong performance across multiple video generation tasks. It particularly excels in efficient and high-quality long video generation, representing our first step toward world models. Key features include: Unified architecture for multiple tasks: Built on the Diffusion Transformer (DiT) framework, LongCat-Video supports Text-to-Video, Image-to-Video, and Video-Continuation tasks with a single model; Long video generation: Pretraining on Video-Continuation tasks enables LongCat-Video to maintain high quality and temporal coherence in the generation of minutes-long videos; Efficient inference: LongCat-Video generates 720p, 30fps videos within minutes by employing a coarse-to-fine generation strategy along both the temporal and spatial axes. Block Sparse Attention further enhances efficiency, particularly at high resolutions; Strong performance with multi-reward RLHF: Multi-reward RLHF training enables LongCat-Video to achieve performance on par with the latest closed-source and leading open-source models. Code and model weights are publicly available to accelerate progress in the field.

