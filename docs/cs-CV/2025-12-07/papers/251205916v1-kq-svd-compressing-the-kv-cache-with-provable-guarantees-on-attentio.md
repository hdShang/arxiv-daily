---
layout: default
title: KQ-SVD: Compressing the KV Cache with Provable Guarantees on Attention Fidelity
---

# KQ-SVD: Compressing the KV Cache with Provable Guarantees on Attention Fidelity

**arXiv**: [2512.05916v1](https://arxiv.org/abs/2512.05916) | [PDF](https://arxiv.org/pdf/2512.05916.pdf)

**作者**: Damien Lesens, Beheshteh T. Rakhshan, Guillaume Rabusseau

---

## 💡 一句话要点

**提出KQ-SVD方法，通过最优低秩分解压缩KV缓存以提升注意力保真度**

**关键词**: `KV缓存压缩` `注意力矩阵分解` `低秩近似` `大语言模型推理` `内存优化`

## 📋 核心要点

1. KV缓存是LLM推理效率的关键，但随序列长度和批量增长成为内存瓶颈
2. 现有压缩方法仅压缩键或联合嵌入查询与键，未直接针对注意力矩阵进行优化
3. KQ-SVD通过闭式解直接分解注意力矩阵，在LLaMA和Mistral模型上验证了更高的投影质量

## 📄 摘要（原文）

> The Key-Value (KV) cache is central to the efficiency of transformer-based large language models (LLMs), storing previously computed vectors to accelerate inference. Yet, as sequence length and batch size grow, the cache becomes a major memory bottleneck. Prior compression methods typically apply low-rank decomposition to keys alone or attempt to jointly embed queries and keys, but both approaches neglect that attention fundamentally depends on their inner products. In this work, we prove that such strategies are suboptimal for approximating the attention matrix. We introduce KQ-SVD, a simple and computationally efficient method that directly performs an optimal low-rank decomposition of the attention matrix via a closed-form solution. By targeting the true source of redundancy, KQ-SVD preserves attention outputs with higher fidelity under compression. Extensive evaluations on LLaMA and Mistral models demonstrate that our approach consistently delivers superior projection quality.

