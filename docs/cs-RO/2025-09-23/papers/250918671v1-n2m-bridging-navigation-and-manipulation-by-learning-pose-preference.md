---
layout: default
title: "N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout"
---

# N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18671" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18671v1</a>
  <a href="https://arxiv.org/pdf/2509.18671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18671v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18671v1', 'N2M: Bridging Navigation and Manipulation by Learning Pose Preference from Rollout')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaixin Chai, Hyunjun Lee, Joseph J. Lim

**分类**: cs.RO

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**提出N2M以解决移动操作中导航与操作不一致问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `移动操作` `导航与操作` `机器人技术` `任务成功率` `数据效率` `环境适应性` `姿态选择`

## 📋 核心要点

1. 现有的移动操作方法中，导航模块与操作策略之间存在不一致，导致任务成功率低。
2. N2M模块通过引导机器人选择合适的初始姿态，解决了导航与操作之间的矛盾。
3. 在PnPCounterToCab任务中，N2M将成功率从3%提升至54%，显示出显著的效果提升。

## 📝 摘要（中文）

在移动操作中，操作策略对执行的初始姿态有强烈偏好，而导航模块仅关注到达任务区域，未考虑下游操作的初始姿态偏好。为了解决这一不匹配问题，本文提出了N2M过渡模块，引导机器人在到达任务区域后选择合适的初始姿态，从而显著提高任务成功率。N2M具有五大优势：仅依赖自我中心观察，无需全局或历史信息；实时适应环境变化；高视角鲁棒性下的可靠预测；广泛适用于多种任务、操作策略和机器人硬件；出色的数据效率和泛化能力。通过大量仿真和实际实验验证了N2M的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决移动操作中导航模块与操作策略之间的偏差，现有方法未能考虑初始姿态的选择，导致任务成功率低下。

**核心思路**：N2M模块通过学习并引导机器人选择更优的初始姿态，确保在到达任务区域后能够更好地执行操作，从而提高整体任务成功率。

**技术框架**：N2M的整体架构包括导航模块、过渡模块和操作模块。导航模块负责到达任务区域，过渡模块则引导选择合适的初始姿态，最后操作模块执行具体的操作任务。

**关键创新**：N2M的主要创新在于其能够实时适应环境变化，并且仅依赖自我中心的观察数据，避免了对全局信息的依赖，这与传统方法有本质区别。

**关键设计**：N2M采用了高视角鲁棒性的预测机制，设计了特定的损失函数以优化初始姿态选择，并在网络结构上进行了针对性的调整，以提高数据效率和泛化能力。

## 📊 实验亮点

在PnPCounterToCab任务中，N2M的引入使得任务成功率从3%提升至54%。在Toybox Handover任务中，N2M在仅使用15个数据样本的情况下，仍能在未见环境中提供可靠的预测，展现出卓越的数据效率和泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和家庭助理等场景。通过提高机器人在复杂环境中的操作成功率，N2M能够显著提升机器人在实际应用中的效率和可靠性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In mobile manipulation, the manipulation policy has strong preferences for initial poses where it is executed. However, the navigation module focuses solely on reaching the task area, without considering which initial pose is preferable for downstream manipulation. To address this misalignment, we introduce N2M, a transition module that guides the robot to a preferable initial pose after reaching the task area, thereby substantially improving task success rates. N2M features five key advantages: (1) reliance solely on ego-centric observation without requiring global or historical information; (2) real-time adaptation to environmental changes; (3) reliable prediction with high viewpoint robustness; (4) broad applicability across diverse tasks, manipulation policies, and robot hardware; and (5) remarkable data efficiency and generalizability. We demonstrate the effectiveness of N2M through extensive simulation and real-world experiments. In the PnPCounterToCab task, N2M improves the averaged success rate from 3% with the reachability-based baseline to 54%. Furthermore, in the Toybox Handover task, N2M provides reliable predictions even in unseen environments with only 15 data samples, showing remarkable data efficiency and generalizability.

