---
layout: default
title: Less is More: Non-uniform Road Segments are Efficient for Bus Arrival Prediction
---

# Less is More: Non-uniform Road Segments are Efficient for Bus Arrival Prediction

**arXiv**: [2512.07200v1](https://arxiv.org/abs/2512.07200) | [PDF](https://arxiv.org/pdf/2512.07200.pdf)

**作者**: Zhen Huang, Jiaxin Deng, Jiayu Xu, Junbiao Pang, Haitao Yu

---

## 💡 一句话要点

**提出基于强化学习的非均匀路段分割方法以提升公交到站时间预测效率**

**关键词**: `公交到站时间预测` `非均匀路段分割` `强化学习` `线性预测模型` `道路网络优化`

## 📋 核心要点

1. 传统均匀路段分割忽略道路物理约束，限制预测效率
2. 方法分两阶段：强化学习提取非均匀路段，线性模型预测
3. 实验显示方法在效率和性能上优于传统方法，线性模型表现佳

## 📄 摘要（原文）

> In bus arrival time prediction, the process of organizing road infrastructure network data into homogeneous entities is known as segmentation. Segmenting a road network is widely recognized as the first and most critical step in developing an arrival time prediction system, particularly for auto-regressive-based approaches. Traditional methods typically employ a uniform segmentation strategy, which fails to account for varying physical constraints along roads, such as road conditions, intersections, and points of interest, thereby limiting prediction efficiency. In this paper, we propose a Reinforcement Learning (RL)-based approach to efficiently and adaptively learn non-uniform road segments for arrival time prediction. Our method decouples the prediction process into two stages: 1) Non-uniform road segments are extracted based on their impact scores using the proposed RL framework; and 2) A linear prediction model is applied to the selected segments to make predictions. This method ensures optimal segment selection while maintaining computational efficiency, offering a significant improvement over traditional uniform approaches. Furthermore, our experimental results suggest that the linear approach can even achieve better performance than more complex methods. Extensive experiments demonstrate the superiority of the proposed method, which not only enhances efficiency but also improves learning performance on large-scale benchmarks. The dataset and the code are publicly accessible at: https://github.com/pangjunbiao/Less-is-More.

