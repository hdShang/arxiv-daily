---
layout: default
title: How Do VLAs Effectively Inherit from VLMs?
---

# How Do VLAs Effectively Inherit from VLMs?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06619" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06619v1</a>
  <a href="https://arxiv.org/pdf/2511.06619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06619v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06619v1', 'How Do VLAs Effectively Inherit from VLMs?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuheng Zhang, Rushuai Yang, Xiaoyu Chen, Kaixin Wang, Li Zhao, Yi Chen, Jiang Bian

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-10

---

## 💡 一句话要点

**提出GrinningFace基准，诊断VLA模型从VLM有效继承知识的能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉语言动作模型` `知识迁移` `具身智能` `机器人操作` `诊断基准`

## 📋 核心要点

1. VLA模型依赖VLM的先验知识，但如何有效继承这些知识仍是挑战，现有机器人数据集缺乏VLM预训练中常见的语义信息。
2. 论文提出GrinningFace基准，利用机器人操作emoji的任务，评估VLA模型从VLM迁移知识的能力，emoji作为VLM知识的代理。
3. 通过在模拟和真实机器人环境中的实验，系统评估了多种知识迁移技术，为VLA模型的泛化能力提供了指导。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型有望实现通用具身控制。一种常见范式是利用大型视觉-语言模型(VLM)丰富的视觉-语义先验知识。然而，一个根本问题依然存在：VLA如何有效地继承VLM的先验知识？为了解决这个关键问题，我们引入了一个诊断基准GrinningFace，这是一个emoji桌面操作任务，要求机器人手臂将物体放置到与语言指令相对应的打印emoji上。这种任务设计特别具有启发性——与emoji相关的知识在用于VLM预训练的互联网规模数据集中无处不在，但emoji本身在标准机器人数据集中却基本不存在。因此，它们提供了一个清晰的代理：成功完成任务表明VLM先验知识已有效转移到具身控制。我们在模拟环境和真实机器人中都实现了这个诊断任务，并比较了各种有前景的知识转移技术。具体来说，我们研究了参数高效微调、VLM冻结、协同训练、预测离散动作和预测潜在动作的效果。通过系统评估，我们的工作不仅证明了保留VLM先验知识对于VLA泛化的重要性，而且为未来开发真正通用的具身AI系统奠定了基础。

## 🔬 方法详解

**问题定义**：VLA模型旨在实现通用具身控制，但如何有效利用VLM中预训练的知识是一个关键问题。现有方法在将VLM知识迁移到VLA时，缺乏有效的评估和诊断工具，难以理解哪些知识被成功迁移，以及哪些迁移策略更有效。标准机器人数据集通常不包含VLM预训练中常见的语义信息，这使得评估VLA模型对新概念的泛化能力变得困难。

**核心思路**：论文的核心思路是设计一个诊断基准，该基准能够清晰地反映VLA模型从VLM继承知识的能力。通过引入包含VLM预训练知识但机器人数据集缺乏的元素（即emoji），可以创建一个“知识代理”，成功完成基于emoji的任务表明VLA模型已有效利用VLM的先验知识。

**技术框架**：整体框架包括以下几个关键部分：1) **GrinningFace基准**：定义了emoji桌面操作任务，要求机器人根据语言指令将物体放置到对应的emoji上。2) **模拟环境和真实机器人平台**：在两种环境下实现该基准，以评估不同知识迁移策略的有效性。3) **多种知识迁移技术**：比较了参数高效微调、VLM冻结、协同训练、预测离散动作和预测潜在动作等方法。4) **系统评估**：通过实验分析不同方法在GrinningFace基准上的性能，从而为VLA模型的知识迁移提供指导。

**关键创新**：该论文最重要的创新点在于提出了GrinningFace基准，它提供了一种新的视角来评估VLA模型从VLM继承知识的能力。与现有方法相比，GrinningFace基准能够更清晰地诊断VLA模型对VLM先验知识的利用情况，并为知识迁移策略的选择提供依据。

**关键设计**：GrinningFace基准的关键设计在于选择emoji作为知识代理。Emoji在互联网规模的数据集中广泛存在，VLM在预训练过程中已经学习了相关的语义知识。然而，emoji在标准机器人数据集中却很少出现，这使得GrinningFace基准能够清晰地评估VLA模型对VLM先验知识的泛化能力。此外，论文还探索了不同的动作表示方法（离散动作和潜在动作），以及不同的训练策略（参数高效微调、VLM冻结、协同训练），以研究它们对知识迁移的影响。

## 📊 实验亮点

实验结果表明，保留VLM的先验知识对于VLA模型的泛化至关重要。通过GrinningFace基准的评估，论文比较了不同知识迁移策略的性能，为未来VLA模型的设计提供了指导。具体性能数据未知，但论文强调了系统评估的重要性，并为未来的研究方向提供了明确的建议。

## 🎯 应用场景

该研究成果可应用于机器人通用技能学习、智能家居服务机器人、自动化装配等领域。通过有效继承VLM的知识，机器人能够更好地理解人类指令，完成更复杂的任务，并具备更强的泛化能力。未来，该研究可以推动具身智能的发展，使机器人能够更好地适应真实世界环境。

## 📄 摘要（原文）

> Vision-language-action (VLA) models hold the promise to attain generalizable embodied control. To achieve this, a pervasive paradigm is to leverage the rich vision-semantic priors of large vision-language models (VLMs). However, the fundamental question persists: How do VLAs effectively inherit the prior knowledge from VLMs? To address this critical question, we introduce a diagnostic benchmark, GrinningFace, an emoji tabletop manipulation task where the robot arm is asked to place objects onto printed emojis corresponding to language instructions. This task design is particularly revealing -- knowledge associated with emojis is ubiquitous in Internet-scale datasets used for VLM pre-training, yet emojis themselves are largely absent from standard robotics datasets. Consequently, they provide a clean proxy: successful task completion indicates effective transfer of VLM priors to embodied control. We implement this diagnostic task in both simulated environment and a real robot, and compare various promising techniques for knowledge transfer. Specifically, we investigate the effects of parameter-efficient fine-tuning, VLM freezing, co-training, predicting discretized actions, and predicting latent actions. Through systematic evaluation, our work not only demonstrates the critical importance of preserving VLM priors for the generalization of VLA but also establishes guidelines for future research in developing truly generalizable embodied AI systems.

