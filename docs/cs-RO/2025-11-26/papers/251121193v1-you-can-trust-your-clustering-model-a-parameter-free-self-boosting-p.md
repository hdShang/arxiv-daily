---
layout: default
title: You Can Trust Your Clustering Model: A Parameter-free Self-Boosting Plug-in for Deep Clustering
---

# You Can Trust Your Clustering Model: A Parameter-free Self-Boosting Plug-in for Deep Clustering

**arXiv**: [2511.21193v1](https://arxiv.org/abs/2511.21193) | [PDF](https://arxiv.org/pdf/2511.21193.pdf)

**作者**: Hanyang Li, Yuheng Jia, Hui Liu, Junhui Hou

---

## 💡 一句话要点

**提出DCBoost插件以解决深度聚类中全局与局部特征结构不一致问题**

**关键词**: `深度聚类` `特征结构优化` `参数免费插件` `自监督学习` `判别损失`

## 📋 核心要点

1. 核心问题：深度聚类模型全局特征边界模糊，局部特征紧凑但分离性差
2. 方法要点：基于自适应k近邻筛选高置信样本，计算判别损失优化网络
3. 实验或效果：提升现有模型性能超3%，轮廓系数放大7倍以上

## 📄 摘要（原文）

> Recent deep clustering models have produced impressive clustering performance. However, a common issue with existing methods is the disparity between global and local feature structures. While local structures typically show strong consistency and compactness within class samples, global features often present intertwined boundaries and poorly separated clusters. Motivated by this observation, we propose DCBoost, a parameter-free plug-in designed to enhance the global feature structures of current deep clustering models. By harnessing reliable local structural cues, our method aims to elevate clustering performance effectively. Specifically, we first identify high-confidence samples through adaptive $k$-nearest neighbors-based consistency filtering, aiming to select a sufficient number of samples with high label reliability to serve as trustworthy anchors for self-supervision. Subsequently, these samples are utilized to compute a discriminative loss, which promotes both intra-class compactness and inter-class separability, to guide network optimization. Extensive experiments across various benchmark datasets showcase that our DCBoost significantly improves the clustering performance of diverse existing deep clustering models. Notably, our method improves the performance of current state-of-the-art baselines (e.g., ProPos) by more than 3% and amplifies the silhouette coefficient by over $7\times$. Code is available at <https://github.com/l-h-y168/DCBoost>.

