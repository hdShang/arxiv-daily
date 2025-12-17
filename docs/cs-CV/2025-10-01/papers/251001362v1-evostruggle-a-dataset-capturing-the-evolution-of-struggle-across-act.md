---
layout: default
title: EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels
---

# EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01362" target="_blank" class="toolbar-btn">arXiv: 2510.01362v1</a>
    <a href="https://arxiv.org/pdf/2510.01362.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01362v1" 
            onclick="toggleFavorite(this, '2510.01362v1', 'EvoStruggle: A Dataset Capturing the Evolution of Struggle across Activities and Skill Levels')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Shijia Feng, Michael Wray, Walterio Mayol-Cuevas

**分类**: cs.CV

**发布日期**: 2025-10-01

**备注**: 10 pages

**🔗 代码/项目**: [GITHUB](https://github.com/FELIXFENG2019/EvoStruggle)

---

## 💡 一句话要点

**EvoStruggle：构建技能学习过程中挣扎演变数据集，用于提升辅助系统性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `挣扎检测` `技能学习` `时间动作定位` `数据集` `行为识别`

## 📋 核心要点

1. 现有操作数据集缺乏对技能学习中挣扎演变的关注，限制了对学习阶段的判断。
2. EvoStruggle数据集通过记录参与者重复任务过程中的挣扎行为，捕捉技能演变。
3. 实验表明，时间动作定位模型能有效检测挣扎，但跨活动泛化仍具挑战。

## 📝 摘要（中文）

本文提出了一个用于挣扎判断的数据集EvoStruggle，旨在捕捉技能习得过程中挣扎行为的演变。该数据集包含61.68小时的视频记录，共2793个视频，以及来自76名参与者的5385个带时间戳的挣扎片段标注。数据集涵盖了18个任务，分为四类活动：绳结、折纸、七巧板和洗牌，代表了不同的任务类型。参与者重复每个任务五次，以记录技能演变过程。作者将挣扎判断问题定义为时间动作定位任务，专注于识别和精确定位挣扎片段的起始和结束时间。实验结果表明，时间动作定位模型可以成功学习检测挣扎线索，即使在未见过的任务或活动上进行评估。模型在跨任务泛化时达到34.56%的平均mAP，在跨活动泛化时达到19.24%，表明挣扎是一个可以在各种技能任务中转移的概念，同时也表明挣扎检测仍面临挑战，有待进一步改进。数据集已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决技能学习过程中，如何准确判断学习者是否遇到困难（即“挣扎”）的问题。现有数据集通常关注动作识别或操作流程，缺乏对挣扎行为随技能提升而变化的细致刻画。因此，现有方法难以有效识别学习者所处的学习阶段，从而无法提供个性化的辅助指导。

**核心思路**：论文的核心思路是通过构建一个包含技能演变过程的数据集，使模型能够学习到挣扎行为的动态变化模式。具体而言，参与者需要重复执行一系列任务，每次执行都可能表现出不同类型的挣扎行为，这些行为与他们的技能水平密切相关。通过对这些挣扎行为进行标注，模型可以学习到挣扎与技能水平之间的对应关系。

**技术框架**：整体框架围绕EvoStruggle数据集的构建和评估展开。首先，设计了包含四类活动（绳结、折纸、七巧板、洗牌）的18个任务，并招募参与者重复执行这些任务。然后，对视频数据进行标注，标注出每个视频中包含的挣扎片段的起始和结束时间。最后，使用时间动作定位模型在数据集上进行训练和评估，验证模型检测挣扎行为的能力。

**关键创新**：该论文的关键创新在于构建了一个专门用于研究技能学习过程中挣扎演变的数据集。与现有数据集相比，EvoStruggle数据集更加关注挣扎行为的时间动态性，并提供了丰富的标注信息。此外，论文还验证了时间动作定位模型在挣扎检测任务上的有效性，为未来的研究提供了基准。

**关键设计**：数据集包含18个任务，每个任务重复5次，以捕捉技能演变。使用时间动作定位模型进行训练，将挣扎检测视为一个时间动作定位问题。评估指标采用平均精度均值（mAP），用于衡量模型检测挣扎片段的准确性。

## 📊 实验亮点

实验结果表明，时间动作定位模型在EvoStruggle数据集上表现出一定的挣扎检测能力。在跨任务泛化时，模型达到了34.56%的平均mAP；在跨活动泛化时，模型达到了19.24%的平均mAP。虽然跨活动泛化性能较低，但也表明挣扎是一个可以在不同技能任务中转移的概念。这些结果为未来的挣扎检测研究提供了基准。

## 🎯 应用场景

该研究成果可应用于智能教学系统、康复训练、人机协作等领域。通过准确识别学习者的挣扎行为，系统可以提供个性化的指导和反馈，帮助学习者更快地掌握技能。在康复训练中，可以监测患者的动作执行情况，及时发现并纠正错误动作。在人机协作中，机器人可以感知人类的困难，并提供必要的帮助。

## 📄 摘要（原文）

> The ability to determine when a person struggles during skill acquisition is crucial for both optimizing human learning and enabling the development of effective assistive systems. As skills develop, the type and frequency of struggles tend to change, and understanding this evolution is key to determining the user's current stage of learning. However, existing manipulation datasets have not focused on how struggle evolves over time. In this work, we collect a dataset for struggle determination, featuring 61.68 hours of video recordings, 2,793 videos, and 5,385 annotated temporal struggle segments collected from 76 participants. The dataset includes 18 tasks grouped into four diverse activities -- tying knots, origami, tangram puzzles, and shuffling cards, representing different task variations. In addition, participants repeated the same task five times to capture their evolution of skill. We define the struggle determination problem as a temporal action localization task, focusing on identifying and precisely localizing struggle segments with start and end times. Experimental results show that Temporal Action Localization models can successfully learn to detect struggle cues, even when evaluated on unseen tasks or activities. The models attain an overall average mAP of 34.56% when generalizing across tasks and 19.24% across activities, indicating that struggle is a transferable concept across various skill-based tasks while still posing challenges for further improvement in struggle detection. Our dataset is available at https://github.com/FELIXFENG2019/EvoStruggle.

