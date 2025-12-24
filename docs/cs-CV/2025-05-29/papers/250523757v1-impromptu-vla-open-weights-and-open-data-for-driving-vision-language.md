---
layout: default
title: "Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models"
---

# Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23757" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23757v1</a>
  <a href="https://arxiv.org/pdf/2505.23757.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23757v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23757v1', 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haohan Chi, Huan-ang Gao, Ziming Liu, Jianing Liu, Chenyu Liu, Jinwei Li, Kaisen Yang, Yangcheng Yu, Zeda Wang, Wenyi Li, Leichen Wang, Xingtao Hu, Hao Sun, Hang Zhao, Hao Zhao

**分类**: cs.CV

**发布日期**: 2025-05-29

**备注**: Project page: https://github.com/ahydchh/Impromptu-VLA

**🔗 代码/项目**: [GITHUB](https://github.com/ahydchh/Impromptu-VLA)

---

## 💡 一句话要点

**提出Impromptu VLA以解决自动驾驶中的视觉-语言-动作模型挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `自动驾驶` `多模态学习` `数据集构建` `性能提升`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在自动驾驶的非结构化场景中表现不佳，缺乏针对性的基准测试和数据集。
2. 论文提出了Impromptu VLA数据集，包含超过80,000个视频片段，并提供丰富的问答注释以支持模型训练。
3. 实验结果显示，使用该数据集训练的模型在NeuroNCAP评分和nuScenes轨迹预测中显著提升，达到了接近最先进的性能。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在自动驾驶中展现出潜力，但在非结构化的边缘案例场景中表现不佳，主要由于缺乏针对性的基准测试。为此，我们提出了Impromptu VLA。我们的核心贡献是Impromptu VLA数据集：该数据集包含超过80,000个精心策划的视频片段，源自8个开源大规模数据集中的200万源片段。该数据集基于我们新颖的四类挑战性非结构化分类法，并提供丰富的规划导向问答注释和动作轨迹。实验表明，使用我们数据集训练的VLA在现有基准测试中取得了显著的性能提升，改善了闭环NeuroNCAP评分和碰撞率，并在开放环nuScenes轨迹预测中达到了接近最先进的L2准确率。此外，我们的问答套件作为有效的诊断工具，揭示了VLM在感知、预测和规划方面的明显改进。我们的代码、数据和模型可在https://github.com/ahydchh/Impromptu-VLA获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视觉-语言-动作模型在自动驾驶中对非结构化场景的适应性不足的问题，特别是在缺乏针对性基准测试的情况下，模型的性能受到限制。

**核心思路**：通过构建Impromptu VLA数据集，提供丰富的多模态数据和问答注释，增强模型在复杂场景下的学习能力和泛化能力。

**技术框架**：整体架构包括数据采集、数据标注、模型训练和评估四个主要阶段。数据采集阶段从多个开源数据集中提取视频片段，标注阶段则为每个片段提供问答和动作轨迹信息。模型训练阶段使用这些数据进行训练，最后通过标准基准进行评估。

**关键创新**：Impromptu VLA数据集的构建是本研究的核心创新，特别是其针对性强的非结构化场景分类和丰富的问答注释，显著提升了模型的学习效果。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态学习效果，并在网络结构上进行了调整，以更好地融合视觉和语言信息。

## 📊 实验亮点

实验结果表明，使用Impromptu VLA数据集训练的视觉-语言-动作模型在闭环NeuroNCAP评分上显著提高，碰撞率降低，且在开放环nuScenes轨迹预测中达到了接近最先进的L2准确率，展示了数据集的有效性和模型的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能交通系统和机器人导航等。通过提升视觉-语言-动作模型在复杂场景下的表现，可以显著提高自动驾驶系统的安全性和可靠性，推动智能交通技术的发展。未来，Impromptu VLA数据集也可能为其他多模态学习任务提供参考和借鉴。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

