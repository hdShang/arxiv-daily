---
layout: default
title: Uncertainty-Aware Dual-Student Knowledge Distillation for Efficient Image Classification
---

# Uncertainty-Aware Dual-Student Knowledge Distillation for Efficient Image Classification

**arXiv**: [2511.18826v1](https://arxiv.org/abs/2511.18826) | [PDF](https://arxiv.org/pdf/2511.18826.pdf)

**作者**: Aakash Gore, Anoushka Dey, Aryan Mishra

---

## 💡 一句话要点

**提出不确定性感知双学生知识蒸馏框架以提升图像分类效率**

**关键词**: `知识蒸馏` `不确定性感知` `双学生架构` `图像分类` `模型压缩`

## 📋 核心要点

1. 传统知识蒸馏方法忽视教师预测不确定性，影响学生模型学习效果
2. 引入双学生架构，通过不确定性感知和同伴学习机制优化知识传递
3. 在ImageNet-100上验证，ResNet-18和MobileNetV2准确率分别提升2.04%和0.92%

## 📄 摘要（原文）

> Knowledge distillation has emerged as a powerful technique for model compression, enabling the transfer of knowledge from large teacher networks to compact student models. However, traditional knowledge distillation methods treat all teacher predictions equally, regardless of the teacher's confidence in those predictions. This paper proposes an uncertainty-aware dual-student knowledge distillation framework that leverages teacher prediction uncertainty to selectively guide student learning. We introduce a peer-learning mechanism where two heterogeneous student architectures, specifically ResNet-18 and MobileNetV2, learn collaboratively from both the teacher network and each other. Experimental results on ImageNet-100 demonstrate that our approach achieves superior performance compared to baseline knowledge distillation methods, with ResNet-18 achieving 83.84\% top-1 accuracy and MobileNetV2 achieving 81.46\% top-1 accuracy, representing improvements of 2.04\% and 0.92\% respectively over traditional single-student distillation approaches.

