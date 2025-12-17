---
layout: default
title: MAFM^3: Modular Adaptation of Foundation Models for Multi-Modal Medical AI
---

# MAFM^3: Modular Adaptation of Foundation Models for Multi-Modal Medical AI

**arXiv**: [2511.11212v1](https://arxiv.org/abs/2511.11212) | [PDF](https://arxiv.org/pdf/2511.11212.pdf)

**作者**: Mohammad Areeb Qazi, Munachiso S Nwadike, Ibrahim Almakky, Mohammad Yaqub, Numan Saeed

---

## 💡 一句话要点

**提出MAFM^3框架，通过模块化组件扩展基础模型以解决医学影像多模态多任务适应问题**

**关键词**: `医学影像` `基础模型适应` `多模态学习` `模块化框架` `轻量组件`

## 📋 核心要点

1. 医学影像数据稀缺，难以针对每个领域、模态或任务预训练基础模型
2. 使用轻量模块化组件，使单一基础模型灵活适应不同输入类型或临床目标
3. 实验显示，在CT和PET扫描任务中，性能优于基线，如Dice分数提升5%

## 📄 摘要（原文）

> Foundational models are trained on extensive datasets to capture the general trends of a domain. However, in medical imaging, the scarcity of data makes pre-training for every domain, modality, or task challenging. Instead of building separate models, we propose MAFM^3 (Modular Adaptation of Foundation Models for Multi-Modal Medical AI), a framework that enables a single foundation model to expand into diverse domains, tasks, and modalities through lightweight modular components. These components serve as specialized skill sets that allow the system to flexibly activate the appropriate capability at the inference time, depending on the input type or clinical objective. Unlike conventional adaptation methods that treat each new task or modality in isolation, MAFM^3 provides a unified and expandable framework for efficient multitask and multimodality adaptation. Empirically, we validate our approach by adapting a chest CT foundation model initially trained for classification into prognosis and segmentation modules. Our results show improved performance on both tasks. Furthermore, by incorporating PET scans, MAFM^3 achieved an improvement in the Dice score 5% compared to the respective baselines. These findings establish that foundation models, when equipped with modular components, are not inherently constrained to their initial training scope but can evolve into multitask, multimodality systems for medical imaging. The code implementation of this work can be found at https://github.com/Areeb2735/CTscan_prognosis_VLM

