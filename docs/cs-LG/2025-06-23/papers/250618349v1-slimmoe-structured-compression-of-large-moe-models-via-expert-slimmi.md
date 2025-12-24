---
layout: default
title: "SlimMoE: Structured Compression of Large MoE Models via Expert Slimming and Distillation"
---

# SlimMoE: Structured Compression of Large MoE Models via Expert Slimming and Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18349" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18349v1</a>
  <a href="https://arxiv.org/pdf/2506.18349.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18349v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18349v1', 'SlimMoE: Structured Compression of Large MoE Models via Expert Slimming and Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zichong Li, Chen Liang, Zixuan Zhang, Ilgee Hong, Young Jin Kim, Weizhu Chen, Tuo Zhao

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-23

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/microsoft/Phi-mini-MoE-instruct) | [HUGGINGFACE](https://huggingface.co/microsoft/Phi-tiny-MoE-instruct)

---

## 💡 一句话要点

**提出SlimMoE以解决大规模MoE模型的压缩与部署问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `模型压缩` `知识蒸馏` `深度学习` `资源优化`

## 📋 核心要点

1. 现有的MoE模型在内存需求上极为庞大，导致在资源受限环境中难以进行微调和部署。
2. SlimMoE通过多阶段压缩框架，精简专家并通过知识转移来减少参数数量，避免了性能下降。
3. 实验结果显示，压缩后的Phi-mini-MoE和Phi-tiny-MoE在性能上优于同类模型，且延迟显著降低。

## 📝 摘要（中文）

混合专家（MoE）架构已成为扩展大型语言模型（LLMs）并保持推理效率的强大范式。然而，其巨大的内存需求使得在资源受限环境中进行微调或部署变得极为昂贵。为了解决这一挑战，本文提出了SlimMoE，一个多阶段压缩框架，旨在将大型MoE模型转化为更小、更高效的变体，而无需从头开始训练。该方法通过精简专家和通过中间阶段转移知识，系统性地减少参数数量，有效缓解了一次性剪枝方法中常见的性能下降问题。实验表明，压缩后的模型在性能上优于同类模型，并与更大模型竞争。

## 🔬 方法详解

**问题定义**：本文旨在解决大型MoE模型在资源受限环境中的高内存需求和微调困难的问题。现有方法在进行模型压缩时，往往会导致性能显著下降。

**核心思路**：SlimMoE的核心思路是通过多阶段的压缩过程，逐步精简模型中的专家，并通过知识蒸馏来保持模型性能。这种设计旨在有效降低参数数量，同时减少一次性剪枝带来的性能损失。

**技术框架**：SlimMoE的整体架构包括多个阶段，首先进行专家的精简，然后通过中间阶段的知识转移，最后得到压缩后的模型。每个阶段都有明确的目标，以确保最终模型的性能和效率。

**关键创新**：本文的主要创新在于将结构化剪枝与分阶段蒸馏相结合，形成了一种新的压缩策略。这与现有的一次性剪枝方法本质上不同，后者往往无法有效保持模型性能。

**关键设计**：在模型压缩过程中，关键的参数设置和损失函数设计确保了知识的有效转移。此外，网络结构的调整也经过精心设计，以适应不同阶段的需求。具体细节包括使用400B的训练数据进行压缩，最终得到的Phi-mini-MoE和Phi-tiny-MoE在参数数量上大幅减少。

## 📊 实验亮点

实验结果表明，Phi-mini-MoE在激活参数数量减少至2/3的情况下，性能与Phi-3-mini相当，且在MMLU评分上与Llama 3.1 8B模型相媲美，尽管延迟显著降低。这些结果展示了SlimMoE在模型压缩与性能保持方面的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括学术研究、资源受限的工业应用以及需要高效推理的移动设备。SlimMoE的压缩模型能够在单个GPU上进行微调，使其在实际应用中具有较高的价值。未来，随着MoE架构的广泛采用，SlimMoE可能会推动更多高效模型的开发与应用。

## 📄 摘要（原文）

> The Mixture of Experts (MoE) architecture has emerged as a powerful paradigm for scaling large language models (LLMs) while maintaining inference efficiency. However, their enormous memory requirements make them prohibitively expensive to fine-tune or deploy in resource-constrained environments. To address this challenge, we introduce SlimMoE, a multi-stage compression framework for transforming large MoE models into much smaller, efficient variants without incurring the prohibitive costs of training from scratch. Our method systematically reduces parameter counts by slimming experts and transferring knowledge through intermediate stages, effectively mitigating the performance degradation common in one-shot pruning approaches. Using this framework, we compress Phi 3.5-MoE (41.9B total/6.6B activated parameters) to create Phi-mini-MoE (7.6B total/2.4B activated parameters) and Phi-tiny-MoE (3.8B total/1.1B activated parameters) using only 400B tokens--less than 10% of the original model's training data. These compressed models can be fine-tuned on a single GPU (A100 for Phi-mini-MoE, A6000 for Phi-tiny-MoE), making them highly suitable for academic and resource-limited settings. Our experiments demonstrate that these compressed models outperform others of similar size and remain competitive with larger models. For instance, Phi-mini-MoE achieves similar or better performance to Phi-3-mini using only 2/3 of the activated parameters and yields comparable MMLU scores to Llama 3.1 8B despite having significantly lower latency. Our findings demonstrate that structured pruning combined with staged distillation offers an effective path to creating high-quality, compact MoE models, paving the way for broader adoption of MoE architectures. We make our models publicly available at https://huggingface.co/microsoft/Phi-mini-MoE-instruct and https://huggingface.co/microsoft/Phi-tiny-MoE-instruct .

