---
layout: default
title: "AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size"
---

# AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26432" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26432v2</a>
  <a href="https://arxiv.org/pdf/2509.26432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26432v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26432v2', 'AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanxi Lu, Hao Mark Chen, Yuto Karashima, Zhican Wang, Daichi Fujiki, Hongxiang Fan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-01)

**备注**: Preprint. Under review

---

## 💡 一句话要点

**AdaBlock-dLLM：通过自适应块大小实现语义感知的扩散LLM推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `大语言模型` `半自回归解码` `自适应块大小` `推理优化`

## 📋 核心要点

1. 传统半自回归解码采用固定块大小，导致高置信度token延迟解码和低置信度token过早提交，影响效率和准确性。
2. AdaBlock-dLLM通过分析解码过程中的置信度动态，识别波动带区域，从而自适应地调整块大小，对齐语义边界。
3. 实验表明，AdaBlock-dLLM在相同吞吐量下，能够提升高达5.3%的精度，展示了自适应块大小的有效性。

## 📝 摘要（中文）

基于扩散的大语言模型(dLLMs)因其固有的并行解码能力而备受关注，为自回归LLM提供了一种引人注目的替代方案。在各种解码策略中，分块半自回归(semi-AR)方法因其对KV缓存的自然支持以及良好的精度-速度权衡而被广泛采用。然而，本文指出了传统采用固定块大小的semi-AR解码方法的两个基本局限性：i) 后期解码开销，即不必要地延迟了解码当前块外部的高置信度token；ii) 提前解码错误，即过早地提交当前块内的低置信度token，导致错误的token。本文首次对semi-AR解码中固定块大小的假设提出了系统的研究。通过对去噪过程中置信度动态的统计分析，我们识别了dLLM解码过程中的波动带(VB)区域，该区域编码了局部语义结构，可用于指导自适应块大小调整。利用这些见解，我们引入了AdaBlock-dLLM，这是一种无需训练、即插即用的调度器，通过在运行时调整块大小，自适应地将块边界与语义步骤对齐。在各种基准测试中进行的大量实验表明，在相同的吞吐量预算下，AdaBlock-dLLM实现了高达5.3%的精度提升。除了推理时优化之外，我们希望我们这种语义感知的自适应调度方法和基于置信度的分析能够激发未来dLLM的训练策略。

## 🔬 方法详解

**问题定义**：论文旨在解决基于扩散的LLM（dLLM）中，使用固定块大小的半自回归（semi-AR）解码方法存在的效率和准确性问题。现有方法的痛点在于，固定块大小无法适应token置信度的动态变化，导致高置信度token的解码延迟和低置信度token的过早提交，从而影响整体性能。

**核心思路**：论文的核心思路是根据解码过程中token置信度的变化，自适应地调整块的大小。通过识别一个“波动带”（Volatility Band, VB）区域，该区域反映了局部语义结构，从而动态地调整块边界，使其与语义步骤对齐。这样可以避免不必要的延迟解码和提前解码错误。

**技术框架**：AdaBlock-dLLM是一个即插即用的调度器，无需额外的训练。其主要流程包括：1) 在解码过程中，监控token的置信度变化；2) 基于置信度变化，识别波动带区域；3) 根据波动带区域，动态调整块的大小，使其与语义边界对齐；4) 使用调整后的块大小进行半自回归解码。

**关键创新**：最重要的技术创新点在于提出了语义感知的自适应块大小调整方法。与现有固定块大小的方法不同，AdaBlock-dLLM能够根据token的置信度动态调整块大小，从而更好地适应解码过程中的语义变化。这种自适应性是其性能提升的关键。

**关键设计**：AdaBlock-dLLM的关键设计在于波动带（VB）的识别和块大小的调整策略。具体来说，VB的识别可能涉及到对token置信度变化率的阈值设定，以及对历史置信度信息的加权平均等。块大小的调整策略则可能涉及到根据VB的宽度和位置，动态调整块的起始位置和长度。

## 📊 实验亮点

实验结果表明，AdaBlock-dLLM在各种基准测试中均取得了显著的性能提升。在相同的吞吐量预算下，AdaBlock-dLLM能够实现高达5.3%的精度提升。这些结果验证了自适应块大小调整方法的有效性，并表明AdaBlock-dLLM是一种有竞争力的dLLM推理优化方案。

## 🎯 应用场景

AdaBlock-dLLM具有广泛的应用前景，可应用于各种基于扩散模型的自然语言生成任务，例如文本摘要、机器翻译、对话生成等。通过提高推理效率和准确性，该方法可以降低dLLM的部署成本，并提升用户体验。未来，该研究可以进一步扩展到其他类型的生成模型，例如图像生成模型。

## 📄 摘要（原文）

> Diffusion-based large language models (dLLMs) are gaining attention for their inherent capacity for parallel decoding, offering a compelling alternative to autoregressive LLMs. Among various decoding strategies, blockwise semi-autoregressive (semi-AR) approaches are widely adopted due to their natural support for KV caching and their favorable accuracy-speed trade-off. However, this paper identifies two fundamental limitations in the conventional semi-AR decoding approach that applies a fixed block size: i) late decoding overhead, where the unmasking of high-confidence tokens outside the current block is unnecessarily delayed, and ii) premature decoding error, where low-confidence tokens inside the current block are committed too early, leading to incorrect tokens. This paper presents the first systematic investigation challenging the fixed block size assumption in semi-AR decoding. Through a statistical analysis of confidence dynamics during the denoising process, we identify a volatility band (VB) region during dLLM decoding, which encodes local semantic structure and can be used to guide adaptive block sizing. Leveraging these insights, we introduce AdaBlock-dLLM, a training-free, plug-and-play scheduler that adaptively aligns block boundaries with semantic steps by adjusting block size during runtime. Extensive experiments across diverse benchmarks show that AdaBlock-dLLM achieves up to 5.3% accuracy improvement under the same throughput budget. Beyond inference-time optimization, we hope our semantics-aware adaptive scheduling approach and confidence-based analysis will inspire future training strategies for dLLMs.

