---
layout: default
title: "E-MMDiT: Revisiting Multimodal Diffusion Transformer Design for Fast Image Synthesis under Limited Resources"
---

# E-MMDiT: Revisiting Multimodal Diffusion Transformer Design for Fast Image Synthesis under Limited Resources

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27135" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27135v1</a>
  <a href="https://arxiv.org/pdf/2510.27135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27135v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27135v1', 'E-MMDiT: Revisiting Multimodal Diffusion Transformer Design for Fast Image Synthesis under Limited Resources')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tong Shen, Jingai Yu, Dong Zhou, Dong Li, Emad Barsoum

**分类**: cs.CV

**发布日期**: 2025-10-31

**🔗 代码/项目**: [GITHUB](https://github.com/AMD-AGI/Nitro-E)

---

## 💡 一句话要点

**提出E-MMDiT，一种轻量级多模态扩散Transformer，用于资源受限下的快速图像合成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `Transformer` `图像生成` `多模态学习` `轻量化模型` `token缩减` `资源受限`

## 📋 核心要点

1. 现有扩散模型训练成本高昂，需要大量数据和算力，或模型结构复杂导致推理延迟高。
2. E-MMDiT通过token缩减策略，结合高压缩视觉tokenizer和多路径压缩模块，实现轻量化设计。
3. 实验表明，E-MMDiT仅用少量数据和资源即可训练，并在图像生成质量上达到具有竞争力的水平。

## 📝 摘要（中文）

扩散模型在从文本提示生成高质量图像方面表现出强大的能力。然而，这些模型通常需要大规模的训练数据和大量的计算资源进行训练，或者存在结构复杂、延迟高等问题。为此，我们提出了高效多模态扩散Transformer（E-MMDiT），这是一个高效且轻量级的多模态扩散模型，仅有304M参数，用于在低训练资源下进行快速图像合成。我们提供了一个易于复现的基线，并取得了具有竞争力的结果。我们的512px生成模型，仅使用25M公共数据在单个包含8个AMD MI300X GPU的节点上训练1.5天，在GenEval上达到了0.66，并且通过一些训练后技术（如GRPO）可以轻松达到0.72。我们的设计理念以token缩减为中心，因为计算成本随token数量显著增加。我们采用了一种高度压缩的视觉tokenizer来产生更紧凑的表示，并提出了一种新颖的多路径压缩模块来进一步压缩token。为了增强我们的设计，我们引入了位置强化（Position Reinforcement），它加强了位置信息以保持空间连贯性，以及交替子区域注意力（ASA），它在子区域内执行注意力以进一步降低计算成本。此外，我们提出了AdaLN-affine，一个高效的轻量级模块，用于计算Transformer块中的调制参数。我们的代码可在https://github.com/AMD-AGI/Nitro-E 获得，我们希望E-MMDiT能够成为未来研究的强大而实用的基线，并为生成式AI模型的普及做出贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散模型在资源受限环境下训练和部署的难题。现有扩散模型通常参数量巨大，需要大量的训练数据和计算资源，这限制了其在算力不足的场景下的应用。此外，即使模型训练完成，其复杂的结构也导致推理速度慢，难以满足实时性要求。

**核心思路**：论文的核心思路是通过token缩减来降低计算复杂度。由于Transformer的计算成本与token数量呈显著相关，因此减少token数量可以直接降低计算量，从而实现模型的轻量化和加速。同时，论文还通过增强位置信息和优化注意力机制来保持图像生成的质量。

**技术框架**：E-MMDiT的整体架构基于扩散Transformer，主要包含以下几个模块：1) 高度压缩的视觉Tokenizer：将输入图像转换为更紧凑的token表示。2) 多路径压缩模块：进一步减少token数量。3) 位置强化（Position Reinforcement）：增强位置信息，保持空间连贯性。4) 交替子区域注意力（ASA）：在子区域内执行注意力，降低计算成本。5) AdaLN-affine：一个轻量级的模块，用于计算Transformer块中的调制参数。

**关键创新**：论文的关键创新在于token缩减策略和交替子区域注意力机制。通过高度压缩的视觉Tokenizer和多路径压缩模块，显著减少了token数量，从而降低了计算复杂度。交替子区域注意力机制则在保证模型性能的同时，进一步降低了计算成本。此外，AdaLN-affine模块也提供了一种高效的计算调制参数的方法。

**关键设计**：在视觉Tokenizer方面，采用了更激进的压缩策略，以获得更少的token。多路径压缩模块的设计细节未知。位置强化模块的具体实现方式未知，但其目的是为了弥补token缩减可能导致的空间信息损失。交替子区域注意力机制将图像划分为多个子区域，并在子区域内进行注意力计算，从而降低了计算复杂度。AdaLN-affine模块的具体结构和参数设置未知。

## 📊 实验亮点

E-MMDiT仅使用304M参数，在单个包含8个AMD MI300X GPU的节点上，使用25M公共数据训练1.5天，即可在512px图像生成任务的GenEval指标上达到0.66。通过GRPO等训练后技术，该指标可轻松提升至0.72。这些结果表明，E-MMDiT在资源受限的情况下，仍能实现具有竞争力的图像生成质量。

## 🎯 应用场景

E-MMDiT可应用于资源受限的边缘设备或移动设备上的图像生成任务，例如移动端的AI绘画应用、低成本的图像编辑工具等。该研究有助于降低生成式AI的使用门槛，促进其在更广泛的场景中应用，并加速生成式AI的普及。

## 📄 摘要（原文）

> Diffusion models have shown strong capabilities in generating high-quality images from text prompts. However, these models often require large-scale training data and significant computational resources to train, or suffer from heavy structure with high latency. To this end, we propose Efficient Multimodal Diffusion Transformer (E-MMDiT), an efficient and lightweight multimodal diffusion model with only 304M parameters for fast image synthesis requiring low training resources. We provide an easily reproducible baseline with competitive results. Our model for 512px generation, trained with only 25M public data in 1.5 days on a single node of 8 AMD MI300X GPUs, achieves 0.66 on GenEval and easily reaches to 0.72 with some post-training techniques such as GRPO. Our design philosophy centers on token reduction as the computational cost scales significantly with the token count. We adopt a highly compressive visual tokenizer to produce a more compact representation and propose a novel multi-path compression module for further compression of tokens. To enhance our design, we introduce Position Reinforcement, which strengthens positional information to maintain spatial coherence, and Alternating Subregion Attention (ASA), which performs attention within subregions to further reduce computational cost. In addition, we propose AdaLN-affine, an efficient lightweight module for computing modulation parameters in transformer blocks. Our code is available at https://github.com/AMD-AGI/Nitro-E and we hope E-MMDiT serves as a strong and practical baseline for future research and contributes to democratization of generative AI models.

