---
layout: default
title: AVGGT: Rethinking Global Attention for Accelerating VGGT
---

# AVGGT: Rethinking Global Attention for Accelerating VGGT

**arXiv**: [2512.02541v1](https://arxiv.org/abs/2512.02541) | [PDF](https://arxiv.org/pdf/2512.02541.pdf)

**作者**: Xianbing Sun, Zhikai Zhu, Zhengyu Lou, Bo Yang, Jinyang Tang, Liqing Zhang, He Wang, Jianfu Zhang

---

## 💡 一句话要点

**提出AVGGT训练无关加速方案，通过分析全局注意力角色并针对性优化，显著提升VGGT/π³推理速度**

**关键词**: `多视图三维重建` `注意力机制优化` `推理加速` `全局注意力分析` `训练无关加速`

## 📋 核心要点

1. 分析VGGT/π³全局注意力机制，发现早期层无有效对应、中间层负责跨视图对齐、后期层仅微调
2. 提出两步加速策略：早期层转为帧注意力，中间层通过令牌子采样保留对角线并补充均值
3. 在标准基准测试中实现8-10倍推理加速，精度持平或略升，在密集多视图场景保持鲁棒

## 📄 摘要（原文）

> Since DUSt3R, models such as VGGT and $π^3$ have shown strong multi-view 3D performance, but their heavy reliance on global self-attention results in high computational cost. Existing sparse-attention variants offer partial speedups, yet lack a systematic analysis of how global attention contributes to multi-view reasoning. In this paper, we first conduct an in-depth investigation of the global attention modules in VGGT and $π^3$ to better understand their roles. Our analysis reveals a clear division of roles in the alternating global-frame architecture: early global layers do not form meaningful correspondences, middle layers perform cross-view alignment, and last layers provide only minor refinements. Guided by these findings, we propose a training-free two-step acceleration scheme: (1) converting early global layers into frame attention, and (2) subsampling global attention by subsampling K/V over patch tokens with diagonal preservation and a mean-fill component. We instantiate this strategy on VGGT and $π^3$ and evaluate across standard pose and point-map benchmarks. Our method achieves up to $8$-$10\times$ speedup in inference time while matching or slightly improving the accuracy of the original models, and remains robust even in extremely dense multi-view settings where prior sparse-attention baselines fail.

