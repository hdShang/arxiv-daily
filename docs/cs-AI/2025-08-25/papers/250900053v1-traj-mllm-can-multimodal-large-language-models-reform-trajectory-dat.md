---
layout: default
title: "Traj-MLLM: Can Multimodal Large Language Models Reform Trajectory Data Mining?"
---

# Traj-MLLM: Can Multimodal Large Language Models Reform Trajectory Data Mining?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00053" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00053v1</a>
  <a href="https://arxiv.org/pdf/2509.00053.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00053v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00053v1', 'Traj-MLLM: Can Multimodal Large Language Models Reform Trajectory Data Mining?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuo Liu, Di Yao, Yan Lin, Gao Cong, Jingping Bi

**分类**: cs.MM, cs.AI, cs.CL

**发布日期**: 2025-08-25

**备注**: 20 pages, 10 figures

---

## 💡 一句话要点

**提出Traj-MLLM以解决轨迹数据挖掘的泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `轨迹数据挖掘` `多模态大语言模型` `智能交通` `数据泛化` `时空特征`

## 📋 核心要点

1. 现有轨迹数据挖掘方法普遍存在泛化能力不足的问题，限制了其在不同区域和任务中的应用。
2. 本文提出的Traj-MLLM框架通过将轨迹转换为图像-文本序列，利用多模态大语言模型的推理能力进行分析。
3. 在四个公开数据集上的实验结果显示，Traj-MLLM在多个任务上均显著超越了当前最先进的方法，提升幅度达到48.05%等。

## 📝 摘要（中文）

构建一个能够分析不同地理区域和任务的人类轨迹的通用模型成为了一个紧迫且重要的问题。然而，现有方法面临泛化问题，通常仅限于特定区域或少数任务。本文提出了Traj-MLLM，这是第一个使用多模态大语言模型（MLLMs）进行轨迹数据挖掘的通用框架。通过整合多视角上下文，Traj-MLLM将原始轨迹转换为交错的图像-文本序列，同时保留关键的时空特征，并直接利用MLLMs的推理能力进行轨迹分析。实验结果表明，Traj-MLLM在旅行时间估计、移动性预测、异常检测和交通模式识别等任务上均优于现有最先进的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决轨迹数据挖掘中的泛化问题，现有方法通常只能针对特定区域或任务进行训练，缺乏通用性。

**核心思路**：Traj-MLLM通过将轨迹数据转化为多模态的图像-文本序列，利用MLLMs的强大推理能力，从而实现对轨迹的灵活分析。

**技术框架**：该框架包括数据预处理、轨迹转换、上下文整合和任务适应等模块，整体流程为：输入轨迹数据 → 生成图像-文本序列 → 应用MLLM进行分析。

**关键创新**：Traj-MLLM的创新在于首次将多模态大语言模型应用于轨迹数据挖掘，克服了传统方法的局限性，提供了更为灵活的分析手段。

**关键设计**：在设计中，采用了数据不变的提示优化方法，确保模型在不同任务间的适应性，同时保持了时空特征的完整性。

## 📊 实验亮点

Traj-MLLM在四个公开数据集上的实验结果显示，在旅行时间估计、移动性预测、异常检测和交通模式识别任务上，分别提升了48.05%、15.52%、51.52%和1.83%的性能，显著超越了现有最先进的基线，展现了其强大的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、城市规划和公共安全等。通过提升轨迹数据分析的准确性和灵活性，Traj-MLLM能够为相关领域提供更为有效的决策支持，推动智能城市的发展。

## 📄 摘要（原文）

> Building a general model capable of analyzing human trajectories across different geographic regions and different tasks becomes an emergent yet important problem for various applications. However, existing works suffer from the generalization problem, \ie, they are either restricted to train for specific regions or only suitable for a few tasks. Given the recent advances of multimodal large language models (MLLMs), we raise the question: can MLLMs reform current trajectory data mining and solve the problem? Nevertheless, due to the modality gap of trajectory, how to generate task-independent multimodal trajectory representations and how to adapt flexibly to different tasks remain the foundational challenges. In this paper, we propose \texttt{Traj-MLLM}}, which is the first general framework using MLLMs for trajectory data mining. By integrating multiview contexts, \texttt{Traj-MLLM}} transforms raw trajectories into interleaved image-text sequences while preserving key spatial-temporal characteristics, and directly utilizes the reasoning ability of MLLMs for trajectory analysis. Additionally, a prompt optimization method is proposed to finalize data-invariant prompts for task adaptation. Extensive experiments on four publicly available datasets show that \texttt{Traj-MLLM}} outperforms state-of-the-art baselines by $48.05\%$, $15.52\%$, $51.52\%$, $1.83\%$ on travel time estimation, mobility prediction, anomaly detection and transportation mode identification, respectively. \texttt{Traj-MLLM}} achieves these superior performances without requiring any training data or fine-tuning the MLLM backbones.

