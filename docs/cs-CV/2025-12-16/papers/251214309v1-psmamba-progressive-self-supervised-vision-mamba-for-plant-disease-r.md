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

**提出PSMamba框架，通过渐进式自监督视觉Mamba和双学生分层蒸馏策略，解决植物病害识别中多尺度病变模式捕获不足的问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `自监督学习` `视觉Mamba` `植物病害识别` `分层蒸馏` `多尺度建模` `表示学习` `农业人工智能` `序列建模`

## 📋 核心要点

1. 现有自监督学习框架主要依赖全局对齐，难以有效捕获植物病害图像中层次化、多尺度的病变模式，导致识别精度受限。
2. PSMamba整合视觉Mamba的高效序列建模与双学生分层蒸馏，通过共享全局教师和专门化学生，实现多粒度监督和跨尺度对齐。
3. 在三个基准数据集上，PSMamba在领域转移和细粒度场景中均超越现有方法，显著提升了准确性和鲁棒性。

## 📝 摘要（中文）

自监督学习已成为无需人工标注的强大表示学习范式，但现有框架多关注全局对齐，难以捕获植物病害图像中层次化、多尺度的病变模式。为填补这一空白，本文提出PSMamba，一个渐进式自监督框架，将视觉Mamba的高效序列建模与双学生分层蒸馏策略相结合。不同于传统的单教师-学生设计，PSMamba采用共享的全局教师和两个专门化学生：一个处理中尺度视图以捕获病变分布和叶脉结构，另一个专注于局部视图以捕获细粒度线索，如纹理不规则和早期病变。这种多粒度监督促进了上下文和细节表示的联合学习，并通过一致性损失确保跨尺度对齐的连贯性。在三个基准数据集上的实验表明，PSMamba在领域转移和细粒度场景中均优于最先进的自监督学习方法，展现出卓越的准确性和鲁棒性。

## 🔬 方法详解

PSMamba是一个渐进式自监督框架，整体架构基于视觉Mamba，结合双学生分层蒸馏策略。关键技术创新点包括：采用共享全局教师和两个专门化学生，分别处理中尺度和局部视图，以捕获病变分布、叶脉结构及细粒度纹理；通过一致性损失实现跨尺度对齐，促进上下文与细节表示的联合学习。与现有方法的主要区别在于，传统自监督学习多依赖单一教师-学生设计，而PSMamba通过多粒度监督和分层蒸馏，更有效地建模植物病害的多尺度特征，提升了表示学习的效率和效果。

## 📊 实验亮点

在三个基准数据集上的实验显示，PSMamba在领域转移和细粒度场景中均优于最先进的自监督学习方法，准确性和鲁棒性显著提升，验证了其多尺度建模和分层蒸馏策略的有效性。

## 🎯 应用场景

该研究主要应用于植物病害识别领域，可支持农业自动化监测、精准病害诊断和早期预警系统。通过提升自监督学习的表示能力，PSMamba有助于减少对大量标注数据的依赖，降低人工成本，并增强模型在复杂环境下的鲁棒性，为智能农业和植物保护提供技术支撑。

## 📄 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

