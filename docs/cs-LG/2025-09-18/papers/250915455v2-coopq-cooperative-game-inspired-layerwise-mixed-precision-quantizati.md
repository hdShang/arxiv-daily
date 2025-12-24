---
layout: default
title: "CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs"
---

# CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15455" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15455v2</a>
  <a href="https://arxiv.org/pdf/2509.15455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15455v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15455v2', 'CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junchen Zhao, Ali Derakhshan, Jayden Kana Hyman, Junhao Dong, Sangeetha Abdu Jyothi, Ian Harris

**分类**: cs.LG

**发布日期**: 2025-09-18 (更新: 2025-12-12)

---

## 💡 一句话要点

**提出CoopQ，利用合作博弈优化LLM混合精度量化，显著提升低比特量化性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合精度量化` `大型语言模型` `合作博弈` `Shapley值` `低比特量化` `模型压缩` `量化感知训练`

## 📋 核心要点

1. 现有混合精度量化方法在低比特（<4bit）时性能下降，原因是忽略了层间依赖关系，仅关注孤立的层级指标。
2. CoopQ将混合精度量化视为层之间的合作博弈，利用Shapley值评估层敏感性和层间交互，指导量化策略。
3. 实验表明，CoopQ在Llama-3、Gemma-2和Qwen-3等模型上，相比现有方法，显著降低了低比特量化下的困惑度。

## 📝 摘要（中文）

大型语言模型(LLMs)展现了强大的能力，但其数十亿的参数规模使得在设备端或低资源环境下的部署变得困难。混合精度量化提供了一个有吸引力的解决方案，但现有方法在平均精度降至4比特以下时表现不佳，因为它们依赖于孤立的、特定于层的指标，忽略了影响整体性能的关键层间交互。为了解决这些限制，我们首先将混合精度量化问题构建为层之间的合作博弈，并引入基于Shapley值的渐进量化估计(SPQE)，以有效地获得层敏感性和层间交互的精确Shapley估计。利用SPQE估计，我们提出了受合作博弈启发的混合精度量化(CoopQ)，它将这些Shapley估计转化为二元二次优化公式，在严格的内存约束下为层分配2或4比特精度。在Llama-3、Gemma-2和Qwen-3模型上，跨三个独立的PTQ后端(Quanto、HQQ、GPTQ)进行的全面实验表明，与仅依赖于孤立指标的方法相比，CoopQ具有可扩展性和始终优越的性能。在4比特到2比特的平均精度范围内，CoopQ相对于最佳基线降低了20-80%的困惑度，并且随着比特宽度的收紧，这一优势越来越大。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在低比特混合精度量化时性能显著下降的问题。现有方法主要基于孤立的层级指标进行量化，忽略了层与层之间的相互依赖关系，导致整体性能不佳。尤其是在平均精度低于4比特时，这种问题更加突出。

**核心思路**：论文将混合精度量化问题建模为一个合作博弈，其中每一层都是一个参与者。通过评估每一层对整体性能的贡献（Shapley值），并考虑层间的相互作用，来确定每一层的最佳量化精度。这种方法能够更准确地反映每一层的重要性，从而优化整体量化策略。

**技术框架**：CoopQ包含两个主要阶段：1) Shapley-based Progressive Quantization Estimation (SPQE)：使用SPQE有效地估计每一层的Shapley值，反映其对模型性能的贡献。SPQE通过逐步量化不同的层子集，并观察性能变化，来近似计算Shapley值。2) Cooperative Game Inspired Mixed-Precision Quantization：将SPQE估计的Shapley值转化为一个二元二次优化问题，目标是在满足内存约束的条件下，最大化模型的性能。该优化问题决定了每一层应该使用2比特还是4比特精度。

**关键创新**：CoopQ的关键创新在于将合作博弈理论引入到混合精度量化中。通过Shapley值来量化层间依赖关系，克服了传统方法中孤立地评估每一层的局限性。SPQE算法能够高效地估计Shapley值，使得CoopQ能够应用于大型语言模型。

**关键设计**：CoopQ使用二元二次优化来确定每一层的量化精度。目标函数是基于Shapley值构建的，反映了每一层对模型性能的贡献。约束条件是内存约束，确保量化后的模型大小不超过预设的阈值。SPQE算法通过逐步量化不同的层子集，并观察性能变化，来近似计算Shapley值。具体而言，SPQE采用了一种progressive的方式，逐步增加量化的层数，从而减少计算复杂度。

## 📊 实验亮点

实验结果表明，CoopQ在Llama-3、Gemma-2和Qwen-3等模型上，相比于现有最佳基线，在平均精度为4比特到2比特的范围内，降低了20-80%的困惑度。并且，随着比特宽度的降低，CoopQ的优势更加明显，证明了其在低比特量化方面的有效性。

## 🎯 应用场景

CoopQ可应用于在资源受限的设备上部署大型语言模型，例如移动设备、嵌入式系统和边缘计算设备。通过降低模型大小和计算复杂度，CoopQ使得这些设备能够运行更强大的AI模型，从而实现更智能的应用，如本地化的自然语言处理、智能助手和实时翻译。

## 📄 摘要（原文）

> Large Language Models (LLMs) promise impressive capabilities, yet their multi-billion-parameter scale makes on-device or low-resource deployment prohibitive. Mixed-precision quantization offers a compelling solution, but existing methods struggle when the average precision drops below four bits, as they rely on isolated, layer-specific metrics that overlook critical inter-layer interactions affecting overall performance. To address these limitations, we first frame the mixed-precision quantization problem as a cooperative game among layers and introduce Shapley-based Progressive Quantization Estimation (SPQE) to efficiently obtain accurate Shapley estimates of layer sensitivities and inter-layer interactions. Leveraging the SPQE estimates, we propose Cooperative Game Inspired Mixed-Precision Quantization (CoopQ) which translates these Shapley estimates into a binary quadratic optimization formulation, assigning either 2 or 4-bit precision to layers under strict memory constraints. Comprehensive experiments conducted on Llama-3, Gemma-2, and Qwen-3 models across three independent PTQ backends (Quanto, HQQ, GPTQ) demonstrate CoopQ's scalability and consistently superior performance compared to methods relying solely on isolated metrics. Across average precisions spanning 4 bit down to 2 bit, CoopQ cuts Perplexity by 20 - 80 % relative to the best baseline, with the margin growing as the bit-width tightens.

