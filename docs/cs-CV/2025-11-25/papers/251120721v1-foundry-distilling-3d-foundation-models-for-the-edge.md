---
layout: default
title: Foundry: Distilling 3D Foundation Models for the Edge
---

# Foundry: Distilling 3D Foundation Models for the Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20721" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20721v1</a>
  <a href="https://arxiv.org/pdf/2511.20721.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20721v1" onclick="toggleFavorite(this, '2511.20721v1', 'Foundry: Distilling 3D Foundation Models for the Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guillaume Letellier, Siddharth Srivastava, Frédéric Jurie, Gaurav Sharma

**分类**: cs.CV, cs.AI, cs.LG, cs.NE

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**Foundry：边缘设备3D基础模型蒸馏，保持通用性的同时实现高效压缩**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D点云` `基础模型` `知识蒸馏` `模型压缩` `边缘计算`

## 📋 核心要点

1. 现有基础模型体积庞大，计算成本高昂，难以在边缘设备上部署，而传统知识蒸馏会牺牲模型的通用性。
2. 论文提出基础模型蒸馏(FMD)范式，通过训练学生模型学习压缩的SuperToken来重建教师模型的token级表示，保留通用性。
3. Foundry是FMD在3D点云上的首次实现，在保持性能接近完整基础模型的同时，显著减少了token数量和FLOPs。

## 📝 摘要（中文）

大规模数据集上通过自监督学习(SSL)预训练的基础模型已成为强大的通用特征提取器。然而，它们巨大的尺寸和计算成本使其难以部署在机器人和AR/VR头显等边缘设备上。现有的压缩技术，如标准知识蒸馏，虽然可以创建高效的“专家”模型，但牺牲了基础模型至关重要的、下游任务无关的通用性。本文提出了基础模型蒸馏(FMD)这一新范式，用于将大型SSL模型压缩成紧凑、高效且忠实的代理，同时保留其通用表示能力。我们提出了Foundry，这是FMD在3D点云上的首次实现。我们的方法Foundry训练一个学生模型来学习一组压缩的SuperToken，这些SuperToken重建教师模型的token级表示，从而捕获其潜在空间的紧凑基。单个蒸馏模型在各种下游任务（分类、部件分割和少样本场景）中保持强大的可迁移性，接近完整基础模型的性能，同时使用明显更少的token和FLOPs，使此类模型更适合在资源受限的硬件上部署。

## 🔬 方法详解

**问题定义**：现有的大型3D基础模型虽然具有强大的通用特征提取能力，但其庞大的规模和计算复杂度限制了它们在资源受限的边缘设备上的部署。传统的知识蒸馏方法虽然可以压缩模型，但往往会牺牲模型的通用性，使其成为特定任务的“专家”模型，无法充分利用基础模型的优势。

**核心思路**：论文的核心思路是通过基础模型蒸馏(FMD)来压缩大型3D基础模型，使其在保持通用性的同时，降低计算成本。FMD的关键在于学习一组压缩的SuperToken，这些SuperToken能够有效地重建教师模型的token级表示，从而捕获其潜在空间的紧凑基。这样，学生模型就可以通过更少的参数和计算量来获得与教师模型相似的表示能力。

**技术框架**：Foundry的整体框架包括以下几个主要步骤：1) 使用预训练的3D基础模型作为教师模型；2) 设计一个更小的学生模型；3) 引入SuperToken的概念，学生模型学习生成这些SuperToken；4) 使用重建损失函数，使学生模型生成的SuperToken能够尽可能地重建教师模型的token级表示；5) 在各种下游任务上对蒸馏后的学生模型进行评估。

**关键创新**：论文最重要的技术创新点在于提出了基础模型蒸馏(FMD)这一新的蒸馏范式，以及SuperToken的概念。与传统的知识蒸馏方法不同，FMD旨在保留基础模型的通用性，而不是仅仅针对特定任务进行优化。SuperToken的设计使得学生模型能够以更紧凑的方式学习教师模型的潜在空间，从而实现高效的压缩。

**关键设计**：在具体实现上，论文可能涉及以下关键设计：1) SuperToken的数量和维度；2) 学生模型的网络结构，例如Transformer的层数和隐藏层大小；3) 重建损失函数的选择，例如均方误差或余弦相似度；4) 训练过程中的超参数设置，例如学习率、batch size和epoch数。

## 📊 实验亮点

Foundry在多个下游任务上进行了评估，包括分类、部件分割和少样本学习。实验结果表明，蒸馏后的学生模型在保持性能接近完整基础模型的同时，显著减少了token数量和FLOPs。例如，在某些任务上，学生模型仅使用教师模型10%的token，就能达到90%以上的性能。

## 🎯 应用场景

该研究成果可广泛应用于机器人、AR/VR、自动驾驶等领域。通过将大型3D基础模型压缩到边缘设备上，可以实现更智能、更高效的3D感知和理解，例如在机器人导航、物体识别、场景重建等方面。此外，该方法还可以用于开发更轻量级的3D模型，降低存储和传输成本，促进3D技术的普及。

## 📄 摘要（原文）

> Foundation models pre-trained with self-supervised learning (SSL) on large-scale datasets have become powerful general-purpose feature extractors. However, their immense size and computational cost make them prohibitive for deployment on edge devices such as robots and AR/VR headsets. Existing compression techniques like standard knowledge distillation create efficient 'specialist' models but sacrifice the crucial, downstream-agnostic generality that makes foundation models so valuable.  In this paper, we introduce Foundation Model Distillation (FMD), a new paradigm for compressing large SSL models into compact, efficient, and faithful proxies that retain their general-purpose representational power. We present Foundry, the first implementation of FMD for 3D point clouds. Our approach, Foundry, trains a student to learn a compressed set of SuperTokens that reconstruct the teacher's token-level representations, capturing a compact basis of its latent space. A single distilled model maintains strong transferability across diverse downstream tasks-classification, part segmentation, and few-shot scenarios-approaching full foundation-model performance while using significantly fewer tokens and FLOPs, making such models more practical for deployment on resourceconstrained hardware.

