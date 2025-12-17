---
layout: default
title: The Directed Prediction Change - Efficient and Trustworthy Fidelity Assessment for Local Feature Attribution Methods
---

# The Directed Prediction Change - Efficient and Trustworthy Fidelity Assessment for Local Feature Attribution Methods

**arXiv**: [2511.21363v1](https://arxiv.org/abs/2511.21363) | [PDF](https://arxiv.org/pdf/2511.21363.pdf)

**作者**: Kevin Iselborn, David Dembinsky, Adriano Lucieri, Andreas Dengel

---

## 💡 一句话要点

**提出定向预测变化以高效可信评估局部特征归因方法的保真度**

**关键词**: `局部特征归因` `保真度评估` `定向预测变化` `可解释人工智能` `高效计算`

## 📋 核心要点

1. 现有保真度指标依赖蒙特卡洛近似，计算成本高且引入随机性
2. 通过结合扰动和归因方向改进预测变化指标，实现确定性评估
3. 在皮肤病变和金融数据上验证，速度提升近十倍，结果可重现

## 📄 摘要（原文）

> The utility of an explanation method critically depends on its fidelity to the underlying machine learning model. Especially in high-stakes medical settings, clinicians and regulators require explanations that faithfully reflect the model's decision process. Existing fidelity metrics such as Infidelity rely on Monte Carlo approximation, which demands numerous model evaluations and introduces uncertainty due to random sampling. This work proposes a novel metric for evaluating the fidelity of local feature attribution methods by modifying the existing Prediction Change (PC) metric within the Guided Perturbation Experiment. By incorporating the direction of both perturbation and attribution, the proposed Directed Prediction Change (DPC) metric achieves an almost tenfold speedup and eliminates randomness, resulting in a deterministic and trustworthy evaluation procedure that measures the same property as local Infidelity. DPC is evaluated on two datasets (skin lesion images and financial tabular data), two black-box models, seven explanation algorithms, and a wide range of hyperparameters. Across $4\,744$ distinct explanations, the results demonstrate that DPC, together with PC, enables a holistic and computationally efficient evaluation of both baseline-oriented and local feature attribution methods, while providing deterministic and reproducible outcomes.

