---
layout: default
title: Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding
---

# Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17817" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17817v1</a>
  <a href="https://arxiv.org/pdf/2512.17817.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17817v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17817v1', 'Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**Chorus：多教师预训练用于整体3D高斯场景编码**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D高斯溅射` `多教师学习` `预训练` `场景编码` `知识蒸馏`

## 📋 核心要点

1. 现有3DGS场景表示缺乏通用的特征编码能力，限制了其在各种下游任务中的应用。
2. Chorus利用多教师预训练框架，从2D基础模型中提取互补信息，学习3DGS场景的整体编码。
3. 实验表明，Chorus在语义分割、实例分割等任务上表现出色，且在数据高效性和跨域迁移方面具有优势。

## 📝 摘要（中文）

3D高斯溅射(3DGS)已成为一种高保真场景表示方法，但直接从其图元中编码丰富的、通用的特征仍未得到充分探索。我们通过引入Chorus来解决这一差距，Chorus是一个多教师预训练框架，通过从2D基础模型中提取互补信号来学习整体前馈3DGS场景编码器。Chorus采用共享的3D编码器和特定于教师的投影器，从语言对齐的、通用的和对象感知的教师那里学习，从而鼓励共享嵌入空间，该空间捕获从高级语义到精细结构的信号。我们在广泛的任务中评估Chorus：开放词汇语义和实例分割、线性探测和解码器探测，以及数据高效监督。除了3DGS，我们还在几个仅支持点云的基准上测试Chorus，方法是预训练一个仅使用高斯中心、颜色、估计法线作为输入的变体。有趣的是，这个编码器显示出强大的迁移能力，并且优于点云基线，同时使用的训练场景减少了39.9倍。最后，我们提出了一种渲染和蒸馏的自适应方法，以促进领域外的微调。我们的代码和模型将在发布后发布。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射(3DGS)场景表示方法虽然在渲染质量上表现出色，但缺乏直接从3DGS图元中提取通用特征的能力。这限制了3DGS在各种需要高级语义理解和推理的下游任务中的应用，例如开放词汇语义分割和实例分割。现有的方法要么依赖于2D图像的特征，要么直接处理点云，无法充分利用3DGS的结构化信息。

**核心思路**：Chorus的核心思路是通过多教师预训练，将2D基础模型的知识迁移到3DGS场景编码器中。通过从多个具有互补能力的2D教师模型（例如，语言对齐模型、通用模型和对象感知模型）中提取信息，Chorus能够学习到更丰富、更通用的3DGS场景表示。这种方法旨在弥合2D和3D之间的差距，并充分利用预训练模型的强大能力。

**技术框架**：Chorus框架包含一个共享的3D编码器和多个特定于教师的投影器。3D编码器负责将3DGS图元（例如，高斯中心、颜色、法线等）编码成特征向量。每个教师模型都有一个对应的投影器，负责将教师模型的输出映射到与3D编码器输出相同的嵌入空间。训练过程中，通过最小化3D编码器输出和教师模型输出之间的差异，将知识从教师模型迁移到3D编码器。框架还包含一个渲染和蒸馏的自适应方法，以促进领域外的微调。

**关键创新**：Chorus的关键创新在于其多教师预训练策略。与传统的单教师蒸馏方法相比，Chorus能够从多个具有互补能力的教师模型中学习，从而获得更全面、更鲁棒的场景表示。此外，Chorus还提出了一种渲染和蒸馏的自适应方法，能够有效地将模型迁移到新的领域。

**关键设计**：3D编码器可以使用各种网络结构，例如MLP或Transformer。教师投影器通常是简单的线性层或MLP。损失函数通常采用对比损失或均方误差损失，用于衡量3D编码器输出和教师模型输出之间的差异。渲染和蒸馏的自适应方法涉及将3D场景渲染成2D图像，然后使用教师模型对渲染图像进行处理，并将教师模型的输出作为3D编码器的目标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17817v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17817v1/figs/view_selection.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17817v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Chorus在多个任务上取得了显著的性能提升。例如，在开放词汇语义分割任务中，Chorus优于现有的点云基线方法。更重要的是，通过仅使用高斯中心、颜色和法线进行预训练，Chorus在点云基准测试中表现出色，同时使用的训练场景减少了39.9倍，展示了其强大的数据效率和泛化能力。渲染和蒸馏的自适应方法也成功地将模型迁移到新的领域。

## 🎯 应用场景

Chorus具有广泛的应用前景，包括但不限于：机器人导航、自动驾驶、虚拟现实/增强现实、三维场景理解与编辑等。通过学习通用的3D场景表示，Chorus能够提升这些应用在复杂环境中的感知和推理能力，实现更智能、更高效的交互。未来，Chorus有望成为3D场景理解领域的重要基础模型。

## 📄 摘要（原文）

> While 3DGS has emerged as a high-fidelity scene representation, encoding rich, general-purpose features directly from its primitives remains under-explored. We address this gap by introducing Chorus, a multi-teacher pretraining framework that learns a holistic feed-forward 3D Gaussian Splatting (3DGS) scene encoder by distilling complementary signals from 2D foundation models. Chorus employs a shared 3D encoder and teacher-specific projectors to learn from language-aligned, generalist, and object-aware teachers, encouraging a shared embedding space that captures signals from high-level semantics to fine-grained structure.
>   We evaluate Chorus on a wide range of tasks: open-vocabulary semantic and instance segmentation, linear and decoder probing, as well as data-efficient supervision. Besides 3DGS, we also test Chorus on several benchmarks that only support point clouds by pretraining a variant using only Gaussians' centers, colors, estimated normals as inputs. Interestingly, this encoder shows strong transfer and outperforms the point clouds baseline while using 39.9 times fewer training scenes. Finally, we propose a render-and-distill adaptation that facilitates out-of-domain finetuning. Our code and model will be released upon publication.

