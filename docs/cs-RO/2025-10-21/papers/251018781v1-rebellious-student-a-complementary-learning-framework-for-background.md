---
layout: default
title: Rebellious Student: A Complementary Learning Framework for Background Feature Enhancement in Hyperspectral Anomaly Detection
---

# Rebellious Student: A Complementary Learning Framework for Background Feature Enhancement in Hyperspectral Anomaly Detection

**arXiv**: [2510.18781v1](https://arxiv.org/abs/2510.18781) | [PDF](https://arxiv.org/pdf/2510.18781.pdf)

**作者**: Wenping Jin, Yuyang Tang, Li Zhu, Fei Guo

---

## 💡 一句话要点

**提出叛逆学生框架以增强高光谱异常检测中的背景特征**

**关键词**: `高光谱异常检测` `互补学习` `叛逆学生框架` `特征增强` `背景建模`

## 📋 核心要点

1. 核心问题：高光谱异常检测中背景特征集成不足，影响通用部署效率。
2. 方法要点：采用叛逆学生范式，训练空间分支与光谱教师分支互补学习。
3. 实验效果：在HAD100基准上显著提升检测性能，计算开销低。

## 📄 摘要（原文）

> A recent class of hyperspectral anomaly detection methods that can be trained
> once on background datasets and then universally deployed -- without per-scene
> retraining or parameter tuning -- has demonstrated remarkable efficiency and
> robustness. Building upon this paradigm, we focus on the integration of
> spectral and spatial cues and introduce a novel "Rebellious Student" framework
> for complementary feature learning. Unlike conventional teacher-student
> paradigms driven by imitation, our method intentionally trains the spatial
> branch to diverge from the spectral teacher, thereby learning complementary
> spatial patterns that the teacher fails to capture. A two-stage learning
> strategy is adopted: (1) a spectral enhancement network is first trained via
> reverse distillation to obtain robust background spectral representations; and
> (2) a spatial network -- the rebellious student -- is subsequently optimized
> using decorrelation losses that enforce feature orthogonality while maintaining
> reconstruction fidelity to avoid irrelevant noise. Once trained, the framework
> enhances both spectral and spatial background features, enabling parameter-free
> and training-free anomaly detection when paired with conventional detectors.
> Extensive experiments on the HAD100 benchmark show substantial improvements
> over several established baselines with minimal computational overhead,
> confirming the effectiveness and generality of the proposed complementary
> learning paradigm. Our code is publicly available at
> https://github.com/xjpp2016/FERS.

