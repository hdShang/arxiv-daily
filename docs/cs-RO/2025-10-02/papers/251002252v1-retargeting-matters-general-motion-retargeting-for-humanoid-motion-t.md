---
layout: default
title: Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking
---

# Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02252" target="_blank" class="toolbar-btn">arXiv: 2510.02252v1</a>
    <a href="https://arxiv.org/pdf/2510.02252.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02252v1" 
            onclick="toggleFavorite(this, '2510.02252v1', 'Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Joao Pedro Araujo, Yanjie Ze, Pei Xu, Jiajun Wu, C. Karen Liu

**分类**: cs.RO

**发布日期**: 2025-10-02

**🔗 代码/项目**: [GITHUB](https://github.com/YanjieZe/GMR) | [PROJECT_PAGE](https://jaraujo98.github.io/retargeting_matters)

---

## 💡 一句话要点

**提出通用运动重定向(GMR)方法，提升人型机器人运动跟踪策略的鲁棒性和真实性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱七：动作重定向 (Motion Retargeting)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `运动重定向` `人型机器人` `运动跟踪` `强化学习` `运动控制`

## 📋 核心要点

1. 现有运动重定向方法在人型机器人运动跟踪中存在伪影，导致策略鲁棒性下降，需要大量奖励工程。
2. 提出通用运动重定向(GMR)方法，旨在减少重定向伪影，提高运动跟踪策略的性能和真实性。
3. 实验表明，GMR在跟踪性能和运动保真度上优于现有开源方法，接近闭源数据集的性能。

## 📝 摘要（中文）

人型机器人运动跟踪策略对于构建遥操作流程和分层控制器至关重要，但它们面临着人与机器人之间形态差异的根本挑战。现有方法通过将人类运动数据重定向到人型机器人身上，然后训练强化学习(RL)策略来模仿这些参考轨迹来解决这一问题。然而，重定向过程中引入的伪影，如脚部滑动、自穿透和物理上不可行的运动，通常会留在参考轨迹中，让RL策略来纠正。虽然之前的工作已经展示了运动跟踪能力，但它们通常需要大量的奖励工程和领域随机化才能成功。本文系统地评估了在抑制过度奖励调整的情况下，重定向质量如何影响策略性能。为了解决现有重定向方法中发现的问题，我们提出了一种新的重定向方法，即通用运动重定向(GMR)。我们与两个开源重定向器PHC和ProtoMotions，以及来自宇树科技的高质量闭源数据集一起评估GMR。使用BeyondMimic进行策略训练，我们隔离了重定向效果，而无需奖励调整。我们在LAFAN1数据集的一个多样化子集上的实验表明，虽然大多数运动都可以被跟踪，但重定向数据中的伪影会显著降低策略的鲁棒性，特别是对于动态或长序列。GMR在跟踪性能和对源运动的忠实度方面始终优于现有的开源方法，实现了接近闭源基线的感知保真度和策略成功率。

## 🔬 方法详解

**问题定义**：论文旨在解决人型机器人运动跟踪中，由于人类运动数据重定向到机器人时产生的伪影（如脚部滑动、自穿透等）导致强化学习策略训练困难，鲁棒性差的问题。现有方法通常依赖大量的奖励函数调整和领域随机化来克服这些伪影，但效率低且泛化能力受限。

**核心思路**：论文的核心思路是通过改进运动重定向算法，从源头上减少伪影的产生，从而降低强化学习策略训练的难度，提高策略的鲁棒性和真实性。GMR方法旨在生成更干净、更符合物理规律的参考轨迹，使强化学习策略更容易学习和模仿。

**技术框架**：GMR方法的整体框架包括以下几个主要阶段：1) 运动数据预处理：对原始人类运动数据进行清洗和标准化。2) 运动重定向：使用GMR算法将人类运动数据映射到人型机器人身上。3) 轨迹优化：对重定向后的轨迹进行优化，减少伪影并提高物理可行性。4) 强化学习策略训练：使用优化后的轨迹作为参考，训练人型机器人的运动跟踪策略。

**关键创新**：GMR方法的关键创新在于其运动重定向算法。与现有方法相比，GMR更加注重保持运动的自然性和物理可行性，通过引入更精细的约束条件和优化目标，减少了伪影的产生。此外，GMR还考虑了不同人型机器人的形态差异，能够更好地适应不同的机器人模型。

**关键设计**：GMR的关键设计包括：1) 基于优化的重定向方法，使用目标函数来最小化源运动和目标运动之间的差异，同时施加约束以避免自穿透和关节限制。2) 使用了加权最小二乘法来解决优化问题，允许对不同的约束条件进行优先级排序。3) 引入了基于物理的约束，例如地面接触约束和重心平衡约束，以确保重定向后的运动是物理上可行的。4) 针对不同的人型机器人，GMR允许调整骨骼比例和关节限制，以更好地适应机器人的形态。

## 📊 实验亮点

实验结果表明，GMR方法在运动跟踪性能和运动保真度方面均优于现有的开源方法PHC和ProtoMotions，并且能够达到接近闭源数据集的性能水平。具体来说，GMR在LAFAN1数据集上的策略成功率显著高于其他开源方法，并且能够生成更自然、更符合物理规律的运动轨迹。在感知保真度方面，GMR也取得了显著的提升。

## 🎯 应用场景

该研究成果可应用于人型机器人的遥操作、运动控制和仿真等领域。通过提高运动跟踪策略的鲁棒性和真实性，可以使人型机器人更好地执行复杂的任务，例如在危险环境中进行救援、在家庭中提供服务等。此外，该方法还可以用于生成逼真的人型机器人动画，应用于游戏和电影等娱乐产业。

## 📄 摘要（原文）

> Humanoid motion tracking policies are central to building teleoperation pipelines and hierarchical controllers, yet they face a fundamental challenge: the embodiment gap between humans and humanoid robots. Current approaches address this gap by retargeting human motion data to humanoid embodiments and then training reinforcement learning (RL) policies to imitate these reference trajectories. However, artifacts introduced during retargeting, such as foot sliding, self-penetration, and physically infeasible motion are often left in the reference trajectories for the RL policy to correct. While prior work has demonstrated motion tracking abilities, they often require extensive reward engineering and domain randomization to succeed. In this paper, we systematically evaluate how retargeting quality affects policy performance when excessive reward tuning is suppressed. To address issues that we identify with existing retargeting methods, we propose a new retargeting method, General Motion Retargeting (GMR). We evaluate GMR alongside two open-source retargeters, PHC and ProtoMotions, as well as with a high-quality closed-source dataset from Unitree. Using BeyondMimic for policy training, we isolate retargeting effects without reward tuning. Our experiments on a diverse subset of the LAFAN1 dataset reveal that while most motions can be tracked, artifacts in retargeted data significantly reduce policy robustness, particularly for dynamic or long sequences. GMR consistently outperforms existing open-source methods in both tracking performance and faithfulness to the source motion, achieving perceptual fidelity and policy success rates close to the closed-source baseline. Website: https://jaraujo98.github.io/retargeting_matters. Code: https://github.com/YanjieZe/GMR.

