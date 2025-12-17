---
layout: default
title: Learning a Thousand Tasks in a Day
---

# Learning a Thousand Tasks in a Day

**arXiv**: [2511.10110v1](https://arxiv.org/abs/2511.10110) | [PDF](https://arxiv.org/pdf/2511.10110.pdf)

**作者**: Kamil Dreczkowski, Pietro Vitiello, Vitalis Vosylius, Edward Johns

---

## 💡 一句话要点

**提出MT3方法，通过分解和检索实现机器人从单演示学习千任务**

**关键词**: `模仿学习` `机器人操作` `轨迹分解` `检索泛化` `多任务学习` `数据效率`

## 📋 核心要点

1. 核心问题：机器人模仿学习需大量演示，数据效率低
2. 方法要点：将轨迹分解为对齐和交互阶段，结合检索泛化
3. 实验或效果：在少演示下数据效率提升十倍，24小时学千任务

## 📄 摘要（原文）

> Humans are remarkably efficient at learning tasks from demonstrations, but today's imitation learning methods for robot manipulation often require hundreds or thousands of demonstrations per task. We investigate two fundamental priors for improving learning efficiency: decomposing manipulation trajectories into sequential alignment and interaction phases, and retrieval-based generalisation. Through 3,450 real-world rollouts, we systematically study this decomposition. We compare different design choices for the alignment and interaction phases, and examine generalisation and scaling trends relative to today's dominant paradigm of behavioural cloning with a single-phase monolithic policy. In the few-demonstrations-per-task regime (<10 demonstrations), decomposition achieves an order of magnitude improvement in data efficiency over single-phase learning, with retrieval consistently outperforming behavioural cloning for both alignment and interaction. Building on these insights, we develop Multi-Task Trajectory Transfer (MT3), an imitation learning method based on decomposition and retrieval. MT3 learns everyday manipulation tasks from as little as a single demonstration each, whilst also generalising to novel object instances. This efficiency enables us to teach a robot 1,000 distinct everyday tasks in under 24 hours of human demonstrator time. Through 2,200 additional real-world rollouts, we reveal MT3's capabilities and limitations across different task families. Videos of our experiments can be found on at https://www.robot-learning.uk/learning-1000-tasks.

