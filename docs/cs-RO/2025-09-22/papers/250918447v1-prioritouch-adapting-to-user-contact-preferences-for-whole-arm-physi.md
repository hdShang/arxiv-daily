---
layout: default
title: "PrioriTouch: Adapting to User Contact Preferences for Whole-Arm Physical Human-Robot Interaction"
---

# PrioriTouch: Adapting to User Contact Preferences for Whole-Arm Physical Human-Robot Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18447" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18447v1</a>
  <a href="https://arxiv.org/pdf/2509.18447.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18447v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18447v1', 'PrioriTouch: Adapting to User Contact Preferences for Whole-Arm Physical Human-Robot Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rishabh Madan, Jiawei Lin, Mahika Goel, Angchen Xie, Xiaoyu Liang, Marcus Lee, Justin Guo, Pranav N. Thakkar, Rohan Banerjee, Jose Barreiros, Kate Tsui, Tom Silver, Tapomayukh Bhattacharjee

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-22

**备注**: Conference on Robot Learning (CoRL)

---

## 💡 一句话要点

**PrioriTouch：通过学习用户接触偏好实现全身物理人机交互**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `物理人机交互` `人机协作` `用户偏好学习` `学习排序` `分层控制`

## 📋 核心要点

1. 现有物理人机交互难以处理全身交互中多个接触点偏好不一致的问题，尤其是在护理等场景下。
2. PrioriTouch框架通过学习排序方法和分层操作空间控制，对多个接触点的控制目标进行优先级排序。
3. 实验表明，PrioriTouch能够适应用户接触偏好，在保证任务性能的同时，提升交互的安全性和舒适性。

## 📝 摘要（中文）

物理人机交互(pHRI)要求机器人适应个体接触偏好，例如接触位置和施力大小。单次接触时识别偏好已经很困难；全身交互涉及机器人与人之间的多个同时接触，挑战更大，因为不同身体部位可能存在不兼容的力需求。在护理任务中，接触频繁且多样，此类冲突不可避免。由于多个接触存在多个偏好，没有单一解决方案可以满足所有目标——权衡是固有的，因此优先级排序至关重要。我们提出了PrioriTouch，一个用于对多个接触中的控制目标进行排序和执行的框架。PrioriTouch可以对一般的控制器集合进行优先级排序，使其不仅适用于诸如床上沐浴和穿衣等护理场景，还适用于更广泛的多接触设置。我们的方法结合了一种新颖的学习排序方法和分层操作空间控制，利用模拟在环rollout进行数据高效和安全探索。我们对身体辅助偏好进行了用户研究，推导了个性化的舒适度阈值，并将它们纳入PrioriTouch。我们通过广泛的模拟和真实世界实验评估了PrioriTouch，证明了其适应用户接触偏好、保持任务性能以及增强安全性和舒适性的能力。

## 🔬 方法详解

**问题定义**：论文旨在解决全身物理人机交互中，机器人需要同时与人体的多个部位进行接触，而不同部位对接触的位置、力度等偏好可能存在冲突的问题。现有方法难以有效地处理这种多目标优化问题，无法兼顾任务完成、用户舒适度和安全性。

**核心思路**：论文的核心思路是引入优先级排序机制，通过学习用户对不同接触点的偏好，对控制目标进行排序，从而在多个目标之间进行权衡。这种方法允许机器人根据用户的个性化需求，动态地调整控制策略，以达到最佳的交互体验。

**技术框架**：PrioriTouch框架主要包含以下几个模块：1) 用户偏好学习模块：通过用户研究或在线学习，获取用户对不同接触点的舒适度阈值等偏好信息。2) 控制目标生成模块：根据任务需求和用户偏好，生成多个控制目标，例如保持特定姿态、施加特定力等。3) 优先级排序模块：使用学习排序算法，根据用户偏好和任务需求，对控制目标进行优先级排序。4) 分层操作空间控制模块：根据控制目标的优先级，采用分层操作空间控制方法，实现对机器人的运动控制。

**关键创新**：论文的关键创新在于将学习排序方法应用于物理人机交互领域，从而能够有效地处理多目标优化问题。此外，论文还提出了一个基于模拟在环rollout的数据高效探索方法，用于学习用户偏好和优化控制策略。

**关键设计**：论文采用了一种新颖的学习排序方法，该方法可以根据用户偏好和任务需求，对控制目标进行排序。具体来说，论文使用了一个神经网络来预测不同控制目标的优先级，并使用模拟在环rollout来训练该网络。此外，论文还设计了一个分层操作空间控制器，该控制器可以根据控制目标的优先级，实现对机器人的运动控制。

## 📊 实验亮点

论文通过模拟和真实世界实验验证了PrioriTouch框架的有效性。实验结果表明，PrioriTouch能够显著提升用户在物理人机交互中的舒适度和安全性，同时保持良好的任务性能。例如，在床上沐浴任务中，PrioriTouch能够根据用户的偏好，调整机器人的接触位置和力度，从而减少用户的不适感。

## 🎯 应用场景

PrioriTouch框架具有广泛的应用前景，尤其是在需要频繁且多样接触的场景中，如护理机器人、康复机器人、辅助机器人等。通过学习和适应用户的个性化接触偏好，该框架可以显著提升人机交互的舒适性和安全性，从而提高机器人的实用性和接受度。未来，该技术有望应用于更广泛的领域，如工业机器人、服务机器人等。

## 📄 摘要（原文）

> Physical human-robot interaction (pHRI) requires robots to adapt to individual contact preferences, such as where and how much force is applied. Identifying preferences is difficult for a single contact; with whole-arm interaction involving multiple simultaneous contacts between the robot and human, the challenge is greater because different body parts can impose incompatible force requirements. In caregiving tasks, where contact is frequent and varied, such conflicts are unavoidable. With multiple preferences across multiple contacts, no single solution can satisfy all objectives--trade-offs are inherent, making prioritization essential. We present PrioriTouch, a framework for ranking and executing control objectives across multiple contacts. PrioriTouch can prioritize from a general collection of controllers, making it applicable not only to caregiving scenarios such as bed bathing and dressing but also to broader multi-contact settings. Our method combines a novel learning-to-rank approach with hierarchical operational space control, leveraging simulation-in-the-loop rollouts for data-efficient and safe exploration. We conduct a user study on physical assistance preferences, derive personalized comfort thresholds, and incorporate them into PrioriTouch. We evaluate PrioriTouch through extensive simulation and real-world experiments, demonstrating its ability to adapt to user contact preferences, maintain task performance, and enhance safety and comfort. Website: https://emprise.cs.cornell.edu/prioritouch.

