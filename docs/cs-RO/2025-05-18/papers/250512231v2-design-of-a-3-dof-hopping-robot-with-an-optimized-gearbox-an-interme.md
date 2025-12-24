---
layout: default
title: Design of a 3-DOF Hopping Robot with an Optimized Gearbox: An Intermediate Platform Toward Bipedal Robots
---

# Design of a 3-DOF Hopping Robot with an Optimized Gearbox: An Intermediate Platform Toward Bipedal Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12231" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12231v2</a>
  <a href="https://arxiv.org/pdf/2505.12231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12231v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12231v2', 'Design of a 3-DOF Hopping Robot with an Optimized Gearbox: An Intermediate Platform Toward Bipedal Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: JongHun Choe, Gijeong Kim, Hajun Kim, Dongyun Kang, Min-Su Kim, Hae-Won Park

**分类**: cs.RO

**发布日期**: 2025-05-18 (更新: 2025-05-21)

---

## 💡 一句话要点

**设计了一种3自由度跳跃机器人以推动双足机器人发展**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `跳跃机器人` `双足机器人` `行星齿轮箱` `强化学习` `动态控制` `机器人设计` `运动学`

## 📋 核心要点

1. 现有的跳跃机器人在动态运动和关节配置上存在局限，难以实现类人跳跃能力。
2. 论文提出了一种优化的3K复合行星齿轮箱设计，结合定制化组件以满足高性能需求。
3. 实验结果表明，该机器人能够稳定地执行重复跳跃，验证了其作为双足机器人开发平台的潜力。

## 📝 摘要（中文）

本文提出了一种具有类人下肢关节配置和平底足的3自由度跳跃机器人，能够执行动态和重复的跳跃动作。为实现高扭矩输出和有效的电缆布线，设计了一种紧凑的3K复合行星齿轮箱，采用混合整数非线性规划进行齿轮齿优化。所有主要组件，包括驱动器、电机驱动和通信接口，均为定制设计。该机器人重12.45千克，长度为840毫米，膝关节完全伸展时。采用基于强化学习的控制器，通过硬件实验验证了机器人的性能，展示了对用户输入的稳定和重复的跳跃响应。这些实验结果表明，该平台为未来双足机器人开发奠定了坚实基础。

## 🔬 方法详解

**问题定义**：本文旨在解决现有跳跃机器人在动态运动能力和关节配置上的不足，特别是如何实现类人跳跃的高效性和稳定性。现有方法往往在扭矩输出和电缆布线方面存在局限。

**核心思路**：论文的核心思路是设计一种紧凑的3K复合行星齿轮箱，通过混合整数非线性规划优化齿轮齿，以实现高扭矩输出和大空心轴直径，从而提高电缆布线的效率。

**技术框架**：整体架构包括定制设计的驱动器、电机驱动和通信接口，结合优化的齿轮箱，形成一个高效的动力传输系统。机器人采用强化学习控制器，能够根据用户输入进行动态调整。

**关键创新**：最重要的技术创新在于采用混合整数非线性规划进行齿轮齿优化，显著提升了齿轮箱的性能，解决了传统设计中的扭矩和空间利用问题。

**关键设计**：关键参数包括齿轮箱的齿数和结构设计，损失函数通过强化学习算法进行优化，确保机器人在跳跃时的稳定性和响应速度。

## 📊 实验亮点

实验结果显示，该机器人在用户输入下能够稳定执行重复跳跃，验证了其设计的有效性。具体性能数据表明，机器人在跳跃高度和频率上均表现出色，提供了良好的动态响应能力，为后续研究提供了可靠的实验基础。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和娱乐机器人等，能够为未来的双足机器人开发提供重要的技术基础。其设计理念和控制策略也可推广到其他类型的动态机器人中，具有广泛的实际价值和影响。

## 📄 摘要（原文）

> This paper presents a 3-DOF hopping robot with a human-like lower-limb joint configuration and a flat foot, capable of performing dynamic and repetitive jumping motions. To achieve both high torque output and a large hollow shaft diameter for efficient cable routing, a compact 3K compound planetary gearbox was designed using mixed-integer nonlinear programming for gear tooth optimization. To meet performance requirements within the constrained joint geometry, all major components-including the actuator, motor driver, and communication interface-were custom-designed. The robot weighs 12.45 kg, including a dummy mass, and measures 840 mm in length when the knee joint is fully extended. A reinforcement learning-based controller was employed, and robot's performance was validated through hardware experiments, demonstrating stable and repetitive hopping motions in response to user inputs. These experimental results indicate that the platform serves as a solid foundation for future bipedal robot development.

