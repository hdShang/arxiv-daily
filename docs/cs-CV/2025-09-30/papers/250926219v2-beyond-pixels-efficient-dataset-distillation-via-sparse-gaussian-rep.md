---
layout: default
title: "Beyond Pixels: Efficient Dataset Distillation via Sparse Gaussian Representation"
---

# Beyond Pixels: Efficient Dataset Distillation via Sparse Gaussian Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26219" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26219v2</a>
  <a href="https://arxiv.org/pdf/2509.26219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26219v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26219v2', 'Beyond Pixels: Efficient Dataset Distillation via Sparse Gaussian Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyang Jiang, Zhengcen Li, Hang Zhao, Qiben Shan, Shaocong Wu, Jingyong Su

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-12-02)

**备注**: 19 pages; Code is available on https://github.com/j-cyoung/GSDatasetDistillation

**🔗 代码/项目**: [GITHUB](https://github.com/j-cyoung/GSDatasetDistillation)

---

## 💡 一句话要点

**提出基于稀疏高斯表示的数据集蒸馏方法GSDD，提升效率与性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `数据集蒸馏` `稀疏表示` `高斯模型` `CUDA加速` `模型压缩`

## 📋 核心要点

1. 传统数据集蒸馏方法依赖密集像素表示，存在冗余且扩展性差的问题。
2. GSDD利用少量高斯基元稀疏表示图像，编码关键判别信息，提升数据集多样性。
3. 采用CUDA加速的splatting算子，实现高效并行推理和训练，性能优于现有方法。

## 📝 摘要（中文）

数据集蒸馏是一种很有前景的范式，它合成紧凑且信息丰富的数据集，能够保留大规模数据集的知识，从而解决现代模型训练中巨大的计算和存储负担。传统方法通常依赖于密集的像素级表示，这引入了冗余并且难以扩展。本文提出GSDD，一种新颖且高效的基于2D高斯分布的数据集蒸馏稀疏表示方法。GSDD并非平等地表示所有像素，而是仅使用少量高斯基元在蒸馏图像中编码关键的判别信息。这种稀疏表示可以在相同的存储预算下提高数据集的多样性，增强对困难样本的覆盖，并提高蒸馏性能。为了确保效率和可扩展性，我们采用了基于CUDA的splatting算子进行并行推理和训练，从而以最小的计算和内存开销实现高质量的渲染。我们的方法简单而有效，广泛适用于不同的蒸馏流程，并且具有高度的可扩展性。实验表明，GSDD在CIFAR-10、CIFAR-100和ImageNet子集上实现了最先进的性能，同时保持了高效的编码和解码成本。代码已开源。

## 🔬 方法详解

**问题定义**：数据集蒸馏旨在用一个远小于原始数据集的合成数据集，训练出与在原始数据集上训练效果相近的模型。现有方法，如基于像素的蒸馏，存在信息冗余，计算成本高，难以扩展到大规模数据集等问题。这些方法平等地对待每个像素，忽略了图像中不同区域的重要性差异。

**核心思路**：GSDD的核心思路是使用稀疏的高斯分布来表示蒸馏数据集中的图像。通过少量的高斯基元，捕捉图像中的关键判别信息，避免了像素级表示的冗余。这种稀疏表示方法能够更有效地利用存储空间，提高数据集的多样性，从而提升蒸馏性能。

**技术框架**：GSDD的整体框架包括以下几个主要阶段：1) 初始化：随机初始化一组高斯参数（位置、方差、幅度等）。2) 前向传播：使用基于CUDA的splatting算子，将高斯基元渲染成图像。3) 损失计算：计算渲染图像与原始图像之间的损失，例如交叉熵损失。4) 反向传播：通过反向传播算法，更新高斯参数。5) 迭代优化：重复步骤2-4，直到高斯参数收敛。

**关键创新**：GSDD最重要的创新点在于使用稀疏高斯表示进行数据集蒸馏。与传统的像素级表示相比，GSDD能够更有效地编码图像中的关键信息，减少冗余，提高数据集的多样性。此外，GSDD采用基于CUDA的splatting算子，实现了高效的并行渲染和训练，使其能够扩展到更大规模的数据集。

**关键设计**：GSDD的关键设计包括：1) 高斯基元的参数化：每个高斯基元由位置、方差、幅度等参数表示。2) 基于CUDA的splatting算子：用于将高斯基元渲染成图像，实现高效的并行计算。3) 损失函数：可以使用交叉熵损失、均方误差损失等，用于衡量渲染图像与原始图像之间的差异。4) 优化算法：可以使用Adam、SGD等优化算法，用于更新高斯参数。

## 📊 实验亮点

GSDD在CIFAR-10、CIFAR-100和ImageNet子集上取得了state-of-the-art的性能。例如，在CIFAR-10上，使用10个图像进行蒸馏，GSDD的准确率超过了现有方法，并且编码和解码成本更低。实验结果表明，GSDD能够有效地提高数据集的多样性，增强对困难样本的覆盖，从而提升蒸馏性能。

## 🎯 应用场景

GSDD可应用于模型压缩、联邦学习、持续学习等领域。在资源受限的边缘设备上，可以使用GSDD蒸馏得到的小型数据集进行模型训练，降低计算和存储成本。在联邦学习中，可以使用GSDD对本地数据进行蒸馏，减少上传的数据量，保护用户隐私。未来，GSDD有望扩展到视频数据集的蒸馏，进一步提升效率。

## 📄 摘要（原文）

> Dataset distillation has emerged as a promising paradigm that synthesizes compact, informative datasets capable of retaining the knowledge of large-scale counterparts, thereby addressing the substantial computational and storage burdens of modern model training. Conventional approaches typically rely on dense pixel-level representations, which introduce redundancy and are difficult to scale up. In this work, we propose GSDD, a novel and efficient sparse representation for dataset distillation based on 2D Gaussians. Instead of representing all pixels equally, GSDD encodes critical discriminative information in a distilled image using only a small number of Gaussian primitives. This sparse representation could improve dataset diversity under the same storage budget, enhancing coverage of difficult samples and boosting distillation performance. To ensure both efficiency and scalability, we adapt CUDA-based splatting operators for parallel inference and training, enabling high-quality rendering with minimal computational and memory overhead. Our method is simple yet effective, broadly applicable to different distillation pipelines, and highly scalable. Experiments show that GSDD achieves state-of-the-art performance on CIFAR-10, CIFAR-100, and ImageNet subsets, while remaining highly efficient encoding and decoding cost. Our code is available at https://github.com/j-cyoung/GSDatasetDistillation.

