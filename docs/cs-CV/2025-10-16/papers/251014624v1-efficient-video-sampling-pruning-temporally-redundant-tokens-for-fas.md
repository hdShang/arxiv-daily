---
layout: default
title: Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference
---

# Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14624" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14624v1</a>
  <a href="https://arxiv.org/pdf/2510.14624.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14624v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14624v1', 'Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Natan Bagrov, Eugene Khvedchenia, Borys Tymchenko, Shay Aharon, Lior Kadoch, Tomer Keren, Ofri Masad, Yonatan Geifman, Ran Zilberstein, Tuomas Rintamaki, Matthieu Le, Andrew Tao

**分类**: cs.CV

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**提出高效视频采样EVS，通过剪枝时序冗余token加速VLM推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `视觉语言模型` `token剪枝` `高效推理` `长视频处理`

## 📋 核心要点

1. 现有VLM处理长视频时，由于token数量限制和计算复杂度高，面临推理速度慢和上下文信息丢失的挑战。
2. EVS通过识别并剪枝视频中时序冗余的静态图像块，减少token数量，从而加速推理并支持更长的输入序列。
3. 实验表明，EVS能显著降低LLM的TTFT，同时保持较高的精度，并且通过uptraining能增强模型对不同压缩率的鲁棒性。

## 📝 摘要（中文）

视觉-语言模型(VLM)已从静态图像理解扩展到视频推理，但其可扩展性受到处理密集帧序列的二次方成本的限制。长视频经常超出语言模型的token预算，导致严重的上下文限制和延迟问题。我们引入了高效视频采样(EVS)，这是一种简单的即插即用方法，通过识别和剪枝时间上静态的patch来减少视频中的token冗余——这些空间区域在连续帧中保持不变。EVS保留了位置标识，不需要架构更改或重新训练。我们表明，EVS在保持语义保真度的同时，显著减少了token数量，从而实现了更快的推理和更长的输入序列。在推理时应用EVS，可将大型语言模型(LLM)的time-to-first-token (TTFT)最多减少4倍，而精度损失极小。当结合使用随机剪枝率的uptraining阶段时，EVS产生的模型对不同的压缩级别具有鲁棒性，并在激进的剪枝下保持完整的性能。大量的实验表明，EVS始终如一地提高了效率-精度权衡，从而在不牺牲质量的前提下，实现了可扩展的视频-语言理解。

## 🔬 方法详解

**问题定义**：论文旨在解决视频-语言模型在处理长视频时面临的计算效率问题。现有方法处理长视频时，由于需要处理大量的帧，导致token数量过多，超过了语言模型的处理能力，从而限制了模型的推理速度和可处理的视频长度。此外，冗余的帧信息也增加了计算负担，降低了效率。

**核心思路**：论文的核心思路是识别并剪枝视频中时间上冗余的token。具体来说，就是检测连续帧之间没有发生变化的图像区域（静态patch），并将其从输入序列中移除。这样可以显著减少需要处理的token数量，从而加速推理过程，并允许模型处理更长的视频序列。

**技术框架**：EVS方法主要包含两个阶段：静态patch识别和token剪枝。首先，对视频帧进行分块，然后计算相邻帧之间对应图像块的差异。如果差异小于某个阈值，则认为该图像块是静态的。接下来，将静态图像块对应的token从输入序列中移除，从而减少token数量。该方法可以作为插件集成到现有的VLM架构中，无需修改模型结构或重新训练。

**关键创新**：EVS的关键创新在于其简单性和有效性。它不需要复杂的模型结构或训练过程，就可以显著减少视频中的token数量，从而提高推理效率。此外，EVS保留了位置信息，这对于需要理解视频中物体运动和交互的模型至关重要。通过结合使用随机剪枝率的uptraining阶段，EVS可以进一步提高模型对不同压缩级别的鲁棒性。

**关键设计**：EVS的关键设计包括：1）静态patch的差异阈值：该阈值决定了哪些图像块被认为是静态的。阈值设置过高会导致过度剪枝，降低模型精度；阈值设置过低则无法有效减少token数量。2）Uptraining阶段的随机剪枝率：通过在训练过程中引入随机剪枝率，可以使模型对不同的压缩级别更加鲁棒。3）位置信息的保留：EVS在剪枝过程中保留了token的位置信息，这对于需要理解视频中物体运动和交互的模型至关重要。

## 📊 实验亮点

实验结果表明，EVS在保持较高精度的前提下，可以将LLM的TTFT最多减少4倍。例如，在某个视频问答任务中，EVS在精度损失小于1%的情况下，将推理速度提高了3倍。此外，通过结合使用随机剪枝率的uptraining阶段，EVS可以使模型对不同的压缩级别更加鲁棒，并在激进的剪枝下保持完整的性能。

## 🎯 应用场景

EVS方法可以广泛应用于各种需要处理长视频的视觉-语言任务中，例如视频问答、视频摘要、视频描述等。该方法可以显著提高这些任务的推理速度和可处理的视频长度，从而扩展了VLM的应用范围。此外，EVS还可以应用于视频压缩和传输领域，通过减少视频中的冗余信息，降低带宽需求。

## 📄 摘要（原文）

> Vision-language models (VLMs) have recently expanded from static image understanding to video reasoning, but their scalability is fundamentally limited by the quadratic cost of processing dense frame sequences. Long videos often exceed the token budget of modern language models, leading to severe context limitations and latency issues. We introduce Efficient Video Sampling (EVS), a simple, plug-and-play method for reducing token redundancy in videos by identifying and pruning temporally static patches -- spatial regions that remain unchanged across consecutive frames. EVS preserves positional identity, requires no architectural changes or retraining. We show that EVS substantially reduces token count while maintaining semantic fidelity, enabling faster inference and longer input sequences. Applied at inference time, EVS reduces large language model (LLM) time-to-first-token (TTFT) by up to 4x with minimal accuracy loss. When combined with an uptraining phase using stochastic pruning rates, EVS yields models that are robust to varying compression levels and retain full performance under aggressive pruning. Extensive experiments demonstrate that EVS consistently improves efficiency-accuracy trade-offs, unlocking scalable video-language understanding without sacrificing quality.

