---
layout: default
title: "TopKD: Top-scaled Knowledge Distillation"
---

# TopKD: Top-scaled Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04539" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04539v1</a>
  <a href="https://arxiv.org/pdf/2508.04539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04539v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04539v1', 'TopKD: Top-scaled Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Wang, Jinjia Zhou

**分类**: cs.CV

**发布日期**: 2025-08-06

**备注**: 12 pages, 6 figures, conference, 8 Tables

---

## 💡 一句话要点

**提出TopKD以提升知识蒸馏中的logit信息利用**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `logit分布` `Top-K知识` `深度学习` `模型压缩` `视觉变换器` `蒸馏训练`

## 📋 核心要点

1. 现有知识蒸馏方法多集中于特征级知识转移，忽视了教师模型logit分布中的重要信息，导致信息利用不足。
2. 本文提出TopKD，通过Top-K Scaling Module和Top-K Decoupled Loss，增强logit信息的利用，提供更有效的蒸馏监督。
3. 在多个数据集上进行的实验表明，TopKD在蒸馏性能上显著优于现有方法，尤其在视觉变换器的蒸馏中表现突出。

## 📝 摘要（中文）

近年来，知识蒸馏（KD）的研究主要集中在特征级知识转移上，常常忽视教师模型logit分布中蕴含的重要信息。本文重新审视基于logit的蒸馏，提出了一个未被充分探索的关键元素：Top-K知识。为此，提出了Top-scaled Knowledge Distillation (TopKD)，这是一个简单、高效且与架构无关的框架，显著增强了基于logit的蒸馏。TopKD包含两个主要组件：（1）Top-K Scaling Module (TSM)，自适应地放大最具信息量的logits；（2）Top-K Decoupled Loss (TDL)，提供有针对性和有效的监督。实验结果表明，TopKD在CIFAR-100、ImageNet、STL-10和Tiny-ImageNet上均超越了现有的蒸馏方法，尤其在蒸馏视觉变换器时表现出显著的有效性，展示了其在多种网络架构中的通用性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有知识蒸馏方法未能充分利用教师模型logit分布中的关键信息的问题，导致蒸馏效果不佳。

**核心思路**：提出TopKD框架，通过放大最具信息量的logits和提供针对性的损失函数，来提升知识蒸馏的效果。这样的设计旨在更好地利用教师模型的输出信息。

**技术框架**：TopKD框架主要由两个模块组成：Top-K Scaling Module (TSM)和Top-K Decoupled Loss (TDL)。TSM负责自适应放大重要logits，而TDL则提供有效的监督信号。

**关键创新**：TopKD的核心创新在于引入Top-K知识的概念，通过放大最有信息量的logits，显著提升了蒸馏效果。这一方法与传统的特征级蒸馏方法本质上不同，强调了logit信息的重要性。

**关键设计**：在设计中，TSM模块通过动态调整logits的权重来放大Top-K信息，而TDL则通过解耦损失函数来提供更精确的监督，确保蒸馏过程的有效性。

## 📊 实验亮点

实验结果显示，TopKD在CIFAR-100、ImageNet、STL-10和Tiny-ImageNet等数据集上均超越了现有的蒸馏方法，尤其在蒸馏视觉变换器时，性能提升显著，展示了其在多种网络架构中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理等多个领域的模型压缩和加速。通过有效的知识蒸馏，TopKD能够帮助在资源受限的环境中部署高性能模型，提升实际应用的效率和效果。未来，TopKD可能会在多种深度学习任务中得到广泛应用，推动模型的轻量化和高效化。

## 📄 摘要（原文）

> Recent advances in knowledge distillation (KD) predominantly emphasize feature-level knowledge transfer, frequently overlooking critical information embedded within the teacher's logit distributions. In this paper, we revisit logit-based distillation and reveal an underexplored yet critical element: Top-K knowledge. Motivated by this insight, we propose Top-scaled Knowledge Distillation (TopKD), a simple, efficient, and architecture-agnostic framework that significantly enhances logit-based distillation. TopKD consists of two main components: (1) a Top-K Scaling Module (TSM), which adaptively amplifies the most informative logits, and (2) a Top-K Decoupled Loss (TDL), which offers targeted and effective supervision. Notably, TopKD integrates seamlessly into existing KD methods without introducing extra modules or requiring architectural changes. Extensive experiments on CIFAR-100, ImageNet, STL-10, and Tiny-ImageNet demonstrate that TopKD consistently surpasses state-of-the-art distillation methods. Moreover, our method demonstrates substantial effectiveness when distilling Vision Transformers, underscoring its versatility across diverse network architectures. These findings highlight the significant potential of logits to advance knowledge distillation.

