---
layout: default
title: ROOT: Robust Orthogonalized Optimizer for Neural Network Training
---

# ROOT: Robust Orthogonalized Optimizer for Neural Network Training

**arXiv**: [2511.20626v1](https://arxiv.org/abs/2511.20626) | [PDF](https://arxiv.org/pdf/2511.20626.pdf)

**作者**: Wei He, Kai Han, Hang Zhou, Hanting Chen, Zhicheng Liu, Xinghao Chen, Yunhe Wang

---

## 💡 一句话要点

**提出ROOT优化器以解决大语言模型训练中的鲁棒性问题**

**关键词**: `优化器设计` `鲁棒训练` `大语言模型` `正交化方法` `近端优化`

## 📋 核心要点

1. 大模型训练对算法不精确和噪声敏感，导致不稳定
2. 采用维度鲁棒正交化和近端优化抑制噪声，提升稳定性
3. 实验显示在噪声和非凸场景下收敛更快、性能更优

## 📄 摘要（原文）

> The optimization of large language models (LLMs) remains a critical challenge, particularly as model scaling exacerbates sensitivity to algorithmic imprecision and training instability. Recent advances in optimizers have improved convergence efficiency through momentum orthogonalization, but suffer from two key robustness limitations: dimensional fragility in orthogonalization precision and vulnerability to outlier-induced noise. To address these robustness challenges, we introduce ROOT, a Robust Orthogonalized Optimizer that enhances training stability through dual robustness mechanisms. First, we develop a dimension-robust orthogonalization scheme using adaptive Newton iterations with fine-grained coefficients tailored to specific matrix sizes, ensuring consistent precision across diverse architectural configurations. Second, we introduce an optimization-robust framework via proximal optimization that suppresses outlier noise while preserving meaningful gradient directions. Extensive experiments demonstrate that ROOT achieves significantly improved robustness, with faster convergence and superior final performance compared to both Muon and Adam-based optimizers, particularly in noisy and non-convex scenarios. Our work establishes a new paradigm for developing robust and precise optimizers capable of handling the complexities of modern large-scale model training. The code will be available at https://github.com/huawei-noah/noah-research/tree/master/ROOT.

