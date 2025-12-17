---
layout: default
title: PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
---

# PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition

**arXiv**: [2512.14309v1](https://arxiv.org/abs/2512.14309) | [PDF](https://arxiv.org/pdf/2512.14309.pdf)

**作者**: Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出PSMamba渐进自监督视觉Mamba框架，以解决植物病害识别中多尺度病变模式捕获不足的问题。**

**关键词**: `自监督学习` `视觉Mamba` `植物病害识别` `多尺度建模` `层次蒸馏` `序列建模` `细粒度识别` `农业人工智能`

## 📋 核心要点

1. 现有自监督学习框架主要依赖全局对齐，难以有效建模植物病害图像中复杂的多尺度病变模式，导致在细粒度识别任务上表现受限。
2. PSMamba创新性地结合视觉Mamba的序列建模能力与双学生层次蒸馏策略，通过共享全局教师和两个专门化学生分别处理中尺度和局部视图，实现多粒度监督学习。
3. 在三个基准数据集上的实验验证了PSMamba的优越性，其准确性和鲁棒性均超越现有自监督方法，尤其在领域偏移和细粒度场景中表现突出。

## 📝 摘要（中文）

自监督学习已成为无需人工标注的强大表示学习范式。然而，现有框架多关注全局对齐，难以捕获植物病害图像中层次化、多尺度的病变模式特征。为填补这一空白，本文提出PSMamba，一种渐进自监督框架，将视觉Mamba的高效序列建模与双学生层次蒸馏策略相结合。不同于传统的单教师-学生设计，PSMamba采用共享全局教师和两个专门化学生：一个处理中尺度视图以捕获病变分布和叶脉结构，另一个聚焦局部视图以捕获细粒度线索，如纹理不规则和早期病变。这种多粒度监督促进了上下文和细节表示的联合学习，并通过一致性损失确保跨尺度对齐的连贯性。在三个基准数据集上的实验表明，PSMamba持续优于最先进的自监督学习方法，在领域偏移和细粒度场景中均展现出卓越的准确性和鲁棒性。

## 🔬 方法详解

PSMamba的整体框架是一个渐进自监督学习系统，核心创新在于将视觉Mamba的高效序列建模与双学生层次蒸馏策略深度融合。关键技术创新点包括：采用共享全局教师提供全局表示指导，同时部署两个专门化学生——一个处理中尺度视图以捕获病变分布和叶脉结构等中层特征，另一个聚焦局部视图以提取纹理不规则和早期病变等细粒度线索；通过多粒度监督和一致性损失实现跨尺度对齐的联合学习。与现有方法的主要区别在于：传统自监督框架多基于单一教师-学生设计或仅关注全局对齐，而PSMamba通过双学生架构和渐进式蒸馏，更精细地建模了植物病害图像中的层次化多尺度模式，提升了表示学习的全面性和鲁棒性。

## 📊 实验亮点

在三个植物病害基准数据集上的实验表明，PSMamba在准确性和鲁棒性上均显著优于现有最先进的自监督学习方法，尤其在处理领域偏移和细粒度识别任务时表现卓越，验证了其多尺度建模的有效性。

## 🎯 应用场景

该研究主要应用于农业领域的植物病害智能识别与监测，可集成于移动设备或无人机平台，实现大规模农田的自动化病害诊断。其潜在价值包括降低人工标注成本、提高早期病害检测精度，并为精准农业和可持续作物管理提供技术支持。

## 📄 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

