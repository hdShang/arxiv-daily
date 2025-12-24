---
layout: default
title: "DiWA: Diffusion Policy Adaptation with World Models"
---

# DiWA: Diffusion Policy Adaptation with World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03645" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03645v1</a>
  <a href="https://arxiv.org/pdf/2508.03645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03645v1', 'DiWA: Diffusion Policy Adaptation with World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akshay L Chandra, Iman Nematollahi, Chenguang Huang, Tim Welschehold, Wolfram Burgard, Abhinav Valada

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-08-05

**备注**: Accepted at the 2025 Conference on Robot Learning (CoRL)

---

## 💡 一句话要点

**提出DiWA框架以解决离线强化学习中的样本效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散策略` `强化学习` `世界模型` `离线学习` `样本效率` `机器人技能` `CALVIN基准测试`

## 📋 核心要点

1. 现有方法在微调扩散策略时面临长去噪序列和大量环境交互的挑战，导致样本效率低下。
2. DiWA框架通过利用世界模型实现离线微调，减少对真实环境交互的依赖，提升样本效率。
3. 在CALVIN基准测试中，DiWA在八个任务上表现优异，显著减少了物理交互需求，提升了学习效率。

## 📝 摘要（中文）

微调扩散策略与强化学习（RL）结合面临重大挑战，长时间去噪序列影响有效奖励传播，且标准RL方法需数百万次真实环境交互，成为实际微调的瓶颈。为此，本文提出DiWA框架，利用世界模型在离线环境中完全微调基于扩散的机器人技能。与需要大量环境交互的无模型方法不同，DiWA通过在数十万次离线交互上训练的世界模型，实现了高效的适应性，显著提高了样本效率，使得实际机器人学习更加安全和可行。在CALVIN基准测试中，DiWA在八个任务上表现出色，仅需离线适应，且物理交互次数远低于无模型基线。至今为止，这是首次展示使用离线世界模型微调扩散策略以实现真实世界机器人技能的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决微调扩散策略时的样本效率低下问题，现有方法依赖大量真实环境交互，导致效率低下和安全隐患。

**核心思路**：DiWA框架通过构建一个离线世界模型，利用该模型进行强化学习微调，避免了对真实环境的频繁交互，从而提高了样本效率。

**技术框架**：DiWA的整体架构包括三个主要模块：首先是世界模型的训练，基于数十万次离线交互；其次是利用该模型进行策略微调；最后是评估微调后的策略在真实环境中的表现。

**关键创新**：DiWA的核心创新在于首次将离线世界模型应用于扩散策略的微调，显著减少了对真实环境交互的需求，与传统的无模型方法形成鲜明对比。

**关键设计**：在设计中，DiWA采用了特定的损失函数来优化策略，同时确保世界模型的准确性，网络结构则基于现有的深度学习框架进行优化，以适应离线学习的需求。

## 📊 实验亮点

在CALVIN基准测试中，DiWA在八个任务上实现了显著的性能提升，物理交互次数比无模型基线减少了几个数量级，展示了其在离线适应中的高效性和实用性。

## 🎯 应用场景

DiWA框架在机器人学习领域具有广泛的应用潜力，尤其是在需要高效学习和适应的场景，如自主导航、机器人操控等。通过减少对真实环境的依赖，DiWA可以加速机器人技能的开发和部署，提高安全性和可靠性，未来可能在智能制造、服务机器人等领域产生深远影响。

## 📄 摘要（原文）

> Fine-tuning diffusion policies with reinforcement learning (RL) presents significant challenges. The long denoising sequence for each action prediction impedes effective reward propagation. Moreover, standard RL methods require millions of real-world interactions, posing a major bottleneck for practical fine-tuning. Although prior work frames the denoising process in diffusion policies as a Markov Decision Process to enable RL-based updates, its strong dependence on environment interaction remains highly inefficient. To bridge this gap, we introduce DiWA, a novel framework that leverages a world model for fine-tuning diffusion-based robotic skills entirely offline with reinforcement learning. Unlike model-free approaches that require millions of environment interactions to fine-tune a repertoire of robot skills, DiWA achieves effective adaptation using a world model trained once on a few hundred thousand offline play interactions. This results in dramatically improved sample efficiency, making the approach significantly more practical and safer for real-world robot learning. On the challenging CALVIN benchmark, DiWA improves performance across eight tasks using only offline adaptation, while requiring orders of magnitude fewer physical interactions than model-free baselines. To our knowledge, this is the first demonstration of fine-tuning diffusion policies for real-world robotic skills using an offline world model. We make the code publicly available at https://diwa.cs.uni-freiburg.de.

