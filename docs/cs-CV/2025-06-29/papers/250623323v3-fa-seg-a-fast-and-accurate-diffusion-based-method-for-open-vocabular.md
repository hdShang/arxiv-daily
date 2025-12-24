---
layout: default
title: "FA-Seg: A Fast and Accurate Diffusion-Based Method for Open-Vocabulary Segmentation"
---

# FA-Seg: A Fast and Accurate Diffusion-Based Method for Open-Vocabulary Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23323" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23323v3</a>
  <a href="https://arxiv.org/pdf/2506.23323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23323v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23323v3', 'FA-Seg: A Fast and Accurate Diffusion-Based Method for Open-Vocabulary Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quang-Huy Che, Vinh-Tiep Nguyen

**分类**: cs.CV

**发布日期**: 2025-06-29 (更新: 2025-07-15)

---

## 💡 一句话要点

**提出FA-Seg以解决开放词汇语义分割中的精度与效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇分割` `扩散模型` `语义分割` `对比学习` `深度学习`

## 📋 核心要点

1. 现有的对比学习模型在开放词汇语义分割中常常因全局表示偏差而失去像素级的精度。
2. FA-Seg通过扩散模型实现快速且准确的分割，采用双提示机制和层次注意力精炼方法来提升分割质量。
3. FA-Seg在多个基准数据集上取得了43.8%的平均mIoU，展示了其在分割质量和推理效率之间的良好平衡。

## 📝 摘要（中文）

开放词汇语义分割（OVSS）旨在从任意文本类别中分割对象，而无需密集标注的数据集。尽管基于对比学习的模型能够实现零-shot 分割，但由于全局表示偏差，往往在像素级别上失去细致的空间精度。与此不同，基于扩散模型的方法通过注意力机制自然地编码细粒度的空间特征，能够捕捉全局上下文和局部细节。然而，这些模型在计算成本与分割质量之间的平衡上面临挑战。本文提出了FA-Seg，一个快速且准确的无训练框架，基于扩散模型实现开放词汇分割。FA-Seg仅需从预训练的扩散模型中进行一次（1+1）步的分割，并且能够一次性对所有类别进行分割。为了进一步提升分割质量，FA-Seg引入了三个关键组件：双提示机制、层次注意力精炼方法（HARD）和测试时翻转（TTF）方案。实验结果表明，FA-Seg在PASCAL VOC、PASCAL Context和COCO Object基准上实现了43.8%的平均mIoU，且推理效率优越。

## 🔬 方法详解

**问题定义**：本文旨在解决开放词汇语义分割中的精度与效率问题。现有的对比学习模型在处理细粒度空间特征时存在全局表示偏差，导致分割精度不足。

**核心思路**：FA-Seg提出了一种基于扩散模型的快速且准确的无训练框架，通过一次性处理所有类别的分割任务，避免了多次运行的计算开销。

**技术框架**：FA-Seg的整体架构包括三个主要模块：双提示机制用于提取类感知的注意力，层次注意力精炼方法（HARD）用于多分辨率的注意力融合，以及测试时翻转（TTF）方案以增强空间一致性。

**关键创新**：FA-Seg的核心创新在于其训练-free的设计和高效的分割策略，尤其是通过双提示机制和HARD方法显著提升了分割的语义精度。

**关键设计**：在设计中，FA-Seg采用了多分辨率的注意力融合策略，并通过测试时翻转来增强分割结果的空间一致性，确保了在推理过程中的高效性和准确性。

## 📊 实验亮点

FA-Seg在PASCAL VOC、PASCAL Context和COCO Object基准上实现了43.8%的平均mIoU，显著优于现有的训练-free 方法，且在推理效率上表现出色，展示了其在开放词汇语义分割中的领先地位。

## 🎯 应用场景

FA-Seg的研究成果在多个领域具有广泛的应用潜力，包括自动驾驶、医学影像分析和智能监控等场景。其高效的分割能力能够支持实时处理需求，为各类视觉任务提供强大的技术支持，未来可能推动更多智能应用的发展。

## 📄 摘要（原文）

> Open-vocabulary semantic segmentation (OVSS) aims to segment objects from arbitrary text categories without requiring densely annotated datasets. Although contrastive learning based models enable zero-shot segmentation, they often lose fine spatial precision at pixel level, due to global representation bias. In contrast, diffusion-based models naturally encode fine-grained spatial features via attention mechanisms that capture both global context and local details. However, they often face challenges in balancing the computation costs and the quality of the segmentation mask. In this work, we present FA-Seg, a Fast and Accurate training-free framework for open-vocabulary segmentation based on diffusion models. FA-Seg performs segmentation using only a (1+1)-step from a pretrained diffusion model. Moreover, instead of running multiple times for different classes, FA-Seg performs segmentation for all classes at once. To further enhance the segmentation quality, FA-Seg introduces three key components: (i) a dual-prompt mechanism for discriminative, class-aware attention extraction, (ii) a Hierarchical Attention Refinement Method (HARD) that enhances semantic precision via multi-resolution attention fusion, and (iii) a Test-Time Flipping (TTF) scheme designed to improve spatial consistency. Extensive experiments show that FA-Seg achieves state-of-the-art training-free performance, obtaining 43.8% average mIoU across PASCAL VOC, PASCAL Context, and COCO Object benchmarks while maintaining superior inference efficiency. Our results demonstrate that FA-Seg provides a strong foundation for extendability, bridging the gap between segmentation quality and inference efficiency. The source code will be open-sourced after this paper is accepted.

