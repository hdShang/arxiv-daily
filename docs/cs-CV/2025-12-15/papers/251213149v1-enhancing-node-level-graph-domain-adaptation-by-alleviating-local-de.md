---
layout: default
title: Enhancing Node-Level Graph Domain Adaptation by Alleviating Local Dependency
---

# Enhancing Node-Level Graph Domain Adaptation by Alleviating Local Dependency

**arXiv**: [2512.13149v1](https://arxiv.org/abs/2512.13149) | [PDF](https://arxiv.org/pdf/2512.13149.pdf)

**作者**: Xinwei Tai, Dongmian Zou, Hongfei Wang

---

## 💡 一句话要点

**提出通过解相关节点特征以缓解局部依赖，提升无监督图域适应性能**

**关键词**: `图域适应` `节点特征解相关` `条件偏移` `图神经网络` `无监督学习` `图Transformer`

## 📋 核心要点

1. 核心问题：无监督图域适应中，节点特征的局部依赖导致条件偏移，阻碍知识迁移。
2. 方法要点：理论分析表明条件偏移源于局部依赖，提出解相关GCN层和图Transformer层来消除依赖。
3. 实验或效果：实验显示方法优于基线，学习到的表示具有小的类内距离，代码已开源。

## 📄 摘要（原文）

> Recent years have witnessed significant advancements in machine learning methods on graphs. However, transferring knowledge effectively from one graph to another remains a critical challenge. This highlights the need for algorithms capable of applying information extracted from a source graph to an unlabeled target graph, a task known as unsupervised graph domain adaptation (GDA). One key difficulty in unsupervised GDA is conditional shift, which hinders transferability. In this paper, we show that conditional shift can be observed only if there exists local dependencies among node features. To support this claim, we perform a rigorous analysis and also further provide generalization bounds of GDA when dependent node features are modeled using markov chains. Guided by the theoretical findings, we propose to improve GDA by decorrelating node features, which can be specifically implemented through decorrelated GCN layers and graph transformer layers. Our experimental results demonstrate the effectiveness of this approach, showing not only substantial performance enhancements over baseline GDA methods but also clear visualizations of small intra-class distances in the learned representations. Our code is available at https://github.com/TechnologyAiGroup/DFT

