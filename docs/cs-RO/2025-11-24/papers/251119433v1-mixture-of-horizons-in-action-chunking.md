---
layout: default
title: Mixture of Horizons in Action Chunking
---

# Mixture of Horizons in Action Chunking

**arXiv**: [2511.19433v1](https://arxiv.org/abs/2511.19433) | [PDF](https://arxiv.org/pdf/2511.19433.pdf)

**作者**: Dong Jing, Gang Wang, Jiaqi Liu, Weiliang Tang, Zelong Sun, Yunchao Yao, Zhenyu Wei, Yunhui Liu, Zhiwu Lu, Mingyu Ding

---

## 💡 一句话要点

**提出混合视野策略以解决机器人操作中动作块长度权衡问题**

**关键词**: `机器人操作` `动作块长度` `混合视野` `并行处理` `动态推理`

## 📋 核心要点

1. 核心问题：固定动作块长度在机器人操作中导致长期任务与精细控制间的权衡
2. 方法要点：将动作块分段并行处理，使用共享变换器和线性门融合输出
3. 实验或效果：在混合任务设置中达到99%平均成功率，提升吞吐量2.5倍

## 📄 摘要（原文）

> Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://github.com/Timsty1/MixtureOfHorizons

