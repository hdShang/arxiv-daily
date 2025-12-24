---
layout: default
title: "InfLLM-V2: Dense-Sparse Switchable Attention for Seamless Short-to-Long Adaptation"
---

# InfLLM-V2: Dense-Sparse Switchable Attention for Seamless Short-to-Long Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24663" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24663v1</a>
  <a href="https://arxiv.org/pdf/2509.24663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24663v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24663v1', 'InfLLM-V2: Dense-Sparse Switchable Attention for Seamless Short-to-Long Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weilin Zhao, Zihan Zhou, Zhou Su, Chaojun Xiao, Yuxuan Li, Yanghao Li, Yudi Zhang, Weilun Zhao, Zhen Li, Yuxiang Huang, Ao Sun, Xu Han, Zhiyuan Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-29

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/openbmb/MiniCPM4.1-8B)

---

## 💡 一句话要点

**提出InfLLM-V2：一种稠密-稀疏可切换注意力机制，实现模型从短序列到长序列的无缝适应。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长序列建模` `稀疏注意力` `稠密注意力` `可切换注意力` `语言模型` `长文本理解` `思维链推理`

## 📋 核心要点

1. 现有稀疏注意力方法引入过多参数，破坏了“短预训练，长微调”流程，导致收敛慢、难加速。
2. InfLLM-V2通过无参数架构修改重用稠密注意力参数，保持短长序列处理一致性，实现无缝适应。
3. InfLLM-V2在短序列使用稠密注意力，长序列使用稀疏注意力，兼顾效率与性能，加速效果显著。

## 📝 摘要（中文）

现代大型语言模型对长序列处理能力至关重要。然而，标准Transformer架构中的自注意力机制在处理长序列时面临严重的计算和内存瓶颈。可训练的稀疏注意力方法提供了一种有希望的解决方案，但现有方法（如NSA）引入了过多的额外参数，并破坏了传统的“短序列预训练，长序列微调”工作流程，导致收敛缓慢和难以加速。为了克服这些限制，我们引入了一种稠密-稀疏可切换注意力框架，称为InfLLM-V2。InfLLM-V2是一种可训练的稀疏注意力机制，可以无缝地将模型从短序列适应到长序列。具体来说，InfLLM-V2通过无参数的架构修改重用稠密注意力参数，保持短序列和长序列处理之间的一致性。此外，InfLLM-V2通过对短输入使用稠密注意力，并平滑过渡到对长序列使用稀疏注意力，确保了所有序列长度上的计算效率。为了实现实际加速，我们进一步引入了InfLLM-V2的高效实现，显著降低了计算开销。在长上下文理解和思维链推理方面的实验表明，InfLLM-V2比稠密注意力快4倍，同时分别保留了98.1%和99.7%的性能。基于InfLLM-V2框架，我们训练并开源了MiniCPM4.1（https://huggingface.co/openbmb/MiniCPM4.1-8B），这是一个混合推理模型，为研究社区提供了一个可复现的实现。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理长序列时，标准的Transformer自注意力机制面临计算和内存瓶颈。可训练的稀疏注意力方法虽然有潜力，但如NSA等方法引入了过多的额外参数，破坏了传统的“短序列预训练，长序列微调”的工作流程，导致收敛速度慢，难以加速，并且增加了模型部署的成本。

**核心思路**：InfLLM-V2的核心思路是设计一种稠密-稀疏可切换的注意力机制，使得模型能够在短序列上利用稠密注意力的优势，并在长序列上平滑过渡到稀疏注意力，从而在保证性能的同时，降低计算和内存开销。通过重用稠密注意力的参数，避免引入额外的参数，保持了模型在短序列和长序列处理上的一致性，从而能够更好地利用预训练模型的知识。

**技术框架**：InfLLM-V2框架主要包含稠密注意力模块和稀疏注意力模块，以及一个切换机制。对于短序列，模型使用稠密注意力进行处理，以获得更好的性能。随着序列长度的增加，模型逐渐切换到稀疏注意力，以降低计算和内存开销。切换机制根据序列长度动态调整稠密和稀疏注意力的权重，实现平滑过渡。

**关键创新**：InfLLM-V2的关键创新在于其稠密-稀疏可切换的注意力机制，以及参数重用策略。通过参数重用，避免了引入额外的参数，保持了模型在短序列和长序列处理上的一致性。可切换的注意力机制使得模型能够根据序列长度动态调整计算资源，从而在保证性能的同时，降低计算和内存开销。

**关键设计**：InfLLM-V2的关键设计包括：1) 无参数的架构修改，以重用稠密注意力参数；2) 基于序列长度的动态切换机制，用于平滑过渡到稀疏注意力；3) 高效的稀疏注意力实现，以降低计算开销。具体的参数设置和网络结构细节未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

实验结果表明，InfLLM-V2在长上下文理解和思维链推理任务上，比稠密注意力快4倍，同时分别保留了98.1%和99.7%的性能。基于InfLLM-V2框架训练的MiniCPM4.1模型已开源，为研究社区提供了一个可复现的实现。

## 🎯 应用场景

InfLLM-V2适用于需要处理长序列的各种自然语言处理任务，例如长文本摘要、文档问答、代码生成和长对话等。该方法可以显著降低计算和内存开销，使得大型语言模型能够更好地处理长序列，从而提升模型在这些任务上的性能。此外，该方法还可以应用于资源受限的设备上，使得这些设备也能够运行大型语言模型。

## 📄 摘要（原文）

> Long-sequence processing is a critical capability for modern large language models. However, the self-attention mechanism in the standard Transformer architecture faces severe computational and memory bottlenecks when processing long sequences. While trainable sparse attention methods offer a promising solution, existing approaches such as NSA introduce excessive extra parameters and disrupt the conventional \textit{pretrain-on-short, finetune-on-long} workflow, resulting in slow convergence and difficulty in acceleration. To overcome these limitations, we introduce dense-sparse switchable attention framework, termed as InfLLM-V2. InfLLM-V2 is a trainable sparse attention that seamlessly adapts models from short to long sequences. Specifically, InfLLM-V2 reuses dense attention parameters through parameter-free architecture modification, maintaining consistency between short and long sequence processing. Additionally, InfLLM-V2 ensures computational efficiency across all sequence lengths, by using dense attention for short inputs and smoothly transitioning to sparse attention for long sequences. To achieve practical acceleration, we further introduce an efficient implementation of InfLLM-V2 that significantly reduces the computational overhead. Our experiments on long-context understanding and chain-of-thought reasoning demonstrate that InfLLM-V2 is 4$\times$ faster than dense attention while retaining 98.1% and 99.7% of the performance, respectively. Based on the InfLLM-V2 framework, we have trained and open-sourced MiniCPM4.1 (https://huggingface.co/openbmb/MiniCPM4.1-8B), a hybrid reasoning model, providing a reproducible implementation for the research community.

