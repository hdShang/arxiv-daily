---
layout: default
title: Personalized Federated Segmentation with Shared Feature Aggregation and Boundary-Focused Calibration
---

# Personalized Federated Segmentation with Shared Feature Aggregation and Boundary-Focused Calibration

**arXiv**: [2511.18847v1](https://arxiv.org/abs/2511.18847) | [PDF](https://arxiv.org/pdf/2511.18847.pdf)

**作者**: Ishmam Tashdeed, Md. Atiqur Rahman, Sabrina Islam, Md. Azam Hossain

---

## 💡 一句话要点

**提出FedOAP方法，利用共享特征聚合和边界聚焦校准解决非IID数据下的个性化联邦分割问题。**

**关键词**: `个性化联邦学习` `医学图像分割` `特征聚合` `边界损失` `非IID数据` `肿瘤分割`

## 📋 核心要点

1. 核心问题：现有方法忽略跨客户端共享特征，难以处理非IID数据异质性。
2. 方法要点：采用解耦交叉注意力聚合共享特征，并引入扰动边界损失提升分割一致性。
3. 实验或效果：在多器官肿瘤分割任务中，FedOAP优于现有联邦和个性化分割方法。

## 📄 摘要（原文）

> Personalized federated learning (PFL) possesses the unique capability of preserving data confidentiality among clients while tackling the data heterogeneity problem of non-independent and identically distributed (Non-IID) data. Its advantages have led to widespread adoption in domains such as medical image segmentation. However, the existing approaches mostly overlook the potential benefits of leveraging shared features across clients, where each client contains segmentation data of different organs. In this work, we introduce a novel personalized federated approach for organ agnostic tumor segmentation (FedOAP), that utilizes cross-attention to model long-range dependencies among the shared features of different clients and a boundary-aware loss to improve segmentation consistency. FedOAP employs a decoupled cross-attention (DCA), which enables each client to retain local queries while attending to globally shared key-value pairs aggregated from all clients, thereby capturing long-range inter-organ feature dependencies. Additionally, we introduce perturbed boundary loss (PBL) which focuses on the inconsistencies of the predicted mask's boundary for each client, forcing the model to localize the margins more precisely. We evaluate FedOAP on diverse tumor segmentation tasks spanning different organs. Extensive experiments demonstrate that FedOAP consistently outperforms existing state-of-the-art federated and personalized segmentation methods.

