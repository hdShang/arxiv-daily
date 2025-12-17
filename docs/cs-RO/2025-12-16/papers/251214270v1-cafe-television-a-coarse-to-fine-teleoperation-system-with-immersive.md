---
layout: default
title: CaFe-TeleVision: A Coarse-to-Fine Teleoperation System with Immersive Situated Visualization for Enhanced Ergonomics
---

# CaFe-TeleVision: A Coarse-to-Fine Teleoperation System with Immersive Situated Visualization for Enhanced Ergonomics

**arXiv**: [2512.14270v1](https://arxiv.org/abs/2512.14270) | [PDF](https://arxiv.org/pdf/2512.14270.pdf)

**作者**: Zixin Tang, Yiming Chen, Quentin Rouxel, Dianxi Li, Shuang Wu, Fei Chen

**分类**: cs.RO

**发布日期**: 2025-12-16

**🔗 代码/项目**: [PROJECT_PAGE](https://clover-cuhk.github.io/cafe_television/)

---

## 💡 一句话要点

**提出CaFe-TeleVision系统，通过粗到精控制与沉浸式可视化提升远程操作的效率与人体工学性能。**

🎯 **匹配领域**: **人形机器人** **强化学习**

**关键词**: `远程操作` `人形机器人` `粗到精控制` `沉浸式可视化` `人体工学` `双手操作` `认知负荷` `工作空间映射`

## 📋 核心要点

1. 现有远程操作系统在挑战性场景下效率与人体工学性能不足，影响操作体验与任务成功率。
2. 提出粗到精控制机制优化工作空间映射，并集成沉浸式情境可视化以降低认知负荷。
3. 用户研究显示系统显著降低任务负荷、提升接受度，定量指标在成功率与完成时间上大幅领先。

## 📝 摘要（中文）

远程操作为远程控制和机器人本体感知数据收集提供了有前景的范式。尽管近期取得进展，当前远程操作系统在效率和人体工学方面仍存在局限，尤其在挑战性场景中。本文提出CaFe-TeleVision，一种具有沉浸式情境可视化功能的粗到精远程操作系统，旨在提升人体工学性能。其核心在于重定向模块中提出的粗到精控制机制，以弥合工作空间差异，共同优化效率和物理人体工学。为提供具有足够视觉线索的沉浸式反馈以适配人类视觉系统，感知模块集成了按需情境可视化技术，降低了多视图处理的认知负荷。该系统基于人形协作机器人构建，并通过六项挑战性双手操作任务进行验证。对24名参与者的用户研究证实，CaFe-TeleVision在统计学上显著提升了人体工学性能，表现为任务负荷更低、用户接受度更高。定量结果也验证了本系统在六项任务中的优越性能，成功率最高超出对比方法28.89%，完成时间加速26.81%。项目网页：https://clover-cuhk.github.io/cafe_television/

## 🔬 方法详解

CaFe-TeleVision系统整体框架包含重定向模块与感知模块。核心创新在于：1) 重定向模块采用粗到精控制机制，通过分层策略（如先粗略定位后精细调整）解决操作者与机器人工作空间不匹配问题，兼顾效率与物理人体工学；2) 感知模块集成按需情境可视化技术，动态提供沉浸式视觉反馈（如关键视角或深度信息），减少多视图处理的认知负担。与现有方法相比，本系统将控制优化与视觉增强紧密结合，而非孤立处理，从而更全面地提升远程操作性能。

## 📊 实验亮点

在六项挑战性双手操作任务中，CaFe-TeleVision相比对比方法，成功率最高提升28.89%，完成时间加速26.81%；用户研究（24名参与者）显示任务负荷显著降低、用户接受度提高，统计学上证实了人体工学性能的增强。

## 🎯 应用场景

该系统可应用于远程机器人操作领域，如危险环境作业（核设施维护、灾难救援）、医疗手术辅助、工业制造中的精密装配，以及机器人数据收集与训练，具有提升操作安全性、精度与效率的实际价值。

## 📄 摘要（原文）

> Teleoperation presents a promising paradigm for remote control and robot proprioceptive data collection. Despite recent progress, current teleoperation systems still suffer from limitations in efficiency and ergonomics, particularly in challenging scenarios. In this paper, we propose CaFe-TeleVision, a coarse-to-fine teleoperation system with immersive situated visualization for enhanced ergonomics. At its core, a coarse-to-fine control mechanism is proposed in the retargeting module to bridge workspace disparities, jointly optimizing efficiency and physical ergonomics. To stream immersive feedback with adequate visual cues for human vision systems, an on-demand situated visualization technique is integrated in the perception module, which reduces the cognitive load for multi-view processing. The system is built on a humanoid collaborative robot and validated with six challenging bimanual manipulation tasks. User study among 24 participants confirms that CaFe-TeleVision enhances ergonomics with statistical significance, indicating a lower task load and a higher user acceptance during teleoperation. Quantitative results also validate the superior performance of our system across six tasks, surpassing comparative methods by up to 28.89% in success rate and accelerating by 26.81% in completion time. Project webpage: https://clover-cuhk.github.io/cafe_television/

