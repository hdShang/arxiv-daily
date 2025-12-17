---
layout: default
title: Heterogeneous Complementary Distillation
---

# Heterogeneous Complementary Distillation

**arXiv**: [2511.10942v1](https://arxiv.org/abs/2511.10942) | [PDF](https://arxiv.org/pdf/2511.10942.pdf)

**作者**: Liuchi Xu, Hao Zheng, Lu Wang, Lisheng Xu, Jun Cheng

---

## 💡 一句话要点

**提出异构互补蒸馏以解决异构架构知识蒸馏中的特征表示差异问题**

**关键词**: `知识蒸馏` `异构架构` `特征对齐` `子对数解耦` `正交损失` `模型泛化`

## 📋 核心要点

1. 异构架构蒸馏面临空间特征表示差异，传统方法难以有效处理
2. HCD通过互补特征映射和子对数解耦蒸馏，促进多样知识转移
3. 在CIFAR-100和ImageNet-1K等数据集上优于现有方法，提升学生模型鲁棒性

## 📄 摘要（原文）

> Knowledge distillation (KD)transfers the dark knowledge from a complex teacher to a compact student. However, heterogeneous architecture distillation, such as Vision Transformer (ViT) to ResNet18, faces challenges due to differences in spatial feature representations.Traditional KD methods are mostly designed for homogeneous architectures and hence struggle to effectively address the disparity. Although heterogeneous KD approaches have been developed recently to solve these issues, they often incur high computational costs and complex designs, or overly rely on logit alignment, which limits their ability to leverage the complementary features. To overcome these limitations, we propose Heterogeneous Complementary Distillation (HCD),a simple yet effective framework that integrates complementary teacher and student features to align representations in shared logits.These logits are decomposed and constrained to facilitate diverse knowledge transfer to the student. Specifically, HCD processes the student's intermediate features through convolutional projector and adaptive pooling, concatenates them with teacher's feature from the penultimate layer and then maps them via the Complementary Feature Mapper (CFM) module, comprising fully connected layer,to produce shared logits.We further introduce Sub-logit Decoupled Distillation (SDD) that partitions the shared logits into n sub-logits, which are fused with teacher's logits to rectify classification.To ensure sub-logit diversity and reduce redundant knowledge transfer, we propose an Orthogonality Loss (OL).By preserving student-specific strengths and leveraging teacher knowledge,HCD enhances robustness and generalization in students.Extensive experiments on the CIFAR-100, Fine-grained (e.g., CUB200)and ImageNet-1K datasets demonstrate that HCD outperforms state-of-the-art KD methods,establishing it as an effective solution for heterogeneous KD.

