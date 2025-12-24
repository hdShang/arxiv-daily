---
layout: default
title: "CoMAD: A Multiple-Teacher Self-Supervised Distillation Framework"
---

# CoMAD: A Multiple-Teacher Self-Supervised Distillation Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04816" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04816v1</a>
  <a href="https://arxiv.org/pdf/2508.04816.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04816v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04816v1', 'CoMAD: A Multiple-Teacher Self-Supervised Distillation Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sriram Mandalika, Lalitha V

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-06

**备注**: 8 Pages, 2 Figures

---

## 💡 一句话要点

**提出CoMAD框架以解决自监督学习模型的资源限制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `知识蒸馏` `视觉变换器` `模型压缩` `深度学习`

## 📋 核心要点

1. 现有自监督学习方法通常在孤立环境中预训练，忽视了模型间的互补信息，导致模型庞大且不适合资源受限的部署。
2. 本文提出的CoMAD框架通过多教师知识蒸馏，结合不同自监督学习模型的优势，构建一个紧凑的学生网络。
3. 在ImageNet-1K上，CoMAD的ViT-Tiny模型达到了75.4%的Top-1准确率，且在其他任务上也创造了新的性能记录。

## 📝 摘要（中文）

许多自监督学习范式，如对比学习和掩码图像建模，能够从无标签数据中学习强大的表示，但通常是孤立预训练，忽视了互补的见解，并导致大型模型在资源受限的环境中不切实际。为了解决这些挑战，本文提出了一种轻量级的无参数框架——共识导向掩码蒸馏（CoMAD），将多个当前最先进的自监督视觉变换器的知识统一到一个紧凑的学生网络中。CoMAD从三个预训练的ViT-Base教师模型中蒸馏知识，分别是MAE、MoCo v3和iBOT，每个模型提供独特的语义和上下文先验。通过不对称掩码，学生仅看到25%的图像块，而每个教师则接收逐渐减轻的独特掩码，迫使学生在更丰富的上下文中插值缺失特征。实验结果表明，CoMAD的ViT-Tiny在ImageNet-1K上达到了75.4%的Top-1准确率，比之前的最先进水平提高了0.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决自监督学习模型在资源受限环境中的应用问题，现有方法通常在孤立环境中预训练，导致模型庞大且难以部署。

**核心思路**：CoMAD框架通过整合多个自监督学习模型的知识，采用不对称掩码策略，迫使学生模型在丰富的上下文中学习，从而提高模型的表现和紧凑性。

**技术框架**：CoMAD的整体架构包括三个主要模块：教师模型（MAE、MoCo v3和iBOT），学生模型（ViT-Tiny），以及共识门控机制。教师模型提供不同的语义和上下文信息，学生模型通过线性适配器和层归一化对齐教师嵌入，并通过共识门控融合信息。

**关键创新**：最重要的创新在于采用不对称掩码策略，使学生模型仅能看到部分输入，同时教师模型接收不同的掩码，从而增强了学生模型的特征插值能力。

**关键设计**：在训练过程中，学生模型使用双层KL散度损失函数，分别对可见标记和重建特征图进行优化，以捕捉局部和全局结构。

## 📊 实验亮点

CoMAD的ViT-Tiny模型在ImageNet-1K上达到了75.4%的Top-1准确率，比之前的最先进水平提高了0.4%。在密集预测任务中，CoMAD在ADE20K上达到了47.3%的mIoU，在MS-COCO上分别达到了44.5%的框平均精度和40.5%的掩码平均精度，确立了紧凑自监督学习蒸馏的新标准。

## 🎯 应用场景

该研究的潜在应用场景包括计算机视觉中的图像分类、目标检测和分割等任务，尤其适合在资源受限的设备上进行高效的模型部署。未来，CoMAD框架有望推动自监督学习在边缘计算和移动设备中的应用，提升智能设备的视觉理解能力。

## 📄 摘要（原文）

> Numerous self-supervised learning paradigms, such as contrastive learning and masked image modeling, learn powerful representations from unlabeled data but are typically pretrained in isolation, overlooking complementary insights and yielding large models that are impractical for resource-constrained deployment. To overcome these challenges, we introduce Consensus-oriented Masked Distillation (CoMAD), a lightweight, parameter-free framework that unifies knowledge from multiple current state-of-the-art self-supervised Vision Transformers into a compact student network. CoMAD distills from three pretrained ViT-Base teachers, MAE, MoCo v3, and iBOT, each offering distinct semantic and contextual priors. Rather than naively averaging teacher outputs, we apply asymmetric masking: the student sees only 25 percent of patches while each teacher receives a progressively lighter, unique mask, forcing the student to interpolate missing features under richer contexts. Teacher embeddings are aligned to the student's space via a linear adapter and layer normalization, then fused through our joint consensus gating, which weights each token by combining cosine affinity with inter-teacher agreement. The student is trained with dual-level KL divergence on visible tokens and reconstructed feature maps, capturing both local and global structure. On ImageNet-1K, CoMAD's ViT-Tiny achieves 75.4 percent Top-1, an increment of 0.4 percent over the previous state-of-the-art. In dense-prediction transfers, it attains 47.3 percent mIoU on ADE20K, and 44.5 percent box average precision and 40.5 percent mask average precision on MS-COCO, establishing a new state-of-the-art in compact SSL distillation.

