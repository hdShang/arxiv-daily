---
layout: default
title: "Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach"
---

# Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14113" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14113v1</a>
  <a href="https://arxiv.org/pdf/2512.14113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14113v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14113v1', 'Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashish Mishra, Gyanaranjan Nayak, Tarun Kumar, Arpit Shah, Suparna Bhattacharya, Martin Foltin

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一种免训练免数据的CLIP可控选择性领域无关知识遗忘方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识遗忘` `CLIP模型` `免训练` `免数据` `零样本学习` `多模态学习` `领域自适应`

## 📋 核心要点

1. 现有CLIP模型缺乏在不重新训练或使用额外数据的情况下，选择性遗忘特定类别知识的能力，限制了其在实际应用中的灵活性。
2. 该论文提出一种免训练免数据的遗忘框架，通过文本提示和合成视觉原型，在CLIP的多模态零空间中选择性地移除不需要的类别信息。
3. 实验结果表明，该方法能够有效地实现全局、领域特定和选择性领域的知识遗忘，同时保持模型在其他任务上的性能。

## 📝 摘要（中文）

预训练模型如CLIP在各种视觉领域（包括自然图像、艺术渲染和抽象表示）都展现了出色的零样本分类能力。然而，实际应用经常需要在不进行额外数据或重新训练的情况下，移除特定的对象类别（或“遗忘”），同时不影响模型在不相关任务上的性能。本文提出了一种新颖的免训练和免数据的遗忘框架，该框架支持三种不同的遗忘范式：（1）跨所有领域的选定对象的全局遗忘；（2）领域特定知识的移除（例如，消除草图表示，同时保留照片识别）；（3）选择性领域的完全遗忘。通过协同集成文本提示和从CLIP的联合嵌入空间导出的合成视觉原型，利用多模态零空间，我们的方法有效地移除了不需要的类别信息，同时保留了剩余的知识。这种方法克服了现有基于重新训练的方法的局限性，并为受控模型遗忘提供了一种灵活且计算高效的解决方案。

## 🔬 方法详解

**问题定义**：CLIP等预训练模型虽然具有强大的零样本能力，但在实际应用中，用户可能需要移除模型中某些特定类别的知识，例如出于隐私保护或模型修正的目的。现有的方法通常需要重新训练模型或者使用额外的遗忘数据，这既耗时又耗资源，并且可能影响模型在其他任务上的性能。因此，如何在不重新训练和不使用额外数据的情况下，实现对CLIP模型的选择性知识遗忘是一个重要的挑战。

**核心思路**：该论文的核心思路是利用CLIP模型的多模态零空间，通过构造与待遗忘类别相关的文本提示和合成视觉原型，将这些类别的信息投影到零空间中，从而实现知识遗忘。这种方法的核心在于，通过精心设计的文本提示和视觉原型，可以有效地引导模型遗忘特定类别的信息，同时避免影响模型在其他任务上的性能。

**技术框架**：该方法主要包含以下几个阶段：1) **文本提示生成**：针对需要遗忘的类别，生成相应的文本提示。2) **视觉原型合成**：利用CLIP的联合嵌入空间，合成与文本提示对应的视觉原型。3) **多模态零空间构建**：将文本提示和视觉原型结合起来，构建多模态零空间。4) **知识遗忘**：将CLIP模型的参数向多模态零空间进行投影，从而实现知识遗忘。

**关键创新**：该论文最重要的技术创新点在于提出了一种免训练免数据的知识遗忘方法，该方法不需要重新训练模型或使用额外的遗忘数据，就可以实现对CLIP模型的选择性知识遗忘。此外，该方法还支持三种不同的遗忘范式：全局遗忘、领域特定遗忘和选择性领域遗忘，具有很强的灵活性和可控性。

**关键设计**：在文本提示生成方面，论文采用了多种策略，例如使用同义词、反义词等来生成不同的文本提示，以提高遗忘效果。在视觉原型合成方面，论文利用CLIP的图像编码器和文本编码器，通过优化算法来生成与文本提示对应的视觉原型。在多模态零空间构建方面，论文采用了奇异值分解（SVD）等方法来构建零空间。在知识遗忘方面，论文采用了投影算子将CLIP模型的参数向零空间进行投影。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113v1/figures/ICCV-CLIP-unlearning-method.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113v1/figures/abl11.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法能够有效地实现全局、领域特定和选择性领域的知识遗忘，同时保持模型在其他任务上的性能。例如，在全局遗忘方面，该方法可以在不影响模型在其他类别上的性能的情况下，将特定类别的识别准确率降低到接近随机水平。在领域特定遗忘方面，该方法可以在移除模型在特定领域（例如草图）的知识的同时，保持模型在其他领域（例如照片）的性能。

## 🎯 应用场景

该研究成果可应用于多种场景，例如，在保护用户隐私方面，可以移除模型中与敏感信息相关的知识；在模型修正方面，可以移除模型中错误的或过时的知识；在领域自适应方面，可以移除模型中与目标领域无关的知识。该方法具有很高的实际应用价值，有望推动预训练模型在更多领域的应用。

## 📄 摘要（原文）

> Pretrained models like CLIP have demonstrated impressive zero-shot classification capabilities across diverse visual domains, spanning natural images, artistic renderings, and abstract representations. However, real-world applications often demand the removal (or "unlearning") of specific object classes without requiring additional data or retraining, or affecting the model's performance on unrelated tasks. In this paper, we propose a novel training- and data-free unlearning framework that enables three distinct forgetting paradigms: (1) global unlearning of selected objects across all domains, (2) domain-specific knowledge removal (e.g., eliminating sketch representations while preserving photo recognition), and (3) complete unlearning in selective domains. By leveraging a multimodal nullspace through synergistic integration of text prompts and synthesized visual prototypes derived from CLIP's joint embedding space, our method efficiently removes undesired class information while preserving the remaining knowledge. This approach overcomes the limitations of existing retraining-based methods and offers a flexible and computationally efficient solution for controlled model forgetting.

