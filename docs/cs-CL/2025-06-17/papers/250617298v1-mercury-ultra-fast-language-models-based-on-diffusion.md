---
layout: default
title: "Mercury: Ultra-Fast Language Models Based on Diffusion"
---

# Mercury: Ultra-Fast Language Models Based on Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17298" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17298v1</a>
  <a href="https://arxiv.org/pdf/2506.17298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17298v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17298v1', 'Mercury: Ultra-Fast Language Models Based on Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Inception Labs, Samar Khanna, Siddhant Kharbanda, Shufan Li, Harshit Varma, Eric Wang, Sawyer Birnbaum, Ziyang Luo, Yanis Miraoui, Akash Palrecha, Stefano Ermon, Aditya Grover, Volodymyr Kuleshov

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-17

**备注**: 15 pages; equal core, cross-function, senior authors listed alphabetically

---

## 💡 一句话要点

**提出Mercury以实现超快的语言模型，提升编程效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `大型语言模型` `编程应用` `Transformer架构` `速度优化` `代码生成` `自然语言处理`

## 📋 核心要点

1. 现有的语言模型在处理速度和质量之间存在权衡，尤其在编程应用中表现不佳。
2. Mercury通过基于扩散的模型设计，采用Transformer架构并行预测多个标记，从而提升处理速度。
3. 实验结果显示，Mercury Coder Mini和Small在速度上分别达到1109和737个标记/秒，显著优于现有速度优化模型。

## 📝 摘要（中文）

我们提出了Mercury，一种基于扩散的商业规模大型语言模型（LLMs）。这些模型采用Transformer架构进行参数化，并训练以并行预测多个标记。本文详细介绍了Mercury Coder，这是我们为编码应用设计的首批扩散LLMs。Mercury Coder目前有Mini和Small两个版本，在速度和质量的平衡上设立了新的行业标杆。根据独立评估，Mercury Coder Mini和Small在NVIDIA H100 GPU上分别达到了1109和737个标记/秒的处理速度，平均超越速度优化模型10倍，同时保持相当的质量。我们还讨论了多种编程语言和用例的基准测试结果，以及在Copilot Arena的开发者实际验证，模型在质量上排名第二，并且是整体最快的模型。此外，我们还发布了公共API和免费的在线平台。

## 🔬 方法详解

**问题定义**：现有的语言模型在速度和质量之间存在明显的权衡，尤其在编程任务中，处理速度往往无法满足实际需求，导致开发效率低下。

**核心思路**：Mercury通过引入扩散模型的概念，利用Transformer架构并行处理多个标记，从而实现更高的处理速度和质量平衡。这种设计使得模型能够在保持输出质量的同时，显著提升推理速度。

**技术框架**：Mercury的整体架构包括数据预处理、模型训练和推理三个主要阶段。首先，数据经过预处理后输入到基于Transformer的扩散模型中进行训练，最后在推理阶段实现并行标记预测。

**关键创新**：Mercury的核心创新在于其基于扩散的训练方法和并行预测能力，这与传统的自回归模型形成了鲜明对比，后者通常在生成时依赖于前一个标记的输出。

**关键设计**：在模型设计上，Mercury采用了特定的损失函数以优化并行预测的效果，并在网络结构上进行了调整，以适应扩散过程的需求。

## 📊 实验亮点

实验结果表明，Mercury Coder Mini和Small在NVIDIA H100 GPU上分别实现了1109和737个标记/秒的处理速度，超越现有速度优化模型10倍，同时保持相似的输出质量。此外，在Copilot Arena中，Mercury Coder在质量上排名第二，整体速度最快，展示了其在实际应用中的优势。

## 🎯 应用场景

Mercury的潜在应用领域包括编程助手、代码生成和自动化测试等。其高效的处理能力和优质的输出使其在软件开发、数据科学和教育等多个领域具有实际价值，能够显著提升开发者的工作效率。未来，Mercury有望推动更多基于自然语言处理的智能应用的发展。

## 📄 摘要（原文）

> We present Mercury, a new generation of commercial-scale large language models (LLMs) based on diffusion. These models are parameterized via the Transformer architecture and trained to predict multiple tokens in parallel. In this report, we detail Mercury Coder, our first set of diffusion LLMs designed for coding applications. Currently, Mercury Coder comes in two sizes: Mini and Small. These models set a new state-of-the-art on the speed-quality frontier. Based on independent evaluations conducted by Artificial Analysis, Mercury Coder Mini and Mercury Coder Small achieve state-of-the-art throughputs of 1109 tokens/sec and 737 tokens/sec, respectively, on NVIDIA H100 GPUs and outperform speed-optimized frontier models by up to 10x on average while maintaining comparable quality. We discuss additional results on a variety of code benchmarks spanning multiple languages and use-cases as well as real-world validation by developers on Copilot Arena, where the model currently ranks second on quality and is the fastest model overall. We also release a public API at https://platform.inceptionlabs.ai/ and free playground at https://chat.inceptionlabs.ai

