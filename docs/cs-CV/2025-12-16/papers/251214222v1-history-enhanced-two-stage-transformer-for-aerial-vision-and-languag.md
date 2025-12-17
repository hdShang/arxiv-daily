---
layout: default
title: History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation
---

# History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation

**arXiv**: [2512.14222v1](https://arxiv.org/abs/2512.14222) | [PDF](https://arxiv.org/pdf/2512.14222.pdf)

**作者**: Xichen Ding, Jianzhe Gao, Cong Pan, Wenguan Wang, Jie Qin

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出历史增强两阶段Transformer框架，以解决无人机视觉语言导航中全局推理与局部理解不平衡的问题。**

**关键词**: `视觉语言导航` `无人机导航` `Transformer架构` `多模态融合` `空间记忆` `粗到细导航` `城市环境` `数据集优化`

## 📋 核心要点

1. 现有无人机代理采用单粒度框架，难以平衡全局环境推理与局部场景理解，导致导航性能受限。
2. 提出历史增强两阶段Transformer框架，通过粗到细流程融合空间地标和历史上下文，并设计历史网格地图增强场景感知。
3. 在优化后的CityNav数据集上，HETT实现显著性能提升，消融研究验证了各组件有效性，证明方法优越性。

## 📝 摘要（中文）

空中视觉语言导航（AVLN）要求无人机代理基于语言指令在大规模城市环境中定位目标。成功导航需要全局环境推理和局部场景理解，但现有无人机代理通常采用单粒度框架，难以平衡这两方面。为应对此限制，本研究提出历史增强两阶段Transformer（HETT）框架，通过粗到细的导航流程整合这两个方面。具体而言，HETT首先通过融合空间地标和历史上下文预测粗粒度目标位置，然后通过细粒度视觉分析精炼动作。此外，设计了一个历史网格地图，动态将视觉特征聚合为结构化空间记忆，增强综合场景感知。同时，手动优化了CityNav数据集标注以提升数据质量。在优化后的CityNav数据集上的实验显示，HETT带来显著性能提升，而广泛的消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

HETT框架采用两阶段Transformer架构，整体流程为粗到细导航。首先，在粗粒度阶段，通过融合空间地标和历史上下文预测目标位置；其次，在细粒度阶段，基于视觉分析精炼动作。关键技术创新包括历史网格地图，动态聚合视觉特征为结构化空间记忆，增强场景感知。与现有方法的主要区别在于其双粒度设计，有效整合全局推理和局部理解，避免了单粒度框架的局限性。

## 📊 实验亮点

在优化后的CityNav数据集上，HETT相比现有方法带来显著性能提升，消融研究证实历史网格地图和两阶段设计是关键贡献，验证了框架的有效性和鲁棒性。

## 🎯 应用场景

该研究可应用于无人机自主导航、城市搜索救援、物流配送和智能监控等领域，通过提升视觉语言导航的准确性和效率，支持复杂环境下的目标定位和路径规划，具有实际工业价值。

## 📄 摘要（原文）

> Aerial Vision-and-Language Navigation (AVLN) requires Unmanned Aerial Vehicle (UAV) agents to localize targets in large-scale urban environments based on linguistic instructions. While successful navigation demands both global environmental reasoning and local scene comprehension, existing UAV agents typically adopt mono-granularity frameworks that struggle to balance these two aspects. To address this limitation, this work proposes a History-Enhanced Two-Stage Transformer (HETT) framework, which integrates the two aspects through a coarse-to-fine navigation pipeline. Specifically, HETT first predicts coarse-grained target positions by fusing spatial landmarks and historical context, then refines actions via fine-grained visual analysis. In addition, a historical grid map is designed to dynamically aggregate visual features into a structured spatial memory, enhancing comprehensive scene awareness. Additionally, the CityNav dataset annotations are manually refined to enhance data quality. Experiments on the refined CityNav dataset show that HETT delivers significant performance gains, while extensive ablation studies further verify the effectiveness of each component.

