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

**提出Efficient-DLM框架，通过改进AR到dLM转换方法，实现高效扩散语言模型，在保持任务准确性的同时提升生成速度。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `扩散语言模型` `自回归模型转换` `注意力模式优化` `位置依赖掩码` `高效文本生成` `KV缓存` `连续预训练` `非自回归生成`

## 📋 核心要点

1. 现有AR-to-dLM转换方法在注意力模式和目标上存在局限性，导致学习效率低和训练-测试分布不匹配。
2. 提出块级注意力模式和位置依赖掩码策略，以保持预训练权重分布并模拟测试行为，实现高效转换。
3. Efficient-DLM系列模型在准确性和吞吐量上显著超越现有AR和dLM模型，如8B版本相比基准模型提升准确率并加速生成。

## 📝 摘要（中文）

扩散语言模型（dLMs）作为一种并行、非自回归生成范式展现出潜力，但其从头训练的学习效率落后于自回归（AR）语言模型。为此，本研究探索AR到dLM的转换方法，将预训练的AR模型转化为高效的dLMs，在保持AR模型任务准确性的同时提升速度。我们通过分析现有AR-to-dLM方法在注意力模式和目标上的局限性，提出更有效的转换原则和方法。具体而言，首先系统比较不同注意力模式，发现保持预训练AR权重分布对有效转换至关重要，因此引入基于块级注意力模式的连续预训练方案，在块间保持因果性、块内实现双向建模，这比完全双向建模更好地保留权重分布，并支持KV缓存，实现准确性和效率的双赢。其次，为缓解训练与测试中掩码标记分布（均匀vs.高度从左到右）的差距，提出位置依赖的标记掩码策略，在训练中为后续标记分配更高掩码概率以更好模拟测试行为。基于此框架，我们深入研究了dLMs的注意力模式、训练动态和其他设计选择，为可扩展的AR-to-dLM转换提供实用见解。这些研究催生了Efficient-DLM系列模型，其性能超越最先进的AR模型和dLMs，例如，我们的Efficient-DLM 8B相比Dream 7B和Qwen3 4B，准确率分别提升+5.4%和+2.7%，吞吐量分别提高4.5倍和2.7倍。

## 🔬 方法详解

论文提出Efficient-DLM框架，核心方法包括AR-to-dLM转换的连续预训练方案。整体框架基于预训练AR模型，通过改进注意力模式和掩码策略实现高效扩散建模。关键技术创新点在于块级注意力模式，它在块间保持因果性以保留AR权重分布，块内实现双向建模以支持并行生成，同时引入位置依赖的掩码策略来缓解训练-测试分布差距。与现有方法的主要区别在于避免了完全双向建模导致的权重分布破坏，并优化了掩码过程以更好地模拟实际生成场景，从而在准确性和效率上取得平衡。

## 📊 实验亮点

Efficient-DLM 8B模型相比Dream 7B和Qwen3 4B，准确率分别提升5.4%和2.7%，吞吐量提高4.5倍和2.7倍，展示了在保持任务准确性的同时显著加速生成的优势。

## 🎯 应用场景

该研究可应用于需要高效文本生成的自然语言处理任务，如机器翻译、文本摘要和对话系统，通过提升扩散语言模型的生成速度和准确性，支持大规模实时应用，降低计算成本。

## 📄 摘要（原文）

> Diffusion language models (dLMs) have emerged as a promising paradigm that enables parallel, non-autoregressive generation, but their learning efficiency lags behind that of autoregressive (AR) language models when trained from scratch. To this end, we study AR-to-dLM conversion to transform pretrained AR models into efficient dLMs that excel in speed while preserving AR models' task accuracy. We achieve this by identifying limitations in the attention patterns and objectives of existing AR-to-dLM methods and then proposing principles and methodologies for more effective AR-to-dLM conversion. Specifically, we first systematically compare different attention patterns and find that maintaining pretrained AR weight distributions is critical for effective AR-to-dLM conversion. As such, we introduce a continuous pretraining scheme with a block-wise attention pattern, which remains causal across blocks while enabling bidirectional modeling within each block. We find that this approach can better preserve pretrained AR models' weight distributions than fully bidirectional modeling, in addition to its known benefit of enabling KV caching, and leads to a win-win in accuracy and efficiency. Second, to mitigate the training-test gap in mask token distributions (uniform vs. highly left-to-right), we propose a position-dependent token masking strategy that assigns higher masking probabilities to later tokens during training to better mimic test-time behavior. Leveraging this framework, we conduct extensive studies of dLMs' attention patterns, training dynamics, and other design choices, providing actionable insights into scalable AR-to-dLM conversion. These studies lead to the Efficient-DLM family, which outperforms state-of-the-art AR models and dLMs, e.g., our Efficient-DLM 8B achieves +5.4%/+2.7% higher accuracy with 4.5x/2.7x higher throughput compared to Dream 7B and Qwen3 4B, respectively.

