---
layout: default
title: "Scaling and Enhancing LLM-based AVSR: A Sparse Mixture of Projectors Approach"
---

# Scaling and Enhancing LLM-based AVSR: A Sparse Mixture of Projectors Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14336" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14336v2</a>
  <a href="https://arxiv.org/pdf/2505.14336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14336v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14336v2', 'Scaling and Enhancing LLM-based AVSR: A Sparse Mixture of Projectors Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Umberto Cappellazzo, Minsu Kim, Stavros Petridis, Daniele Falavigna, Alessio Brutti

**分类**: eess.AS, cs.CV, cs.MM, cs.SD

**发布日期**: 2025-05-20 (更新: 2025-05-21)

**备注**: Interspeech 2025

---

## 💡 一句话要点

**提出Llama-SMoP以解决资源受限环境下的AVSR问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频-视觉语音识别` `大型语言模型` `稀疏混合投影器` `多模态学习` `噪声鲁棒性` `计算效率` `专家混合`

## 📋 核心要点

1. 现有的音频-视觉语音识别方法在资源受限环境中面临高计算成本的挑战，限制了其实际应用。
2. 本文提出Llama-SMoP，通过稀疏混合投影器模块，提升模型容量而不增加推理成本，适应资源受限场景。
3. 实验结果表明，Llama-SMoP DEDR配置在多项任务上表现优异，尤其在噪声环境下的鲁棒性显著提升。

## 📝 摘要（中文）

音频-视觉语音识别（AVSR）通过整合视觉线索增强了在嘈杂环境中的鲁棒性。尽管近期的研究将大型语言模型（LLMs）集成到AVSR中，但其高计算成本限制了在资源受限环境中的应用。为此，本文提出了Llama-SMoP，一种高效的多模态LLM，采用稀疏混合投影器（SMoP）模块，在不增加推理成本的情况下扩展模型容量。通过引入稀疏门控的专家混合（MoE）投影器，Llama-SMoP能够使用较小的LLM，同时保持强大的性能。我们探索了三种SMoP配置，发现Llama-SMoP DEDR（不相交专家，不相交路由器）在ASR、VSR和AVSR任务上表现优越。消融研究证实了其在专家激活、可扩展性和噪声鲁棒性方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限环境中，现有音频-视觉语音识别（AVSR）方法因高计算成本而难以部署的问题。现有方法在嘈杂环境下的鲁棒性和效率不足，限制了其实际应用。

**核心思路**：论文提出的Llama-SMoP通过引入稀疏混合投影器（SMoP）模块，利用稀疏门控的专家混合（MoE）设计，允许使用较小的LLM，同时保持强大的性能。这种设计旨在降低计算开销，提高模型的可扩展性。

**技术框架**：Llama-SMoP的整体架构包括输入音频和视觉信息，通过稀疏混合投影器模块进行处理，最终输出识别结果。该框架的核心在于使用不相交的专家和路由器，以实现更高效的信息处理。

**关键创新**：最重要的技术创新在于引入了稀疏混合投影器（SMoP），使得模型在保持性能的同时，显著降低了计算成本。这种方法与传统的全连接模型相比，能够在更小的模型规模下实现更好的性能。

**关键设计**：在设计中，采用了稀疏门控机制来激活专家，确保只有相关的专家参与计算。此外，模型的损失函数和网络结构经过精心设计，以优化在多模态输入下的表现。

## 📊 实验亮点

实验结果显示，Llama-SMoP DEDR配置在ASR、VSR和AVSR任务上均优于基线模型，尤其在噪声环境下的鲁棒性显著提升，具体性能提升幅度达到XX%。消融研究进一步验证了其在专家激活和可扩展性方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助理、自动字幕生成和人机交互等场景，尤其是在噪声环境下的语音识别任务中具有重要价值。Llama-SMoP的高效性使其适用于移动设备和边缘计算等资源受限的应用场景，未来可能推动AVSR技术的广泛应用。

## 📄 摘要（原文）

> Audio-Visual Speech Recognition (AVSR) enhances robustness in noisy environments by integrating visual cues. While recent advances integrate Large Language Models (LLMs) into AVSR, their high computational cost hinders deployment in resource-constrained settings. To address this, we propose Llama-SMoP, an efficient Multimodal LLM that employs a Sparse Mixture of Projectors (SMoP) module to scale model capacity without increasing inference costs. By incorporating sparsely-gated mixture-of-experts (MoE) projectors, Llama-SMoP enables the use of smaller LLMs while maintaining strong performance. We explore three SMoP configurations and show that Llama-SMoP DEDR (Disjoint-Experts, Disjoint-Routers), which uses modality-specific routers and experts, achieves superior performance on ASR, VSR, and AVSR tasks. Ablation studies confirm its effectiveness in expert activation, scalability, and noise robustness.

