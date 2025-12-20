---
layout: default
title: LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding
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

**关键词**: `扩散大语言模型` `并行解码` `Token填充顺序` `推理加速` `多设备推理`

## 📋 核心要点

1. 现有扩散大语言模型推理受限于置信度驱动的解码策略，并行度低，严重影响推理速度。
2. LoPA通过并行探索不同的Token填充顺序，并基于置信度选择最优顺序，从而提升并行度。
3. 实验表明，LoPA显著提升了D2F模型的解码效率，在GSM8K上实现了更高的TPF和性能。

## 📝 摘要（中文）

扩散大语言模型(dLLM)在高速推理方面展现出巨大潜力。然而，当前基于置信度的解码策略受到有限并行性的约束，通常每次前向传播只能实现1-3个token的生成(TPF)。本文发现dLLM推理过程中的并行度对Token填充顺序(TFO)高度敏感。因此，我们提出了Lookahead PArallel Decoding (LoPA)，一种无需训练、即插即用的算法，用于识别更优的TFO，从而加速推理。LoPA通过并行分支同时探索不同的候选TFO，并基于分支置信度选择未来并行潜力最大的一个。我们将LoPA应用于最先进的D2F模型，观察到解码效率的显著提升。值得注意的是，LoPA在GSM8K上将D2F-Dream的TPF提高到10.1，同时保持优于Dream基线的性能。此外，为了支持这种前所未有的并行度，我们开发了一种专门的多设备推理系统，该系统具有分支并行性(BP)，在多GPU部署下实现了每秒1073.9个token的单样本吞吐量。代码已开源。

## 🔬 方法详解

**问题定义**：扩散大语言模型（dLLM）的推理速度受限于其解码过程的并行度。传统的置信度驱动的解码策略，由于其固有的串行性，导致每次前向传播只能生成少量的token，严重限制了推理效率。现有方法难以充分挖掘dLLM的并行潜力，成为提升推理速度的瓶颈。

**核心思路**：LoPA的核心思路是通过优化Token填充顺序（TFO）来提高dLLM推理的并行度。不同的TFO会导致不同的并行潜力。LoPA通过并行探索多个候选TFO，并根据每个分支的置信度来评估其未来并行潜力，从而选择最优的TFO。这种前瞻性的策略能够有效地挖掘dLLM的并行潜力，从而加速推理。

**技术框架**：LoPA的整体框架包括以下几个主要步骤：1) **并行分支探索**：同时探索多个不同的候选TFO，每个TFO对应一个并行分支。2) **置信度评估**：评估每个分支的置信度，用于衡量其未来并行潜力。3) **最优TFO选择**：基于置信度选择具有最高未来并行潜力的TFO。4) **并行解码**：使用选择的最优TFO进行并行解码，生成多个token。

**关键创新**：LoPA的关键创新在于其前瞻性的并行解码策略。与传统的串行解码方法不同，LoPA通过并行探索多个候选TFO，并根据置信度选择最优的TFO，从而最大化并行度。这种前瞻性的策略能够有效地挖掘dLLM的并行潜力，显著提升推理速度。此外，LoPA是一种无需训练、即插即用的算法，易于集成到现有的dLLM推理系统中。

**关键设计**：LoPA的关键设计包括：1) **分支数量**：并行探索的分支数量是一个重要的参数，需要根据计算资源和性能需求进行调整。2) **置信度评估方法**：置信度评估方法的选择会影响最优TFO的选择，需要根据具体的dLLM模型进行优化。3) **多设备推理系统**：为了支持高并行度，论文开发了一个专门的多设备推理系统，该系统具有分支并行性(BP)，能够充分利用多GPU的计算资源。

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

LoPA在D2F-Dream模型上取得了显著的性能提升。在GSM8K数据集上，LoPA将D2F-Dream的TPF提高到10.1，同时保持了优于Dream基线的性能。此外，通过开发专门的多设备推理系统，LoPA实现了每秒1073.9个token的单样本吞吐量，展示了其强大的并行解码能力。

## 🎯 应用场景

LoPA具有广泛的应用前景，可应用于各种需要高速推理的场景，例如实时对话系统、机器翻译、文本摘要等。通过提高dLLM的推理速度，LoPA可以显著提升这些应用的性能和用户体验。此外，LoPA还可以促进dLLM在资源受限设备上的部署，例如移动设备和嵌入式系统，从而拓展dLLM的应用范围。

## 📄 摘要（原文）

> Diffusion Large Language Models (dLLMs) have demonstrated significant potential for high-speed inference. However, current confidence-driven decoding strategies are constrained by limited parallelism, typically achieving only 1--3 tokens per forward pass (TPF). In this work, we identify that the degree of parallelism during dLLM inference is highly sensitive to the Token Filling Order (TFO). Then, we introduce Lookahead PArallel Decoding LoPA, a training-free, plug-and-play algorithm, to identify a superior TFO and hence accelerate inference. LoPA concurrently explores distinct candidate TFOs via parallel branches, and selects the one with the highest potential for future parallelism based on branch confidence. We apply LoPA to the state-of-the-art D2F model and observe a substantial enhancement in decoding efficiency. Notably, LoPA increases the TPF of D2F-Dream to 10.1 on the GSM8K while maintaining performance superior to the Dream baseline. Furthermore, to facilitate this unprecedented degree of parallelism, we develop a specialized multi-device inference system featuring Branch Parallelism (BP), which achieves a single-sample throughput of 1073.9 tokens per second under multi-GPU deployment. The code is available at https://github.com/zhijie-group/LoPA.

