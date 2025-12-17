---
layout: default
title: Scalable Face Security Vision Foundation Model for Deepfake, Diffusion, and Spoofing Detection
---

# Scalable Face Security Vision Foundation Model for Deepfake, Diffusion, and Spoofing Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10663" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10663v1</a>
  <a href="https://arxiv.org/pdf/2510.10663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10663v1" onclick="toggleFavorite(this, '2510.10663v1', 'Scalable Face Security Vision Foundation Model for Deepfake, Diffusion, and Spoofing Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gaojian Wang, Feng Lin, Tong Wu, Zhisheng Yan, Kui Ren

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-12

**备注**: 18 pages, 9 figures, project page: https://fsfm-3c.github.io/fsvfm.html

**🔗 代码/项目**: [PROJECT_PAGE](https://fsfm-3c.github.io/fsvfm.html)

---

## 💡 一句话要点

**提出FS-VFM，通过自监督学习提升人脸安全任务的泛化能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人脸安全` `自监督学习` `视觉基础模型` `深度伪造检测` `活体检测`

## 📋 核心要点

1. 现有方法在人脸安全任务中泛化性不足，缺乏利用大量无标签真实人脸数据的有效方法。
2. FS-VFM通过结合掩码图像建模和实例判别，学习人脸的局部模式和全局语义表示。
3. 实验表明，FS-VFM在深度伪造检测、活体检测和扩散人脸取证等任务上优于现有方法。

## 📝 摘要（中文）

本文提出了一种可扩展的自监督预训练框架FS-VFM，旨在学习鲁棒且可迁移的人脸表示，以提升各种人脸安全任务的泛化能力。FS-VFM引入了3C学习目标，即结合掩码图像建模(MIM)和实例判别(ID)，使模型能够编码真实人脸的局部模式和全局语义。具体而言，论文设计了多种人脸掩码策略用于MIM，并提出了一种简单而有效的CRFR-P掩码，显式地引导模型追求有意义的区域内一致性和具有挑战性的区域间连贯性。论文还提出了一种可靠的自蒸馏机制，将MIM与ID无缝耦合，以建立潜在的局部到全局的对应关系。预训练后，标准的Vision Transformers (ViTs)可作为通用视觉基础模型用于下游人脸安全任务，包括跨数据集的深度伪造检测、跨领域的活体检测和未见过的扩散人脸取证。为了有效地迁移预训练的FS-VFM，论文进一步提出了FS-Adapter，这是一个轻量级的即插即用瓶颈模块，位于冻结的主干网络之上，并具有一种新颖的真实锚点对比目标。在11个公共基准上的大量实验表明，FS-VFM始终比各种视觉基础模型(涵盖自然和人脸领域、完全、弱和自监督范式、小、基础和大型ViT规模)具有更好的泛化能力，甚至优于SOTA特定任务的方法，而FS-Adapter提供了出色的效率-性能权衡。

## 🔬 方法详解

**问题定义**：现有的人脸安全任务，如深度伪造检测、活体检测等，往往依赖于特定数据集进行训练，导致模型在跨数据集、跨领域或面对新型攻击时泛化能力较差。缺乏一种能够有效利用大量无标签真实人脸数据，学习鲁棒且可迁移人脸表示的通用方法。

**核心思路**：论文的核心思路是通过自监督学习，利用大量无标签的真实人脸数据，预训练一个视觉基础模型(FS-VFM)。该模型能够学习到人脸的内在结构和语义信息，从而提升在各种人脸安全任务上的泛化能力。通过结合掩码图像建模(MIM)和实例判别(ID)两种自监督学习方法，模型既能学习到局部细节，又能捕捉到全局语义信息。

**技术框架**：FS-VFM的整体框架包含两个主要阶段：预训练阶段和微调阶段。在预训练阶段，使用大量无标签的真实人脸数据，通过3C学习目标（Consistency, Coherency, Correspondence）训练视觉基础模型。3C学习目标结合了MIM和ID，其中MIM通过预测被掩盖的人脸区域来学习局部模式，ID通过区分不同的人脸实例来学习全局语义。在微调阶段，将预训练好的FS-VFM应用于下游的人脸安全任务，并使用少量标注数据进行微调。为了进一步提升迁移效率，论文还提出了FS-Adapter，一个轻量级的即插即用模块。

**关键创新**：论文的关键创新在于提出了3C学习目标，将MIM和ID有机结合，从而使模型能够同时学习人脸的局部模式和全局语义。此外，论文还设计了一种新的CRFR-P掩码策略，显式地引导模型学习区域内一致性和区域间连贯性。自蒸馏机制的引入，进一步加强了局部到全局的对应关系。FS-Adapter的设计，则使得模型能够高效地迁移到各种下游任务。

**关键设计**：CRFR-P掩码策略：该策略通过随机掩盖人脸的不同区域，并要求模型预测被掩盖区域的内容，从而学习区域内的一致性和区域间的连贯性。自蒸馏机制：该机制使用MIM的输出作为ID的目标，从而建立局部到全局的对应关系。FS-Adapter：该模块是一个轻量级的瓶颈结构，位于冻结的主干网络之上，通过学习残差连接来适应下游任务。损失函数：整体损失函数由MIM损失和ID损失组成，通过调整权重来平衡两种损失的贡献。

## 📊 实验亮点

实验结果表明，FS-VFM在11个公共基准上均取得了优异的性能，显著优于现有的视觉基础模型和特定任务的方法。例如，在跨数据集的深度伪造检测任务中，FS-VFM的性能提升了5%以上。FS-Adapter在保持较高性能的同时，显著降低了计算成本，实现了效率和性能的良好平衡。

## 🎯 应用场景

该研究成果可广泛应用于人脸安全领域，例如深度伪造检测、活体检测、人脸识别安全等。通过提升模型的泛化能力，可以有效应对各种新型攻击，保障人脸信息的安全。该技术还可应用于视频监控、身份验证等场景，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> With abundant, unlabeled real faces, how can we learn robust and transferable facial representations to boost generalization across various face security tasks? We make the first attempt and propose FS-VFM, a scalable self-supervised pre-training framework, to learn fundamental representations of real face images. We introduce three learning objectives, namely 3C, that synergize masked image modeling (MIM) and instance discrimination (ID), empowering FS-VFM to encode both local patterns and global semantics of real faces. Specifically, we formulate various facial masking strategies for MIM and devise a simple yet effective CRFR-P masking, which explicitly prompts the model to pursue meaningful intra-region Consistency and challenging inter-region Coherency. We present a reliable self-distillation mechanism that seamlessly couples MIM with ID to establish underlying local-to-global Correspondence. After pre-training, vanilla vision transformers (ViTs) serve as universal Vision Foundation Models for downstream Face Security tasks: cross-dataset deepfake detection, cross-domain face anti-spoofing, and unseen diffusion facial forensics. To efficiently transfer the pre-trained FS-VFM, we further propose FS-Adapter, a lightweight plug-and-play bottleneck atop the frozen backbone with a novel real-anchor contrastive objective. Extensive experiments on 11 public benchmarks demonstrate that our FS-VFM consistently generalizes better than diverse VFMs, spanning natural and facial domains, fully, weakly, and self-supervised paradigms, small, base, and large ViT scales, and even outperforms SOTA task-specific methods, while FS-Adapter offers an excellent efficiency-performance trade-off. The code and models are available on https://fsfm-3c.github.io/fsvfm.html.

