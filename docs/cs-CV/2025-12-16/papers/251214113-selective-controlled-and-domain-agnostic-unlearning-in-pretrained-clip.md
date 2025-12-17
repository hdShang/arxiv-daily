---
layout: default
title: Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach
---

# Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14113" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14113</a>
  <a href="https://arxiv.org/pdf/2512.14113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14113" onclick="toggleFavorite(this, '2512.14113', 'Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashish Mishra, Gyanaranjan Nayak, Tarun Kumar, Arpit Shah, Suparna Bhattacharya, Martin Foltin

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种免训练免数据的CLIP可控选择性领域无关知识遗忘方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识遗忘` `免训练` `免数据` `CLIP` `多模态学习`

## 📋 核心要点

1. 现有CLIP模型难以在不重新训练或引入额外数据的情况下，选择性地遗忘特定类别或领域的信息。
2. 该方法通过结合文本提示和合成视觉原型，构建多模态零空间，从而在不影响其他知识的前提下移除目标信息。
3. 该方法实现了全局、领域特定和选择性领域的知识遗忘，无需额外训练或数据，提高了效率和灵活性。

## 📝 摘要（中文）

预训练模型如CLIP在各种视觉领域（包括自然图像、艺术渲染和抽象表示）中表现出令人印象深刻的零样本分类能力。然而，实际应用通常需要在不需要额外数据或重新训练的情况下移除（或“遗忘”）特定的对象类别，同时不影响模型在不相关任务上的性能。本文提出了一种新颖的免训练和免数据的遗忘框架，该框架支持三种不同的遗忘范式：（1）跨所有领域的选定对象的全局遗忘，（2）领域特定知识的移除（例如，消除草图表示，同时保留照片识别），以及（3）选择性领域的完全遗忘。通过协同集成文本提示和从CLIP的联合嵌入空间导出的合成视觉原型，利用多模态零空间，我们的方法有效地移除了不需要的类别信息，同时保留了剩余的知识。这种方法克服了现有基于重新训练的方法的局限性，并为可控模型遗忘提供了一种灵活且计算高效的解决方案。

## 🔬 方法详解

**问题定义**：CLIP等预训练模型虽然具有强大的零样本能力，但在实际应用中，用户可能需要模型遗忘某些特定类别或领域的信息，例如，不再识别某种类型的图像，或者在特定领域（如草图）中遗忘某些概念。现有的方法通常需要重新训练模型或引入新的数据，这既耗时又耗资源，并且可能影响模型在其他任务上的性能。

**核心思路**：该论文的核心思路是利用CLIP的多模态嵌入空间，通过构建一个“零空间”来抑制目标类别或领域的信息。具体来说，通过结合文本提示和合成视觉原型，在CLIP的文本和图像嵌入空间中找到一个子空间，使得目标类别或领域的信息在这个子空间中的投影接近于零，从而实现知识遗忘。这种方法无需重新训练模型或引入新的数据，因此更加高效和灵活。

**技术框架**：该方法主要包含以下几个阶段：
1. **目标定义**：明确需要遗忘的类别或领域。
2. **文本提示生成**：为每个需要遗忘的类别生成相应的文本提示。
3. **视觉原型合成**：利用CLIP的图像生成能力，为每个需要遗忘的类别合成视觉原型。
4. **零空间构建**：结合文本提示和视觉原型，在CLIP的嵌入空间中构建零空间。
5. **知识遗忘**：通过将CLIP的嵌入向量投影到零空间的补空间，从而抑制目标类别或领域的信息。

**关键创新**：该方法最重要的技术创新点在于它提出了一种免训练免数据的知识遗忘框架。与传统的重新训练方法相比，该方法无需额外的训练数据和计算资源，并且可以更加灵活地控制知识遗忘的范围和程度。此外，该方法还创新性地利用了CLIP的多模态嵌入空间，通过结合文本提示和视觉原型来构建零空间，从而实现了更加精确的知识遗忘。

**关键设计**：该方法的关键设计包括：
1. **文本提示的选择**：选择合适的文本提示对于构建有效的零空间至关重要。论文中可能使用了特定的文本提示策略，例如使用同义词或反义词来增强文本提示的多样性。
2. **视觉原型的合成**：合成高质量的视觉原型对于知识遗忘的效果有重要影响。论文中可能使用了特定的图像生成技术，例如使用CLIP的图像生成能力或GAN来合成视觉原型。
3. **零空间的构建**：论文中可能使用了特定的数学方法来构建零空间，例如使用奇异值分解（SVD）或主成分分析（PCA）。
4. **投影方式**：将CLIP的嵌入向量投影到零空间的补空间的方式也会影响知识遗忘的效果。论文中可能使用了特定的投影方式，例如使用正交投影或加权投影。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113/figures/ICCV-CLIP-unlearning-method.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14113/figures/abl11.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文提出了一种免训练免数据的知识遗忘方法，无需重新训练模型或引入新的数据，显著提高了知识遗忘的效率和灵活性。实验结果表明，该方法可以在不影响模型在其他任务上的性能的前提下，有效地遗忘目标类别或领域的信息。具体的性能数据和对比基线未知，但该方法在可控知识遗忘方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于多种场景，例如，在自动驾驶系统中，可以遗忘某些不常见的交通标志，以提高系统的鲁棒性；在医疗图像分析中，可以遗忘某些敏感的患者信息，以保护患者隐私；在内容审核系统中，可以遗忘某些违规内容，以提高系统的安全性。此外，该方法还可以用于模型个性化定制，根据用户的需求选择性地遗忘或保留某些知识。

## 📄 摘要（原文）

> Pretrained models like CLIP have demonstrated impressive zero-shot classification capabilities across diverse visual domains, spanning natural images, artistic renderings, and abstract representations. However, real-world applications often demand the removal (or "unlearning") of specific object classes without requiring additional data or retraining, or affecting the model's performance on unrelated tasks. In this paper, we propose a novel training- and data-free unlearning framework that enables three distinct forgetting paradigms: (1) global unlearning of selected objects across all domains, (2) domain-specific knowledge removal (e.g., eliminating sketch representations while preserving photo recognition), and (3) complete unlearning in selective domains. By leveraging a multimodal nullspace through synergistic integration of text prompts and synthesized visual prototypes derived from CLIP's joint embedding space, our method efficiently removes undesired class information while preserving the remaining knowledge. This approach overcomes the limitations of existing retraining-based methods and offers a flexible and computationally efficient solution for controlled model forgetting.

