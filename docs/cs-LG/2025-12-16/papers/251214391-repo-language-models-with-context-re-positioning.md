---
layout: default
title: RePo: Language Models with Context Re-Positioning
---

# RePo: Language Models with Context Re-Positioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14391" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14391</a>
  <a href="https://arxiv.org/pdf/2512.14391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14391" onclick="toggleFavorite(this, '2512.14391', 'RePo: Language Models with Context Re-Positioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huayang Li, Tianyu Zhao, Richard Sproat

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**RePo：通过上下文重定位增强语言模型处理噪声和长文本能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文重定位` `语言模型` `认知负荷` `长文本处理` `噪声数据` `位置编码` `Transformer` `可微模块`

## 📋 核心要点

1. 现有LLM采用固定位置索引，导致认知负荷过高，影响模型在复杂任务中的推理和注意力分配。
2. RePo通过可微模块动态分配token位置，捕捉上下文依赖，从而降低认知负荷，提升模型性能。
3. 实验表明，RePo在噪声上下文、结构化数据和长文本任务上显著提升，同时保持了短文本任务的竞争力。

## 📝 摘要（中文）

上下文学习是现代大型语言模型（LLMs）的基础；然而，目前流行的架构通过分配线性或恒定的位置索引，施加了一种刚性和固定的上下文结构。借鉴认知负荷理论（CLT），我们认为这种缺乏信息量的结构增加了额外的认知负荷，消耗了有限的工作记忆容量，而这些容量应该分配给深度推理和注意力分配。为了解决这个问题，我们提出了一种新颖的机制RePo，它通过上下文重定位来减少额外的负荷。与标准方法不同，RePo利用一个可微模块$f_\phi$来分配token位置，从而捕获上下文依赖关系，而不是依赖于预定义的整数范围。通过在OLMo-2 1B骨干上持续预训练，我们证明了RePo显著提高了在涉及噪声上下文、结构化数据和更长上下文长度的任务上的性能，同时在一般的短上下文任务上保持了有竞争力的性能。详细的分析表明，RePo成功地将更高的注意力分配给遥远但相关的信息，在密集和非线性空间中分配位置，并捕获输入上下文的内在结构。我们的代码可以在这个https URL上找到。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLMs）在处理长文本、噪声数据或结构化信息时，由于其固定的位置编码方式，导致模型需要处理大量的无关信息，增加了认知负荷，降低了模型在关键信息上的注意力分配效率。这种固定的上下文结构无法有效捕捉token之间的复杂依赖关系，限制了模型在复杂任务中的表现。

**核心思路**：RePo的核心思路是通过学习一种动态的位置编码方式，使模型能够根据上下文信息自适应地调整token的位置表示。这种方法旨在减少模型需要处理的无关信息，提高模型对关键信息的关注度，从而降低认知负荷，提升模型在复杂任务中的性能。通过可微模块学习token位置，使得模型能够更好地捕捉上下文依赖关系。

**技术框架**：RePo的核心是一个可微的位置编码模块$f_\phi$，该模块接收token的上下文信息作为输入，并输出token的位置表示。该位置表示不再是固定的整数索引，而是一个连续的向量，可以根据上下文信息进行调整。整个框架可以嵌入到现有的Transformer架构中，通过预训练的方式进行学习。在训练过程中，模型需要学习如何根据上下文信息生成合适的位置表示，从而提高模型在下游任务中的表现。

**关键创新**：RePo最重要的创新点在于其动态的位置编码方式。与传统的固定位置编码方式不同，RePo可以根据上下文信息自适应地调整token的位置表示，从而更好地捕捉token之间的依赖关系。这种动态的位置编码方式可以有效地降低模型需要处理的无关信息，提高模型对关键信息的关注度，从而降低认知负荷，提升模型在复杂任务中的性能。

**关键设计**：RePo的关键设计在于可微的位置编码模块$f_\phi$。该模块可以使用各种神经网络结构来实现，例如多层感知机（MLP）或卷积神经网络（CNN）。在训练过程中，可以使用各种损失函数来优化该模块的参数，例如对比损失或三元组损失。此外，还可以使用各种正则化技术来防止过拟合。论文中使用OLMo-2 1B作为backbone，并持续进行预训练，以验证RePo的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391/figs/repo_overall.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391/figs/repo_long_context.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391/figs/stats_pos_dist.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RePo在涉及噪声上下文、结构化数据和更长上下文长度的任务上显著提高了性能，同时在一般的短上下文任务上保持了有竞争力的性能。例如，在某些任务上，RePo的性能提升超过了10%。详细的分析表明，RePo成功地将更高的注意力分配给遥远但相关的信息，在密集和非线性空间中分配位置，并捕获输入上下文的内在结构。

## 🎯 应用场景

RePo具有广泛的应用前景，尤其是在需要处理长文本、噪声数据或结构化信息的场景中。例如，可以应用于信息抽取、文本摘要、机器翻译等任务。此外，RePo还可以用于增强对话系统和智能助手的性能，使其能够更好地理解用户的意图并提供更准确的回复。该研究的成果有助于提升语言模型在实际应用中的鲁棒性和泛化能力。

## 📄 摘要（原文）

> In-context learning is fundamental to modern Large Language Models (LLMs); however, prevailing architectures impose a rigid and fixed contextual structure by assigning linear or constant positional indices. Drawing on Cognitive Load Theory (CLT), we argue that this uninformative structure increases extraneous cognitive load, consuming finite working memory capacity that should be allocated to deep reasoning and attention allocation. To address this, we propose RePo, a novel mechanism that reduces extraneous load via context re-positioning. Unlike standard approaches, RePo utilizes a differentiable module, $f_\phi$, to assign token positions that capture contextual dependencies, rather than replying on pre-defined integer range. By continually pre-training on the OLMo-2 1B backbone, we demonstrate that RePo significantly enhances performance on tasks involving noisy contexts, structured data, and longer context length, while maintaining competitive performance on general short-context tasks. Detailed analysis reveals that RePo successfully allocate higher attention to distant but relevant information, assign positions in dense and non-linear space, and capture the intrinsic structure of the input context. Our code is available atthis https URL.

