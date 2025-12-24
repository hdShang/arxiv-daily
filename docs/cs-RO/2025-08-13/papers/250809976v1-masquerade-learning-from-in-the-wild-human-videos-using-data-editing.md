---
layout: default
title: "Masquerade: Learning from In-the-wild Human Videos using Data-Editing"
---

# Masquerade: Learning from In-the-wild Human Videos using Data-Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09976" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09976v1</a>
  <a href="https://arxiv.org/pdf/2508.09976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09976v1', 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marion Lepert, Jiaying Fang, Jeannette Bohg

**分类**: cs.RO

**发布日期**: 2025-08-13

**备注**: Project website at https://masquerade-robot.github.io/

---

## 💡 一句话要点

**提出Masquerade以解决机器人操作数据稀缺问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人操作` `数据稀缺` `视频编辑` `视觉体现` `策略学习` `人机协作` `深度学习`

## 📋 核心要点

1. 现有的机器人操作研究面临数据稀缺的问题，现有数据集的规模和多样性远不及其他领域。
2. Masquerade通过编辑人类视频，估计手部姿态并叠加机器人演示，来解决视觉体现差距。
3. 在三个长时间的厨房任务中，Masquerade的策略表现比基线提高了5-6倍，显示出显著的泛化能力。

## 📝 摘要（中文）

机器人操作研究仍面临显著的数据稀缺问题：即使是最大的机器人数据集，其规模和多样性也远不及推动语言和视觉领域突破的那些数据集。我们提出Masquerade，一种通过编辑野外人类视频来缩小人类与机器人之间的视觉体现差距的方法，并利用这些编辑后的视频学习机器人策略。我们的流程将每个视频转化为机器人演示，具体步骤包括：估计三维手部姿态、修复人类手臂以及叠加跟踪恢复的末端执行器轨迹的双手机器人。通过在675K帧编辑片段上预训练视觉编码器以预测未来的二维机器人关键点，并在每个任务仅用50个机器人演示微调扩散策略头，得到了显著优于以往工作的策略。在三个长时间的双手厨房任务中，Masquerade的表现比基线提高了5-6倍。消融实验表明，机器人叠加和共同训练都是不可或缺的，性能与编辑人类视频的数量呈对数关系。这些结果表明，明确缩小视觉体现差距可以利用人类视频这一丰富的数据源来改善机器人策略。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人操作领域的数据稀缺问题，现有方法在多样性和规模上无法满足需求，限制了机器人的学习能力。

**核心思路**：通过编辑真实的人类视频，将其转化为机器人演示，缩小人类与机器人之间的视觉体现差距，从而利用丰富的现有视频数据来训练机器人策略。

**技术框架**：整体流程包括三个主要步骤：首先，估计三维手部姿态；其次，修复人类手臂以消除干扰；最后，叠加一个双手机器人模型，该模型能够跟踪恢复的末端执行器轨迹。

**关键创新**：最重要的创新在于通过编辑人类视频生成机器人演示，并结合视觉编码器的预训练与扩散策略的微调，显著提高了策略的泛化能力。

**关键设计**：在675K帧的编辑视频上预训练视觉编码器，使用辅助损失来提高性能，并在每个任务中仅用50个机器人演示进行微调，确保了高效的学习过程。

## 📊 实验亮点

在三个长时间的双手厨房任务中，Masquerade的策略表现比基线提高了5-6倍，显示出显著的性能提升。消融实验表明，机器人叠加和共同训练是不可或缺的，且性能与编辑人类视频的数量呈对数关系。

## 🎯 应用场景

该研究的潜在应用领域包括家庭服务机器人、工业自动化以及人机协作等场景。通过利用丰富的人类视频数据，Masquerade能够显著提升机器人在复杂任务中的表现，推动机器人技术的实际应用和发展。

## 📄 摘要（原文）

> Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

