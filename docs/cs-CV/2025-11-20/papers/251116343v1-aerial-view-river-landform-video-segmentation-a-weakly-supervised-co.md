---
layout: default
title: Aerial View River Landform Video segmentation: A Weakly Supervised Context-aware Temporal Consistency Distillation Approach
---

# Aerial View River Landform Video segmentation: A Weakly Supervised Context-aware Temporal Consistency Distillation Approach

**arXiv**: [2511.16343v1](https://arxiv.org/abs/2511.16343) | [PDF](https://arxiv.org/pdf/2511.16343.pdf)

**作者**: Chi-Han Chen, Chieh-Ming Chen, Wen-Huang Cheng, Ching-Chun Huang

---

## 💡 一句话要点

**提出弱监督上下文感知时序一致性蒸馏方法以解决无人机河流地貌视频分割问题**

**关键词**: `无人机遥感` `弱监督学习` `时序一致性` `知识蒸馏` `视频分割` `地貌分类`

## 📋 核心要点

1. 核心问题：无人机遥感中数据标注复杂、时序一致性差及数据稀缺限制地貌分类
2. 方法要点：采用师生架构结合关键帧选择与更新算法，实现弱监督学习和时序知识蒸馏
3. 实验或效果：仅用30%标注数据，同时提升mIoU和时序一致性，稳定定位地形对象

## 📄 摘要（原文）

> The study of terrain and landform classification through UAV remote sensing diverges significantly from ground vehicle patrol tasks. Besides grappling with the complexity of data annotation and ensuring temporal consistency, it also confronts the scarcity of relevant data and the limitations imposed by the effective range of many technologies. This research substantiates that, in aerial positioning tasks, both the mean Intersection over Union (mIoU) and temporal consistency (TC) metrics are of paramount importance. It is demonstrated that fully labeled data is not the optimal choice, as selecting only key data lacks the enhancement in TC, leading to failures. Hence, a teacher-student architecture, coupled with key frame selection and key frame updating algorithms, is proposed. This framework successfully performs weakly supervised learning and TC knowledge distillation, overcoming the deficiencies of traditional TC training in aerial tasks. The experimental results reveal that our method utilizing merely 30\% of labeled data, concurrently elevates mIoU and temporal consistency ensuring stable localization of terrain objects. Result demo : https://gitlab.com/prophet.ai.inc/drone-based-riverbed-inspection

