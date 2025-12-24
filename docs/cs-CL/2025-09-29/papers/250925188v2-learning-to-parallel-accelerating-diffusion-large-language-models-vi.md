---
layout: default
title: "Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding"
---

# Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25188" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25188v2</a>
  <a href="https://arxiv.org/pdf/2509.25188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25188v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25188v2', 'Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenrui Bao, Zhiben Chen, Dan Xu, Yuzhang Shang

**分类**: cs.CL

**发布日期**: 2025-09-29 (更新: 2025-10-03)

---

## 💡 一句话要点

**提出Learn2PD以解决大语言模型推理速度瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `并行解码` `自适应过滤` `扩散模型` `自然语言处理` `推理速度` `机器学习` `EoTP`

## 📋 核心要点

1. 现有的自回归解码方法在推理过程中需要顺序处理，导致速度瓶颈，限制了大型语言模型的应用。
2. 本文提出Learn2PD框架，通过训练自适应过滤模型，动态预测每个标记的最终输出，优化并行解码过程。
3. 实验结果显示，Learn2PD在LLaDA基准上实现了最高22.58倍的速度提升，结合KV-Cache时可达57.51倍，且无性能下降。

## 📝 摘要（中文）

自回归解码在大型语言模型（LLMs）中需要$	ext{O}(n)$的顺序步骤来处理$n$个标记，这在根本上限制了推理吞吐量。近期的扩散基础LLMs（dLLMs）通过迭代去噪实现了并行标记生成。然而，现有的并行解码策略依赖于固定的、与输入无关的启发式方法（如置信度阈值），未能适应输入特征，导致在不同NLP任务中速度与质量的权衡不理想。本文提出了一种更灵活和动态的并行解码方法，名为学习并行解码（Learn2PD），该框架训练一个轻量级自适应过滤模型，预测每个标记位置的当前预测是否与最终输出匹配。该过滤器在后训练阶段学习，优化计算量小（仅需分钟级GPU时间）。实验表明，该方法在LLaDA基准上实现了最高22.58倍的加速，且没有性能下降，结合KV-Cache时可达57.51倍的加速。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在自回归解码中存在的速度瓶颈问题。现有方法依赖于固定的启发式策略，无法根据输入特征进行动态调整，导致速度与质量的权衡不理想。

**核心思路**：论文提出了Learn2PD框架，通过训练一个轻量级的自适应过滤模型，预测每个标记位置的当前预测是否与最终输出匹配，从而实现更高效的并行解码。

**技术框架**：该框架包括两个主要模块：自适应过滤模型和结束标记预测（EoTP）。自适应过滤模型用于动态判断标记的预测准确性，而EoTP用于检测序列解码的完成，避免冗余的填充标记解码。

**关键创新**：最重要的创新在于引入了自适应过滤模型，该模型在后训练阶段学习，能够根据输入特征动态调整解码策略，与现有固定策略形成鲜明对比。

**关键设计**：过滤模型的训练仅需少量计算资源（分钟级GPU时间），并且通过优化损失函数来提高预测准确性。此外，EoTP的引入有效减少了不必要的解码步骤，进一步提升了整体效率。

## 📊 实验亮点

实验结果表明，Learn2PD在LLaDA基准上实现了最高22.58倍的速度提升，且在结合KV-Cache时可达57.51倍的加速，且在此过程中没有性能下降，展示了其在加速解码过程中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的实时对话系统、文本生成和机器翻译等场景。通过提高推理速度，Learn2PD能够显著提升用户体验，满足对快速响应的需求，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Autoregressive decoding in large language models (LLMs) requires $\mathcal{O}(n)$ sequential steps for $n$ tokens, fundamentally limiting inference throughput. Recent diffusion-based LLMs (dLLMs) enable parallel token generation through iterative denoising. However, current parallel decoding strategies rely on fixed, input-agnostic heuristics (e.g., confidence thresholds), which fail to adapt to input-specific characteristics, resulting in suboptimal speed-quality trade-offs across diverse NLP tasks. In this work, we explore a more flexible and dynamic approach to parallel decoding. We propose Learning to Parallel Decode (Learn2PD), a framework that trains a lightweight and adaptive filter model to predict, for each token position, whether the current prediction matches the final output. This learned filter approximates an oracle parallel decoding strategy that unmasks tokens only when correctly predicted. Importantly, the filter model is learned in a post-training manner, requiring only a small amount of computation to optimize it (minute-level GPU time). Additionally, we introduce End-of-Text Prediction (EoTP) to detect decoding completion at the end of sequence, avoiding redundant decoding of padding tokens. Experiments on the LLaDA benchmark demonstrate that our method achieves up to 22.58$\times$ speedup without any performance drop, and up to 57.51$\times$ when combined with KV-Cache.

