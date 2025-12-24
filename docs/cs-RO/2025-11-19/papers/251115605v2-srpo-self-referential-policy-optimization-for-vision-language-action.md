---
layout: default
title: "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models"
---

# SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15605" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15605v2</a>
  <a href="https://arxiv.org/pdf/2511.15605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15605v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.15605v2', 'SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Senyu Fei, Siyin Wang, Li Ji, Ao Li, Shiduo Zhang, Liming Liu, Jinlong Hou, Jingjing Gong, Xianzhong Zhao, Xipeng Qiu

**分类**: cs.RO, cs.CL, cs.CV

**发布日期**: 2025-11-19 (更新: 2025-11-30)

---

## 💡 一句话要点

**提出SRPO，利用自参照策略优化视觉-语言-动作模型，解决奖励稀疏问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言-动作模型` `强化学习` `自参照策略优化` `奖励稀疏` `世界模型`

## 📋 核心要点

1. 现有VLA模型依赖专家演示，存在演示偏差，且强化学习训练中奖励稀疏，导致训练效率低下。
2. SRPO利用模型自身生成的成功轨迹作为参照，为失败轨迹分配基于进度的奖励，无需额外监督。
3. SRPO使用世界模型的潜在空间编码来衡量行为进度，实现跨环境的泛化，并在LIBERO基准上取得显著提升。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在机器人操作方面表现出色，但过度依赖专家演示，导致演示偏差并限制性能。强化学习（RL）是克服这些限制的关键后训练策略，然而，现有的VLA-RL方法，包括基于群体的优化方法，都受到严重奖励稀疏性的阻碍。依赖二元成功指标浪费了失败轨迹中的宝贵信息，导致训练效率低下。为了解决这个问题，我们提出了自参照策略优化（SRPO），一种新颖的VLA-RL框架。SRPO通过利用模型自身在当前训练批次中生成的成功轨迹作为自参照，消除了对外部演示或手动奖励工程的需求。这使得我们能够为失败的尝试分配一个基于进度的奖励。一个核心创新是使用潜在世界表征来稳健地衡量行为进度。我们利用来自世界模型的潜在空间的压缩、可转移的编码，而不是依赖原始像素或需要特定领域的微调。这些表征自然地捕捉了跨环境的进度模式，从而实现准确、通用的轨迹比较。在LIBERO基准上的经验评估证明了SRPO的效率和有效性。从48.9%的成功率的监督基线开始，SRPO仅在200个RL步骤中就实现了99.2%的最新成功率，在没有任何额外监督的情况下，相对提高了103%。此外，SRPO显示出显著的鲁棒性，在LIBERO-Plus基准上实现了167%的性能提升。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作（VLA）模型在强化学习微调过程中，由于奖励稀疏性导致的训练效率低下的问题。现有方法依赖二元成功/失败信号，忽略了失败轨迹中包含的进度信息，或者需要额外的人工设计的奖励函数，增加了复杂性。

**核心思路**：SRPO的核心思路是利用模型自身产生的成功轨迹作为参照，来评估失败轨迹的进度。通过比较失败轨迹与成功轨迹在潜在空间中的相似度，可以推断出失败轨迹的完成程度，从而赋予其一个连续的、基于进度的奖励。这种自参照的方式避免了对外部演示或人工奖励工程的依赖。

**技术框架**：SRPO的整体框架包括以下几个主要阶段：1) VLA模型初始化：使用监督学习在专家数据集上预训练VLA模型。2) 轨迹生成：使用当前策略生成一批轨迹。3) 自参照选择：从当前批次中选择成功的轨迹作为参照。4) 潜在空间编码：使用世界模型将轨迹编码到潜在空间。5) 奖励计算：计算失败轨迹与成功轨迹在潜在空间中的相似度，作为奖励信号。6) 策略更新：使用强化学习算法（如PPO）更新策略。

**关键创新**：SRPO最重要的创新点在于其自参照的奖励生成机制。与传统的依赖二元奖励或人工设计的奖励函数的方法不同，SRPO利用模型自身生成的成功轨迹作为参照，自动地为失败轨迹赋予基于进度的奖励。此外，使用世界模型的潜在空间编码，使得奖励信号更加鲁棒和泛化。

**关键设计**：SRPO的关键设计包括：1) 世界模型的选择：论文使用预训练的世界模型，以获得高质量的潜在空间编码。2) 相似度度量：论文使用余弦相似度来衡量失败轨迹与成功轨迹在潜在空间中的相似度。3) 奖励缩放：论文对奖励信号进行缩放，以控制其大小和方差。4) 策略更新算法：论文使用PPO算法来更新策略，并调整了PPO的超参数以适应自参照奖励的特点。

## 📊 实验亮点

SRPO在LIBERO基准测试中，从48.9%的监督学习基线成功率提升至99.2%，仅需200步强化学习，相对提升103%。在更具挑战性的LIBERO-Plus基准上，SRPO实现了167%的性能提升，展示了其强大的鲁棒性和泛化能力。这些结果表明，SRPO能够有效地解决奖励稀疏问题，并显著提高VLA模型的性能。

## 🎯 应用场景

SRPO具有广泛的应用前景，可应用于机器人操作、自动驾驶、游戏AI等领域。通过减少对人工标注数据的依赖，降低了模型训练的成本，并提高了模型的泛化能力。该方法有望推动机器人智能的进一步发展，使其能够更好地适应复杂和动态的环境。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models excel in robotic manipulation but are constrained by their heavy reliance on expert demonstrations, leading to demonstration bias and limiting performance. Reinforcement learning (RL) is a vital post-training strategy to overcome these limits, yet current VLA-RL methods, including group-based optimization approaches, are crippled by severe reward sparsity. Relying on binary success indicators wastes valuable information in failed trajectories, resulting in low training efficiency. To solve this, we propose Self-Referential Policy Optimization (SRPO), a novel VLA-RL framework. SRPO eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference. This allows us to assign a progress-wise reward to failed attempts. A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, we utilize the compressed, transferable encodings from a world model's latent space. These representations naturally capture progress patterns across environments, enabling accurate, generalized trajectory comparison. Empirical evaluations on the LIBERO benchmark demonstrate SRPO's efficiency and effectiveness. Starting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.

