---
layout: default
title: DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation
---

# DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11258" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11258v1</a>
  <a href="https://arxiv.org/pdf/2510.11258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11258v1" onclick="toggleFavorite(this, '2510.11258v1', 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhui Fu, Feiyang Xie, Chaoyi Xu, Jing Xiong, Haoqi Yuan, Zongqing Lu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**DemoHLM：基于单次演示实现通用人形机器人移动操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `移动操作` `模仿学习` `全身控制` `Sim-to-Real`

## 📋 核心要点

1. 人形机器人移动操作面临缺乏自主性和泛化性的挑战，现有方法依赖硬编码或昂贵的真实数据。
2. DemoHLM框架通过分层控制和模仿学习，从单次模拟演示中学习通用移动操作策略。
3. 实验表明，该方法在真实机器人上实现了良好的sim-to-real迁移，并在多个任务中表现出鲁棒性。

## 📝 摘要（中文）

移动操作是人形机器人在人类环境中实现多功能交互的一项基本挑战。尽管最近的研究在人形机器人全身控制方面取得了显著进展，但移动操作仍未得到充分探索，并且通常依赖于硬编码的任务定义或昂贵的真实世界数据收集，这限制了自主性和泛化能力。我们提出了DemoHLM，一个用于人形机器人移动操作的框架，它能够从模拟中的单个演示中实现真实人形机器人上的通用移动操作。DemoHLM采用了一种层次结构，该结构将低级通用全身控制器与高级操作策略集成在一起，以执行多个任务。全身控制器将全身运动命令映射到关节扭矩，并为人形机器人提供全向移动能力。操作策略通过我们的数据生成和模仿学习流程在模拟中学习，利用闭环视觉反馈来指挥全身控制器，以执行具有挑战性的移动操作任务。实验表明，合成数据的数量与策略性能之间存在正相关关系，突显了我们的数据生成流程的有效性和我们方法的data efficiency。在配备RGB-D相机的Unitree G1机器人上的真实世界实验验证了DemoHLM的sim-to-real可迁移性，展示了在十个移动操作任务中空间变化下的稳健性能。

## 🔬 方法详解

**问题定义**：人形机器人在复杂环境中进行移动操作，需要同时控制机器人的运动和操作，现有方法通常依赖于人工设计的控制器或大量的真实世界数据，难以泛化到新的任务和环境。痛点在于缺乏一种能够高效学习、泛化性强的移动操作框架。

**核心思路**：DemoHLM的核心思路是利用分层控制结构和模仿学习，从模拟环境中少量的数据中学习到通用的移动操作策略。通过低级全身控制器实现精确的运动控制，并通过高级操作策略实现任务级别的规划和执行。这种分层结构降低了学习的难度，提高了泛化能力。

**技术框架**：DemoHLM框架包含两个主要模块：低级全身控制器和高级操作策略。低级全身控制器负责将全身运动命令转换为关节扭矩，实现机器人的运动控制。高级操作策略通过模仿学习从模拟数据中学习，根据视觉反馈生成全身运动命令，控制机器人完成特定的操作任务。整个流程是闭环的，可以根据环境变化进行实时调整。

**关键创新**：DemoHLM的关键创新在于其数据生成和模仿学习流程，能够从单次演示中学习到通用的移动操作策略。通过在模拟环境中生成大量的合成数据，并利用模仿学习算法训练高级操作策略，实现了高效的sim-to-real迁移。此外，分层控制结构也提高了系统的鲁棒性和泛化能力。

**关键设计**：低级全身控制器采用通用的Whole-Body Controller，具体实现细节未知。高级操作策略的网络结构未知，损失函数可能包含模仿学习损失和正则化项。数据生成流程的关键在于如何生成多样化的训练数据，具体方法未知。

## 📊 实验亮点

实验结果表明，DemoHLM框架在Unitree G1机器人上实现了成功的sim-to-real迁移，并在十个不同的移动操作任务中表现出良好的鲁棒性。合成数据的数量与策略性能之间存在正相关关系，验证了数据生成流程的有效性。具体的性能指标和对比基线数据未知。

## 🎯 应用场景

DemoHLM框架可应用于人形机器人在家庭服务、工业制造、医疗辅助等领域的复杂操作任务。例如，机器人可以在家庭环境中进行物品拾取、放置等操作，或在工厂中进行装配、搬运等任务。该研究降低了人形机器人应用门槛，加速了人形机器人在实际场景中的部署。

## 📄 摘要（原文）

> Loco-manipulation is a fundamental challenge for humanoid robots to achieve versatile interactions in human environments. Although recent studies have made significant progress in humanoid whole-body control, loco-manipulation remains underexplored and often relies on hard-coded task definitions or costly real-world data collection, which limits autonomy and generalization. We present DemoHLM, a framework for humanoid loco-manipulation that enables generalizable loco-manipulation on a real humanoid robot from a single demonstration in simulation. DemoHLM adopts a hierarchy that integrates a low-level universal whole-body controller with high-level manipulation policies for multiple tasks. The whole-body controller maps whole-body motion commands to joint torques and provides omnidirectional mobility for the humanoid robot. The manipulation policies, learned in simulation via our data generation and imitation learning pipeline, command the whole-body controller with closed-loop visual feedback to execute challenging loco-manipulation tasks. Experiments show a positive correlation between the amount of synthetic data and policy performance, underscoring the effectiveness of our data generation pipeline and the data efficiency of our approach. Real-world experiments on a Unitree G1 robot equipped with an RGB-D camera validate the sim-to-real transferability of DemoHLM, demonstrating robust performance under spatial variations across ten loco-manipulation tasks.

