---
layout: default
title: REWA: Witness-Overlap Theory -- Foundations for Composable Binary Similarity Systems
---

# REWA: Witness-Overlap Theory -- Foundations for Composable Binary Similarity Systems

**arXiv**: [2511.19998v1](https://arxiv.org/abs/2511.19998) | [PDF](https://arxiv.org/pdf/2511.19998.pdf)

**作者**: Nikit Phadke

---

## 💡 一句话要点

**提出基于见证重叠结构的相似性理论，实现可组合二进制相似性系统**

**关键词**: `相似性理论` `见证重叠结构` `二进制编码` `可组合系统` `排名保留` `对数复杂度`

## 📋 核心要点

1. 核心问题：相似性定义多样，缺乏统一理论支持高效编码与排名保留
2. 方法要点：通过见证集、半随机位分配和重叠单调性，实现对数位编码
3. 实验或效果：理论证明在重叠间隙条件下，top-k 排名保留，编码复杂度为 O(log(\|V\|/δ))

## 📄 摘要（原文）

> REWA introduces a general theory of similarity based on witness-overlap structures. We show that whenever similarity between concepts can be expressed as monotone witness overlap -- whether arising from graph neighborhoods, causal relations, temporal structure, topological features, symbolic patterns, or embedding-based neighborhoods -- it admits a reduction to compact encodings with provable ranking preservation guarantees. REWA systems consist of: (1) finite witness sets $W(v)$, (2) semi-random bit assignments generated from each witness, and (3) monotonicity of expected similarity in the overlap $Δ(u, v) = \|W(u) \cap W(v)\|$. We prove that under an overlap-gap condition on the final witness sets -- independent of how they were constructed -- top-$k$ rankings are preserved using $m = O(\log(\|V\|/δ))$ bits. The witness-set formulation is compositional: any sequence of structural, temporal, causal, topological, information-theoretic, or learned transformations can be combined into pipelines that terminate in discrete witness sets. The theory applies to the final witness overlap, enabling modular construction of similarity systems from reusable primitives. This yields a vast design space: millions of composable similarity definitions inherit logarithmic encoding complexity. REWA subsumes and unifies Bloom filters, minhash, LSH bitmaps, random projections, sketches, and hierarchical filters as special cases. It provides a principled foundation for similarity systems whose behavior is governed by witness overlap rather than hash-function engineering. This manuscript presents the axioms, the main reducibility theorem, complete proofs with explicit constants, and a detailed discussion of compositional design, limitations, and future extensions including multi-bit encodings, weighted witnesses, and non-set representations.

