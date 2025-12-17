---
layout: default
title: RadioFlow: Efficient Radio Map Construction Framework with Flow Matching
---

# RadioFlow: Efficient Radio Map Construction Framework with Flow Matching

**arXiv**: [2510.09314v1](https://arxiv.org/abs/2510.09314) | [PDF](https://arxiv.org/pdf/2510.09314.pdf)

**作者**: Haozhe Jia, Wenshuo Chen, Xiucheng Wang, Nan Cheng, Hongbo Zhang, Kuimou Yu, Songning Lai, Nanjian Jia, Bowen Tian, Hongru Xiao, Yutao Yue

---

## 💡 一句话要点

**提出RadioFlow框架，通过流匹配实现高效无线电地图构建，用于6G网络**

**关键词**: `无线电地图生成` `流匹配` `高效采样` `6G网络` `生成模型` `推理加速`

## 📋 核心要点

1. 扩散模型在无线电地图生成中模型大、推理慢，阻碍实际部署
2. 采用流匹配学习噪声到数据的连续轨迹，实现单步高效采样
3. 实验显示参数减少8倍、推理加速4倍，保持高重建精度

## 📄 摘要（原文）

> Accurate and real-time radio map (RM) generation is crucial for
> next-generation wireless systems, yet diffusion-based approaches often suffer
> from large model sizes, slow iterative denoising, and high inference latency,
> which hinder practical deployment. To overcome these limitations, we propose
> \textbf{RadioFlow}, a novel flow-matching-based generative framework that
> achieves high-fidelity RM generation through single-step efficient sampling.
> Unlike conventional diffusion models, RadioFlow learns continuous transport
> trajectories between noise and data, enabling both training and inference to be
> significantly accelerated while preserving reconstruction accuracy.
> Comprehensive experiments demonstrate that RadioFlow achieves state-of-the-art
> performance with \textbf{up to 8$\times$ fewer parameters} and \textbf{over
> 4$\times$ faster inference} compared to the leading diffusion-based baseline
> (RadioDiff). This advancement provides a promising pathway toward scalable,
> energy-efficient, and real-time electromagnetic digital twins for future 6G
> networks. We release the code at
> \href{https://github.com/Hxxxz0/RadioFlow}{GitHub}.

