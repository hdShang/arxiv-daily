---
layout: default
title: RzenEmbed: Towards Comprehensive Multimodal Retrieval
---

# RzenEmbed: Towards Comprehensive Multimodal Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27350" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27350v1</a>
  <a href="https://arxiv.org/pdf/2510.27350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27350v1" onclick="toggleFavorite(this, '2510.27350v1', 'RzenEmbed: Towards Comprehensive Multimodal Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijian Jian, Yajun Zhang, Dawei Liang, Chunyu Xie, Yixiao He, Dawei Leng, Yuhui Yin

**分类**: cs.CV

**发布日期**: 2025-10-31

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/qihoo360/RzenEmbed)

---

## 💡 一句话要点

**RzenEmbed：提出统一多模态嵌入框架，显著提升视频和文档检索性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `跨模态学习` `视频检索` `文档检索` `对比学习` `InfoNCE损失` `硬度加权`

## 📋 核心要点

1. 现有方法在多模态检索中对视频和视觉文档等模态支持不足，限制了通用嵌入的应用。
2. RzenEmbed采用两阶段训练策略，结合硬度加权InfoNCE损失和假阴性缓解，提升判别能力。
3. RzenEmbed在MMEB基准测试中取得SOTA，尤其在视频和视觉文档检索任务上表现突出。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）的快速发展推动了基于CLIP的框架，使其能够为检索任务生成强大的通用嵌入。然而，现有方法主要集中于自然图像，对视频和视觉文档等其他关键视觉模态的支持有限。为了弥补这一差距，我们提出了RzenEmbed，一个统一的框架，用于学习跨多种模态（包括文本、图像、视频和视觉文档）的嵌入。我们采用了一种新颖的两阶段训练策略来学习判别性表示。第一阶段侧重于基础文本和多模态检索。在第二阶段，我们引入了一种改进的InfoNCE损失，其中包含两项关键增强：首先，一种硬度加权机制通过在每个批次中为具有挑战性的样本分配更高的权重来引导模型优先处理这些样本；其次，我们实施了一种方法来减轻假阴性的影响并缓解数据噪声。这种策略不仅增强了模型的判别能力，还提高了其指令遵循能力。我们还通过可学习的温度参数和模型融合进一步提升了性能。RzenEmbed在MMEB基准测试上取得了新的state-of-the-art。它不仅实现了最佳的总体得分，而且在具有挑战性的视频和视觉文档检索任务上也优于所有先前的工作。我们的模型可在https://huggingface.co/qihoo360/RzenEmbed 上找到。

## 🔬 方法详解

**问题定义**：现有基于CLIP的多模态检索方法主要针对自然图像，忽略了视频和视觉文档等重要模态。这导致模型在处理这些模态时性能下降，无法满足通用多模态检索的需求。现有方法在训练过程中容易受到噪声数据和假阴性的影响，降低了模型的判别能力。

**核心思路**：RzenEmbed的核心思路是构建一个统一的框架，能够同时学习文本、图像、视频和视觉文档的嵌入表示。通过两阶段训练策略，首先进行基础的文本和多模态检索训练，然后通过改进的InfoNCE损失进一步提升模型的判别能力和指令遵循能力。

**技术框架**：RzenEmbed采用两阶段训练框架。第一阶段，模型在文本和图像数据上进行预训练，学习基础的多模态对齐。第二阶段，模型在包含视频和视觉文档的更广泛数据集上进行训练，并使用改进的InfoNCE损失函数。该框架还包括可学习的温度参数和模型融合等技术，以进一步提升性能。

**关键创新**：RzenEmbed的关键创新在于改进的InfoNCE损失函数，它包含两个关键增强：硬度加权机制和假阴性缓解。硬度加权机制使模型能够更加关注具有挑战性的样本，从而提高模型的判别能力。假阴性缓解机制则可以减少噪声数据对模型训练的影响。

**关键设计**：硬度加权机制通过计算每个样本的损失值，并根据损失值的大小分配不同的权重。损失值越大的样本，权重越高。假阴性缓解机制通过引入额外的负样本，并对这些负样本进行加权，从而减少假阴性的影响。此外，模型还使用了可学习的温度参数来调整InfoNCE损失函数的温度，并采用模型融合技术来进一步提升性能。

## 📊 实验亮点

RzenEmbed在MMEB基准测试中取得了新的state-of-the-art，总体得分超过了所有先前的工作。尤其是在具有挑战性的视频和视觉文档检索任务上，RzenEmbed的性能提升显著，验证了其在处理非自然图像模态方面的优势。

## 🎯 应用场景

RzenEmbed可应用于各种多模态检索场景，例如视频内容搜索、文档图像检索、跨模态信息推荐等。该研究成果有助于提升多模态信息检索的准确性和效率，为用户提供更优质的搜索体验，并推动多模态人工智能的发展。

## 📄 摘要（原文）

> The rapid advancement of Multimodal Large Language Models (MLLMs) has extended CLIP-based frameworks to produce powerful, universal embeddings for retrieval tasks. However, existing methods primarily focus on natural images, offering limited support for other crucial visual modalities such as videos and visual documents. To bridge this gap, we introduce RzenEmbed, a unified framework to learn embeddings across a diverse set of modalities, including text, images, videos, and visual documents. We employ a novel two-stage training strategy to learn discriminative representations. The first stage focuses on foundational text and multimodal retrieval. In the second stage, we introduce an improved InfoNCE loss, incorporating two key enhancements. Firstly, a hardness-weighted mechanism guides the model to prioritize challenging samples by assigning them higher weights within each batch. Secondly, we implement an approach to mitigate the impact of false negatives and alleviate data noise. This strategy not only enhances the model's discriminative power but also improves its instruction-following capabilities. We further boost performance with learnable temperature parameter and model souping. RzenEmbed sets a new state-of-the-art on the MMEB benchmark. It not only achieves the best overall score but also outperforms all prior work on the challenging video and visual document retrieval tasks. Our models are available in https://huggingface.co/qihoo360/RzenEmbed.

