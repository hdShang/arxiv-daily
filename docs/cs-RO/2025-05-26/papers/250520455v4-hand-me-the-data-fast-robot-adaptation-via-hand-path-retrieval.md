---
layout: default
title: "HAND Me the Data: Fast Robot Adaptation via Hand Path Retrieval"
---

# HAND Me the Data: Fast Robot Adaptation via Hand Path Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20455" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20455v4</a>
  <a href="https://arxiv.org/pdf/2505.20455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20455v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20455v4', 'HAND Me the Data: Fast Robot Adaptation via Hand Path Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthew Hong, Anthony Liang, Kevin Kim, Harshitha Rajaprakash, Jesse Thomason, Erdem Bıyık, Jesse Zhang

**分类**: cs.RO

**发布日期**: 2025-05-26 (更新: 2025-10-27)

---

## 💡 一句话要点

**提出HAND方法以解决机器人快速适应新任务的问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人适应` `手部示范` `行为检索` `实时学习` `视觉跟踪` `任务无关数据`

## 📋 核心要点

1. 现有方法依赖于特定任务的机器人示范，收集过程复杂且耗时，限制了机器人快速适应新任务的能力。
2. HAND方法通过人类手部示范提取运动信息，利用任务无关的机器人数据进行行为检索，从而实现快速学习。
3. 实验结果显示，HAND在真实机器人上的平均任务成功率提升超过2倍，显著优于传统的检索基线。

## 📝 摘要（中文）

本文提出了一种简单高效的方法HAND，通过人类手部示范教会机器人新的操作任务。与依赖于特定任务的机器人示范不同，HAND利用易于提供的手部示范，从任务无关的机器人游戏数据中检索相关行为。通过视觉跟踪管道，HAND提取人类手部的运动，并分两个阶段检索机器人子轨迹：首先通过视觉相似性过滤，然后检索与手部行为相似的轨迹。对检索数据进行策略微调，使得任务的实时学习在四分钟内完成，无需校准相机或详细的手部姿态估计。实验表明，HAND在真实机器人上的平均任务成功率超过检索基线2倍以上。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在新操作任务中快速适应的问题。现有方法依赖于复杂的任务特定示范，导致学习效率低下。

**核心思路**：HAND方法通过人类手部示范提取运动信息，并从任务无关的机器人游戏数据中检索相关行为，避免了对复杂示范的依赖。

**技术框架**：整体流程分为两个主要阶段：首先通过视觉相似性过滤手部示范，提取手部运动轨迹；然后检索与手部行为相似的机器人轨迹。最后，对检索到的数据进行策略微调，实现实时学习。

**关键创新**：HAND的主要创新在于利用人类手部示范进行行为检索，而非依赖于复杂的任务特定示范。这种方法显著提高了学习效率和适应性。

**关键设计**：在技术细节上，HAND采用了视觉跟踪管道来提取手部运动，且不需要校准相机或详细的手部姿态估计，简化了系统的复杂性。

## 📊 实验亮点

实验结果表明，HAND方法在真实机器人上的平均任务成功率超过传统检索基线2倍，显示出其在任务学习效率上的显著提升。这一成果验证了HAND在快速适应新操作任务中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过快速适应新任务，机器人能够更灵活地应对多变的工作环境，提高工作效率和安全性。未来，HAND方法可能推动机器人在更广泛领域的应用，促进智能自动化的发展。

## 📄 摘要（原文）

> We hand the community HAND, a simple and time-efficient method for teaching robots new manipulation tasks through human hand demonstrations. Instead of relying on task-specific robot demonstrations collected via teleoperation, HAND uses easy-to-provide hand demonstrations to retrieve relevant behaviors from task-agnostic robot play data. Using a visual tracking pipeline, HAND extracts the motion of the human hand from the hand demonstration and retrieves robot sub-trajectories in two stages: first filtering by visual similarity, then retrieving trajectories with similar behaviors to the hand. Fine-tuning a policy on the retrieved data enables real-time learning of tasks in under four minutes, without requiring calibrated cameras or detailed hand pose estimation. Experiments also show that HAND outperforms retrieval baselines by over 2x in average task success rates on real robots. Videos can be found at our project website: https://liralab.usc.edu/handretrieval/.

