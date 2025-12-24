---
layout: default
title: "RADLADS: Rapid Attention Distillation to Linear Attention Decoders at Scale"
---

# RADLADS: Rapid Attention Distillation to Linear Attention Decoders at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03005" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03005v3</a>
  <a href="https://arxiv.org/pdf/2505.03005.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03005v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03005v3', 'RADLADS: Rapid Attention Distillation to Linear Attention Decoders at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel Goldstein, Eric Alcaide, Janna Lu, Eugene Cheah

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-05 (更新: 2025-07-25)

**🔗 代码/项目**: [GITHUB](https://github.com/recursal/RADLADS-paper) | [HUGGINGFACE](https://huggingface.co/collections/recursal)

---

## 💡 一句话要点

**提出RADLADS以快速转换软max注意力变换器为线性解码模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `线性注意力` `模型蒸馏` `自然语言处理` `高效推理` `大规模模型`

## 📋 核心要点

1. 现有的软max注意力变换器在计算效率和资源消耗上存在显著挑战，尤其在大规模模型中。
2. RADLADS协议通过快速蒸馏技术，将软max注意力变换器转换为高效的线性注意力解码器，显著降低了所需的训练token数量。
3. 实验结果表明，转换后的模型在多个标准基准测试中表现出色，且推理质量与原始模型相近，具有较高的性价比。

## 📝 摘要（中文）

我们提出了快速注意力蒸馏到线性注意力解码器的协议（RADLADS），旨在快速将软max注意力变换器转换为线性注意力解码模型。该方法引入了两种新的RWKV变体架构，并将流行的Qwen2.5开源模型转换为7B、32B和72B的规模。我们的转换过程仅需350-700M个token，远低于原始教师模型训练所需的token数量的0.005%。转换为72B线性注意力模型的成本不到2000美元，但推理质量接近原始变换器。这些模型在标准基准测试中实现了同类线性注意力模型的最先进下游性能。我们在HuggingFace上发布了所有模型，72B模型受Qwen许可协议约束。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有软max注意力变换器在大规模模型训练中面临的计算效率低和资源消耗高的问题。现有方法在处理大规模数据时，往往需要大量的token和计算资源，限制了其应用范围。

**核心思路**：RADLADS协议的核心在于通过快速蒸馏技术，将软max注意力变换器转换为线性注意力解码器，从而在保持推理质量的同时，显著降低训练所需的token数量和成本。

**技术框架**：该方法包括两个主要阶段：首先，利用少量token进行模型蒸馏；其次，将蒸馏后的模型架构调整为线性注意力解码器。整个流程高效且易于实施。

**关键创新**：RADLADS的最大创新在于其蒸馏过程所需的token数量极低，仅为原始模型的0.005%，同时保持了推理质量，显著提升了模型的训练效率。

**关键设计**：在模型设计中，采用了新的RWKV变体架构，并对损失函数和网络结构进行了优化，以确保在转换过程中尽可能保留原始模型的性能。

## 📊 实验亮点

实验结果显示，转换后的72B线性注意力模型在多个标准基准测试中达到了最先进的性能，推理质量接近原始软max注意力变换器，且转换成本低于2000美元，展现了极高的性价比。

## 🎯 应用场景

RADLADS的研究成果在多个领域具有广泛的应用潜力，尤其是在需要高效推理的自然语言处理任务中。通过降低计算资源的需求，该方法能够使得大规模模型在边缘设备或资源受限环境中得以应用，推动智能应用的普及与发展。

## 📄 摘要（原文）

> We present Rapid Attention Distillation to Linear Attention Decoders at Scale (RADLADS), a protocol for rapidly converting softmax attention transformers into linear attention decoder models, along with two new RWKV-variant architectures, and models converted from popular Qwen2.5 open source models in 7B, 32B, and 72B sizes. Our conversion process requires only 350-700M tokens, less than 0.005% of the token count used to train the original teacher models. Converting to our 72B linear attention model costs less than \$2,000 USD at today's prices, yet quality at inference remains close to the original transformer. These models achieve state-of-the-art downstream performance across a set of standard benchmarks for linear attention models of their size. We release all our models on HuggingFace under the Apache 2.0 license, with the exception of our 72B models which are also governed by the Qwen License Agreement.
>   Models at https://huggingface.co/collections/recursal/radlads-6818ee69e99e729ba8a87102 Training Code at https://github.com/recursal/RADLADS-paper

