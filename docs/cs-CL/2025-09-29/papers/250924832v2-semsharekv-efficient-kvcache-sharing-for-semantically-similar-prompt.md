---
layout: default
title: "SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching"
---

# SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24832" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24832v2</a>
  <a href="https://arxiv.org/pdf/2509.24832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24832v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24832v2', 'SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinye Zhao, Spyridon Mastorakis

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-12-16)

**备注**: 11 figures, 14pages

---

## 💡 一句话要点

**SemShareKV：通过Token级LSH匹配为语义相似Prompt高效共享KVCache**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `KV缓存共享` `局部敏感哈希` `大型语言模型` `推理加速` `语义相似性`

## 📋 核心要点

1. LLM推理时KV缓存占用大量内存，现有方法在语义相似但词汇不同的prompt上效果有限。
2. SemShareKV利用token嵌入的LSH匹配进行模糊token匹配，并结合RoPE保留位置信息，实现KV缓存共享。
3. 实验表明，SemShareKV在摘要任务上显著提升推理速度并降低内存占用，同时保证输出质量。

## 📝 摘要（中文）

随着大型语言模型（LLMs）规模的持续扩大，推理过程中键值（KV）缓存的内存占用已成为一个重要的瓶颈。现有方法主要集中在压缩单个prompt内的KV缓存，或重用跨prompt共享的前缀或频繁出现的文本片段。然而，这些策略在prompt语义相似但词汇不同的场景中受到限制，这种情况在多文档摘要和对话代理等任务中经常发生。我们提出了	extit{SemShareKV}，一个KV缓存共享和压缩框架，通过重用语义相似prompt中的KVCache来加速LLM推理。SemShareKV不依赖于精确的token匹配，而是使用局部敏感哈希（LSH）在token嵌入上应用模糊token匹配，并结合旋转位置嵌入（RoPE）以更好地保留位置信息。通过选择性地重用来自参考prompt缓存的相关键值对，SemShareKV减少了冗余计算，同时保持了输出质量。在不同的摘要数据集上的实验表明，在5k token输入的情况下，速度提高了6.25倍，GPU内存使用量降低了42％，而质量下降可忽略不计。这些结果突出了语义感知缓存共享在高效LLM推理方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型推理过程中，由于KV缓存占用大量内存而导致的效率瓶颈问题。现有方法主要依赖于精确的token匹配，无法有效利用语义相似但词汇不同的prompt之间的KV缓存，导致冗余计算和内存浪费。这种现象在多文档摘要、对话系统等场景中尤为突出。

**核心思路**：SemShareKV的核心思路是利用语义相似性来共享KV缓存。它不再依赖于精确的token匹配，而是通过模糊匹配的方式，识别语义上相似的token，并重用这些token对应的KV缓存。这样可以在减少冗余计算的同时，降低内存占用。

**技术框架**：SemShareKV框架主要包含以下几个阶段：1) **Token嵌入**：将输入prompt和参考prompt的token转换为嵌入向量。2) **LSH匹配**：使用局部敏感哈希（LSH）在token嵌入上进行模糊匹配，找到语义相似的token对。3) **RoPE编码**：结合旋转位置嵌入（RoPE）来更好地保留token的位置信息，提高匹配的准确性。4) **KV缓存重用**：根据LSH匹配的结果，选择性地重用参考prompt的KV缓存，减少冗余计算。5) **LLM推理**：使用重用后的KV缓存进行LLM推理，生成最终输出。

**关键创新**：SemShareKV的关键创新在于引入了基于token嵌入的模糊匹配机制，打破了传统方法对精确token匹配的依赖。通过LSH和RoPE的结合，SemShareKV能够更准确地识别语义相似的token，并有效地重用KV缓存。这种方法在语义相似但词汇不同的prompt上具有显著优势。

**关键设计**：SemShareKV的关键设计包括：1) **LSH哈希函数的选择**：选择合适的LSH哈希函数，以保证匹配的准确性和效率。2) **RoPE的参数设置**：调整RoPE的参数，以更好地保留位置信息。3) **KV缓存重用策略**：设计合理的KV缓存重用策略，避免引入噪声或降低输出质量。4) **相似度阈值**：设置合适的相似度阈值，控制匹配的严格程度。

## 📊 实验亮点

SemShareKV在多文档摘要数据集上取得了显著的性能提升。实验结果表明，在5k token输入的情况下，SemShareKV可以将推理速度提高6.25倍，同时将GPU内存使用量降低42％，而输出质量的下降可以忽略不计。这些结果表明，SemShareKV是一种高效且实用的LLM推理加速方法。

## 🎯 应用场景

SemShareKV具有广泛的应用前景，尤其适用于需要处理大量语义相似prompt的场景，例如多文档摘要、对话系统、代码生成等。通过降低内存占用和提高推理速度，SemShareKV可以显著提升LLM在这些领域的应用效率，并降低部署成本。未来，该技术有望进一步推广到其他LLM应用领域，推动LLM的普及和发展。

## 📄 摘要（原文）

> As large language models (LLMs) continue to scale, the memory footprint of key-value (KV) caches during inference has become a significant bottleneck. Existing approaches primarily focus on compressing KV caches within a single prompt or reusing shared prefixes or frequently ocurred text segments across prompts. However, such strategies are limited in scenarios where prompts are semantically similar but lexically different, which frequently occurs in tasks such as multi-document summarization and conversational agents. We propose \textit{SemShareKV}, a KV cache sharing and compression framework that accelerates LLM inference by reusing KVCache in semantically similar prompts. Instead of relying on exact token matches, SemShareKV applies fuzzy token matching using locality-sensitive hashing (LSH) on token embeddings and incorporates Rotary Position Embedding (RoPE) to better preserve positional information. By selectively reusing relevant key-value pairs from a reference prompt's cache, SemShareKV reduces redundant computation while maintaining output quality. Experiments on diverse summarization datasets show up to 6.25$\times$ speedup and 42\% lower GPU memory usage with 5k tokens input, with negligible quality degradation. These results highlight the potential of semantic-aware cache sharing for efficient LLM inference.

