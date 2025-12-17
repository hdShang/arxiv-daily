---
layout: default
title: Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition
---

# Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition

**arXiv**: [2512.11545v1](https://arxiv.org/abs/2512.11545) | [PDF](https://arxiv.org/pdf/2512.11545.pdf)

**作者**: Sheng Feng, Shuqing Ma, Xiaoqian Zhu

---

## 💡 一句话要点

**提出UATR-GTransformer，结合Transformer与图神经网络，用于水下声学目标识别。**

**关键词**: `水下声学目标识别` `图神经网络` `Transformer` `梅尔频谱图` `非欧氏深度学习`

## 📋 核心要点

1. 核心问题：水下声学信号非平稳、非线性，传统欧氏空间假设不适用。
2. 方法要点：将梅尔频谱图分块，用Transformer编码器生成图嵌入，再经GNN增强特征。
3. 实验或效果：在两个基准数据集上性能达到先进水平，可解释性分析显示有效提取频域信息。

## 📄 摘要（原文）

> Underwater acoustic target recognition (UATR) is extremely challenging due to the complexity of ship-radiated noise and the variability of ocean environments. Although deep learning (DL) approaches have achieved promising results, most existing models implicitly assume that underwater acoustic data lie in a Euclidean space. This assumption, however, is unsuitable for the inherently complex topology of underwater acoustic signals, which exhibit non-stationary, non-Gaussian, and nonlinear characteristics. To overcome this limitation, this paper proposes the UATR-GTransformer, a non-Euclidean DL model that integrates Transformer architectures with graph neural networks (GNNs). The model comprises three key components: a Mel patchify block, a GTransformer block, and a classification head. The Mel patchify block partitions the Mel-spectrogram into overlapping patches, while the GTransformer block employs a Transformer Encoder to capture mutual information between split patches to generate Mel-graph embeddings. Subsequently, a GNN enhances these embeddings by modeling local neighborhood relationships, and a feed-forward network (FFN) further performs feature transformation. Experiments results based on two widely used benchmark datasets demonstrate that the UATR-GTransformer achieves performance competitive with state-of-the-art methods. In addition, interpretability analysis reveals that the proposed model effectively extracts rich frequency-domain information, highlighting its potential for applications in ocean engineering.

