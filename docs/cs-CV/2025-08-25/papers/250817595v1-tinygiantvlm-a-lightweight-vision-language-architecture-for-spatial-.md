---
layout: default
title: "TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints"
---

# TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17595" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17595v1</a>
  <a href="https://arxiv.org/pdf/2508.17595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17595v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17595v1', 'TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vinh-Thuan Ly, Hoang M. Truong, Xuan-Huong Nguyen

**分类**: cs.CV

**发布日期**: 2025-08-25

**备注**: Accepted for presentation at the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops, 2025

**期刊**: IEEE/CVF International Conference on Computer Vision (ICCV) Workshops, Hawaii, 2025

---

## 💡 一句话要点

**提出TinyGiantVLM以解决工业环境中的空间推理问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间推理` `视觉-语言模型` `混合专家` `工业应用` `深度学习`

## 📋 核心要点

1. 现有视觉-语言模型在理解三维布局和物体排列方面存在显著不足，难以应对复杂的工业环境。
2. TinyGiantVLM通过模块化设计和混合专家融合模块，有效处理高模态输入，提升空间推理能力。
3. 在AI City Challenge 2025中，64M参数的基础模型取得第5名，得分66.8861，展示了其在空间推理任务中的优越性能。

## 📝 摘要（中文）

在仓储规模环境中，细粒度空间关系推理对现有视觉-语言模型（VLMs）构成了重大挑战，尤其是在理解三维布局、物体排列和多模态线索方面。本文提出了TinyGiantVLM，一个轻量级和模块化的两阶段框架，专为物理空间推理而设计，区别于复杂物流场景中的传统地理推理。该方法利用预训练的视觉骨干网络，从RGB和深度模态中编码全局和区域级特征。为有效处理高模态输入和多样化问题类型，我们引入了混合专家（MoE）融合模块，动态组合空间表示以支持下游推理任务并提高收敛性。经过两阶段训练，模型在AI City Challenge 2025的第三轨道评估中取得了第5名的成绩，显示出在工业环境中视觉感知与空间理解的强大表现。

## 🔬 方法详解

**问题定义**：本文旨在解决在仓储规模环境中进行细粒度空间推理的挑战，现有方法在处理三维布局和物体排列方面表现不足，难以适应复杂的工业场景。

**核心思路**：TinyGiantVLM采用轻量级和模块化的两阶段框架，结合混合专家（MoE）模块，动态融合空间表示，以支持多样化的推理任务，提升模型的收敛性和推理能力。

**技术框架**：该框架分为两个主要阶段：第一阶段生成自由形式的答案以增强空间推理能力，第二阶段使用标准化答案进行评估。整体架构包括预训练的视觉骨干网络和MoE融合模块。

**关键创新**：最重要的创新在于引入了混合专家模块，能够动态组合不同的空间表示，显著提高了模型在复杂任务中的表现，与传统方法相比，具有更高的灵活性和适应性。

**关键设计**：模型参数设置为64M和80M，后者具有扩展的MoE容量，采用特定的损失函数以优化空间推理能力，网络结构经过精心设计以适应多模态输入。

## 📊 实验亮点

在AI City Challenge 2025中，TinyGiantVLM的64M参数基础模型取得了第5名，得分66.8861，显示出在复杂空间推理任务中的强大能力。80M参数的变体进一步提升了性能，展示了混合专家模块的有效性。

## 🎯 应用场景

TinyGiantVLM的研究成果在物流、仓储管理和智能制造等领域具有广泛的应用潜力。通过提高空间推理能力，该模型能够优化物体布局、提升自动化水平，并为智能机器人提供更好的环境理解能力，未来可能推动工业4.0的发展。

## 📄 摘要（原文）

> Reasoning about fine-grained spatial relationships in warehouse-scale environments poses a significant challenge for existing vision-language models (VLMs), which often struggle to comprehend 3D layouts, object arrangements, and multimodal cues in real-world industrial settings. In this paper, we present TinyGiantVLM, a lightweight and modular two-stage framework designed for physical spatial reasoning, distinguishing itself from traditional geographic reasoning in complex logistics scenes. Our approach encodes both global and region-level features from RGB and depth modalities using pretrained visual backbones. To effectively handle the complexity of high-modality inputs and diverse question types, we incorporate a Mixture-of-Experts (MoE) fusion module, which dynamically combines spatial representations to support downstream reasoning tasks and improve convergence. Training is conducted in a two-phase strategy: the first phase focuses on generating free-form answers to enhance spatial reasoning ability, while the second phase uses normalized answers for evaluation. Evaluated on Track 3 of the AI City Challenge 2025, our 64M-parameter base model achieved 5th place on the leaderboard with a score of 66.8861, demonstrating strong performance in bridging visual perception and spatial understanding in industrial environments. We further present an 80M-parameter variant with expanded MoE capacity, which demonstrates improved performance on spatial reasoning tasks.

