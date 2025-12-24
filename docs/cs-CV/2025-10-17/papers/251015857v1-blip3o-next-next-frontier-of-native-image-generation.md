---
layout: default
title: "BLIP3o-NEXT: Next Frontier of Native Image Generation"
---

# BLIP3o-NEXT: Next Frontier of Native Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15857" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15857v1</a>
  <a href="https://arxiv.org/pdf/2510.15857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15857v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15857v1', 'BLIP3o-NEXT: Next Frontier of Native Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiuhai Chen, Le Xue, Zhiyang Xu, Xichen Pan, Shusheng Yang, Can Qin, An Yan, Honglu Zhou, Zeyuan Chen, Lifu Huang, Tianyi Zhou, Junnan Li, Silvio Savarese, Caiming Xiong, Ran Xu

**分类**: cs.CV

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**BLIP3o-NEXT：原生图像生成的新前沿，统一文本到图像生成与图像编辑**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `图像编辑` `自回归模型` `扩散模型` `多模态学习` `原生图像生成` `强化学习`

## 📋 核心要点

1. 现有图像生成模型在统一文本到图像生成和图像编辑方面存在挑战，难以兼顾指令遵循和图像质量。
2. BLIP3o-NEXT采用自回归+扩散架构，利用自回归模型进行推理和指令遵循，扩散模型生成高保真图像。
3. 实验表明，BLIP3o-NEXT在文本到图像生成和图像编辑任务上均优于现有模型，实现了更好的连贯性和真实感。

## 📝 摘要（中文）

BLIP3o-NEXT是BLIP3系列中的一个完全开源的基础模型，它推进了原生图像生成的新前沿。BLIP3o-NEXT在一个单一架构中统一了文本到图像的生成和图像编辑，展示了强大的图像生成和图像编辑能力。在开发最先进的原生图像生成模型时，我们确定了四个关键见解：（1）大多数架构选择产生相当的性能；只要架构能够有效地扩展并支持快速推理，就可以认为是有效的；（2）强化学习的成功应用可以进一步推动原生图像生成的前沿；（3）图像编辑仍然是一项具有挑战性的任务，但通过后训练和数据引擎，可以显著提高指令遵循以及生成图像和参考图像之间的一致性；（4）数据质量和规模仍然是决定模型性能上限的决定性因素。基于这些见解，BLIP3o-NEXT利用自回归+扩散架构，其中自回归模型首先生成以多模态输入为条件的离散图像tokens，然后将其隐藏状态用作扩散模型生成高保真图像的条件信号。这种架构集成了自回归模型的推理能力和指令遵循能力，以及扩散模型的精细细节渲染能力，从而实现了新的连贯性和真实感。对各种文本到图像和图像编辑基准的广泛评估表明，BLIP3o-NEXT优于现有模型。

## 🔬 方法详解

**问题定义**：论文旨在解决原生图像生成领域中，如何构建一个既能进行高质量图像生成，又能进行精确图像编辑的统一模型的问题。现有方法通常难以在指令遵循的准确性和生成图像的真实感之间取得平衡，并且图像编辑任务仍然具有挑战性。

**核心思路**：BLIP3o-NEXT的核心思路是结合自回归模型和扩散模型的优势。自回归模型擅长推理和指令遵循，而扩散模型擅长生成高保真图像。通过将两者结合，模型既能理解复杂的文本指令，又能生成细节丰富的图像。

**技术框架**：BLIP3o-NEXT采用自回归+扩散的架构。首先，自回归模型接收多模态输入（例如文本描述），并生成离散的图像tokens。然后，这些tokens的隐藏状态被用作扩散模型的条件信号，引导扩散模型生成最终的高质量图像。这种两阶段的架构允许模型分别处理语义理解和图像生成，从而提高整体性能。

**关键创新**：BLIP3o-NEXT的关键创新在于将自回归模型的推理能力和扩散模型的图像生成能力有效地结合起来。通过自回归模型生成离散的图像tokens，并将其作为扩散模型的条件信号，模型能够更好地理解文本指令，并生成与指令一致的图像。此外，论文还强调了数据质量和规模的重要性，以及强化学习在提升图像生成质量方面的潜力。

**关键设计**：具体的技术细节包括自回归模型的选择、扩散模型的架构、以及如何将自回归模型的输出有效地传递给扩散模型。论文还强调了后训练和数据引擎在提高指令遵循和图像一致性方面的重要性，但具体实现细节未知。

## 📊 实验亮点

BLIP3o-NEXT在文本到图像生成和图像编辑的多个基准测试中均取得了优于现有模型的性能。具体性能数据和对比基线在论文中进行了详细展示，表明该模型在图像质量、指令遵循和编辑能力方面均有显著提升。强化学习的应用进一步提升了图像生成的质量。

## 🎯 应用场景

BLIP3o-NEXT具有广泛的应用前景，包括创意设计、内容生成、虚拟现实、游戏开发等领域。它可以根据用户的文本描述生成各种图像，也可以对现有图像进行编辑和修改。该模型有望降低图像生成和编辑的门槛，使更多人能够参与到创意内容创作中。

## 📄 摘要（原文）

> We present BLIP3o-NEXT, a fully open-source foundation model in the BLIP3 series that advances the next frontier of native image generation. BLIP3o-NEXT unifies text-to-image generation and image editing within a single architecture, demonstrating strong image generation and image editing capabilities. In developing the state-of-the-art native image generation model, we identify four key insights: (1) Most architectural choices yield comparable performance; an architecture can be deemed effective provided it scales efficiently and supports fast inference; (2) The successful application of reinforcement learning can further push the frontier of native image generation; (3) Image editing still remains a challenging task, yet instruction following and the consistency between generated and reference images can be significantly enhanced through post-training and data engine; (4) Data quality and scale continue to be decisive factors that determine the upper bound of model performance. Building upon these insights, BLIP3o-NEXT leverages an Autoregressive + Diffusion architecture in which an autoregressive model first generates discrete image tokens conditioned on multimodal inputs, whose hidden states are then used as conditioning signals for a diffusion model to generate high-fidelity images. This architecture integrates the reasoning strength and instruction following of autoregressive models with the fine-detail rendering ability of diffusion models, achieving a new level of coherence and realism. Extensive evaluations of various text-to-image and image-editing benchmarks show that BLIP3o-NEXT achieves superior performance over existing models.

