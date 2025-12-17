---
layout: default
title: RzenEmbed: Towards Comprehensive Multimodal Retrieval
---

# RzenEmbed: Towards Comprehensive Multimodal Retrieval

**arXiv**: [2510.27350v1](https://arxiv.org/abs/2510.27350) | [PDF](https://arxiv.org/pdf/2510.27350.pdf)

**作者**: Weijian Jian, Yajun Zhang, Dawei Liang, Chunyu Xie, Yixiao He, Dawei Leng, Yuhui Yin

---

## 💡 一句话要点

**提出RzenEmbed统一框架以解决多模态检索中视频和视觉文档支持不足的问题**

**关键词**: `多模态检索` `统一嵌入学习` `两阶段训练` `改进InfoNCE损失` `视频检索` `视觉文档检索`

## 📋 核心要点

1. 现有CLIP框架主要针对自然图像，缺乏对视频和视觉文档等模态的全面支持
2. 采用两阶段训练策略，包括基础检索和改进的InfoNCE损失以增强判别能力
3. 在MMEB基准上实现新SOTA，尤其在视频和视觉文档检索任务中表现优异

## 📄 摘要（原文）

> The rapid advancement of Multimodal Large Language Models (MLLMs) has
> extended CLIP-based frameworks to produce powerful, universal embeddings for
> retrieval tasks. However, existing methods primarily focus on natural images,
> offering limited support for other crucial visual modalities such as videos and
> visual documents. To bridge this gap, we introduce RzenEmbed, a unified
> framework to learn embeddings across a diverse set of modalities, including
> text, images, videos, and visual documents. We employ a novel two-stage
> training strategy to learn discriminative representations. The first stage
> focuses on foundational text and multimodal retrieval. In the second stage, we
> introduce an improved InfoNCE loss, incorporating two key enhancements.
> Firstly, a hardness-weighted mechanism guides the model to prioritize
> challenging samples by assigning them higher weights within each batch.
> Secondly, we implement an approach to mitigate the impact of false negatives
> and alleviate data noise. This strategy not only enhances the model's
> discriminative power but also improves its instruction-following capabilities.
> We further boost performance with learnable temperature parameter and model
> souping. RzenEmbed sets a new state-of-the-art on the MMEB benchmark. It not
> only achieves the best overall score but also outperforms all prior work on the
> challenging video and visual document retrieval tasks. Our models are available
> in https://huggingface.co/qihoo360/RzenEmbed.

