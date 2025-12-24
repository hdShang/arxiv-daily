---
layout: default
title: "Rethinking Sparse Autoencoders: Select-and-Project for Fairness and Control from Encoder Features Alone"
---

# Rethinking Sparse Autoencoders: Select-and-Project for Fairness and Control from Encoder Features Alone

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10809" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10809v2</a>
  <a href="https://arxiv.org/pdf/2509.10809.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10809v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10809v2', 'Rethinking Sparse Autoencoders: Select-and-Project for Fairness and Control from Encoder Features Alone')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Bărbălau, Cristian Daniel Păduraru, Teodor Poncu, Alexandru Tifrea, Elena Burceanu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-13 (更新: 2025-12-05)

---

## 💡 一句话要点

**提出S&P Top-K，一种encoder-centric的稀疏自编码器改进方法，用于提升模型公平性和可控性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `模型操控` `公平性` `可控性` `编码器干预` `视觉-语言模型` `大型语言模型`

## 📋 核心要点

1. 传统稀疏自编码器(SAE)依赖解码器修改中间表示进行模型操控，存在跨模态性能瓶颈。
2. 提出S&P Top-K框架，通过选择和投影编码器特征，直接在模型原生嵌入空间进行干预。
3. 实验表明，S&P Top-K在视觉-语言模型和大型语言模型中显著提升了公平性和可控性。

## 📝 摘要（中文）

稀疏自编码器(SAEs)被广泛应用于机制可解释性和模型操控。通常，模型操控通过解码修改后的SAE中间表示来实现，本质上是将原始激活重写为解码器特征的加权和。与现有文献不同，本文提出了一种以编码器为中心的模型操控替代方案，该方案展示了更强的跨模态性能。我们引入了S&P Top-K，一种无需重新训练且计算量轻的Selection and Projection框架，用于识别与敏感属性或行为对齐的Top-K编码器特征，可选择性地将它们聚合为单个控制轴，并计算正交投影，随后直接应用于模型的原生嵌入空间。在视觉-语言模型中，它在CelebA和FairFace上将公平性指标提高了高达3.2倍，在大型语言模型中，它显著降低了Llama-3 8B Instruct的攻击性和谄媚性，实现了高达3.6倍的增益。这些发现表明，与传统的以解码器为中心的SAE使用相比，以编码器为中心的干预提供了一种通用、高效且更有效的机制，用于在推理时塑造模型行为。

## 🔬 方法详解

**问题定义**：现有基于稀疏自编码器（SAE）的模型操控方法主要依赖于解码器，通过修改SAE的中间表示来实现对模型行为的干预。这种方法的痛点在于，解码器可能无法充分捕捉到编码器中蕴含的全部信息，导致操控效果受限，尤其是在跨模态任务中表现不佳。此外，解码器中心的干预方式可能引入额外的计算负担和复杂性。

**核心思路**：本文的核心思路是转变视角，从编码器入手，直接在编码器的特征空间中进行干预。通过选择与特定属性或行为相关的Top-K个编码器特征，并进行投影操作，从而在模型的原生嵌入空间中实现对模型行为的精确控制。这种方法避免了对解码器的依赖，简化了干预流程，并有望提升干预效果。

**技术框架**：S&P Top-K框架主要包含以下几个阶段：1) **特征选择**：基于某种度量标准（例如，特征与敏感属性的相关性），从编码器的特征空间中选择Top-K个最相关的特征。2) **特征聚合（可选）**：将选定的Top-K个特征聚合为一个单一的控制轴，用于后续的投影操作。3) **正交投影**：计算一个正交投影矩阵，将模型的嵌入向量投影到与控制轴正交的空间中。4) **干预应用**：将计算得到的正交投影应用于模型的原生嵌入空间，从而实现对模型行为的干预。

**关键创新**：S&P Top-K框架的关键创新在于其以编码器为中心的干预策略。与传统的解码器中心方法相比，S&P Top-K直接在编码器的特征空间中进行操作，避免了对解码器的依赖，简化了干预流程，并有望提升干预效果。此外，S&P Top-K是一种无需重新训练的方法，计算量轻，易于部署和应用。

**关键设计**：S&P Top-K框架的关键设计包括：1) **Top-K选择策略**：如何选择与特定属性或行为相关的Top-K个特征？可以使用相关性分析、互信息等方法来衡量特征与属性之间的关系。2) **特征聚合方法**：如果选择将Top-K个特征聚合为一个控制轴，应该采用何种聚合方法？可以使用简单的平均、加权平均等方法。3) **正交投影的计算**：如何计算正交投影矩阵？可以使用线性代数中的正交化方法，例如Gram-Schmidt正交化。

## 📊 实验亮点

实验结果表明，S&P Top-K框架在视觉-语言模型（CelebA和FairFace数据集）上将公平性指标提高了高达3.2倍，在大型语言模型（Llama-3 8B Instruct）上显著降低了攻击性和谄媚性，实现了高达3.6倍的增益。这些结果表明，S&P Top-K是一种有效且高效的模型操控方法，优于传统的基于解码器的SAE方法。

## 🎯 应用场景

该研究成果可广泛应用于需要提升模型公平性和可控性的领域，例如人脸识别、自然语言处理等。通过S&P Top-K框架，可以有效地减少模型对敏感属性的偏见，提升模型在特定场景下的行为可控性，从而提高模型的可靠性和安全性。未来，该方法有望应用于更多复杂的模型和任务中，为人工智能的健康发展做出贡献。

## 📄 摘要（原文）

> Sparse Autoencoders (SAEs) are widely employed for mechanistic interpretability and model steering. Within this context, steering is by design performed by means of decoding altered SAE intermediate representations. This procedure essentially rewrites the original activations as a weighted sum of decoder features. In contrast to existing literature, we forward an encoder-centric alternative to model steering which demonstrates a stronger cross-modal performance. We introduce S&P Top-K, a retraining-free and computationally lightweight Selection and Projection framework that identifies Top-K encoder features aligned with a sensitive attribute or behavior, optionally aggregates them into a single control axis, and computes an orthogonal projection to be subsequently applied directly in the model's native embedding space. In vision-language models, it improves fairness metrics on CelebA and FairFace by up to 3.2 times over conventional SAE usage, and in large language models, it substantially reduces aggressiveness and sycophancy in Llama-3 8B Instruct, achieving up to 3.6 times gains over masked reconstruction. These findings suggest that encoder-centric interventions provide a general, efficient, and more effective mechanism for shaping model behavior at inference time than the traditional decoder-centric use of SAEs.

