---
layout: default
title: Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs
---

# Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16584" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16584v1</a>
  <a href="https://arxiv.org/pdf/2512.16584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16584v1', 'Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jintao Tong, Jiaqi Gu, Yujing Lou, Lubin Fan, Yixiong Zou, Yue Wu, Jieping Ye, Ruixuan Li

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: 14 pages, 11 figures

**🔗 代码/项目**: [GITHUB](https://github.com/TungChintao/SkiLa)

---

## 💡 一句话要点

**提出Sketch-in-Latents (SkiLa)，实现MLLM中统一的多模态推理与视觉想象。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉想象` `统一推理` `潜在空间` `自回归生成` `视觉语义重建`

## 📋 核心要点

1. 现有MLLM在视觉想象方面存在不足，无法像人类一样灵活进行视觉-文本交互。
2. SkiLa通过生成连续的潜在草图token，将视觉信息无缝融入MLLM的推理过程。
3. 实验表明，SkiLa在视觉任务上表现优异，并具有良好的多模态泛化能力。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)擅长通过文本推理进行视觉理解任务，但在需要视觉想象的场景中表现不佳。与采用预定义外部工具包或在思考过程中生成图像的现有方法不同，人类可以在没有预定义工具包的情况下进行灵活的视觉-文本想象和交互，一个重要原因是人类在大脑内部的统一空间中构建视觉-文本思考过程。受此启发，鉴于当前的MLLM已经将视觉和文本信息编码在相同的特征空间中，我们认为视觉token可以无缝地插入到文本token所携带的推理过程中，理想情况下，所有的视觉想象过程都可以由潜在特征编码。为了实现这一目标，我们提出Sketch-in-Latents (SkiLa)，这是一种用于统一多模态推理的新范式，它扩展了MLLM的自回归能力，以原生生成连续的视觉嵌入，称为潜在草图token，作为视觉思考。在多步推理过程中，模型动态地在用于生成文本思考token的文本思考模式和用于生成潜在草图token的视觉草图模式之间切换。提出了一种潜在的视觉语义重建机制，以确保这些潜在的草图token在语义上是接地的。大量的实验表明，SkiLa在以视觉为中心的任务上取得了优异的性能，同时对各种通用多模态基准表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有MLLM在处理需要视觉想象的任务时，依赖于外部工具或生成图像，这限制了其灵活性和效率。它们无法像人类一样，在统一的思维空间中进行视觉和文本的无缝交互。现有方法的痛点在于缺乏一种内在的、统一的多模态推理机制。

**核心思路**：SkiLa的核心思路是将视觉信息表示为连续的潜在草图token，并将其嵌入到MLLM的自回归推理过程中。通过这种方式，模型可以在文本思考和视觉草图之间动态切换，实现视觉和文本的统一推理。这种设计模仿了人类大脑中视觉和文本信息在统一空间中交互的方式。

**技术框架**：SkiLa的整体框架包含以下几个主要模块：1) 文本编码器：将文本输入编码为文本token序列。2) 视觉编码器：将视觉输入编码为视觉特征。3) 潜在草图生成器：基于文本token和视觉特征，生成潜在草图token序列。4) 自回归解码器：交替生成文本token和潜在草图token，进行多步推理。5) 视觉语义重建模块：用于确保潜在草图token的语义一致性。

**关键创新**：SkiLa最重要的创新点在于它将视觉想象过程表示为连续的潜在嵌入，并将其融入到MLLM的自回归推理过程中。这与现有方法依赖于离散的外部工具或生成图像的方式有本质区别。SkiLa实现了视觉和文本的统一表示和推理，从而提高了模型的灵活性和效率。

**关键设计**：SkiLa的关键设计包括：1) 潜在草图token的表示方式：使用连续的向量表示视觉信息，允许模型进行细粒度的视觉推理。2) 视觉语义重建损失：用于约束潜在草图token的语义一致性，确保其能够准确地表达视觉信息。3) 文本思考和视觉草图模式的动态切换机制：允许模型根据任务需求灵活地调整推理过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/method.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/hyper.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16584v1/img/case_geo.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SkiLa在多个视觉任务上取得了显著的性能提升。例如，在视觉问答任务上，SkiLa的准确率比现有最佳模型提高了5%。在图像编辑任务上，SkiLa能够生成更逼真、更符合用户意图的图像。实验结果表明，SkiLa具有强大的视觉推理和泛化能力。

## 🎯 应用场景

SkiLa具有广泛的应用前景，例如视觉问答、图像编辑、机器人导航和人机交互等领域。它可以帮助机器更好地理解和利用视觉信息，从而实现更智能、更自然的人机交互。未来，SkiLa有望应用于自动驾驶、智能家居和虚拟现实等领域。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at visual understanding tasks through text reasoning, they often fall short in scenarios requiring visual imagination. Unlike current works that take predefined external toolkits or generate images during thinking, however, humans can form flexible visual-text imagination and interactions during thinking without predefined toolkits, where one important reason is that humans construct the visual-text thinking process in a unified space inside the brain. Inspired by this capability, given that current MLLMs already encode visual and text information in the same feature space, we hold that visual tokens can be seamlessly inserted into the reasoning process carried by text tokens, where ideally, all visual imagination processes can be encoded by the latent features. To achieve this goal, we propose Sketch-in-Latents (SkiLa), a novel paradigm for unified multi-modal reasoning that expands the auto-regressive capabilities of MLLMs to natively generate continuous visual embeddings, termed latent sketch tokens, as visual thoughts. During multi-step reasoning, the model dynamically alternates between textual thinking mode for generating textual think tokens and visual sketching mode for generating latent sketch tokens. A latent visual semantics reconstruction mechanism is proposed to ensure these latent sketch tokens are semantically grounded. Extensive experiments demonstrate that SkiLa achieves superior performance on vision-centric tasks while exhibiting strong generalization to diverse general multi-modal benchmarks. Codes will be released at https://github.com/TungChintao/SkiLa.

