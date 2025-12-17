---
layout: default
title: Transform Trained Transformer: Accelerating Naive 4K Video Generation Over 10$\times$
---

# Transform Trained Transformer: Accelerating Naive 4K Video Generation Over 10$\times$

**arXiv**: [2512.13492v1](https://arxiv.org/abs/2512.13492) | [PDF](https://arxiv.org/pdf/2512.13492.pdf)

**作者**: Jiangning Zhang, Junwei Zhu, Teng Hu, Yabiao Wang, Donghao Luo, Weijian Cao, Zhenye Gan, Xiaobin Hu, Zhucun Xue, Chengjie Wang

---

## 💡 一句话要点

**提出T3-Video方法，通过优化前向逻辑加速原生4K视频生成超10倍。**

**关键词**: `视频生成` `Transformer优化` `4K分辨率` `注意力机制` `计算加速`

## 📋 核心要点

1. 核心问题：原生4K视频生成面临全注意力计算爆炸，效率与质量难以平衡。
2. 方法要点：引入多尺度权重共享窗口注意力，结合分层分块和轴保持全注意力设计，无需改变预训练模型架构。
3. 实验或效果：在4K-VBench上性能提升（VQA +4.29，VTC +0.08），加速超10倍。

## 📄 摘要（原文）

> Native 4K (2160$\times$3840) video generation remains a critical challenge due to the quadratic computational explosion of full-attention as spatiotemporal resolution increases, making it difficult for models to strike a balance between efficiency and quality. This paper proposes a novel Transformer retrofit strategy termed $\textbf{T3}$ ($\textbf{T}$ransform $\textbf{T}$rained $\textbf{T}$ransformer) that, without altering the core architecture of full-attention pretrained models, significantly reduces compute requirements by optimizing their forward logic. Specifically, $\textbf{T3-Video}$ introduces a multi-scale weight-sharing window attention mechanism and, via hierarchical blocking together with an axis-preserving full-attention design, can effect an "attention pattern" transformation of a pretrained model using only modest compute and data. Results on 4K-VBench show that $\textbf{T3-Video}$ substantially outperforms existing approaches: while delivering performance improvements (+4.29$\uparrow$ VQA and +0.08$\uparrow$ VTC), it accelerates native 4K video generation by more than 10$\times$. Project page at https://zhangzjn.github.io/projects/T3-Video

