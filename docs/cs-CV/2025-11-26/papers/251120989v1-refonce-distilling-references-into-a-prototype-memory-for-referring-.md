---
layout: default
title: RefOnce: Distilling References into a Prototype Memory for Referring Camouflaged Object Detection
---

# RefOnce: Distilling References into a Prototype Memory for Referring Camouflaged Object Detection

**arXiv**: [2511.20989v1](https://arxiv.org/abs/2511.20989) | [PDF](https://arxiv.org/pdf/2511.20989.pdf)

**作者**: Yu-Huan Wu, Zi-Xuan Zhu, Yan Wang, Liangli Zhen, Deng-Ping Fan

---

## 💡 一句话要点

**提出RefOnce框架，通过蒸馏参考图像到原型内存，实现无测试时参考的伪装目标检测。**

**关键词**: `伪装目标检测` `原型蒸馏` `参考图像` `双向注意力对齐` `无测试参考` `类别原型内存`

## 📋 核心要点

1. 核心问题：现有Ref-COD系统需测试时参考图像，导致部署困难和延迟。
2. 方法要点：训练时蒸馏参考到类别原型，推理时通过查询条件混合生成参考向量。
3. 实验效果：在R2C7K基准上表现竞争或优于最新方法，代码已开源。

## 📄 摘要（原文）

> Referring Camouflaged Object Detection (Ref-COD) segments specified camouflaged objects in a scene by leveraging a small set of referring images. Though effective, current systems adopt a dual-branch design that requires reference images at test time, which limits deployability and adds latency and data-collection burden. We introduce a Ref-COD framework that distills references into a class-prototype memory during training and synthesizes a reference vector at inference via a query-conditioned mixture of prototypes. Concretely, we maintain an EMA-updated prototype per category and predict mixture weights from the query to produce a guidance vector without any test-time references. To bridge the representation gap between reference statistics and camouflaged query features, we propose a bidirectional attention alignment module that adapts both the query features and the class representation. Thus, our approach yields a simple, efficient path to Ref-COD without mandatory references. We evaluate the proposed method on the large-scale R2C7K benchmark. Extensive experiments demonstrate competitive or superior performance of the proposed method compared with recent state-of-the-arts. Code is available at https://github.com/yuhuan-wu/RefOnce.

