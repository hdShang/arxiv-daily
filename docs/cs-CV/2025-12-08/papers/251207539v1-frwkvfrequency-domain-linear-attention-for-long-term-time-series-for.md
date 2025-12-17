---
layout: default
title: FRWKV:Frequency-Domain Linear Attention for Long-Term Time Series Forecasting
---

# FRWKV:Frequency-Domain Linear Attention for Long-Term Time Series Forecasting

**arXiv**: [2512.07539v1](https://arxiv.org/abs/2512.07539) | [PDF](https://arxiv.org/pdf/2512.07539.pdf)

**作者**: Qingyuan Yang, Shizhuo, Dongyue Chen, Da Teng, Zehua Gan

---

## 💡 一句话要点

**提出FRWKV，结合频域分析与线性注意力，解决长序列时间序列预测中的计算复杂度和频域信息利用问题。**

**关键词**: `长序列时间序列预测` `线性注意力` `频域分析` `计算复杂度优化` `时间序列建模`

## 📋 核心要点

1. 传统Transformer在长序列预测中面临二次计算复杂度和频域信息利用不足的瓶颈。
2. FRWKV集成线性注意力与频域分析，实现线性计算复杂度并增强时间特征表示。
3. 在八个真实数据集上取得平均排名第一，消融研究验证了线性注意力和频域编码器的重要性。

## 📄 摘要（原文）

> Traditional Transformers face a major bottleneck in long-sequence time series forecasting due to their quadratic complexity $(\mathcal{O}(T^2))$ and their limited ability to effectively exploit frequency-domain information. Inspired by RWKV's $\mathcal{O}(T)$ linear attention and frequency-domain modeling, we propose FRWKV, a frequency-domain linear-attention framework that overcomes these limitations. Our model integrates linear attention mechanisms with frequency-domain analysis, achieving $\mathcal{O}(T)$ computational complexity in the attention path while exploiting spectral information to enhance temporal feature representations for scalable long-sequence modeling. Across eight real-world datasets, FRWKV achieves a first-place average rank. Our ablation studies confirm the critical roles of both the linear attention and frequency-encoder components. This work demonstrates the powerful synergy between linear attention and frequency analysis, establishing a new paradigm for scalable time series modeling. Code is available at this repository: https://github.com/yangqingyuan-byte/FRWKV.

