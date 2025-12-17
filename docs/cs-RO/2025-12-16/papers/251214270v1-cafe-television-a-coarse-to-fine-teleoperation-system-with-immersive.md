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

**提出CaFe-TeleVision系统，通过粗到精控制与沉浸式可视化提升远程操作的效率和人机工程学**

**关键词**: `远程操作` `人机工程学` `粗到精控制` `沉浸式可视化` `机器人重定向` `双手操作` `人机交互` `协作机器人`

## 📋 核心要点

1. 现有远程操作系统在挑战性场景下效率与人机工程学表现不足，影响用户体验与任务性能。
2. 提出粗到精控制机制与沉浸式情境可视化，分别优化操作精度与视觉反馈，降低认知负荷。
3. 用户研究显示系统显著降低任务负荷、提升接受度，任务成功率最高提升28.89%，完成时间加速26.81%。

## 📝 摘要（中文）

远程操作为远程控制和机器人本体感知数据收集提供了有前景的范式。尽管近期有所进展，但现有系统在效率和人体工程学方面仍存在局限，尤其是在挑战性场景中。本文提出CaFe-TeleVision，一种具有沉浸式情境可视化的粗到精远程操作系统，以提升人体工程学。其核心在于重定向模块中提出的粗到精控制机制，以弥合工作空间差异，共同优化效率和物理人体工程学。为了提供具有足够视觉线索的沉浸式反馈以适配人类视觉系统，感知模块集成了按需情境可视化技术，降低了多视图处理的认知负荷。该系统基于人形协作机器人构建，并通过六项挑战性双手操作任务进行验证。对24名参与者的用户研究证实，CaFe-TeleVision在统计学上显著提升了人体工程学，表明在远程操作期间任务负荷更低、用户接受度更高。定量结果也验证了我们的系统在六项任务中的优越性能，成功率最高超出对比方法28.89%，完成时间加速26.81%。项目网页：https://clover-cuhk.github.io/cafe_television/

## 🔬 方法详解

CaFe-TeleVision系统整体框架包含重定向模块与感知模块。重定向模块采用粗到精控制机制，先进行粗略空间对齐，再精细调整机器人姿态，以解决操作者与机器人工作空间不匹配问题，同时优化效率与物理人机工程学。感知模块集成按需情境可视化技术，动态提供沉浸式视觉反馈，减少多视图处理的认知负担。关键创新在于将粗到精控制与沉浸式可视化结合，系统性地提升远程操作的整体性能。与现有方法相比，主要区别在于更注重人机交互的舒适性与效率平衡，而非单一追求控制精度或视觉逼真度。

## 📊 实验亮点

在六项挑战性双手操作任务中，系统成功率最高超出对比方法28.89%，完成时间加速26.81%；用户研究（24名参与者）显示任务负荷显著降低、用户接受度提升，统计学上证实了人机工程学的改进。

## 🎯 应用场景

该系统适用于远程机器人操作、危险环境作业（如核设施维护、太空探索）、医疗手术辅助及工业自动化等领域，能提升操作安全性、效率与用户体验，具有实际应用价值。

## 📄 摘要（原文）

> Teleoperation presents a promising paradigm for remote control and robot proprioceptive data collection. Despite recent progress, current teleoperation systems still suffer from limitations in efficiency and ergonomics, particularly in challenging scenarios. In this paper, we propose CaFe-TeleVision, a coarse-to-fine teleoperation system with immersive situated visualization for enhanced ergonomics. At its core, a coarse-to-fine control mechanism is proposed in the retargeting module to bridge workspace disparities, jointly optimizing efficiency and physical ergonomics. To stream immersive feedback with adequate visual cues for human vision systems, an on-demand situated visualization technique is integrated in the perception module, which reduces the cognitive load for multi-view processing. The system is built on a humanoid collaborative robot and validated with six challenging bimanual manipulation tasks. User study among 24 participants confirms that CaFe-TeleVision enhances ergonomics with statistical significance, indicating a lower task load and a higher user acceptance during teleoperation. Quantitative results also validate the superior performance of our system across six tasks, surpassing comparative methods by up to 28.89% in success rate and accelerating by 26.81% in completion time. Project webpage: https://clover-cuhk.github.io/cafe_television/

