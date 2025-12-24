---
layout: default
title: "Stitch: Training-Free Position Control in Multimodal Diffusion Transformers"
---

# Stitch: Training-Free Position Control in Multimodal Diffusion Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26644" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26644v1</a>
  <a href="https://arxiv.org/pdf/2509.26644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26644v1', 'Stitch: Training-Free Position Control in Multimodal Diffusion Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jessica Bader, Mateusz Pach, Maria A. Bravo, Serge Belongie, Zeynep Akata

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-30

**备注**: Preprint

**🔗 代码/项目**: [GITHUB](https://github.com/ExplainableML/Stitch)

---

## 💡 一句话要点

**Stitch：一种免训练的多模态扩散Transformer位置控制方法**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `位置控制` `多模态扩散Transformer` `免训练方法` `图像拼接`

## 📋 核心要点

1. 现有T2I模型难以准确捕捉空间关系，且早期位置控制方法与现代模型不兼容。
2. Stitch通过自动生成边界框，在MMDiT中实现免训练的位置控制，提升空间关系准确性。
3. 实验表明，Stitch在多个模型上显著提升了空间关系生成效果，并在PosEval基准上取得了SOTA结果。

## 📝 摘要（中文）

近年来，文本到图像（T2I）生成模型发展迅速，但准确捕捉空间关系（如“上方”或“右侧”）仍然是一个挑战。早期方法通过外部位置控制来改善空间关系。然而，随着架构的演进以提高图像质量，这些技术与现代模型变得不兼容。我们提出Stitch，一种免训练的方法，通过自动生成的边界框将外部位置控制整合到多模态扩散Transformer（MMDiT）中。Stitch通过在指定的边界框内生成单个对象并将它们无缝拼接在一起，从而生成在空间上准确且视觉上吸引人的图像。我们发现，目标注意力头捕获了必要的信息，可以在生成过程中隔离和切出单个对象，而无需完全完成图像。我们在PosEval（我们用于基于位置的T2I生成的基准）上评估Stitch。PosEval包含五个新任务，扩展了位置的概念，超越了基本的GenEval任务，表明即使是顶级模型在基于位置的生成方面仍有很大的改进空间。在Qwen-Image、FLUX和SD3.5上测试，Stitch始终增强了基础模型，甚至在GenEval的位置任务上将FLUX提高了218%，在PosEval上提高了206%。Stitch在PosEval上使用Qwen-Image实现了最先进的结果，比以前的模型提高了54%，所有这些都是在无需训练的情况下将位置控制集成到领先模型中实现的。

## 🔬 方法详解

**问题定义**：论文旨在解决文本到图像生成模型中，难以准确控制生成对象空间位置关系的问题。现有方法要么依赖于额外的训练，要么与最新的图像生成模型架构不兼容，无法在保证图像质量的同时实现精确的位置控制。

**核心思路**：Stitch的核心思路是利用多模态扩散Transformer（MMDiT）中已经存在的注意力机制，通过自动生成的边界框来引导模型在指定区域内生成特定对象，然后将这些对象无缝拼接在一起。这种方法无需额外的训练，可以直接应用于现有的预训练模型。

**技术框架**：Stitch方法的整体流程如下：1. 给定文本提示和目标对象的边界框位置。2. 利用预训练的MMDiT模型进行图像生成，但在生成过程中，模型会根据边界框的位置信息，将注意力集中在对应的区域。3. 在每个边界框内独立生成对象。4. 将生成的对象无缝拼接在一起，形成最终的图像。

**关键创新**：Stitch的关键创新在于它是一种免训练的方法，可以直接应用于现有的预训练模型，而无需进行额外的训练或微调。此外，Stitch还利用了MMDiT模型中已经存在的注意力机制，通过边界框来引导模型生成对象，从而实现了精确的位置控制。

**关键设计**：Stitch的关键设计包括：1. 自动生成边界框：论文使用了一种自动生成边界框的方法，可以根据文本提示自动确定对象的位置和大小。2. 注意力引导：在图像生成过程中，模型会根据边界框的位置信息，将注意力集中在对应的区域，从而保证生成的对象位于指定的位置。3. 无缝拼接：论文使用了一种无缝拼接技术，可以将生成的对象无缝拼接在一起，从而保证最终图像的质量。

## 📊 实验亮点

Stitch在PosEval基准测试中表现出色，显著提升了Qwen-Image、FLUX和SD3.5等模型的性能。例如，在GenEval的位置任务上，Stitch将FLUX模型提高了218%，在PosEval上提高了206%。Stitch在PosEval上使用Qwen-Image实现了最先进的结果，比以前的模型提高了54%。这些结果表明Stitch是一种有效且通用的位置控制方法。

## 🎯 应用场景

Stitch技术可应用于图像编辑、内容创作、虚拟现实等领域。例如，用户可以通过指定物体的位置和描述，快速生成符合要求的图像。在虚拟现实中，可以用于创建具有精确空间布局的虚拟场景。该技术有望提升图像生成的可控性和实用性，降低图像编辑的门槛。

## 📄 摘要（原文）

> Text-to-Image (T2I) generation models have advanced rapidly in recent years, but accurately capturing spatial relationships like "above" or "to the right of" poses a persistent challenge. Earlier methods improved spatial relationship following with external position control. However, as architectures evolved to enhance image quality, these techniques became incompatible with modern models. We propose Stitch, a training-free method for incorporating external position control into Multi-Modal Diffusion Transformers (MMDiT) via automatically-generated bounding boxes. Stitch produces images that are both spatially accurate and visually appealing by generating individual objects within designated bounding boxes and seamlessly stitching them together. We find that targeted attention heads capture the information necessary to isolate and cut out individual objects mid-generation, without needing to fully complete the image. We evaluate Stitch on PosEval, our benchmark for position-based T2I generation. Featuring five new tasks that extend the concept of Position beyond the basic GenEval task, PosEval demonstrates that even top models still have significant room for improvement in position-based generation. Tested on Qwen-Image, FLUX, and SD3.5, Stitch consistently enhances base models, even improving FLUX by 218% on GenEval's Position task and by 206% on PosEval. Stitch achieves state-of-the-art results with Qwen-Image on PosEval, improving over previous models by 54%, all accomplished while integrating position control into leading models training-free. Code is available at https://github.com/ExplainableML/Stitch.

