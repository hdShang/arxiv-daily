---
layout: default
title: "SpikingBrain: Spiking Brain-inspired Large Models"
---

# SpikingBrain: Spiking Brain-inspired Large Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05276" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05276v3</a>
  <a href="https://arxiv.org/pdf/2509.05276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05276v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05276v3', 'SpikingBrain: Spiking Brain-inspired Large Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Pan, Yupeng Feng, Jinghao Zhuang, Siyu Ding, Han Xu, Zehao Liu, Bohan Sun, Yuhong Chou, Xuerui Qiu, Anlin Deng, Anjie Hu, Shurong Wang, Peng Zhou, Man Yao, Jibin Wu, Jian Yang, Guoliang Sun, Bo Xu, Guoqi Li

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-05 (更新: 2025-12-01)

---

## 💡 一句话要点

**SpikingBrain：受脑启发的大模型，提升长文本处理效率并降低功耗**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脉冲神经网络` `大语言模型` `长文本处理` `线性注意力` `低功耗计算` `MetaX GPU` `模型优化`

## 📋 核心要点

1. 现有基于Transformer的大语言模型在长文本处理中面临计算和内存瓶颈，限制了其应用。
2. SpikingBrain通过线性/混合线性注意力、脉冲神经元和定制的训练流程，实现了高效的长文本处理。
3. SpikingBrain模型在长文本任务上表现出显著的加速和内存优化，并实现了高稀疏性，降低了功耗。

## 📝 摘要（中文）

本文介绍了SpikingBrain，一个受脑启发的模型家族，旨在提高长文本训练和推理的效率。SpikingBrain利用MetaX GPU集群，重点关注三个方面：模型架构（具有自适应脉冲神经元的线性及混合线性注意力机制）、算法优化（高效的基于转换的训练流程和专用脉冲编码框架）以及系统工程（为MetaX硬件定制的训练框架、算子库和并行策略）。研究人员开发了SpikingBrain-7B（线性LLM）和SpikingBrain-76B（混合线性MoE LLM）两个模型，证明了在非NVIDIA平台上开发大规模LLM的可行性。SpikingBrain在持续预训练中使用约150B tokens，性能与开源Transformer基线相当，并显著提高了长文本效率，实现了（部分）恒定内存和事件驱动的脉冲行为。例如，SpikingBrain-7B在4M token序列的首次token生成时间上实现了超过100倍的加速，脉冲方案实现了69.15%的稀疏性，从而降低了功耗。

## 🔬 方法详解

**问题定义**：现有基于Transformer的大语言模型在处理长文本时，训练计算量随序列长度呈平方增长，推理内存呈线性增长，导致效率低下。同时，在非NVIDIA平台上训练大型模型也面临稳定性和效率的挑战。

**核心思路**：SpikingBrain的核心思路是借鉴大脑的脉冲神经元机制，设计一种新型的、更高效的大语言模型架构。通过线性注意力机制、脉冲编码和专门的硬件优化，降低计算复杂度和内存需求，从而实现高效的长文本处理和推理。

**技术框架**：SpikingBrain的技术框架主要包括三个部分：1) 模型架构：采用线性或混合线性注意力机制，并结合自适应脉冲神经元；2) 算法优化：设计高效的基于转换的训练流程和专用的脉冲编码框架；3) 系统工程：针对MetaX硬件定制训练框架、算子库和并行策略。整体流程是从数据预处理开始，经过脉冲编码，输入到SpikingBrain模型进行训练或推理，最后解码得到结果。

**关键创新**：SpikingBrain的关键创新在于将脉冲神经元和线性注意力机制引入到大语言模型中。与传统的Transformer模型相比，SpikingBrain通过脉冲编码和线性注意力降低了计算复杂度，并实现了更高的稀疏性，从而提高了效率和降低了功耗。

**关键设计**：SpikingBrain的关键设计包括：1) 自适应脉冲神经元：根据输入动态调整脉冲发放频率；2) 线性注意力机制：降低了注意力计算的复杂度；3) 脉冲编码框架：将连续的输入转换为离散的脉冲序列；4) 针对MetaX硬件的优化：定制了训练框架、算子库和并行策略，以充分利用硬件性能。

## 📊 实验亮点

SpikingBrain-7B在4M token序列的首次token生成时间上实现了超过100倍的加速。脉冲方案实现了69.15%的稀疏性，显著降低了功耗。SpikingBrain-7B和SpikingBrain-76B在性能上与开源Transformer基线相当，同时使用了更少的tokens进行持续预训练，证明了其高效性。

## 🎯 应用场景

SpikingBrain具有广泛的应用前景，包括长文本生成、对话系统、信息检索等领域。其高效的计算和低功耗特性使其特别适用于资源受限的场景，如移动设备、边缘计算和嵌入式系统。未来，SpikingBrain有望推动大语言模型在更多领域的应用，并促进人工智能技术的可持续发展。

## 📄 摘要（原文）

> Mainstream Transformer-based large language models face major efficiency bottlenecks: training computation scales quadratically with sequence length, and inference memory grows linearly, limiting long-context processing. Building large models on non-NVIDIA platforms also poses challenges for stable and efficient training. To address this, we introduce SpikingBrain, a family of brain-inspired models designed for efficient long-context training and inference. SpikingBrain leverages the MetaX GPU cluster and focuses on three aspects: (1) Model Architecture: linear and hybrid-linear attention architectures with adaptive spiking neurons; (2) Algorithmic Optimizations: an efficient, conversion-based training pipeline and a dedicated spike coding framework; (3) System Engineering: customized training frameworks, operator libraries, and parallelism strategies tailored to MetaX hardware.
>   Using these techniques, we develop two models: SpikingBrain-7B, a linear LLM, and SpikingBrain-76B, a hybrid-linear MoE LLM. These models demonstrate the feasibility of large-scale LLM development on non-NVIDIA platforms, and training remains stable for weeks on hundreds of MetaX GPUs with Model FLOPs Utilization at expected levels. SpikingBrain achieves performance comparable to open-source Transformer baselines while using only about 150B tokens for continual pre-training. Our models also significantly improve long-context efficiency and deliver inference with (partially) constant memory and event-driven spiking behavior. For example, SpikingBrain-7B attains over 100x speedup in Time to First Token for 4M-token sequences. Furthermore, the proposed spiking scheme achieves 69.15 percent sparsity, enabling low-power operation. Overall, this work demonstrates the potential of brain-inspired mechanisms to drive the next generation of efficient and scalable large model design.

