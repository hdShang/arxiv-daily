---
layout: default
title: RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling
---

# RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20206" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20206v1</a>
  <a href="https://arxiv.org/pdf/2510.20206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20206v1', 'RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingjie Gao, Qianli Ma, Xiaoxue Wu, Shuai Yang, Guanzhou Lan, Haonan Zhao, Jiaxuan Chen, Qingyang Liu, Yu Qiao, Xinyuan Chen, Yaohui Wang, Li Niu

**分类**: cs.CV

**发布日期**: 2025-10-23

**🔗 代码/项目**: [GITHUB](https://github.com/Vchitect/RAPO)

---

## 💡 一句话要点

**RAPO++：通过数据对齐和测试时缩放优化文本到视频生成中的跨阶段Prompt**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到视频生成` `Prompt优化` `跨阶段优化` `数据对齐` `大型语言模型`

## 📋 核心要点

1. 现有的文本到视频生成模型受限于用户提供的prompt通常简短、结构化程度低，且与训练数据不匹配，限制了生成潜力。
2. RAPO++通过跨阶段的prompt优化，包括检索增强、样本特定优化和LLM微调，在不改变底层生成模型的前提下提升生成质量。
3. 实验结果表明，RAPO++在多个基准测试和模型上显著提升了语义对齐、组合推理、时间稳定性和物理合理性。

## 📝 摘要（中文）

本文提出RAPO++，一个跨阶段的prompt优化框架，它统一了训练数据对齐的prompt精炼、测试时迭代缩放以及大型语言模型（LLM）微调，从而在不修改底层生成骨干网络的情况下，显著提升文本到视频（T2V）的生成质量。在第一阶段，检索增强的Prompt优化（RAPO）通过从关系图中检索语义相关的修饰词来丰富用户prompt，并重构它们以匹配训练分布，从而增强组合性和多对象保真度。第二阶段引入了样本特定的Prompt优化（SSPO），这是一种闭环机制，它使用多源反馈（包括语义对齐、空间保真度、时间连贯性和任务特定信号，如光流）迭代地细化prompt，从而逐步提高视频生成质量。第三阶段利用来自SSPO的优化prompt对来微调重写器LLM，从而内化任务特定的优化模式，并实现高效、高质量的prompt生成，甚至在推理之前。在五个最先进的T2V模型和五个基准测试上的大量实验表明，RAPO++在语义对齐、组合推理、时间稳定性和物理合理性方面取得了显著的提升，大大优于现有方法。我们的结果表明，RAPO++是一种模型无关、成本高效且可扩展的解决方案，为T2V生成中的prompt优化设定了新的标准。

## 🔬 方法详解

**问题定义**：文本到视频生成任务中，用户提供的prompt通常较为简短、非结构化，并且与模型的训练数据存在偏差，导致生成的视频质量受限，无法充分发挥扩散模型的潜力。现有方法难以有效地将用户意图转化为高质量的视频内容，尤其是在处理复杂场景和多对象交互时表现不佳。

**核心思路**：RAPO++的核心思路是通过多阶段的prompt优化，逐步提升prompt的质量和与训练数据的对齐程度。首先，利用检索增强来丰富prompt，使其更具语义信息。然后，通过闭环反馈机制迭代优化prompt，使其更符合视频生成的约束。最后，利用LLM学习优化模式，实现高效的prompt生成。这种分阶段、迭代式的优化方法能够有效地克服用户prompt的局限性，提升视频生成质量。

**技术框架**：RAPO++包含三个主要阶段：1) **RAPO (Retrieval-Augmented Prompt Optimization)**：利用关系图检索与用户prompt相关的语义修饰词，并重构prompt以匹配训练数据的分布。2) **SSPO (Sample-Specific Prompt Optimization)**：通过闭环机制，利用语义对齐、空间保真度、时间连贯性以及光流等任务特定信号，迭代优化prompt。3) **LLM Fine-tuning**：利用SSPO阶段生成的优化prompt对，微调LLM，使其学习任务特定的优化模式。

**关键创新**：RAPO++的关键创新在于其跨阶段的prompt优化框架，它将检索增强、样本特定优化和LLM微调相结合，形成一个完整的prompt优化流程。与现有方法相比，RAPO++能够更有效地利用训练数据，并根据视频生成的特定约束来优化prompt，从而显著提升生成质量。此外，RAPO++是一种模型无关的方法，可以应用于不同的文本到视频生成模型。

**关键设计**：RAPO阶段，关系图的构建和检索策略是关键。SSPO阶段，多源反馈信号的融合方式以及迭代优化的停止条件需要仔细设计。LLM微调阶段，损失函数的选择和训练数据的构建至关重要。具体参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

RAPO++在五个最先进的T2V模型和五个基准测试上进行了广泛的实验，结果表明其在语义对齐、组合推理、时间稳定性和物理合理性方面取得了显著的提升，大幅优于现有方法。具体的性能数据和提升幅度在论文中未详细给出，属于未知信息。但摘要强调了其显著的提升效果，表明RAPO++具有很强的竞争力。

## 🎯 应用场景

RAPO++在视频内容创作、虚拟现实、游戏开发等领域具有广泛的应用前景。它可以帮助用户更轻松地生成高质量的视频内容，降低视频制作的门槛。此外，RAPO++还可以用于提升现有文本到视频生成模型的性能，推动该领域的发展。未来，该技术有望应用于更复杂的视频生成任务，例如生成具有故事情节的电影片段。

## 📄 摘要（原文）

> Prompt design plays a crucial role in text-to-video (T2V) generation, yet user-provided prompts are often short, unstructured, and misaligned with training data, limiting the generative potential of diffusion-based T2V models. We present \textbf{RAPO++}, a cross-stage prompt optimization framework that unifies training-data--aligned refinement, test-time iterative scaling, and large language model (LLM) fine-tuning to substantially improve T2V generation without modifying the underlying generative backbone. In \textbf{Stage 1}, Retrieval-Augmented Prompt Optimization (RAPO) enriches user prompts with semantically relevant modifiers retrieved from a relation graph and refactors them to match training distributions, enhancing compositionality and multi-object fidelity. \textbf{Stage 2} introduces Sample-Specific Prompt Optimization (SSPO), a closed-loop mechanism that iteratively refines prompts using multi-source feedback -- including semantic alignment, spatial fidelity, temporal coherence, and task-specific signals such as optical flow -- yielding progressively improved video generation quality. \textbf{Stage 3} leverages optimized prompt pairs from SSPO to fine-tune the rewriter LLM, internalizing task-specific optimization patterns and enabling efficient, high-quality prompt generation even before inference. Extensive experiments across five state-of-the-art T2V models and five benchmarks demonstrate that RAPO++ achieves significant gains in semantic alignment, compositional reasoning, temporal stability, and physical plausibility, outperforming existing methods by large margins. Our results highlight RAPO++ as a model-agnostic, cost-efficient, and scalable solution that sets a new standard for prompt optimization in T2V generation. The code is available at https://github.com/Vchitect/RAPO.

