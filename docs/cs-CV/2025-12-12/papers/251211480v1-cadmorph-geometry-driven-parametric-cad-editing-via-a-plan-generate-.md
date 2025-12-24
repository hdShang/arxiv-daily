---
layout: default
title: "CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop"
---

# CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11480" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11480v1</a>
  <a href="https://arxiv.org/pdf/2512.11480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11480v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.11480v1', 'CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijian Ma, Shizhao Sun, Ruiyu Wang, Jiang Bian

**分类**: cs.CV

**发布日期**: 2025-12-12

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**CADMorph：提出几何驱动的参数化CAD编辑框架，解决设计迭代中几何形状调整与参数序列同步编辑问题。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `CAD编辑` `参数化建模` `几何驱动` `扩散模型` `掩码预测`

## 📋 核心要点

1. 现有几何驱动的参数化CAD编辑方法难以在数据稀缺情况下，同时保证结构保持、语义有效性和形状保真度。
2. CADMorph通过计划-生成-验证循环，利用预训练的参数到形状(P2S)和掩码参数预测(MPP)模型，实现几何驱动的参数化CAD编辑。
3. 实验表明，CADMorph在CAD编辑任务上优于GPT-4o和现有CAD基线，并能支持迭代编辑和逆向工程增强等应用。

## 📝 摘要（中文）

计算机辅助设计(CAD)模型以两种耦合形式编码对象：参数化构造序列及其产生的可见几何形状。在迭代设计过程中，对几何形状的调整不可避免地需要对底层参数序列进行同步编辑，这被称为几何驱动的参数化CAD编辑。该任务要求：1)保持原始序列的结构，2)确保每次编辑的语义有效性，3)保持对目标形状的高度保真度，所有这些都在稀缺的编辑数据三元组下进行。我们提出了CADMorph，一个迭代的计划-生成-验证框架，在推理过程中协调预训练的领域特定基础模型：一个参数到形状(P2S)的潜在扩散模型和一个掩码参数预测(MPP)模型。在计划阶段，来自P2S模型的交叉注意力图精确定位需要修改的段，并提供编辑掩码。然后，MPP模型在生成阶段用语义上有效的编辑填充这些掩码。在验证过程中，P2S模型将每个候选序列嵌入到形状潜在空间中，测量其与目标形状的距离，并选择最接近的一个。这三个阶段利用了预训练先验中固有的几何意识和设计知识，从而分别解决了结构保持、语义有效性和形状保真度。此外，P2S和MPP模型都在没有三元组数据的情况下进行训练，绕过了数据稀缺的瓶颈。CADMorph超越了GPT-4o和专门的CAD基线，并支持迭代编辑和逆向工程增强等下游应用。

## 🔬 方法详解

**问题定义**：论文旨在解决几何驱动的参数化CAD编辑问题。现有方法在迭代设计过程中，当用户调整CAD模型的几何形状时，需要同步修改底层的参数化构造序列。然而，在数据稀缺的情况下，如何保持原始序列的结构、确保编辑的语义有效性以及维持对目标形状的高度保真度是一个挑战。现有方法通常难以同时满足这些要求，导致编辑结果不理想。

**核心思路**：CADMorph的核心思路是利用预训练的领域特定基础模型，即参数到形状(P2S)的潜在扩散模型和掩码参数预测(MPP)模型，通过一个迭代的计划-生成-验证循环来实现几何驱动的参数化CAD编辑。这种方法利用了预训练模型中蕴含的几何意识和设计知识，从而在数据稀缺的情况下也能较好地保持结构、保证语义有效性并维持形状保真度。

**技术框架**：CADMorph框架包含三个主要阶段：计划、生成和验证。在计划阶段，P2S模型的交叉注意力图用于定位需要修改的参数序列段，并生成编辑掩码。在生成阶段，MPP模型使用语义上有效的编辑填充这些掩码，生成候选的参数序列。在验证阶段，P2S模型将每个候选序列嵌入到形状潜在空间中，计算其与目标形状的距离，并选择距离最小的序列作为最终编辑结果。

**关键创新**：CADMorph的关键创新在于利用预训练的P2S和MPP模型来解决几何驱动的参数化CAD编辑问题。与传统方法不同，CADMorph不需要大量的编辑数据三元组进行训练，从而绕过了数据稀缺的瓶颈。此外，通过计划-生成-验证循环，CADMorph能够有效地利用预训练模型中的几何意识和设计知识，从而在结构保持、语义有效性和形状保真度方面都取得了较好的效果。

**关键设计**：P2S模型是一个潜在扩散模型，用于将参数序列映射到形状潜在空间。MPP模型用于预测被掩码的参数序列段。计划阶段使用P2S模型的交叉注意力图来确定需要编辑的区域。验证阶段使用形状潜在空间中的距离度量来评估候选序列与目标形状的相似度。P2S和MPP模型均在大量CAD数据上进行预训练，无需编辑数据三元组。

## 📊 实验亮点

CADMorph在几何驱动的参数化CAD编辑任务上取得了显著的性能提升，超越了GPT-4o和专门的CAD基线。实验结果表明，CADMorph能够有效地保持原始序列的结构，确保编辑的语义有效性，并维持对目标形状的高度保真度。此外，CADMorph在数据稀缺的情况下也能表现出良好的性能，验证了其在实际应用中的潜力。

## 🎯 应用场景

CADMorph具有广泛的应用前景，可用于CAD模型的迭代编辑、逆向工程增强、以及自动化设计流程。该方法能够帮助设计师更高效地修改和优化CAD模型，提高设计效率和质量。此外，CADMorph还可以应用于教育领域，帮助学生更好地理解和掌握CAD设计原理。

## 📄 摘要（原文）

> A Computer-Aided Design (CAD) model encodes an object in two coupled forms: a parametric construction sequence and its resulting visible geometric shape. During iterative design, adjustments to the geometric shape inevitably require synchronized edits to the underlying parametric sequence, called geometry-driven parametric CAD editing. The task calls for 1) preserving the original sequence's structure, 2) ensuring each edit's semantic validity, and 3) maintaining high shape fidelity to the target shape, all under scarce editing data triplets. We present CADMorph, an iterative plan-generate-verify framework that orchestrates pretrained domain-specific foundation models during inference: a parameter-to-shape (P2S) latent diffusion model and a masked-parameter-prediction (MPP) model. In the planning stage, cross-attention maps from the P2S model pinpoint the segments that need modification and offer editing masks. The MPP model then infills these masks with semantically valid edits in the generation stage. During verification, the P2S model embeds each candidate sequence in shape-latent space, measures its distance to the target shape, and selects the closest one. The three stages leverage the inherent geometric consciousness and design knowledge in pretrained priors, and thus tackle structure preservation, semantic validity, and shape fidelity respectively. Besides, both P2S and MPP models are trained without triplet data, bypassing the data-scarcity bottleneck. CADMorph surpasses GPT-4o and specialized CAD baselines, and supports downstream applications such as iterative editing and reverse-engineering enhancement.

