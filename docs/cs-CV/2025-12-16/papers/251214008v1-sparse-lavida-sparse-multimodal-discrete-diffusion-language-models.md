---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14008" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14008v1</a>
  <a href="https://arxiv.org/pdf/2512.14008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14008v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14008v1', 'Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 18 pages (12 pages for the main paper and 6 pages for the appendix), 9 figures

---

## 💡 一句话要点

**Sparse-LaViDa：通过稀疏化采样加速多模态离散扩散语言模型**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `离散扩散模型` `模型加速` `稀疏化` `文本到图像生成`

## 📋 核心要点

1. 掩码离散扩散模型(MDM)在多模态任务中表现出色，但推理速度因重复处理冗余掩码token而受限。
2. Sparse-LaViDa通过动态截断不必要的掩码token来加速MDM采样，并引入寄存器token保持生成质量。
3. 实验表明，Sparse-LaViDa在多种任务中实现了高达2倍的加速，同时保持了与LaViDa-O相当的生成质量。

## 📝 摘要（中文）

本文提出Sparse-LaViDa，一种新颖的建模框架，旨在动态截断每个推理步骤中不必要的掩码token，从而加速掩码离散扩散模型(MDM)的采样过程。为了保持生成质量，引入了专门的寄存器token，作为被截断token的紧凑表示。此外，为了确保训练和推理之间的一致性，设计了一种专门的注意力掩码，在训练期间忠实地匹配截断采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在包括文本到图像生成、图像编辑和数学推理等多种任务中实现了高达2倍的加速，同时保持了生成质量。

## 🔬 方法详解

**问题定义**：现有的掩码离散扩散模型（MDMs）在多模态任务中取得了显著成果，但其推理速度受到限制。主要原因是需要在每个采样步骤中重复处理大量的掩码token，这些token在后续步骤中可能变得不必要，从而造成计算资源的浪费。因此，如何减少冗余计算，加速MDM的推理过程是一个关键问题。

**核心思路**：Sparse-LaViDa的核心思路是在推理过程中动态地截断那些不必要的掩码token，从而减少计算量。为了弥补截断token可能带来的信息损失，引入了“寄存器token”作为被截断token的紧凑表示，以保留关键信息。通过这种方式，可以在加速推理的同时，尽可能地保持生成质量。

**技术框架**：Sparse-LaViDa建立在现有的MDM框架（具体为LaViDa-O）之上。其主要流程如下：1. 在每个采样步骤中，模型评估各个掩码token的重要性。2. 根据重要性得分，截断一部分不重要的掩码token。3. 将被截断的token的信息聚合到对应的寄存器token中。4. 使用剩余的token（包括未截断的掩码token和寄存器token）进行后续的采样步骤。

**关键创新**：Sparse-LaViDa的关键创新在于动态截断机制和寄存器token的设计。动态截断机制能够自适应地减少计算量，而寄存器token则能够有效地保留被截断token的信息，从而避免生成质量的下降。此外，为了保证训练和推理的一致性，论文还设计了一种特殊的注意力掩码，在训练过程中模拟截断采样过程。

**关键设计**：关于动态截断机制，论文可能采用了一种基于注意力得分或者其他重要性指标的方法来评估掩码token的重要性。寄存器token的设计可能涉及到一种信息聚合机制，例如使用注意力机制或者简单的平均池化。注意力掩码的设计需要保证在训练过程中，模型能够学习到如何处理被截断的token以及寄存器token。具体的参数设置、损失函数和网络结构等细节在论文中应该有更详细的描述，但根据摘要信息无法得知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Sparse-LaViDa在多种任务中实现了显著的加速效果。例如，在文本到图像生成、图像编辑和数学推理等任务中，Sparse-LaViDa实现了高达2倍的加速，同时保持了与基线模型LaViDa-O相当的生成质量。这些实验结果表明，Sparse-LaViDa是一种有效的加速MDM推理的方法。

## 🎯 应用场景

Sparse-LaViDa具有广泛的应用前景，包括但不限于：文本到图像生成、图像编辑、视频生成、数学推理等。其加速推理的能力使得MDM能够更高效地应用于资源受限的设备上，例如移动设备和嵌入式系统。此外，该方法还可以促进MDM在交互式应用中的应用，例如实时图像编辑和生成。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

