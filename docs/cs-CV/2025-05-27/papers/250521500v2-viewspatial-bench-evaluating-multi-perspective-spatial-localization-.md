---
layout: default
title: ViewSpatial-Bench: Evaluating Multi-perspective Spatial Localization in Vision-Language Models
---

# ViewSpatial-Bench: Evaluating Multi-perspective Spatial Localization in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21500" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21500v2</a>
  <a href="https://arxiv.org/pdf/2505.21500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21500v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21500v2', 'ViewSpatial-Bench: Evaluating Multi-perspective Spatial Localization in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dingming Li, Hongxing Li, Zixuan Wang, Yuchen Yan, Hang Zhang, Siqi Chen, Guiyang Hou, Shengpei Jiang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Yueting Zhuang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-27 (更新: 2025-09-30)

**备注**: Project: https://zju-real.github.io/ViewSpatial-Page/

---

## 💡 一句话要点

**提出ViewSpatial-Bench以解决多视角空间定位问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `空间推理` `多视角评估` `3D注释` `机器人导航` `增强现实` `虚拟现实`

## 📋 核心要点

1. 核心问题：现有视觉语言模型在跨视角空间推理方面存在显著不足，尤其是在从人类视角进行推理时表现不佳。
2. 方法要点：论文提出了ViewSpatial-Bench基准，专注于多视角空间定位评估，并引入自动化3D注释管道以生成方向标签。
3. 实验或效果：通过在多视角空间数据集上微调VLMs，整体性能提升达46.24%，显示出该方法的有效性。

## 📝 摘要（中文）

视觉语言模型（VLMs）在理解和推理视觉内容方面表现出色，但在需要跨视角理解和空间推理的任务中仍面临重大挑战。我们发现当前VLMs主要在自我中心空间推理（从相机视角）方面表现良好，但在需要采用其他实体空间参考框架时，难以推广到外部视角。为此，我们提出了ViewSpatial-Bench，这是第一个专门为多视角空间定位识别评估设计的综合基准，涵盖五种不同任务类型，并支持一个自动化的3D注释管道以生成精确的方向标签。对多种VLMs在ViewSpatial-Bench上的全面评估显示，模型在相机视角任务上表现合理，但在从人类视角推理时准确性降低。通过在我们的多视角空间数据集上微调VLMs，我们在各任务上实现了46.24%的整体性能提升，突显了我们方法的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型在多视角空间定位任务中的不足，尤其是在从人类视角进行推理时的准确性问题。现有方法主要集中在自我中心的空间推理，导致在需要外部视角时性能下降。

**核心思路**：我们提出ViewSpatial-Bench基准，专门设计用于评估多视角空间定位能力。通过引入一个自动化的3D注释管道，生成精确的方向标签，帮助模型更好地理解和推理空间关系。

**技术框架**：整个框架包括数据收集、3D注释生成、模型训练和评估四个主要模块。数据收集阶段涵盖多种视角的图像和文本描述，注释生成阶段则利用自动化工具生成方向标签。模型训练阶段通过微调现有VLMs，最后在评估阶段对模型性能进行全面测试。

**关键创新**：本研究的主要创新在于提出了一个专门针对多视角空间定位的基准和相应的3D注释管道。这一设计使得模型能够在不同的空间参考框架下进行有效推理，显著提升了模型的空间理解能力。

**关键设计**：在模型训练过程中，我们采用了特定的损失函数以优化空间推理能力，并调整了网络结构以适应多视角数据的特性。通过这些设计，模型在处理不同视角时的表现得到了显著改善。

## 📊 实验亮点

在实验中，我们对多种视觉语言模型进行了评估，结果显示模型在相机视角任务上表现良好，但在从人类视角推理时准确性显著下降。通过在我们的多视角空间数据集上微调模型，整体性能提升达46.24%，证明了我们方法的有效性和必要性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和虚拟现实等场景。在这些领域中，准确的空间定位和理解是实现高效交互和操作的关键。未来，随着技术的进步，ViewSpatial-Bench可能成为评估和提升多模态AI系统空间智能的重要工具。

## 📄 摘要（原文）

> Vision-language models (VLMs) have demonstrated remarkable capabilities in understanding and reasoning about visual content, but significant challenges persist in tasks requiring cross-viewpoint understanding and spatial reasoning. We identify a critical limitation: current VLMs excel primarily at egocentric spatial reasoning (from the camera's perspective) but fail to generalize to allocentric viewpoints when required to adopt another entity's spatial frame of reference. We introduce ViewSpatial-Bench, the first comprehensive benchmark designed specifically for multi-viewpoint spatial localization recognition evaluation across five distinct task types, supported by an automated 3D annotation pipeline that generates precise directional labels. Comprehensive evaluation of diverse VLMs on ViewSpatial-Bench reveals a significant performance disparity: models demonstrate reasonable performance on camera-perspective tasks but exhibit reduced accuracy when reasoning from a human viewpoint. By fine-tuning VLMs on our multi-perspective spatial dataset, we achieve an overall performance improvement of 46.24% across tasks, highlighting the efficacy of our approach. Our work establishes a crucial benchmark for spatial intelligence in embodied AI systems and provides empirical evidence that modeling 3D spatial relationships enhances VLMs' corresponding spatial comprehension capabilities.

