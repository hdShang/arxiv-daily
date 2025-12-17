---
layout: default
title: $\mathbf{M^3A}$ Policy: Mutable Material Manipulation Augmentation Policy through Photometric Re-rendering
---

# $\mathbf{M^3A}$ Policy: Mutable Material Manipulation Augmentation Policy through Photometric Re-rendering

**arXiv**: [2512.01446v1](https://arxiv.org/abs/2512.01446) | [PDF](https://arxiv.org/pdf/2512.01446.pdf)

**作者**: Jiayi Li, Yuxuan Hu, Haoran Geng, Xiangyu Chen, Chuhao Zhou, Ziteng Cui, Jianfei Yang

---

## 💡 一句话要点

**提出M^3A策略，通过光度重渲染增强材料泛化能力，解决机器人操作中材料多样性挑战。**

**关键词**: `材料泛化` `光度重渲染` `机器人操作` `数据增强` `跨材料基准` `光传输`

## 📋 核心要点

1. 核心问题：机器人操作需处理玻璃、金属等材料，其透明或反射表面导致视觉分布外变化，现有方法受限于模拟-真实域差距或数据收集成本。
2. 方法要点：基于单次真实演示，利用光传输物理特性进行光度重渲染，生成多样化材料属性的逼真演示，解耦任务技能与表面外观。
3. 实验或效果：构建首个多材料操作基准，实验显示M^3A策略提升跨材料泛化，真实任务平均成功率提高58.03%，对未见材料表现稳健。

## 📄 摘要（原文）

> Material generalization is essential for real-world robotic manipulation, where robots must interact with objects exhibiting diverse visual and physical properties. This challenge is particularly pronounced for objects made of glass, metal, or other materials whose transparent or reflective surfaces introduce severe out-of-distribution variations. Existing approaches either rely on simulated materials in simulators and perform sim-to-real transfer, which is hindered by substantial visual domain gaps, or depend on collecting extensive real-world demonstrations, which is costly, time-consuming, and still insufficient to cover various materials. To overcome these limitations, we resort to computational photography and introduce Mutable Material Manipulation Augmentation (M$^3$A), a unified framework that leverages the physical characteristics of materials as captured by light transport for photometric re-rendering. The core idea is simple yet powerful: given a single real-world demonstration, we photometrically re-render the scene to generate a diverse set of highly realistic demonstrations with different material properties. This augmentation effectively decouples task-specific manipulation skills from surface appearance, enabling policies to generalize across materials without additional data collection. To systematically evaluate this capability, we construct the first comprehensive multi-material manipulation benchmark spanning both simulation and real-world environments. Extensive experiments show that the M$^3$A policy significantly enhances cross-material generalization, improving the average success rate across three real-world tasks by 58.03\%, and demonstrating robust performance on previously unseen materials.

