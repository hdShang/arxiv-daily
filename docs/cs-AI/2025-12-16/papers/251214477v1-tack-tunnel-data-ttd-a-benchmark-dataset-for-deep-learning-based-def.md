---
layout: default
title: TACK Tunnel Data (TTD): A Benchmark Dataset for Deep Learning-Based Defect Detection in Tunnels
---

# TACK Tunnel Data (TTD): A Benchmark Dataset for Deep Learning-Based Defect Detection in Tunnels

**arXiv**: [2512.14477v1](https://arxiv.org/abs/2512.14477) | [PDF](https://arxiv.org/pdf/2512.14477.pdf)

**作者**: Andreas Sjölander, Valeria Belloni, Robel Fekadu, Andrea Nascetti

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出TACK隧道数据集（TTD）以解决隧道缺陷检测中领域数据稀缺问题**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `隧道缺陷检测` `深度学习数据集` `基础设施检查` `图像分割` `模型泛化性` `自动化视觉检查` `移动测绘系统` `半监督学习`

## 📋 核心要点

1. 核心问题：隧道缺陷检测依赖传统人工检查，存在耗时、主观和成本高的问题，且深度学习应用受限于领域数据稀缺。
2. 方法要点：构建公开隧道数据集TTD，包含多种衬砌类型的标注图像，支持监督、半监督和无监督学习方法。
3. 实验或效果：数据集促进模型泛化性研究，提升自动化检测效率，为基础设施维护提供数据基础。

## 📝 摘要（中文）

隧道是交通基础设施的关键组成部分，但日益受到老化和劣化机制（如开裂）的影响。为确保其安全，需要定期检查，但传统的人工检查方法耗时、主观且成本高昂。移动测绘系统和深度学习的最新进展使得自动化视觉检查成为可能，但其有效性受限于隧道数据集的稀缺性。本文介绍了一个新的公开可用数据集，包含三种不同隧道衬砌的标注图像，捕捉了典型缺陷：裂缝、渗漏和水渗透。该数据集旨在支持有监督、半监督和无监督的深度学习方法进行缺陷检测和分割。其在纹理和施工技术方面的多样性也使得能够研究模型在不同隧道类型间的泛化性和可迁移性。通过解决领域特定数据的关键缺乏问题，该数据集有助于推进自动化隧道检查，并促进更安全、更高效的基础设施维护策略。

## 🔬 方法详解

论文的核心方法是构建TACK隧道数据集（TTD），整体框架包括数据采集、标注和公开共享。关键技术创新点在于数据集覆盖三种不同隧道衬砌类型（如混凝土、砖石等），并标注了裂缝、渗漏和水渗透等典型缺陷，增强了纹理和施工技术的多样性。与现有方法的主要区别在于，TTD专门针对隧道领域，解决了数据稀缺问题，支持多种深度学习范式（监督、半监督、无监督），并强调模型跨隧道类型的泛化性和可迁移性研究，而现有数据集往往规模小或缺乏多样性。

## 📊 实验亮点

最重要的实验结果包括数据集成功捕捉了多种隧道缺陷，支持深度学习模型训练，并通过多样性设计促进了模型泛化性研究，为自动化检测提供了基准数据，但具体性能提升数据未知。

## 🎯 应用场景

该研究主要应用于交通基础设施的自动化隧道检查领域，潜在价值包括提升隧道安全监测效率、降低人工检查成本，并支持智能维护策略的开发，促进更可持续的基础设施管理。

## 📄 摘要（原文）

> Tunnels are essential elements of transportation infrastructure, but are increasingly affected by ageing and deterioration mechanisms such as cracking. Regular inspections are required to ensure their safety, yet traditional manual procedures are time-consuming, subjective, and costly. Recent advances in mobile mapping systems and Deep Learning (DL) enable automated visual inspections. However, their effectiveness is limited by the scarcity of tunnel datasets. This paper introduces a new publicly available dataset containing annotated images of three different tunnel linings, capturing typical defects: cracks, leaching, and water infiltration. The dataset is designed to support supervised, semi-supervised, and unsupervised DL methods for defect detection and segmentation. Its diversity in texture and construction techniques also enables investigation of model generalization and transferability across tunnel types. By addressing the critical lack of domain-specific data, this dataset contributes to advancing automated tunnel inspection and promoting safer, more efficient infrastructure maintenance strategies.

