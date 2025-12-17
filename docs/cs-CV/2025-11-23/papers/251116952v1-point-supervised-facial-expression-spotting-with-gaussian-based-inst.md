---
layout: default
title: Point-Supervised Facial Expression Spotting with Gaussian-Based Instance-Adaptive Intensity Modeling
---

# Point-Supervised Facial Expression Spotting with Gaussian-Based Instance-Adaptive Intensity Modeling

**arXiv**: [2511.16952v1](https://arxiv.org/abs/2511.16952) | [PDF](https://arxiv.org/pdf/2511.16952.pdf)

**作者**: Yicheng Deng, Hideaki Hayashi, Hajime Nagahara

---

## 💡 一句话要点

**提出基于高斯实例自适应强度建模的点监督框架以解决面部表情定位问题**

**关键词**: `面部表情定位` `点监督学习` `高斯强度建模` `软伪标签` `宏微表情分类`

## 📋 核心要点

1. 核心问题：点监督面部表情定位依赖单时间戳标注，避免昂贵边界标注。
2. 方法要点：使用高斯建模软伪标签优化强度分支，结合分类分支区分宏微表情。
3. 实验或效果：在SAMM-LV等数据集验证有效性，提升定位和分类性能。

## 📄 摘要（原文）

> Automatic facial expression spotting, which aims to identify facial expression instances in untrimmed videos, is crucial for facial expression analysis. Existing methods primarily focus on fully-supervised learning and rely on costly, time-consuming temporal boundary annotations. In this paper, we investigate point-supervised facial expression spotting (P-FES), where only a single timestamp annotation per instance is required for training. We propose a unique two-branch framework for P-FES. First, to mitigate the limitation of hard pseudo-labeling, which often confuses neutral and expression frames with various intensities, we propose a Gaussian-based instance-adaptive intensity modeling (GIM) module to model instance-level expression intensity distribution for soft pseudo-labeling. By detecting the pseudo-apex frame around each point label, estimating the duration, and constructing an instance-level Gaussian distribution, GIM assigns soft pseudo-labels to expression frames for more reliable intensity supervision. The GIM module is incorporated into our framework to optimize the class-agnostic expression intensity branch. Second, we design a class-aware apex classification branch that distinguishes macro- and micro-expressions solely based on their pseudo-apex frames. During inference, the two branches work independently: the class-agnostic expression intensity branch generates expression proposals, while the class-aware apex-classification branch is responsible for macro- and micro-expression classification.Furthermore, we introduce an intensity-aware contrastive loss to enhance discriminative feature learning and suppress neutral noise by contrasting neutral frames with expression frames with various intensities. Extensive experiments on the SAMM-LV, CAS(ME)$^2$, and CAS(ME)$^3$ datasets demonstrate the effectiveness of our proposed framework.

