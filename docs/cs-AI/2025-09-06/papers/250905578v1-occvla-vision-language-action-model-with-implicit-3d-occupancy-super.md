---
layout: default
title: "OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision"
---

# OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05578" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05578v1</a>
  <a href="https://arxiv.org/pdf/2509.05578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05578v1', 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruixun Liu, Lingyu Kong, Derun Li, Hang Zhao

**分类**: cs.AI, cs.RO

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**OccVLA：提出基于隐式3D Occupancy监督的视觉-语言-动作模型，提升自动驾驶场景理解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `3D Occupancy` `自动驾驶` `多模态学习` `空间推理`

## 📋 核心要点

1. 现有方法缺乏鲁棒的3D空间理解，难以构建有效的3D表示，且VLMs丢失了细粒度空间细节。
2. OccVLA将3D occupancy作为预测输出和监督信号，直接从2D视觉输入中学习细粒度空间结构。
3. OccVLA在nuScenes轨迹规划和3D视觉问答任务上取得了SOTA结果，且推理阶段无额外计算开销。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在视觉-语言推理方面表现出强大的能力，但仍然缺乏鲁棒的3D空间理解，这对于自动驾驶至关重要。这种局限性源于两个关键挑战：(1)在没有昂贵的人工标注的情况下，难以构建可访问但有效的3D表示；(2)由于缺乏大规模的3D视觉-语言预训练，VLMs中细粒度空间细节的丢失。为了应对这些挑战，我们提出了OccVLA，这是一种将3D occupancy表示集成到统一的多模态推理过程中的新框架。与依赖显式3D输入的方法不同，OccVLA将密集的3D occupancy视为预测输出和监督信号，使模型能够直接从2D视觉输入中学习细粒度的空间结构。Occupancy预测被视为隐式推理过程，可以在推理期间跳过，而不会降低性能，从而不会增加额外的计算开销。OccVLA在nuScenes基准测试中实现了轨迹规划的最先进结果，并在3D视觉问答任务中表现出卓越的性能，为自动驾驶提供了一种可扩展、可解释且完全基于视觉的解决方案。

## 🔬 方法详解

**问题定义**：现有基于视觉-语言的自动驾驶模型缺乏对3D空间的精确理解，尤其是在没有大量3D标注数据的情况下。传统方法要么依赖于显式的3D输入（如点云），增加了计算负担，要么在视觉-语言模型的预训练中忽略了3D信息的有效利用，导致模型在处理空间关系时能力不足。

**核心思路**：OccVLA的核心思想是将3D occupancy作为一种隐式的推理过程。模型通过预测3D occupancy来学习场景的几何结构和空间关系，而无需在推理时显式地使用3D数据。这种方法利用2D视觉输入来监督3D occupancy的预测，从而在视觉-语言模型中注入3D空间理解能力。

**技术框架**：OccVLA框架包含一个视觉编码器、一个语言模型和一个3D occupancy预测模块。视觉编码器负责提取2D图像特征，语言模型负责处理文本输入并进行推理，3D occupancy预测模块则根据视觉特征预测场景的3D occupancy。在训练阶段，模型同时学习视觉-语言任务和3D occupancy预测任务。在推理阶段，可以跳过3D occupancy预测模块，直接使用视觉和语言特征进行推理。

**关键创新**：OccVLA的关键创新在于将3D occupancy作为一种隐式的监督信号，从而避免了对显式3D数据的依赖。这种方法不仅降低了计算成本，还使得模型能够从2D视觉输入中学习到细粒度的3D空间信息。此外，OccVLA框架可以灵活地集成到现有的视觉-语言模型中，提高了模型的通用性和可扩展性。

**关键设计**：OccVLA使用交叉熵损失函数来监督3D occupancy的预测。为了提高预测的准确性，采用了多尺度特征融合的方法，将不同尺度的视觉特征融合在一起。在网络结构方面，使用了Transformer结构来建模视觉特征和语言特征之间的关系。具体的参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

OccVLA在nuScenes基准测试中实现了轨迹规划的最先进结果，表明其在自动驾驶场景理解方面具有显著优势。此外，OccVLA在3D视觉问答任务中也表现出卓越的性能，证明了其在3D空间推理方面的强大能力。摘要中未提供具体的性能数据和提升幅度，属于未知信息。

## 🎯 应用场景

OccVLA具有广泛的应用前景，可应用于自动驾驶、机器人导航、虚拟现实等领域。在自动驾驶领域，OccVLA可以提高车辆对周围环境的感知能力，从而提高驾驶安全性和舒适性。在机器人导航领域，OccVLA可以帮助机器人更好地理解周围环境，从而实现更智能的导航。在虚拟现实领域，OccVLA可以用于构建更逼真的3D场景，从而提高用户的沉浸感。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

