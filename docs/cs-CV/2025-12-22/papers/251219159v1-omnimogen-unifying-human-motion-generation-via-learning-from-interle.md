---
layout: default
title: "OmniMoGen: Unifying Human Motion Generation via Learning from Interleaved Text-Motion Instructions"
---

# OmniMoGen: Unifying Human Motion Generation via Learning from Interleaved Text-Motion Instructions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19159" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19159v1</a>
  <a href="https://arxiv.org/pdf/2512.19159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19159v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19159v1', 'OmniMoGen: Unifying Human Motion Generation via Learning from Interleaved Text-Motion Instructions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wendong Bu, Kaihang Pan, Yuze Lin, Jiacheng Li, Kai Shen, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang

**分类**: cs.CV

**发布日期**: 2025-12-22

**🔗 代码/项目**: [PROJECT_PAGE](https://OmniMoGen.github.io/)

---

## 💡 一句话要点

**OmniMoGen：通过学习交错的文本-动作指令，统一了人体运动生成任务。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人体运动生成` `文本到运动` `运动编辑` `交错指令学习` `统一框架`

## 📋 核心要点

1. 现有运动生成方法局限于孤立任务，缺乏自由形式和全目标生成的灵活性。
2. OmniMoGen通过学习交错的文本-动作指令，统一了多种运动生成任务，实现通用运动生成。
3. OmniMoGen在文本到运动、运动编辑和AnyContext基准上取得了SOTA性能，并展现了新兴能力。

## 📝 摘要（中文）

大型语言模型（LLMs）已在单个框架内统一了各种语言任务，但这种统一性在人体运动生成中仍未被探索。现有方法仅限于孤立的任务，限制了自由形式和全目标生成的灵活性。为了解决这个问题，我们提出了OmniMoGen，一个统一的框架，它通过交错的文本-动作指令实现多功能的运动生成。OmniMoGen建立在一个简洁的RVQ-VAE和Transformer架构之上，支持端到端的指令驱动运动生成。我们构建了一个大规模的X2Mo数据集，包含超过137K的交错文本-动作指令，并引入了AnyContext，一个用于评估交错运动生成的基准。实验表明，OmniMoGen在文本到运动、运动编辑和AnyContext上实现了最先进的性能，展现了诸如组合编辑、自我反思生成和知识驱动生成等新兴能力。这些结果标志着朝着下一代智能运动生成迈出了一步。

## 🔬 方法详解

**问题定义**：现有的人体运动生成方法通常针对特定任务设计，例如文本到运动、运动编辑等，缺乏通用性和灵活性。用户难以通过自由组合文本和动作指令来控制运动生成过程，限制了应用场景。现有方法难以处理复杂的、多目标的运动生成任务。

**核心思路**：论文的核心思路是将各种运动生成任务统一到一个框架下，通过学习交错的文本-动作指令，使模型能够理解和生成复杂的运动序列。通过将文本和动作视为统一的输入模态，模型可以根据上下文信息生成更自然、更符合用户意图的运动。

**技术框架**：OmniMoGen框架基于RVQ-VAE（Residual Vector Quantized Variational Autoencoder）和Transformer架构。RVQ-VAE用于将连续的运动数据离散化为码本，Transformer则用于学习文本和离散化运动码之间的关系。整个框架支持端到端的训练，可以直接根据交错的文本-动作指令生成运动序列。框架包含编码器、解码器和量化模块。

**关键创新**：OmniMoGen的关键创新在于其统一的框架设计，能够处理多种运动生成任务。通过学习交错的文本-动作指令，模型能够理解复杂的上下文信息，并生成更符合用户意图的运动。此外，X2Mo数据集的构建和AnyContext基准的提出，为交错运动生成的研究提供了数据和评估标准。

**关键设计**：RVQ-VAE的码本大小、Transformer的网络结构（层数、注意力头数等）、损失函数的设计（包括重构损失、量化损失等）是关键的设计细节。论文还可能采用了特定的数据增强方法来提高模型的泛化能力。具体的参数设置和网络结构需要在论文中查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19159v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19159v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19159v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OmniMoGen在文本到运动、运动编辑和AnyContext基准上取得了SOTA性能。在AnyContext基准上，OmniMoGen显著优于现有方法，展现了强大的交错运动生成能力。此外，OmniMoGen还展现了组合编辑、自我反思生成和知识驱动生成等新兴能力，证明了其在复杂运动生成任务上的潜力。

## 🎯 应用场景

OmniMoGen具有广泛的应用前景，例如虚拟现实、游戏开发、动画制作、机器人控制等。它可以用于生成各种自然的人体运动，例如行走、跑步、跳跃、舞蹈等。通过结合文本指令，用户可以精确地控制运动的风格、速度、方向等。此外，OmniMoGen还可以用于运动编辑，例如修改运动的姿势、节奏等。未来，该技术有望应用于智能康复、人机交互等领域。

## 📄 摘要（原文）

> Large language models (LLMs) have unified diverse linguistic tasks within a single framework, yet such unification remains unexplored in human motion generation. Existing methods are confined to isolated tasks, limiting flexibility for free-form and omni-objective generation. To address this, we propose OmniMoGen, a unified framework that enables versatile motion generation through interleaved text-motion instructions. Built upon a concise RVQ-VAE and transformer architecture, OmniMoGen supports end-to-end instruction-driven motion generation. We construct X2Mo, a large-scale dataset of over 137K interleaved text-motion instructions, and introduce AnyContext, a benchmark for evaluating interleaved motion generation. Experiments show that OmniMoGen achieves state-of-the-art performance on text-to-motion, motion editing, and AnyContext, exhibiting emerging capabilities such as compositional editing, self-reflective generation, and knowledge-informed generation. These results mark a step toward the next intelligent motion generation. Project Page: https://OmniMoGen.github.io/.

