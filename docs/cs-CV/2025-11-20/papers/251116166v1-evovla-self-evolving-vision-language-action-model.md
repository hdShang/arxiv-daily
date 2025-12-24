---
layout: default
title: "EvoVLA: Self-Evolving Vision-Language-Action Model"
---

# EvoVLA: Self-Evolving Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16166" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16166v1</a>
  <a href="https://arxiv.org/pdf/2511.16166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16166v1', 'EvoVLA: Self-Evolving Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeting Liu, Zida Yang, Zeyu Zhang, Hao Tang

**分类**: cs.CV

**发布日期**: 2025-11-20

**🔗 代码/项目**: [GITHUB](https://github.com/AIGeeksGroup/EvoVLA) | [PROJECT_PAGE](https://aigeeksgroup.github.io/EvoVLA)

---

## 💡 一句话要点

**EvoVLA：一种自进化视觉-语言-动作模型，解决长时程机器人操作中的阶段幻觉问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言-动作模型` `机器人操作` `长时程任务` `自监督学习` `阶段幻觉` `对比学习` `sim-to-real`

## 📋 核心要点

1. 现有VLA模型在长时程机器人操作中存在阶段幻觉问题，即利用粗糙的评估信号来跳过多步骤任务。
2. EvoVLA通过阶段对齐奖励、基于姿态的物体探索和长时程记忆三个组件，解决阶段幻觉问题，提升长时程操作性能。
3. EvoVLA在模拟和真实机器人实验中均优于现有方法，证明了其有效性和泛化能力。

## 📝 摘要（中文）

本文提出EvoVLA，一种自监督的视觉-语言-动作（VLA）框架，旨在解决长时程机器人操作中存在的阶段幻觉问题。该框架包含三个互补组件：阶段对齐奖励（SAR），通过与Gemini生成的困难负样本进行三元组对比学习来防止视觉捷径；基于姿态的物体探索（POE），将好奇心建立在相对物体-夹爪姿态上，而非原始像素；以及长时程记忆，利用选择性上下文保留和门控融合来稳定扩展rollout期间的内在塑造。在Discoverse-L基准测试中，EvoVLA比最强的基线（OpenVLA-OFT）平均任务成功率提高了10.2个百分点，达到69.2%。EvoVLA的样本效率提高了1.5倍，阶段幻觉从38.5%降低到14.8%。在物理机器人上的真实世界部署中，EvoVLA在四个操作任务上的平均成功率为54.6%，超过OpenVLA-OFT 11个百分点，证明了有效的sim-to-real迁移和强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在长时程机器人操作任务中，容易出现“阶段幻觉”问题。这意味着智能体为了获得更高的奖励，会利用一些粗糙的视觉信号来“欺骗”系统，例如，在任务尚未真正完成时就报告很高的进度，从而导致任务失败。这种现象阻碍了VLA模型在复杂操作任务中的应用。

**核心思路**：EvoVLA的核心思路是通过自监督学习的方式，让模型更好地理解任务的真实进展，从而避免阶段幻觉。具体来说，它通过三个关键组件：阶段对齐奖励（SAR）、基于姿态的物体探索（POE）和长时程记忆，来分别解决视觉捷径、探索效率和长期依赖问题。

**技术框架**：EvoVLA的整体框架包含以下几个主要模块：1) 视觉编码器：用于提取场景的视觉特征。2) 语言编码器：用于理解任务指令。3) 动作解码器：根据视觉特征、语言指令和历史记忆生成动作。4) 阶段对齐奖励模块：通过对比学习，鼓励模型关注任务的真实进展。5) 基于姿态的物体探索模块：引导模型探索有意义的物体交互。6) 长时程记忆模块：存储和检索历史信息，帮助模型理解长期依赖关系。

**关键创新**：EvoVLA的关键创新在于其三个互补的组件：SAR通过Gemini生成的困难负样本进行对比学习，有效防止了视觉捷径；POE将好奇心建立在相对物体-夹爪姿态上，提高了探索效率；长时程记忆则通过选择性上下文保留和门控融合，稳定了长期rollout中的内在塑造。这些组件共同作用，显著降低了阶段幻觉，提升了长时程操作的性能。

**关键设计**：SAR使用三元组损失，其中正样本是任务的真实进展状态，负样本是Gemini生成的具有迷惑性的状态。POE使用相对物体-夹爪姿态作为探索的依据，避免了原始像素带来的噪声。长时程记忆使用GRU结构，并通过门控机制来控制信息的流入和流出。损失函数综合考虑了SAR、POE和任务奖励，并通过加权的方式进行平衡。

## 📊 实验亮点

EvoVLA在Discoverse-L基准测试中，相比最强基线OpenVLA-OFT，平均任务成功率提高了10.2个百分点，达到69.2%。同时，样本效率提高了1.5倍，阶段幻觉从38.5%降低到14.8%。在真实机器人实验中，EvoVLA在四个操作任务上的平均成功率为54.6%，超过OpenVLA-OFT 11个百分点，验证了其有效的sim-to-real迁移能力。

## 🎯 应用场景

EvoVLA在机器人操作领域具有广泛的应用前景，例如家庭服务机器人、工业自动化、医疗辅助机器人等。它可以帮助机器人更好地理解人类指令，完成复杂的长时程操作任务，提高工作效率和安全性。未来，EvoVLA可以进一步扩展到其他领域，例如自动驾驶、智能家居等，实现更智能、更自主的人机交互。

## 📄 摘要（原文）

> Long-horizon robotic manipulation remains challenging for Vision-Language-Action (VLA) models despite recent progress in zero-shot generalization and simulation-to-real-world transfer. Current VLA models suffer from stage hallucination, where agents exploit coarse evaluation signals to shortcut multi-step tasks, reporting high progress without truly completing them. We present EvoVLA, a self-supervised VLA framework that addresses this issue through three complementary components: Stage-Aligned Reward (SAR), which uses triplet contrastive learning with Gemini-generated hard negatives to prevent visual shortcuts; Pose-Based Object Exploration (POE), which grounds curiosity in relative object-gripper pose instead of raw pixels; and Long-Horizon Memory, which uses selective context retention and gated fusion to stabilize intrinsic shaping during extended rollouts. Extensive evaluations on Discoverse-L, a long-horizon manipulation benchmark with three multi-stage tasks, show that EvoVLA improves average task success by 10.2 percentage points over the strongest baseline (OpenVLA-OFT), reaching 69.2 percent. EvoVLA also achieves one-and-a-half times better sample efficiency and reduces stage hallucination from 38.5 percent to 14.8 percent. Real-world deployment on physical robots reaches an average success rate of 54.6 percent across four manipulation tasks, outperforming OpenVLA-OFT by 11 points, demonstrating effective sim-to-real transfer and strong generalization. Code: https://github.com/AIGeeksGroup/EvoVLA. Website: https://aigeeksgroup.github.io/EvoVLA.

