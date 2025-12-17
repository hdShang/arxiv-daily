---
layout: default
title: Learning-Augmented Online Bipartite Matching in the Random Arrival Order Model
---

# Learning-Augmented Online Bipartite Matching in the Random Arrival Order Model

**arXiv**: [2511.23388v1](https://arxiv.org/abs/2511.23388) | [PDF](https://arxiv.org/pdf/2511.23388.pdf)

**作者**: Kunanon Burathep, Thomas Erlebach, William K. Moses

---

## 💡 一句话要点

**提出学习增强在线二分图匹配算法，在随机到达顺序模型中实现高一致性和鲁棒性。**

**关键词**: `在线二分图匹配` `学习增强算法` `随机到达顺序模型` `一致性鲁棒性分析` `预测误差平滑性`

## 📋 核心要点

1. 研究在线无权重二分图匹配问题，在随机到达顺序模型中结合不可信预测。
2. 扩展先前工作，移除最优匹配大小的假设，仅要求预测匹配大小至少为αn。
3. 算法达到(1-o(1))一致性和(β-o(1))鲁棒性，竞争比随预测误差平滑下降。

## 📄 摘要（原文）

> We study the online unweighted bipartite matching problem in the random arrival order model, with $n$ offline and $n$ online vertices, in the learning-augmented setting: The algorithm is provided with untrusted predictions of the types (neighborhoods) of the online vertices. We build upon the work of Choo et al. (ICML 2024, pp. 8762-8781) who proposed an approach that uses a prefix of the arrival sequence as a sample to determine whether the predictions are close to the true arrival sequence and then either follows the predictions or uses a known baseline algorithm that ignores the predictions and is $β$-competitive. Their analysis is limited to the case that the optimal matching has size $n$, i.e., every online vertex can be matched. We generalize their approach and analysis by removing any assumptions on the size of the optimal matching while only requiring that the size of the predicted matching is at least $αn$ for any constant $0 < α\le 1$. Our learning-augmented algorithm achieves $(1-o(1))$-consistency and $(β-o(1))$-robustness. Additionally, we show that the competitive ratio degrades smoothly between consistency and robustness with increasing prediction error.

