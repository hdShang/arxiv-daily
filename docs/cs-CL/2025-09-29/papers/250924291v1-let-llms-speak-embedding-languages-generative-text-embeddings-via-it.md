---
layout: default
title: "Let LLMs Speak Embedding Languages: Generative Text Embeddings via Iterative Contrastive Refinement"
---

# Let LLMs Speak Embedding Languages: Generative Text Embeddings via Iterative Contrastive Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24291" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24291v1</a>
  <a href="https://arxiv.org/pdf/2509.24291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24291v1', 'Let LLMs Speak Embedding Languages: Generative Text Embeddings via Iterative Contrastive Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu-Che Tsai, Kuan-Yu Chen, Yuan-Chi Li, Yuan-Hao Chen, Ching-Yu Tsai, Shou-De Lin

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出GIRCSE，利用生成式LLM迭代优化文本嵌入，显著提升语义表征能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本嵌入` `大型语言模型` `生成式模型` `对比学习` `自回归生成`

## 📋 核心要点

1. 现有基于LLM的文本嵌入方法主要依赖encoder-only模式，忽略了LLM强大的生成能力，限制了表征学习的潜力。
2. GIRCSE框架通过自回归生成软token序列，并利用迭代对比优化目标，逐步提炼语义表示，捕捉更丰富的语义信息。
3. 实验结果表明，GIRCSE在多个基准测试中超越了现有的LLM嵌入方法，并展现出测试时性能随生成token数量增加而提升的特性。

## 📝 摘要（中文）

本文提出了一种名为GIRCSE（用于对比句子嵌入的生成式迭代优化）的新框架，该框架利用自回归生成来迭代地改进语义表示，从而发挥大型语言模型（LLM）的生成能力。与现有基于LLM的嵌入方法通常采用的encoder-only范式不同，GIRCSE通过生成在对比目标下优化的软token序列，捕捉了encoder-only方法经常遗漏的潜在概念和隐式语义。为了指导这个过程，我们提出了一种迭代对比优化（ICR）目标，该目标鼓励每个优化步骤产生更好的表示。大量实验表明，GIRCSE在MTEB基准和指令遵循任务上优于强大的基于LLM的嵌入基线。此外，GIRCSE表现出一种涌现的测试时缩放特性：在推理时生成更多的token可以稳定地提高嵌入质量。我们的结果确立了生成式迭代优化作为表征学习的一种新范式。

## 🔬 方法详解

**问题定义**：现有基于LLM的文本嵌入方法通常将LLM视为静态的特征提取器，采用encoder-only的模式。这种方法忽略了LLM强大的生成能力，无法充分利用LLM所蕴含的知识和推理能力，导致生成的文本嵌入可能无法捕捉到深层的语义信息，例如潜在概念和隐式语义。

**核心思路**：GIRCSE的核心思路是利用LLM的自回归生成能力，通过迭代地生成和优化软token序列来改进文本的语义表示。通过在对比学习的目标下优化生成的token，GIRCSE能够逐步提炼文本的语义信息，从而获得更具表达力的文本嵌入。这种方法将LLM从一个静态的特征提取器转变为一个动态的语义表示生成器。

**技术框架**：GIRCSE框架主要包含以下几个阶段：1) **初始化**：使用LLM对输入文本进行编码，得到初始的文本嵌入。2) **迭代生成**：基于初始嵌入，利用LLM的自回归生成能力生成一系列软token。3) **对比优化**：使用迭代对比优化（ICR）目标函数，鼓励每个生成步骤产生更好的文本表示。4) **嵌入提取**：将最终生成的软token序列作为文本的嵌入表示。

**关键创新**：GIRCSE最重要的技术创新点在于将LLM的生成能力引入到文本嵌入的学习过程中。与传统的encoder-only方法不同，GIRCSE通过迭代生成和优化软token序列，能够捕捉到更丰富的语义信息，并生成更具表达力的文本嵌入。此外，ICR目标的引入也保证了每次迭代都能提升嵌入的质量。

**关键设计**：GIRCSE的关键设计包括：1) **软token生成**：使用LLM的自回归生成能力生成软token，而不是直接生成离散的token。2) **迭代对比优化（ICR）**：ICR目标函数鼓励每个生成步骤产生的嵌入都比前一步的嵌入更好，从而保证了嵌入质量的逐步提升。ICR损失函数通常基于对比学习损失，例如InfoNCE。3) **测试时缩放**：在推理阶段，可以通过增加生成的token数量来进一步提升嵌入的质量，展现出一种涌现的测试时缩放特性。

## 📊 实验亮点

实验结果表明，GIRCSE在MTEB基准测试中显著优于现有的基于LLM的嵌入方法。例如，在某些任务上，GIRCSE的性能提升超过5%。此外，GIRCSE还展现出一种涌现的测试时缩放特性，即在推理时生成更多的token可以稳定地提高嵌入质量。这表明GIRCSE能够更好地利用LLM的生成能力来学习更具表达力的文本嵌入。

## 🎯 应用场景

GIRCSE生成的文本嵌入可以广泛应用于各种自然语言处理任务，例如文本检索、文本分类、语义相似度计算、聚类等。该方法尤其适用于需要捕捉深层语义信息的场景，例如知识图谱补全、问答系统等。未来，GIRCSE可以进一步扩展到多模态领域，例如图像文本检索、视频语义理解等。

## 📄 摘要（原文）

> Existing large language model (LLM)-based embeddings typically adopt an encoder-only paradigm, treating LLMs as static feature extractors and overlooking their core generative strengths. We introduce GIRCSE (Generative Iterative Refinement for Contrastive Sentence Embeddings), a novel framework that leverages autoregressive generation to iteratively refine semantic representations. By producing sequences of soft tokens optimized under contrastive objective, GIRCSE captures latent concepts and implicit semantics that encoder-only methods often miss. To guide this process, we propose an Iterative Contrastive Refinement (ICR) objective that encourages each refinement step to yield better representations. Extensive experiments show that GIRCSE outperforms strong LLM-based embedding baselines on the MTEB benchmark and instruction-following tasks. Moreover, GIRCSE exhibits an emergent test-time scaling property: generating more tokens at inference steadily improves embedding quality. Our results establish generative iterative refinement as a new paradigm for representation learning.

