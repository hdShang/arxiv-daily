---
layout: default
title: MaskCaptioner: Learning to Jointly Segment and Caption Object Trajectories in Videos
---

# MaskCaptioner: Learning to Jointly Segment and Caption Object Trajectories in Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14904" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14904v2</a>
  <a href="https://arxiv.org/pdf/2510.14904.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14904v2" onclick="toggleFavorite(this, '2510.14904v2', 'MaskCaptioner: Learning to Jointly Segment and Caption Object Trajectories in Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Fiastre, Antoine Yang, Cordelia Schmid

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-16 (更新: 2025-10-30)

**备注**: 20 pages, 8 figures

---

## 💡 一句话要点

**提出MaskCaptioner，通过联合学习分割和描述视频中的物体轨迹，实现端到端的密集视频物体描述。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `密集视频物体描述` `视频理解` `视觉语言模型` `端到端学习` `联合训练`

## 📋 核心要点

1. 密集视频物体描述(DVOC)任务复杂且标注成本高，现有方法采用分离训练策略，性能受限。
2. 论文提出MaskCaptioner，利用VLM生成时空局部实体的描述，并扩展数据集进行联合训练。
3. MaskCaptioner在VidSTG、VLN和BenSMOT等基准测试中取得了最先进的DVOC结果，验证了方法的有效性。

## 📝 摘要（中文）

密集视频物体描述(DVOC)任务旨在联合检测、跟踪和描述视频中的物体轨迹，这需要理解时空细节并用自然语言描述它们的能力。由于任务的复杂性和手动标注的高成本，以往的方法通常采用分离的训练策略，可能导致次优的性能。为了解决这个问题，我们提出利用最先进的VLM生成关于时空局部实体的描述。通过使用我们的合成描述扩展LVIS和LV-VIS数据集（LVISCap和LV-VISCap），我们训练了MaskCaptioner，一个能够联合检测、分割、跟踪和描述物体轨迹的端到端模型。此外，通过在LVISCap和LV-VISCap上进行预训练，MaskCaptioner在三个现有的基准测试VidSTG、VLN和BenSMOT上取得了最先进的DVOC结果。数据集和代码可在https://www.gabriel.fiastre.fr/maskcaptioner/ 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决密集视频物体描述（DVOC）任务，即在视频中同时检测、跟踪和描述物体轨迹。现有方法的痛点在于，由于任务的复杂性和标注成本高昂，通常采用分离的训练策略，例如先检测和跟踪，再进行描述，这导致各个模块之间缺乏有效的联合优化，从而限制了整体性能的提升。

**核心思路**：论文的核心思路是利用大规模视觉语言模型（VLM）的强大能力，生成关于时空局部实体的描述，并以此扩展现有的数据集。通过构建包含物体分割、跟踪和描述信息的合成数据，实现端到端的联合训练。这样可以避免分离训练带来的次优问题，充分利用各个模块之间的关联性，提升整体性能。

**技术框架**：MaskCaptioner的整体框架是一个端到端的模型，它接收视频作为输入，输出包含物体分割、跟踪和描述信息的轨迹。该框架主要包含以下几个模块：1) 物体检测和分割模块：负责检测视频中的物体并生成分割掩码。2) 物体跟踪模块：负责跟踪视频中物体的运动轨迹。3) 描述生成模块：利用VLM生成关于物体轨迹的自然语言描述。4) 联合训练模块：将上述三个模块进行端到端的联合训练，优化整体性能。

**关键创新**：论文最重要的技术创新点在于提出了一个端到端的联合训练框架MaskCaptioner，能够同时进行物体检测、分割、跟踪和描述。与现有方法相比，MaskCaptioner避免了分离训练带来的次优问题，实现了各个模块之间的有效协同。此外，论文还通过利用VLM生成合成数据，有效缓解了DVOC任务中数据标注成本高昂的问题。

**关键设计**：论文的关键设计包括：1) 利用LVIS和LV-VIS数据集，并使用VLM生成合成描述，构建了LVISCap和LV-VISCap数据集。2) 采用Mask R-CNN作为物体检测和分割模块的基础架构。3) 使用Transformer架构作为描述生成模块的基础架构。4) 设计了合适的损失函数，用于联合优化物体检测、分割、跟踪和描述任务。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

MaskCaptioner在VidSTG、VLN和BenSMOT三个基准测试中取得了最先进的DVOC结果。例如，在VidSTG数据集上，MaskCaptioner的性能显著优于现有方法，证明了其有效性。通过在LVISCap和LV-VISCap上进行预训练，模型性能得到进一步提升。

## 🎯 应用场景

该研究成果可应用于智能视频监控、自动驾驶、机器人导航等领域。例如，在智能视频监控中，可以自动识别和描述视频中的异常行为。在自动驾驶中，可以帮助车辆理解周围环境，并做出更安全的决策。在机器人导航中，可以帮助机器人理解任务指令，并完成复杂的任务。

## 📄 摘要（原文）

> Dense Video Object Captioning (DVOC) is the task of jointly detecting, tracking, and captioning object trajectories in a video, requiring the ability to understand spatio-temporal details and describe them in natural language. Due to the complexity of the task and the high cost associated with manual annotation, previous approaches resort to disjoint training strategies, potentially leading to suboptimal performance. To circumvent this issue, we propose to generate captions about spatio-temporally localized entities leveraging a state-of-the-art VLM. By extending the LVIS and LV-VIS datasets with our synthetic captions (LVISCap and LV-VISCap), we train MaskCaptioner, an end-to-end model capable of jointly detecting, segmenting, tracking and captioning object trajectories. Moreover, with pretraining on LVISCap and LV-VISCap, MaskCaptioner achieves state-of-the-art DVOC results on three existing benchmarks, VidSTG, VLN and BenSMOT. The datasets and code are available at https://www.gabriel.fiastre.fr/maskcaptioner/.

