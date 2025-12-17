---
layout: default
title: $\mathcal{V}isi\mathcal{P}runer$: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs
---

# $\mathcal{V}isi\mathcal{P}runer$: Decoding Discontinuous Cross-Modal Dynamics for Efficient Multimodal LLMs

**arXiv**: [2510.17205v1](https://arxiv.org/abs/2510.17205) | [PDF](https://arxiv.org/pdf/2510.17205.pdf)

**作者**: Yingqi Fan, Anhao Zhao, Jinlan Fu, Junlong Tong, Hui Su, Yijie Pan, Wei Zhang, Xiaoyu Shen

---

## 💡 一句话要点

**提出VisiPruner以高效减少多模态大语言模型的计算开销**

**关键词**: `多模态大语言模型` `令牌剪枝` `跨模态交互` `计算效率` `注意力机制` `模型优化`

## 📋 核心要点

1. 多模态大语言模型计算开销大，源于注意力计算随多模态令牌数二次增长
2. 基于三阶段跨模态交互分析，设计无需训练的剪枝框架，移除冗余视觉令牌
3. 在LLaVA-v1.5 7B上减少99%视觉相关注意力计算和53.9% FLOPs，优于现有方法

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved strong performance
> across vision-language tasks, but suffer from significant computational
> overhead due to the quadratic growth of attention computations with the number
> of multimodal tokens. Though efforts have been made to prune tokens in MLLMs,
> \textit{they lack a fundamental understanding of how MLLMs process and fuse
> multimodal information.} Through systematic analysis, we uncover a
> \textbf{three-stage} cross-modal interaction process: (1) Shallow layers
> recognize task intent, with visual tokens acting as passive attention sinks;
> (2) Cross-modal fusion occurs abruptly in middle layers, driven by a few
> critical visual tokens; (3) Deep layers discard vision tokens, focusing solely
> on linguistic refinement. Based on these findings, we propose
> \emph{VisiPruner}, a training-free pruning framework that reduces up to 99\% of
> vision-related attention computations and 53.9\% of FLOPs on LLaVA-v1.5 7B. It
> significantly outperforms existing token pruning methods and generalizes across
> diverse MLLMs. Beyond pruning, our insights further provide actionable
> guidelines for training efficient MLLMs by aligning model architecture with its
> intrinsic layer-wise processing dynamics. Our code is available at:
> https://github.com/EIT-NLP/VisiPruner.

