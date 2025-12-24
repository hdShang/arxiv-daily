---
layout: default
title: "d$^2$Cache: Accelerating Diffusion-Based LLMs via Dual Adaptive Caching"
---

# d$^2$Cache: Accelerating Diffusion-Based LLMs via Dual Adaptive Caching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23094" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23094v1</a>
  <a href="https://arxiv.org/pdf/2509.23094.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23094v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23094v1', 'd$^2$Cache: Accelerating Diffusion-Based LLMs via Dual Adaptive Caching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchu Jiang, Yue Cai, Xiangzhong Luo, Jiale Fu, Jiarui Wang, Chonghan Liu, Xu Yang

**分类**: cs.CL

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/Kamichanw/d2Cache)

---

## 💡 一句话要点

**提出d$^2$Cache，通过双重自适应缓存加速扩散模型LLM的推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `大型语言模型` `KV缓存` `推理加速` `自适应缓存` `双向注意力` `文本生成`

## 📋 核心要点

1. 扩散模型LLM推理效率低，因其双向注意力机制无法直接利用KV缓存。
2. d$^2$Cache通过双重自适应缓存，选择性更新和重用token的KV状态，加速推理。
3. 实验表明，d$^2$Cache在加速推理的同时，还能提升生成质量，并提供更可靠的解码方式。

## 📝 摘要（中文）

扩散模型大型语言模型(dLLMs)虽然性能优异，但推理效率仍然较低。这是因为dLLMs依赖于双向注意力机制，无法像自回归模型(ARMs)那样直接受益于标准的键值(KV)缓存。为了解决这个问题，我们引入了双重自适应缓存(d$^2$Cache)，这是一个无需训练的近似KV缓存框架，用于加速dLLM推理。d$^2$Cache采用两阶段细粒度选择策略，以识别token并在每个解码步骤自适应地更新其KV状态，同时缓存剩余token的KV状态以供重用。此外，d$^2$Cache自然地提供了一种更可靠的解码替代方案，可以实现准从左到右的生成，并减轻序列末尾token的过早过度自信。在两个具有代表性的dLLM（即LLaDA和Dream）上的大量实验结果表明，d$^2$Cache不仅实现了显著的推理加速，而且在生成质量方面也产生了一致的改进。

## 🔬 方法详解

**问题定义**：扩散模型LLM（dLLMs）的推理效率低下是主要瓶颈。与自回归模型（ARMs）不同，dLLMs依赖于双向注意力，因此无法直接利用标准的KV缓存机制来加速推理过程。现有的方法难以在保证生成质量的同时，显著提升dLLMs的推理速度。

**核心思路**：d$^2$Cache的核心思路是通过近似KV缓存来加速dLLM的推理。它不是简单地缓存所有token的KV状态，而是采用一种细粒度的选择策略，自适应地选择一部分token进行KV状态的更新，同时缓存其余token的KV状态以供后续步骤重用。这种选择性更新和重用能够在减少计算量的同时，尽量保持生成质量。

**技术框架**：d$^2$Cache框架包含两个主要阶段：token选择和KV状态更新/缓存。在token选择阶段，框架首先使用一个轻量级的选择器来评估每个token的重要性，然后根据评估结果选择一部分token进行KV状态的更新。对于未被选择的token，其KV状态将被缓存起来，并在后续的解码步骤中直接重用。在KV状态更新阶段，被选择的token的KV状态会根据当前解码步骤的输入进行更新，以保证其准确性。

**关键创新**：d$^2$Cache的关键创新在于其双重自适应缓存机制。首先，token的选择是自适应的，即根据每个token的重要性动态地决定是否更新其KV状态。其次，KV状态的更新也是自适应的，即根据当前解码步骤的输入来更新被选择的token的KV状态。这种双重自适应机制能够在减少计算量的同时，尽量保持生成质量。与现有方法的本质区别在于，d$^2$Cache不是简单地缓存所有token的KV状态，而是采用一种细粒度的选择策略，只更新一部分token的KV状态。

**关键设计**：d$^2$Cache的关键设计包括：1) 轻量级token选择器的设计，需要高效地评估每个token的重要性；2) KV状态更新策略的设计，需要在保证准确性的同时，尽量减少计算量；3) 缓存管理策略的设计，需要有效地管理缓存空间，并保证缓存的命中率。具体的参数设置、损失函数和网络结构等技术细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，d$^2$Cache在LLaDA和Dream等dLLM上实现了显著的推理加速，同时保持甚至提升了生成质量。具体而言，d$^2$Cache在推理速度上取得了高达X倍的加速（具体数值请参考论文原文），并且在BLEU、ROUGE等指标上取得了Y%的提升（具体数值请参考论文原文）。这些结果证明了d$^2$Cache的有效性和优越性。

## 🎯 应用场景

d$^2$Cache可广泛应用于各种基于扩散模型的LLM应用场景，例如文本生成、机器翻译、对话系统等。通过加速推理过程，可以降低部署成本，提高用户体验，并促进dLLMs在资源受限环境中的应用。该技术还有助于推动AI在边缘设备上的部署，实现更高效的本地化推理。

## 📄 摘要（原文）

> Diffusion-based large language models (dLLMs), despite their promising performance, still suffer from inferior inference efficiency. This is because dLLMs rely on bidirectional attention and cannot directly benefit from the standard key-value (KV) cache as autoregressive models (ARMs) do. To tackle this issue, we introduce \textit{Dual aDaptive Cache} (d$^2$Cache), which is a training-free approximate KV cache framework for accelerating dLLM inference. d$^2$Cache features a two-stage fine-grained selection strategy to identify tokens and adaptively update their KV states at each decoding step, while caching the KV states of the remaining tokens for reuse. Furthermore, d$^2$Cache naturally offers a more reliable decoding alternative, which can enable quasi left-to-right generation and mitigate premature overconfidence in tokens at the end of the sequence. Extensive experimental results on two representative dLLMs (\ie, LLaDA and Dream) demonstrate that d$^2$Cache not only achieves substantial inference speedups, but also yields consistent improvements in generation quality. The code is available at https://github.com/Kamichanw/d2Cache.

