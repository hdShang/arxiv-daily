---
layout: default
title: FGC-Comp: Adaptive Neighbor-Grouped Attribute Completion for Graph-based Anomaly Detection
---

# FGC-Comp: Adaptive Neighbor-Grouped Attribute Completion for Graph-based Anomaly Detection

**arXiv**: [2512.02705v1](https://arxiv.org/abs/2512.02705) | [PDF](https://arxiv.org/pdf/2512.02705.pdf)

**作者**: Junpeng Wu, Pinheng Zong

---

## 💡 一句话要点

**提出FGC-Comp自适应邻居分组属性补全模块，以增强图异常检测中缺失属性下的邻域聚合稳定性。**

**关键词**: `图异常检测` `属性补全` `邻域聚合` `自适应分组` `轻量级模块`

## 📋 核心要点

1. 核心问题：图异常检测中节点属性缺失或被对抗性遮蔽，影响邻域聚合稳定性和预测可靠性。
2. 方法要点：将邻居按标签分组，应用组特定变换，通过节点条件门处理未知组，残差连接融合消息，端到端训练。
3. 实验或效果：在两个真实欺诈数据集上验证有效性，计算开销可忽略。

## 📄 摘要（原文）

> Graph-based Anomaly Detection models have gained widespread adoption in recent years, identifying suspicious nodes by aggregating neighborhood information. However, most existing studies overlook the pervasive issues of missing and adversarially obscured node attributes, which can undermine aggregation stability and prediction reliability. To mitigate this, we propose FGC-Comp, a lightweight, classifier-agnostic, and deployment-friendly attribute completion module-designed to enhance neighborhood aggregation under incomplete attributes. We partition each node's neighbors into three label-based groups, apply group-specific transforms to the labeled groups while a node-conditioned gate handles unknowns, fuse messages via residual connections, and train end-to-end with a binary classification objective to improve aggregation stability and prediction reliability under missing attributes. Experiments on two real-world fraud datasets validate the effectiveness of the approach with negligible computational overhead.

