---
layout: default
title: Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding
---

# Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09110" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09110v3</a>
  <a href="https://arxiv.org/pdf/2510.09110.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09110v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09110v3', 'Synthetic Object Compositions for Scalable and Accurate Learning in Detection, Segmentation, and Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikai Huang, Jieyu Zhang, Taoyang Jia, Chenhao Zheng, Ziqi Gao, Jae Sung Park, Winson Han, Ranjay Krishna

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-10 (更新: 2025-11-21)

**备注**: Project website: https://github.com/weikaih04/Synthetic-Detection-Segmentation-Grounding-Data

---

## 💡 一句话要点

**提出SOC：一种可扩展、精确的合成对象组合方法，用于提升检测、分割和定位任务性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `目标检测` `实例分割` `视觉定位` `数据增强` `3D几何布局` `生成式和谐化`

## 📋 核心要点

1. 现有视觉任务依赖的大规模数据集存在构建成本高、覆盖偏差和难以扩展等问题，限制了模型性能和泛化能力。
2. SOC通过对象中心组合策略，结合3D几何布局和相机配置增强，以及生成式和谐化等技术，生成高质量、多样化的合成数据。
3. 实验表明，仅用少量SOC合成数据训练的模型，性能显著优于在更大规模的真实或合成数据集上训练的模型，并在低数据场景下表现突出。

## 📝 摘要（中文）

视觉分组（通过实例分割、视觉定位和目标检测等任务实现）支持从机器人感知到照片编辑等应用。这些计算机视觉中的基本问题依赖于大规模、精心标注的数据集。然而，这些数据集构建成本高昂、覆盖范围存在偏差且难以扩展。合成数据集提供了一种有希望的替代方案，但面临灵活性、准确性和组合多样性的挑战。我们提出了一种名为合成对象组合（SOC）的精确且可扩展的数据合成流程，该流程通过一种新颖的以对象为中心的组合策略实现。它使用3D几何布局增强和相机配置增强，结合生成式和谐化和掩码面积加权混合，将高质量的合成对象分割组合成新的图像，从而产生准确且多样化的掩码、框和指代表达式。仅使用10万张合成图像训练的模型，其性能优于在更大的真实数据集（GRIT 20M、V3Det 200K）和合成流程（Copy-Paste、X-Paste、SynGround、SegGen）上训练的模型，提升幅度为+24-36%，在LVIS上达到+10.9 AP，在gRefCOCO上达到+8.4 NAcc。除了通用的开放词汇设置外，SOC还支持针对不同用例的可控数据集构建，并提高了在低数据和封闭词汇场景中的性能。通过使用合成对象分割增强LVIS和COCO，可以在不同的真实数据规模下实现强大的性能，并且在极有限的真实数据条件下产生更大的改进，包括在1% COCO数据设置下+6.59 AP。此外，这种可控性使得能够针对类内指代进行目标数据生成，我们提出了一种需要细粒度属性区分的诊断性定位任务。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉任务中对大规模、高质量标注数据的依赖问题。现有方法，如直接使用真实数据或简单的合成数据增强，存在标注成本高、数据偏差大、合成数据质量低等痛点，限制了模型的泛化能力和性能提升。

**核心思路**：论文的核心思路是构建一个以对象为中心的合成数据生成流程，通过将高质量的合成对象分割组合成新的图像，并利用3D几何布局和相机配置增强数据的多样性，同时采用生成式和谐化技术提高合成数据的真实感。这样既能降低数据标注成本，又能保证数据的质量和多样性。

**技术框架**：SOC的整体框架包含以下几个主要阶段：1) **对象分割库构建**：收集或生成高质量的3D对象模型和对应的分割掩码。2) **场景布局**：利用3D几何布局算法，将对象放置在虚拟场景中，模拟真实世界的物体排列方式。3) **相机配置**：随机调整虚拟相机的参数，如位置、角度和焦距，以生成不同的视角。4) **图像合成**：将对象分割和场景布局信息渲染成图像，并使用生成式和谐化技术，使合成对象与背景更加融合。5) **数据标注**：自动生成目标检测、实例分割和视觉定位所需的标注信息。

**关键创新**：SOC最重要的技术创新点在于其以对象为中心的组合策略和3D几何布局增强。与传统的图像级合成方法不同，SOC直接操作对象分割，可以更精确地控制合成数据的属性和关系。3D几何布局增强则可以模拟真实世界的物体排列方式，提高合成数据的真实感和多样性。

**关键设计**：SOC的关键设计包括：1) 使用高质量的3D对象模型和分割掩码，保证合成数据的准确性。2) 采用掩码面积加权混合，使合成对象与背景更加自然地融合。3) 利用生成式对抗网络（GAN）进行图像和谐化，提高合成数据的真实感。4) 设计了针对类内指代的诊断性定位任务，用于评估模型对细粒度属性的区分能力。

## 📊 实验亮点

实验结果表明，仅使用10万张SOC合成图像训练的模型，在LVIS数据集上达到了+10.9 AP的提升，在gRefCOCO数据集上达到了+8.4 NAcc的提升，显著优于在更大规模的真实数据集（GRIT 20M、V3Det 200K）和合成流程（Copy-Paste、X-Paste、SynGround、SegGen）上训练的模型。在1% COCO数据设置下，使用SOC进行数据增强，可以获得+6.59 AP的提升。

## 🎯 应用场景

SOC具有广泛的应用前景，可用于机器人感知、自动驾驶、智能安防、图像编辑等领域。通过生成大量高质量的合成数据，可以降低对人工标注数据的依赖，加速相关算法的开发和部署。此外，SOC的可控性使得能够针对特定场景和任务生成定制化的数据集，从而提高模型的性能和泛化能力。

## 📄 摘要（原文）

> Visual grouping -- operationalized through tasks such as instance segmentation, visual grounding, and object detection -- enables applications ranging from robotic perception to photo editing. These fundamental problems in computer vision are powered by large-scale, painstakingly annotated datasets. Despite their impact, these datasets are costly to build, biased in coverage, and difficult to scale. Synthetic datasets offer a promising alternative but struggle with flexibility, accuracy, and compositional diversity.
>   We introduce Synthetic Object Compositions (SOC), an accurate and scalable data synthesis pipeline via a novel object-centric composition strategy. It composes high-quality synthetic object segments into new images using 3D geometric layout augmentation and camera configuration augmentation with generative harmonization and mask-area-weighted blending, yielding accurate and diverse masks, boxes, and referring expressions.
>   Models trained on just 100K of our synthetic images outperform those trained on larger real datasets (GRIT 20M, V3Det 200K) and synthetic pipelines (Copy-Paste, X-Paste, SynGround, SegGen) by +24-36% -- achieving +10.9 AP on LVIS and +8.4 NAcc on gRefCOCO. Beyond the general open-vocabulary setup, SOC also enables controllable dataset construction for different use cases and boosts performance in both low-data and closed-vocabulary scenarios.
>   Augmenting LVIS and COCO with synthetic object segments delivers strong performance across different real-data scales and yields even greater improvements under extremely limited real-data conditions, including +6.59 AP on a 1% COCO data setup. Furthermore, this controllability enables targeted data generation for intra-class referring, a diagnostic grounding task we propose that requires fine-grained attribute discrimination.

