---
layout: default
title: Experts-Guided Unbalanced Optimal Transport for ISP Learning from Unpaired and/or Paired Data
---

# Experts-Guided Unbalanced Optimal Transport for ISP Learning from Unpaired and/or Paired Data

**arXiv**: [2512.05635v1](https://arxiv.org/abs/2512.05635) | [PDF](https://arxiv.org/pdf/2512.05635.pdf)

**作者**: Georgy Perevozchikov, Nancy Mehta, Egor Ershov, Radu Timofte

---

## 💡 一句话要点

**提出专家引导的不平衡最优传输框架，以解决ISP学习中对配对数据依赖的瓶颈问题。**

**关键词**: `图像信号处理学习` `不平衡最优传输` `无配对训练` `专家判别器` `跨域翻译` `鲁棒性优化`

## 📋 核心要点

1. 核心问题：ISP学习依赖大规模配对数据，获取成本高，是性能瓶颈。
2. 方法要点：基于不平衡最优传输，结合专家判别器委员会，实现无配对或配对训练。
3. 实验或效果：在配对模式下超越原方法，无配对模式性能媲美甚至超越配对训练。

## 📄 摘要（原文）

> Learned Image Signal Processing (ISP) pipelines offer powerful end-to-end performance but are critically dependent on large-scale paired raw-to-sRGB datasets. This reliance on costly-to-acquire paired data remains a significant bottleneck. To address this challenge, we introduce a novel, unsupervised training framework based on Optimal Transport capable of training arbitrary ISP architectures in both unpaired and paired modes. We are the first to successfully apply Unbalanced Optimal Transport (UOT) for this complex, cross-domain translation task. Our UOT-based framework provides robustness to outliers in the target sRGB data, allowing it to discount atypical samples that would be prohibitively costly to map. A key component of our framework is a novel ``committee of expert discriminators,'' a hybrid adversarial regularizer. This committee guides the optimal transport mapping by providing specialized, targeted gradients to correct specific ISP failure modes, including color fidelity, structural artifacts, and frequency-domain realism. To demonstrate the superiority of our approach, we retrained existing state-of-the-art ISP architectures using our paired and unpaired setups. Our experiments show that while our framework, when trained in paired mode, exceeds the performance of the original paired methods across all metrics, our unpaired mode concurrently achieves quantitative and qualitative performance that rivals, and in some cases surpasses, the original paired-trained counterparts. The code and pre-trained models are available at: https://github.com/gosha20777/EGUOT-ISP.git.

