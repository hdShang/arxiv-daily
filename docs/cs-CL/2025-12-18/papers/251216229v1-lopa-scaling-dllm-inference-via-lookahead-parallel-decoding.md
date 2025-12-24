---
layout: default
title: "LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding"
---

# LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16229" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16229v1</a>
  <a href="https://arxiv.org/pdf/2512.16229.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16229v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16229v1', 'LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenkai Xu, Yijie Jin, Jiajun Li, Yi Tu, Guoping Long, Dandan Tu, Tianqi Hou, Junchi Yan, Zhijie Deng

**分类**: cs.CL

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/zhijie-group/LoPA)

---

## 💡 一句话要点

**LoPA：通过前瞻并行解码加速扩散大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `大语言模型` `并行解码` `推理加速` `Token填充顺序`

## 📋 核心要点

1. 现有扩散大语言模型推理受限于置信度驱动的解码策略，并行度低，严重影响推理速度。
2. LoPA通过并行探索不同的Token填充顺序，并基于置信度选择最优方案，从而提升并行度。
3. 实验表明，LoPA显著提升了D2F模型的解码效率，并在GSM8K数据集上实现了更高的TPF和性能。

## 📝 摘要（中文）

扩散大语言模型(dLLM)在高速推理方面展现出巨大潜力。然而，当前基于置信度的解码策略受到有限并行性的约束，通常每次前向传播只能实现1-3个token。本文发现dLLM推理过程中的并行度对Token填充顺序(TFO)高度敏感。因此，我们提出了Lookahead PArallel Decoding (LoPA)，一种无需训练、即插即用的算法，用于识别更优的TFO，从而加速推理。LoPA通过并行分支同时探索不同的候选TFO，并基于分支置信度选择具有最高未来并行潜力的TFO。我们将LoPA应用于最先进的D2F模型，观察到解码效率的显著提高。值得注意的是，LoPA将GSM8K上的D2F-Dream的TPF提高到10.1，同时保持优于Dream基线的性能。此外，为了支持这种前所未有的并行度，我们开发了一种专门的多设备推理系统，该系统具有分支并行性(BP)，在多GPU部署下实现了每秒1073.9个token的单样本吞吐量。代码已开源。

## 🔬 方法详解

**问题定义**：扩散大语言模型（dLLM）的推理速度受限于其解码过程的并行度。现有的基于置信度的解码策略，如D2F，在选择下一个要填充的token时，通常只能实现较低的并行度（1-3个token/次前向传播）。这主要是因为token填充顺序（TFO）的选择会显著影响后续解码的并行潜力。如果选择了不合适的TFO，可能会导致后续token的填充必须串行进行，从而降低整体推理速度。

**核心思路**：LoPA的核心思想是通过前瞻性的并行探索不同的TFO，并选择能够最大化未来并行度的TFO。具体来说，LoPA维护多个并行的解码分支，每个分支代表一种不同的TFO。通过并行地评估这些分支的置信度，LoPA可以预测每个TFO在未来解码过程中能够实现的并行度。然后，LoPA选择具有最高并行度潜力的分支继续解码。

**技术框架**：LoPA的整体框架包括以下几个主要步骤：1）**初始化**：从当前已解码的token序列出发，生成多个候选的TFO。2）**并行解码**：对于每个候选TFO，创建一个解码分支，并并行地进行解码。3）**置信度评估**：评估每个解码分支的置信度，用于预测未来解码的并行度。4）**分支选择**：选择具有最高置信度的解码分支，并将其作为下一步解码的基础。5）**迭代**：重复步骤1-4，直到生成完整的token序列。为了支持LoPA的高并行度，论文还开发了一个专门的多设备推理系统，该系统利用分支并行性（BP）在多个GPU上并行执行不同的解码分支。

**关键创新**：LoPA的关键创新在于其前瞻性的并行解码策略。与传统的贪心解码方法不同，LoPA不是简单地选择当前置信度最高的token，而是通过并行探索不同的TFO，并选择能够最大化未来并行度的TFO。这种前瞻性的策略能够显著提高dLLM的推理速度。此外，LoPA是一种无需训练的即插即用算法，可以方便地应用于现有的dLLM模型。

**关键设计**：LoPA的关键设计包括：1）**TFO生成**：论文采用了一种启发式的TFO生成方法，该方法基于token之间的依赖关系来生成候选的TFO。2）**置信度评估**：论文使用模型的输出概率作为置信度，并结合一些启发式规则来预测未来解码的并行度。3）**分支并行性（BP）**：论文开发了一种专门的多设备推理系统，该系统利用BP在多个GPU上并行执行不同的解码分支，从而充分利用硬件资源。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LoPA在D2F-Dream模型上取得了显著的性能提升。在GSM8K数据集上，LoPA将TPF提高到10.1，同时保持了优于Dream基线的性能。此外，通过开发专门的多设备推理系统，LoPA实现了每秒1073.9个token的单样本吞吐量，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

LoPA具有广泛的应用前景，可以应用于各种需要高速推理的场景，例如实时对话系统、机器翻译、文本摘要等。通过提高dLLM的推理速度，LoPA可以降低计算成本，并使得dLLM能够部署在资源受限的设备上。此外，LoPA的即插即用特性使其可以方便地应用于现有的dLLM模型，从而加速这些模型的部署和应用。

## 📄 摘要（原文）

> Diffusion Large Language Models (dLLMs) have demonstrated significant potential for high-speed inference. However, current confidence-driven decoding strategies are constrained by limited parallelism, typically achieving only 1--3 tokens per forward pass (TPF). In this work, we identify that the degree of parallelism during dLLM inference is highly sensitive to the Token Filling Order (TFO). Then, we introduce Lookahead PArallel Decoding LoPA, a training-free, plug-and-play algorithm, to identify a superior TFO and hence accelerate inference. LoPA concurrently explores distinct candidate TFOs via parallel branches, and selects the one with the highest potential for future parallelism based on branch confidence. We apply LoPA to the state-of-the-art D2F model and observe a substantial enhancement in decoding efficiency. Notably, LoPA increases the TPF of D2F-Dream to 10.1 on the GSM8K while maintaining performance superior to the Dream baseline. Furthermore, to facilitate this unprecedented degree of parallelism, we develop a specialized multi-device inference system featuring Branch Parallelism (BP), which achieves a single-sample throughput of 1073.9 tokens per second under multi-GPU deployment. The code is available at https://github.com/zhijie-group/LoPA.

