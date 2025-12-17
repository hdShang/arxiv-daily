---
layout: default
title: Bayesian Topological Convolutional Neural Nets
---

# Bayesian Topological Convolutional Neural Nets

**arXiv**: [2510.11704v1](https://arxiv.org/abs/2510.11704) | [PDF](https://arxiv.org/pdf/2510.11704.pdf)

**作者**: Sarah Harkins Dayton, Hayden Everett, Ioannis Schizas, David L. Boothe Jr., Vasileios Maroulas

---

## 💡 一句话要点

**提出贝叶斯拓扑卷积神经网络以解决图像分类中数据不足和不确定性量化问题**

**关键词**: `贝叶斯神经网络` `拓扑卷积网络` `不确定性量化` `图像分类` `数据效率`

## 📋 核心要点

1. 核心问题：传统CNN需要大量数据训练、预测过度自信且缺乏不确定性量化能力
2. 方法要点：结合拓扑感知学习和贝叶斯采样，通过先验分布和一致性条件优化网络参数
3. 实验或效果：在基准数据集上优于传统CNN、BNN和拓扑CNN，尤其在数据有限或损坏时表现优越

## 📄 摘要（原文）

> Convolutional neural networks (CNNs) have been established as the main
> workhorse in image data processing; nonetheless, they require large amounts of
> data to train, often produce overconfident predictions, and frequently lack the
> ability to quantify the uncertainty of their predictions. To address these
> concerns, we propose a new Bayesian topological CNN that promotes a novel
> interplay between topology-aware learning and Bayesian sampling. Specifically,
> it utilizes information from important manifolds to accelerate training while
> reducing calibration error by placing prior distributions on network parameters
> and properly learning appropriate posteriors. One important contribution of our
> work is the inclusion of a consistency condition in the learning cost, which
> can effectively modify the prior distributions to improve the performance of
> our novel network architecture. We evaluate the model on benchmark image
> classification datasets and demonstrate its superiority over conventional CNNs,
> Bayesian neural networks (BNNs), and topological CNNs. In particular, we supply
> evidence that our method provides an advantage in situations where training
> data is limited or corrupted. Furthermore, we show that the new model allows
> for better uncertainty quantification than standard BNNs since it can more
> readily identify examples of out-of-distribution data on which it has not been
> trained. Our results highlight the potential of our novel hybrid approach for
> more efficient and robust image classification.

