---
layout: default
title: VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tunin
---

# VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tunin

**arXiv**: [2510.14930v1](https://arxiv.org/abs/2510.14930) | [PDF](https://arxiv.org/pdf/2510.14930.pdf)

**作者**: Binghao Huang, Jie Xu, Iretiayo Akinola, Wei Yang, Balakumar Sundaralingam, Rowland O'Flaherty, Dieter Fox, Xiaolong Wang, Arsalan Mousavian, Yu-Wei Chao, Yunzhu Li

---

## 💡 一句话要点

**提出VT-Refine框架，结合视觉触觉反馈与仿真微调，解决机器人双手装配任务**

**关键词**: `双手装配` `视觉触觉反馈` `扩散策略` `强化学习` `仿真到真实迁移` `触觉传感器`

## 📋 核心要点

1. 核心问题：仅靠行为克隆难以复制人类双手装配的触觉适应能力，因演示数据有限且次优。
2. 方法要点：使用扩散策略从真实演示学习，再通过仿真强化学习微调，提升鲁棒性和泛化。
3. 实验效果：在仿真和真实世界中提高装配性能，增加数据多样性和策略优化效果。

## 📄 摘要（原文）

> Humans excel at bimanual assembly tasks by adapting to rich tactile feedback
> -- a capability that remains difficult to replicate in robots through
> behavioral cloning alone, due to the suboptimality and limited diversity of
> human demonstrations. In this work, we present VT-Refine, a visuo-tactile
> policy learning framework that combines real-world demonstrations,
> high-fidelity tactile simulation, and reinforcement learning to tackle precise,
> contact-rich bimanual assembly. We begin by training a diffusion policy on a
> small set of demonstrations using synchronized visual and tactile inputs. This
> policy is then transferred to a simulated digital twin equipped with simulated
> tactile sensors and further refined via large-scale reinforcement learning to
> enhance robustness and generalization. To enable accurate sim-to-real transfer,
> we leverage high-resolution piezoresistive tactile sensors that provide normal
> force signals and can be realistically modeled in parallel using
> GPU-accelerated simulation. Experimental results show that VT-Refine improves
> assembly performance in both simulation and the real world by increasing data
> diversity and enabling more effective policy fine-tuning. Our project page is
> available at https://binghao-huang.github.io/vt_refine/.

