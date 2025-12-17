---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

**arXiv**: [2512.14008v1](https://arxiv.org/abs/2512.14008) | [PDF](https://arxiv.org/pdf/2512.14008.pdf)

**作者**: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 18 pages (12 pages for the main paper and 6 pages for the appendix), 9 figures

---

## 💡 一句话要点

**Sparse-LaViDa：通过稀疏化采样加速多模态离散扩散语言模型**

🎯 **匹配领域**: **动作生成与物理动画 (Animation & Physics)**

**关键词**: `多模态扩散模型` `稀疏采样` `模型加速` `图像生成` `图像编辑`

## 📋 核心要点

1. MDM推理速度受限于重复处理冗余掩码token，效率有待提升。
2. Sparse-LaViDa动态截断不必要的掩码token，并用register token保持生成质量。
3. 通过专门设计的注意力掩码，保证训练与推理过程的一致性，提升模型性能。

## 📝 摘要（中文）

本文提出了一种名为Sparse-LaViDa的新建模框架，旨在加速Masked Discrete Diffusion Models (MDMs)的推理过程。MDMs在图像理解、生成和编辑等多种模态任务中表现出色，但由于需要在每个采样步骤中重复处理冗余的掩码token，导致推理速度较慢。Sparse-LaViDa通过在每个推理步骤中动态截断不必要的掩码token来解决这个问题。为了保持生成质量，引入了专门的register token，作为被截断token的紧凑表示。此外，为了确保训练和推理之间的一致性，设计了一种专门的注意力掩码，在训练期间忠实地匹配截断的采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理等多种任务中实现了高达2倍的加速，同时保持了生成质量。

## 🔬 方法详解

**问题定义**：现有的Masked Discrete Diffusion Models (MDMs)在多模态任务中表现优异，但推理速度较慢。主要原因是需要在每个采样步骤中重复处理大量的掩码token，这些token在后续的迭代中可能变得冗余，从而浪费计算资源。因此，如何减少冗余计算，加速MDM的推理过程是一个关键问题。

**核心思路**：Sparse-LaViDa的核心思路是在推理过程中动态地截断不必要的掩码token，从而减少计算量。为了避免截断token导致的信息损失，引入了register token作为被截断token的紧凑表示。通过这种方式，模型可以在加速推理的同时，尽可能地保持生成质量。

**技术框架**：Sparse-LaViDa建立在现有的LaViDa-O模型之上，主要包含以下几个关键模块：1) Masked Discrete Diffusion Model (MDM)：负责生成离散token序列。2) 动态截断模块：根据一定的策略，在每个采样步骤中截断不必要的掩码token。3) Register Token：用于存储被截断token的信息，保持生成质量。4) 注意力机制：用于token之间的信息交互。5) 特殊设计的注意力掩码：保证训练和推理过程的一致性。

**关键创新**：Sparse-LaViDa的关键创新在于动态截断策略和register token的设计。动态截断策略能够有效地减少冗余计算，而register token则能够尽可能地保留被截断token的信息，从而保证生成质量。此外，特殊设计的注意力掩码保证了训练和推理过程的一致性，避免了模型性能下降。

**关键设计**：在动态截断策略方面，论文可能采用了一种基于注意力权重的截断方法，即优先截断注意力权重较低的token。Register token的设计可能采用了类似于pooling的方法，将多个被截断token的信息压缩到一个register token中。注意力掩码的设计需要保证在训练过程中，模型能够学习到如何利用register token的信息，从而在推理过程中能够正确地进行生成。

## 📊 实验亮点

Sparse-LaViDa在多种任务中实现了显著的加速效果。在文本到图像生成、图像编辑和数学推理等任务中，Sparse-LaViDa实现了高达2倍的加速，同时保持了与LaViDa-O相当的生成质量。这些实验结果表明，Sparse-LaViDa是一种有效的加速MDM推理的方法。

## 🎯 应用场景

Sparse-LaViDa具有广泛的应用前景，包括文本到图像生成、图像编辑、数学推理等。该方法可以应用于需要快速生成或编辑图像的场景，例如在线图像生成服务、实时图像编辑工具等。此外，该方法还可以应用于机器人领域，例如机器人可以通过Sparse-LaViDa快速生成视觉指令，从而完成复杂的任务。未来，Sparse-LaViDa有望成为多模态生成领域的重要技术。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

