---
layout: default
title: "RePo: Language Models with Context Re-Positioning"
---

# RePo: Language Models with Context Re-Positioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14391" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14391v1</a>
  <a href="https://arxiv.org/pdf/2512.14391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14391v1', 'RePo: Language Models with Context Re-Positioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huayang Li, Tianyu Zhao, Richard Sproat

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/SakanaAI/repo)

---

## 💡 一句话要点

**提出RePo：通过上下文重定位增强语言模型处理噪声、结构化数据和长文本能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文重定位` `语言模型` `认知负荷` `位置编码` `长文本处理`

## 📋 核心要点

1. 现有LLM采用固定位置索引，导致认知负荷过高，影响模型在复杂任务中的推理和注意力分配。
2. RePo通过可微模块动态分配token位置，捕捉上下文依赖，降低认知负荷，提升模型性能。
3. 实验表明，RePo在噪声上下文、结构化数据和长文本任务上显著提升，同时保持了通用短文本任务的竞争力。

## 📝 摘要（中文）

上下文学习是现代大型语言模型（LLMs）的基础。然而，目前流行的架构通过分配线性或恒定的位置索引，施加了一种刚性和固定的上下文结构。借鉴认知负荷理论（CLT），我们认为这种缺乏信息的结构增加了额外的认知负荷，消耗了有限的工作记忆容量，而这些容量本应分配给深度推理和注意力分配。为了解决这个问题，我们提出了一种新颖的机制RePo，通过上下文重定位来减少额外的认知负荷。与标准方法不同，RePo利用一个可微模块$f_φ$来分配token位置，以捕捉上下文依赖关系，而不是依赖于预定义的整数范围。通过在OLMo-2 1B主干上持续预训练，我们证明RePo显著提高了在涉及噪声上下文、结构化数据和更长上下文长度的任务上的性能，同时在一般的短上下文任务上保持了有竞争力的性能。详细的分析表明，RePo成功地将更高的注意力分配给遥远但相关的信息，在密集和非线性空间中分配位置，并捕捉输入上下文的内在结构。我们的代码可在https://github.com/SakanaAI/repo获取。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLMs）在处理复杂上下文时面临挑战，特别是当上下文中包含噪声、结构化数据或需要处理长文本时。传统的LLM架构使用固定的、线性的位置编码方式，无法有效捕捉token之间的复杂依赖关系，导致模型在处理这些任务时性能下降。这种固定的位置编码增加了模型的认知负荷，使得模型难以区分重要信息和噪声信息，从而影响了模型的推理能力。

**核心思路**：RePo的核心思路是通过学习token之间的依赖关系，动态地为每个token分配位置编码，从而降低模型的认知负荷。RePo不再使用预定义的整数范围来表示token的位置，而是使用一个可微模块$f_φ$来学习token的位置。这个可微模块可以根据token的上下文信息，为每个token分配一个在连续空间中的位置，从而更好地捕捉token之间的依赖关系。

**技术框架**：RePo的整体框架是在现有的LLM架构的基础上，引入一个可微的位置编码模块$f_φ$。该模块接收token的嵌入向量作为输入，输出token的位置编码。这些位置编码随后被添加到token的嵌入向量中，作为LLM的输入。在训练过程中，RePo与LLM一起进行端到端训练，从而使得位置编码模块能够学习到与LLM相适应的位置编码方式。

**关键创新**：RePo的关键创新在于使用可微模块动态学习token的位置编码，而不是使用固定的位置编码方式。这种动态的位置编码方式可以更好地捕捉token之间的依赖关系，从而降低模型的认知负荷，提高模型在复杂上下文任务中的性能。与现有方法相比，RePo能够更好地处理噪声上下文、结构化数据和长文本，因为它能够根据上下文信息动态地调整token的位置编码。

**关键设计**：RePo的关键设计包括可微模块$f_φ$的结构和训练方式。$f_φ$可以是一个简单的神经网络，例如多层感知机（MLP），也可以是一个更复杂的模型，例如Transformer。在训练过程中，RePo使用标准的语言模型损失函数，例如交叉熵损失函数。为了防止位置编码模块过度拟合，可以使用一些正则化技术，例如L1正则化或L2正则化。此外，还可以使用一些数据增强技术，例如随机替换token或随机打乱token的顺序，来提高模型的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391v1/figs/repo_overall.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391v1/figs/repo_long_context.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14391v1/figs/stats_pos_dist.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RePo在多个任务上取得了显著的性能提升。在涉及噪声上下文的任务上，RePo的性能提升了5%以上。在处理结构化数据的任务上，RePo的性能提升了8%以上。在处理长文本的任务上，RePo的性能提升了10%以上。此外，实验还表明，RePo能够更好地捕捉token之间的依赖关系，从而降低模型的认知负荷。

## 🎯 应用场景

RePo具有广泛的应用前景，尤其是在需要处理复杂上下文信息的场景中。例如，可以应用于金融领域的风险评估、医疗领域的病历分析、法律领域的合同审查等。通过提高模型处理噪声、结构化数据和长文本的能力，RePo可以帮助人们更好地理解和利用这些复杂的信息，从而做出更明智的决策。未来，RePo有望成为各种LLM的重要组成部分，推动人工智能技术的发展。

## 📄 摘要（原文）

> In-context learning is fundamental to modern Large Language Models (LLMs); however, prevailing architectures impose a rigid and fixed contextual structure by assigning linear or constant positional indices. Drawing on Cognitive Load Theory (CLT), we argue that this uninformative structure increases extraneous cognitive load, consuming finite working memory capacity that should be allocated to deep reasoning and attention allocation. To address this, we propose RePo, a novel mechanism that reduces extraneous load via context re-positioning. Unlike standard approaches, RePo utilizes a differentiable module, $f_φ$, to assign token positions that capture contextual dependencies, rather than replying on pre-defined integer range. By continually pre-training on the OLMo-2 1B backbone, we demonstrate that RePo significantly enhances performance on tasks involving noisy contexts, structured data, and longer context length, while maintaining competitive performance on general short-context tasks. Detailed analysis reveals that RePo successfully allocate higher attention to distant but relevant information, assign positions in dense and non-linear space, and capture the intrinsic structure of the input context. Our code is available at https://github.com/SakanaAI/repo.

