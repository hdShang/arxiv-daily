---
layout: default
title: ChicGrasp: Imitation-Learning based Customized Dual-Jaw Gripper Control for Delicate, Irregular Bio-products Manipulation
---

# ChicGrasp: Imitation-Learning based Customized Dual-Jaw Gripper Control for Delicate, Irregular Bio-products Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08986" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08986v1</a>
  <a href="https://arxiv.org/pdf/2505.08986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08986v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08986v1', 'ChicGrasp: Imitation-Learning based Customized Dual-Jaw Gripper Control for Delicate, Irregular Bio-products Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amirreza Davar, Zhengtong Xu, Siavash Mahmoudi, Pouya Sohrabipour, Chaitanya Pallerla, Yu She, Wan Shou, Philip Crandall, Dongyi Wang

**分类**: cs.RO, cs.LG

**发布日期**: 2025-05-13

**备注**: Submitted for journal review

---

## 💡 一句话要点

**提出ChicGrasp以解决生物产品操控中的抓取难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `生物产品操控` `气动夹具` `条件扩散策略` `农业机器人`

## 📋 核心要点

1. 现有的禽类加工方法依赖人工操作，面临抓取滑腻且易损伤的尸体的挑战，传统方法不可靠。
2. ChicGrasp通过硬件与软件的协同设计，利用独立驱动的双爪夹具和条件扩散策略控制器，实现了对鸡腿的有效抓取。
3. 实验结果显示，ChicGrasp在抓取和提升成功率上达到了40.6%，显著优于现有的隐式行为克隆和LSTM-GMM方法。

## 📝 摘要（中文）

自动化禽类加工线仍依赖人工将滑腻且易损伤的尸体放置到输送带上。由于变形性、解剖差异和严格的卫生规则，传统的吸附和脚本动作不可靠。我们提出ChicGrasp，这是一个针对该任务的端到端硬件-软件协同设计。该系统采用独立驱动的双爪气动夹具夹住鸡腿，同时使用条件扩散策略控制器，从仅50个多视角遥操作演示（RGB + 自我感知）中训练，规划5自由度的末端执行器运动，包括一次性发出夹具指令。在单独呈现的生鸡尸体上，我们的系统实现了40.6%的抓取和提升成功率，并在38秒内完成抓取到输送带的周期，而现有的隐式行为克隆（IBC）和LSTM-GMM基线则完全失败。所有CAD、代码和数据集将开源。ChicGrasp展示了模仿学习如何弥合刚性硬件与可变生物产品之间的差距，为农业工程和机器人学习研究者提供了可重复的基准和公共数据集。

## 🔬 方法详解

**问题定义**：本论文旨在解决自动化禽类加工中，如何有效抓取滑腻且易损伤的鸡尸体的问题。现有的传统方法如吸附和脚本动作在面对变形性和解剖差异时表现不佳，导致抓取失败。

**核心思路**：ChicGrasp的核心思路是通过模仿学习，结合硬件与软件的协同设计，利用独立驱动的双爪气动夹具和条件扩散策略控制器，使得系统能够适应不同形状和状态的生物产品。

**技术框架**：该系统的整体架构包括独立驱动的双爪夹具、条件扩散策略控制器和多视角遥操作演示数据的训练模块。控制器负责规划5自由度的末端执行器运动，并在一次性发出夹具指令。

**关键创新**：ChicGrasp的主要创新在于其使用的条件扩散策略控制器，通过仅50个多视角演示进行训练，显著提高了对复杂生物产品的抓取能力，与现有的隐式行为克隆和LSTM-GMM方法相比，表现出更高的成功率。

**关键设计**：在设计中，系统采用了独立驱动的双爪气动夹具，能够灵活适应不同形状的鸡腿。同时，控制器的训练采用了RGB图像和自我感知数据，确保了抓取动作的准确性和可靠性。

## 📊 实验亮点

ChicGrasp在实验中实现了40.6%的抓取和提升成功率，且完成抓取到输送带的周期时间为38秒，显著优于现有的隐式行为克隆和LSTM-GMM基线，后者在此任务中完全失败，展示了其在生物产品操控中的优越性。

## 🎯 应用场景

ChicGrasp的研究成果在农业工程和机器人学习领域具有广泛的应用潜力。其能够有效处理生物产品的抓取问题，未来可推广至其他易损物品的自动化处理，提升生产效率和安全性。

## 📄 摘要（原文）

> Automated poultry processing lines still rely on humans to lift slippery, easily bruised carcasses onto a shackle conveyor. Deformability, anatomical variance, and strict hygiene rules make conventional suction and scripted motions unreliable. We present ChicGrasp, an end--to--end hardware--software co-design for this task. An independently actuated dual-jaw pneumatic gripper clamps both chicken legs, while a conditional diffusion-policy controller, trained from only 50 multi--view teleoperation demonstrations (RGB + proprioception), plans 5 DoF end--effector motion, which includes jaw commands in one shot. On individually presented raw broiler carcasses, our system achieves a 40.6\% grasp--and--lift success rate and completes the pick to shackle cycle in 38 s, whereas state--of--the--art implicit behaviour cloning (IBC) and LSTM-GMM baselines fail entirely. All CAD, code, and datasets will be open-source. ChicGrasp shows that imitation learning can bridge the gap between rigid hardware and variable bio--products, offering a reproducible benchmark and a public dataset for researchers in agricultural engineering and robot learning.

