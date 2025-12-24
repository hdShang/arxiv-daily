---
layout: default
title: "Rolling Forcing: Autoregressive Long Video Diffusion in Real Time"
---

# Rolling Forcing: Autoregressive Long Video Diffusion in Real Time

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25161" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25161v1</a>
  <a href="https://arxiv.org/pdf/2509.25161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25161v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25161v1', 'Rolling Forcing: Autoregressive Long Video Diffusion in Real Time')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kunhao Liu, Wenbo Hu, Jiale Xu, Ying Shan, Shijian Lu

**分类**: cs.CV

**发布日期**: 2025-09-29

**备注**: Project page: https://kunhao-liu.github.io/Rolling_Forcing_Webpage/

---

## 💡 一句话要点

**提出Rolling Forcing，实现实时自回归长视频扩散生成，显著降低误差累积。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `流式视频生成` `长视频生成` `扩散模型` `自回归模型` `误差累积` `注意力机制` `实时生成` `联合去噪`

## 📋 核心要点

1. 现有流式视频生成方法存在误差累积问题，导致长视频生成质量下降，难以满足实时性要求。
2. Rolling Forcing通过联合去噪、注意力汇聚和高效训练算法，抑制误差累积，提升长期一致性。
3. 实验表明，Rolling Forcing能够在单GPU上实时生成多分钟视频，显著降低误差累积。

## 📝 摘要（中文）

流式视频生成是交互式世界模型和神经游戏引擎中的一个基本组成部分，旨在生成高质量、低延迟和时间上连贯的长视频流。然而，现有的大多数工作都存在严重的误差累积问题，这通常会显著降低生成视频流的质量。本文设计了一种名为Rolling Forcing的新型视频生成技术，该技术能够以最小的误差累积实现流式长视频生成。Rolling Forcing包含三个创新设计。首先，它采用联合去噪方案，同时对多个具有渐进噪声水平的帧进行去噪，从而放松了相邻帧之间的严格因果关系，有效抑制了误差增长。其次，引入了注意力汇聚机制，将初始帧的关键值状态作为全局上下文锚点，增强了长期全局一致性。第三，设计了一种高效的训练算法，能够在很大程度上扩展去噪窗口上进行少步蒸馏，该算法在非重叠窗口上运行，并减轻了以自生成历史为条件的暴露偏差。大量实验表明，Rolling Forcing能够在单个GPU上实现多分钟视频的实时流式生成，并显著减少误差累积。

## 🔬 方法详解

**问题定义**：论文旨在解决流式视频生成中长期误差累积的问题。现有方法通常逐帧迭代生成，导致误差随着时间推移不断累积，最终影响生成视频的质量和连贯性，难以生成高质量的长视频。

**核心思路**：Rolling Forcing的核心思路是通过联合去噪多个帧来放松相邻帧之间的严格因果关系，从而抑制误差增长。同时，利用注意力汇聚机制保持全局上下文信息，增强长期一致性。此外，设计高效的训练算法，减轻暴露偏差。

**技术框架**：Rolling Forcing的整体框架包括以下几个主要部分：1) 联合去噪模块，同时处理多个帧，并采用逐渐增加的噪声水平；2) 注意力汇聚模块，将初始帧的关键值状态作为全局上下文锚点；3) 高效训练算法，在非重叠窗口上进行少步蒸馏，减轻暴露偏差。

**关键创新**：Rolling Forcing的关键创新在于：1) 联合去噪方案，打破了逐帧生成的严格因果关系，有效抑制了误差累积；2) 注意力汇聚机制，增强了长期全局一致性；3) 高效的训练算法，能够在扩展的去噪窗口上进行少步蒸馏，减轻了暴露偏差。与现有方法相比，Rolling Forcing能够生成更长、更连贯的视频，且误差累积更小。

**关键设计**：联合去噪模块采用扩散模型，通过逐步去噪的方式生成视频帧。注意力汇聚模块使用Transformer架构，将初始帧的信息融入到后续帧的生成过程中。训练算法采用非重叠窗口，并使用蒸馏损失来加速训练。具体的参数设置和网络结构细节在论文中有详细描述，但摘要中未明确给出具体数值。

## 📊 实验亮点

实验结果表明，Rolling Forcing能够在单个GPU上实现多分钟视频的实时流式生成，并显著减少误差累积。具体性能数据和对比基线在摘要中未给出，但强调了其在实时性和误差控制方面的优势。

## 🎯 应用场景

Rolling Forcing技术可应用于交互式世界模型、神经游戏引擎、虚拟现实、增强现实等领域。它能够生成高质量、低延迟、时间连贯的长视频流，为用户提供更沉浸式的体验。该技术还有潜力应用于视频编辑、内容创作等领域，提高生产效率和创作质量。

## 📄 摘要（原文）

> Streaming video generation, as one fundamental component in interactive world models and neural game engines, aims to generate high-quality, low-latency, and temporally coherent long video streams. However, most existing work suffers from severe error accumulation that often significantly degrades the generated stream videos over long horizons. We design Rolling Forcing, a novel video generation technique that enables streaming long videos with minimal error accumulation. Rolling Forcing comes with three novel designs. First, instead of iteratively sampling individual frames, which accelerates error propagation, we design a joint denoising scheme that simultaneously denoises multiple frames with progressively increasing noise levels. This design relaxes the strict causality across adjacent frames, effectively suppressing error growth. Second, we introduce the attention sink mechanism into the long-horizon stream video generation task, which allows the model to keep key value states of initial frames as a global context anchor and thereby enhances long-term global consistency. Third, we design an efficient training algorithm that enables few-step distillation over largely extended denoising windows. This algorithm operates on non-overlapping windows and mitigates exposure bias conditioned on self-generated histories. Extensive experiments show that Rolling Forcing enables real-time streaming generation of multi-minute videos on a single GPU, with substantially reduced error accumulation.

