---
layout: default
title: Disentangling Progress in Medical Image Registration: Beyond Trend-Driven Architectures towards Domain-Specific Strategies
---

# Disentangling Progress in Medical Image Registration: Beyond Trend-Driven Architectures towards Domain-Specific Strategies

**arXiv**: [2512.01913v1](https://arxiv.org/abs/2512.01913) | [PDF](https://arxiv.org/pdf/2512.01913.pdf)

**作者**: Bailiang Jian, Jiazhen Pan, Rohit Jena, Morteza Ghahremani, Hongwei Bran Li, Daniel Rueckert, Christian Wachinger, Benedikt Wiestler

---

## 💡 一句话要点

**通过模块化框架揭示医学图像配准中领域特定设计优于通用架构趋势**

**关键词**: `医学图像配准` `模块化框架` `领域特定设计` `趋势驱动架构` `可扩展基准`

## 📋 核心要点

1. 核心问题：医学图像配准中通用计算模块与领域特定设计的贡献不明确，需明确未来研究方向
2. 方法要点：采用模块化框架系统分离低层趋势驱动模块和高层配准特定设计的影响
3. 实验或效果：领域特定设计显著提升配准性能，平均相对改进约3%，优于趋势驱动模块

## 📄 摘要（原文）

> Medical image registration drives quantitative analysis across organs, modalities, and patient populations. Recent deep learning methods often combine low-level "trend-driven" computational blocks from computer vision, such as large-kernel CNNs, Transformers, and state-space models, with high-level registration-specific designs like motion pyramids, correlation layers, and iterative refinement. Yet, their relative contributions remain unclear and entangled. This raises a central question: should future advances in registration focus on importing generic architectural trends or on refining domain-specific design principles? Through a modular framework spanning brain, lung, cardiac, and abdominal registration, we systematically disentangle the influence of these two paradigms. Our evaluation reveals that low-level "trend-driven" computational blocks offer only marginal or inconsistent gains, while high-level registration-specific designs consistently deliver more accurate, smoother, and more robust deformations. These domain priors significantly elevate the performance of a standard U-Net baseline, far more than variants incorporating "trend-driven" blocks, achieving an average relative improvement of $\sim3\%$. All models and experiments are released within a transparent, modular benchmark that enables plug-and-play comparison for new architectures and registration tasks (https://github.com/BailiangJ/rethink-reg). This dynamic and extensible platform establishes a common ground for reproducible and fair evaluation, inviting the community to isolate genuine methodological contributions from domain priors. Our findings advocate a shift in research emphasis: from following architectural trends to embracing domain-specific design principles as the true drivers of progress in learning-based medical image registration.

