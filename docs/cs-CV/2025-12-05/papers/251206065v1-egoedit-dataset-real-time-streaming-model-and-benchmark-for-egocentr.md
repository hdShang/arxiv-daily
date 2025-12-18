---
layout: default
title: EgoEdit: Dataset, Real-Time Streaming Model, and Benchmark for Egocentric Video Editing
---

# EgoEdit: Dataset, Real-Time Streaming Model, and Benchmark for Egocentric Video Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06065" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06065v1</a>
  <a href="https://arxiv.org/pdf/2512.06065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06065v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.06065v1', 'EgoEdit: Dataset, Real-Time Streaming Model, and Benchmark for Egocentric Video Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runjia Li, Moayed Haji-Ali, Ashkan Mirzaei, Chaoyang Wang, Arpit Sahni, Ivan Skorokhodov, Aliaksandr Siarohin, Tomas Jakab, Junlin Han, Sergey Tulyakov, Philip Torr, Willi Menapace

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-05

**备注**: Project page: https://snap-research.github.io/EgoEdit

**🔗 代码/项目**: [PROJECT_PAGE](https://snap-research.github.io/EgoEdit)

---

## 💡 一句话要点

**EgoEdit：用于第一人称视频编辑的数据集、实时模型与评测基准**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `第一人称视频编辑` `指令引导编辑` `实时视频编辑` `数据集` `评测基准` `手部交互` `增强现实`

## 📋 核心要点

1. 现有视频编辑方法在第一人称视角下，由于快速运动和手部交互，效果不佳。
2. EgoEdit通过构建数据集、设计实时模型和评测基准，解决第一人称视频编辑难题。
3. 实验表明，EgoEdit在第一人称编辑任务上显著优于现有方法，并保持了实时性。

## 📝 摘要（中文）

本文研究了交互式AR应用中，指令引导的第一人称视频编辑。虽然现有的AI视频编辑器在第三人称素材上表现良好，但第一人称视角带来了独特的挑战，包括快速的自我运动和频繁的手部-物体交互，造成了显著的领域差距。此外，现有的离线编辑流程延迟较高，限制了实时交互。为了解决这些问题，本文提出了一个完整的第一人称视频编辑生态系统。首先，构建了EgoEditData，一个精心设计和手动策划的数据集，专门用于第一人称编辑场景，具有丰富的手部-物体交互，并明确保留了手部。其次，开发了EgoEdit，一个指令跟随的第一人称视频编辑器，支持在单个GPU上进行实时流推理。最后，引入了EgoEditBench，一个评估套件，针对指令保真度、手部和交互保留以及自我运动下的时间稳定性。在第一人称和通用编辑任务中，EgoEdit产生了时间稳定、指令保真的结果，并具有交互式延迟。它在第一人称编辑基准上取得了明显的优势，而现有方法难以胜任，同时在通用编辑任务上保持了与最强基线相当的性能。EgoEditData和EgoEditBench将向研究社区公开。

## 🔬 方法详解

**问题定义**：论文旨在解决第一人称视角视频的指令引导编辑问题。现有视频编辑方法主要针对第三人称视角，无法很好地处理第一人称视频中常见的快速自我运动、频繁手部-物体交互等复杂情况，导致编辑效果不佳，且延迟较高，难以满足实时交互需求。

**核心思路**：论文的核心思路是构建一个专门针对第一人称视频编辑的完整生态系统，包括数据集、实时模型和评测基准。通过高质量的数据集训练模型，并设计针对性的评估指标，从而提升模型在第一人称视频编辑任务上的性能和鲁棒性。

**技术框架**：EgoEdit的整体框架包含三个主要组成部分：EgoEditData数据集、EgoEdit实时编辑模型和EgoEditBench评测基准。EgoEditData提供高质量的第一人称视频数据，用于模型训练。EgoEdit模型基于流式处理架构，支持实时推理。EgoEditBench用于评估模型在指令保真度、手部和交互保留以及时间稳定性等方面的性能。

**关键创新**：论文的关键创新在于构建了专门针对第一人称视频编辑的数据集EgoEditData，该数据集包含丰富的手部-物体交互，并明确保留了手部信息。此外，论文还提出了EgoEditBench评测基准，用于全面评估模型在第一人称视频编辑任务上的性能。

**关键设计**：EgoEdit模型采用了流式处理架构，以实现实时推理。具体的技术细节，例如网络结构、损失函数等，论文中没有详细描述，属于未知信息。数据集EgoEditData的构建过程中，作者进行了精心的设计和手动策划，以保证数据的质量和多样性。评测基准EgoEditBench则针对第一人称视频编辑的特点，设计了多个评估指标，包括指令保真度、手部和交互保留以及时间稳定性。

## 📊 实验亮点

EgoEdit在第一人称编辑基准上取得了显著的性能提升，超越了现有方法。在通用编辑任务上，EgoEdit保持了与最强基线相当的性能，同时实现了实时推理。EgoEditData和EgoEditBench的发布将为第一人称视频编辑领域的研究提供有力支持。

## 🎯 应用场景

该研究成果可应用于增强现实(AR)应用、机器人控制、虚拟现实(VR)内容创作等领域。例如，用户可以通过语音指令实时编辑第一人称视角下的视频，实现虚拟物体的添加、场景的修改等功能。该技术有望提升用户在AR/VR环境中的交互体验，并为机器人提供更智能的视觉感知能力。

## 📄 摘要（原文）

> We study instruction-guided editing of egocentric videos for interactive AR applications. While recent AI video editors perform well on third-person footage, egocentric views present unique challenges - including rapid egomotion and frequent hand-object interactions - that create a significant domain gap. Moreover, existing offline editing pipelines suffer from high latency, limiting real-time interaction. To address these issues, we present a complete ecosystem for egocentric video editing. First, we construct EgoEditData, a carefully designed and manually curated dataset specifically designed for egocentric editing scenarios, featuring rich hand-object interactions, while explicitly preserving hands. Second, we develop EgoEdit, an instruction-following egocentric video editor that supports real-time streaming inference on a single GPU. Finally, we introduce EgoEditBench, an evaluation suite targeting instruction faithfulness, hand and interaction preservation, and temporal stability under egomotion. Across both egocentric and general editing tasks, EgoEdit produces temporally stable, instruction-faithful results with interactive latency. It achieves clear gains on egocentric editing benchmarks-where existing methods struggle-while maintaining performance comparable to the strongest baselines on general editing tasks. EgoEditData and EgoEditBench will be made public for the research community. See our website at https://snap-research.github.io/EgoEdit

