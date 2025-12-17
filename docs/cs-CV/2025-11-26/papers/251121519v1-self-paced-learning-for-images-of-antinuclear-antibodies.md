---
layout: default
title: Self-Paced Learning for Images of Antinuclear Antibodies
---

# Self-Paced Learning for Images of Antinuclear Antibodies

**arXiv**: [2511.21519v1](https://arxiv.org/abs/2511.21519) | [PDF](https://arxiv.org/pdf/2511.21519.pdf)

**作者**: Yiyang Jiang, Guangwu Qian, Jiaxin Wu, Qi Huang, Qing Li, Yongkang Wu, Xiao-Yong Wei

---

## 💡 一句话要点

**提出自步学习框架以解决抗核抗体图像多实例多标签检测问题**

**关键词**: `抗核抗体检测` `多实例多标签学习` `自步学习` `医学图像分析` `端到端优化`

## 📋 核心要点

1. 核心问题：抗核抗体检测涉及多实例多标签学习，图像复杂且需处理多种荧光模式组合
2. 方法要点：使用实例采样器、伪标签分发器和自步学习系数，实现端到端优化
3. 实验或效果：在ANA数据集上F1-Macro提升7.0%，mAP提升12.6%，公开数据集排名前列

## 📄 摘要（原文）

> Antinuclear antibody (ANA) testing is a crucial method for diagnosing autoimmune disorders, including lupus, Sjögren's syndrome, and scleroderma. Despite its importance, manual ANA detection is slow, labor-intensive, and demands years of training. ANA detection is complicated by over 100 coexisting antibody types, resulting in vast fluorescent pattern combinations. Although machine learning and deep learning have enabled automation, ANA detection in real-world clinical settings presents unique challenges as it involves multi-instance, multi-label (MIML) learning. In this paper, a novel framework for ANA detection is proposed that handles the complexities of MIML tasks using unaltered microscope images without manual preprocessing. Inspired by human labeling logic, it identifies consistent ANA sub-regions and assigns aggregated labels accordingly. These steps are implemented using three task-specific components: an instance sampler, a probabilistic pseudo-label dispatcher, and self-paced weight learning rate coefficients. The instance sampler suppresses low-confidence instances by modeling pattern confidence, while the dispatcher adaptively assigns labels based on instance distinguishability. Self-paced learning adjusts training according to empirical label observations. Our framework overcomes limitations of traditional MIML methods and supports end-to-end optimization. Extensive experiments on one ANA dataset and three public medical MIML benchmarks demonstrate the superiority of our framework. On the ANA dataset, our model achieves up to +7.0% F1-Macro and +12.6% mAP gains over the best prior method, setting new state-of-the-art results. It also ranks top-2 across all key metrics on public datasets, reducing Hamming loss and one-error by up to 18.2% and 26.9%, respectively. The source code can be accessed at https://github.com/fletcherjiang/ANA-SelfPacedLearning.

