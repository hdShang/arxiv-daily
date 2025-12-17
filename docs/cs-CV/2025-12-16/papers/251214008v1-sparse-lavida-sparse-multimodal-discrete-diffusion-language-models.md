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

**提出Sparse-LaViDa框架，通过动态截断冗余掩码标记以加速掩码离散扩散模型推理，同时保持生成质量。**

**关键词**: `稀疏扩散模型` `多模态推理` `掩码离散扩散` `加速采样` `寄存器标记` `注意力掩码` `文本到图像生成` `图像编辑`

## 📋 核心要点

1. 现有掩码离散扩散模型推理速度慢，因需在每个采样步骤重复处理冗余掩码标记，导致效率低下。
2. 提出Sparse-LaViDa框架，动态截断冗余标记并使用寄存器标记保持质量，设计注意力掩码确保训练与推理一致。
3. 在文本到图像生成等任务中实现高达2倍加速，同时维持生成质量，验证了方法的有效性。

## 📝 摘要（中文）

掩码离散扩散模型（MDMs）在图像理解、生成和编辑等多模态任务中表现出色，但其推理速度因需在每个采样步骤重复处理冗余掩码标记而受限。本文提出Sparse-LaViDa，一种新颖的建模框架，通过动态截断每个推理步骤中不必要的掩码标记来加速MDM采样。为保持生成质量，引入了专门的寄存器标记作为截断标记的紧凑表示。此外，为确保训练与推理的一致性，设计了专门的注意力掩码，在训练中忠实匹配截断采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理等多样化任务中实现了高达2倍的加速，同时维持生成质量。

## 🔬 方法详解

Sparse-LaViDa基于LaViDa-O统一MDM框架，核心创新在于动态截断机制：在推理时识别并移除冗余掩码标记，引入寄存器标记作为其紧凑表示以保留信息。关键技术创新包括专门设计的注意力掩码，确保训练过程模拟截断采样，从而保持一致性。与现有MDM方法相比，主要区别在于通过稀疏化处理减少计算开销，而非依赖全标记处理，显著提升推理效率。

## 📊 实验亮点

实验结果显示，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理任务中实现高达2倍推理加速，同时生成质量与基线模型相当，验证了框架的有效性和实用性。

## 🎯 应用场景

该研究可应用于多模态人工智能领域，如文本到图像生成、图像编辑和数学推理任务，通过加速推理过程，提升实时交互和批量处理效率，具有实际部署价值。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

