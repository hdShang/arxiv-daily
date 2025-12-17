---
layout: default
title: Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion
---

# Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13090" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13090v1</a>
  <a href="https://arxiv.org/pdf/2512.13090.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13090v1" onclick="toggleFavorite(this, '2512.13090v1', 'Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jebeom Chae, Junwoo Chang, Seungho Yeom, Yujin Kim, Jongeun Choi

**分类**: cs.RO

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出基于热扩散的多机器人视觉语言运动规划框架LCHD**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多机器人运动规划` `视觉语言导航` `扩散模型` `CLIP模型` `碰撞避免` `热扩散` `机器人学习`

## 📋 核心要点

1. 现有基于扩散的机器人运动规划方法计算成本高，泛化能力弱，难以处理多机器人和语言条件任务。
2. LCHD框架结合CLIP语义先验和碰撞避免扩散核，在可达工作空间内解析语言指令，提升泛化性。
3. 实验表明，LCHD在成功率上优于现有方法，并降低了规划延迟，验证了其有效性。

## 📝 摘要（中文）

扩散模型在机器人运动规划中表现出强大的能力，能够捕捉可行轨迹的多模态分布。然而，将其扩展到具有灵活的、语言条件任务规范的多机器人环境仍然有限。此外，现有的基于扩散的方法在推理过程中计算成本高昂，并且由于需要显式构建环境表示且缺乏几何可达性推理机制，因此难以泛化。为了解决这些局限性，我们提出了语言条件热扩散（LCHD），这是一个端到端的基于视觉的框架，可以生成语言条件下的无碰撞轨迹。LCHD集成了基于CLIP的语义先验知识和一个避免碰撞的扩散核，作为一种物理归纳偏置，使规划器能够在可达工作空间内严格地解释语言命令。通过引导机器人找到与语义意图相匹配的可达替代方案，自然地处理了可达性方面的分布外场景，同时消除了推理时对显式障碍物信息的需求。在各种受现实世界启发的地图上的大量评估以及真实的机器人实验表明，LCHD在成功率方面始终优于先前的基于扩散的规划器，同时降低了规划延迟。

## 🔬 方法详解

**问题定义**：现有的基于扩散的机器人运动规划方法，在多机器人场景下，难以结合语言指令进行任务规划。它们通常需要显式地构建环境表示，计算成本高昂，并且缺乏对几何可达性的有效推理，导致泛化能力不足，难以处理分布外场景。

**核心思路**：LCHD的核心思路是将语言指令、视觉信息和物理约束（碰撞避免）集成到一个扩散模型中。通过CLIP模型提取语言指令的语义信息，并将其作为扩散过程的条件。同时，利用一个碰撞避免的扩散核作为物理归纳偏置，引导机器人生成无碰撞轨迹，并确保轨迹的可达性。

**技术框架**：LCHD框架主要包含以下几个模块：1) 基于视觉的场景理解模块（输入图像，提取环境特征）；2) 基于CLIP的语言指令编码模块（输入语言指令，提取语义特征）；3) 热扩散运动规划模块（结合视觉和语言特征，生成无碰撞轨迹）。整个流程是端到端的，可以直接从视觉输入和语言指令生成机器人的运动轨迹。

**关键创新**：LCHD的关键创新在于：1) 将CLIP模型引入到机器人运动规划中，实现了语言条件下的运动规划；2) 提出了一个碰撞避免的扩散核，作为物理归纳偏置，提高了规划的效率和泛化能力；3) 无需显式构建环境表示，直接从视觉输入进行规划，降低了计算成本。

**关键设计**：LCHD使用CLIP模型提取语言指令的语义特征，并将其与视觉特征进行融合。扩散核的设计基于热扩散方程，通过调整扩散系数来控制轨迹的平滑性和碰撞避免能力。损失函数包括轨迹平滑损失、碰撞避免损失和语言一致性损失，用于优化扩散模型的参数。

## 📊 实验亮点

LCHD在多个真实场景和模拟环境中进行了评估，结果表明，LCHD在成功率方面始终优于先前的基于扩散的规划器，并且显著降低了规划延迟。在真实机器人实验中，LCHD也表现出了良好的性能，验证了其在实际应用中的可行性。

## 🎯 应用场景

LCHD可应用于多机器人协同作业、自动驾驶、服务机器人等领域。例如，在仓库自动化场景中，可以通过语言指令控制多个机器人完成货物的搬运任务。在家庭服务机器人中，可以根据用户的语音指令，引导机器人完成各种家务任务。该研究有助于提升机器人的智能化水平和人机交互能力。

## 📄 摘要（原文）

> Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-Conditioned Heat-Inspired Diffusion (LCHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LCHD integrates CLIP-based semantic priors with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LCHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency.

