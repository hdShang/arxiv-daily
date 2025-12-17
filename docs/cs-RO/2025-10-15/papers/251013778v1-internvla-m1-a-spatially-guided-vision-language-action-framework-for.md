---
layout: default
title: InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy
---

# InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13778" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13778v1</a>
  <a href="https://arxiv.org/pdf/2510.13778.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13778v1" onclick="toggleFavorite(this, '2510.13778v1', 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyi Chen, Yilun Chen, Yanwei Fu, Ning Gao, Jiaya Jia, Weiyang Jin, Hao Li, Yao Mu, Jiangmiao Pang, Yu Qiao, Yang Tian, Bin Wang, Bolun Wang, Fangjing Wang, Hanqing Wang, Tai Wang, Ziqin Wang, Xueyuan Wei, Chao Wu, Shuai Yang, Jinhui Ye, Junqiu Yu, Jia Zeng, Jingjing Zhang, Jinyu Zhang, Shi Zhang, Feng Zheng, Bowen Zhou, Yangkun Zhu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-15

**备注**: Technical report

**🔗 代码/项目**: [GITHUB](https://github.com/InternRobotics/InternVLA-M1)

---

## 💡 一句话要点

**InternVLA-M1：面向通用机器人策略的空间引导视觉-语言-动作框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `视觉语言动作` `空间推理` `指令跟随` `通用机器人`

## 📋 核心要点

1. 现有指令跟随机器人难以泛化到复杂环境和任务，缺乏对空间信息的有效利用。
2. 提出空间引导的视觉-语言-动作框架InternVLA-M1，通过空间定位连接指令和动作，提升泛化能力。
3. 实验表明，InternVLA-M1在多个机器人平台和任务上显著优于现有方法，尤其在长时程推理中。

## 📝 摘要（中文）

本文提出了InternVLA-M1，一个统一的空间定位和机器人控制框架，旨在推动指令跟随机器人向可扩展的通用智能发展。其核心思想是空间引导的视觉-语言-动作训练，其中空间定位作为指令和机器人动作之间的关键连接。InternVLA-M1采用两阶段流程：（i）在超过230万个空间推理数据上进行空间定位预训练，通过将指令与视觉、与具体实施无关的位置对齐来确定“在哪里行动”；（ii）进行空间引导的动作后训练，通过即插即用的空间提示生成与具体实施相关的动作，从而决定“如何行动”。这种空间引导的训练方法带来了持续的收益：InternVLA-M1在SimplerEnv Google Robot上优于没有空间引导的变体+14.6%，在WidowX上+17%，在LIBERO Franka上+4.3%，同时在盒子、点和轨迹预测中表现出更强的空间推理能力。为了进一步扩展指令跟随，我们构建了一个仿真引擎来收集24.4万个可泛化的抓取和放置片段，从而在200个任务和3000多个对象上实现了平均6.2%的改进。在真实世界的集群抓取和放置中，InternVLA-M1提高了7.3%，通过合成协同训练，在未见过的对象和新配置上实现了+20.6%。此外，在长时程推理密集型场景中，它超过了现有工作10%以上。这些结果表明，空间引导训练是可扩展和有弹性的通用机器人的统一原则。

## 🔬 方法详解

**问题定义**：现有指令跟随机器人策略在处理复杂任务和环境时，泛化能力不足。它们通常难以有效地理解和利用空间信息，导致在需要精确定位和操作的任务中表现不佳。现有方法往往依赖于大量特定任务的数据，难以扩展到新的场景和机器人平台。

**核心思路**：InternVLA-M1的核心思路是利用空间引导作为连接指令和机器人动作的关键桥梁。通过显式地学习指令与视觉空间位置之间的对应关系，模型能够更好地理解“在哪里行动”，从而更准确地执行任务。这种空间引导的训练方法旨在提高模型的泛化能力，使其能够适应不同的环境和机器人平台。

**技术框架**：InternVLA-M1采用两阶段训练流程。第一阶段是空间定位预训练，模型在大规模空间推理数据集上学习将指令与视觉空间位置对齐。第二阶段是空间引导的动作后训练，模型利用预训练的空间定位能力，通过空间提示生成与具体机器人相关的动作。整体架构包含视觉编码器、语言编码器、空间定位模块和动作生成模块。

**关键创新**：InternVLA-M1最重要的技术创新在于其空间引导的训练方法。与传统的端到端训练方法不同，InternVLA-M1显式地学习空间信息，并将其作为指导动作生成的重要线索。这种方法使得模型能够更好地理解指令的意图，并生成更准确的动作。此外，该框架采用即插即用的空间提示，使得模型能够轻松地适应不同的机器人平台。

**关键设计**：空间定位预训练使用对比学习损失，鼓励模型将相似的指令和空间位置映射到相近的嵌入空间。动作后训练使用行为克隆损失，鼓励模型模仿专家轨迹。网络结构采用Transformer架构，用于处理视觉和语言信息。空间提示通过将空间位置信息嵌入到动作生成模块中，引导动作的生成。

## 📊 实验亮点

InternVLA-M1在SimplerEnv Google Robot上相比无空间引导的变体提升了14.6%，在WidowX上提升了17%，在LIBERO Franka上提升了4.3%。在真实世界的集群抓取和放置任务中，InternVLA-M1提高了7.3%，通过合成协同训练，在未见过的对象和新配置上实现了20.6%的提升。在长时程推理密集型场景中，它超过了现有工作10%以上。

## 🎯 应用场景

InternVLA-M1具有广泛的应用前景，可用于各种需要指令跟随和空间推理的机器人任务，如家庭服务机器人、工业自动化机器人和医疗辅助机器人。该研究有助于实现更智能、更通用的机器人，从而提高生产效率和服务质量。未来，该技术有望应用于更复杂的任务，如自主导航、环境探索和人机协作。

## 📄 摘要（原文）

> We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

