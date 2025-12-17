---
layout: default
title: Multivariate Time Series Forecasting with Hybrid Euclidean-SPD Manifold Graph Neural Networks
---

# Multivariate Time Series Forecasting with Hybrid Euclidean-SPD Manifold Graph Neural Networks

**arXiv**: [2512.14023v1](https://arxiv.org/abs/2512.14023) | [PDF](https://arxiv.org/pdf/2512.14023.pdf)

**作者**: Yong Fang, Na Li, Hangguan Shan, Eryun Liu, Xinyu Li, Wei Ni, Er-Ping Li

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出混合欧几里得-对称正定流形图神经网络以解决多元时间序列预测中几何结构建模不足的问题。**

**关键词**: `多元时间序列预测` `图神经网络` `混合几何表示` `对称正定流形` `时空依赖性建模` `自适应距离库` `融合图卷积网络` `预测准确性提升`

## 📋 核心要点

1. 现有方法在欧几里得或黎曼空间中建模多元时间序列，难以捕捉真实数据中的多样几何结构和复杂时空依赖性。
2. 提出HSMGNN模型，通过混合几何表示和子流形交叉段嵌入，在双空间中捕捉时空变化，并设计自适应距离库层降低计算成本。
3. 在三个基准数据集上，HSMGNN相比最先进基线在预测准确性上提升高达13.8%，验证了其有效性。

## 📝 摘要（中文）

多元时间序列预测在交通管理和预测性维护等实际应用中至关重要。现有方法通常在欧几里得空间或黎曼空间中建模MTS数据，限制了其捕捉真实数据中多样几何结构和复杂时空依赖性的能力。为克服这一限制，我们提出了混合对称正定流形图神经网络，这是一种基于图神经网络的新模型，在混合欧几里得-黎曼框架内捕捉数据几何。据我们所知，这是首次利用混合几何表示进行MTS预测的工作，实现了对几何属性的表达性和全面建模。具体来说，我们引入了子流形交叉段嵌入，将输入MTS投影到欧几里得和黎曼空间，从而捕捉不同几何域中的时空变化。为减轻黎曼距离的高计算成本，我们进一步设计了具有可训练记忆机制的自适应距离库层。最后，开发了融合图卷积网络，通过可学习融合算子整合双空间特征以进行准确预测。在三个基准数据集上的实验表明，HSMGNN在预测准确性上比最先进基线提高了高达13.8%。

## 🔬 方法详解

HSMGNN的整体框架基于混合欧几里得-黎曼空间，通过图神经网络建模多元时间序列。关键技术创新包括：子流形交叉段嵌入将数据投影到欧几里得和黎曼空间以捕捉几何多样性；自适应距离库层利用可训练记忆机制优化黎曼距离计算，降低计算复杂度；融合图卷积网络通过可学习算子整合双空间特征进行预测。与现有方法的主要区别在于首次引入混合几何表示，克服了单一空间建模的局限性，实现了更全面的几何属性捕捉。

## 📊 实验亮点

在三个基准数据集上的实验显示，HSMGNN相比最先进基线在预测准确性上最高提升13.8%，显著优于现有方法，证明了混合几何表示的有效性。

## 🎯 应用场景

该研究可应用于交通管理、预测性维护等领域，通过准确预测多元时间序列，优化资源分配和故障预警，提升系统效率和可靠性。

## 📄 摘要（原文）

> Multivariate Time Series (MTS) forecasting plays a vital role in various real-world applications, such as traffic management and predictive maintenance. Existing approaches typically model MTS data in either Euclidean or Riemannian space, limiting their ability to capture the diverse geometric structures and complex spatio-temporal dependencies inherent in real-world data. To overcome this limitation, we propose the Hybrid Symmetric Positive-Definite Manifold Graph Neural Network (HSMGNN), a novel graph neural network-based model that captures data geometry within a hybrid Euclidean-Riemannian framework. To the best of our knowledge, this is the first work to leverage hybrid geometric representations for MTS forecasting, enabling expressive and comprehensive modeling of geometric properties. Specifically, we introduce a Submanifold-Cross-Segment (SCS) embedding to project input MTS into both Euclidean and Riemannian spaces, thereby capturing spatio-temporal variations across distinct geometric domains. To alleviate the high computational cost of Riemannian distance, we further design an Adaptive-Distance-Bank (ADB) layer with a trainable memory mechanism. Finally, a Fusion Graph Convolutional Network (FGCN) is devised to integrate features from the dual spaces via a learnable fusion operator for accurate prediction. Experiments on three benchmark datasets demonstrate that HSMGNN achieves up to a 13.8 percent improvement over state-of-the-art baselines in forecasting accuracy.

