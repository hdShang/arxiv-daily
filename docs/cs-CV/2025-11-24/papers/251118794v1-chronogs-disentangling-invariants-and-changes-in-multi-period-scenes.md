---
layout: default
title: ChronoGS: Disentangling Invariants and Changes in Multi-Period Scenes
---

# ChronoGS: Disentangling Invariants and Changes in Multi-Period Scenes

**arXiv**: [2511.18794v1](https://arxiv.org/abs/2511.18794) | [PDF](https://arxiv.org/pdf/2511.18794.pdf)

**作者**: Zhongtao Wang, Jiaqi Dai, Qingtian Zhu, Yilong Li, Mai Su, Fei Zhu, Meng Gai, Shaorong Wang, Chengwei Pan, Yisong Chen, Guoping Wang

---

## 💡 一句话要点

**提出ChronoGS以解决多时期场景重建中几何与外观变化的问题**

**关键词**: `多时期场景重建` `时间调制高斯表示` `几何外观解耦` `ChronoScene数据集` `时间一致性`

## 📋 核心要点

1. 核心问题：多时期图像集合中几何和外观演化，现有方法在长期不连续变化下失效
2. 方法要点：使用时间调制高斯表示，在统一锚架中重建所有时期并解耦稳定与演化组件
3. 实验或效果：在ChronoScene数据集上，重建质量和时间一致性优于基线

## 📄 摘要（原文）

> Multi-period image collections are common in real-world applications. Cities are re-scanned for mapping, construction sites are revisited for progress tracking, and natural regions are monitored for environmental change. Such data form multi-period scenes, where geometry and appearance evolve. Reconstructing such scenes is an important yet underexplored problem. Existing pipelines rely on incompatible assumptions: static and in-the-wild methods enforce a single geometry, while dynamic ones assume smooth motion, both failing under long-term, discontinuous changes. To solve this problem, we introduce ChronoGS, a temporally modulated Gaussian representation that reconstructs all periods within a unified anchor scaffold. It's also designed to disentangle stable and evolving components, achieving temporally consistent reconstruction of multi-period scenes. To catalyze relevant research, we release ChronoScene dataset, a benchmark of real and synthetic multi-period scenes, capturing geometric and appearance variation. Experiments demonstrate that ChronoGS consistently outperforms baselines in reconstruction quality and temporal consistency. Our code and the ChronoScene dataset are publicly available at https://github.com/ZhongtaoWang/ChronoGS.

