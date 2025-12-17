---
layout: default
title: M-STAR: Multi-Scale Spatiotemporal Autoregression for Human Mobility Modeling
---

# M-STAR: Multi-Scale Spatiotemporal Autoregression for Human Mobility Modeling

**arXiv**: [2512.07314v1](https://arxiv.org/abs/2512.07314) | [PDF](https://arxiv.org/pdf/2512.07314.pdf)

**作者**: Yuxiao Luo, Songming Zhang, Sijie Ruan, Siran Chen, Kang Liu, Yang Xu, Yu Zheng, Ling Yin

---

## 💡 一句话要点

**提出M-STAR框架，通过多尺度时空自回归解决长时轨迹生成效率与建模不足问题。**

**关键词**: `人类移动建模` `多尺度时空预测` `自回归生成` `轨迹生成` `Transformer解码器`

## 📋 核心要点

1. 核心问题：现有方法在长时轨迹生成中效率低且缺乏显式多尺度时空建模。
2. 方法要点：结合多尺度时空分词器与Transformer解码器，实现从粗到细的自回归预测。
3. 实验或效果：在真实数据集上优于现有方法，提升生成速度与保真度。

## 📄 摘要（原文）

> Modeling human mobility is vital for extensive applications such as transportation planning and epidemic modeling. With the rise of the Artificial Intelligence Generated Content (AIGC) paradigm, recent works explore synthetic trajectory generation using autoregressive and diffusion models. While these methods show promise for generating single-day trajectories, they remain limited by inefficiencies in long-term generation (e.g., weekly trajectories) and a lack of explicit spatiotemporal multi-scale modeling. This study proposes Multi-Scale Spatio-Temporal AutoRegression (M-STAR), a new framework that generates long-term trajectories through a coarse-to-fine spatiotemporal prediction process. M-STAR combines a Multi-scale Spatiotemporal Tokenizer that encodes hierarchical mobility patterns with a Transformer-based decoder for next-scale autoregressive prediction. Experiments on two real-world datasets show that M-STAR outperforms existing methods in fidelity and significantly improves generation speed. The data and codes are available at https://github.com/YuxiaoLuo0013/M-STAR.

