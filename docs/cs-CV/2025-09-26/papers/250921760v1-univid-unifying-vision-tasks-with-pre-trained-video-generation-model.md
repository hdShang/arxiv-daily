---
layout: default
title: "UniVid: Unifying Vision Tasks with Pre-trained Video Generation Models"
---

# UniVid: Unifying Vision Tasks with Pre-trained Video Generation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21760" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21760v1</a>
  <a href="https://arxiv.org/pdf/2509.21760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21760v1', 'UniVid: Unifying Vision Tasks with Pre-trained Video Generation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lan Chen, Yuchao Gu, Qi Mao

**分类**: cs.CV

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/CUC-MIPG/UniVid)

---

## 💡 一句话要点

**UniVid：利用预训练视频生成模型统一视觉任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成模型` `视觉任务统一` `跨模态学习` `扩散模型` `视觉句子`

## 📋 核心要点

1. 现有视觉模型通常需要针对特定任务进行预训练，成本高昂且难以扩展到新任务。
2. UniVid利用预训练的视频生成模型，通过视觉句子的形式统一表示各种视觉任务，无需任务特定修改。
3. 实验表明，UniVid在跨模态推理和跨源任务上表现出良好的泛化能力，并能灵活切换理解和生成任务。

## 📝 摘要（中文）

大型语言模型通过在广泛语料库上训练，成功地将各种语言任务统一在一个生成框架中。受此启发，最近的大型视觉模型（LVM）通过将任务组织成顺序视觉句子，将这种范式扩展到视觉领域，其中视觉提示作为指导输出的上下文。然而，这种建模需要在跨模态和来源的任务特定预训练，这既昂贵又限制了对未见任务的可扩展性。鉴于预训练的视频生成模型固有地捕获了时间序列依赖关系，我们探索了一种更统一和可扩展的替代方案：预训练的视频生成模型能否适应各种图像和视频任务？为了回答这个问题，我们提出了UniVid，一个微调视频扩散Transformer以处理各种视觉任务的框架，无需任务特定的修改。任务被表示为视觉句子，其中上下文序列定义了任务和预期的输出模态。我们从两个角度评估UniVid的泛化能力：（1）具有由图像和视频组成的上下文的跨模态推理，超越了LVM的单模态设置；（2）从自然数据到标注数据的跨源任务，无需多源预训练。尽管仅在自然视频数据上训练，UniVid在这两种设置中都表现出良好的泛化能力。值得注意的是，通过简单地反转这种范式中的视觉句子顺序，可以轻松切换理解和生成任务。这些发现突出了预训练视频生成模型作为视觉建模的可扩展和统一基础的潜力。我们的代码将在https://github.com/CUC-MIPG/UniVid发布。

## 🔬 方法详解

**问题定义**：现有的大型视觉模型（LVM）虽然能够统一多种视觉任务，但需要针对特定任务进行预训练，这限制了其可扩展性和泛化能力。此外，现有方法通常局限于单模态输入，难以处理图像和视频混合的复杂场景。

**核心思路**：UniVid的核心思路是利用预训练的视频生成模型所具备的时间序列建模能力，将各种视觉任务转化为视觉句子的形式。通过微调视频扩散Transformer，使模型能够理解并生成不同模态的视觉内容，从而实现任务的统一表示和处理。这种方法避免了任务特定的预训练，提高了模型的泛化能力。

**技术框架**：UniVid的整体框架包括以下几个主要步骤：1) 将视觉任务表示为视觉句子，其中包含上下文序列（例如，输入图像或视频）和目标序列（例如，任务的输出）。2) 使用预训练的视频扩散Transformer作为基础模型。3) 对基础模型进行微调，使其能够根据输入的视觉句子生成相应的输出。4) 通过反转视觉句子的顺序，可以轻松切换理解和生成任务。

**关键创新**：UniVid最重要的创新点在于利用预训练的视频生成模型来统一视觉任务。与现有方法相比，UniVid无需任务特定的预训练，能够处理跨模态输入，并且可以灵活切换理解和生成任务。这种方法具有更高的可扩展性和泛化能力。

**关键设计**：UniVid的关键设计包括：1) 使用视频扩散Transformer作为基础模型，以充分利用其时间序列建模能力。2) 将视觉任务表示为视觉句子，以便模型能够理解任务的上下文和目标。3) 通过微调策略，使模型能够适应各种视觉任务，而无需修改其网络结构。

## 📊 实验亮点

UniVid在跨模态推理和跨源任务上表现出良好的泛化能力。例如，在仅使用自然视频数据训练的情况下，UniVid能够成功处理来自标注数据的任务。此外，通过简单地反转视觉句子的顺序，UniVid可以轻松切换理解和生成任务，展示了其强大的灵活性。

## 🎯 应用场景

UniVid具有广泛的应用前景，例如视频编辑、图像修复、视频预测、视觉问答等。该研究的实际价值在于提供了一种更通用、更可扩展的视觉建模方法，可以降低开发成本，并促进视觉智能在各个领域的应用。未来，UniVid可以进一步扩展到更多模态和任务，例如结合文本信息，实现更复杂的视觉理解和生成。

## 📄 摘要（原文）

> Large language models, trained on extensive corpora, successfully unify diverse linguistic tasks within a single generative framework. Inspired by this, recent works like Large Vision Model (LVM) extend this paradigm to vision by organizing tasks into sequential visual sentences, where visual prompts serve as the context to guide outputs. However, such modeling requires task-specific pre-training across modalities and sources, which is costly and limits scalability to unseen tasks. Given that pre-trained video generation models inherently capture temporal sequence dependencies, we explore a more unified and scalable alternative: can a pre-trained video generation model adapt to diverse image and video tasks? To answer this, we propose UniVid, a framework that fine-tunes a video diffusion transformer to handle various vision tasks without task-specific modifications. Tasks are represented as visual sentences, where the context sequence defines both the task and the expected output modality. We evaluate the generalization of UniVid from two perspectives: (1) cross-modal inference with contexts composed of both images and videos, extending beyond LVM's uni-modal setting; (2) cross-source tasks from natural to annotated data, without multi-source pre-training. Despite being trained solely on natural video data, UniVid generalizes well in both settings. Notably, understanding and generation tasks can easily switch by simply reversing the visual sentence order in this paradigm. These findings highlight the potential of pre-trained video generation models to serve as a scalable and unified foundation for vision modeling. Our code will be released at https://github.com/CUC-MIPG/UniVid.

