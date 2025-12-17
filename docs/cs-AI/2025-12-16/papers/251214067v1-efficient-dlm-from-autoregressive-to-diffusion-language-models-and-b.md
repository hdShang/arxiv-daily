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

**提出Efficient-DLM框架，通过改进AR到dLM转换方法，实现高效扩散语言模型，在保持准确性的同时大幅提升生成速度。**

**关键词**: `扩散语言模型` `自回归模型转换` `注意力模式优化` `训练策略改进` `高效文本生成` `模型加速` `预训练权重保留` `并行生成`

## 📋 核心要点

1. 现有AR-to-dLM转换方法在注意力模式和目标函数上存在局限，导致转换后模型性能下降或效率不足。
2. 提出块状注意力模式和位置相关掩码策略，优化AR权重保留和训练-测试一致性，实现高效转换。
3. Efficient-DLM 8B在准确率和吞吐量上显著超越Dream 7B和Qwen3 4B，验证了方法的有效性。

## 📝 摘要（中文）

扩散语言模型（dLMs）作为一种支持并行、非自回归生成的新范式，展现出巨大潜力，但其从头训练的学习效率仍落后于自回归（AR）语言模型。为此，本研究探索AR到dLM的转换方法，旨在将预训练的AR模型转化为高效的dLMs，在保持AR模型任务准确性的同时显著提升生成速度。我们通过分析现有AR-to-dLM方法在注意力模式和目标函数上的局限性，提出了更有效的转换原则和方法。具体而言，首先系统比较不同注意力模式，发现保持预训练AR权重分布对有效转换至关重要。因此，我们引入了一种基于块状注意力模式的持续预训练方案，该方案在块间保持因果性，同时在块内支持双向建模。这种方法比完全双向建模能更好地保留预训练AR模型的权重分布，并具备KV缓存优势，实现了准确性和效率的双赢。其次，为缓解训练与测试阶段掩码标记分布（均匀分布与高度从左到右分布）的差异，我们提出了一种位置相关的标记掩码策略，在训练时对后续标记赋予更高的掩码概率，以更好地模拟测试时的行为。基于此框架，我们深入研究了dLMs的注意力模式、训练动态及其他设计选择，为可扩展的AR-to-dLM转换提供了实用见解。这些研究催生了Efficient-DLM系列模型，其在性能上超越了当前最先进的AR模型和dLMs。例如，我们的Efficient-DLM 8B模型在准确率上分别比Dream 7B和Qwen3 4B高出5.4%和2.7%，同时吞吐量分别提升了4.5倍和2.7倍。

## 🔬 方法详解

论文提出Efficient-DLM框架，核心是通过改进AR到dLM的转换过程，将预训练AR模型高效转化为扩散语言模型。整体框架包括两个关键技术：一是块状注意力模式，在块内进行双向建模以提升效率，同时块间保持因果性以保留AR权重分布；二是位置相关掩码策略，通过调整训练时掩码概率分布，减少与测试阶段的差异。与现有方法相比，该方法更注重保持预训练权重和优化训练动态，而非完全重新设计模型架构。

## 📊 实验亮点

Efficient-DLM 8B模型在准确率上比Dream 7B和Qwen3 4B分别提升5.4%和2.7%，吞吐量提高4.5倍和2.7倍，实现了速度与精度的双重突破。

## 🎯 应用场景

该研究可应用于需要高速文本生成的场景，如实时对话系统、内容创作工具和大规模语言模型部署，通过提升生成效率降低计算成本，同时保持高质量输出。

## 📄 摘要（原文）

> Diffusion language models (dLMs) have emerged as a promising paradigm that enables parallel, non-autoregressive generation, but their learning efficiency lags behind that of autoregressive (AR) language models when trained from scratch. To this end, we study AR-to-dLM conversion to transform pretrained AR models into efficient dLMs that excel in speed while preserving AR models' task accuracy. We achieve this by identifying limitations in the attention patterns and objectives of existing AR-to-dLM methods and then proposing principles and methodologies for more effective AR-to-dLM conversion. Specifically, we first systematically compare different attention patterns and find that maintaining pretrained AR weight distributions is critical for effective AR-to-dLM conversion. As such, we introduce a continuous pretraining scheme with a block-wise attention pattern, which remains causal across blocks while enabling bidirectional modeling within each block. We find that this approach can better preserve pretrained AR models' weight distributions than fully bidirectional modeling, in addition to its known benefit of enabling KV caching, and leads to a win-win in accuracy and efficiency. Second, to mitigate the training-test gap in mask token distributions (uniform vs. highly left-to-right), we propose a position-dependent token masking strategy that assigns higher masking probabilities to later tokens during training to better mimic test-time behavior. Leveraging this framework, we conduct extensive studies of dLMs' attention patterns, training dynamics, and other design choices, providing actionable insights into scalable AR-to-dLM conversion. These studies lead to the Efficient-DLM family, which outperforms state-of-the-art AR models and dLMs, e.g., our Efficient-DLM 8B achieves +5.4%/+2.7% higher accuracy with 4.5x/2.7x higher throughput compared to Dream 7B and Qwen3 4B, respectively.

