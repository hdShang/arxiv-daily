---
layout: default
title: In Pursuit of Pixel Supervision for Visual Pre-training
---

# In Pursuit of Pixel Supervision for Visual Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15715" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15715v1</a>
  <a href="https://arxiv.org/pdf/2512.15715.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15715v1" onclick="toggleFavorite(this, '2512.15715v1', 'In Pursuit of Pixel Supervision for Visual Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihe Yang, Shang-Wen Li, Yang Li, Xinjie Lei, Dong Wang, Abdelrahman Mohamed, Hengshuang Zhao, Hu Xu

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: Project page: https://github.com/facebookresearch/pixio

---

## 💡 一句话要点

**Pixio：基于像素监督的视觉预训练，实现简单、高效且强大的表征学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉预训练` `自监督学习` `掩码自编码器` `像素空间学习` `深度估计` `3D重建` `语义分割` `机器人学习`

## 📋 核心要点

1. 现有视觉预训练方法通常依赖于复杂的潜在空间学习，计算成本高昂且训练不稳定，Pixio旨在探索更简单有效的像素空间自监督学习。
2. Pixio通过增强的掩码自编码器（MAE）结构，结合更具挑战性的预训练任务和更大规模的数据集，提升了像素空间自监督学习的性能。
3. 实验表明，Pixio在单目深度估计、3D重建、语义分割和机器人学习等多个下游任务中，性能与DINOv3等先进方法相当甚至更优。

## 📝 摘要（中文）

像素是视觉信息最基本的来源，包含了从低级属性到高级概念的各个层次的信息。自编码器是一种经典且历史悠久的范例，用于从像素或其他原始输入中学习表征。本文证明，基于自编码器的自监督学习在今天仍然具有竞争力，并且可以为下游任务产生强大的表征，同时保持简单、稳定和高效。该模型名为“Pixio”，是一个增强的掩码自编码器（MAE），具有更具挑战性的预训练任务和更强大的架构。该模型在包含20亿张网络爬取图像的数据集上进行训练，采用了一种自我管理策略，最大限度地减少了人工干预。Pixio在各种实际下游任务中表现出色，包括单目深度估计（例如，Depth Anything）、前馈3D重建（即MapAnything）、语义分割和机器人学习，其性能优于或与以类似规模训练的DINOv3相匹配。研究结果表明，像素空间自监督学习可以作为潜在空间方法的有希望的替代和补充。

## 🔬 方法详解

**问题定义**：现有的视觉预训练方法，例如基于对比学习的方法，通常在潜在空间中进行操作，这可能导致信息损失和训练复杂性。此外，这些方法往往需要大量的计算资源和精细的超参数调整。因此，需要一种更简单、更高效且更稳定的自监督学习方法，可以直接从像素空间学习有用的视觉表征。

**核心思路**：Pixio的核心思路是利用增强的掩码自编码器（MAE）在像素空间中进行自监督学习。通过掩盖输入图像的部分区域，并训练模型来重建这些被掩盖的区域，模型可以学习到图像的底层结构和语义信息。这种方法避免了复杂的潜在空间操作，从而简化了训练过程并提高了效率。

**技术框架**：Pixio的整体框架基于MAE，包括一个编码器和一个解码器。编码器接收部分被掩盖的图像作为输入，并提取图像的特征表示。解码器接收编码器的输出，并尝试重建被掩盖的像素。整个训练过程通过最小化重建误差来进行优化。为了提高模型的性能，Pixio还采用了更具挑战性的预训练任务和更大规模的数据集。

**关键创新**：Pixio的关键创新在于它强调了像素空间自监督学习的潜力，并证明了通过简单的MAE架构和大规模数据训练，可以获得与复杂潜在空间方法相媲美的性能。此外，Pixio还采用了自我管理的数据集构建策略，以减少人工干预，并提高数据的质量。

**关键设计**：Pixio的关键设计包括：1) 使用高比例的掩码（例如，75%）来增加重建任务的难度；2) 使用Transformer架构作为编码器和解码器，以捕捉图像中的长程依赖关系；3) 使用大规模的网络爬取图像数据集进行训练，以提高模型的泛化能力；4) 采用自监督的数据集管理策略，自动筛选高质量的训练样本；5) 使用像素级别的重建损失函数，例如L1损失或L2损失，来衡量重建的准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15715v1/figure/mae_teaser_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15715v1/figure/mae_teaser_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15715v1/figure/mae_teaser_3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Pixio在多个下游任务中取得了显著的成果。例如，在单目深度估计任务中，Pixio的性能与Depth Anything相当甚至更优。在3D重建任务中，Pixio的性能与MapAnything相当。在语义分割任务中，Pixio的性能也达到了与DINOv3等先进方法相媲美的水平。这些结果表明，Pixio是一种非常有竞争力的视觉预训练方法。

## 🎯 应用场景

Pixio的潜在应用领域非常广泛，包括计算机视觉的各个方面，例如图像分类、目标检测、语义分割、深度估计和3D重建。此外，Pixio还可以应用于机器人学习领域，帮助机器人理解和感知周围环境。该研究的实际价值在于提供了一种简单、高效且强大的视觉预训练方法，可以降低模型训练的成本和复杂性，并提高下游任务的性能。未来，Pixio可以进一步扩展到其他模态的数据，例如视频和音频，以实现更全面的多模态表征学习。

## 📄 摘要（原文）

> At the most basic level, pixels are the source of the visual information through which we perceive the world. Pixels contain information at all levels, ranging from low-level attributes to high-level concepts. Autoencoders represent a classical and long-standing paradigm for learning representations from pixels or other raw inputs. In this work, we demonstrate that autoencoder-based self-supervised learning remains competitive today and can produce strong representations for downstream tasks, while remaining simple, stable, and efficient. Our model, codenamed "Pixio", is an enhanced masked autoencoder (MAE) with more challenging pre-training tasks and more capable architectures. The model is trained on 2B web-crawled images with a self-curation strategy with minimal human curation. Pixio performs competitively across a wide range of downstream tasks in the wild, including monocular depth estimation (e.g., Depth Anything), feed-forward 3D reconstruction (i.e., MapAnything), semantic segmentation, and robot learning, outperforming or matching DINOv3 trained at similar scales. Our results suggest that pixel-space self-supervised learning can serve as a promising alternative and a complement to latent-space approaches.

