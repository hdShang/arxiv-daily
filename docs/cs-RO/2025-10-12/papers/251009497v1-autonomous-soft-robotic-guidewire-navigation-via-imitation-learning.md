---
layout: default
title: Autonomous Soft Robotic Guidewire Navigation via Imitation Learning
---

# Autonomous Soft Robotic Guidewire Navigation via Imitation Learning

**arXiv**: [2510.09497v1](https://arxiv.org/abs/2510.09497) | [PDF](https://arxiv.org/pdf/2510.09497.pdf)

**作者**: Noah Barnes, Ji Woong Kim, Lingyun Di, Hannah Qu, Anuruddha Bhattacharjee, Miroslaw Janowski, Dheeraj Gandhi, Bailey Felix, Shaopeng Jiang, Olivia Young, Mark Fuge, Ryan D. Sochol, Jeremy D. Brown, Axel Krieger

---

## 💡 一句话要点

**提出基于Transformer的模仿学习框架，实现软体机器人导丝在血管瘤导航中的自主控制。**

**关键词**: `软体机器人导航` `模仿学习` `Transformer模型` `血管内手术` `自主控制`

## 📋 核心要点

1. 核心问题：软体机器人导丝在血管内导航中建模与控制困难，影响精度与安全。
2. 方法要点：采用目标条件、相对动作输出和自动造影剂注射的Transformer模仿学习框架。
3. 实验或效果：在未见血管几何上，模型导航成功率83%，优于多个基线方法。

## 📄 摘要（原文）

> In endovascular surgery, endovascular interventionists push a thin tube
> called a catheter, guided by a thin wire to a treatment site inside the
> patient's blood vessels to treat various conditions such as blood clots,
> aneurysms, and malformations. Guidewires with robotic tips can enhance
> maneuverability, but they present challenges in modeling and control.
> Automation of soft robotic guidewire navigation has the potential to overcome
> these challenges, increasing the precision and safety of endovascular
> navigation. In other surgical domains, end-to-end imitation learning has shown
> promising results. Thus, we develop a transformer-based imitation learning
> framework with goal conditioning, relative action outputs, and automatic
> contrast dye injections to enable generalizable soft robotic guidewire
> navigation in an aneurysm targeting task. We train the model on 36 different
> modular bifurcated geometries, generating 647 total demonstrations under
> simulated fluoroscopy, and evaluate it on three previously unseen vascular
> geometries. The model can autonomously drive the tip of the robot to the
> aneurysm location with a success rate of 83% on the unseen geometries,
> outperforming several baselines. In addition, we present ablation and baseline
> studies to evaluate the effectiveness of each design and data collection
> choice. Project website: https://softrobotnavigation.github.io/

