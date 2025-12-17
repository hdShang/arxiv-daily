---
layout: default
title: Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models
---

# Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models

**arXiv**: [2510.20707v1](https://arxiv.org/abs/2510.20707) | [PDF](https://arxiv.org/pdf/2510.20707.pdf)

**作者**: Xuyang Liu, Xiyan Gui, Yuchao Zhang, Linfeng Zhang

---

## 💡 一句话要点

**提出MixKV方法以优化大型视觉语言模型中的KV缓存压缩问题**

**关键词**: `KV缓存压缩` `大型视觉语言模型` `多模态冗余` `重要性多样性平衡` `头级自适应` `内存优化`

## 📋 核心要点

1. 核心问题：KV缓存扩展导致内存瓶颈，现有方法忽略多模态语义冗余模式
2. 方法要点：结合重要性和多样性，自适应头级语义冗余进行KV对压缩
3. 实验或效果：在极端压缩下提升基准方法5.1%，GUI任务增益达8.0-9.0%

## 📄 摘要（原文）

> Recent large vision-language models (LVLMs) demonstrate remarkable
> capabilities in processing extended multi-modal sequences, yet the resulting
> key-value (KV) cache expansion creates a critical memory bottleneck that
> fundamentally limits deployment scalability. While existing KV cache
> compression methods focus on retaining high-importance KV pairs to minimize
> storage, they often overlook the modality-specific semantic redundancy patterns
> that emerge distinctively in multi-modal KV caches. In this work, we first
> analyze how, beyond simple importance, the KV cache in LVLMs exhibits varying
> levels of redundancy across attention heads. We show that relying solely on
> importance can only cover a subset of the full KV cache information
> distribution, leading to potential loss of semantic coverage. To address this,
> we propose \texttt{MixKV}, a novel method that mixes importance with diversity
> for optimized KV cache compression in LVLMs. \texttt{MixKV} adapts to head-wise
> semantic redundancy, selectively balancing diversity and importance when
> compressing KV pairs. Extensive experiments demonstrate that \texttt{MixKV}
> consistently enhances existing methods across multiple LVLMs. Under extreme
> compression (budget=64), \texttt{MixKV} improves baseline methods by an average
> of \textbf{5.1\%} across five multi-modal understanding benchmarks and achieves
> remarkable gains of \textbf{8.0\%} and \textbf{9.0\%} for SnapKV and AdaKV on
> GUI grounding tasks, all while maintaining comparable inference efficiency.
> Furthermore, \texttt{MixKV} extends seamlessly to LLMs with comparable
> performance gains. Our code is available at
> \href{https://github.com/xuyang-liu16/MixKV}{\textcolor{citeblue}{https://github.com/xuyang-liu16/MixKV}}.

