---
layout: default
title: Energy-Efficient Vision Transformer Inference for Edge-AI Deployment
---

# Energy-Efficient Vision Transformer Inference for Edge-AI Deployment

**arXiv**: [2511.23166v1](https://arxiv.org/abs/2511.23166) | [PDF](https://arxiv.org/pdf/2511.23166.pdf)

**作者**: Nursultan Amanzhol, Jurn-Gyu Park

---

## 💡 一句话要点

**提出两阶段评估方法以优化边缘AI部署中视觉Transformer的能效。**

**关键词**: `视觉Transformer` `能效评估` `边缘AI部署` `NetScore` `Sustainable Accuracy Metric` `混合模型`

## 📋 核心要点

1. 核心问题：边缘设备部署视觉Transformer需超越准确率的能效评估。
2. 方法要点：结合设备无关模型筛选与设备相关测量进行两阶段评估。
3. 实验或效果：在NVIDIA Jetson TX2和RTX 3050上测试，混合模型和蒸馏模型分别显著降低能耗。

## 📄 摘要（原文）

> The growing deployment of Vision Transformers (ViTs) on energy-constrained devices requires evaluation methods that go beyond accuracy alone. We present a two-stage pipeline for assessing ViT energy efficiency that combines device-agnostic model selection with device-related measurements. We benchmark 13 ViT models on ImageNet-1K and CIFAR-10, running inference on NVIDIA Jetson TX2 (edge device) and an NVIDIA RTX 3050 (mobile GPU). The device-agnostic stage uses the NetScore metric for screening; the device-related stage ranks models with the Sustainable Accuracy Metric (SAM). Results show that hybrid models such as LeViT_Conv_192 reduce energy by up to 53% on TX2 relative to a ViT baseline (e.g., SAM5=1.44 on TX2/CIFAR-10), while distilled models such as TinyViT-11M_Distilled excel on the mobile GPU (e.g., SAM5=1.72 on RTX 3050/CIFAR-10 and SAM5=0.76 on RTX 3050/ImageNet-1K).

