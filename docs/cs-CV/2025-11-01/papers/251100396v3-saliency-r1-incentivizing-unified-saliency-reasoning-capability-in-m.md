---
layout: default
title: "Saliency-R1: Incentivizing Unified Saliency Reasoning Capability in MLLM with Confidence-Guided Reinforcement Learning"
---

# Saliency-R1: Incentivizing Unified Saliency Reasoning Capability in MLLM with Confidence-Guided Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00396" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00396v3</a>
  <a href="https://arxiv.org/pdf/2511.00396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00396v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00396v3', 'Saliency-R1: Incentivizing Unified Saliency Reasoning Capability in MLLM with Confidence-Guided Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Li, Shuichen Ji, Ziyang Luo, Zhihui Li, Dingwen Zhang, Junwei Han, Nian Liu

**分类**: cs.CV

**发布日期**: 2025-11-01 (更新: 2025-11-26)

**备注**: Main text (excluding references): 8 pages, 4 figures; Supplementary Materials (excluding references): 9 pages, 10 figures

---

## 💡 一句话要点

**Saliency-R1：利用置信度引导强化学习，提升MLLM的统一显著性推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态大语言模型` `显著性检测` `强化学习` `视觉推理` `指代分割`

## 📋 核心要点

1. 现有的多模态大语言模型缺乏对视觉显著性的内在感知，难以识别关键视觉元素，限制了其视觉理解能力。
2. Saliency-R1通过统一框架处理SOD、SIS和CoSOD三个任务，并引入文本接口和结构化标签来编码区域和实例级别的指代表达式。
3. 提出的CGPO算法利用奖励-置信度差异作为单样本信号，有效提升了训练效率，模型性能超越了现有MLLM和专用方法。

## 📝 摘要（中文）

本文提出了Saliency-R1，这是一个统一的多模态大语言模型（MLLM）框架，旨在共同解决三个具有代表性的、异构的显著性任务：显著性目标检测（SOD）、显著性实例分割（SIS）和共显著性目标检测（CoSOD），从而增强模型对显著性推理的能力。我们引入了一个带有结构化标签（<rg>，<ins>）的文本接口来编码区域和实例级别的指代表达式，使得单个指代分割器能够生成适合任务的掩码。为了高效地训练MLLM，我们提出了一种新的单样本强化学习算法——置信度引导策略优化（CGPO）。CGPO通过用基于奖励-置信度差异的单样本信号替换组归一化优势，改进了GRPO，从而减少了计算浪费，减轻了信号稀释，并降低了训练开销。我们的模型在所有三个任务中都超过或匹配了强大的开源/闭源MLLM和专门的最先进方法的性能，证明了我们的框架在显著性推理方面的有效性。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型（MLLM）在视觉-语言推理方面表现出色，但缺乏对视觉显著性的内在感知，难以准确识别图像中的关键视觉元素。这限制了它们在需要关注重要区域的任务中的表现。此外，现有的显著性检测任务通常是独立处理的，缺乏一个统一的框架来整合不同类型的显著性推理能力。

**核心思路**：Saliency-R1的核心思路是构建一个统一的MLLM框架，使其能够同时处理显著性目标检测（SOD）、显著性实例分割（SIS）和共显著性目标检测（CoSOD）这三个不同的显著性任务。通过引入文本接口和结构化标签，模型可以理解不同任务的需求，并生成相应的显著性掩码。此外，利用置信度引导的强化学习算法（CGPO）来高效地训练模型，提升其显著性推理能力。

**技术框架**：Saliency-R1框架主要包含以下几个模块：1) 视觉编码器：用于提取输入图像的视觉特征。2) 文本编码器：用于编码文本指令，包括任务类型和指代表达式。3) 跨模态融合模块：将视觉特征和文本特征进行融合，以理解图像内容和任务需求。4) 指代分割器：根据融合后的特征生成显著性掩码。5) 奖励函数：用于评估生成的掩码的质量。6) 置信度引导策略优化（CGPO）：用于优化模型的参数，使其能够生成更准确的显著性掩码。

**关键创新**：Saliency-R1的关键创新在于以下几个方面：1) 统一的显著性推理框架：首次将SOD、SIS和CoSOD三个任务整合到一个统一的MLLM框架中。2) 文本接口和结构化标签：引入了文本接口和结构化标签，使得模型能够理解不同任务的需求，并生成相应的显著性掩码。3) 置信度引导策略优化（CGPO）：提出了一种新的单样本强化学习算法，利用奖励-置信度差异作为单样本信号，提高了训练效率。

**关键设计**：在文本接口设计上，使用了`<rg>`和`<ins>`标签来区分区域级别和实例级别的指代表达式。在CGPO算法中，使用奖励-置信度差异来代替传统的组归一化优势，从而减少了计算浪费，减轻了信号稀释。具体的奖励函数设计取决于具体的显著性任务，例如，可以使用IoU（交并比）来评估生成的掩码与真实掩码的重叠程度。

## 📊 实验亮点

Saliency-R1在SOD、SIS和CoSOD三个任务上都取得了显著的性能提升。例如，在SOD任务上，Saliency-R1超过了现有的开源和闭源MLLM，并且与专门的SOTA方法相媲美。在SIS和CoSOD任务上，Saliency-R1也取得了类似的性能提升，证明了该框架在显著性推理方面的有效性。

## 🎯 应用场景

Saliency-R1具有广泛的应用前景，例如：机器人视觉、自动驾驶、图像编辑、视频监控、医学图像分析等。该研究可以提升机器对图像关键区域的理解能力，从而提高相关任务的性能。未来，该技术可以应用于更复杂的视觉场景，例如：复杂场景理解、视觉问答等。

## 📄 摘要（原文）

> Although multimodal large language models (MLLMs) excel in high-level vision-language reasoning, they lack inherent awareness of visual saliency, making it difficult to identify key visual elements. To bridge this gap, we propose Saliency-R1, the first unified MLLM framework that jointly tackles three representative and heterogeneous saliency tasks: Salient Object Detection (SOD), Salient Instance Segmentation (SIS), and Co-salient Object Detection (CoSOD), enhancing the model's capacity for saliency reasoning. We introduce a textual interface with structured tags (<rg>, <ins>) to encode region- and instance-level referring expressions, enabling a single referring segmenter to produce task-appropriate masks. To train the MLLM efficiently, we propose Confidence-Guided Policy Optimization (CGPO), a novel single-sample reinforcement learning algorithm. CGPO improves on GRPO by replacing group-normalized advantages with a per-sample signal based on reward-confidence discrepancy, thereby reducing computational waste, mitigating signal dilution, and lowering training overhead. Our model exceeds or matches the performance of robust open/closed-source MLLMs and specialized state-of-the-art methods across all three tasks, demonstrating the efficacy of our framework in saliency reasoning.

