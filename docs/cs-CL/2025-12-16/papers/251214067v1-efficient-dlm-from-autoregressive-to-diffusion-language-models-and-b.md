---
layout: default
title: Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed
---

# Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed

**arXiv**: [2512.14067v1](https://arxiv.org/abs/2512.14067) | [PDF](https://arxiv.org/pdf/2512.14067.pdf)

**作者**: Yonggan Fu, Lexington Whalen, Zhifan Ye, Xin Dong, Shizhe Diao, Jingyu Liu, Chengyue Wu, Hao Zhang, Enze Xie, Song Han, Maksim Khadkevich, Jan Kautz, Yingyan Celine Lin, Pavlo Molchanov

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Efficient-DLM，通过AR到dLM转换，提升Diffusion语言模型的训练效率和推理速度。**

🎯 **匹配领域**: **3D感知与状态估计 (Perception & State Est)**

**关键词**: `Diffusion语言模型` `自回归模型` `AR到dLM转换` `注意力机制` `并行生成`

## 📋 核心要点

1. 现有AR到dLM转换方法在注意力模式和目标函数上存在局限性，导致转换后的dLM模型性能不佳。
2. 提出Efficient-DLM，通过块状注意力模式的连续预训练和位置相关的token掩码策略，更有效地进行AR到dLM的转换。
3. Efficient-DLM 8B在准确率和吞吐量上均优于现有AR模型和dLM，例如Dream 7B和Qwen3 4B。

## 📝 摘要（中文）

Diffusion语言模型(dLMs)作为一种新兴范式，实现了并行、非自回归生成，但从头开始训练时，其学习效率落后于自回归(AR)语言模型。为此，我们研究了AR到dLM的转换，将预训练的AR模型转化为高效的dLM，在保持AR模型任务准确性的同时，提高速度。我们通过识别现有AR到dLM方法在注意力模式和目标上的局限性，提出了更有效的AR到dLM转换的原则和方法。具体来说，我们首先系统地比较了不同的注意力模式，发现保持预训练的AR权重分布对于有效的AR到dLM转换至关重要。因此，我们引入了一种具有块状注意力模式的连续预训练方案，该方案在块之间保持因果关系，同时在每个块内实现双向建模。我们发现，除了实现KV缓存的已知好处外，这种方法比完全双向建模更能保持预训练的AR模型权重分布，从而在准确性和效率方面实现双赢。其次，为了缓解掩码token分布的训练-测试差距（均匀vs.高度从左到右），我们提出了一种位置相关的token掩码策略，该策略在训练期间为后面的token分配更高的掩码概率，以更好地模拟测试时行为。利用这个框架，我们对dLM的注意力模式、训练动态和其他设计选择进行了广泛的研究，为可扩展的AR到dLM转换提供了可操作的见解。这些研究产生了Efficient-DLM系列，其性能优于最先进的AR模型和dLM，例如，我们的Efficient-DLM 8B与Dream 7B和Qwen3 4B相比，分别实现了+5.4%/+2.7%的更高准确率和4.5x/2.7x的更高吞吐量。

## 🔬 方法详解

**问题定义**：论文旨在解决Diffusion语言模型(dLMs)训练效率低下的问题。虽然dLMs具有并行生成的能力，但在从头开始训练时，其效率远低于自回归(AR)模型。现有的AR到dLM转换方法在保持预训练AR模型的性能方面存在不足，并且在训练和测试阶段存在掩码token分布的差异，影响了最终模型的性能。

**核心思路**：论文的核心思路是通过更有效地将预训练的AR模型转换为dLM，从而在保持AR模型准确性的同时，提高dLM的训练效率和推理速度。关键在于设计合适的注意力模式和训练策略，以更好地保留预训练AR模型的知识，并缓解训练和测试阶段的差异。

**技术框架**：Efficient-DLM的整体框架包括两个主要部分：1) 具有块状注意力模式的连续预训练，用于更好地保留预训练AR模型的权重分布；2) 位置相关的token掩码策略，用于缓解训练和测试阶段掩码token分布的差异。该框架利用预训练的AR模型作为起点，通过特定的训练策略和注意力机制，将其转换为高效的dLM。

**关键创新**：论文的关键创新在于：1) 提出了一种块状注意力模式，该模式在块之间保持因果关系，同时在每个块内实现双向建模，从而更好地保留预训练AR模型的权重分布；2) 提出了一种位置相关的token掩码策略，该策略在训练期间为后面的token分配更高的掩码概率，以更好地模拟测试时行为。

**关键设计**：块状注意力模式的关键设计在于将序列分成多个块，每个块内部采用双向注意力，块之间采用因果注意力。位置相关的token掩码策略的关键设计在于根据token的位置动态调整掩码概率，使得后面的token更容易被掩码。具体的掩码概率函数需要根据实验进行调整。

## 📊 实验亮点

Efficient-DLM系列模型在多个任务上取得了显著的性能提升。例如，Efficient-DLM 8B模型与Dream 7B和Qwen3 4B相比，分别实现了+5.4%/+2.7%的更高准确率和4.5x/2.7x的更高吞吐量。这些结果表明，Efficient-DLM在准确性和效率方面均优于现有的AR模型和dLM。

## 🎯 应用场景

Efficient-DLM具有广泛的应用前景，可用于各种自然语言生成任务，例如文本摘要、机器翻译、对话生成等。其高效的并行生成能力使其特别适用于对延迟敏感的应用场景。此外，该研究为AR到dLM的转换提供了新的思路和方法，有助于推动Diffusion模型在自然语言处理领域的进一步发展。

## 📄 摘要（原文）

> Diffusion language models (dLMs) have emerged as a promising paradigm that enables parallel, non-autoregressive generation, but their learning efficiency lags behind that of autoregressive (AR) language models when trained from scratch. To this end, we study AR-to-dLM conversion to transform pretrained AR models into efficient dLMs that excel in speed while preserving AR models' task accuracy. We achieve this by identifying limitations in the attention patterns and objectives of existing AR-to-dLM methods and then proposing principles and methodologies for more effective AR-to-dLM conversion. Specifically, we first systematically compare different attention patterns and find that maintaining pretrained AR weight distributions is critical for effective AR-to-dLM conversion. As such, we introduce a continuous pretraining scheme with a block-wise attention pattern, which remains causal across blocks while enabling bidirectional modeling within each block. We find that this approach can better preserve pretrained AR models' weight distributions than fully bidirectional modeling, in addition to its known benefit of enabling KV caching, and leads to a win-win in accuracy and efficiency. Second, to mitigate the training-test gap in mask token distributions (uniform vs. highly left-to-right), we propose a position-dependent token masking strategy that assigns higher masking probabilities to later tokens during training to better mimic test-time behavior. Leveraging this framework, we conduct extensive studies of dLMs' attention patterns, training dynamics, and other design choices, providing actionable insights into scalable AR-to-dLM conversion. These studies lead to the Efficient-DLM family, which outperforms state-of-the-art AR models and dLMs, e.g., our Efficient-DLM 8B achieves +5.4%/+2.7% higher accuracy with 4.5x/2.7x higher throughput compared to Dream 7B and Qwen3 4B, respectively.

