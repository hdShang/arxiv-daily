---
layout: default
title: MiMo-Embodied: X-Embodied Foundation Model Technical Report
---

# MiMo-Embodied: X-Embodied Foundation Model Technical Report

**arXiv**: [2511.16518v1](https://arxiv.org/abs/2511.16518) | [PDF](https://arxiv.org/pdf/2511.16518.pdf)

**作者**: Xiaoshuai Hao, Lei Zhou, Zhijian Huang, Zhiwen Hou, Yingbo Tang, Lingfeng Zhang, Guang Li, Zheng Lu, Shuhuai Ren, Xianhui Meng, Yuchen Zhang, Jing Wu, Jinghui Lu, Chenxu Dang, Jiayi Guan, Jianhua Wu, Zhiyi Hou, Hanbing Li, Shumeng Xia, Mingliang Zhou, Yinan Zheng, Zihao Yue, Shuhao Gu, Hao Tian, Yuannan Shen, Jianwei Cui, Wen Zhang, Shaoqing Xu, Bing Wang, Haiyang Sun, Zeyu Zhu, Yuncheng Jiang, Zibin Guo, Chuhong Gong, Chaofan Zhang, Wenbo Ding, Kun Ma, Guang Chen, Rui Cai, Diyun Xiang, Heng Qu, Fuli Luo, Hangjun Ye, Long Chen

---

## 💡 一句话要点

**提出MiMo-Embodied跨具身基础模型，在自动驾驶与具身AI中实现最优性能**

**关键词**: `跨具身基础模型` `自动驾驶` `具身AI` `多任务学习` `基准测试` `正向迁移`

## 📋 核心要点

1. 核心问题：未知，但模型整合自动驾驶与具身AI，解决多任务性能挑战
2. 方法要点：采用多阶段学习、数据构建和CoT/RL微调，促进领域间正向迁移
3. 实验或效果：在29个基准测试中创纪录，显著超越开源、闭源及专用基线

## 📄 摘要（原文）

> We open-source MiMo-Embodied, the first cross-embodied foundation model to successfully integrate and achieve state-of-the-art performance in both Autonomous Driving and Embodied AI. MiMo-Embodied sets new records across 17 embodied AI benchmarks in Task Planning, Affordance Prediction and Spatial Understanding, while also excelling in 12 autonomous driving benchmarks across Environmental Perception, Status Prediction, and Driving Planning. Across these tasks, MiMo-Embodied significantly outperforms existing open-source, closed-source, and specialized baselines. Our results indicate that through multi-stage learning, curated data construction, and CoT/RL fine-tuning, these two domains exhibit strong positive transfer and mutually reinforce one another. We provide a detailed analysis of our model design and training methodologies to facilitate further research. Code and models are available at https://github.com/XiaomiMiMo/MiMo-Embodied.

