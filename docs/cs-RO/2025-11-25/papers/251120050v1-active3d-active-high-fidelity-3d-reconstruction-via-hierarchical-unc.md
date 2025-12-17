---
layout: default
title: Active3D: Active High-Fidelity 3D Reconstruction via Hierarchical Uncertainty Quantification
---

# Active3D: Active High-Fidelity 3D Reconstruction via Hierarchical Uncertainty Quantification

**arXiv**: [2511.20050v1](https://arxiv.org/abs/2511.20050) | [PDF](https://arxiv.org/pdf/2511.20050.pdf)

**作者**: Yan Li, Yingzhao Li, Gim Hee Lee

---

## 💡 一句话要点

**提出主动探索框架以解决高保真3D重建问题**

**关键词**: `主动3D重建` `不确定性量化` `混合表示` `下一最佳视角规划` `机器人感知`

## 📋 核心要点

1. 核心问题：如何在主动探索中高效重建高保真3D场景
2. 方法要点：融合隐式-显式表示和分层不确定性量化
3. 实验效果：在基准测试中实现高精度、完整性和渲染质量

## 📄 摘要（原文）

> In this paper, we present an active exploration framework for high-fidelity 3D reconstruction that incrementally builds a multi-level uncertainty space and selects next-best-views through an uncertainty-driven motion planner. We introduce a hybrid implicit-explicit representation that fuses neural fields with Gaussian primitives to jointly capture global structural priors and locally observed details. Based on this hybrid state, we derive a hierarchical uncertainty volume that quantifies both implicit global structure quality and explicit local surface confidence. To focus optimization on the most informative regions, we propose an uncertainty-driven keyframe selection strategy that anchors high-entropy viewpoints as sparse attention nodes, coupled with a viewpoint-space sliding window for uncertainty-aware local refinement. The planning module formulates next-best-view selection as an Expected Hybrid Information Gain problem and incorporates a risk-sensitive path planner to ensure efficient and safe exploration. Extensive experiments on challenging benchmarks demonstrate that our approach consistently achieves state-of-the-art accuracy, completeness, and rendering quality, highlighting its effectiveness for real-world active reconstruction and robotic perception tasks.

