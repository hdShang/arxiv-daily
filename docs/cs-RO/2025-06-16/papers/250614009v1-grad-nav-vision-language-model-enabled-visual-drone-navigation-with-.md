---
layout: default
title: "GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics"
---

# GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14009" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14009v1</a>
  <a href="https://arxiv.org/pdf/2506.14009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14009v1', 'GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager

**分类**: cs.RO

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出GRaD-Nav++以解决无人机语言指令导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `视觉-语言-动作` `可微强化学习` `专家混合` `多任务学习` `环境适应性`

## 📋 核心要点

1. 现有方法依赖手工技能和复杂参数调优，难以实现高效的自主无人机导航。
2. GRaD-Nav++是一个轻量级的视觉-语言-动作框架，能够实时执行自然语言指令，运行于无人机机载系统上。
3. 在多任务和多环境实验中，GRaD-Nav++分别在模拟和现实环境中取得了显著的成功率，展示了其强大的适应能力。

## 📝 摘要（中文）

自主无人机能够在非结构化环境中理解和执行高层语言指令一直是一个长期目标。然而，现有方法受限于手工技能、广泛的参数调优或不适合机载使用的计算密集型模型。我们提出了GRaD-Nav++，一个轻量级的视觉-语言-动作（VLA）框架，能够实时执行自然语言命令。我们的策略在一个光照真实的3D高斯点云（3DGS）模拟器中通过可微强化学习（DiffRL）进行训练，从视觉和语言输入中高效学习低级控制。核心是一个专家混合（MoE）动作头，能够自适应路由计算以提高泛化能力并减轻遗忘。在多任务泛化实验中，GRaD-Nav++在训练任务上取得了83%的成功率，在未见任务上为75%。在实际硬件上部署时，训练任务成功率为67%，未见任务为50%。在多环境适应实验中，GRaD-Nav++在多样化的模拟环境中平均成功率为81%，在不同的现实世界环境中为67%。这些结果为完全机载的视觉-语言-动作（VLA）飞行建立了新的基准，并证明紧凑高效的模型能够实现可靠的语言引导导航，而无需依赖外部基础设施。

## 🔬 方法详解

**问题定义**：论文旨在解决自主无人机在非结构化环境中理解和执行语言指令的挑战。现有方法通常依赖于手工技能和复杂的参数调优，导致效率低下和适应性差。

**核心思路**：GRaD-Nav++通过引入轻量级的视觉-语言-动作框架，结合可微强化学习，能够实时处理视觉和语言输入，从而实现高效的低级控制学习。

**技术框架**：该框架包括一个光照真实的3D高斯点云模拟器和一个专家混合（MoE）动作头。MoE结构能够根据任务需求自适应地分配计算资源，提高模型的泛化能力。

**关键创新**：最重要的创新在于引入了Mixture-of-Experts（MoE）机制，使得模型能够在不同任务间有效切换，减少遗忘现象，与传统方法相比显著提升了适应性和效率。

**关键设计**：在训练过程中，采用可微强化学习（DiffRL）策略，结合特定的损失函数和网络结构设计，以确保模型能够在多任务和多环境中保持高效的学习能力。

## 📊 实验亮点

在多任务泛化实验中，GRaD-Nav++在训练任务上取得了83%的成功率，在未见任务上为75%。在实际硬件上，训练任务成功率为67%，未见任务为50%。在多环境适应实验中，平均成功率为81%，展示了其在不同环境中的强大适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括无人机自动化、智能物流和搜索救援等场景。通过实现语言引导的自主导航，GRaD-Nav++能够显著提高无人机在复杂环境中的操作效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Autonomous drones capable of interpreting and executing high-level language instructions in unstructured environments remain a long-standing goal. Yet existing approaches are constrained by their dependence on hand-crafted skills, extensive parameter tuning, or computationally intensive models unsuitable for onboard use. We introduce GRaD-Nav++, a lightweight Vision-Language-Action (VLA) framework that runs fully onboard and follows natural-language commands in real time. Our policy is trained in a photorealistic 3D Gaussian Splatting (3DGS) simulator via Differentiable Reinforcement Learning (DiffRL), enabling efficient learning of low-level control from visual and linguistic inputs. At its core is a Mixture-of-Experts (MoE) action head, which adaptively routes computation to improve generalization while mitigating forgetting. In multi-task generalization experiments, GRaD-Nav++ achieves a success rate of 83% on trained tasks and 75% on unseen tasks in simulation. When deployed on real hardware, it attains 67% success on trained tasks and 50% on unseen ones. In multi-environment adaptation experiments, GRaD-Nav++ achieves an average success rate of 81% across diverse simulated environments and 67% across varied real-world settings. These results establish a new benchmark for fully onboard Vision-Language-Action (VLA) flight and demonstrate that compact, efficient models can enable reliable, language-guided navigation without relying on external infrastructure.

