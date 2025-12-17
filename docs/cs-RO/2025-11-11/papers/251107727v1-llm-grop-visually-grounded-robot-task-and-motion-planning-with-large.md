---
layout: default
title: LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models
---

# LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07727" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07727v1</a>
  <a href="https://arxiv.org/pdf/2511.07727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07727v1" onclick="toggleFavorite(this, '2511.07727v1', 'LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaohan Zhang, Yan Ding, Yohei Hayamizu, Zainab Altaweel, Yifeng Zhu, Yuke Zhu, Peter Stone, Chris Paxton, Shiqi Zhang

**分类**: cs.RO

**发布日期**: 2025-11-11

**期刊**: The International Journal of Robotics Research, 2025, Vol. 0(0), pp. 1-19

**DOI**: [10.1177/02783649251378196](https://doi.org/10.1177/02783649251378196)

---

## 💡 一句话要点

**LLM-GROP：利用大语言模型实现视觉引导的机器人任务与运动规划**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人` `任务与运动规划` `大语言模型` `视觉引导` `移动操作` `常识推理` `物体重排列`

## 📋 核心要点

1. 移动操作（MoMa）中的任务与运动规划（TAMP）需要交错导航和操作动作，现有方法难以有效利用常识知识。
2. LLM-GROP利用LLM的常识知识辅助任务级和运动级规划，并结合视觉方法学习机器人基座位置选择策略。
3. 实验表明，该方法在真实和模拟环境中均能有效完成长时程物体重排列任务，成功率达到84.4%。

## 📝 摘要（中文）

本文提出了一种基于大语言模型（LLM）的视觉引导机器人任务与运动规划（TAMP）框架，用于解决多物体移动操作（MoMa）问题。该框架利用LLM丰富的常识知识，例如餐具的摆放方式，来辅助任务级和运动级规划。此外，利用计算机视觉方法学习选择机器人基座位置的策略，以促进MoMa行为。该框架适用于包含多个待移动物体的新场景。在真实环境和模拟环境中进行了定量实验，评估了完成长时程物体重排列任务的成功率和效率。实验结果表明，机器人完成了84.4%的真实物体重排列试验，但主观人类评估表明，机器人的性能仍低于经验丰富的人类服务员。

## 🔬 方法详解

**问题定义**：论文旨在解决移动操作（MoMa）场景下的任务与运动规划（TAMP）问题，特别是涉及多个物体重排列的复杂任务。现有方法在处理此类问题时，难以有效利用常识知识，导致规划效率低下或无法生成合理的解决方案。例如，如何根据“摆放餐桌”这一高层指令，合理地安排餐具的位置和顺序，并规划出可行的机器人运动轨迹。

**核心思路**：论文的核心思路是利用大语言模型（LLM）蕴含的丰富常识知识，来指导任务级和运动级规划。LLM可以提供关于物体之间关系的先验知识，例如餐具的摆放规则，从而帮助机器人更好地理解任务目标并生成合理的规划方案。此外，论文还结合计算机视觉技术，学习选择机器人基座位置的策略，以优化机器人的运动效率。

**技术框架**：LLM-GROP框架主要包含以下几个模块：1) **LLM常识推理模块**：利用LLM对任务目标进行解析，提取物体之间的关系和约束，生成任务级的规划方案。2) **视觉感知模块**：利用计算机视觉技术感知环境中的物体信息，包括物体的位置、形状和类别等。3) **基座位置选择模块**：学习选择合适的机器人基座位置，以优化机器人的运动效率和操作能力。4) **运动规划模块**：根据任务级规划方案和视觉感知信息，生成可行的机器人运动轨迹。这些模块协同工作，实现端到端的任务与运动规划。

**关键创新**：该论文的关键创新在于将大语言模型（LLM）的常识知识引入到机器人任务与运动规划中。与传统的基于规则或优化的TAMP方法相比，LLM-GROP能够更好地理解任务目标，并生成更符合人类常识的规划方案。此外，论文还提出了一种基于视觉的基座位置选择策略，进一步提高了机器人的运动效率。

**关键设计**：论文中一个关键的设计是利用LLM生成物体之间的关系图，该图表示了物体之间的依赖关系和约束。例如，在“摆放餐桌”任务中，LLM可以生成一个关系图，表示盘子应该放在桌子上，刀叉应该放在盘子旁边等。该关系图被用于指导任务级规划和运动规划，确保生成的规划方案符合人类常识。此外，基座位置选择模块采用深度学习方法，通过学习大量的训练数据，预测最佳的机器人基座位置。

## 📊 实验亮点

实验结果表明，LLM-GROP在真实环境和模拟环境中均能有效完成长时程物体重排列任务。在真实环境中，机器人完成了84.4%的物体重排列试验。主观人类评估表明，虽然机器人的性能仍低于经验丰富的人类服务员，但已经展现出良好的应用潜力。该研究证明了利用LLM辅助机器人任务与运动规划的可行性和有效性。

## 🎯 应用场景

该研究成果可应用于各种需要机器人进行物体重排列的场景，例如家庭服务、餐厅服务、仓储物流等。通过利用LLM的常识知识，机器人可以更好地理解人类指令，并完成复杂的任务。未来，该技术有望进一步推广到更广泛的机器人应用领域，例如智能制造、医疗服务等。

## 📄 摘要（原文）

> Task planning and motion planning are two of the most important problems in robotics, where task planning methods help robots achieve high-level goals and motion planning methods maintain low-level feasibility. Task and motion planning (TAMP) methods interleave the two processes of task planning and motion planning to ensure goal achievement and motion feasibility. Within the TAMP context, we are concerned with the mobile manipulation (MoMa) of multiple objects, where it is necessary to interleave actions for navigation and manipulation.
>   In particular, we aim to compute where and how each object should be placed given underspecified goals, such as ``set up dinner table with a fork, knife and plate.'' We leverage the rich common sense knowledge from large language models (LLMs), e.g., about how tableware is organized, to facilitate both task-level and motion-level planning. In addition, we use computer vision methods to learn a strategy for selecting base positions to facilitate MoMa behaviors, where the base position corresponds to the robot's ``footprint'' and orientation in its operating space. Altogether, this article provides a principled TAMP framework for MoMa tasks that accounts for common sense about object rearrangement and is adaptive to novel situations that include many objects that need to be moved. We performed quantitative experiments in both real-world settings and simulated environments. We evaluated the success rate and efficiency in completing long-horizon object rearrangement tasks. While the robot completed 84.4\% real-world object rearrangement trials, subjective human evaluations indicated that the robot's performance is still lower than experienced human waiters.

