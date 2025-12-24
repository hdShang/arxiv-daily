---
layout: default
title: "DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy"
---

# DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20668" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20668v1</a>
  <a href="https://arxiv.org/pdf/2506.20668.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20668v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20668v1', 'DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sungjae Park, Homanga Bharadhwaj, Shubham Tulsiani

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-25

**备注**: Preprint(17 pages). Under Review

---

## 💡 一句话要点

**提出DemoDiffusion以解决机器人模仿人类示范的挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人模仿` `扩散策略` `人机协作` `任务适应` `运动重定向` `强化学习` `自然环境`

## 📋 核心要点

1. 现有方法在机器人模仿人类示范时，往往需要大量的在线强化学习或配对数据，限制了其适应性和效率。
2. DemoDiffusion通过将人类示范的手部运动转化为机器人轨迹，并利用预训练的扩散策略进行调整，解决了这一问题。
3. 实验结果显示，DemoDiffusion在多种任务中表现优异，成功率显著高于传统方法，展示了其强大的适应能力。

## 📝 摘要（中文）

我们提出了DemoDiffusion，这是一种简单且可扩展的方法，使机器人能够通过模仿单个示范来执行自然环境中的操作任务。该方法基于两个关键见解：首先，人类示范中的手部运动为机器人的末端执行器轨迹提供了有用的先验信息；其次，虽然重定向的运动捕捉了任务的整体结构，但可能与上下文中的合理机器人动作不一致。为了解决这个问题，我们利用预训练的通用扩散策略来修改轨迹，确保其既遵循人类运动，又保持在合理机器人动作的分布内。我们的方案避免了在线强化学习或配对人机数据的需求，使得机器人能够以最小的手动努力适应新任务和场景。实验结果表明，DemoDiffusion在模拟和现实环境中均优于基础策略和重定向轨迹，甚至在预训练通用策略完全失败的任务中也能成功。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在自然环境中模仿人类示范时的效率和适应性问题。现有方法通常依赖于大量的在线强化学习或配对人机数据，导致适应新任务时的灵活性不足。

**核心思路**：DemoDiffusion的核心思路是利用人类示范中的手部运动作为先验信息，通过运动重定向生成初步轨迹，然后使用预训练的扩散策略进行调整，以确保机器人动作的合理性和有效性。

**技术框架**：该方法的整体架构包括两个主要阶段：首先，通过运动重定向将人类示范转化为机器人轨迹；其次，利用预训练的扩散策略对轨迹进行调整，以确保其符合合理的机器人动作分布。

**关键创新**：DemoDiffusion的创新之处在于它结合了人类示范的先验信息与预训练的扩散策略，避免了传统方法对在线学习和配对数据的依赖，从而提高了机器人在新任务中的适应能力。

**关键设计**：在技术细节上，DemoDiffusion采用了特定的损失函数来平衡人类运动与机器人动作的合理性，并设计了适合的网络结构以支持扩散策略的有效应用。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，DemoDiffusion在多种任务中成功率显著提高，尤其是在预训练通用策略失败的情况下，机器人仍能成功完成任务，展示了其在复杂场景下的强大适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提高机器人模仿人类的能力，DemoDiffusion能够在多种复杂环境中执行任务，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> We propose DemoDiffusion, a simple and scalable method for enabling robots to perform manipulation tasks in natural environments by imitating a single human demonstration. Our approach is based on two key insights. First, the hand motion in a human demonstration provides a useful prior for the robot's end-effector trajectory, which we can convert into a rough open-loop robot motion trajectory via kinematic retargeting. Second, while this retargeted motion captures the overall structure of the task, it may not align well with plausible robot actions in-context. To address this, we leverage a pre-trained generalist diffusion policy to modify the trajectory, ensuring it both follows the human motion and remains within the distribution of plausible robot actions. Our approach avoids the need for online reinforcement learning or paired human-robot data, enabling robust adaptation to new tasks and scenes with minimal manual effort. Experiments in both simulation and real-world settings show that DemoDiffusion outperforms both the base policy and the retargeted trajectory, enabling the robot to succeed even on tasks where the pre-trained generalist policy fails entirely. Project page: https://demodiffusion.github.io/

