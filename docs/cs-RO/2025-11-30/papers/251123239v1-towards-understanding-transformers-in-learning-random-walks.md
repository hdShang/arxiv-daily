---
layout: default
title: Towards Understanding Transformers in Learning Random Walks
---

# Towards Understanding Transformers in Learning Random Walks

**arXiv**: [2511.23239v1](https://arxiv.org/abs/2511.23239) | [PDF](https://arxiv.org/pdf/2511.23239.pdf)

**作者**: Wei Shi, Yuan Cao

---

## 💡 一句话要点

**理论分析单层Transformer学习圆上随机游走的能力与可解释性**

**关键词**: `Transformer理论` `随机游走` `可解释性` `梯度下降` `注意力机制` `序列预测`

## 📋 核心要点

1. 研究Transformer在经典统计模型（圆上随机游走）中的理论能力与可解释性
2. 证明单层Transformer经梯度下降训练可达到最优预测精度，注意力机制作为令牌选择器聚焦父状态
3. 实验验证理论发现，揭示小初始化梯度下降在简单任务中可能失败

## 📄 摘要（原文）

> Transformers have proven highly effective across various applications, especially in handling sequential data such as natural languages and time series. However, transformer models often lack clear interpretability, and the success of transformers has not been well understood in theory. In this paper, we study the capability and interpretability of transformers in learning a family of classic statistical models, namely random walks on circles. We theoretically demonstrate that, after training with gradient descent, a one-layer transformer model can achieve optimal accuracy in predicting random walks. Importantly, our analysis reveals that the trained model is interpretable: the trained softmax attention serves as a token selector, focusing on the direct parent state; subsequently, the value matrix executes a one-step probability transition to predict the location of the next state based on this parent state. We also show that certain edge cases not covered by our theory are indeed failure cases, demonstrating that our theoretical conditions are tight. By investigating these success and failure cases, it is revealed that gradient descent with small initialization may fail or struggle to converge to a good solution in certain simple tasks even beyond random walks. Experiments are conducted to support our theoretical findings.

